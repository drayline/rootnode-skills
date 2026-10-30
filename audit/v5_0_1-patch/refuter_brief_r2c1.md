# Refuter brief — catalog v5.0.1 content branch, rev 2, cycle 1

You are the Refuter for branch `release/v5.0.1` in the repository at the current working directory. You review; you do not edit. Work only from the artifacts named below and return the format in field 6.

**Shell rule.** Run one pipeline per Bash call. Do not use loops, `&&` or `||` chains, `;`, or subshells; they are denied. Allowed commands: `git diff`, `git show`, `git log`, `git grep`, `tr`, `sha256sum`. Example of an allowed call: `git show HEAD:README.md | tr -d '\r' | sha256sum`. Prefer Read, Grep and Glob for reading files.

## 1. Goal

Decide whether the branch implements spec §3 and §8 exactly, and nothing else, over the full diff `git diff origin/main...HEAD`. The earlier ACCEPT (cycle 1 of the first build, diff digest `457185ca…`) was bound to a smaller diff and no longer holds. Review the whole diff, not only the rev 2 commits.

## 2. In scope

- The spec: `design/root_DESIGN_catalog_v5.0.1_patch.md`, rev 2. Read it from HEAD: `git show HEAD:design/root_DESIGN_catalog_v5.0.1_patch.md`. §8 is new in rev 2.
- The branch diff: `git diff origin/main...HEAD` (4 commits: `a88d449`, `6a257f9`, `0cab5c8`, `4538de0`).
- The staged sources for the synced files: `design/staging-kf/root_CC_ENVIRONMENT_GUIDE.md`, `root_AGENT_ENVIRONMENT_ARCHITECTURE.md`, `root_SKILLS_RELEASE_PLAYBOOK.md`, `README.md` (on disk, untracked; read with Read).

## 3. May change

Nothing. Do not write, stage, commit or delete any file.

## 4. Verify against external artifacts

