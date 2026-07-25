# root_skill_5gen_alignment_design.md

**Version:** 2.0 — REVISED for Claude Opus 5 GA (7/24/26). Supersedes v1.3 in full. v1.3's D1–D3 are **UNLOCKED and re-decided** here; its landscape table (§1) is obsolete. Workstream structure survives; scope expands.
**Repo home:** `design/root_skill_5gen_alignment_design.md` — committed on the release branch.
**Cycle:** 5-generation alignment — successor to the Opus 4.8 alignment cycle (catalog v3.1)
**Status:** APPROVED FOR CC EXECUTION — D1–D8 locked by operator 2026-07-24. Companion artifact: the CC session prompt (`root_5gen_alignment_session_prompt.md` v2.3) — chat-paste only, NOT committed.
**Scope class:** Calibration-scope change + **methodology change** (verification-instruction discipline; tendency taxonomy expansion) + contract change (prompt-compilation delivery) + description/tier sweep. This is materially larger than v1.3 scoped. SBD §11 catalog-wide consistency discipline applies.

---

## 0. What changed since v1.3, and why this is a re-decision not a patch

v1.3 locked D1–D3 on 7/21/26 against a landscape in which Opus 4.8 was the current Opus and the Fable fallback target. On **7/24/26 Anthropic released Claude Opus 5** (`claude-opus-5`). Opus 4.8 now sits in the Legacy models section of the platform models overview; Opus 5 is Anthropic's front-page default recommendation.

Three consequences, in ascending order of impact:

1. **D1's primary model no longer exists as a current model.** Executing v1.3 would ship a catalog calibrated to a legacy-classified model as "primary." Mechanical fix.
2. **Effort guidance inverted.** The 4.7/4.8 rule was "start at `xhigh` for coding and agentic." Opus 5's rule is start at `high` (the default) and use `low`/`medium` liberally as the primary cost control. Every effort recommendation in the catalog is now pointing the wrong direction by default.
3. **Anthropic's Opus 5 prompting guidance directly contradicts a load-bearing root.node pattern.** The guide instructs removing explicit verification instructions because they cause over-verification, and instructs not using subagents to verify the model's own work. root.node's quality gates, validation stages, critic-gate, and CC verification topology are built on exactly that shape. This is not a sweep line. It is a methodology decision, and it is the most consequential finding in this cycle. See D4.

Phase 0 of the CC pass (executed 7/24) independently surfaced (1) plus four scope findings that are folded in below as D5–D8.

---

## 1. Model landscape (verified 7/24/26 from official Anthropic sources)

### Current models (platform "Latest models comparison")

| | **Fable 5** | **Opus 5** | **Sonnet 5** | **Haiku 4.5** |
|---|---|---|---|---|
| API ID | `claude-fable-5` | `claude-opus-5` | `claude-sonnet-5` | `claude-haiku-4-5-20251001` |
| Price /MTok | $10 / $50 | **$5 / $25** | $3 / $15 (intro $2/$10 thru 8/31/26) | $1 / $5 |
| Context | 1M | **1M (default = max)** | 1M | **200k** |
| Max output | 128k | 128k | 128k | 64k |
| Thinking | Adaptive, always on | **Adaptive, on by default** | Adaptive | **Extended thinking only** (no adaptive) |
| Reliable cutoff | Jan 2026 | **May 2026** | Jan 2026 | Feb 2025 |
| Latency | Slower | Moderate | Fast | Fastest |

Opus 4.8 and Sonnet 4.6 have moved to the **Legacy models** section. Both remain available on all platforms.

### Opus 5 — facts that drive this design

