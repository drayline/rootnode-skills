# root_DESIGN_catalog_v5.0.1_patch — catalog patch after the v5.0 D9a

Status: ACCEPTED 2026-10-29. Rev 2 (2026-10-29) adds §8: everything the build and its review identified, folded into the same cut before release. Rev 3 (2026-10-29) adds §9: the rev 2 build's findings, then freezes the cut. Inputs:
- the D9a report `audit/v5_0-alignment/d9a_cc-design_v5.0_20261029-1406Z.md` and its `out/` folder;
- the 16 open findings in `audit/v5_0-alignment/session_report_20261023-0042Z.md` (final list at its line 415);
- the product facts verified in this cycle (§6).

## 1. D9a triage — test defects versus Skill defects

The D9a run graded v5.0 at 23/26 against v4.2 at 17/26. That result stands as measured: one sample per case, with C4 (+4) the only strong signal. Chat reviewed the three v5.0 misses against the outputs, the run streams, and execution of the generated hooks.

| D9a finding | Verdict | Evidence | Action |
|---|---|---|---|
| F-1 C2 A5: no continuation phrase per halt | **Test defect.** The request was an unattended run, and continuation phrases apply when an operator answers a halt (CC_EG §5.6). | v5.0 C2 output: "UNATTENDED RUN… When a halt trigger fires, write the halt note and the session report, then stop." | A2 (low): the autonomous template says how a halted unattended run resumes |
| F-2 C3 A1: Stop hook does not release when `stop_hook_active` is true | **Test defect that exposed a Skill defect.** Both arms read the field and bounded the block with a cap. Run here on 8 repeated failing stops: v4.2 releases after 3 blocks; v5.0 releases after 2 identical failures. The v5.0 Skill's own sketch exits 0 on the first `true`, so a hook can block only once per stop chain. Its no-progress cap ("2 interactive, 8 unattended") can then never trigger inside a chain. Both models chose the consistent design over the Skill's. | `out/runs/*/C3.md`; execution log in chat 2026-10-29; `cc-skills-and-hooks-composition.md` §5 sketch, bound 1 | **A1** |
| F-3 C4 A6: no Haiku 5.5 scout | **Test defect.** v5.0 left out the Scout on purpose under the Skill's tool/agent gap rule. | v5.0 C4: "No Scout or Debugger by default. No gap justifies them yet… (add a Haiku Scout)" | None |

Also from the outputs:

- **C1: both arms' hooks work.** Both blocked writes to `migrations/` (exit 2), including an absolute path. Both allowed `src/` and `migrations_backup/`.
- **Observation 28 needs a qualifier.** The v4.2 arm's C1 and C3 outputs open with "Fix the Skill first". They then correct the `matchers` shape and the exit-1 claim from model knowledge; the arm had only the `Skill` and `Read` tools. The Skill defect was real, but on Opus 5.5 it did not reach the output in this sample.
- **Rubric lesson.** All three misses trace to rubric assertions built from the spec's §11 change list. Two were wrong for the request (F-1, F-3): they tested whether a change was present, not whether it fit. The third (F-2) copied the Skill's own contradiction into the rubric.

## 2. Decisions

- **P1 — one cut.** The D9a fixes, the 16 open findings, and the KF deltas ship as one catalog patch (anti-churn rule). No D9a re-run (SBD §3.9 stopping rule). Fix A1 is verified by running the revised sketch against fixtures (§4 G5), not by a new D9a.
- **P2 — versions.** Each touched Skill goes to `5.0.1`. Untouched Skills stay `5.0.0`. Expected touched set, from §3 (11): cc-design, critic-gate, handoff-trigger-check, context-budget, full-stack-audit, global-audit, project-audit, prompt-compilation, prompt-validation, domain-agentic-context, domain-research-analysis. The build computes the actual set from its diff and halts if the two lists differ, or if any version is bumped wrongly.
- **P3 — release shape (operator decision at the release prompt, not now).** Recommended default:
  - per-Skill releases `rootnode-<skill>/v5.0.1` for the touched Skills, with `--latest=false`;
  - plus umbrella `catalog-v5.0.1`, marked Latest, whose bundle carries all 29 artifacts at their current versions, so the bundle stays the one full-catalog download.
  - The playbook gains this patch shape (D2).

## 3. Changes

Locators in the session report date from the PR #25 build, and some line numbers have since moved. Locate each item by its quoted content.

