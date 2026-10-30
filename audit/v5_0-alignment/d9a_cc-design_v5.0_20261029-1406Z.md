---
prompt: pasted — root_CC_d9a_cc-design_v5.0.md
outcome: COMPLETED
started: 2026-10-29T13:33Z
ended: 2026-10-29T14:06Z
---

# Session report — d9a_cc-design_v5.0

D9a behavioral validation, rootnode-cc-design v4.2 vs v5.0, cases C1–C6 from `design/root_DESIGN_cc-design_v5.md` §11, one run per case per arm on Opus 5.5, blind Opus 5.5 grader.

## Pre-state (report-only)
| Branch | HEAD | Dirty paths |
|---|---|---|
| main | e336bce54941a6b0ec0fae01f8dbcc9261324b37 | 2 |

Also recorded: `claude --version` → `2.1.302 (Claude Code)`; `git fetch origin --tags` exited 0; Python command `python` (3.12.13). Skills loaded in the orchestrating session include `anthropic-skills:rootnode-cc-design` (account sync); it was not invoked.

## Post-state
HEAD: uncommitted (HEAD unchanged at e336bce54941a6b0ec0fae01f8dbcc9261324b37)

| File | LF-sha256 | Expected (prompt) | Match |
|---|---|---|---|
| design/audit-artifacts/v5.0/d9a/d9a_runner.py | 634efdb00b71e041e857ac7a22b870d835d1a8f55a9f9d561b70df168fca02f5 | 634efdb00b71e041e857ac7a22b870d835d1a8f55a9f9d561b70df168fca02f5 | yes |
| arm v4.2 SKILL.md (`setup.json` `skill_md_lf_sha256`) | 4a85a0468dbf106b63206aa65c371ab82a41751bbf056a3ac8da99dccbfce397 | 4a85a0468dbf106b63206aa65c371ab82a41751bbf056a3ac8da99dccbfce397 | yes |
| arm v5.0 SKILL.md (`setup.json` `skill_md_lf_sha256`) | 02ac690c1275953b9314927121e17c4768fc1c49b69f7ab181a5188fe2011345 | 02ac690c1275953b9314927121e17c4768fc1c49b69f7ab181a5188fe2011345 | yes |

## Files changed — 3 rows
`git status --porcelain` after writing this report:
```
?? audit/v5_0-alignment/d9a_cc-design_v5.0_20261029-1406Z.md
?? design/audit-artifacts/v4.2/
?? design/audit-artifacts/v5.0/
```
The two `design/audit-artifacts/` rows were untracked before the session (pre-state 2). This session added `design/audit-artifacts/v5.0/d9a/out/` and `design/audit-artifacts/v5.0/d9a/run.log` inside the already-untracked `v5.0/` row, and the report row above. No tracked file was modified. Outside the repo: `~/d9a-cc-design-v5.0/` (arm-v4.2, arm-v5.0, grader).

## Gates
| ID | Command | Result | Evidence |
|---|---|---|---|
| G1 | `tr -d '\r' < design/audit-artifacts/v5.0/d9a/d9a_runner.py \| sha256sum` | PASS | `634efdb00b71e041e857ac7a22b870d835d1a8f55a9f9d561b70df168fca02f5` |
| G2 v4.2 | runner `setup` | PASS | `setup.json` v4.2: `gate: PASS`, files 13, mismatched [], extra_in_zip [] |
| G2 v5.0 | runner `setup` | PASS | `setup.json` v5.0: `gate: PASS`, files 14, mismatched [], extra_in_zip [] |
| G3 arm-v4.2 | runner `probe` | PASS | `probe.json`: `init_cc_skills: ["rootnode-cc-design"]` |
| G3 arm-v5.0 | runner `probe` | PASS | `probe.json`: `init_cc_skills: ["rootnode-cc-design"]` |
| G3 grader | runner `probe` | PASS | `probe.json`: `init_cc_skills: []` |
| G4 | runner `arms` | PASS | 12/12 `VALID`, all attempt 1 (`runs/*/*.json`) |
| G5 | runner `grade` | PASS | 6/6 `GRADED` (`run.log`) |
| G6 C1/v4.2 (report-only) | runner `exec` | NOT_RUN | `exec.json`: why `no bash` |
| G6 C1/v5.0 (report-only) | runner `exec` | NOT_RUN | `exec.json`: why `no bash` |
| G6 C3/v4.2 (report-only) | runner `exec` | NOT_RUN | `exec.json`: why `no bash` |
| G6 C3/v5.0 (report-only) | runner `exec` | NOT_RUN | `exec.json`: why `no bash` |

Runner exit code: 0. Log: `design/audit-artifacts/v5.0/d9a/run.log`.

## Results
Pass counts from `summary.json` `per_case`:

| Case | v4.2 | v5.0 | A1 | A2 | A3 | A4 | A5 | A6 |
|---|---|---|---|---|---|---|---|---|
| C1 | 5/5 | 5/5 | 4.2 P · 5.0 P | 4.2 P · 5.0 P | 4.2 P · 5.0 P | 4.2 P · 5.0 P | 4.2 P · 5.0 P | — |
| C2 | 3/5 | 4/5 | 4.2 F · 5.0 P | 4.2 P · 5.0 P | 4.2 P · 5.0 P | 4.2 P · 5.0 P | 4.2 F · 5.0 F | — |
| C3 | 2/3 | 2/3 | 4.2 F · 5.0 F | 4.2 P · 5.0 P | 4.2 P · 5.0 P | — | — | — |
| C4 | 1/6 | 5/6 | 4.2 F · 5.0 P | 4.2 F · 5.0 P | 4.2 F · 5.0 P | 4.2 F · 5.0 P | 4.2 F · 5.0 P | 4.2 P · 5.0 F |
| C5 | 2/3 | 3/3 | 4.2 F · 5.0 P | 4.2 P · 5.0 P | 4.2 P · 5.0 P | — | — | — |
| C6 | 4/4 | 4/4 | 4.2 P · 5.0 P | 4.2 P · 5.0 P | 4.2 P · 5.0 P | 4.2 P · 5.0 P | — | — |

P = pass, F = fail.

- totals: `{"v4.2": "17/26", "v5.0": "23/26"}`
- differential: `6`
- verdict: `PASS_WITH_FINDINGS`

## Findings
| ID | Severity | Locator | Status | Owner |
|---|---|---|---|---|
| F-1 | untriaged | C2 A5 — "Each halt names an exact continuation phrase for resuming." v5.0 evidence: "absent" | open | cc-design 5.0.1 |
| F-2 | untriaged | C3 A1 — "The script reads stop_hook_active from the hook input and allows the stop when it is true." v5.0 evidence: "absent" | open | cc-design 5.0.1 |
| F-3 | untriaged | C4 A6 — "A scout or search role is named on Haiku 5.5." v5.0 evidence: "absent" | open | cc-design 5.0.1 |

## Operator decisions
None. No halt fired.

## Observations
- [observed] `summary.observations`, verbatim:
  - C1 A1: v4.2 passed an assertion the spec predicted it would fail
  - C1 A2: v4.2 passed an assertion the spec predicted it would fail
  - C2 A2: v4.2 passed an assertion the spec predicted it would fail
  - C3 A2: v4.2 passed an assertion the spec predicted it would fail
  - C4 A6: v4.2 passed an assertion the spec predicted it would fail
  - C5 A2: v4.2 passed an assertion the spec predicted it would fail
  - C6 A1: v4.2 passed an assertion the spec predicted it would fail
- [observed] All 12 arm runs report `model: claude-opus-5-5`. Each run's `model_usage` lists `["claude-haiku-5-5", "claude-opus-5-5"]`.
- [observed] `claude_code_version` in `probe.json` is `2.1.302` for all three folders. The prompt's isolation note was observed on 2.1.312, but isolation held on 2.1.302 (G3 PASS for all folders, and per-run isolation checks passed on all 12 arm runs).
- [observed] `claude_children_this_invocation`: 21, under the 40-child cap (3 probes + 12 arm runs + 6 grader runs, no retries).
- [observed] G6 `no bash` cause: `shutil.which('git')` returns `C:\Program Files\Git\mingw64\bin\git.EXE`. The runner's `find_bash` takes `parents[1] / "bin" / "bash.exe"`, which resolves to `C:\Program Files\Git\mingw64\bin\bash.exe`, and that path does not exist. Git Bash is installed. The runner's lookup path is wrong for this PATH layout.
- [observed] Both arms failed C3 A1, so F-2 is not a regression from v4.2. F-3 is the one assertion where v5.0 lost to v4.2 (C4 A6).
- [inferred] The `claude-haiku-5-5` entry in every arm's `model_usage` is most likely Claude Code's own background model use. Arm children had only `Skill,Read`, so they could not spawn subagents. Not confirmed from the stream.
- [inferred] Because v4.2 passed 7 assertions the spec predicted it would fail, the spec's §11 predictions overstate the v4.2 baseline gap. The measured differential (+6) is the number to use, not the predicted one.

## Not verified
- One sample per case per arm, so a one-assertion difference may be noise.
- Effort was the Claude Code default for Opus 5.5 and was not pinned.
- User-level CLAUDE.md may load into every child. This is the same for both arms.
- The grader is the same model as the arms.
- Hook execution covered only extractable bash scripts and the fixtures in the runner. In this run it covered nothing: all four G6 rows are `NOT_RUN` (`no bash`), so no generated hook was executed.
- The grader's "absent" verdicts for F-1 to F-3 were not checked against the v5.0 `.md` outputs. Per the prompt, this session did not read the outputs.
- The pasted prompt was not hashed. A copy exists at `design/audit-artifacts/v5.0/d9a/root_CC_d9a_cc-design_v5.0.md`, but this session did not confirm it is identical to the paste.
- The template in `rootnode-cc-design/references/cc-session-reports.md` §7 was read from the repo working tree at HEAD e336bce, not from either arm's installed copy.

## KF deltas
none from this run — the 5.0.1 cycle decides