- **Released 7/24/26**, available on Claude API, Bedrock, Google Cloud, Microsoft Foundry, and all consumer surfaces. New default on Claude Max; strongest model on Claude Pro.
- **Same price as Opus 4.8** ($5/$25). Anthropic frames it as near-Fable-5 intelligence at half Fable's cost.
- **Full effort ladder** `low` → `medium` → `high` → `xhigh` → `max`, no beta header. API default `high` on Claude API and Claude Code.
- **Recommended effort:** start at `high` (default); step to `xhigh` for demanding coding/agentic work, `max` when a task justifies unconstrained spend; use `low`/`medium` liberally as the primary cost/latency control wherever evals show quality holds. Anthropic explicitly says to re-run an effort sweep rather than carry settings over from a prior model.
- **Breaking change vs 4.8:** thinking is on by default, and `thinking: {"type": "disabled"}` is accepted **only at effort `high` or below** — `xhigh`/`max` with thinking disabled returns 400.
- **Effort controls thinking volume, not visible response length.** Lowering effort does not reliably shorten responses; length must be prompted for.
- **Safety classifiers on Opus 5**, expected to intervene ~85% less often than Fable 5's. Flagged requests **fall back to Opus 4.8 by default** in Claude.ai, Claude Code, and Cowork; fallback to 4.8 can also be enabled on the API. Biology requests blocked on Fable 5 now route to Opus 5 rather than 4.8.
- **New in beta:** mid-conversation tool changes (`mid-conversation-tool-changes-2026-07-01`); `fallbacks` gains a `"default"` mode applying Anthropic's recommended fallback models by refusal category.
- **Prompt cache minimum lowered** to 512 tokens (from 1,024 on 4.8).
- **Fast mode** at ~2.5x speed, $10/$50 (Claude API only; not on Bedrock/GCP/Foundry).
- **No data retention requirements for general access** — unlike Fable 5, which is a Covered Model with 30-day retention and no ZDR. This inverts the v1.3 guidance that treated no-ZDR as the frontier-tier constraint.
- **Alignment:** Anthropic's automated behavioral audit scores Opus 5 as its most aligned model to date — better Constitution adherence than Opus 4.8, Sonnet 5, or Fable 5; lowest deceptive-behavior rates; least susceptible to misuse.

### Opus 5 documented behavior deltas vs Opus 4.8

These come from the official prompting guide and the what's-new page, not community reporting. Each maps to a catalog change below.

| Behavior | Direction | Anthropic's prescribed response |
|---|---|---|
| Conversational response length | **Longer** | Prompt explicitly for concision; pair a short reminder near the end of a long system prompt |
| Written deliverables (files on disk) | **Longer** | Add explicit length calibration for authored documents |
| Agentic progress narration | **More** | Describe the update cadence and shape you want; positive examples beat prohibitions |
| Self-verification | **Automatic** | **Remove** explicit verification instructions — they compound and cause over-verification |
| Subagent delegation | **More readily** | Cap delegation; do not use subagents to verify the model's own work |
| Correction narration | **More** | Restrict corrections to those that change the user's code, conclusions, or decisions |
| Task scope | **Expands** | Constrain scope explicitly; deliver at the scope intended |
| Conservative review instructions | **Followed literally** | "Only report high-severity" / "be conservative" causes under-reporting — ask for everything, filter in a separate pass |
| Thinking-disabled artifacts | New failure mode | Tool calls leak as text; internal XML tags leak. Keep thinking on and control cost with effort instead |

### Sources

anthropic.com/news/claude-opus-5 · platform.claude.com/docs/en/about-claude/models/whats-new-opus-5 · .../models/overview · .../build-with-claude/effort · .../build-with-claude/prompt-engineering/prompting-claude-opus-5 · .../build-with-claude/refusals-and-fallback

**Documented conflict, unresolved:** the what's-new page names `server-side-fallback-2026-07-01` for the new `"default"` fallbacks mode; the refusals-and-fallback page states the beta header must carry exactly `2026-06-01`. Both read as current. Do not assert either in a KF — carry as V9 below. Separately, the refusals page is still written as Fable-5-only while the Opus 5 announcement documents Opus 5 classifiers; the docs lag the release.

---

## 2. D1 (revised) — Calibration scope

