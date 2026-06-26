# root.node Skill Catalog — Opus 4.8 Alignment Rubric

**Purpose:** The single execution spec for recalibrating the rootnode Skill catalog (and README) to Claude Opus 4.8, with safe regression to Sonnet 4.6 and Haiku 4.5. Chat designs this rubric; Claude Code executes against the live `drayline/rootnode-skills` repo using `rootnode-skill-builder` methodology grounded in `root_SKILL_BUILD_DISCIPLINE.md`.

**Status:** Draft for execution. Sections marked **[APPLY NOW]** are locked and CC may execute. Sections marked **[TEST-GATED]** wait on Phase 4 empirical results before shipping.

**Scope note — no API migration.** Opus 4.8's API surface is unchanged from 4.7 (omit `temperature`/`top_p`/`top_k`; adaptive-thinking-only; effort defaults to `high` on all surfaces). The rootnode Skills contain no API calls. The migration that matters here is **behavioral framing in the prose**, not code. The only mechanical model-string work is the version sweep in §4.

---

## §0 — How to use this rubric

CC processes each Skill in the repo through four operations, in order:

1. **Version sweep** (§4) — mechanical, apply now.
2. **Voice-and-framing recalibration** (§2 + §3) — the substantive pass; apply the confirmed (relax) and universal (reframe) items now, hold the strengthen items for §7.
3. **Regression targeting** (§5) — set the tier marker per the category profile; the caveat-drop decisions are test-gated.
4. **Quality guardrail check** (§8) — verify the pass recalibrated framing without altering methodology, then re-run the validator.

The README compatibility matrix and per-Skill tier markers are regenerated from §5's validated results as the final step.

---

## §1 — Confidence ledger

Every change in this rubric traces to one of these findings. CC and reviewer should know which are Anthropic-official and which are community-inferred-and-test-gated.

| # | Finding | Source | Confidence | Status |
|---|---------|--------|-----------|--------|
| F1 | ~4x less likely to let a flaw in its own work pass unflagged; flags uncertainty; avoids unsupported claims | Anthropic announcement + System Card | High (official) | APPLY NOW |
| F2 | Better tool triggering — fewer skipped tool calls the task required | Anthropic docs (whats-new) | High (official) | APPLY NOW |
| F3 | Steadier effort calibration; better long-context + compaction recovery | Anthropic docs (whats-new) | High (official) | APPLY NOW |
| F4 | Increased verbosity / unsolicited disclaimers / unrequested preamble on code | Multiple independent hands-on reports | Medium (community, consistent) | TEST-GATED |
| F5 | Degraded instruction adherence under a strong self-plan ("told it one function, refactored three") | Multiple independent reports | Medium (community, consistent) | TEST-GATED |
| F6 | Stronger planning makes **procedural step-by-step prompts constrain rather than guide**; goal-oriented framing is the reported fix | Community inference from the planning observation | Medium (inferred) | APPLY NOW via §4 reframe (see thesis) |
| F7 | Training cutoff still January 2026; specs (1M context, 128k out, adaptive thinking) carried over from 4.7 | Anthropic docs | High (official) | Context only |

Note on F6: the *observation* is community-sourced, but the *response* — the graceful-degradation reframe in §4 — is low-risk and strictly improving across the model range regardless of whether F6 holds at full strength. It is therefore APPLY NOW, not test-gated. F4/F5 require strengthening countermeasures, which can over-steer if the reports are overstated, so those are gated.

---

## §2 — Organizing thesis (governs the whole pass)

**This is a voice-and-framing recalibration, not a rewrite.** It applies two principles root.node already owns — §4.11 calibrated voice and §4.12 / SBD §10 environment-adaptive degradation — to a new model. The methodology each Skill encodes does not change. What changes is *how the prose is calibrated* so one artifact serves the full model tier (Opus 4.8 ceiling, Sonnet 4.6 / Haiku 4.5 floor) without per-model variants.

Two consequences shape every edit:

**(a) Relaxation is model-conditional, so it is expressed as voice, not deletion.** Opus 4.8 handles self-critique and tool-firing natively (F1, F2). But Sonnet 4.6 and Haiku 4.5 do **not** share those gains — the countermeasures scaffolding those behaviors are still load-bearing on the regression targets. So we never *delete* a countermeasure that 4.8 made redundant. We *lighten its voice* (imperative → reasoned) so it stops over-steering 4.8 into the F4/F5 failure modes while remaining present for models that need it. §4.11 voice calibration is the regression-safety mechanism.

