# root_CC_d9a_cc-design_v5.0 — D9a behavioral validation, rootnode-cc-design v4.2 vs v5.0

Run this in a Claude Code session started in `C:\Projects\rootnode-skills`. It is the controlling session prompt under the repo CLAUDE.md §Scope authorization. It changes no tracked file and makes no commit.

## Mission

Compare rootnode-cc-design v5.0 against v4.2 on the six composition cases in `design/root_DESIGN_cc-design_v5.md` §11 (C1–C6). Each case runs once per arm on Opus 5.5. A blind Opus 5.5 grader scores both outputs against binary assertions with quoted evidence. The result feeds the cc-design 5.0.1 fix pass: one test pass, one fix pass, then ship (SBD §3.9 stopping rule). This session does not fix anything.

## How the run is built

All Claude calls run inside `design/audit-artifacts/v5.0/d9a/d9a_runner.py`. You start the runner and read its small summary files; you do not make Claude calls yourself.

- **Arm isolation.** Each arm is a `claude -p` child in its own folder, `~/d9a-cc-design-v5.0/arm-v4.2` or `arm-v5.0`, outside the repo. The arm's Skill is installed there at project level from its GitHub release `-cc` zip. Children run with `--setting-sources project,local`. On Claude Code 2.1.312, that flag kept the account-synced `anthropic-skills:rootnode-cc-design` out of the run; a plain `claude -p` loaded both copies. `[observed 2026-10-29, Claude Code 2.1.312]`
- **Per-run evidence.** For every run, the runner reads the harness `init` event and checks three things. Exactly one cc-design Skill is listed, and it is the arm's project copy. The model starts with `claude-opus-5-5`. A `Skill` tool call names `rootnode-cc-design`. A run that fails any of these is retried once, then recorded `INVALID`.
- **Blind grading.** Per case, the runner randomly labels the outputs X and Y and keeps the key in a file the grader never sees. The grader runs with no tools and no cc-design Skill.
- **Hook execution (report only).** For C1 and C3, the runner extracts the bash hook from each output and runs it against fixture input in a temp folder. Each run has a 10-second limit. A script that uses `rm`, `git`, `curl`, `wget` or a package install is not run. The result is evidence for the report, not part of the verdict.

## Scope

**In scope:** create `design/audit-artifacts/v5.0/d9a/out/` and `design/audit-artifacts/v5.0/d9a/run.log`; let the runner create `~/d9a-cc-design-v5.0/`; write the session report to `audit/v5_0-alignment/d9a_cc-design_v5.0_<YYYYMMDD-HHMM>Z.md` (stamp from `date -u +%Y%m%d-%H%M`). Do not commit the report; it rides the 5.0.1 commit cycle.

**Out of scope:** git commits, branches, and pushes; edits to any tracked file; installing software; invoking any Skill (this session may list `rootnode-cc-design` from the account sync — do not use it); the Agent tool; Claude calls outside the runner.

**Delegation:** no subagents. The runner caps Claude child processes in code, at 40 per invocation; by construction the run needs at most 39 (3 probes, 12 arm runs plus up to 12 retries, 6 grader runs plus up to 6 retries). Arm children get only the `Skill` and `Read` tools, and graders get none, so no child can write files or spawn agents.

**Cost:** about 18 Opus 5.5 calls plus 3 Haiku 5.5 probes. In a Haiku smoke test, each arm call read about 170k input tokens, mostly cache, and wrote about 4k. Opus calls on C2 and C4 will be larger. Plan for a large share of one usage window and about 30–90 minutes of wall time. These figures are estimates.

## Phase 0 — Pre-flight

Record for the report (report-only):

```bash
date -u +%Y-%m-%dT%H:%MZ
git branch --show-current
git rev-parse HEAD
git status --porcelain | wc -l
claude --version
git fetch origin --tags
```

Find a Python 3 command: use `python` if `python --version` prints 3.x, otherwise `py -3`. Use that command below as `<py>`.

Enumerate the Skills loaded in this session and note whether `rootnode-cc-design` is among them (report-only; do not invoke it).

**Gate G1 — runner digest.** `tr -d '\r' < design/audit-artifacts/v5.0/d9a/d9a_runner.py | sha256sum` must print `634efdb00b71e041e857ac7a22b870d835d1a8f55a9f9d561b70df168fca02f5`. On mismatch, or if the file is missing, halt **H1**: the operator saves the delivered `d9a_runner.py` to that path.