**New scope: Opus 5 + Sonnet 5 dual-primary; Fable 5 integrated-aware; Opus 4.8 fallback-graceful; Sonnet 4.6 legacy-graceful; Haiku 4.5 graceful-with-extended-thinking. Mythos 5 / Mythos Preview out of scope.**

- **Opus 5 → primary**, replacing Opus 4.8. Anthropic's default recommendation, same price as its predecessor, step-change capability, and the strongest model available to Pro subscribers. Its documented behavior deltas are substantial enough that calibrating to 4.8 would actively misfit.
- **Sonnet 5 stays primary.** Unchanged from v1.3: it is the default runtime on Free and Pro, so the majority of CP-side Skill invocations execute there.
- **Fable 5 stays integrated-aware, not primary.** v1.3's reasoning holds and strengthens: Opus 5 delivers near-Fable capability at half the cost, which further narrows Fable's routine-use case to long-horizon autonomous work and 1M-context tasks where its edge is worth $10/$50. The integration floor from v1.3 stands.
- **Opus 4.8 → fallback-graceful. This is a new category, not a demotion label.** Opus 4.8 is no longer a model users choose, but it is a model users are *silently served*: it is the default fallback destination for classifier-flagged requests on both Opus 5 and Fable 5 in Claude.ai, Claude Code, and Cowork. A Skill invoked on Opus 5 can therefore execute on Opus 4.8 mid-session without the operator knowing. Skills must produce correct-shape output there. Distinct from legacy-graceful (a model the user may still deliberately select) and from primary (a design-and-test target).
- **Sonnet 4.6 → legacy-graceful.** Unchanged from v1.3.
- **Haiku 4.5 → graceful-with-extended-thinking.** Unchanged in posture, but now materially distinct: it is the only current model at 200k context and the only one using extended thinking rather than adaptive thinking. Both facts need explicit statement rather than inheritance.

**Dual-primary tie-break (revised):** where Opus 5 and Sonnet 5 behavior diverges, document both. T3 Skills favor Opus 5 behavior; T1/T2 favor Sonnet 5. Where Opus 5's documented deltas (verbosity, narration, scope expansion, delegation) have no Sonnet 5 equivalent confirmed, state the delta as Opus-5-specific rather than generalizing it across the tier.

**Revision trigger:** a Sonnet 6 / Opus 5.x release, or a Fable pricing change making it routine, re-opens this decision. Given two landscape shifts inside one cycle, see D8.

**Rejected — hold Opus 4.8 as primary:** it is legacy-classified on the platform docs and superseded at identical price. **Rejected — Opus 5 sole-primary:** Sonnet 5 still carries the CP-side invocation volume. **Rejected — tri-primary including Fable:** the token economics argument from v1.3 is unchanged and Opus 5 makes it stronger.

---

## 3. D2 (revised) — Tier model and effort guidance

Keep the 3-tier structure. Two changes beyond v1.3's relabel.

**New T3 label:** "High-effort recommended — run on Opus 5 or Sonnet 5. Both default to `high`, which is the recommended starting point; step up to `xhigh` for long-horizon agentic work. Quality degrades at `low` effort and on legacy models."

Note this is a *different* label than v1.3's, not just different model names. v1.3 said "at `high`+" against a landscape where `xhigh` was the recommended coding/agentic start. Opus 5 inverts that: `high` is the start, `xhigh` is the step-up for demanding work, and `low`/`medium` are legitimate primary cost controls rather than degraded modes.

**Effort guidance sweep (new, catalog-wide).** Every effort recommendation in the catalog was written against 4.7/4.8's "start at `xhigh`" rule. All of it now points the wrong way for the primary models. This is a distinct change surface from tier markers — 149 effort hits across 38 files per the Phase 0 sweep — and it needs its own classification pass, not a find-and-replace.

**Tier re-assessment:** unchanged in method (per-Skill, D9 Tier C minimum, Tier A/B where the harness exists), but the expected outcome changes. Opus 5 raises the capability floor at the same price point, so more T3 markers are likely obsolete than v1.3 anticipated. v1.3's ≥5-move → v4.0 escalation rule is now near-certain to fire; D3 pre-resolves it.

