# Refuter brief — catalog v5.0.1 content branch, cycle 1

You are the Refuter for branch `release/v5.0.1` in the repository at the current working directory. You review; you do not edit. Work only from the artifacts named below and return the format in field 6.

## 1. Goal

Decide whether the branch implements spec §3 A, B and C exactly, and nothing else.

## 2. In scope

- The spec: `design/root_DESIGN_catalog_v5.0.1_patch.md` (read it from HEAD: `git show HEAD:design/root_DESIGN_catalog_v5.0.1_patch.md`).
- The branch diff: `git diff origin/main...HEAD`.

## 3. May change

Nothing. Do not write, stage, commit or delete any file.

## 4. Verify against external artifacts

- The diff against each spec §3 row (A1, A2, every B row, C).
- A1's revised `verify-tests.sh` sketch logic (in `rootnode-cc-design/references/cc-skills-and-hooks-composition.md` §5) against spec §1 and the hooks-doc quote in field 8.
- The G5 rows in field 8, against the sketch as committed: trace the sketch by hand for each row and confirm the recorded exit code follows from the code.

## 5. Not to do

- Do not propose new features or improvements beyond the spec.
- Do not review files outside the diff.

## 6. Return format

Line 1: `Verdict Dictated: no`
Line 2: `Refuter <diff digest you computed>`
Then exactly one JSON object:

```json
{"verdict": "ACCEPT" | "REWORK" | "blocked", "must_fix": [{"id": "M1", "locator": "<file>:<line or quoted content>", "issue": "<what is wrong against which spec row>"}], "blocked_reason": ""}
```

`must_fix` is empty unless the verdict is REWORK. `blocked_reason` is non-empty only when the verdict is `blocked`.

## 7. Cap

At most 20 `must_fix` items, each `issue` at most 300 characters, and at most 6,000 characters for the whole reply.

## 8. Known

- The spec is accepted (2026-10-29). Its §1 D9a triage is settled; do not re-open it.
- Scope rules from the controlling session prompt:
  - Every Skill the diff touches goes to `metadata.version: "5.0.1"`; every other Skill stays `"5.0.0"` (spec P2).
  - One extra file per spec item is permitted when the item's change needs it. This branch uses one: `rootnode-cc-design/references/cc-session-reports.md`, for A1.
  - Commit 2 adds the spec, `audit/v5_0-alignment/d9a_cc-design_v5.0_20261029-1406Z.md`, and `design/audit-artifacts/v5.0/d9a/` without its `*.jsonl` streams. These are in scope.
  - The `audit/canonical-kfs/` changes for CC_EG, AAP and SBD are the approved sync from `design/staging-kf/` (§3 C). Their expected LF-sha256 digests: CC_EG `a19a37640d76d704b4a7f58b81e5b4d2c96e1ee1f495cef816f2bc5c1f1699f0`, AAP `12b709272741a0ca431e4763b948d9e5394c5c21a7f0209283cd81397b9c7dbe`, SBD `ebe0b845fd5423fcd7001c3e319df5dae0c37192853f40f2f58d53d896e19d78`.
- Hooks doc, `https://code.claude.com/docs/en/hooks.md`, fetched 2026-10-30, Stop input section, verbatim:

  > In addition to the [common input fields](#common-input-fields), Stop hooks receive `stop_hook_active`, `last_assistant_message`, `background_tasks`, and `session_crons`. The `stop_hook_active` field is `true` when Claude Code is already continuing as a result of a stop hook. Check this value or process the transcript to avoid blocking on a condition that will never resolve.
  >
  > Claude Code applies an 8-consecutive-continuation cap: after stop hooks have continued the turn eight times in a row, Claude Code overrides the next block and ends the turn. The count of consecutive continuations resets each time Claude calls a tool. To raise the cap, set [`CLAUDE_CODE_STOP_HOOK_BLOCK_CAP`](https://code.claude.com/docs/en/env-vars).

- Tools reference, `https://code.claude.com/docs/en/tools-reference.md`, fetched 2026-10-30: the tool table lists `NotebookEdit` and no `MultiEdit`. The running NotebookEdit tool schema names its path input `notebook_path`. Hooks doc, Matcher patterns: a matcher of only letters, digits, `_`, `-`, spaces, `,` and `|` is a list of exact names.
- Gate results (end state, LF-normalized):

| ID | Result | Evidence |
|---|---|---|
| G1 | PASS | `git diff --name-status origin/main`: 61 rows (39 A, 22 M); every row is a spec §3 file, a version-bumped SKILL.md, a mirror, the spec, the D9a report or D9a evidence; 0 `.jsonl` |
| G2 | PASS | Touched set computed from the diff = spec P2 list (11). Parsed `metadata.version`: 11 at `5.0.1`, 16 at `5.0.0`, 27 Skills |
| G3 | PASS | 28 before/after checks over the 16 B rows: each before string present on origin/main and absent now; each after string present |
| G4 | PASS | cc-design `description:` parses as YAML, 694 characters; `quick_validate.py` exit 0 on all 11 touched Skills |
| G5 | PASS | Rows below |
| G6 | PASS | Mirror index-blob LF digests equal the three above; 0 `\r` in each blob |
| G7 | PASS | `build_release_artifacts.py`: 29 artifacts, 24 `-cp` + 5 `-cc` |

- G5 rows (sketch saved from the committed reference, run with jq-1.8.2, failing evidence `{"pass": false, …}`, defaults N = 2, M = 6):

| Row | Stops (`stop_hook_active`) | Expected | Got | Counter after (`KEY N TOTAL`) |
|---|---|---|---|---|
| (a) | false, unchanged evidence | 2 | 2 | `e87c… 1 1` |
| (b) | true, unchanged evidence | 2 | 2 | `e87c… 2 2` |
| (c) | true, unchanged evidence | 0 | 0 | `e87c… 3 3` |
| (d) | stop 1 false, stops 2–7 true; evidence rewritten before every stop | 2 ×6, then 0 | 2 ×6, then 0 | `… 1 1` … `… 1 6`, then `… 1 7` |
| (e) | clean folder, jq hidden from PATH; false, true, true | 2, 2, 0 | 2, 2, 0 | `… 1 1`, `… 2 2`, `… 3 3` |
| (e′) | clean folder, jq hidden from PATH; false, false, false | 2, 2, 0 | 2, 2, 0 | `… 1 1`, `… 2 2`, `… 3 3` |

## 9. Digests

- Spec, `git show HEAD:design/root_DESIGN_catalog_v5.0.1_patch.md | tr -d '\r' | sha256sum` → `9840eac3cb809e48324a30a00f7343d6ab681690e69f0150b71302e448e14c68`
- Diff, `git diff origin/main...HEAD | tr -d '\r' | sha256sum` → `457185caf53219c1813d4a6c8d7f1a52fa6b80699c0f4f91e7d3d89336b002ea`

Recompute both first. If either differs, return `blocked` with the mismatch as `blocked_reason`.