## Phase 1 — Run

*Turn-boundary continuation (Anthropic canonical block, CC_EG §5.9). It controls when the turn ends; it is not a self-check instruction:*

Keep working until everything the user asked for is done, and only stop to ask when you can't go on without the user or before a risky step.

When the work the user asked for is done and checked, stop and report. Don't add features, tests, files, docs or refactors that weren't asked for. If you think one would help, mention it at the end instead of doing it.

Start the runner in the background. It runs longer than a foreground command may run. Wait for it to exit; do not poll the log more often than every five minutes.

```bash
<py> design/audit-artifacts/v5.0/d9a/d9a_runner.py all --repo . --out design/audit-artifacts/v5.0/d9a/out > design/audit-artifacts/v5.0/d9a/run.log 2>&1
```

When it exits, read `tail -n 40 design/audit-artifacts/v5.0/d9a/run.log` and act on the exit code:

| Exit | Meaning | Action |
|---|---|---|
| 0 | All phases ran | Continue to Phase 2 |
| 10 | An arm's files do not match its tag or expected SKILL.md digest (`out/setup.json`) | Halt **H2**; report `setup.json` |
| 11 | Isolation failed: an arm folder lists a second cc-design copy, or the grader folder lists one (`out/probe.json`) | Halt **H3**; report `probe.json`, including its `stderr` fields |
| 12 | A run's model does not start with `claude-opus-5-5` | Halt **H4**; report the run's `.json` |
| 13 | `claude` or `git` not found by the runner | Halt **H5** |
| 14 | Child-process cap reached | Halt **H6**; report the log tail |

**H3 fallback for the operator:** in claude.ai → Settings → Skills, turn `rootnode-cc-design` off (do not delete it), then start a new Claude Code session so the sync removes the local copy, and paste this prompt again. Turn it back on after the run.

Every halt ends the session after the report is written. To resume, start a new session and paste this prompt again. The runner skips arm runs already `VALID` and cases already `GRADED`.

## Phase 2 — Report

Read only these files: `out/summary.json`, `out/setup.json`, `out/probe.json`, `out/exec.json`, and the `runs/*/*.json` metadata files. Do not read the `.md` outputs, `.jsonl` streams, or grader `raw` text into this session; the summary carries the evidence the report needs.

Write the session report using the template in rootnode-cc-design `references/cc-session-reports.md` §7. Fill every field from command output or the files above:

- **prompt:** `pasted — root_CC_d9a_cc-design_v5.0.md`
- **outcome:** `COMPLETED`, `HALTED H<n>`, or `BLOCKED`
- **post_state:** `uncommitted`. Then G1's digest, and each arm's `skill_md_lf_sha256` with `expected` from `setup.json`.
- **files_changed:** `git status --porcelain` rows. The count is the number of rows.
- **gates:**
  - G1, the runner digest.
  - G2, arm source per arm (`setup.json` `gate`).
  - G3, isolation per folder (`probe.json` `gate` and `init_cc_skills`).
  - G4, arm runs `VALID` out of 12.
  - G5, cases `GRADED` out of 6.
  - G6, hook execution per row from `exec.json`, marked report-only. A row the runner did not run is `NOT_RUN` with its `why`.
- **results:** one table, case × arm, with pass counts and the per-assertion pass/fail from `per_case`. Then `totals`, `differential` and `verdict` from `summary.json`, copied exactly.
- **findings:** one F-n per item in `v5_0_misses`: case, assertion text, and the quoted v5.0 evidence. Owner is cc-design 5.0.1. Mark the severity `untriaged`.
- **observations:**
  - `[observed]` each item in `summary.observations`, the model IDs in the run metadata, and `claude_code_version` from `probe.json`.
  - `[inferred]` only where a conclusion goes beyond the files.
- **not_verified:** at least the following, plus anything else the run did not check:
  - One sample per case per arm, so a one-assertion difference may be noise.
  - Effort was the Claude Code default for Opus 5.5 and was not pinned.
  - User-level CLAUDE.md may load into every child. This is the same for both arms.
  - The grader is the same model as the arms.
  - Hook execution covered only extractable bash scripts and the fixtures in the runner.
- **kf_deltas:** `none from this run — the 5.0.1 cycle decides`.

End with three lines: the verdict, the report path, and "If you turned off rootnode-cc-design on claude.ai for this run, turn it back on."
