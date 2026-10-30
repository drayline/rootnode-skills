#!/usr/bin/env python3
"""d9a_runner.py - D9a behavioral comparison of rootnode-cc-design v4.2 vs v5.0.

Runs every Claude Code call itself, so the orchestrating session reads only the
small summary files. Each arm is a `claude -p` child process in its own folder
outside the repo, with that arm's Skill installed at project level and
`--setting-sources project,local`, which keeps the account-synced copy out of
the run (verified on Claude Code 2.1.312). Every run's own init event is checked
for isolation and model, so the evidence is per run, not per session.

Usage:  python d9a_runner.py all --repo <repo root> --out <artifact dir>
Phases: setup, probe, arms, grade, exec, score (all = in order; each is resumable).
Exit codes: 0 ok; 10 setup gate; 11 isolation gate; 12 model gate; 13 missing tool;
14 child-process cap reached.
"""
import argparse, hashlib, io, json, random, re, shutil, subprocess, sys, tempfile, time, urllib.request, zipfile
from pathlib import Path

REPO_SLUG = "drayline/rootnode-skills"
ARMS = {  # tag, SKILL.md LF-sha256, file count - verified 2026-10-29 against the tags and release zips
    "v4.2": ("rootnode-cc-design/v4.2", "4a85a0468dbf106b63206aa65c371ab82a41751bbf056a3ac8da99dccbfce397", 13),
    "v5.0": ("rootnode-cc-design/v5.0", "02ac690c1275953b9314927121e17c4768fc1c49b69f7ab181a5188fe2011345", 14),
}
MODEL, PROBE_MODEL = "claude-opus-5-5", "claude-haiku-5-5"
ISOLATE = ["--setting-sources", "project,local"]
CAP = 40  # hard cap on claude child processes per invocation of this script
SUFFIX = ("\n\nUse the rootnode-cc-design Skill for this. Return the complete deliverable in your "
          "reply as Markdown. Do not create or edit files.")