**(b) The reframe is the graceful-degradation form, so it serves the whole tier at once.** Goal-oriented framing (F6) is not an Opus-only calibration that would starve weaker models of scaffolding. The correct form — *state the outcome prominently, then provide the method as supporting structure* — gives Opus 4.8 the goal it routes from (so it treats the steps as available-not-mandatory and doesn't fight them) **and** gives Sonnet/Haiku the goal plus the scaffold they still need. It is strictly better for both. This is §4.12 degradation applied to model tier rather than tooling tier.

The whole pass therefore collapses to: **calibrate voice and framing so one Skill degrades gracefully across the tier.** This keeps changes conservative and protects D3 (methodology preservation).

---

## §3 — Bifurcated countermeasure map

### RELAX — lighten voice **[APPLY NOW]** (F1, F2)

These behaviors are native on 4.8. Where a Skill scaffolds them in heavy imperative voice, recast to reasoned voice. Do **not** remove — they remain load-bearing on Sonnet/Haiku.

- **Self-critique / honesty scaffolding** — "lead with the flaw," self-referential-fabrication guards, the multi-lens-audit *rationale framing*. Lighten the imperative emphasis; keep the instruction. (The audit *gates* themselves stay — see §8.)
- **Tool-firing / under-triggering countermeasures** — the under-firing tendency in `rootnode-behavioral-tuning` and any "remember to call the tool" nudges. De-escalate; 4.8 skips required calls far less.

**How much to lighten:** target the point where the instruction still reads as a clear expectation on a weaker model but no longer reads as a hard command that an Opus 4.8 already-aligned on the behavior would over-apply (producing the F4 over-disclaiming / over-explaining failure). When unsure, lighten less — under-relaxation is safe; over-relaxation risks Sonnet/Haiku regression.

### STRENGTHEN — sharpen countermeasures **[TEST-GATED]** (F4, F5)

Ship only if Phase 4 confirms the behavior on 4.8. If confirmed:

- **Verbosity / unsolicited preamble** — sharpen the anti-verbosity and "no preamble" countermeasures, especially in Skills that emit code or structured artifacts.
- **Editorial drift / unrequested disclaimers** — strengthen the editorial-drift countermeasure.
- **Instruction adherence under self-plan** — add a countermeasure: when the user scopes a change narrowly, honor the stated scope; surface a larger refactor as a recommendation rather than executing it unprompted. This is the F5 fix and is new taxonomy if confirmed — route to `root_OPTIMIZATION_REFERENCE.md` behavioral catalog.

These are model-conditional in the same way: if confirmed, they target 4.8 specifically. Keep them light enough not to suppress legitimate Sonnet/Haiku behavior.

---

## §4 — Procedural → goal-oriented reframe **[APPLY NOW]** (F6)

The headline calibration. Applies to **advisory step-sequences only**. Gates are exempt (§8).

**The rule.** For any procedural block framed as a bare ordered sequence ("Stage 1: do X. Stage 2: do Y."), recast so the **outcome leads** and the **steps follow as supporting method**:

- Before (procedural — 4.8 may fight it, under-specifies nothing for it to route from): *"Stage 1 — Inventory. Stage 2 — Assess. Stage 3 — Structure. Stage 4 — Produce."*
- After (outcome-anchored — serves the whole tier): *"Produce a handoff that captures every active stream at full fidelity, is persistence-correct, and is ingestion-optimized for the next session. The method that reliably gets there: inventory the session, assess each item against the persistence test, structure to the schema, then produce. Steps are the path, not a checklist to recite."*

**Gate exemption.** Hard checkpoints stay imperative and stay sequenced. A gate is any step whose skipping invalidates the output: pre-build gates, the persistence test, "decisions require rationale," validation/quality gates, "XML/format non-negotiable" type constraints. These read as commands because they *are* commands (§4.11). Do not soften them; do not reframe them as optional structure.

**Worked example — `rootnode-session-handoff` (the Skill we are rebuilding):** Its 4-stage pipeline is *advisory sequence* → reframe to outcome-anchored. But its persistence test (Stage 2), "decisions without rationale are the #1 failure," and "format non-negotiable" are *gates* → leave imperative. This Skill is a clean specimen of the split: most of its structure reframes, three load-bearing constraints stay hard.

**Test for which is which:** ask "does skipping this step produce a wrong artifact, or just a less-ordered path to the right one?" Wrong artifact → gate, keep imperative. Less-ordered path → advisory, reframe.

---

## §5 — Model-version sweep spec **[APPLY NOW]**

Mechanical, but with one halt. CC greps every `SKILL.md` + `references/**` + the repo README.

**Targets:** `4.7`, `4.6`, `claude-opus-4-7`, `claude-opus-4-6`, `Opus 4.7`, `Opus 4.6`, "Opus-primary", "Opus recommended", "calibrated for", and any model-compatibility marker or calibration line.

**Replacement rules:**
- Primary-model references → **Opus 4.8**.
- Secondary/fallback references → **4.6 / 4.7** as the prior generation.
- Tier/calibration markers (e.g. the `> Calibration: Tier 1, Opus-primary` line) → keep the abstraction where the Skill already abstracts; bump explicit versions where it pins them.
- README model-compatibility matrix → regenerate from §5 validated tier results (final step).

**Two patterns to expect** (confirmed by reading `rootnode-session-handoff`): some Skills **abstract** ("Opus-primary, see README") — their sweep target is the README matrix, not the body. Others **pin** explicit version strings in the body — those get bumped in place.

**HALT — ambiguous reference.** Do **not** auto-edit a model reference whose intent is unclear: a deliberate "works on 4.6+" capability statement reads identically to a stale "calibrated for 4.7" marker on a grep. When intent is ambiguous, flag the line for review rather than rewriting. (This is the in-scope-with-notification / halt boundary from the CC scope authorization.)

---

## §6 — Regression-targeting test design **[TEST-GATED verdicts; category profiles APPLY NOW as defaults]**

The category profile sets the **default** tier marker now; the **caveat-drop** decision waits on Phase 4. Phase 4 runs one representative per category on its target tier and compares output to the Opus baseline; the "Opus recommended" caveat is dropped only when output is equivalent.

| Category | Default tier target | Rationale | Representative for Phase 4 |
|----------|--------------------|-----------|---------------------------|
| **Synthesis-heavy audit** — project-audit, full-stack-audit, global-audit, context-budget, memory-optimization, anti-pattern-detection | Opus floor (keep "Opus recommended") | Multi-dimensional synthesis + cross-layer judgment; highest regression risk | `rootnode-project-audit` |
| **Domain packs** — business-strategy, software-engineering, content-communications, research-analysis, agentic-context | Sonnet 4.6 target | Structured application of a known framework; less open-ended synthesis | `rootnode-domain-software-engineering` |
| **Methodology / compilation** — prompt-compilation, prompt-validation | Sonnet 4.6 target (compilation may hold Opus-recommended pending test) | Compilation is generative-structural; validation is rubric-scored | `rootnode-prompt-validation` |
| **Behavioral / builder / meta** — behavioral-tuning, skill-builder, profile-builder, cc-design | Sonnet 4.6 target | Framework-driven; skill-builder/cc-design carry heavier judgment — test before dropping caveat | `rootnode-behavioral-tuning` |
| **Block libraries (retrieval)** — identity-blocks, reasoning-blocks, output-blocks, block-selection | Haiku 4.5 candidate | Lookup / selection, not synthesis | `rootnode-block-selection` |
| **Session continuity** — session-handoff | Broad compatibility (Tier 1, all tiers) | Most-used Skill; must run everywhere. The §4 graceful-degradation reframe is what makes broad compatibility real | `rootnode-session-handoff` |
| **Project brief / continuity** — project-brief, handoff-trigger-check | Sonnet 4.6 target | Structured extraction / gated check | `rootnode-project-brief` |
| **CC-only runtime** — critic-gate, mode-router, repo-hygiene | Per CC deployment; test on the model the CC env runs | In repo, not installed in this CP project; CC enumerates | `rootnode-repo-hygiene` |
| **Ecosystem context** — drayline-ecosystem | Compatibility-neutral (context, not reasoning) | Portable context; no model-sensitive reasoning | n/a (no behavioral test) |

**CC enumerates the full set from the repo** and maps any Skill not listed above to a category by function. The repo is the source of truth for the catalog count; this table is the category framework, not an exhaustive inventory (chat does not have the repo).

---

## §7 — Apply-now vs. test-gated split (CC sequencing)

CC may execute a **first pass** on the locked items while Phase 4 testing proceeds in parallel:

**Apply now (first pass):**
- §4 version sweep (with the ambiguous-reference halt).
- §3 RELAX items via voice-lightening.
- §4 procedural → goal-oriented reframe (universal, low-risk).
- §6 default tier markers.

**Test-gated (second pass, after Phase 4):**
- §3 STRENGTHEN items (F4/F5) — ship only if confirmed on 4.8.
- §6 caveat-drop decisions — drop "Opus recommended" only where the representative validated equivalent on its target tier.
- README compatibility matrix regeneration — from validated results.

First-pass output goes to a branch + PR for review before the second pass commits. This lets the mechanical and universal work land and get eyes on it while the empirical questions resolve.

---

## §8 — Quality guardrails for the pass

The failure mode of a "calibration pass" is silent scope creep into a rewrite. Guard against it:

- **D3 — methodology preservation is the hard line.** Recalibrate framing and voice; do **not** change what any Skill *does*. If an edit changes the method, the output, or the gates, it is out of scope for this pass — flag it as a separate methodology-change proposal, do not fold it in.
- **Gates stay intact.** Every pre-build gate, persistence test, validation step, and "non-negotiable" constraint survives the reframe unchanged (§4 exemption).
- **Re-run the validator** on every touched Skill. Description ≤ 1024 chars; SKILL.md ≤ 500 lines; activation precision preserved. A reframe that pushes SKILL.md over budget or blunts a description's triggers is a regression.
- **Per Phase 6 propagation:** the "Opus 4.7 primary / 4.6 secondary" calibration line appears in the seed KFs, `audit/canonical-kfs/`, installed Skill copies, **and** Project Memory's model-context entry — all four landing locations get the 4.8 bump. Do a CRLF-normalized `diff` between seed KFs and `canonical-kfs/` at session start to catch drift before editing against stale methodology.

---

## Execution boundary

This rubric is the **what** and the **how-calibrated**. The **per-file edits** happen in CC against the repo — that is deliberate, not a gap: chat does not have the SKILL.md bodies, and the edits are exactly the repetitive repo work CC is for. The CC session prompt + scope-authorization clauses + halt triggers are a separate deliverable (produced via `rootnode-cc-design` DESIGN mode once this rubric is locked).
