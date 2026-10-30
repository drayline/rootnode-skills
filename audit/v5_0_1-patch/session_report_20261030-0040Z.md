---
prompt: root_CC_build_catalog_v5.0.1 (pasted into the session; no file path, digest not computed)
outcome: COMPLETED
started: 2026-10-30T00:22Z
ended: 2026-10-30T00:40Z
---

# Session report — catalog v5.0.1 content PR

Phase 3 closed: PR #28 (`release/v5.0.1` → `main`) is open at head `6a257f9f73305b7ef248cc5d353f1cc2bd04b5a2`. The Refuter returned ACCEPT in cycle 1, bound to diff digest `457185caf53219c1813d4a6c8d7f1a52fa6b80699c0f4f91e7d3d89336b002ea`. No halt fired.

## Pre-state (report-only)

| Branch | HEAD | Dirty paths |
|---|---|---|
| main | `e336bce54941a6b0ec0fae01f8dbcc9261324b37` | 4 |

- `origin/main` after `git fetch`: `e336bce54941a6b0ec0fae01f8dbcc9261324b37`.
- `claude --version`: 2.1.302 (Claude Code). `claude --help` lists `--effort`: yes (`--effort <level>`).
- `rootnode-*` Skills loaded in this session: all 27, as `anthropic-skills:rootnode-*` (account sync). None was invoked.
- `gh auth status`: logged in as `drayline`.

**Phase 0 halt checks**

