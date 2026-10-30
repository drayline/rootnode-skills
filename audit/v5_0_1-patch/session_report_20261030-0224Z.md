---
prompt: root_CC_build_catalog_v5.0.1_rev2 (pasted inline; no file on disk; digest not computed)
outcome: COMPLETED
started: 2026-10-30T02:08Z
ended: 2026-10-30T02:24Z
---

# Session report — catalog v5.0.1 rev 2 build (fold all identified items into PR #28)

Phase 3 closed. PR #28 (`release/v5.0.1` → `main`) is OPEN at head `4538de014e2e3640c3e60045379aa0b6e3502127`. The Refuter returned ACCEPT in cycle 1 of 2, bound to diff digest `433bd4ec1dba5fc1b1370405ad2429d432fa62bab9b209b6f036bca70605a70c`. No halt fired.

## Pre-state (report-only)

| Branch | HEAD | Dirty paths |
|---|---|---|
| release/v5.0.1 | `6a257f9f73305b7ef248cc5d353f1cc2bd04b5a2` | 15 |

- `claude --version`: 2.1.302 (Claude Code). `jq --version`: jq-1.8.2, now on this session's PATH (F-1 and F-H3 cleared by the restart).
- **Interpreter:** `py -3 --version` = Python 3.14.3, so `py -3` was used for every Python run (G2, G4, G7, the G1 classifier, and the G8 replacement). `python` would have resolved to Python 3.12.13 (LibreOffice's bundled copy; F-5). PyYAML 6.0.3 is present under `py -3`.
- After `git switch release/v5.0.1` (already on it) and `git pull --ff-only` (already up to date), HEAD was `6a257f9f73305b7ef248cc5d353f1cc2bd04b5a2`.

**H0 / H1 / H3**

| Check | Command | Result | Evidence |
|---|---|---|---|
| H0 PR | `gh pr view 28 --json state,headRefOid` | clear | `{"headRefOid":"6a257f9f73305b7ef248cc5d353f1cc2bd04b5a2","state":"OPEN"}` |
| H0 main | `git rev-parse origin/main` (after `git fetch origin`) | clear | `e336bce54941a6b0ec0fae01f8dbcc9261324b37` |
| H1 spec rev 2 | `tr -d '\r' < design/root_DESIGN_catalog_v5.0.1_patch.md \| sha256sum` | clear | `1be89609b35d04818ae5be3412f2b650e85449ae1f4e168d2b2a00ca3e9e1be9` |
| H1 CC_EG staged | same | clear | `0995dfff3dedbaeb71f57cd500f6f0843e3356d0e3a0cd9b05746911bd1de619` |
| H1 AEA staged | same | clear | `82853f6d50c8cc885e20ce04497228809fc3ea5f2e3f162e06aee15eb2306a8a` |
| H1 playbook staged | same | clear | `b0b3e96213ef508c7e194c4b5d8d87ec297f1dae61877b7ad547c783b2623584` |
| H1 README staged | same | clear | `f379645503a01965ec47bc3c77cfc0216bc45f5b2e8f91fddaec11489edbc333` |
| H3 jq | `jq --version` | clear | `jq-1.8.2` |

## Post-state

HEAD: `4538de014e2e3640c3e60045379aa0b6e3502127` (= `origin/release/v5.0.1`). New commits:
- `0cab5c8`, commit 3: `fix: catalog v5.0.1 rev 2 — …`, 17 files.
- `4538de0`, commit 4: `docs(audit): v5.0.1 build report and review files; v4.2 inventory report`, 4 files.

| File | LF-sha256 (index blob at HEAD) | Expected (prompt) | Match |
|---|---|---|---|
| `design/root_DESIGN_catalog_v5.0.1_patch.md` | `1be89609b35d04818ae5be3412f2b650e85449ae1f4e168d2b2a00ca3e9e1be9` | H1 spec | yes |
| `audit/canonical-kfs/root_CC_ENVIRONMENT_GUIDE.md` | `0995dfff3dedbaeb71f57cd500f6f0843e3356d0e3a0cd9b05746911bd1de619` | H1 CC_EG | yes |
| `audit/canonical-kfs/root_AGENT_ENVIRONMENT_ARCHITECTURE.md` | `82853f6d50c8cc885e20ce04497228809fc3ea5f2e3f162e06aee15eb2306a8a` | H1 AEA | yes |
| `docs/root_SKILLS_RELEASE_PLAYBOOK.md` | `b0b3e96213ef508c7e194c4b5d8d87ec297f1dae61877b7ad547c783b2623584` | H1 playbook | yes |
| `README.md` | `f379645503a01965ec47bc3c77cfc0216bc45f5b2e8f91fddaec11489edbc333` | H1 README | yes |

## Files changed — 76 rows

`git diff --name-status origin/main`: 76 rows, 43 A and 33 M. 21 rows are §8, 18 are §3, and 37 are D9a evidence (21 + 18 + 37 = 76). The 61 rev 1 rows are unchanged in status, as listed in `session_report_20261030-0040Z.md`. Commit 3 added 11 rows and commit 4 added 4 (61 + 11 + 4 = 76).

Rows touched by rev 2 (17 + 4 = 21, which is the §8 class):

| Status | File | Category |
|---|---|---|
| M | `README.md` | §8.2 README (Tier 1, operator approves at merge) |
| M | `audit/canonical-kfs/root_AGENT_ENVIRONMENT_ARCHITECTURE.md` | §8.2 mirror (new row) |
| M | `audit/canonical-kfs/root_CC_ENVIRONMENT_GUIDE.md` | §3 C + §8.2 mirror |
| M | `build_release_artifacts.py` | §8.3 `CATALOG_VERSION` |
| A | `design/root_DESIGN_catalog_v5.0.1_patch.md` | spec, rev 2 |
| M | `docs/root_SKILLS_RELEASE_PLAYBOOK.md` | §8.2 playbook D1/D2 |
| M | `rootnode-cc-design/references/cc-prompt-design-patterns.md` | §3 A2/F21 + §8.1 R5 |
| M | `rootnode-cc-design/references/cc-skills-and-hooks-composition.md` | §3 A1/F27–F29 + §8.1 R1, R4 |
| M | `rootnode-cc-design/references/troubleshooting.md` | §8.1 R2 |
| M | `rootnode-critic-gate/SKILL.md` | §3 B F19 + version + §8.1 R3 |
| M | `rootnode-critic-gate/references/checks-detailed.md` | §8.1 R3 |
| M | `rootnode-handoff-trigger-check/SKILL.md` | §3 B F17 + version + §8.1 R3 |
| M | `rootnode-handoff-trigger-check/references/examples.md` | §8.1 R3 |
| M | `rootnode-handoff-trigger-check/references/troubleshooting.md` | §8.1 R3 |
| M | `rootnode-mode-router/SKILL.md` | §8.1 R3 + version 5.0.1 |
| M | `rootnode-mode-router/references/trigger-types-detailed.md` | §8.1 R3 |
| M | `rootnode-mode-router/references/troubleshooting.md` | §8.1 R3 |
| A | `audit/v5_0_1-patch/session_report_20261030-0040Z.md` | §8.3 |
| A | `audit/v5_0_1-patch/refuter_brief_c1.md` | §8.3 |
| A | `audit/v5_0_1-patch/refuter_c1.json` | §8.3 |
| A | `design/audit-artifacts/v4.2/v42_inventory_report.md` | §8.3 |

**In scope with notification:** none used in rev 2; every change landed in the file its §8.1 row names.

**Untracked, not committed:**
- `audit/v5_0_1-patch/`: this report, `refuter_brief_r2c1.md`, `refuter_r2c1.json`, and `session_report_20261030-0107Z.md` (the H3-halted run; not on the commit-4 list).
- `design/audit-artifacts/v4.2/scratch/` (out of scope per the prompt), plus `root_CC_DESIGN_v42_spec.md` and `root_CC_LANDSCAPE_20260911.md` (not on the commit-4 list).
- The 12 `design/audit-artifacts/v5.0/d9a/out/runs/*/C*.jsonl` streams.
- `design/staging-kf/PR_BODY_v5.0.1.md` (gitignored).
- `dist/` (gitignored).

## Gates

| ID | Command | Result | Evidence |
|---|---|---|---|
| G1 | `git diff --name-status origin/main`, each row classified against spec §3/§8 (script under `py -3`) | PASS | 76 rows; 0 unexpected; 0 `.jsonl` |
| G2 | Touched set from `git diff --name-only origin/main -- ':(glob)rootnode-*/**'` (25 matches); parsed `metadata.version` of all 27 `SKILL.md` | PASS | Touched set = P2 + mode-router (12), 0 differences. 12 × `5.0.1`, 15 × `5.0.0`, 0 mismatches |
| G3 | Staged diff lines; `git grep -c handoff-gate -- ':(glob)rootnode-*/**'` | PASS | Rows below |
| G4 | `py -3 rootnode-skill-builder/scripts/quick_validate.py rootnode-<s>` × 12; YAML-parsed description length | PASS | 12 × exit 0, "Skill is valid!"; cc-design `description:` 694 characters |
| G5 | Sketch extracted from the composition reference (0 `\r`, `bash -n` OK); harness at N=2, M=6, jq-1.8.2; jq hidden by PATH filter for rows (e)/(e′) | PASS | 16 of 16 rows; rows below |
| G5b | Guard extracted from the composition reference (0 `\r`, `bash -n` OK); 35 fixture rows (24 from rev 1 + 11 new) in a folder with decoys `mig_decoy` and `migrations_backup/` | PASS | 35 of 35; 22 audit rows written (= the 22 expected-2 rows); `.claude/` created by the guard |
| G6 | `git show :<path> \| tr -d '\r' \| sha256sum`; `git rev-parse :<p>` vs `6a257f9:<p>`; `\r` count per staged blob | PASS | Four digests equal H1 (Post-state); AAP `cfff4a31…` and SBD `db6bbdc8…` unchanged; 0 `\r` in 17 + 4 committed blobs |
| G7 | `py -3 build_release_artifacts.py` | PASS | exit 0; "29 artifacts: 24 -cp (flat) + 5 -cc (wrapper)"; `dist/rootnode-catalog-v5.0.1.zip` holds 29 entries (24 `-cp`, 5 `-cc`) |
| G8 | Regex scan of the 4 commit-4 files (API keys, GitHub/Slack/AWS/Google tokens, private keys, bearer tokens, emails, `C:\Users\<name>`, `C:/Users/<name>`, `/c/Users/<name>`, the username anywhere) | PASS | 0 keys or tokens, 0 emails. Replacements: `session_report_20261030-0040Z.md` 1 (`C:\Users\<name>` → `%USERPROFILE%`), `refuter_brief_c1.md` 0, `refuter_c1.json` 0, `v42_inventory_report.md` 0. After replacement: 0 username hits |

**G3 rows**

| Row | File | Before → after |
|---|---|---|
| R1 | `cc-skills-and-hooks-composition.md` | After L291 `MAX_TOTAL=…`, new L292: `# Keep M at or below CLAUDE_CODE_STOP_HOOK_BLOCK_CAP (default 8) when stops can repeat without a tool call between them.` New paragraph at the end of "Bounded Stop hooks" (L345): "Claude Code also caps stop-hook continuations on the host side: …". The 634-character paragraph is found verbatim in the CC_EG §6 index blob (`grep -cF` = 1) |
| R2 | `rootnode-cc-design/references/troubleshooting.md` L82 | Before: "(`stop_hook_active`, no-progress cap)". After: "(chain-scoped by `stop_hook_active`; no-progress and chain-total caps; Claude Code's own continuation cap — composition reference §5)" |
| R3 | 9 sites, 8 files | Before: 9 `handoff-gate` hits (`critic-gate/SKILL.md:214`, `checks-detailed.md:199`, `handoff-trigger-check/SKILL.md:82`, `examples.md:3`, `examples.md:142`, `handoff-trigger-check/references/troubleshooting.md:3`, `mode-router/SKILL.md:105`, `trigger-types-detailed.md:191`, `mode-router/references/troubleshooting.md:45`). After: `git grep -c` prints nothing, over a pathspec matching 155 tracked files. Cross-Skill sites → `` `rootnode-handoff-trigger-check` ``; own-file sites → "the handoff trigger check". No "(if available)" was added: each site names a consumer, a comparison or a methodology citation, not a dependency |
| R4 | `cc-skills-and-hooks-composition.md` L218 | Before: `"matcher": "Edit|Write|NotebookEdit|Bash"`. After: `"matcher": "Edit|Write|NotebookEdit|Bash|PowerShell"`. The header comment (L234) changed to match. The guard body was rewritten for (a)–(c) |
| R5 | `cc-prompt-design-patterns.md` L410 | The shell paragraph gains the three sentences, tagged `[observed: v5.0 catalog generator (Observation 30) and the v5.0.1 build, 2026-10-30]`, plus the `claude -p` allow-list sentence tagged `[observed, Claude Code 2.1.302]` |

**G5 rows** (exit codes equal the first build's; keys differ because the evidence bytes differ)

| Row | Stops (`stop_hook_active`) | Expected | Got | Counter after |
|---|---|---|---|---|
| (a) | false, unchanged | 2 | 2 | `25ff80f492a7f9ba 1 1` |
| (b) | true, unchanged | 2 | 2 | `… 2 2` |
| (c) | true, unchanged | 0 | 0 | `… 3 3` |
| (d1) | false, evidence rewritten | 2 | 2 | `a4d6fb02ab0cc2eb 1 1` |
| (d2)–(d6) | true, rewritten each stop | 2 each | 2 each | N = 1; TOTAL 2…6 |
| (d7) | true, rewritten | 0 | 0 | `a3ffd77996e96854 1 7` |
| (e1)–(e3) | jq hidden (`command -v jq` empty); false, true, true | 2, 2, 0 | 2, 2, 0 | `1 1`, `2 2`, `3 3` |
| (e′1)–(e′3) | jq hidden; false, false, false | 2, 2, 0 | 2, 2, 0 | `1 1`, `2 2`, `3 3` |

**G5b rows** (expected = got on every row)

| # | Tool | Input | Exp | Got |
|---|---|---|---|---|
| 1 | Bash | `rm -rf migrations` | 2 | 2 |
| 2 | Bash | `rm migrations/0001.sql` | 2 | 2 |
| 3 | Bash | `find migrations -delete` | 2 | 2 |
| 4 | Bash | `find . -path './migrations/*' -delete` | 2 | 2 |
| 5 | Bash | `find db/migrations -name x -exec rm {} +` | 2 | 2 |
| 6 | Bash | `cd migrations && rm 0001.sql` | 2 | 2 |
| 7 | Bash | `cd db/migrations; rm -rf *` | 2 | 2 |
| 8 | Bash | `rm -rf mig*` | 2 | 2 |
| 9 | Bash | `rm -rf ./m*` | 2 | 2 |
| 10 | Bash | `mv m* /tmp` | 2 | 2 |
| 11 | Bash | `rm -rf */mig*` | 2 | 2 |
| 12 | Bash | `echo rm migrations` (accepted false positive) | 2 | 2 |
| 13 | Edit | `migrations/x.sql` | 2 | 2 |
| 14 | Edit | `C:\repo\migrations\x.sql` | 2 | 2 |
| 15 | NotebookEdit | `/repo/migrations/a.ipynb` | 2 | 2 |
| 16 | Bash | `rm -rf migrations_backup` | 0 | 0 |
| 17 | Bash | `rm -rf src/*` | 0 | 0 |
| 18 | Bash | `rm *.tmp` | 0 | 0 |
| 19 | Bash | `ls mig*` | 0 | 0 |
| 20 | Bash | `cd migrations_backup && rm x` | 0 | 0 |
| 21 | Bash | `find . -name '*.pyc' -delete` | 0 | 0 |
| 22 | Bash | `cat migrations/0001.sql` | 0 | 0 |
| 23 | NotebookEdit | `/repo/nb/a.ipynb` | 0 | 0 |
| 24 | Write | `src/x.py` | 0 | 0 |
| 25 | Bash | `find . -delete` | 2 | 2 |
| 26 | Bash | `find / -delete` | 2 | 2 |
| 27 | Bash | `find -delete` | 2 | 2 |
| 28 | Bash | `ls mig* ; rm -rf mig*` | 2 | 2 |
| 29 | PowerShell | `Remove-Item -Recurse migrations` | 2 | 2 |
| 30 | PowerShell | `remove-item .\migrations\0001.sql` | 2 | 2 |
| 31 | PowerShell | `Move-Item m* C:\tmp` | 2 | 2 |
| 32 | Bash | `find . -name '*.pyc' -delete` (repeat of row 21; the prompt lists it in both sets) | 0 | 0 |
| 33 | Bash | `ls m* && rm x` | 0 | 0 |
| 34 | PowerShell | `Remove-Item src\x.py` | 0 | 0 |
| 35 | PowerShell | `Get-ChildItem m*` | 0 | 0 |

Extra probes, not gate rows:
- These block (2): `sudo rm -rf mig*`, `if true; then rm -rf mig*; fi`, `(rm -rf mig*)`, `X=1 rm -rf mig*`, `find ~ -exec rm {} \;`, `find .. -exec mv {} /tmp \;`, `find . -type f -delete`, `git rm -r mig*` (after the `git` prefix fix), PowerShell `RI -r migrations`, `del M*`, `Set-Location migrations; Remove-Item *`.
- These are allowed (0): `find src -delete`, `git log m*`.
- These are gaps (0, should block): `rm -rf ../mig*` and PowerShell `Get-ChildItem migrations | Remove-Item` (F-10, F-11).

## R4(b) tools-reference quote

`https://code.claude.com/docs/en/tools-reference.md`, fetched 2026-10-30 (HTTP 200, 87,846 bytes):

> | `PowerShell` | Executes PowerShell commands natively. See [PowerShell tool](#powershell-tool) for availability | Yes |

> Your [PreToolUse hooks](https://code.claude.com/docs/en/hooks.md#powershell) receive the tool's command string in `tool_input.command`, with the same fields as the Bash tool.

> Match `Bash|PowerShell` in hooks that inspect shell commands; the [PowerShell hook input section](https://code.claude.com/docs/en/hooks.md#powershell) explains why matching `Bash` alone is not enough.

The tool name is `PowerShell`, and the command field is `tool_input.command`. The guard's existing jq path already reads that field, so only the matcher and the verb set changed. `MultiEdit` appears 0 times in the tools reference (re-checked). The hooks doc (`https://code.claude.com/docs/en/hooks.md`, fetched 2026-10-30, 283,477 bytes) has a PowerShell input table with `command` as a field. L2746 of the same doc carries the 8-consecutive-continuation cap quoted for R1.

## Refuter cycles

| Cycle | Verdict | Diff digest | Must-fix IDs | Run |
|---|---|---|---|---|
| r2c1 | ACCEPT | `433bd4ec1dba5fc1b1370405ad2429d432fa62bab9b209b6f036bca70605a70c` (the Refuter's line 2 equals the Builder's) | none | `claude -p --model claude-opus-5-5 --effort high --setting-sources project,local --tools "Read,Grep,Glob,Bash"`, allow-list `git diff/show/log/grep`, `tr`, `sha256sum`; 31 turns, $6.82, 0 permission denials; first line "Verdict Dictated: no" |

- Brief: `audit/v5_0_1-patch/refuter_brief_r2c1.md`, with ten fields and the shell rule "one pipeline per Bash call". Output: `audit/v5_0_1-patch/refuter_r2c1.json`.
- What the Refuter reported doing:
  - traced all 35 guard rows by hand;
  - recomputed the four synced-file digests itself (F-4 closed);
  - confirmed R1 verbatim;
  - accepted the R3 no-"(if available)" judgment;
  - accepted the `git` prefix extension beyond the R4 text.
- **Receipt freeze:** the diff digest was recomputed after the verdict and before `git push`, and it was unchanged. No reviewed file was written after the ACCEPT.
- Cycle 2 was not needed. The Agent tool was not used, and no Skill was invoked.

## Findings

| ID | Severity | Locator | Status | Owner |
|---|---|---|---|---|
| F-1 | low | Environment: `jq` | closed (on PATH after restart) | operator |
| F-H3 | blocker | Session PATH (0107Z run) | closed | operator |
| F-2 | medium | Build prompt pathspec `'rootnode-*/'` | closed (prompt rule + R5 text) | chat |
| F-3 | medium | Build prompt untracked-folder staging | closed (explicit lists; R5 text) | chat |
| F-4 | low | Refuter allow-list | closed (0 denials in r2c1) | chat |
| F-5 | low | Environment: `python` | mitigated (`py -3` used; R5 text) | operator |
| F-6 | low | `rootnode-cc-design/references/troubleshooting.md:82` | closed by R2 | — |
| F-7 | low | "handoff-gate" outside cc-design | closed by R3 | — |
| F-8 | low | Guard sketch gaps | closed by R4 | — |
| F-9 | medium | Host Stop-hook cap | closed by R1 + CC_EG sync | — |
| F-10 | low | `cc-skills-and-hooks-composition.md` §4 guard, glob candidates | next patch | chat |
| F-11 | low | Same guard, pipeline-fed deletes | next patch | chat |
| F-12 | low | Spec §4 G5 wording | note for spec author | chat |
| F-13 | low | `audit/v5_0_1-patch/session_report_20261030-0107Z.md` and two `design/audit-artifacts/v4.2/` files untracked | operator decision | operator |
| F-14 | low | Sketch default `MAX_TOTAL = 3×N` | next design cycle | chat |

- **F-10.** `rm -rf ../mig*` is not caught. The glob candidates are `migrations`, `./migrations` and `x/migrations`, with no `../migrations`. This was a gap before rev 2 too. Next-patch block: add `../migrations` to the candidate list.
- **F-11.** Deletes fed by a pipe are not caught: PowerShell `Get-ChildItem migrations | Remove-Item`, and by analogy Bash `ls migrations | xargs rm`. The delete segment has no migrations word, and the listing segment's command is not a delete. Next-patch block: treat a delete or move segment that reads from a pipe as covering the previous segment's path words.
- **F-12.** Spec §4 G5 says "2 further `true` stops on unchanged evidence block, then the next releases". The sketch at N = 2 blocks on the `false` stop and one `true` stop, then releases. The Refuter and both builds read A1's "N blocks" and "release when `N > MAX`" as controlling. Read literally, G5 would mean three blocks.
- **F-13.** The prompt's commit-4 list names only the 0040Z report, the c1 Refuter files and `v42_inventory_report.md`. The H3-halted run's report (0107Z) and `design/audit-artifacts/v4.2/root_CC_DESIGN_v42_spec.md` and `root_CC_LANDSCAPE_20260911.md` remain untracked. Whether they ride the release closeout is the operator's decision.
- **F-14.** With the unattended N = 8, the default M = 24 exceeds the host cap of 8. R1 adds the comment the spec asked for; the default itself is unchanged. A design cycle could default M to `min(3×N, CLAUDE_CODE_STOP_HOOK_BLOCK_CAP)`.

## Operator decisions

None this session. The only operator input was the pasted build prompt.

## Observations

- [observed] Built-in safety check: a cleanup `rm -rf "$W"` on a scratch-folder variable was denied. The harness then used fresh, uniquely named folders and removed nothing. Scratch folders remain under the session scratchpad.
- [observed] A `sed` replacement of `C:\Users\<name>` silently did not apply because of backslash escaping. The count check, also mis-escaped, reported 0 remaining. A fixed-string `grep -cF` exposed the mismatch, and a literal byte replacement in Python fixed it. Same lesson as AEA §4.14: an instrument that cannot express the pattern returns a null that falsifies nothing.
- [observed] The first R4 draft scoped the glob rule by segment command (rule (c)). That let `git rm -r mig*` through, which the pre-rev-2 guard blocked. Adding `git` to the segment-prefix skip list closed it, and all 35 rows were re-run afterwards (35 of 35).
- [inferred] The R1 paragraph is placed at the end of the "Bounded Stop hooks" subsection, after "The block reason…", reading "append" literally. The Refuter did not object.
- [observed] `gh pr view 28 --json body` equals the body file, LF-normalized, apart from one trailing newline.

## Not verified

- Live hook behavior: the guard and the Stop sketch ran as standalone scripts against JSON fixtures, not as hooks in a running Claude Code session, and not under the PowerShell tool itself.
- The rendered PR page: the body was checked as stored, not in a browser.
- Build prompt digest: not computed, because the prompt was pasted with no file.
- The CI half of spec §3 C (seed Project custom instructions) is outside this repo.

## KF deltas

- **Synced this cycle (§8.2):** `audit/canonical-kfs/root_CC_ENVIRONMENT_GUIDE.md` (`0995dfff…`; §6 host-cap paragraph, §9 R3 naming) and `audit/canonical-kfs/root_AGENT_ENVIRONMENT_ARCHITECTURE.md` (`82853f6d…`; §6.3 R3 naming). This is the approved sync under repo halt #5.
- **New KF block:** none. F-10, F-11 and F-14 are Skill-content items (cc-design composition reference). No KF text in `audit/canonical-kfs/` carries the guard sketch; the CC_EG §6 Stop-hook text already names the host cap.

Phase 3 closed; PR #28 updated. Merge it, then ask chat for the v5.0.1 release prompt.