**A — D9a-driven (cc-design)**

- **A1 — chain-scoped Stop bounds.** Applies to `references/cc-skills-and-hooks-composition.md` §5: the `verify-tests.sh` sketch and "Bounded Stop hooks".
  - Rule text replaces bound 1: "Read `stop_hook_active` to scope the count. The field is true when Claude is already continuing because of a stop hook. A hook that ignores it can trap the session. A hook that releases on the first `true` can block only once per stop chain, so no block cap can trigger. Reset the chain counter when the field is false; count blocks while it is true."
  - Bound 2 becomes two caps:
    - No-progress: N blocks on unchanged evidence (AI-DLC working values 2 interactive, 8 unattended).
    - Chain total: M blocks, default 3×N `[assumption — tune per repo]`.
    - Either cap releases, logged. The session report records the gate `NOT_RUN`.
  - Without `jq`, treat every stop as a chain continuation, so the caps still release (closes F30).
  - Sketch: read stdin once into `INPUT`. Delete the line `[ "$(jq -r '.stop_hook_active // false')" = "true" ] && exit 0   # bound 1`. Reset the counter file when the field is not `true`. Store `KEY N TOTAL` in the counter file, and release when `N > MAX` or `TOTAL > MAX_TOTAL`.
  - Before editing, fetch the hooks reference (`code.claude.com/docs/en/hooks.md`) and quote the `stop_hook_active` field description in the commit message, tagged `[Anthropic docs — hooks, fetched <date>]`.
  - Update the matching row in `cc-anti-patterns.md` ("Unbounded Stop hook") to name a chain-scoped cap.
- **A2 — resume line.** In `references/cc-prompt-design-patterns.md` §6, the autonomous template's halt section gains one line: "Resume: after the operator fixes the cause, re-run this prompt; completed steps are skipped by <restart marker or idempotent check>."

**B — open findings from the v5.0 session report**