**Marker gap:** extend to **all 6** Skills missing inline calibration markers — critic-gate, mode-router, repo-hygiene (design scope) plus cc-design, handoff-trigger-check, profile-builder (surfaced by the Phase 0 sweep). Marginal cost, and leaving three known gaps open to close later is how this backlog item survived two cycles.

---

## 4. D3 (revised) — Release is catalog v4.0

**v4.0, not v3.2.**

Rationale: v1.3 chose minor on the grounds that structure, surface roles, and packaging shapes were unchanged — still true. But three things now cross the major line independently. The behavioral tendency taxonomy expands (D4), which propagates into every consumer of behavioral-tuning and OPT_REF. The prompt-compilation delivery contract changes (D5), which is a public product-surface change. And D2's own ≥5-tier-move escalation rule is near-certain to fire. Declaring v4.0 up front avoids a mid-execution HALT and re-decision, which is the churn pattern this cycle is explicitly trying to avoid.

**Release-expectation rule (carried from v1.3):** all 27 Skills expected to bump; a zero-edit Skill is HALT-and-ask, because the mixed-version umbrella remains an undecided pattern.

**Rejected — v3.2 with escalation-on-discovery:** technically correct under the letter of SBD version discipline, but it defers a near-certain decision into the middle of a release run.

---

## 5. D4 (NEW) — Verification-instruction discipline

**This is the cycle's methodology decision.** Anthropic's Opus 5 guidance says to remove explicit verification instructions and not to use subagents to verify the model's own work. root.node's architecture is dense with verification instructions. Taken literally, that guidance would gut the quality gates. Taken as written, it does not — but the distinction has to be drawn explicitly, because it is not currently drawn anywhere in the methodology.

**The line: remove self-directed re-checking; keep external-artifact verification.**

- **Self-directed re-checking** asks the model to re-examine its own reasoning or output with no new information: "double-check your answer," "re-verify before responding," "include a final verification step," "use a subagent to verify your work." Opus 5 already does this. Instructing it compounds the behavior and burns tokens for no quality gain. **Remove.**
- **External-artifact verification** asks the model to check a claim against a source outside its own output: read the file, run the diff, execute the test, inspect the rendered page, confirm the tag exists. This is not re-checking — it is evidence grounding, and it is the discipline that catches the failure class root.node's Observation 21 family documents. Opus 5's own behavior (building test harnesses, verifying against reality) reinforces rather than duplicates it. **Keep, and keep imperative.**

**Where this lands:**
- New principle section in **AEA** — this is surface-invariant and governs both CP and CC.
- **SBD** quality gate: D9 remains (an independent grader on a separate artifact is external verification, not self-re-checking). Audit the gate text for self-re-check phrasing.
- **CC_EG** agent topology: the Critic role survives as an independent reviewer of a *different* agent's work; "use a subagent to verify your own output" does not. The verification-topology section needs this distinction stated.
- **critic-gate** Skill: unaffected in purpose (it is cross-agent review), but its invocation guidance should not read as self-verification.
- **behavioral-tuning** and **OPT_REF**: over-verification becomes a documented tendency with a countermeasure that is *removal of instructions*, which is a new countermeasure shape for the taxonomy.
- Catalog-wide sweep for self-re-check phrasing. New sweep patterns: `double-check`, `re-verify`, `verification step`, `verify your (own )?work`, `subagent to verify`.

**Second, related finding — conservative-instruction literalism.** Opus 5 follows "only report high-severity issues" and "be conservative" literally and under-reports. root.node's audit Skills (project-audit, prompt-validation, full-stack-audit, repo-hygiene, critic-gate) are exactly the surface where that phrasing appears. Sweep for it; replace with report-everything-then-filter where found. New patterns: `high-severity`, `be conservative`, `only report`, `only flag`.

---

## 6. D5 (NEW) — prompt-compilation delivery contract