CASES = {
    "C1": ("Design a PreToolUse hook for a Claude Code project that blocks any write to files under "
           "`migrations/`. Give the complete `.claude/settings.json` hook entry and the complete hook script. "
           "The team runs Claude Code on Windows with Git Bash and on Linux CI.",
           ["The hook blocks by exiting with code 2, or by exiting 0 with JSON whose decision is block. A hook that signals the block with exit code 1 fails.",
            "The settings entry uses a \"matcher\" key whose value is a string, not a \"matchers\" array.",
            "The settings entry nests the command in a \"hooks\" array of objects that carry \"type\": \"command\".",
            "The block message tells the agent what to do next, not only that the write was refused.",
            "The design gives an off-switch: an environment variable or setting that disables the hook without deleting it."]),
    "C2": ("Write a session prompt for an unattended three-phase database migration run in Claude Code: phase 1 "
           "generates migration files, phase 2 runs them against a staging database, phase 3 updates the ORM models. "
           "Nobody watches the run; it runs overnight. The repo keeps its audit outputs in `reports/`.",
           ["The prompt has an early-stop countermeasure: it tells the agent to keep working until the work is done and to stop only at named gates or risky steps.",
            "The prompt authorizes writing a session report and makes writing it the final item.",
            "The report path is in the repo's audit folder `reports/`.",
            "At least one halt or gate binds to the end state (a digest or a checked post-action state), not only to starting conditions.",
            "Each halt names an exact continuation phrase for resuming."]),
    "C3": ("Add a verification iron-law Stop hook to a Claude Code project: the agent must not end its turn while "
           "the test suite (`npm test`) is failing. Give the hook configuration and the complete script.",
           ["The script reads stop_hook_active from the hook input and allows the stop when it is true.",
            "The design caps repeated blocking: after a no-progress or attempt limit, the hook releases the stop.",
            "The block reason names the evidence (the failing command or its output), not only a generic message."]),
    "C4": ("Design a Builder-to-Refuter loop for a TypeScript monorepo (pnpm, tests via `pnpm test`) where Claude Code "
           "implements feature specs from `specs/*.md`. Give the role table, the delegation briefs, and the loop rules.",
           ["The delegation brief has ten fields, including a bound spec or diff digest and a rule that the brief does not dictate the verdict.",
            "The loop is capped at two Builder-to-Refuter cycles before an operator gate.",
            "The Refuter's return contract has a blocked outcome that is distinct from an empty findings list.",
            "Each Builder or Refuter return opens with an identity line naming the role and the SHA or digest it worked against.",
            "A Refuter approval binds to the reviewed diff, and any later write to a reviewed file re-opens review.",
            "A scout or search role is named on Haiku 5.5."]),
    "C5": ("We hit friction in our Claude Code project: after the Refuter approves a change, the Builder agent keeps "
           "editing the same files, so what lands is not what was reviewed. Evolve our setup to fix this.",
           ["The response routes the correction to one home (a rule, a deterministic check, or discard) and says which.",
            "It proposes an enforced mechanism (a hook or scripted check) that blocks or detects writes to reviewed files after approval, not only a prose rule.",
            "The mechanism decides by evidence, comparing the current file or diff against the reviewed digest, not by the agent's own claim."]),
    "C6": ("Which model, and at what effort, should the Refuter role use in our Claude Code Builder-to-Refuter loop?",
           ["It recommends Opus 5.5 or a more capable model for the Refuter.",
            "It states that the reviewer must be at least as capable as the builder.",
            "It gives an effort recommendation.",
            "It marks the model recommendation as dated or time-sensitive (a date or a landscape marker)."]),
}
# Spec section 11 predicted these v4.2 failures; report-only.
PREDICTED_V42_FAIL = {"C1": ["A1", "A2"], "C2": ["A1", "A2"], "C3": ["A2"], "C4": ["A1", "A2", "A6"], "C5": ["A2"], "C6": ["A1"]}
FORBIDDEN = re.compile(r"\brm\s|\bcurl\b|\bwget\b|\bgit\s|\bsudo\b|Invoke-|Remove-Item|\b(npm|pnpm|yarn)\s+(i|add|install)\b")

spawned = 0

def lf_sha(b):
    return hashlib.sha256(b.replace(b"\r", b"")).hexdigest()

def tool(name):
    p = shutil.which(name)
    if not p:
        print(f"HALT 13: `{name}` not found on PATH"); sys.exit(13)
    return p

def wjson(p, obj):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, indent=2), encoding="utf-8")

def rjson(p):
    return json.loads(p.read_text(encoding="utf-8"))

def run_claude(cwd, prompt, model, tools, timeout):
    """One claude -p child. Prompt goes on stdin: --tools is variadic and would swallow a positional prompt."""
    global spawned
    if spawned >= CAP:
        print(f"HALT 14: child-process cap {CAP} reached"); sys.exit(14)
    spawned += 1
    cmd = [tool("claude"), "-p", "--model", model, "--output-format", "stream-json", "--verbose",
           *ISOLATE, "--tools", tools]
    t0 = time.time()
    try:
        cp = subprocess.run(cmd, cwd=str(cwd), input=prompt.encode("utf-8"), capture_output=True, timeout=timeout)
        raw, err, code = cp.stdout.decode("utf-8", "replace"), cp.stderr.decode("utf-8", "replace"), cp.returncode
    except subprocess.TimeoutExpired:
        raw, err, code = "", f"timeout after {timeout}s", -1
    ev = {"init": {}, "result": {}, "skill_calls": [], "raw": raw, "stderr": err[:500], "exit": code,
          "seconds": round(time.time() - t0)}
    for line in raw.splitlines():
        try:
            e = json.loads(line)
        except ValueError:
            continue
        if e.get("type") == "system" and e.get("subtype") == "init":
            ev["init"] = e
        elif e.get("type") == "result":
            ev["result"] = e
        content = (e.get("message") or {}).get("content")
        if isinstance(content, list):
            for c in content:
                if isinstance(c, dict) and c.get("type") == "tool_use" and c.get("name") == "Skill":
                    ev["skill_calls"].append((c.get("input") or {}).get("skill"))
    return ev