| Halt | Result | Evidence |
|---|---|---|
| H0 | clear | `git branch -a --list '*release/v5.0.1*'` and `git ls-remote --heads origin release/v5.0.1` both empty |
| H1 | clear | All four LF digests match (Post-state table) |
| H2 | clear | The prompt's pathspec `'rootnode-*/'` matches nothing (F-2), so I re-ran it with `':(glob)rootnode-*/**'` → 0 files. The whole tree `e336bce..origin/main` also shows 0 files. |
| H3 | clear | jq-1.8.2 (jqlang winget package). It is not on this process's PATH but is on the persisted user PATH; used by prepending the folder (F-1) |
| H4 | clear | The doc says "Check this value or process the transcript". It does not require a hook to allow the stop whenever the field is true. Quote below. |

## Post-state

HEAD: `6a257f9f73305b7ef248cc5d353f1cc2bd04b5a2` (= `origin/release/v5.0.1`). Commits: `a88d449` (fix), `6a257f9` (docs(audit)).

| File | LF-sha256 | Expected (prompt) | Match |
|---|---|---|---|
| `design/root_DESIGN_catalog_v5.0.1_patch.md` | `9840eac3cb809e48324a30a00f7343d6ab681690e69f0150b71302e448e14c68` | same | yes (input, and index blob at commit 2) |
| `design/staging-kf/root_CC_ENVIRONMENT_GUIDE.md` | `a19a37640d76d704b4a7f58b81e5b4d2c96e1ee1f495cef816f2bc5c1f1699f0` | same | yes |
| `design/staging-kf/root_AGENT_ANTI_PATTERNS.md` | `12b709272741a0ca431e4763b948d9e5394c5c21a7f0209283cd81397b9c7dbe` | same | yes |
| `design/staging-kf/root_SKILL_BUILD_DISCIPLINE.md` | `ebe0b845fd5423fcd7001c3e319df5dae0c37192853f40f2f58d53d896e19d78` | same | yes |
| `audit/canonical-kfs/root_CC_ENVIRONMENT_GUIDE.md` (index blob) | `a19a37640d76d704b4a7f58b81e5b4d2c96e1ee1f495cef816f2bc5c1f1699f0` | H1 CC_EG | yes, 0 `\r` |
| `audit/canonical-kfs/root_AGENT_ANTI_PATTERNS.md` (index blob) | `12b709272741a0ca431e4763b948d9e5394c5c21a7f0209283cd81397b9c7dbe` | H1 AAP | yes, 0 `\r` |
| `audit/canonical-kfs/root_SKILL_BUILD_DISCIPLINE.md` (index blob) | `ebe0b845fd5423fcd7001c3e319df5dae0c37192853f40f2f58d53d896e19d78` | H1 SBD | yes, 0 `\r` |

## Files changed — 61 rows

`git diff --name-status origin/main` (39 A, 22 M); the third column gives the scope category.

| Status | File | Category |
|---|---|---|
| M | `audit/canonical-kfs/root_AGENT_ANTI_PATTERNS.md` | mirror (§3 C) |
| M | `audit/canonical-kfs/root_CC_ENVIRONMENT_GUIDE.md` | mirror (§3 C) |
| M | `audit/canonical-kfs/root_SKILL_BUILD_DISCIPLINE.md` | mirror (§3 C) |
| A | `audit/v5_0-alignment/d9a_cc-design_v5.0_20261029-1406Z.md` | D9a report |
| A | `design/audit-artifacts/v5.0/d9a/d9a_runner.py` | D9a evidence |
| A | `design/audit-artifacts/v5.0/d9a/out/exec.json` | D9a evidence |
| A | `design/audit-artifacts/v5.0/d9a/out/grading/C1.json` | D9a evidence |
| A | `design/audit-artifacts/v5.0/d9a/out/grading/C2.json` | D9a evidence |
| A | `design/audit-artifacts/v5.0/d9a/out/grading/C3.json` | D9a evidence |
| A | `design/audit-artifacts/v5.0/d9a/out/grading/C4.json` | D9a evidence |
| A | `design/audit-artifacts/v5.0/d9a/out/grading/C5.json` | D9a evidence |
| A | `design/audit-artifacts/v5.0/d9a/out/grading/C6.json` | D9a evidence |
| A | `design/audit-artifacts/v5.0/d9a/out/probe.json` | D9a evidence |
| A | `design/audit-artifacts/v5.0/d9a/out/runs/v4.2/C1.json` | D9a evidence |
| A | `design/audit-artifacts/v5.0/d9a/out/runs/v4.2/C1.md` | D9a evidence |
| A | `design/audit-artifacts/v5.0/d9a/out/runs/v4.2/C2.json` | D9a evidence |
| A | `design/audit-artifacts/v5.0/d9a/out/runs/v4.2/C2.md` | D9a evidence |
| A | `design/audit-artifacts/v5.0/d9a/out/runs/v4.2/C3.json` | D9a evidence |
| A | `design/audit-artifacts/v5.0/d9a/out/runs/v4.2/C3.md` | D9a evidence |
| A | `design/audit-artifacts/v5.0/d9a/out/runs/v4.2/C4.json` | D9a evidence |
| A | `design/audit-artifacts/v5.0/d9a/out/runs/v4.2/C4.md` | D9a evidence |
| A | `design/audit-artifacts/v5.0/d9a/out/runs/v4.2/C5.json` | D9a evidence |
| A | `design/audit-artifacts/v5.0/d9a/out/runs/v4.2/C5.md` | D9a evidence |
| A | `design/audit-artifacts/v5.0/d9a/out/runs/v4.2/C6.json` | D9a evidence |
| A | `design/audit-artifacts/v5.0/d9a/out/runs/v4.2/C6.md` | D9a evidence |
| A | `design/audit-artifacts/v5.0/d9a/out/runs/v5.0/C1.json` | D9a evidence |
| A | `design/audit-artifacts/v5.0/d9a/out/runs/v5.0/C1.md` | D9a evidence |
| A | `design/audit-artifacts/v5.0/d9a/out/runs/v5.0/C2.json` | D9a evidence |
| A | `design/audit-artifacts/v5.0/d9a/out/runs/v5.0/C2.md` | D9a evidence |
| A | `design/audit-artifacts/v5.0/d9a/out/runs/v5.0/C3.json` | D9a evidence |
| A | `design/audit-artifacts/v5.0/d9a/out/runs/v5.0/C3.md` | D9a evidence |
| A | `design/audit-artifacts/v5.0/d9a/out/runs/v5.0/C4.json` | D9a evidence |
| A | `design/audit-artifacts/v5.0/d9a/out/runs/v5.0/C4.md` | D9a evidence |
| A | `design/audit-artifacts/v5.0/d9a/out/runs/v5.0/C5.json` | D9a evidence |
| A | `design/audit-artifacts/v5.0/d9a/out/runs/v5.0/C5.md` | D9a evidence |
| A | `design/audit-artifacts/v5.0/d9a/out/runs/v5.0/C6.json` | D9a evidence |
| A | `design/audit-artifacts/v5.0/d9a/out/runs/v5.0/C6.md` | D9a evidence |
| A | `design/audit-artifacts/v5.0/d9a/out/setup.json` | D9a evidence |
| A | `design/audit-artifacts/v5.0/d9a/out/summary.json` | D9a evidence |
| A | `design/audit-artifacts/v5.0/d9a/root_CC_d9a_cc-design_v5.0.md` | D9a evidence |
| A | `design/audit-artifacts/v5.0/d9a/run.log` | D9a evidence |
| A | `design/root_DESIGN_catalog_v5.0.1_patch.md` | spec |
| M | `design/root_DESIGN_catalog_v5_model_alignment.md` | spec §3 B F2 |
| M | `rootnode-cc-design/SKILL.md` | spec §3 B F13/F14/F15/F31 + version |
| M | `rootnode-cc-design/references/cc-anti-patterns.md` | spec §3 A1 (+F27/F28/F29) |
| M | `rootnode-cc-design/references/cc-environment-design-patterns.md` | spec §3 B F22 |
| M | `rootnode-cc-design/references/cc-prompt-design-patterns.md` | spec §3 A2, F21 |
| M | `rootnode-cc-design/references/cc-session-reports.md` | A1 notification extra |
| M | `rootnode-cc-design/references/cc-skills-and-hooks-composition.md` | spec §3 A1 (+F27/F28/F29) |
| M | `rootnode-context-budget/SKILL.md` | spec §3 B F18/F20 + version |
| M | `rootnode-critic-gate/SKILL.md` | spec §3 B F19 + version |
| M | `rootnode-domain-agentic-context/SKILL.md` | version bump only |
| M | `rootnode-domain-agentic-context/references/reasoning-approaches.md` | spec §3 B F16 |
| M | `rootnode-domain-research-analysis/SKILL.md` | spec §3 B F24 + version |
| M | `rootnode-full-stack-audit/SKILL.md` | spec §3 B F18 + version |
| M | `rootnode-global-audit/SKILL.md` | spec §3 B F18 + version |
| M | `rootnode-handoff-trigger-check/SKILL.md` | spec §3 B F17 + version |
| M | `rootnode-project-audit/SKILL.md` | spec §3 B F18 + version |
| M | `rootnode-prompt-compilation/SKILL.md` | spec §3 B F18 + version |
| M | `rootnode-prompt-validation/SKILL.md` | version bump only |
| M | `rootnode-prompt-validation/references/symptom-fix-map.md` | spec §3 B F16 |

Untracked, not committed: `audit/v5_0_1-patch/` (this report, `refuter_brief_c1.md`, `refuter_c1.json`), `design/audit-artifacts/v4.2/` (out of scope), and the 12 `design/audit-artifacts/v5.0/d9a/out/runs/*/C*.jsonl` streams. `design/staging-kf/PR_BODY_v5.0.1.md` is gitignored.

**In scope with notification (one extra file per spec item):** `rootnode-cc-design/references/cc-session-reports.md`, used for A1. Its line "released on its no-progress cap is recorded `NOT_RUN`" now reads "released on either cap (no-progress or chain total)".

## Touched Skills

Computed from `git diff --name-only origin/main -- ':(glob)rootnode-*/**'`; equals spec P2: cc-design, context-budget, critic-gate, domain-agentic-context, domain-research-analysis, full-stack-audit, global-audit, handoff-trigger-check, project-audit, prompt-compilation, prompt-validation (11). Two of them (domain-agentic-context, prompt-validation) change only `references/` plus the version line in SKILL.md.

## Gates

| ID | Command | Result | Evidence |
|---|---|---|---|
| G1 | `git diff --name-status origin/main`, each row classified | PASS | 61 rows = 1 spec + 1 D9a report + 37 D9a evidence + 3 mirrors + 2 version-only SKILL.md + 16 spec §3 A/B files + 1 A1 notification extra; 0 unexpected; 0 `.jsonl` |
| G2 | Touched set vs P2; parsed `metadata.version` of all 27 `SKILL.md` (PyYAML) | PASS | Sets equal (11). 11 × `5.0.1`, 16 × `5.0.0`, 0 mismatches |
| G3 | Before string on `origin/main` vs now; after string now (LF-normalized `grep -F`) | PASS | 28 checks, 0 fail; rows below |
| G4 | YAML parse of the cc-design `description:`; `python rootnode-skill-builder/scripts/quick_validate.py <dir>` × 11 | PASS | Parsed, 694 characters (≤ 1024). All 11: exit 0, "Skill is valid!" |
| G5 | Revised sketch extracted from the committed reference (0 `\r`, `bash -n` OK), run with jq-1.8.2, failing evidence, N = 2, M = 6 | PASS | Rows below; harness exit 0, 0 fails |
| G6 | `git show :<path> \| tr -d '\r' \| sha256sum`; `\r` count per blob | PASS | Three digests equal H1; 0 `\r`; 0 `\r` in every staged blob of both commits |
| G7 | `python build_release_artifacts.py` | PASS | exit 0; "29 artifacts: 24 -cp (flat) + 5 -cc (wrapper)". Bundle name `rootnode-catalog-v5.0.zip` left alone (P3 belongs to the release prompt). `dist/` is gitignored; 0 status rows |

**G3 rows** (line numbers: before on `origin/main` → after now)

| Row | File | Before → after |
|---|---|---|
| F2a, F2b | `design/root_DESIGN_catalog_v5_model_alignment.md` | L6 → L6 (Status ACCEPTED); L74 → L74 (block-selection T2) |
| F13a/b/c | `rootnode-cc-design/SKILL.md` | L164 §2→§1; L180 §4→§7; L109 "§ Assert the END state" → "§10" (target headings verified: methodology §1 "The agent-warranted test", §7 "Additive evolution with narrow detection"; prompt-design §10 holds "Why the end state and not the pre state") |
| F14 | `rootnode-cc-design/SKILL.md` | L266, 15 → 17 (`cc-anti-patterns.md`: 17 catalog rows, 17 `## §` sections, counted) |
| F15 | `rootnode-cc-design/SKILL.md` | L6–7 |
| F16a, F16b | `reasoning-approaches.md`, `symptom-fix-map.md` | L89 → L89; L176 → L176. The fallback lines naming Opus 5 (agentic-context SKILL.md L25, L57; prompt-validation SKILL.md L26) are unchanged |
| F17 | `rootnode-handoff-trigger-check/SKILL.md` | L36 → L36; no anchors referenced the old heading |
| F18a–e | context-budget L49, full-stack-audit L43, global-audit L43, project-audit L41, prompt-compilation L51 | Each paragraph now states the D4 rule once (approach under Observations) |
| F19 | `rootnode-critic-gate/SKILL.md` | L156 → L107 (`"status": "complete \| blocked"`) and L157 (`blocked_reason`) |
| F20 | `rootnode-context-budget/SKILL.md` | L123 → L123 (cites `root_CLAUDE_OPTIMIZATION_NOTES.md` §3; its §3 table L136–137 carries the ≤100K / >100K band and the cache-read rates) |
| F21 | `cc-prompt-design-patterns.md` | L249 → L250 |
| F22 | `cc-environment-design-patterns.md` | L223 → L223 |
| F24 | `rootnode-domain-research-analysis/SKILL.md` | L47 → L47 (`examples.md` "Example 4: Marked Quotations in the Output Layer" exists) |
| F27 | `cc-skills-and-hooks-composition.md` | L244 → L246; L234 → L248 |
| F28 | `cc-skills-and-hooks-composition.md` | L218 → L218 (matcher); L238 → L238 (`notebook_path`) |
| F29 | `cc-skills-and-hooks-composition.md` | L249 → L257 |
| F31 | `rootnode-cc-design/SKILL.md` | L168 → L168 |