Phase 0 (V6) read `rootnode-prompt-compilation/SKILL.md:224-231` and found the current contract **prescribes inline code-block delivery**. So v1.3's W4 was mis-framed: this is not a defect within the contract, it is the contract. Hypotheses H1–H4 are moot.

**Decision: change the contract.** Project Mode completes by creating one complete file per scaffold artifact — the CI file and each KF as separate uploadable files, `{code}_` prefixed. Inline delivery is permitted only where the runtime cannot create files, and must be flagged explicitly when used.

Rationale: inline blocks are unusable for the actual downstream action (uploading files into a Claude Project), and Opus 5's longer written deliverables make long inline blocks worse. The contract was written for a runtime that could not create files; that constraint no longer holds on the primary surfaces.

Because this changes the Skill's public product surface, it belongs in a major release — reinforcing D3.

**Behavioral test (D9):** scaffold a 3-KF project via the updated Skill on Opus 5 and Sonnet 5. Pass = every scaffold artifact delivered as a file on both runs.

---

## 7. D6–D8 (NEW) — scope resolutions from Phase 0

**D6 — Context budget is a rebuild, not a note.** Phase 0 surfaced that Anthropic Projects appears to have moved from a fixed ~66,500-token RAG threshold to automatic RAG when knowledge exceeds the context window. If confirmed (V3), the ~66,500 figure is not stale-but-directionally-right — it is a wrong mental model, and context-budget's Step 4 math, tier bands, and budget-pool table all derive from it. Compounding: the "33% of 200K" derivation is doubly obsolete now that every current model except Haiku 4.5 is at 1M.

Rebuild `rootnode-context-budget` and the OPT_REF context-budget section against the platform's actual current model. **Gate:** confirm from the Anthropic support article first. If unconfirmed, fall back to explicit tolerance language ("measured under the 200K-era platform; revalidation pending") and queue a Calibration Lab session — never assert an unmeasured replacement threshold.

**Preserve the distinction the old framing blurred:** a model's context window is not the Projects RAG threshold. They were numerically entangled under the 200K era and must be stated separately now.

**D7 — Packager version handling authorized (expanded 7/25/26).** `build_release_artifacts.py:59` pins `CATALOG_VERSION = "v3.1"`; the release cannot produce a v4.0 bundle without it. Authorize the constant bump to `v4.0` — narrowly, that line only, in that file.

**Expansion:** additionally author a version-agnostic `generate_release_notes.py` at repo root, adapted from `audit/v3_1-release/generate_release_notes.py`, taking version and tier labels as parameters rather than constants. The v3.1 artifact hardcodes the version throughout and its `TIER_LABEL` dict carries `"Opus-recommended (T3)"` — the exact label D2 retires — so it needs editing regardless. v4.0 requires 27 per-Skill notes files whose tier labels all change; hand-assembly across three variant templates is the churn class this cycle exists to prevent, and inconsistency across 27 hand-written files is invisible until it renders. Repo root is the correct home under the `audit/README.md` convention (standing tooling at root, cycle artifacts under `audit/v<N>-*/`). Leave the v3.1 original untouched — historical and correct where it sits. Any *other* change to `build_release_artifacts.py` remains recommendation-surface — HALT and report.

**D8 — Canonical-KF mirror completion.** OPT_NOTES and AUDIT_FRAMEWORK are named as W1 targets but are absent from `audit/canonical-kfs/`, so the O10 staleness diff structurally cannot catch their drift. Add both to the mirror this cycle. This is the architecture fix behind a recurring class of drift, not housekeeping.

**Landscape-volatility discipline (methodology observation, for build_context).** Two model landscapes inside one cycle, with locked decisions invalidated by the second. The design-doc pattern should isolate the landscape as a dated, independently-versioned block that decisions *reference* rather than embed, so a landscape refresh does not unlock the decision record wholesale. Codify in build_context; evaluate for AEA.

---

## 8. Workstreams

Order matters: KFs are canonical, Skills derive.