def cc_skills(ev):
    return sorted(s for s in ev["init"].get("skills", []) if "cc-design" in str(s))

WORK = Path.home() / "d9a-cc-design-v5.0"

def work_dir():
    return WORK

def find_bash():
    """Git Bash on Windows; System32\\bash.exe is the WSL launcher and runs in another filesystem."""
    if sys.platform == "win32":
        g = Path(tool("git")).resolve().parents[1] / "bin" / "bash.exe"
        return str(g) if g.exists() else None
    return shutil.which("bash")

# ---------------- phases ----------------

def setup(a):
    git, w, rec = tool("git"), work_dir(), {}
    for arm, (tag, want_sha, want_n) in ARMS.items():
        if a.zips:
            data = (Path(a.zips) / arm / "rootnode-cc-design-cc.zip").read_bytes()
        else:
            url = f"https://github.com/{REPO_SLUG}/releases/download/{tag}/rootnode-cc-design-cc.zip"
            data = urllib.request.urlopen(url, timeout=120).read()
        dest = w / f"arm-{arm}" / ".claude" / "skills"
        if dest.exists():
            shutil.rmtree(dest)
        dest.mkdir(parents=True)
        zipfile.ZipFile(io.BytesIO(data)).extractall(dest)
        got = {str(p.relative_to(dest)).replace("\\", "/"): lf_sha(p.read_bytes()) for p in dest.rglob("*") if p.is_file()}
        names = subprocess.run([git, "-C", a.repo, "ls-tree", "-r", "--name-only", tag, "rootnode-cc-design/"],
                               capture_output=True, text=True).stdout.split()
        mism = [n for n in names if got.pop(n, None) != lf_sha(subprocess.run([git, "-C", a.repo, "show", f"{tag}:{n}"], capture_output=True).stdout)]
        skill_sha = lf_sha((dest / "rootnode-cc-design" / "SKILL.md").read_bytes())
        ok = not mism and not got and len(names) == want_n and skill_sha == want_sha
        rec[arm] = {"tag": tag, "zip_sha256": hashlib.sha256(data).hexdigest(), "files": len(names),
                    "mismatched": mism, "extra_in_zip": sorted(got), "skill_md_lf_sha256": skill_sha,
                    "expected": want_sha, "gate": "PASS" if ok else "FAIL"}
    (w / "grader").mkdir(parents=True, exist_ok=True)
    wjson(Path(a.out) / "setup.json", rec)
    print(json.dumps({k: v["gate"] for k, v in rec.items()}))
    if any(v["gate"] != "PASS" for v in rec.values()):
        print("HALT 10: arm source does not match its tag or expected digest"); sys.exit(10)

def probe(a):
    w, q = work_dir(), "Reply OK."  # the gate reads the harness init event, not the reply
    rec, fail = {}, []
    for name, expect in (("arm-v4.2", ["rootnode-cc-design"]), ("arm-v5.0", ["rootnode-cc-design"]), ("grader", [])):
        ev = run_claude(w / name, q, a.probe_model, "", 180)
        got = cc_skills(ev)
        rec[name] = {"init_cc_skills": got, "reply": str(ev["result"].get("result", ""))[:200],
                     "claude_code_version": ev["init"].get("claude_code_version"), "exit": ev["exit"], "stderr": ev["stderr"][:300],
                     "gate": "PASS" if got == expect and ev["init"] else "FAIL"}
        if rec[name]["gate"] != "PASS":
            fail.append(name)
    wjson(Path(a.out) / "probe.json", rec)
    print(json.dumps({k: (v["gate"], v["init_cc_skills"]) for k, v in rec.items()}))
    if fail:
        print(f"HALT 11: isolation failed for {fail}"); sys.exit(11)