**G5 rows**

| Row | Stops (`stop_hook_active`) | Expected | Got | Counter after (`KEY N TOTAL`) |
|---|---|---|---|---|
| (a) | false, unchanged evidence | 2 | 2 | `e87c9f3cc9d96aca 1 1` |
| (b) | true, unchanged | 2 | 2 | `e87c9f3cc9d96aca 2 2` |
| (c) | true, unchanged | 0 | 0 | `e87c9f3cc9d96aca 3 3` |
| (d1) | false, evidence rewritten | 2 | 2 | `e66da32a2b790c35 1 1` |
| (d2)–(d6) | true, evidence rewritten each stop | 2 each | 2 each | N stays 1; TOTAL 2…6 |
| (d7) | true, evidence rewritten | 0 | 0 | `85ff95f2ca9e26ea 1 7` |
| (e1)–(e3) | clean folder, jq hidden (`command -v jq` empty); false, true, true | 2, 2, 0 | 2, 2, 0 | `230d… 1 1`, `2 2`, `3 3` |
| (e′1)–(e′3) | clean folder, jq hidden; false, false, false (stronger fixture: no reset without jq) | 2, 2, 0 | 2, 2, 0 | `b539… 1 1`, `2 2`, `3 3` |

Gate log, case (a)–(d) folder: blocks 1–3 then `release … 3 3`; blocks `1 1` … `1 7` then `release … 1 7`.

