# rootnode-skill-builder_ap_warnings.md

Anti-pattern warnings produced during D7 catalog scan for `rootnode-skill-builder` v3.0. Per `root_SKILL_BUILD_DISCIPLINE.md §4.3`. Produced because D7 surfaced one catch.

Build date: 2026-05-08
Predecessor AP-warnings: v2.1 produced none beyond the §3.4 Kitchen Sink expectation (workflows co-located in one Skill); v3.0 inherits and extends that disposition.

---

## Summary table

| Pattern | Catalog reference | Surface tag | Status | Disposition |
|---|---|---|---|---|
| §3.4 Kitchen Sink | `root_AGENT_ANTI_PATTERNS.md §3.4` | Structural CP-side | CATCH | ACCEPTED with three-part decomposition test pass |

One catch, expected per design spec §18.9. ACCEPTED disposition with formal decomposition test result.

---

## Per-catch detail

### §3.4 Kitchen Sink — multiple workflows co-located

**Pattern name:** Kitchen Sink (multiple semi-independent concerns co-located in a single Skill, structural CP-side)

**Catalog reference:** `root_AGENT_ANTI_PATTERNS.md §3.4`

**Surface tag:** Structural CP-side

**Catch context:** v3.0 carries 6+ workflows in one Skill: Build New Skill, Review Existing Skill, Revise Existing Skill, Iterate the Skill, Optimize the Description, Compare Skill Versions, plus the Multi-Environment Adaptation cross-cutting principle. A naive D7 walk flags this as Kitchen Sink — the workflows could in principle belong in separate Skills.

**Disposition: ACCEPTED with reasoning per design spec §18.9 three-part decomposition test.**

#### Test 1 — Lifecycle coherence

**Question:** Do the workflows form a sequential or iterative lifecycle, or could they operate independently?

**Result: PASS.** The workflows are sequential lifecycle stages of a single Skill build:

```
design → build → review → iterate → optimize description → compare versions → ship
```

Every workflow operates on the same artifact (a Skill). A user iterating on a Skill (D9 testing) returns to the same governance context (gates + quality gate) that produced the build. A user optimizing the description loops back through the build pipeline's Step 2a. A user comparing versions invokes the same quality-gate criteria that scored each version.

Splitting into separate Skills would force the user to invoke `skill-builder` for new builds, then a separate `skill-tester` for iteration, then a separate `skill-comparator` for comparison — each with the same governance imports, the same rubric semantics, and the same methodology preservation discipline. The lifecycle coherence is the design intent, not a packaging accident. (See design spec §1.3 "Workflow coherence (anti-Kitchen-Sink rationale)" for the architectural argument.)

#### Test 2 — Governance duplication

**Question:** Would splitting into separate Skills (e.g., `skill-builder` + `skill-tester` + `skill-comparator`) require duplicating the governance floor or cross-Skill composition contracts?

**Result: PASS (governance duplication confirmed; integration prevents it).**

Concretely, the governance floor each split Skill would need:

- **Pre-build gates** (decomposition, warrant, ecosystem fit) — apply to new builds AND review/iteration of existing Skills (you re-walk Gate 1 to confirm the Skill's mechanism remains correct after revision).
- **9-dimension quality gate** — applies whether the workflow is a new build, a review, an iteration, an optimization, or a comparison. Each workflow's verdict is a quality gate output.
- **Methodology preservation discipline** (§7) — applies to revision, iteration, and version comparison. Each split Skill would need to know what's preserved verbatim from a predecessor.
- **Content-class policy** (§7) — applies to any workflow that touches ported content (the description optimizer, the comparator, the grader all rely on the same verbatim/tone-adapted treatment).
- **Cross-Skill contract semantics** — the Producer→Consumer chain with `rootnode-repo-hygiene` is a single contract that surfaces across multiple workflows.

Duplicating the governance floor across 3+ split Skills would (a) bloat each Skill's reference content, (b) introduce drift risk (the gates in `skill-builder` could evolve out of sync with the gates in `skill-tester`), (c) break methodology preservation (a v2 of one split Skill would have to re-derive what the others' v2 already established).

#### Test 3 — Independent invocation

**Question:** Would a user ever invoke one workflow without the others being available?

**Result: PASS (no — workflows are not independently invoked).**

Practical examples:

- "Test my Skill" implies the build governance context. The user is not asking for arbitrary behavioral testing of arbitrary content; they are asking whether their Skill (built per the build discipline) achieves its claimed effect under realistic prompts. Tier A invocation of D9a needs the build's grader subagent prompt and the rubric assertions defined per the Skill's Quality Gate.
- "Compare these two versions" implies the build's quality gate context. The comparison rubric inherits content/structure dimensions from the build methodology; the analyzer needs the build's understanding of what makes a Skill better.
- "Optimize the description" implies the build's description discipline. The optimizer's revision prompt encodes the description structure (verb-based + trigger phrases + negative triggers) from the build methodology.

The workflows are not independently useful as standalone Skills. They are the operational expression of the single Skill build methodology applied to different lifecycle stages.

---

## Final disposition

**ACCEPTED.** All three decomposition tests pass. The Kitchen Sink catch is a deliberate architectural choice driven by lifecycle coherence and governance integration; the alternative (split Skills) would force methodology duplication and break cross-workflow consistency.

The catch and its disposition are documented here for durable record. Future audits, future v3.x builds, and future evolution discussions read this artifact to understand that the integration was a design decision, not an oversight.

The architectural argument also lives in design spec §1.3 (workflow coherence as the intentional design intent) and design spec §18.9 (the three-part decomposition test as the verification mechanism).

---

## Other patterns scanned — no catches

| Pattern | Disposition |
|---|---|
| §2.1 Monolithic standing context | NO CATCH (SKILL.md 433 lines under bloat threshold; routing-surface design applied) |
| §3.5 Blurred Layers | NO CATCH (rules in SKILL.md, references in references/, scripts in scripts/, agents in agents/, eval-viewer in eval-viewer/; clean separation) |
| §3.6 Build-scaffolding leak | NO CATCH (no project-specific brief references in `metadata.original-source`; brand-cleanliness applied to ported HTML; no internal phase tags in user-facing surface) |
| §4.3 Manual-only Skills | NO CATCH (auto-invocation default; no `disable-model-invocation` flag) |
| §4.11 Verification-before-completion absent | NO CATCH (Quality Gate section + per-step verification language present) |
| §4.14 Stale content | NO CATCH (built today against current methodology) |

---

## Filing destination

`design/audit-artifacts/v3.0/rootnode-skill-builder_ap_warnings.md`. Operator may file a copy at `Projects/ROOT/research/` per the canonical filing destination convention (KF §4.3).

---

*End of rootnode-skill-builder_ap_warnings.md.*