**W0 — Verification-instruction + conservative-instruction sweep (NEW, runs with W2).** Patterns in D4. Classify every hit: self-re-check → remove; external-artifact → keep and confirm imperative voice; ambiguous → flag for review. This sweep is the one most likely to surface false positives; do not batch-apply.

**W1 — Canonical KF updates.** Work order:
1. **OPT_NOTES** — header calibration line → D1 scope. New "5-Generation Landscape" section: §1 landscape table, Opus 5 behavior deltas, effort ladder with the inverted starting-point rule, thinking-on-by-default and the `xhigh`/`max` disable restriction, fallback semantics (Opus 5 → Opus 4.8; Fable → configurable; `"default"` mode pending V9), Fable refusal-aware prompt design (carried from v1.3, now extended: the `reasoning_extraction` refusal category confirms the "don't ask for reproduced reasoning" guidance), model-selection guidance across the five in-scope models, no-ZDR as a Fable-specific constraint rather than a frontier-tier one.
2. **OPT_REF** — full body recalibration (closes playbook §6 debt; ~45 4.7-era refs per the sweep). Tendency taxonomy expansion per D4 and §9 below. Context-budget section per D6. Effort tables per D2.
3. **AEA** — new verification-instruction discipline section (D4). Landscape-volatility discipline (D8) if adopted.
4. **CC_EG** — verification topology and Critic role clarified per D4; subagent delegation caps; CC default-model and effort facts (V4).
5. **AUDIT_FRAMEWORK** — Dimension 6 anchor text; conservative-instruction literalism as an audit target.
6. **SBD** — quality gate audit for self-re-check phrasing; D9 grader guidance to Opus 5 / Sonnet 5.
7. **AAP** — grep-driven touch; evaluate over-verification and scope-expansion as catalog entries.
8. **CALIBRATION_SCOPE_DECISION + TIER_ASSIGNMENTS** successors carrying D1/D2.
9. **Release playbook** — §6 debt closures; v4.0 conventions.

**W2 — Mechanical sweep** (all 27 Skills + KFs + README). v1.3 patterns plus: `Opus 5`, `opus-5`, `4\.8`, `Fast mode`, `max effort`, `prompt cach`, plus D4's patterns. README Model Compatibility rewritten; compatibility matrix and per-Skill tier markers regenerated against *this pass's* tier assignments.

**W3 — Deep-update Skills.** v1.3's table carries forward with these changes: **prompt-compilation** gains the D5 contract change; **behavioral-tuning** gains the full Opus 5 delta set and the removal-as-countermeasure shape; **context-budget** is a rebuild per D6, not a note; **cc-design** gains subagent-delegation caps and the D4 topology distinction; **domain-agentic-context** gains the refusal-category table, `fallback` content-block semantics, `usage.iterations` accounting, and the "instrument refusals as their own signal" pattern (a refusal is HTTP 200 — error-rate monitoring never sees it); **domain-software-engineering** gains the Opus 5 cyber-classifier posture (source-code vulnerability finding allowed; binary scanning, pentesting, exploit generation blocked; ~85% less intervention than Fable) and the conservative-review-instruction fix; **skill-builder** D9 grader guidance to Opus 5 / Sonnet 5; the 6 marker-gap Skills per D2.

**W4 — Tokenizer revalidation (conditional).** Now three models to measure: Opus 5, Sonnet 5, Opus 4.8 (fallback target). Same gate as v1.3 — measure via `count_tokens` if API access exists, otherwise explicit tolerance language, never a point estimate under an unmeasured tokenizer.

**W5 — Release v4.0 + propagation.** Per the release playbook, unchanged in process. D7 authorizes the packager constant.

---

## 9. Tendency taxonomy expansion (W1 sub-decision)

The current taxonomy is 10 tendencies. Opus 5's documented deltas do not fit cleanly as columns on the existing rows.

**Refactor verbosity into a three-surface family** — conversational response length, agentic progress narration, and written-deliverable length. These have different triggers and different countermeasures on Opus 5 (explicit concision instruction; cadence description; document length calibration), and collapsing them loses the fix.