**Guard fixtures (F27–F29 evidence, beyond G3).** 24 of 24 pass with the guard extracted from the committed reference:
- Blocked (exit 2):
  - `rm -rf migrations`, `rm migrations/0001.sql`
  - `find migrations -delete`, `find . -path './migrations/*' -delete`, `find db/migrations -name x -exec rm {} +`
  - `cd migrations && rm 0001.sql`, `cd db/migrations; rm -rf *`
  - `rm -rf mig*`, `rm -rf ./m*`, `mv m* /tmp`, `rm -rf */mig*`
  - `echo rm migrations` (accepted false positive)
  - Edit `migrations/x.sql`, Edit `C:\repo\migrations\x.sql`
  - NotebookEdit `/repo/migrations/a.ipynb`
- Allowed (exit 0): `rm -rf migrations_backup`, `rm -rf src/*`, `rm *.tmp`, `ls mig*`, `cd migrations_backup && rm x`, `find . -name '*.pyc' -delete`, `cat migrations/0001.sql`, NotebookEdit `/repo/nb/a.ipynb`, Write `src/x.py`.
- F29: in a folder with no `.claude/`, the guard created it and wrote 14 audit rows.
- Decoy files `mig_decoy` and `migrations_backup` in the working folder did not cause glob expansion (`set -f`).