| ID | Where (locate by content) | Change |
|---|---|---|
| F2 | `design/root_DESIGN_catalog_v5_model_alignment.md` (tracked copy) | Header "Status: DRAFT for operator decision on D1–D6" → "Status: ACCEPTED 2026-10-22 — D1–D5 as recommended, D6 as revised". Block-selection tier T1 → T2 (it shipped T2, F1). |
| F13 | cc-design SKILL.md section cross-refs | cc-methodology §2 → §1; §4 → §7; "§ Assert the END state" → cc-prompt-design-patterns §10. Check each target heading exists. |
| F14 | cc-design SKILL.md "15-anti-pattern catalog" | 15 → 17, matching `cc-anti-patterns.md`. Count the catalog's rows; do not copy the number. |
| F15 | cc-design `description:` | "…chat-to-CC handoff specs, and EXECUTION_PLAN.md remediation plans, session-report standards." → "…chat-to-CC handoff specs, EXECUTION_PLAN.md remediation plans, and session-report standards." Description stays ≤ 1024 characters (694 today). |
| F16 | domain-agentic-context `reasoning-approaches.md`; prompt-validation `symptom-fix-map.md` | An "Opus 5" named as the current tier → D2 wording (Opus 5.5 + Sonnet 5.5). Leave a line that names Opus 5 as the fallback. |
| F17 | handoff-trigger-check SKILL.md heading "v4.0 update — condition 7 (token/usage budget headroom) under 1M windows" | → "Condition 7 — token/usage budget headroom under 1M windows" |
| F18 | T3 effort paragraphs in context-budget, full-stack-audit, global-audit, project-audit, prompt-compilation | "benefits from `high` or higher" → the D4 wording already in the same paragraph's calibration line; the paragraph must state one effort rule, not two |
| F19 | critic-gate SKILL.md Output Format JSON | Add `"status": "complete" \| "blocked"`, plus a `blocked_reason` string when blocked. The field is additive. If `audit/canonical-kfs/` AEA §5.4 enumerates critic-gate output fields, surface a KF block; do not edit the mirror (halt #5). |
| F20 | context-budget SKILL.md "pays the higher band on the whole prompt" | Remove the inference. State only the landscape's ≤100K / >100K band fact, citing CON §3. |
| F21 | cc-design `cc-prompt-design-patterns.md` mention of `rootnode-behavioral-tuning` | Append "(if available)" |
| F22 | cc-design `cc-environment-design-patterns.md` line with two hooks tags | Keep the "fetched 2026-10-22" tag; drop the older one |
| F24 | domain-research-analysis SKILL.md "For annotated examples of complete research prompts…" | → "…complete research prompts, plus one output-format fragment (Example 4)…" |
| F27 | cc-design migration-guard example | Catch `find migrations -delete`, `cd migrations && rm …`, and globs such as `rm -rf mig*` that can expand to the protected folder. The false positive on `echo rm migrations` stays (fails closed; operator-accepted). |
| F28 | cc-design guard settings `matcher` | Add the edit tools of the running Claude Code that are missing. Check `MultiEdit` and `NotebookEdit` against the tools reference first; add only the names that exist, and record the check. |
| F29 | cc-design guard audit-row append | `mkdir -p` the log folder before the append |
| F31 | cc-design SKILL.md "handoff-gate" | → "rootnode-handoff-trigger-check (if available)" |

**C — KF deltas.** Chat applied the first three to the seed copies on 2026-10-29 and delivered them with the build prompt. The build syncs CC_EG, AAP and SBD from `design/staging-kf/` into `audit/canonical-kfs/` in the same PR, gated on digests. This is the approved sync step that repo halt #5 names.

- **CC_EG §6 "Bounded Stop hooks."** Same correction as A1. The current text says the hook "does not re-block when Claude is already continuing from a stop hook". That makes the cap unreachable.
- **AAP §6.** The "Unbounded Stop hook" candidate's wording: "without a chain-scoped cap".
- **SBD §3.9 D9a arm hygiene.** Replace "Park any user-level copy of the same Skill name for generation" with:
  - "Account sync loads a second copy: Claude Code v2.1.273+ signed in with claude.ai loads the account's Skills as `anthropic-skills:<name>` beside any project or personal copy, so parking the user-level copy no longer isolates an arm."
  - "Run each arm as `claude -p` in its own folder outside the repo, with the arm's Skill at project level and `--setting-sources project,local`. Gate every run on the harness `init` event's `skills` list showing exactly one copy. Observed 2026-10-29 on 2.1.302 and 2.1.312."
  - "Verify a synced copy by parsed frontmatter plus body, not raw digest: claude.ai re-serializes SKILL.md frontmatter on upload."
- **CI.** The SBD description's arm-hygiene clause gains the sync-isolation rule. Delivered by chat with the build prompt.
- **Release playbook (seed + `docs/`) — applied by the release prompt, with P3.** Adds:
  - (D1) the install note: "A user whose claude.ai account holds the Skills gets them in Claude Code through account sync (v2.1.273+, claude.ai sign-in). `-cc` zips serve API-key sessions and users who do not upload to claude.ai. Installing both loads two copies."
  - (D2) the P3 patch-release shape.
  - README install text carrying the same caveat is Tier 1, so it needs explicit operator approval at the content PR.

## 4. Build gates (end-state, LF-normalized)

| ID | Gate |
|---|---|
| G1 | `git diff --name-only <base>` lists only the files in §3 A/B plus version-bumped SKILL.md frontmatter. The count is computed from the list. |
| G2 | Every touched Skill's `metadata.version` is `5.0.1`; every untouched Skill's is `5.0.0`. Both lists are computed from G1. |
| G3 | Each §3 B item: before/after grep of the quoted content, both lines in the report |
| G4 | cc-design `description:` length ≤ 1024 and parse-valid YAML; skill-builder `quick_validate.py` passes on every touched Skill |
| G5 | The revised `verify-tests.sh` sketch, saved and run with real `jq` against a failing-evidence fixture: `stop_hook_active:false` blocks (exit 2); 2 further `true` stops on unchanged evidence block, then the next releases (exit 0); changing evidence resets N but TOTAL still releases at M; with `jq` removed from PATH, the caps still release. Each row's exit code is recorded. |
| G6 | `build_release_artifacts.py` dry run still yields 24 + 5 = 29 |

Topology: Builder→Refuter, bounded at two cycles (CC_EG §3.5). The Refuter re-derives A1 from §1's evidence and from the hooks doc quote, not from the Builder's summary.

## 5. Out of scope

- Re-running the D9a.
- The runner's remaining defects. The runner is untracked tooling; its Git Bash lookup is fixed. Still open: nested-fence extraction, JS hooks, and the command guard's false positives on block-list strings. Fix them if the runner is reused, for example in Phase Loop.
- Website sync (separate task).

## 6. Facts verified this cycle (for build_context)

- `--setting-sources project,local` isolates a project-level Skill from its synced copy in `claude -p`. A plain `claude -p` loads both. Observed on CC 2.1.312 and 2.1.302.
- In `claude -p` stream-json, the `init` event carries `skills`, `model`, `tools`, and `claude_code_version`. A Skill call appears as `tool_use` named `Skill` with `input.skill`.
- `--tools` takes a variable number of values. Put the prompt on stdin, or `--tools` consumes it. `--bare` needs an API key. `--restricted` drops project Skills.
- claude.ai re-serializes SKILL.md frontmatter on upload. The body and the parsed frontmatter stay identical, but the raw digest changes.

## 7. build_context deltas (closeout)

- PR #27 mirror sync, merge `e336bce54941a6b0ec0fae01f8dbcc9261324b37`.
- Install outcome: 27 Skills on the account at 5.0.0. Sync verified on 2.1.302. Personal copies moved to a backup.
- D9a result and triage (§1). The Observation 28 qualifier (§1).
- Observation candidate: "an assertion copied from a change list tests for the change's presence, not its fit to the request". Pattern (h) neighbor of O26/O27.
- §6 facts.

## 8. Rev 2 — fold every identified item into this cut

The operator directed that every identified change ship in this patch rather than a later one (anti-churn). The changes below are added to PR #28 on the same branch. The ACCEPT bound to the old diff no longer holds (receipt freeze), so the review re-runs on the full diff.

**8.1 Skill content**

| ID | Where | Change |
|---|---|---|
| R1 (F-9) | cc-design `cc-skills-and-hooks-composition.md` §5 "Bounded Stop hooks" and sketch | Append the host-cap paragraph from CC_EG §6, verbatim. In the sketch, comment the chain-total default: keep it at or below `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP` (default 8) when stops can repeat without a tool call between them. |
| R2 (F-6) | cc-design `troubleshooting.md` hook-fix paragraph | "(`stop_hook_active`, no-progress cap)" → "(chain-scoped by `stop_hook_active`; no-progress and chain-total caps; Claude Code's own continuation cap — composition reference §5)" |
| R3 (F-7) | Every "handoff-gate" in `rootnode-*/`: critic-gate SKILL.md and `references/checks-detailed.md`; handoff-trigger-check SKILL.md, `references/examples.md` (2), `references/troubleshooting.md`; mode-router SKILL.md, `references/trigger-types-detailed.md`, `references/troubleshooting.md` | In another Skill: `rootnode-handoff-trigger-check`, plus "(if available)" where it reads as a dependency. Inside handoff-trigger-check's own files: "the handoff trigger check". Gate: `git grep -c handoff-gate -- ':(glob)rootnode-*/**'` returns nothing. |
| R4 (F-8) | cc-design migration guard (composition reference §4 sketch and settings example) | (a) A `find` whose start path is `.`, `./`, `..`, `/`, `~` or absent, with `-delete` or `-exec rm\|mv`, and with no `-name`/`-iname`/`-path` filter → block. (b) Add the PowerShell tool: check its exact tool name and command field in the Claude Code tools reference first, add it to the matcher, and match `Remove-Item\|ri\|del\|erase\|rd\|rmdir\|Move-Item\|mi\|move\|rm\|mv` without regard to case, with the same migrations and glob rules. (c) Evaluate the glob rule per command segment, split on `;`, `&&`, `\|\|` and `\|`: only words in a segment whose command is `rm`, `mv` or `find` (or a PowerShell delete or move) count. |
| R5 (build lessons) | cc-design `cc-prompt-design-patterns.md` §10, shell paragraph | Add three sentences. (1) A git pathspec with a trailing slash, such as `'dir-*/'`, matches nothing; use `':(glob)dir-*/**'`, and have the gate print its match count so an empty match shows. (2) An exclude pathspec does not stage files in an untracked folder; stage an explicit file list. (3) Name the interpreter: on Windows, `python` can resolve to an application's bundled copy, so prefer the `py` launcher when present and record which interpreter ran. Tag: `[observed: v5.0 catalog generator (Observation 30) and the v5.0.1 build, 2026-10-30]`. Add one sentence on `claude -p` worker allow-lists: loops and `&&` chains were denied under a `git`-only allow-list while a single `git … \| tr \| sha256sum` pipeline ran `[observed, Claude Code 2.1.302]`; name every command the worker runs, or tell it to run one pipeline per call. |

R3 touches mode-router, so the touched set becomes 12, with mode-router at `5.0.1`.

**8.2 Repo files delivered by chat (digest-gated)**

| File | Change |
|---|---|
| `audit/canonical-kfs/root_CC_ENVIRONMENT_GUIDE.md` | Adds the F-9 host-cap paragraph to §6, and R3 in §9 |
| `audit/canonical-kfs/root_AGENT_ENVIRONMENT_ARCHITECTURE.md` | R3 in §6.3 |
| `docs/root_SKILLS_RELEASE_PLAYBOOK.md` | §1.2 install note (D1); new §1.6 patch catalog release (D2) |
| `README.md` | Version badge v4.0 → v5.0.1. Calibration badge → Opus 5.5 + Sonnet 5.5. Bundle name made version-free (two places, so it cannot go stale). The account-sync caveat after the dual-surface paragraph. README is Tier 1, and the operator approves it at merge. |

**8.3 Repo housekeeping**

- `build_release_artifacts.py`: `CATALOG_VERSION` `"v5.0"` → `"v5.0.1"` (P3 option 1, operator default).
- Commit the first build's session report and Refuter files (`audit/v5_0_1-patch/`). They ride this commit cycle.
- Commit `design/audit-artifacts/v4.2/v42_inventory_report.md` if it exists and passes the secret scan. Leave `scratch/` untracked and list it in the report.

**8.4 Seed-side (chat, not the build)**

- The Project carries the same CC_EG, AEA and playbook text, written by chat on 2026-10-29.
- build_context closeout after release:
  - PR #27 and PR #28;
  - the install outcome;
  - the D9a result and triage;
  - the Observation 28 qualifier;
  - the Observation candidate from §7;
  - the trailing-slash pathspec as a recurrence of the Observation 30 root cause, in the v5.0.1 build prompt;
  - the §6 facts and the host Stop-hook cap.

## 9. Rev 3 — the rev 2 build's findings, then freeze

| ID | Where | Change |
|---|---|---|
| S1 (F-14) | CC_EG §6 (mirror, from staging) and cc-design `cc-skills-and-hooks-composition.md` §5 "Bounded Stop hooks", where the paragraph is a verbatim copy | Replace "Set the hook's caps to release first — a chain-total cap at or below the host cap when stops can repeat without a tool call between them — or raise the host cap deliberately and say so in the design." with the staged CC_EG sentence. The point: the host's count runs alongside N, not M. A stop with no tool call leaves the evidence unchanged, so N advances. M advances past N only when the evidence changes, which takes a tool call and resets the host's count. No default changes: N = 8 unattended equals the host cap, so the hook releases first. In the sketch, delete the comment line under `MAX_TOTAL=` and extend the `MAX=` comment to: `# N: 2 interactive, 8 unattended; keep N ≤ CLAUDE_CODE_STOP_HOOK_BLOCK_CAP (default 8)`. |
| S2 (F-10) | Guard glob candidates | `for X in migrations ./migrations x/migrations` → `for X in migrations ./migrations ../migrations x/migrations` |
| S3 (F-11) | Guard, a paragraph after the sketch | **What the guard cannot see.** It matches command text, so a delete that does not appear as text gets through. Examples: a pipe-fed delete (`ls migrations \| xargs rm`, `Get-ChildItem migrations \| Remove-Item`), a script or another interpreter that deletes, or a variable that expands to the path. For a guarantee, pair the guard with the Claude Code mechanism that denies writes to the path. Check that mechanism in the permissions and sandboxing docs, and quote the rule syntax and the platforms it covers. The guard then adds an on-task message and an audit row; it is not the guarantee itself. Do not name a mechanism the docs do not state. |
| S4 (F-12) | This spec, §4 G5 | Erratum. N = 2 means two blocks, then release on the third stop. A literal reading of "2 further `true` stops … block, then the next releases" gives three blocks. The A1 rule ("release when `N > MAX`") controls, and both builds applied it. |
| S5 (F-13) | Commit list | Commit, after the G8 scan: `audit/v5_0_1-patch/session_report_20261030-0107Z.md`, `session_report_20261030-0224Z.md`, `refuter_brief_r2c1.md`, `refuter_r2c1.json`, `design/audit-artifacts/v4.2/root_CC_DESIGN_v42_spec.md`, `design/audit-artifacts/v4.2/root_CC_LANDSCAPE_20260911.md`. `design/audit-artifacts/v4.2/scratch/` stays untracked. |

No Skill outside cc-design changes, so the touched set stays at 12.

**Freeze.** After rev 3 the cut is closed. A finding from the rev 3 build or its review goes to the next patch unless it is a regression in this PR (SBD §3.9 stopping rule). Shell-pattern coverage in an example guard has no natural end. S3 replaces further pattern-chasing by stating the guard's limit and pointing to the mechanism that enforces.

## 10. Release docs in the content PR

Playbook §2 Phase A step 3 puts the release notes in the content PR, and §1.6 sets their shape for a patch catalog release. PR #28 did not carry them through rev 2, so they join it here. They are planned release content, not findings, so the §9 freeze does not apply to them.

| Target | Source | LF-sha256 of the end state |
|---|---|---|
| `audit/v5_0_1-patch/release-notes-v5.0.1-config.py` | `design/staging-kf/release-notes-v5.0.1-config.py` | `af36d3355bba909823fbba68d5aa0d2715910f12c5f266d80d871562646c3986` |
| `release-notes/catalog-v5.0.1.md` | `design/staging-kf/catalog-v5.0.1.md` | `a5c017c6ad20b55208a20c9f5a46b001fedd221260d4c793e0e7dd79af13de4f` |
| `CHANGELOG.md` | `origin/main` content, one blank line, then `design/staging-kf/CHANGELOG_v5.0.1_entry.md` (`8f08943143d7220ab36a8526a5ed6cc6d86bc0ae34e178a323b60c31d05730a4`) | `3eccbe6f146d479a0f40ecf3ca2a5e001f04b1a9ef43b4aac7793be389a05702` |

The 12 per-Skill notes are generated, not copied: `generate_release_notes.py --config audit/v5_0_1-patch/release-notes-v5.0.1-config.py` writes `release-notes/<skill>-v5.0.1.md` and prints `Counts OK` for A 9, B 2, C 1, total 12.

| File in `release-notes/` | LF-sha256 |
|---|---|
| `rootnode-cc-design-v5.0.1.md` | `6f4f5b885b270893ffdc6cba078a3c59d3ad88ed681ef4ca0e182d1f60c011e4` |
| `rootnode-context-budget-v5.0.1.md` | `4e47eb8b6e189ed20c287c16d9f31f37f1b6c3cdfd79690ace364e09d4108c43` |
| `rootnode-critic-gate-v5.0.1.md` | `6974ee1df2eb0000a27204a22cdd0ef698e55b50fc80254eff250dd0e64559b9` |
| `rootnode-domain-agentic-context-v5.0.1.md` | `496b97b463cffc8390481ca3e3fa12e52d9572cb9b77f1c69438ad93d17587bc` |
| `rootnode-domain-research-analysis-v5.0.1.md` | `9e9ac6d6656677747d31cf4c032c6999bde27c0ccedb907552091a498ab5d867` |
| `rootnode-full-stack-audit-v5.0.1.md` | `4aa73d80945711f920b81e6fa63929426eb4975e1a27b93fe5e912a6f79f594f` |
| `rootnode-global-audit-v5.0.1.md` | `a9ee6195a6c3490fb0bf045603117adb59aa8b7c1677c60b6ce96ae08385ec39` |
| `rootnode-handoff-trigger-check-v5.0.1.md` | `e99cbb6fbe4a5688d63e588da84867329959735aac7912ea4a5a6827258d5b5d` |
| `rootnode-mode-router-v5.0.1.md` | `2203936b1487123e1a1564e265820f17f13a259abc244800289b356b2264778e` |
| `rootnode-project-audit-v5.0.1.md` | `f050eae13b2dcd4d76aa0ac57a61bbf987aad0943839e0837f655713007ba6e3` |
| `rootnode-prompt-compilation-v5.0.1.md` | `928cd8c526b96a1fa4f01ace4ffe875e0875ea38db0ae5defa2877606c37066d` |
| `rootnode-prompt-validation-v5.0.1.md` | `0a10e46bea456c6f4852d41537ef7317070006a95925b7a2653a76d308e5f08a` |

Umbrella invariants: 27 `releases/tag/rootnode-` links; 12 end in `/v5.0.1)`, one for each Skill at 5.0.1, and 15 end in `/v5.0)`, one for each Skill at 5.0.0; 0 `]](`; one `## Download`; the bundle named `rootnode-catalog-v5.0.1.zip`.