**Add four:** over-verification (countermeasure = *remove* instructions, a new countermeasure shape); scope expansion (distinct from the existing over-exploration, which is search breadth — this is deliverable-boundary drift); subagent over-delegation; correction narration.

**Treat as prompt/environment-conditional defects rather than tendencies:** conservative-instruction literalism (a prompt defect the model exposes) and thinking-disabled artifacts — tool calls leaking as text, internal XML tags in visible output (an API-configuration failure mode, with the notable sub-finding that a system-prompt rule telling the model not to think *increases* tag leakage).

Exact final count and numbering settle during the OPT_REF rewrite. Flag if the refactor would break downstream references by number.

---

## 10. Verification items

| ID | Item | Gates |
|---|---|---|
| V1 | Opus 5 availability across CP / CC / Cowork surfaces and subscription tiers | OPT_NOTES, README |
| V2 | Sonnet 5 system card — behavioral deltas vs 4.6 and vs Opus 5 (**unresolved from the first pass**) | behavioral-tuning tables, OPT_REF columns |
| V3 | Projects RAG behavior — fixed threshold vs automatic-by-window (**D6 gate**) | context-budget rebuild scope |
| V4 | Claude Code default model and effort default post-Opus-5 | cc-design, CC_EG |
| V5 | Opus 4.8 and Sonnet 4.6 official deprecation timelines | fallback-graceful and legacy-graceful language |
| V6 | ~~prompt-compilation contract~~ **RESOLVED** — contract prescribes inline delivery; D5 supersedes | closed |
| V7 | Sweep manifest = actual change surface | W0/W2/W3 scope |
| V8 | `build_release_artifacts.py` read in full pre-run; surface map, suffixes, 29-assert, `write_bundle()` | W5 packaging |
| V9 | **NEW** — server-side fallback beta header date conflict (`2026-06-01` vs `2026-07-01`) | any KF statement of fallback API shape |
| V10 | **NEW** — Opus 5 system card, for alignment/safety claims beyond the announcement | OPT_REF, domain-software-engineering |

---

## 11. Out of scope

Unchanged from v1.3: Phase 31f/g/h audit sequence; R6–R11 CC_EG codification; Distribution Blocks 2/3/5; Calibration Engine build; Hermes/UCIS; rootnode-for-code plugin. Adding: the packager CLI-argument refactor (D7 follow-on) and any Mythos-tier calibration.

---

## 12. Decision record

| Decision | Status |
|---|---|
| D1 — Opus 5 + Sonnet 5 dual-primary; Fable integrated-aware; **Opus 4.8 fallback-graceful (new category)**; Sonnet 4.6 legacy-graceful; Haiku 4.5 graceful-with-thinking | LOCKED 7/24/26 (operator) |
| D2 — T3 relabel to Opus 5 / Sonnet 5 at `high`+; catalog-wide effort-guidance inversion; all 6 marker gaps | LOCKED 7/24/26 (operator) |
| D3 — catalog **v4.0** (escalated from v3.2) | LOCKED 7/24/26 (operator) |
| D4 — verification-instruction discipline: remove self-re-checking, keep external-artifact verification; conservative-instruction literalism sweep | LOCKED 7/24/26 (operator) |
| D5 — prompt-compilation delivery contract changes to file-per-artifact | LOCKED 7/24/26 (operator) |
| D6 — context-budget is a rebuild, gated on V3 | LOCKED 7/24/26 (operator) |
| D7 — packager `CATALOG_VERSION` bump authorized (that line only) **+ author a version-agnostic `generate_release_notes.py` at repo root** (expanded 7/25/26) | LOCKED 7/24/26, expanded 7/25/26 (operator) |
| D8 — OPT_NOTES + AUDIT_FRAMEWORK added to canonical-kfs mirror; landscape-volatility discipline codified | LOCKED 7/24/26 (operator) |
| v1.3 D1–D3 | **SUPERSEDED** |