## Refuter cycles

| Cycle | Verdict | Diff digest | Must-fix IDs | Run |
|---|---|---|---|---|
| 1 | ACCEPT | `457185caf53219c1813d4a6c8d7f1a52fa6b80699c0f4f91e7d3d89336b002ea` (Refuter's line 2 equals the Builder's) | none | `claude -p --model claude-opus-5-5 --effort high --setting-sources project,local --tools "Read,Grep,Glob,Bash"`, allow-list `git diff/show/log`; 23 turns, $5.95, 3 permission denials (F-4); first line "Verdict Dictated: no" |

- Receipt freeze: the digest was recomputed after the verdict and before the push, and it was unchanged. No reviewed file was written after the ACCEPT.
- Pre-run permission probe: one `claude -p` on Haiku 5.5 with the Refuter's exact flags ran `git diff origin/main...HEAD | tr -d '\r' | sha256sum`, with 0 denials and a matching digest. It did no review and was not a Refuter cycle.
- The Agent tool was not used.

## H4 doc quote

`https://code.claude.com/docs/en/hooks.md`, fetched 2026-10-30 (HTTP 200, 283,477 bytes), Stop input section:

> In addition to the [common input fields](#common-input-fields), Stop hooks receive `stop_hook_active`, `last_assistant_message`, `background_tasks`, and `session_crons`. The `stop_hook_active` field is `true` when Claude Code is already continuing as a result of a stop hook. Check this value or process the transcript to avoid blocking on a condition that will never resolve.

The paragraph that follows in the same section (relevant to F-9):

> Claude Code applies an 8-consecutive-continuation cap: after stop hooks have continued the turn eight times in a row, Claude Code overrides the next block and ends the turn. The count of consecutive continuations resets each time Claude calls a tool. To raise the cap, set [`CLAUDE_CODE_STOP_HOOK_BLOCK_CAP`](https://code.claude.com/docs/en/env-vars).

## Findings

| ID | Severity | Locator | Status | Owner |
|---|---|---|---|---|
| F-1 | low | Environment: `jq` | open | operator |
| F-2 | medium | Build prompt H2 and Phase 1 step 4 | open | chat |
| F-3 | medium | Build prompt Phase 1 step 7 | open | chat |
| F-4 | low | Build prompt Phase 2 Refuter allow-list | open | chat |
| F-5 | low | Environment: `python` | open | operator |
| F-6 | low | `rootnode-cc-design/references/troubleshooting.md:82` | next patch | chat |
| F-7 | low | "handoff-gate" shorthand outside cc-design | next patch | chat |
| F-8 | low | `cc-skills-and-hooks-composition.md` guard sketch | next patch | chat |
| F-9 | medium | CC_EG §6, cc-design §5: host Stop-hook cap | KF block surfaced | chat → seed |

- **F-1.** jq-1.8.2 is installed by winget, and its folder is on the persisted user PATH. It is not on this Claude Code process's PATH, because the process predates the install. Every jq use here prepended `%USERPROFILE%\AppData\Local\Microsoft\WinGet\Packages\jqlang.jq_Microsoft.Winget.Source_8wekyb3d8bbwe`. Restarting VS Code / Claude Code clears it.
- **F-2.** The pathspec `'rootnode-*/'` (in H2 and in step 4) matches no files in git 2.53.0.windows.2: it returned 0 even with 16 modified Skill files present. As written, H2 would pass vacuously and step 4 would compute an empty touched set. This run used `':(glob)rootnode-*/**'`. Future prompts should use that form or `'rootnode-*'`.
- **F-3.** `git add design/audit-artifacts/v5.0/d9a ':!*.jsonl'` exited 0 but staged nothing for the untracked folder (tried twice). This run used the same intended set: `find design/audit-artifacts/v5.0/d9a -type f ! -name '*.jsonl' -print0 | xargs -0 git add --`, which staged 37 files and 0 `.jsonl`. Before committing that public evidence, it was scanned for API keys, GitHub tokens, bearer tokens, email addresses and user-home paths: 0 hits.
- **F-4.** With the allow-list `Bash(git diff:*)`, `Bash(git show:*)`, `Bash(git log:*)`, the Refuter's mirror-digest recomputations were denied: a `for` loop and a `&&` chain of `git show | tr | sha256sum`, plus one compound heading-listing command. Single `git … | tr | sha256sum` pipelines run (probe). G6 therefore rests on the Builder's check, and the JSON output does not show whether the Refuter verified the mirrors another way. Fix in the template: add `Bash(sha256sum:*)` and `Bash(tr:*)`, or tell the Refuter to run one pipeline per call.
- **F-5.** `python` resolves to LibreOffice's bundled Python 3.12.13 (`C:\Program Files\LibreOffice\program\python-core-3.12.13`). G2, G4 and G7 ran on it and passed. A future gate needing packages it lacks would fail for an environment reason.
- **F-6.** "If it is a Stop hook, also bound it (`stop_hook_active`, no-progress cap)" predates A1. It is not contradictory, but it omits the chain-total cap. A1's one-extra-file allowance went to `cc-session-reports.md`. Next-patch block: "(chain-scoped by `stop_hook_active`; no-progress and chain-total caps)".
- **F-7.** F31 was scoped to cc-design SKILL.md. The same shorthand remains at:
  - `rootnode-critic-gate/SKILL.md:213`
  - `rootnode-critic-gate/references/checks-detailed.md:199`
  - `rootnode-handoff-trigger-check/SKILL.md:82`
  - `rootnode-handoff-trigger-check/references/examples.md:142`
  - `rootnode-mode-router/SKILL.md:105`

  Next-patch block: replace with "rootnode-handoff-trigger-check" ("(if available)" where cross-Skill).
- **F-8.** Gaps the spec's F27/F28 lists did not cover:
  - `find . -delete` with an unrestricted start path is not caught.
  - The tools reference lists a `PowerShell` tool, which can delete files and is not in the matcher. F28 asked only about edit tools.
  - The glob check fails closed on any glob token in a command that also contains `rm`/`mv`/`find` (for example `ls m* && rm x`).

  These go to the next design cycle.
- **F-9 (KF block).** The hooks doc documents a host-side cap. After 8 consecutive stop-hook continuations, Claude Code overrides the next block, and the count resets each time Claude calls a tool (`CLAUDE_CODE_STOP_HOOK_BLOCK_CAP`). With the unattended working value N = 8, M defaults to 24. In a chain where Claude makes no tool call between stops, the host cap releases first. Neither the A1 text nor the synced CC_EG §6 names the host cap. Block under KF deltas.

## Operator decisions

None. No halt fired, and the only operator input this session was the pasted build prompt.

## Observations

- [observed] The H4 doc does not require releasing on `true`. Spec A1's chain-scoped count is consistent with "Check this value or process the transcript to avoid blocking on a condition that will never resolve."
- [observed] `MultiEdit` is absent from the tools reference's tool table; `NotebookEdit` is present. The running `NotebookEdit` schema names its path `notebook_path`, not `file_path`. Adding `NotebookEdit` to the matcher alone would have let notebook edits under `migrations/` through, because the guard would read an empty path and exit 0. F28 therefore also adds `.tool_input.notebook_path` to the guard's jq path. Hooks doc: `Edit|Write|Bash` is an exact-name list, so `NotebookEdit` was not covered before.
- [observed] AEA §5.4 (`audit/canonical-kfs/root_AGENT_ENVIRONMENT_ARCHITECTURE.md`) defines only the `critic_gate_threshold` profile field. It does not enumerate critic-gate output fields, so F19 surfaces no KF block.
- [inferred] G5 (d): the only reading consistent with "release when `TOTAL > MAX_TOTAL`" and M = 6 counts the fresh `false` stop as stop 1 of 7. Under the other reading (six `true` stops after the `false`), the release would fall on the sixth `true` stop.
- [inferred] F18 approach:
  - context-budget and full-stack-audit already state the full D4 rule in their Run sentence, so the trailing clause was dropped.
  - global-audit, project-audit and prompt-compilation state only "start at `medium`" / "Sonnet `high`", so the trailing clause became the D4 step-up wording ("step to `high` when verification matters or edge cases are likely").
- [observed] F2 was applied literally: the header's trailing sentence "CC build prompt follows acceptance." still follows the new ACCEPTED status.
- [observed] The A1 tag reads `fetched 2026-10-30`, the UTC fetch date; local Phoenix date was 2026-10-29.
- [observed] F20 removes the "pays the higher band on the whole prompt" inference and the "budget against the band" guidance that rested on it.

## Not verified

- **CI (spec §3 C, "The SBD description's arm-hygiene clause gains the sync-isolation rule").** This lives in the seed Project's custom instructions, not in this repo. Only the SBD KF body line changed in the synced mirror.
- **Refuter mirror-digest check.** Whether the Refuter verified the three mirror digests itself is unknown (F-4); G6 is Builder-verified.
- **Rendered PR page.** The PR body was checked as stored (`gh pr view 28 --json body`, LF-normalized equal to the body file apart from a trailing newline). The page was not inspected in a browser.
- **Live hook behavior.** The guard and Stop sketches ran as standalone scripts against JSON fixtures, not as hooks in a live Claude Code session.
- **Build prompt digest.** Not computed; the prompt was pasted with no file.

## KF deltas

- **Synced this PR (§3 C):** `audit/canonical-kfs/root_CC_ENVIRONMENT_GUIDE.md`, `root_AGENT_ANTI_PATTERNS.md`, `root_SKILL_BUILD_DISCIPLINE.md`, digests in Post-state.
- **New block (F-9), not applied:**
  - Target KF: `root_CC_ENVIRONMENT_GUIDE.md` §6 "Bounded Stop hooks" (and the parallel `rootnode-cc-design/references/cc-skills-and-hooks-composition.md` §5 at the next patch).
  - Action: ADD.
  - Block: "Claude Code also caps stop-hook continuations on the host side: after 8 consecutive continuations it overrides the next block and ends the turn; the count resets each time Claude calls a tool, and `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP` raises it `[Anthropic docs — hooks, fetched 2026-10-30]`. A hook's own caps should release first: with N = 8 unattended, set M at or below the host cap, or raise the host cap deliberately."
  - Rationale: the default M = 3×N = 24 exceeds the host cap whenever stops repeat without a tool call between them, so a hook can be overridden by the host instead of releasing on its own logged cap.
- **Next-patch blocks (Skill content, not KF):** F-6, F-7, F-8.

Phase 3 closed; PR #28 open. Merge it, then ask chat for the v5.0.1 release prompt.