- The diff against every spec §3 row (A1, A2, each B row, C) and every §8 row (R1–R5, §8.2, §8.3).
- R1: the paragraph appended to `rootnode-cc-design/references/cc-skills-and-hooks-composition.md` §5 "Bounded Stop hooks" is verbatim from CC_EG §6 (the "Claude Code also caps stop-hook continuations…" sentences), and the sketch comment names `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP` (default 8).
- R3: `git grep -c handoff-gate -- ':(glob)rootnode-*/**'` prints nothing; each replacement follows the R3 rule (another Skill → `rootnode-handoff-trigger-check`; inside handoff-trigger-check's own files → "the handoff trigger check").
- R4: trace the guard in composition §4 by hand for each G5b row in field 8 and confirm the recorded exit code follows from the code. Check (a), (b) and (c) of R4 against the code, and the matcher line against the tools-reference quote in field 8.
- §8.2: the four synced files' LF digests at HEAD equal the digests in field 8.
- Versions: 12 touched Skills at `5.0.1` (spec P2 list plus mode-router, per §8.1), 15 at `5.0.0`.

## 5. Not to do

- Do not propose new features or improvements beyond the spec.
- Do not review files outside the diff, except the staged sources named in field 2.
- Do not re-open the spec's §1 triage or its decisions.

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

- The spec is accepted (2026-10-29; rev 2 the same day). The operator directed that every identified item ship in this cut (§8 preamble).
- Scope rules from the controlling session prompt:
  - Touched Skills go to `metadata.version: "5.0.1"`; every other Skill stays `"5.0.0"`.
  - One extra file per spec row is permitted when the row's change needs it. The first build used one, `rootnode-cc-design/references/cc-session-reports.md`, for A1. Rev 2 uses none.
  - Commit 2 adds the spec, the D9a report, and `design/audit-artifacts/v5.0/d9a/` without its `*.jsonl` streams. Commit 4 adds the first build's report and Refuter files and `design/audit-artifacts/v4.2/v42_inventory_report.md` (§8.3). One user-home path in that report was replaced with `%USERPROFILE%` (secret scan).
  - `audit/canonical-kfs/` changes are the approved sync from `design/staging-kf/` (repo halt #5). README is Tier 1; the operator approves it at merge.
- Builder disclosures (judge them; do not take them as settled):
  - R1: the host-cap paragraph is appended at the end of the "Bounded Stop hooks" subsection, after "The block reason…" line.
  - R3: no site was judged to read as a dependency of its host Skill. Each names a consumer of mode-router output, a verdict comparison, or a methodology citation, so no "(if available)" was added.
  - R4: besides (a)–(c), the segment-prefix skip list includes `sudo`, `command`, `env`, `nohup`, `time`, `git`, `then`, `do`, `else`, `!` and `VAR=value`, and the segment split also breaks on `( ) { }` and backtick. Without the skip list, rule (c) would let `sudo rm -rf mig*` and `git rm -r mig*` through, where the pre-rev-2 guard blocked them. The PowerShell `cd` rule also uses `chdir`, `sl`, `Set-Location` and `Push-Location`.
- Tools reference, `https://code.claude.com/docs/en/tools-reference.md`, fetched 2026-10-30, verbatim:
  - Tool table: "| `PowerShell` | Executes PowerShell commands natively. See [PowerShell tool](#powershell-tool) for availability | Yes |"
  - PowerShell tool section: "Your [PreToolUse hooks](https://code.claude.com/docs/en/hooks.md#powershell) receive the tool's command string in `tool_input.command`, with the same fields as the Bash tool." and "Match `Bash|PowerShell` in hooks that inspect shell commands".
  - The tool table lists no `MultiEdit`.
- Hooks doc, `https://code.claude.com/docs/en/hooks.md`, fetched 2026-10-30, Stop input section, verbatim:

  > Claude Code applies an 8-consecutive-continuation cap: after stop hooks have continued the turn eight times in a row, Claude Code overrides the next block and ends the turn. The count of consecutive continuations resets each time Claude calls a tool. To raise the cap, set [`CLAUDE_CODE_STOP_HOOK_BLOCK_CAP`](https://code.claude.com/docs/en/env-vars).

- Synced-file LF digests (expected at HEAD): CC_EG `0995dfff3dedbaeb71f57cd500f6f0843e3356d0e3a0cd9b05746911bd1de619`, AEA `82853f6d50c8cc885e20ce04497228809fc3ea5f2e3f162e06aee15eb2306a8a`, playbook `b0b3e96213ef508c7e194c4b5d8d87ec297f1dae61877b7ad547c783b2623584`, README `f379645503a01965ec47bc3c77cfc0216bc45f5b2e8f91fddaec11489edbc333`. AAP and SBD are unchanged from `6a257f9`.
- Gate results (end state, LF-normalized):

| ID | Result | Evidence |
|---|---|---|
| G1 | PASS | `git diff --name-status origin/main`: 76 rows (43 A, 33 M) = 21 §8 rows + 18 §3 rows + 37 D9a evidence; 0 unexpected; 0 `.jsonl` |
| G2 | PASS | Touched set from the diff = P2 list + mode-router (12). Parsed `metadata.version`: 12 at `5.0.1`, 15 at `5.0.0`, 27 Skills |
| G3 | PASS | R1, R2, R5 before/after lines; R3 `git grep -c` prints nothing; R4 matcher `Edit|Write|NotebookEdit|Bash|PowerShell` |
| G4 | PASS | `quick_validate.py` exit 0 on all 12; cc-design `description:` 694 characters |
| G5 | PASS | Stop sketch rows (a)–(e′) give the same exit codes as the first build (N = 2, M = 6) |
| G5b | PASS | Guard rows below, 35 of 35 |
| G6 | PASS | Digests above; 0 `\r` in every committed blob of commits 3 and 4 |
| G7 | PASS | Packager: 29 artifacts, 24 `-cp` + 5 `-cc`; `dist/rootnode-catalog-v5.0.1.zip` holds 29 zips |
| G8 | PASS | Commit 4 files: 0 keys or tokens, 0 email addresses, 1 home path replaced |

- G5b rows (guard extracted from the committed reference; JSON `{"tool_name": T, "tool_input": {field: value}}`; expected exit code first):
  - Expected 2: Bash `rm -rf migrations`, `rm migrations/0001.sql`, `find migrations -delete`, `find . -path './migrations/*' -delete`, `find db/migrations -name x -exec rm {} +`, `cd migrations && rm 0001.sql`, `cd db/migrations; rm -rf *`, `rm -rf mig*`, `rm -rf ./m*`, `mv m* /tmp`, `rm -rf */mig*`, `echo rm migrations`, `find . -delete`, `find / -delete`, `find -delete`, `ls mig* ; rm -rf mig*`; Edit `migrations/x.sql`, Edit `C:\repo\migrations\x.sql`; NotebookEdit `/repo/migrations/a.ipynb`; PowerShell `Remove-Item -Recurse migrations`, `remove-item .\migrations\0001.sql`, `Move-Item m* C:\tmp`.
  - Expected 0: Bash `rm -rf migrations_backup`, `rm -rf src/*`, `rm *.tmp`, `ls mig*`, `cd migrations_backup && rm x`, `find . -name '*.pyc' -delete` (listed twice in the prompt; run twice), `cat migrations/0001.sql`, `ls m* && rm x`; NotebookEdit `/repo/nb/a.ipynb`; Write `src/x.py`; PowerShell `Remove-Item src\x.py`, `Get-ChildItem m*`.
  - Every row: expected = got.

## 9. Digests

- Spec, `git show HEAD:design/root_DESIGN_catalog_v5.0.1_patch.md | tr -d '\r' | sha256sum` → `1be89609b35d04818ae5be3412f2b650e85449ae1f4e168d2b2a00ca3e9e1be9`
- Diff, `git diff origin/main...HEAD | tr -d '\r' | sha256sum` → `433bd4ec1dba5fc1b1370405ad2429d432fa62bab9b209b6f036bca70605a70c`

Recompute both first, one call each. If either differs, return `blocked` with the mismatch as `blocked_reason`.