def arms(a):
    out = Path(a.out) / "runs"
    for i, case in enumerate(a.cases):
        order = ["v4.2", "v5.0"] if i % 2 == 0 else ["v5.0", "v4.2"]
        for arm in order:
            meta_p = out / arm / f"{case}.json"
            if meta_p.exists() and rjson(meta_p).get("status") == "VALID":
                continue
            for attempt in (1, 2):
                ev = run_claude(work_dir() / f"arm-{arm}", CASES[case][0] + SUFFIX, a.model, "Skill,Read", 1500)
                model = ev["init"].get("model")
                reasons = []
                if cc_skills(ev) != ["rootnode-cc-design"]:
                    reasons.append(f"isolation {cc_skills(ev)}")
                if not (model or "").startswith(a.model):
                    reasons.append(f"model {model}")
                if "rootnode-cc-design" not in ev["skill_calls"]:
                    reasons.append(f"skill not invoked {ev['skill_calls']}")
                if ev["result"].get("is_error") or not ev["result"].get("result"):
                    reasons.append(f"no result (exit {ev['exit']}: {ev['stderr'][:120]})")
                (out / arm).mkdir(parents=True, exist_ok=True)
                (out / arm / f"{case}.jsonl").write_text(ev["raw"], encoding="utf-8")
                (out / arm / f"{case}.md").write_text(str(ev["result"].get("result", "")), encoding="utf-8")
                meta = {"status": "VALID" if not reasons else "INVALID", "reasons": reasons, "attempt": attempt,
                        "model": model, "model_usage": list((ev["result"].get("modelUsage") or {}).keys()),
                        "num_turns": ev["result"].get("num_turns"), "seconds": ev["seconds"],
                        "skill_calls": ev["skill_calls"]}
                wjson(meta_p, meta)
                print(f"{case} {arm} attempt {attempt}: {meta['status']} {reasons}")
                if any(r.startswith("model") for r in reasons):
                    print("HALT 12: run model differs from the pinned model"); sys.exit(12)
                if not reasons:
                    break

def grader_prompt(case, x_text, y_text):
    req, asserts = CASES[case]
    lines = "\n".join(f"A{i}: {t}" for i, t in enumerate(asserts, 1))
    return (
        "You grade two anonymous responses, X and Y, to the same request, against binary assertions.\n"
        "Judge each response on its own text. Pass an assertion only when the response itself contains the "
        "required element; quote up to 200 characters from that response as evidence. When the element is absent, "
        "set pass to false and evidence to \"absent\". Do not reward length or style.\n\n"
        f"Request:\n{req}\n\nAssertions:\n{lines}\n\n"
        "Return only JSON, no prose and no code fence, in this shape:\n"
        '{"case": "' + case + '", "results": [{"id": "A1", "X": {"pass": true, "evidence": "..."}, '
        '"Y": {"pass": false, "evidence": "absent"}}], "notes": "<=300 characters"}\n'
        "Include every assertion id once.\n\n"
        f"<response_X>\n{x_text}\n</response_X>\n\n<response_Y>\n{y_text}\n</response_Y>\n")

def parse_grade(text, case):
    t = re.sub(r"^```(?:json)?\s*|\s*```$", "", text.strip())
    g = json.loads(t)
    ids = [r["id"] for r in g["results"]]
    want = [f"A{i}" for i in range(1, len(CASES[case][1]) + 1)]
    assert sorted(ids) == sorted(want), f"ids {ids}"
    for r in g["results"]:
        for s in ("X", "Y"):
            assert isinstance(r[s]["pass"], bool) and isinstance(r[s]["evidence"], str)
            assert not (r[s]["pass"] and r[s]["evidence"].strip().lower() == "absent"), "pass without evidence"
    return g

