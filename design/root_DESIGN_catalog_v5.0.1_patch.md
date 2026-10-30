# root_DESIGN_catalog_v5.0.1_patch — catalog patch after the v5.0 D9a

Status: ACCEPTED 2026-10-29. Inputs:
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
