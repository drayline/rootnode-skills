# root_DESIGN_cc-design_v5 — design spec for rootnode-cc-design 5.0.0

**Predecessor:** rootnode-cc-design 4.2.0 (`820e5c0`; SKILL.md 31,931 bytes, 268 lines; description 668 chars YAML-parsed; 10 references + 2 schemas).
**Inputs consumed:** (1) `root_MODEL_LANDSCAPE_2026-10.md`; (2) the operator's EVOLVE design `root_EVOLVE_cc-design_session-reports.md` (2026-09-17, RSA origin); (3) three read-only analyses of `awslabs/aidlc-workflows` v2.11.1 (orchestration / hooks-and-sensors / audit-and-review slices) checked against the cc-design v4.2 baseline; (4) the Anthropic hooks reference (code.claude.com/docs/en/hooks, fetched 2026-10-22) — the instrument that confirmed the hook defect.
**Mode of this spec:** EVOLVE at major-version scale — section-level deltas against files that exist; one new reference file. Everything else in v4.2 is preserved.

---

## 1. What changes, in priority order

| # | Delta | Why it is in v5.0 | Class |
|---|---|---|---|
| A | **Hook reference defect fix** — `cc-skills-and-hooks-composition.md` §4–§6 teach `exit 1` as blocking and a `"matchers": [{...}]` schema | Verified wrong against the Anthropic hooks doc ("Exit code 1 without valid JSON output is a non-blocking error… If your hook is meant to enforce a policy, use `exit 2`"; config is `"matcher": "<string>"` + `"hooks": [{type, command, timeout}]`). Every hook the Skill has emitted from these examples is enforcement-as-preference — the Skill's own §4.4 anti-pattern. Highest priority because it is a correctness defect in shipped output, not a landscape drift | FIX |
| B | **Model-landscape refresh** — calibration line, role-table model column, effort-per-role, product-fact version markers, new CC mechanisms | Landscape block §1, §5, §6; the role table's "Haiku tier via `Explore` override" row now has a real model (Haiku 5.5: 1M, effort-capable, "subagent tasks" positioning) | REFRESH |
| C | **Session report output standard** — the attached EVOLVE delta, upgraded to a computed schema | Two RSA runs produced no durable record because the prompt scope never authorized a report write; the completion report pasted into chat is ephemeral. Adopted as designed, with three AI-DLC-informed changes (§5) | ADD |
| D | **Delegation hardening** (AI-DLC-derived, 8 items) — content-bound briefs, bounded refute loop, `blocked` ≠ empty, verdict-dictation self-report, write-before-cap, failure ladder, receipt freeze, kill-first refuter | Each closes a named gap in `cc-delegation-patterns.md` §2–§5 that the v4.1 Builder→Refuter loop left open (no cycle cap; no spec digest in the brief; silent cutoff reads as "no findings") | ADD |
| E | **Prompt-design additions** (AI-DLC + landscape, 6 items) — early-stop countermeasure, bookkeeping-in-tools, include-and-exclude justification, assumption status survives, autonomy escalation rule, permission-shaped commands | Early-stop is the one behavior documented across all four 5.5-generation prompting guides and is absent from §6 autonomous prompts; the rest are one-paragraph rules with CC_EG homes | ADD |
| F | **Environment-design additions** (AI-DLC, 5 items) — Stop-hook bounding, guard fail-direction, advisory-check tier, one-owner-per-rule, correction routing (learning loop) | Extend the hooks-vs-prompts boundary from binary (prompt / blocking hook) to three tiers and give the iron-law Stop hook a bound it currently lacks | ADD |

Token budget (D1 of the skill-builder gate; v4.2 rule: resident description flat, per-activation growth capped): description stays ≤ 700 chars (668 now; the session-report trigger adds ≤ 30); SKILL.md ≤ 290 lines and ≤ 34,500 bytes (+8% over 31,931 — every addition below is a routing line, with depth in references); references may grow where the table in §9 says so; one new reference (`cc-session-reports.md`, target ≤ 180 lines). DESIGN-mode per-activation estimate must stay within +10% of the v4.2 inventory figure (~27–28k est. tokens); the build reports the measured figure.

## 2. Delta A — hook reference fix (`references/cc-skills-and-hooks-composition.md`)

Rewrite §4 "Hooks lifecycle reference" and the examples in §5–§6. Required content, each line `[Anthropic docs — hooks, verified 2026-10-22; re-verify on the running version]`:

1. **Exit-code contract.** `exit 0` = success, JSON output fields applied; `exit 2` = blocking error on events that can block (PreToolUse blocks the call; Stop prevents stopping; UserPromptSubmit blocks the prompt; PostToolUse only shows stderr — the tool already ran); any other exit code = non-blocking, the action goes ahead. State the doc's own warning verbatim. A timed-out `command` hook does not block on PreToolUse unless `onFailure: "block"` is set.
2. **JSON contract.** `{"decision":"block","reason":"…"}` (the only `decision` value is `block`); PreToolUse `hookSpecificOutput.permissionDecision` ∈ allow/deny/ask/defer with `permissionDecisionReason`; universal `continue:false` + `stopReason` overrides everything. Note: with `exit 2`, even `permissionDecision:"allow"` does not let the action through.
3. **Configuration shape.** `"hooks": {"<Event>": [{"matcher": "<exact | a|b | regex>", "hooks": [{"type":"command","command":"…","timeout":<seconds>}]}]}`. Replace the three `"matchers": [{...}]` examples (lines 142, 217, 223) and the three `exit 1` scripts (257, 264, 271) and the line-218 inline command.
4. **Event set.** Replace the four-event list with the documented set, grouped: session (`SessionStart`, `SessionEnd` — 1.5 s shared budget, raisable to 60 s; `Setup`), prompt (`UserPromptSubmit`, `UserPromptExpansion`), tool (`PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PostToolBatch`, `PermissionRequest`, `PermissionDenied`), agent (`SubagentStart`, `SubagentStop`, `TeammateIdle`, `TaskCreated`, `TaskCompleted`), stop (`Stop`, `StopFailure`), context (`PreCompact`, `PostCompact`), model (`PreModelSwitch`, `PostModelSwitch`), environment (`ConfigChange`, `CwdChanged`, `DirectoryAdded`, `FileChanged`, `WorktreeCreate`, `WorktreeRemove`, `InstructionsLoaded`), UI (`Notification`, `MessageDisplay`, `Elicitation`, `ElicitationResult`). Keep the "common uses" prose for the four the Skill already covers; add one line each for `SessionStart` (re-inject context after resume/compaction), `PreCompact` (validate state before compaction), `SubagentStop` (maintain an in-flight ledger so a Stop hook can wait on background agents without the orchestrator reading anything), `PostToolUseFailure`.
5. **Bounded Stop hooks** (new subsection in §5). A Stop hook that blocks can trap a session. Two bounds, both required in any iron-law hook the Skill emits: honor the `stop_hook_active` input field (do not re-block when Claude is already continuing from a stop hook — *verify field name on the running version*), and keep a no-progress counter in a state file that releases the session after N blocks with the same evidence (AI-DLC's working values: 2 interactive, 8 unattended; reset when the gate evidence changes). The block reason is worded as an on-task continuation naming the missing evidence, never an override-shaped instruction. Source: `[practitioner: awslabs/aidlc-workflows `core/hooks/aidlc-continue-workflow.ts` header — "a stuck block is the ONE way to trap a session"]`.
6. **Fail direction and stderr contract** (new column in the §1 decision tree). Each hook declares which way it fails: observers fail open (`exit 0`); a guard that loses its own bookkeeping fails toward the last recorded instruction with a one-line note, never into a re-ask loop; evidence that binds a human decision never falls back to a guess. A blocking hook's stderr names the exact next step. Promote a prose rule to a hook only on observed evidence that prose lost; give each such hook its own off-switch env var and an audit row per block. `[practitioner: aidlc `AGENTS.md` §Guards; `aidlc-plan-approval-guard.ts` header]`
7. **Health carrier.** An observer hook that may legitimately do nothing writes a heartbeat file (`.claude/hooks-health/<hook>.last` or the repo's convention) so a doctor check can tell a healthy idle hook from a silent failure — the Skill's own carrier discipline (build_context O26/O27) applied to hooks. `[practitioner: aidlc `06-hooks-and-tools.md` §PostToolUse]`
8. **MCP/agent product facts to re-verify** (§6 Pattern D and `cc-environment-design-patterns.md` §8): a `tools:` allowlist in agent frontmatter drops inherited MCP tools unless fully-qualified names are listed; a bare `mcp__<server>` entry is not honored; a pinned `effort:` is a cap, not a floor. Source is a 2.1.159-era spike `[practitioner: aidlc `14-claude-features.md`]` — carry as `[verify on running version]`, not as fact.

Troubleshooting (SKILL.md) gains one entry: "A hook the Skill designed never blocks anything" → check exit code (must be 2) and config shape; see §4.

## 3. Delta B — model-landscape refresh

| Surface | Change |
|---|---|
| SKILL.md line 24 calibration | §3.1 Tier 3 template from the catalog spec |
| `cc-delegation-patterns.md` §1 role table | Scout: "Haiku 5.5 via a project `Explore` override, effort `low`"; Researcher: "Haiku 5.5 at `medium`–`high`, or Sonnet 5.5 for judgment-heavy reads"; Builder: "Sonnet 5.5 baseline, Opus 5.5 for hard specs"; Refuter: "Opus 5.5 or above"; Debugger: "Opus 5.5 at `high`; `xhigh` only on measured gain"; Orchestrator: "Opus 5.5 (CC default) or Fable 5.1 for multi-sitting runs". Reviewer ≥ builder rule unchanged |
| §1 "Model tier selection" paragraph (line 42) | Rewrite with the landscape §3 scope: Opus 5.5 at its `medium` default is the recommended CC default (Anthropic: matches Opus 5 at `high`); Sonnet 5.5 at `high` for lighter agentic work; Fable 5.1 "when your evals on Opus 5.5 at higher effort still don't meet your requirements"; Haiku 5.5 is the scout/extraction tier (1M, effort-capable, >100K-prompt price band noted). Keep the "CC default model is not restated here" sentence — it was right (the default moved from Opus 5 to Opus 5.5 in one release) |
| §1 "Effort per role" (line 48) | Replace the `thinking: disabled` 400 sentence: thinking cannot be disabled at all on Opus 5.5 / Sonnet 5.5 / Fable 5.1 (Sonnet 5.5 floor is `between_tools` at ≤`high`); Haiku 5.5 accepts `disabled` at ≤`high`. Add: the Agent tool accepts an `effort` parameter per invocation (v2.1.292+) in addition to frontmatter `effort`; at `xhigh`/`max` Sonnet 5.5 self-launches reviewer subagents — a delegation-cap concern, countered by the one-paragraph Anthropic block (behavioral-tuning spec §3, #13 facet) |
| §1 Builder tier-switch (line 44) | Add `CLAUDE_CODE_WORKFLOW_SUBAGENT_MODEL` (v2.1.296) — runs every *workflow* agent on one model while other subagents keep theirs; keep `_FORCE` semantics |
| §1 "Built-in behavior that changed" (line 46) | Rephrase per current doc: Explore inherits the main model; when main runs Fable, Explore runs on the `opus` alias (Anthropic-hosted only); on third-party providers it stays on main |
| §5 cap table (lines 119–126) | Names verified: `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` (default 3; `1` disables nesting), `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` (default 20, v2.1.217+; ultracode sessions exempt), `CLAUDE_CODE_SUBAGENT_MODEL` / `_FORCE`, `CLAUDE_CODE_FORK_SUBAGENT=0` (fork mode is **on by default** — a Refuter that must be non-fork needs this or an explicit non-fork spawn), `CLAUDE_CODE_DISABLE_EXPLORE_PLAN_AGENTS`, `maxTurns` partial-return (v2.1.246+). `CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION` (line 121) and `CLAUDE_CODE_DISABLE_WORKFLOWS` (line 125): not on the fetched pages — mark `[unverified on 2.1.30x]` or remove if the build cannot verify |
| §6 Ultracode | Add `/effort ultracode off` (v2.1.284+); ultracode unavailable when workflows are off or the model lacks `xhigh` |
| `cc-environment-design-patterns.md` lines 181–185 | Same Explore rephrase; model column of the built-in table → "inherits (Fable → `opus` alias)" |
| `cc-prompt-design-patterns.md` line 57, `cc-anti-patterns.md` line 195 | "(Haiku, read-only, cheap)" → "(Haiku 5.5 via `Explore` override, read-only, cheap)" |
| All `CLAUDE_CODE_*` mentions | Carry the version-annotation convention from v4.2 (`[v2.1.NNN+ — verify on running version]`) on every new name |

## 4. Delta C is in §5. Delta D — delegation hardening (`references/cc-delegation-patterns.md`)

Each item lands as one paragraph; the eight-field brief grows by two fields (9 and 10) — the SKILL.md Step 4 bullet "Delegation briefs are complete or absent" updates its field count.

1. **Brief field 9 — bound spec digest.** Every Builder/Refuter brief opens with the LF-sha256 of the spec (or diff) it works from; the worker halts on mismatch. This extends the end-state rule (§10 of prompt patterns) to delegation: authority binds to content, not to who issued it or when. `[practitioner: aidlc `12-state-machine.md` "Authority binds to content and attempt"; `stage-protocol-swarm.md` §12b]`
2. **Brief field 10 — no verdict dictation; self-report.** A Refuter brief never names a verdict to write or prefer and never passes the Builder's reasoning or plan; the Refuter's return opens with `Verdict Dictated: yes|no` so a contaminated brief is visible in the record. `[practitioner: aidlc `stage-protocol-reviewer.md` §12a]`
3. **Bounded loop.** Builder→Refuter cycles default to **2**; after the cap the work goes to the operator gate with open findings listed. A Refuter return with no verdict is re-dispatched once; a second incomplete return is recorded as `NOT-READY` — "a silent cutoff becomes a visible finding." Operator gate escape: after 3 REWORK cycles, offer "accept as-is with open findings." Aligns with REMEDIATE's existing 3-cycle critic cap. `[practitioner: aidlc `15-stage-definition.md` reviewer_max_iterations; `guide/06-agents.md`]`
4. **`blocked` ≠ empty.** A return contract has three outcomes: findings, no findings, or `status: blocked` (could not inspect — missing file, tool failure, cap hit before inspection). An empty findings list is never the encoding of "could not look." Shared wording with critic-gate (catalog spec §4). `[practitioner: aidlc `ai-pr-review-lens-json.md`]`
5. **Identity marker + write-before-cap.** The first line of a Refuter/Builder return names its role and the head SHA (or spec digest) it worked against; the orchestrator checks it before trusting the body. The brief's turn budget reserves the final turns for writing the return: "write the review BEFORE the cap, never on your last turn." `[practitioner: aidlc `aidlc-architecture-reviewer-agent.md` §Turn Budget]`
6. **Failure ladder.** On a failed subagent: retry once with reduced context; then the orchestrator chooses "run inline" or "skip and record"; never a third identical retry. Non-empty concerns in a return must reach the operator; fewer files than expected is investigated before marking complete. `[practitioner: aidlc `04-stage-protocol.md` Subagent Return Summary]`
7. **Receipt freeze.** After a Refuter ACCEPT bound to a diff digest, any write to the reviewed files invalidates the ACCEPT; the loop re-enters at the Refuter, not at "done." A PreToolUse hook (exit 2) is the mechanism when the guarantee must hold; prose is the fallback. `[practitioner: aidlc `aidlc-review-freeze.ts` header — the observed oscillation it was built for]`
8. **Kill-first refuting.** The Refuter's first move on each Builder claim is to try to disprove it (upstream guard, unreachable path, covered by a test it can run), then re-derive survivors from base + diff. Findings carry a locator (`path:line`) and, at top severity, a one-step repro and a concrete loss — a finding that cannot state both is re-rated. `[practitioner: aidlc `ai-pr-review-judge.md`, `ai-pr-review-common.md`]` This is also the shape to recommend when a deployment composes `rootnode-critic-gate` (Step 6).

Worktree caveat (one sentence in §4): `isolation: worktree` branches from the default branch by default, not from the parent's `HEAD` `[Anthropic docs — sub-agents]`; uncommitted orchestrator edits are invisible to the Builder — commit (never auto-commit) before forking.

## 5. Delta C — session report output standard

Adopted from the attached EVOLVE design at both sites it names, with these changes:

**Site 1 — SKILL.md Step 4, new bullet after "CC-prompt-specific output discipline" (line 112):**
> **Session reports are mandatory.** Every CC prompt authorizes a report write in its scope and ends with a "Write session report" item. The report records computed state, not narrated state — SHAs, LF digests, `git diff --name-status` rows, gate results with evidence, findings with locators — and names what it does not prove. Path and filename follow the delivery repo's audit convention, set in the design brief (`report_dir`); default `reports/`, timestamped `_{YYYYMMDD-HHMM}Z`. The report is not committed by the same prompt; it rides the next commit cycle. See `references/cc-session-reports.md`.

**Site 2 — `references/cc-prompt-design-patterns.md` § Output discipline:** the one-line entry as drafted in the EVOLVE design, with the path/filename and "computed, not narrated" clauses.

**Site 3 (new) — `references/cc-session-reports.md`** (routing from Step 4; ≤ 180 lines): the schema below, the rationale, and the paste-ready prompt block.

| Field | Content | Why computed |
|---|---|---|
| `prompt` | governing prompt path + its LF-sha256 | provenance, not identity (a field belongs in a fingerprint only if a human-visible change moves it) |
| `outcome` | `COMPLETED` / `HALTED <trigger #>` / `BLOCKED` | `BLOCKED` is distinct from "nothing to report" |
| `started` / `ended` | UTC from `date -u` | never hand-written |
| `pre_state` | branch, HEAD SHA, `git status --porcelain | wc -l` | report-only (end-state rule) |
| `post_state` | HEAD SHA or "uncommitted" + LF-sha256 per replaced file, matched to the prompt's end-state digests | the halt binds here |
| `files_changed` | rows from `git diff --name-status <pre_sha>` + untracked; count summed from rows | summary-vs-itemization rule |
| `gates` | id · command · `PASS`/`FAIL`/`NOT_RUN` · evidence (quoted output line or log path) | `NOT_RUN` ≠ `PASS` |
| `findings` | F-n · severity · `path:line` · open/resolved · owner; IDs persist across continuation prompts | content-anchored ledger |
| `operator_decisions` | verbatim reply + the halt it answered | never summarized |
| `observations` | each tagged `[observed]` / `[inferred]` | |
| `not_verified` | mandatory; "None identified." when empty | a criterion silence can satisfy measures nothing |
| `kf_deltas` | pointer or "none — confirmed" | mirrors session-handoff's gate; the report does not duplicate the handoff |

What the standard does **not** import from AI-DLC: the 121-event audit taxonomy, sharded event logs, hook-emitted rows, readiness/risk scores. A single-prompt report is a final snapshot, not an event stream.

Two corrections to the attached design: (1) `reports/` is the RSA repo's convention; `rootnode-skills` uses `audit/phase-XX/` and `design/audit-artifacts/vN.N/` (repo CLAUDE.md; no `reports/` in the 20260913 catalog) — hence the brief parameter; (2) `<descriptive_name>_<date>` collides on same-day runs — hence the `HHMM` stamp, matching session-handoff's convention. Schema: add `report_dir` (string, default `reports/`) to `schema/cc-design-brief.schema.json`.

## 6. Delta E — prompt-design additions (`references/cc-prompt-design-patterns.md`)

1. **§6 Autonomous prompts — early-stop countermeasure.** New subsection with the Anthropic unattended-runs pattern: treat a text-only end of turn as a report, not proof; name the four early stops to avoid (summary-then-announce with no tool call; offer to continue; non-blocking decision list; milestone report) and the stops you do want (destructive actions, scope changes, things deliberately protected); harness continuation message capped at 2–3; confirmation step for risky actions retained. Include the Sonnet 5.5 / Haiku 5.5 short form ("Keep working until everything the user asked for is done…") as the default block and the Opus 5.5 long block as the fully-unattended variant. Cross-reference tendency #15. `[Anthropic docs — four prompting guides]`. Pairs with the existing turn-economy rule (CC_EG §5.9).
2. **§2 Universal principles — bookkeeping belongs in a tool.** Routing, counts, digests, and audit rows come from commands the prompt names; the model copies tool output and does not compute it. A prose instruction to "append an audit row" is the smell. `[practitioner: aidlc `12-state-machine.md` North-star]`. Ties to the summary-vs-itemization rule.
3. **§10 Output discipline — include-and-exclude justification.** Every gate, halt, and plan step the prompt carries names what it protects; every omitted step names what already covers it. Overlapping "just in case" ceremony is the more common failure. `[practitioner: aidlc `aidlc-composer-agent.md` Adversarial Framing]`
4. **§10 — assumption status survives.** A `[speculation]` or `[assumption]` tag in the brief stays on the fact in CLAUDE.md, the prompt, and the report until the operator confirms it; never silently promoted. Lands also in `source-grading-and-tagging.md` §4 and the handoff bundle (§3 of handoff patterns). `[practitioner: aidlc `stage-protocol.md` §3]`
5. **§6 — autonomy escalation rule.** Autonomy widens only on a fresh operator turn; it narrows on any trigger; a scope grant for one phase is never read as session-wide; hands-off mode removes happy-path gates but keeps failure halts loud; the Refuter is never dropped because the run is autonomous. `[practitioner: aidlc `stage-protocol-construction.md` Autonomy choice]`
6. **§10 shell paragraph — permission-shaped commands.** One command per line, no leading `cd`, no pipes that hide the permission-relevant verb; `cd` in a subshell; text with `$`, backticks, or quotes goes through a file, never interpolated into a shell line. `[practitioner: aidlc `conductor.md` Files and commands; `08-construction-and-swarm.md`]`

## 7. Delta F — environment-design additions (`references/cc-environment-design-patterns.md`, `cc-methodology-patterns.md`)

1. **Three-tier enforcement** (env-patterns §2 placement; composition §1 decision tree): prompt (advisory, no guarantee) → **advisory check** (deterministic, runs on write, surfaces a finding, never blocks; a check whose tool was unavailable "evaluated nothing and does not clear an earlier failure") → blocking hook (`exit 2`, at a gate). Overriding a blocking check is a logged operator decision and is forbidden in unattended runs. `[practitioner: aidlc `06-sensors.md`]`
2. **One owner per rule** (env-patterns §2): every invariant has one owner and one shared check; enforcing it at two boundaries (hook + CLI floor) is fine; a second independently written version is a defect. `[practitioner: aidlc `AGENTS.md`]`
3. **Correction routing** (methodology §4 additive evolution / change_log; SKILL.md Step 3 EVOLVE bullet): each friction correction routes to exactly one of — a standing rule at the narrowest scope, a deterministic check, or discard — and the routing is recorded; a recurring manual check becomes a check, not a prose rule. `[practitioner: aidlc `05-rules-and-the-loop.md`]`
4. **Prior-judgement locks** (env-patterns §10/§12): a setting the team explicitly locked (a strict mode in a settings file) outranks one chat request; the refusal names the file. Defaults are not locks. `[practitioner: aidlc `AGENTS.md` Prior judgement]`
5. **Deliberate-deviations register** (methodology §7): a list of known deviations with reasons, kept "to prevent future 'fix' attempts." `[practitioner: aidlc `03-orchestrator.md`]`

## 8. Not adopted (recorded so the next cycle does not re-litigate)

The AI-DLC engine-as-code runtime (typed directives, HMAC receipts, 121-event taxonomy, six-subcommand orchestrator); the voice contract and per-stage ceremony (UX for non-expert users; fails lean-over-comprehensive); caps-everywhere MANDATORY voice (AEA §4.11); "verify syntax is valid" self-checks (§4.14); the uncalibrated ARS weights (tendency #5); guards lifted by chat words (conflicts with hook-backed halts that must not be bypassable from chat); reviewer step-down tier (`sonnet`/`medium` reviewers invert reviewer ≥ builder); advisory-only, never-blocking PR review; readiness/risk scores (non-deciding); `skip` on non-deterministic assertions (passes by silence — O27); the five-server `.mcp.json` with `@latest` (MCP minimalism); AI-DLC's Opus 4.8 model recommendation (dated; superseded). Multi-lens note: AI-DLC's lens/judge set runs one runtime under one contract — decomposition by concern, not independent lenses per AEA §4.13; adopt the structure (kill-first, severity-only decision, ledger) and source lens independence from different methodology, as §4.13 requires.

## 9. File-level change map

| File | Action | Size guidance |
|---|---|---|
| `SKILL.md` | line 24 calibration; Step 4 bullet (session reports); Step 4 brief-field count 8 → 10; Step 3 EVOLVE bullet gains "route each correction to rule / check / discard"; Reference table gains `cc-session-reports.md`; Troubleshooting +1 (hook never blocks); description +1 trigger ("write the session report standard") | ≤ 290 lines / ≤ 34,500 B |
| `references/cc-skills-and-hooks-composition.md` | §1 fail-direction column + advisory tier; §4 rewrite (exit codes, JSON, config shape, event set); §5 bounded Stop hook + health carrier + spec-file tamper check; §6 examples corrected; Pattern D product-fact markers | may grow ≤ +40% (14,638 → ≤ 20,500 B) |
| `references/cc-delegation-patterns.md` | §1 model refresh; §2 fields 9–10; §3 `blocked`, identity marker, write-before-cap, failure ladder; §4 cycle cap, receipt freeze, kill-first, worktree caveat; §5 cap-table name verification; §6 ultracode off | ≤ +30% |
| `references/cc-prompt-design-patterns.md` | §2, §6, §10 additions; Output-discipline session-report line; line 57 model | ≤ +20% |
| `references/cc-environment-design-patterns.md` | §2 three-tier + one-owner; §8/§Pattern-D markers; §10/§12 locks; built-in table model column | ≤ +15% |
| `references/cc-methodology-patterns.md` | §4 correction routing; §7 deviations register | ≤ +8% |
| `references/source-grading-and-tagging.md` | §4 assumption-status rule | ≤ +5% |
| `references/cc-anti-patterns.md` | line 195 model; three **candidate** rows appended to the "not promoted" note (unbounded Stop hook; exit-code enforcement-as-preference; two owners per rule) — candidates only; promotion needs 3 deployments | ≤ +5% |
| `references/cc-session-reports.md` | NEW | ≤ 180 lines |
| `references/troubleshooting.md` | +1 entry (hook never blocks) | — |
| `schema/cc-design-brief.schema.json` | `report_dir` property | — |
| `references/remediate-mode-execution.md`, `chat-to-code-handoff-patterns.md` | handoff §3: assumption tags travel in the bundle; REMEDIATE: finding IDs persist across REQUEST_CHANGES cycles (ledger) | ≤ +5% |

## 10. Description (draft, 668 → ≤ 700 chars)

Current description retained verbatim except: append ", session-report standards" after "EXECUTION_PLAN.md remediation plans" in the output list. No trigger vocabulary changes; the modes are unchanged. Routing collision check: "session report" does not collide with rootnode-session-handoff ("session handoff" — different artifact, different trigger: the report is written by the CC run; the handoff is written at CV close) — add the sentence "Do NOT use for session handoff documents (rootnode-session-handoff)" to the negative-trigger list if the measured length allows; otherwise rely on the distinct noun.

## 11. Composition tests (D9c at design time; D9a at build)

| Case | Expected with v5.0 | Expected failure on v4.2 |
|---|---|---|
| C1 "Design a PreToolUse hook that blocks writes to `migrations/`" | `exit 2`, `matcher` string, `hooks` array, stderr names the next step, off-switch env var | `exit 1` + `matchers` array (non-blocking) |
| C2 "Write a session prompt for an unattended 3-phase migration" | Early-stop block present; report write in scope; `report_dir` from brief; end-state digests; continuation phrase per halt | No report; no early-stop countermeasure |
| C3 "Add a verification iron-law Stop hook" | `stop_hook_active` honored; no-progress cap; evidence-named block reason | Unbounded Stop hook |
| C4 "Design a Builder→Refuter loop for repo X" | Brief fields 1–10; cycle cap 2; `blocked` outcome; identity marker; receipt freeze; Haiku 5.5 scout | 8 fields; no cap; Haiku-tier unnamed |
| C5 "We hit friction: the agent keeps editing files after review" (EVOLVE) | Routes the correction (rule vs check vs discard); proposes receipt-freeze hook with evidence threshold | Prose rule only |
| C6 Model question: "which model for the Refuter?" | Opus 5.5 or above, reviewer ≥ builder, effort note, dated marker | Opus 5 |
| C7 Routing: "build me a session handoff" | Does not activate (session-handoff) | — |

D9a: two arms (v4.2 installed vs v5.0 installed), grader on Opus 5.5, cases C1–C6; arm verified by loaded-Skill listing + LF digest (SBD §3.9 arm hygiene). One test pass, one fix pass, ship.

## 12. KF blocks this spec surfaces (routed via the catalog spec §3.5)

CC_EG §6 (hooks-vs-prompts worked example gains the exit-code contract and the bounded-Stop rule; the three-tier enforcement model); CC_EG §3.3 (brief fields 9–10); CC_EG §3.5 (cycle cap, `blocked`, Haiku 5.5 row); CC_EG §5.7 (receipt freeze as an end-state corollary); CC_EG §5.9 (early-stop countermeasure cross-reference); AEA §4.14 (the Anthropic "run a real check" block as the canonical external-verification template; the early-stop block as the canonical non-self-verification continuation); AAP §6 (three structural candidates, unpromoted); build_context (O28 candidate: the exit-code claim — a stale proxy that survived two major versions because the check was against memory of the docs, not the docs).