def grade(a):
    out, rng = Path(a.out), random.SystemRandom()
    for case in a.cases:
        gp = out / "grading" / f"{case}.json"
        if gp.exists() and rjson(gp).get("status") == "GRADED":
            continue
        metas = {arm: (out / "runs" / arm / f"{case}.json") for arm in ARMS}
        if not all(m.exists() and rjson(m)["status"] == "VALID" for m in metas.values()):
            wjson(gp, {"status": "NOT_GRADED", "reason": "an arm run is not VALID"}); continue
        x_arm = rng.choice(list(ARMS))
        key = {"X": x_arm, "Y": next(k for k in ARMS if k != x_arm)}
        texts = {lbl: (out / "runs" / arm / f"{case}.md").read_text(encoding="utf-8") for lbl, arm in key.items()}
        rec = {"status": "NOT_GRADED", "key": key}
        for attempt in (1, 2):
            ev = run_claude(work_dir() / "grader", grader_prompt(case, texts["X"], texts["Y"]), a.grader_model, "", 900)
            rec.update({"attempt": attempt, "grader_model": ev["init"].get("model"),
                        "grader_cc_skills": cc_skills(ev), "raw": str(ev["result"].get("result", ""))})
            try:
                if cc_skills(ev):
                    raise AssertionError(f"grader saw {cc_skills(ev)}")
                rec["grade"] = parse_grade(rec["raw"], case)
                rec["status"] = "GRADED"; break
            except Exception as e:  # malformed grader output: retry once, then record
                rec["error"] = str(e)[:200]
        wjson(gp, rec)
        print(f"{case}: {rec['status']}")

def extract_script(md, need):
    for lang, body in re.findall(r"```([\w-]*)\n(.*?)```", md, re.S):
        if lang.lower() in ("bash", "sh", "shell", "") and "exit" in body and need in body and not body.lstrip().startswith("{"):
            return body
    return None

def exec_hooks(a):
    out, bash, jq = Path(a.out), find_bash(), shutil.which("jq")
    fixtures = {
        "C1": [("write migrations/", {"hook_event_name": "PreToolUse", "tool_name": "Write",
                                      "tool_input": {"file_path": "migrations/001_init.sql", "content": "x"}}, 2),
               ("write src/", {"hook_event_name": "PreToolUse", "tool_name": "Write",
                               "tool_input": {"file_path": "src/app.py", "content": "x"}}, 0)],
        "C3": [("stop_hook_active true", {"hook_event_name": "Stop", "stop_hook_active": True}, 0)],
    }
    rec = {}
    for case, fx in fixtures.items():
        for arm in ARMS:
            key = f"{case}/{arm}"
            mdp = out / "runs" / arm / f"{case}.md"
            script = extract_script(mdp.read_text(encoding="utf-8"), "migrations" if case == "C1" else "stop_hook_active") if mdp.exists() else None
            if not bash or script is None:
                rec[key] = {"result": "NOT_RUN", "why": "no bash" if not bash else "no extractable bash script"}; continue
            if FORBIDDEN.search(script):
                rec[key] = {"result": "NOT_RUN", "why": "script uses a command outside the safe set"}; continue
            if "jq" in script and not jq:
                rec[key] = {"result": "NOT_RUN", "why": "script needs jq; jq not on PATH"}; continue
            rows = []
            with tempfile.TemporaryDirectory() as td:
                sp = Path(td) / "hook.sh"; sp.write_text(script, encoding="utf-8")
                for label, payload, want in fx:
                    payload = dict(payload, session_id="d9a", cwd=td)
                    try:
                        cp = subprocess.run([bash, str(sp)], cwd=td, input=json.dumps(payload).encode(), capture_output=True, timeout=10)
                        code, err = cp.returncode, cp.stderr.decode("utf-8", "replace").strip().splitlines()[:1]
                    except subprocess.TimeoutExpired:
                        code, err = "timeout", []
                    rows.append({"fixture": label, "exit": code, "expected": want, "stderr_first_line": (err[0][:200] if err else "")})
            rec[key] = {"result": "PASS" if all(r["exit"] == r["expected"] for r in rows) else "FAIL", "rows": rows}
    wjson(out / "exec.json", rec)
    print(json.dumps({k: v["result"] for k, v in rec.items()}))

def score(a):
    out = Path(a.out)
    table, findings, obs, graded = [], [], [], 0
    totals = {arm: [0, 0] for arm in ARMS}
    for case in a.cases:
        gp = out / "grading" / f"{case}.json"
        g = rjson(gp) if gp.exists() else {"status": "NOT_GRADED"}
        if g["status"] != "GRADED":
            table.append({"case": case, "status": g["status"]}); continue
        graded += 1
        inv = {arm: lbl for lbl, arm in g["key"].items()}
        row = {"case": case, "status": "GRADED", "assertions": []}
        for r in g["grade"]["results"]:
            cell = {arm: r[inv[arm]] for arm in ARMS}
            row["assertions"].append({"id": r["id"], **{arm: cell[arm]["pass"] for arm in ARMS}})
            for arm in ARMS:
                totals[arm][0] += cell[arm]["pass"]; totals[arm][1] += 1
            if not cell["v5.0"]["pass"]:
                findings.append({"case": case, "assertion": r["id"], "text": CASES[case][1][int(r["id"][1:]) - 1],
                                 "v5.0_evidence": cell["v5.0"]["evidence"][:200]})
            if cell["v4.2"]["pass"] and r["id"] in PREDICTED_V42_FAIL.get(case, []):
                obs.append(f"{case} {r['id']}: v4.2 passed an assertion the spec predicted it would fail")
        row["v4.2"] = sum(x["v4.2"] for x in row["assertions"]); row["v5.0"] = sum(x["v5.0"] for x in row["assertions"])
        table.append(row)
    rows = [r for r in table if r["status"] == "GRADED"]
    if graded < len(a.cases):
        verdict = "INCOMPLETE"
    elif any(r["v5.0"] < r["v4.2"] for r in rows):
        verdict = "FAIL"
    elif findings:
        verdict = "PASS_WITH_FINDINGS"
    else:
        verdict = "PASS"
    summary = {"verdict": verdict, "graded": graded, "cases": len(a.cases),
               "totals": {arm: f"{p}/{n}" for arm, (p, n) in totals.items()},
               "differential": totals["v5.0"][0] - totals["v4.2"][0], "per_case": table,
               "v5_0_misses": findings, "observations": obs, "claude_children_this_invocation": spawned}
    wjson(out / "summary.json", summary)
    print(json.dumps({k: summary[k] for k in ("verdict", "graded", "totals", "differential")}))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("phase", choices=["setup", "probe", "arms", "grade", "exec", "score", "all"])
    ap.add_argument("--repo", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--cases", nargs="*", default=list(CASES))
    ap.add_argument("--model", default=MODEL)
    ap.add_argument("--grader-model", default=MODEL)
    ap.add_argument("--probe-model", default=PROBE_MODEL)
    ap.add_argument("--zips", help="folder with <arm>/rootnode-cc-design-cc.zip instead of downloading")
    ap.add_argument("--work", help="arm and grader folders (default ~/d9a-cc-design-v5.0, outside the repo)")
    a = ap.parse_args()
    global WORK
    if a.work:
        WORK = Path(a.work)
    Path(a.out).mkdir(parents=True, exist_ok=True)
    steps = {"setup": setup, "probe": probe, "arms": arms, "grade": grade, "exec": exec_hooks, "score": score}
    for name in (list(steps) if a.phase == "all" else [a.phase]):
        print(f"== {name}")
        steps[name](a)

if __name__ == "__main__":
    main()
