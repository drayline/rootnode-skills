# root_DS_skill_builder_v3.md (rev3.4)

**Design specification for `rootnode-skill-builder` v3.0**

Author: root.node seed Project · Phase 32 design CV
Predecessor: `rootnode-skill-builder` v2.1 (shipped May 2026)
Build target: `rootnode-skill-builder` v3.0
Build mechanism: CC-driven build using v2.1 methodology files as content reference. v2.1 is not invoked as an executable Skill during the build.
Status: design — scope-lock approved (rev3.4); pending Phase 32a KF precondition CV
Revision: rev3.4 (delta from rev3.3 — pre-launch verification of upstream Anthropic skill-creator source surfaced 2 implementation-level corrections: (1) scripts/ directory has 7 portable files (not 5 as rev3.3 enumerated): adds `utils.py` shared utility and empty `__init__.py` package marker; (2) HTML eval viewer is a separate `eval-viewer/` subdirectory with its own generator `generate_review.py` + `viewer.html` template — distinct from `scripts/generate_report.py` which is a per-iteration HTML report from run_loop output. Methodology unchanged: still Tier 3 full tooling layer port. Implementation-surface adjustments only — no scope expansion beyond the original "port the tooling layer" intent.)
Prior revisions: rev1 (initial Tier 1/2/3 integration), rev2 (Opus 4.6 analysis improvements: Tier A/B/C, D9 sub-levels, verbatim schemas, grader principles, triggering detection, calibrated scoring), rev3 (intelligent abstraction principle as primary architectural lens; Calibration Engine boundary deferred to backlog), rev3.1 (9 evaluation findings applied), rev3.2 (Opus 4.6 cross-pass: content-class policy elevated to §7 methodology layer, Kitchen Sink decomposition test condensed from 5 to 3 questions, risk register numbering stabilized with Kitchen Sink as §18.9, canonical-kfs/ sync subsection added to §3.3, description consolidation note tightened with precise char accounting), rev3.3 (structural correction in §3.1 KF update instructions — new disciplines placed as top-level §9/§10 instead of §3.10/§3.11 under quality gate parent)

---

## 1. Release framing

### 1.1 Why v3.0 (not v2.2)

This release crosses two thresholds that justify a major version bump rather than a minor:

1. **Architectural shift.** v2.1 is markdown-only — pure methodology layer. v3.0 adds an executable layer (`scripts/` + `agents/`) that the methodology invokes. The Skill becomes a multi-modality artifact: methodology + tooling. This is a category change, not a refinement.
2. **Methodology surface expansion.** D9 expands from RECOMMENDED single-scenario to a tiered formalism (D9a/D9b/D9c) with empirical evidence tiers, full behavioral validation procedure, description optimization loop, and blind version comparison capability. New methodology dimensions (description optimization, blind version comparison, multi-environment adaptation, environment degradation tiers) are added. This is the largest methodology addition since Phase 27/28's v2.0 release.

Same `name:` field (`rootnode-skill-builder`); predecessor folder overwritten in place per KF §6.4. No rename rule triggered. v2.1 deployable zip remains in `Projects/ROOT/research/` for rollback per KF §6.5.

### 1.2 Scope summary

This release integrates the full Tier 1 / Tier 2 / Tier 3 absorption plan from the comparison analysis against Anthropic's `skill-creator`, with rev2 incorporating the Opus 4.6 analysis's structural improvements (Tier A/B/C, D9 sub-levels, verbatim schemas, grader principles), and rev3 extending the intelligent abstraction principle as the primary lens for SKILL.md design.

**Tier 1 — methodology gaps:**
- Expanded D9 behavioral validation, formalized into D9a/D9b/D9c sub-levels
- New Description Refinement Loop methodology (replaces "make it pushy" heuristic)
- "Explain the why" tone calibration discipline

**Tier 2 — useful additions:**
- Realistic test-prompt template library (folded into auto-activation-discipline.md)
- Multi-environment adaptation discipline with Tier A/B/C operational model

**Tier 3 — full tooling layer port:**
- 5 Python scripts (description optimizer, packaging, validation, benchmark aggregation, eval viewer)
- 3 subagent prompt files (grader, comparator, analyzer) — comparator/analyzer pair INCLUDED per user override

### 1.3 Design philosophy

The release does not import Anthropic's tone, casual framing, or instructional voice. It imports the *operational disciplines* (iteration loop, train/test split, blind A/B, anti-overfitting, evidence-tiered evaluation). The result composes Anthropic's empirical rigor with our existing architectural rigor — neither Skill currently does both. The governance floor (gates + 9-dimension quality gate) is non-negotiable; empirical capabilities layer on top, never replace.

**Intelligent abstraction principle (primary lens for SKILL.md design).** Every new SKILL.md section is **routing surface**, not procedural depth. It specifies when to enter the workflow, names the tier(s) used, and points to the reference where the actual procedure lives. The 500-line SKILL.md ceiling is not a constraint to compress around — it is a **forcing function for correct layer placement**. Procedural detail belongs in references; SKILL.md orchestrates. Applied this way, the ceiling raises architectural quality automatically rather than requiring discipline.

**The principle compounds.** skill-builder v3 enforces routing-surface discipline on every Skill it builds. Those Skills (when they build other Skills, e.g., a future skill-builder successor) enforce it further. The architectural floor rises with every generation.

This is a refinement of progressive disclosure (already canonicalized in KF §3.4), not a new principle — but applied with full rigor from the design phase rather than as a compression-time fallback.

**Workflow coherence (anti-Kitchen-Sink rationale).** v3.0 carries five workflows in one Skill: Build, Review, Iterate, Optimize Description, Compare Versions, Multi-Environment Adaptation. These are not unrelated capabilities co-located opportunistically — they are sequential stages of a single Skill build lifecycle: design → build → review → iterate → optimize → compare. Every workflow operates on the same artifact (a Skill). Every workflow shares the same methodology references (SKILL_BUILD_DISCIPLINE, AGENT_ANTI_PATTERNS, etc.). Every workflow shares the same quality gate evidence framework (D1–D9). Splitting into separate Skills would force context duplication — both halves would import the same methodology references — without producing operational benefit. The integration coherence is the design intent, not an oversight. D7 anti-pattern verification (per §15) explicitly checks this rationale; see §18.X for the corresponding risk register entry that documents the intentional coherence as the pass criterion.

---

## 2. Pre-build gates verification

### 2.1 Gate 1 — Decomposition: PASS

The work is a multi-step procedure (gates → build → validate → empirically test → optimize → iterate → compare → package), triggered by user intent expressed in language ("build this Skill," "test this Skill," "optimize the description," "compare these versions"), produces coherent deliverables (deployable zip + audit artifacts + benchmark + comparison report), and is reusable across Skill builds.

Layer placement: still Skill (not hook, not rule, not CLAUDE.md, not subagent, not MCP, not settings). The added executable layer (`scripts/`, `agents/`) sits inside the Skill, not as a separate mechanism — Skills can carry scripts per the Agent Skills spec.

### 2.2 Gate 2 — Warrant: PASS

The warrant evidence for each addition:

| Addition | Warrant source | Evidence |
|---|---|---|
| D9 expansion + D9a/b/c sub-levels | Tier 1 source (Anthropic methodology) + 4.6 competitive analysis + concrete gap analysis | `skill-creator` ships full iteration loop; v2.1 D9 is single-scenario MVP; 4.6 analysis formalizes sub-level architecture. Comparison output documents failure modes single-scenario doesn't catch. |
| Description Refinement Loop | Tier 1 source + 4.6 analysis + concrete gap analysis | `improve_description.py` runs 5-iteration train/test optimization with held-out scoring; v2.1 uses manual heuristic. Stream-event triggering detection mechanism (4.6 §3.4) is critical port artifact. |
| Tier A/B/C degradation model | 4.6 analysis (§5.1) | Skill operates in CP / CC / Cowork; tooling availability differs per environment; explicit tier model required for systematic fallback. |
| "Explain the why" calibration | Tier 1 source + production observation | `skill-creator` explicitly cautions against MUSTs and ALWAYS in caps; favors theory-of-mind reasoning. v2.1 SKILL.md leans on "non-negotiable" framing where reasoned voice would suffice. |
| Test prompt library | Production observation + 4.6 analysis (§6.3) | Anthropic's "Q4 sales final FINAL v2.xlsx" example demonstrates realistic user-voice triggers; query quality criteria extracted in 4.6 §6.3. |
| Multi-environment adaptation | Production observation + Tier A/B/C model | `skill-creator` explicitly branches behavior across claude.ai, Cowork, Claude Code; v2.1 assumes one execution context. |
| Tooling layer (5 scripts) | Tier 1 source + 4.6 verbatim schemas | Production-tested scripts in `skill-creator` provide capability v2.1 cannot match manually. Schemas extracted in 4.6 §6.1-6.2 enable direct port. |
| Subagent prompts (grader, comparator, analyzer) | Tier 1 source + user override | User explicitly elected to include comparator/analyzer pair despite 4.6 analysis's ADAPT-2 deferral recommendation. Override captured in promotion provenance. |
| Grader design principles verbatim | 4.6 analysis (§6.4) | Foundational principle "a passing grade on a weak assertion is worse than useless" is a methodology-level claim worth canonicalizing. |
| Intelligent abstraction principle as primary lens | User direction (rev3) | Promotes routing-surface discipline from compression-time fallback to design-phase architectural choice. Refines progressive disclosure (KF §3.4) without introducing a new methodology claim. |

**Override notation 1.** Scripts in v3.0: 4.6 analysis recommended deferring to v3.1+ (§5.6 item 3, Q-1). User override: include in v3.0. Override captured.

**Override notation 2.** Comparator/analyzer pair: 4.6 analysis classified ADAPT-2 (low priority, possibly separate Skill per Q-5). User override: include in v3.0 within skill-builder. Override captured.

### 2.3 Gate 3 — Ecosystem fit: PASS

**Surface placement:** Same as v2.1 (CP-side methodology Skill, build-time tool). No surface change. Tier A/B/C model formalizes per-environment behavior within the same surface placement.

**Composition:**
- Producer for: deployable Skill zips (consumed by `~/.claude/skills/` install path or rootnode-skills repo)
- Composes with: `rootnode-cc-design` (CC-side companion), `rootnode-handoff-trigger-check` (autonomous execution handoff)
- No duplication: still the only rootnode Skill that builds Skills.

**Routing collision check:** Cross-checked against rootnode-prompt-validation, rootnode-project-audit, rootnode-prompt-compilation, rootnode-handoff-trigger-check, rootnode-cc-design, rootnode-block-selection. No collision; verb-class and vocabulary differentiate cleanly.

---

## 3. KF updates required as precondition

Per KF §8.2, canonical KFs are NOT auto-edited by Skill builds. The methodology evolutions in this release require KF updates first, in a separate human-reviewed cycle.

### 3.1 root_SKILL_BUILD_DISCIPLINE.md updates

**Structural note (rev3.3 correction):** Current §3 in canonical SKILL_BUILD_DISCIPLINE is titled "The 9-dimension quality gate" with §3.1–§3.9 mapping to D1–D9. The "description refinement loop discipline" and "environment-adaptive degradation discipline" are NOT new quality gate dimensions — they are independent methodology disciplines that the dimensions reference. Placing them as §3.10 and §3.11 would put non-dimension content under a header that explicitly enumerates the dimensions. Correct placement: NEW top-level sections inserted after §8 "Design-spec consumption discipline" and before existing §9 "Where to go next" (which renumbers to §11).

**Updates to existing sections:**

- **§3.4 (D4 — Progressive disclosure)** — Refinement within the existing dimension. Add subsection or paragraph articulating the intelligent abstraction principle: SKILL.md sections that introduce new workflows are routing surfaces by default; procedural depth lives in references; the 500-line ceiling is a design-phase forcing function. Refines existing progressive disclosure language; does not introduce a new methodology claim.
- **§3.9 (D9 — Behavioral validation)** — Expansion within the existing dimension. Replace the existing single-dimension RECOMMENDED text with three sub-levels:
  - **D9a (Empirical, Tier A):** With-skill vs. without-skill comparison with graded outcomes via subagent grader. Strongest evidence. Required infrastructure: subagents available, execution environment available.
  - **D9b (Empirical, Tier B):** With-skill execution confirmed via realistic test prompts; no baseline comparison; qualitative review. Moderate evidence. Required infrastructure: execution environment available; subagents not required.
  - **D9c (Analytical):** Current v2.1 D9 pass conditions (pressure scenario documented, baseline failure credibly expected, compliance credibly expected). Weakest evidence; valid floor. No infrastructure required.
  
  D9 remains classified RECOMMENDED, not REQUIRED. The verdict per dimension specifies which sub-level was applied, captured in the build summary. Cross-reference the new §9 (description refinement loop discipline) and §10 (environment-adaptive degradation discipline) where the sub-levels invoke them.
- **§7.2 (What can change without warrant)** — Update to add tone calibration consistent with AEA "explain the why" principle.

**New top-level sections (replacing the prior rev3.2 plan for §3.10 and §3.11):**

- **§9 — NEW: Description refinement loop discipline.** Insert as a new top-level section after §8 "Design-spec consumption discipline" and before existing §9 "Where to go next." Cover trigger eval generation procedure, manual walkthrough discipline, optional automation via `description_optimizer.py`, train/test split methodology with held-out scoring, anti-overfitting principle, triggering detection mechanism. Cite design spec §9.2 (the reference file `description-optimization.md`). Cross-reference §3.9 D9b/D9c sub-levels which invoke this discipline.
- **§10 — NEW: Environment-adaptive degradation discipline.** Insert as a new top-level section after the new §9. Cover Tier A/B/C operational model, per-tier verdict scoring, fallback paths. Cross-reference §3.9 D9a/D9b/D9c sub-levels which apply per-tier.
- **§11 — RENUMBERED: Where to go next.** Existing §9 content renumbered to §11 (shifted by the two new sections). No content change; only the section number changes. Update any internal cross-references that pointed to "§9 Where to go next" to point to "§11 Where to go next."

### 3.2 root_AGENT_ENVIRONMENT_ARCHITECTURE.md updates

**§4.X — NEW: "Explain the why" calibration.** Add a new subsection in surface-invariant principles. Establishes the principle: where a constraint genuinely warrants imperative voice (spec compliance, safety boundaries), use it; where reasoning would carry equal force, prefer reasoning. Theory-of-mind framing for instruction-tuned models.

**§4.Y — NEW: Multi-environment adaptation discipline.** Add a new subsection. Skills that may run across CP / CC / Cowork should flag environment-dependent steps explicitly. Compatibility matrix pattern. Tier A/B/C operational model referenced from this principle layer.

### 3.3 Sequencing

The KF updates run as a separate CV (Phase 32a) before the v3.0 Skill build CV (Phase 32b). Skill build then references the canonicalized methodology rather than introducing new claims that would themselves require warrant.

**Canonical-kfs/ sync (rev3.1 addition).** After Phase 32a KFs are approved and uploaded to the seed Project, the Phase 32b release branch must also sync the approved KFs into the repo-local `audit/canonical-kfs/` directory. This ensures the CC build agent reads current methodology when resolving `@audit/canonical-kfs/` citations. The sync is a Phase 32b precondition step, committed on the release branch before any Skill content authoring begins. The build prompt (§32b.1.5) verifies the synced content matches v3 expectations (e.g., §3.9 contains D9a/D9b/D9c sub-levels) — if it does not, halt because Phase 32a output was not correctly staged.

---

## 4. Locked decisions (scope-lock)

The following decisions are locked for the v3.0 build CV. Mid-build deviations require scope-lock v2.

1. **Combined release.** Tier 1 / 2 / 3 ship as a single v3.0, not sequenced v2.2 → v2.3.
2. **Comparator/analyzer pair INCLUDED.** User override against 4.6 analysis ADAPT-2 deferral.
3. **Scripts INCLUDED in v3.0.** User override against 4.6 analysis §5.6 item 3 deferral. Tier A/B/C model resolves the underlying concern.
4. **Subagent prompts placed in `agents/` subdirectory.** Anthropic precedent.
5. **Major version bump to 3.0.** Same `name:`, predecessor overwritten in place.
6. **D9 split into D9a/D9b/D9c sub-levels** per 4.6 analysis §5.2. Quality gate is D1–D8 + D9 (with one of D9a/b/c sub-levels applied per build environment). Total dimensions remain 9; D9 has three tiered evidence levels.
7. **5 new reference files + 3 updated reference files.** Total references: 12.
8. **5 Python scripts in `scripts/`.**
9. **3 subagent prompt files in `agents/`.**
10. **SKILL.md body kept under 500 lines** via intelligent abstraction (routing-surface design), not compression. Target ~480 lines.
11. **Description field stays under 1024 chars (YAML-parsed).**
12. **No removal of existing v2.1 content.**
13. **KF precondition CV (Phase 32a) precedes Skill build CV (Phase 32b).**
14. **CC-driven build using v2.1 methodology files as content reference.** v2.1 is the methodology source (SKILL.md and references read by the CC agent during the build). v2.1 is not invoked as an executable Skill during the v3.0 build. The build mechanism is a CC agent reading v2.1's content and applying the v3.0 design spec to produce v3.0 artifacts.
15. **Tier A/B/C model adopted as the operational pattern for D9 and broader empirical workflows.**
16. **Intelligent abstraction is the primary design lens for new SKILL.md sections.** All four new workflow sections (Iterate the Skill, Optimize the Description, Compare Skill Versions, Multi-Environment Adaptation) are routing surfaces; procedural detail lives in references. Examples in §8.6 are compressed to 5-line patterns rather than 20-line walkthroughs.

---

## 5. Description field draft

```yaml
description: >-
  Builds, validates, packages, tests, and optimizes deployment-ready Skill
  files (SKILL.md + references/ + scripts/ + agents/) from design
  specifications. Three pre-build gates + 9-dimension quality gate (with
  D9a/b/c empirical evidence tiers) + behavioral iteration loop + automated
  description optimizer + blind version comparator. Use for building,
  reviewing, revising, testing, or optimizing Skills. Trigger on: "build
  this Skill," "review this Skill," "test my Skill," "optimize the
  description," "compare these Skill versions," "should this be a hook
  instead," "build a template first." Also: "my Skill doesn't activate,"
  "my description truncates," "my SKILL.md is too long," "my Skill is
  overtriggering." Do NOT use when designing Skill methodology — that's
  design work, not packaging. Do NOT use for prompt compilation, project
  auditing, or prompt scoring (use rootnode-prompt-compilation,
  rootnode-project-audit, or rootnode-prompt-validation if available).
```

**Estimated parsed length:** ~961 chars. ~63-char headroom against 1024 ceiling. Build CV must verify YAML-parsed length.

**Rev3.1 consolidation note.** Removed redundant trigger phrases to gain headroom: "convert this to a Skill" (subsumed by "build this Skill"), "iterate on my Skill" (subsumed by "test my Skill"), "is the new version better" (subsumed by "compare these Skill versions"). Also removed "iterating" from the "Use for" list (subsumed by "testing"). Net reduction: ~96 chars from rev3's ~1015 starting count. Headroom sufficient for one or two future trigger additions without rebudgeting.

---

## 6. Routing collision analysis

(Unchanged from rev2.) No collision detected. Verb-class and vocabulary differentiate cleanly.

---

## 7. Internal language adaptation notes

(Unchanged from rev2 except rev3.2 content-class policy addition.)

**Existing exception preserved:** Skill operates ON root.node Skills as subject matter.

**New "explain the why" calibration applied to new content.** All new SKILL.md sections and new reference files follow AEA-grounded discipline.

**Content-class policy for ported material (rev3.2 addition — promoted from build-prompt-only to methodology layer).** Material ported from Anthropic's `skill-creator` falls into three content classes with different treatment:

1. **Schemas and structural fields** (eval schema, grading schema, trigger eval schema, comparison rubric, analyzer output fields): **verbatim.** These are interface contracts; paraphrasing breaks compatibility.
2. **Prose passages** (subagent prompt instructions, procedural explanations, rationale paragraphs): **tone-adapted while preserving meaning.** Apply AEA §4.10 brand-cleanliness and "explain the why" calibration. Remove Anthropic-specific examples, casual framing, or instructional voice; replace with neutral root.node equivalents.
3. **Structural-only content** (directory layouts, file naming, config patterns): **preserved exactly.** No tone component to adapt; structural accuracy is the only concern.

The build CV applies this classification when encountering the "preserve verbatim" AND "apply brand-cleanliness" instructions — this policy resolves which wins per content class. The two instructions do not conflict when classified correctly.

This policy lives at the methodology layer (§7) rather than only in the build prompt because: (a) future builds and reviews can cite §7 as the canonical home; (b) §19 build behavioral calibration references it; (c) it generalizes beyond the v3.0 build to any future port of external methodology content.

---

## 8. SKILL.md v3.0 structural changes

**Insertable section blocks** (per design-then-build discipline; build CV produces complete files).

**Architectural note:** Every new section below is a **routing surface** per scope-lock item 16. Each names the workflow, identifies tier routing, and points to the reference. Procedural detail does NOT live in SKILL.md.

### 8.1 Section: Iterate the Skill (new — routing surface)

**Placement:** After "Build New Skill" section.

**Content shape (routing-surface only):**
- One-paragraph introduction: what behavioral iteration is, when to enter the loop.
- Tier routing logic: detect environment capabilities; route to Tier A (full subagent grading), Tier B (sequential inline), or Tier C (analytical fallback per D9c).
- Pointer to `references/behavioral-validation.md` for full procedure including step-by-step iteration, grader principles, schemas, and tier-specific procedures.

**Estimated lines:** 15-20.

### 8.2 Section: Optimize the Description (new — routing surface)

**Placement:** After "Iterate the Skill" section.

**Content shape (routing-surface only):**
- One-paragraph introduction: why description optimization is highest-leverage.
- Tier routing logic: Tier A invokes `description_optimizer.py` for automated 5-iteration train/test loop; Tier B/C falls to manual procedure.
- Pointer to `references/description-optimization.md` for full procedure including triggering detection mechanism, schemas, train/test split methodology.

**Estimated lines:** 12-15.

### 8.3 Section: Compare Skill Versions (new — routing surface)

**Placement:** After "Optimize the Description" section.

**Content shape (routing-surface only):**
- One-sentence introduction: when blind A/B comparison is warranted.
- Tier routing logic: Tier A invokes comparator + analyzer subagents; Tier B/C falls to inline manual blind procedure.
- Pointer to `references/version-comparison.md` for full procedure, rubric, and analyzer outputs.

**Estimated lines:** ~5.

### 8.4 Section: Multi-Environment Adaptation (new — routing surface)

**Placement:** After "Conversion Rules Quick Reference" section.

**Content shape (routing-surface only):**
- One-paragraph introduction: why some Skills behave differently across CP / CC / Cowork.
- Tier A/B/C compatibility matrix (compact inline reference; detail in references).
- Pointer to `references/multi-environment-adaptation.md` for full discipline.

**Estimated lines:** 15-20.

### 8.5 Section: Build Behavioral Calibration (updated)

**Update:** Add one paragraph on "explain the why" principle for new Skill content.

**Estimated added lines:** 5.

### 8.6 Section: Examples (updated — compressed)

**Update:** Add four new examples — one per new workflow. **Each example compressed to ~5 lines** (brief input, action list as one-line bullets, brief result) per scope-lock item 16. Total ~20 lines.

**Estimated added lines:** ~20.

### 8.7 Section: Quality Gate (updated)

**Update:** Add checklist items for new workflows.

**Estimated added lines:** 12-15.

### 8.8 Section: Reference table (updated)

**Update:** Add five new reference file entries. Update three existing entries.

**Estimated added lines:** 12-15.

### 8.9 Total SKILL.md projection (revised under intelligent abstraction)

v2.1 baseline: 370 lines.
Revised additions:
- New routing-surface sections (8.1-8.4): ~50 lines (was 85-105 in rev2)
- Build Behavioral Calibration update (8.5): ~5 lines
- Examples update (8.6): ~20 lines (was ~50 in rev2)
- Quality Gate update (8.7): ~12-15 lines
- Reference table update (8.8): ~12-15 lines

Total revised additions: ~100-105 lines.
Estimated v3.0 total: **~470-480 lines.** Comfortably under 500.

The intelligent abstraction principle eliminates the 500-line ceiling risk entirely. No compression-time discipline required; correct layer placement at design time produces the right size automatically.

---

## 9. New reference files (5)

(Reference file contents unchanged from rev2 — already designed as the canonical home for procedural depth, consistent with intelligent abstraction principle.)

### 9.1 references/behavioral-validation.md

(rev2 content preserved.) D9 sub-level architecture; test prompt generation; with-Skill vs. baseline protocol (Tier A); qualitative review; quantitative grading via subagent or inline; iteration loop conditions; anti-overfitting framing; grader design principles verbatim from 4.6 §6.4; eval schema verbatim from 4.6 §6.1; grading schema verbatim from 4.6 §6.2; tooling integration. Estimated 300-340 lines (TOC required).

### 9.2 references/description-optimization.md

(rev2 content preserved.) Why description optimization is highest-leverage; trigger eval generation; eval query schema verbatim from 4.6 §6.3; eval query realism principles; manual walkthrough (Tier B/C); automated procedure via `description_optimizer.py` (Tier A); anti-overfitting principle; triggering detection mechanism verbatim from 4.6 §3.4; description improvement prompt structure verbatim from 4.6 §6.5; train/test split methodology verbatim from 4.6 §6.6; how triggering actually works. Estimated 280-320 lines.

### 9.3 references/version-comparison.md

(rev2 content preserved.) When to use; when to skip; subagent vs. inline modes; blind comparison rubric verbatim from 4.6 §6.7; post-hoc analyzer outputs verbatim from 4.6 §6.8; subagent procedure; inline procedure; identifier leak prevention. Estimated 220-260 lines.

### 9.4 references/multi-environment-adaptation.md

(rev2 content preserved.) Tier A/B/C operational model; per-environment compatibility matrix; per-script tier compatibility table; Skill authoring discipline; pattern library; detection patterns. Estimated 220-260 lines.

### 9.5 references/tooling-layer-overview.md

(rev2 content preserved.) Map of `scripts/` and `agents/`; per-script details with tier compatibility; per-subagent details; integration patterns; maintenance discipline; drift detection. Estimated 280-320 lines (TOC required).

---

## 10. Updated reference files (3)

(Unchanged from rev2.)

### 10.1 references/auto-activation-discipline.md

Add: realistic test prompt patterns subsection (~80-100 lines); tone calibration subsection (~20 lines).

### 10.2 references/conversion-guide.md

Add: tone calibration in produced Skill content subsection (~30-40 lines).

### 10.3 references/skills-spec.md

Add: Skill subdirectory structure subsection; executable layer in Skills subsection (~60-80 lines).

---

## 11. New scripts/ directory (7 files)

(Expanded from rev3.3's 5-file enumeration following pre-launch verification of upstream Anthropic skill-creator source.)

Per design §13.3 promotion provenance, port from `design/skill-creator/scripts/` with content-class policy from §7 applied per file:

1. **`scripts/description_optimizer.py`** — fused from upstream `run_loop.py` + `run_eval.py` + `improve_description.py`. Preserves triggering detection mechanism, train/test split, improvement prompt structure verbatim (content class 1: structural contracts). Adapts comments and docstrings per content class 2 (tone-adapted). Tier A capability (full automation); Tier B falls to manual procedure documented in `references/description-optimization.md`.
2. **`scripts/package_zip.py`** — adapted from upstream `package_skill.py` for `.zip` format with root.node folder structure (`{skill-name}/SKILL.md` + `{skill-name}/references/*.md` + `{skill-name}/scripts/*` + `{skill-name}/agents/*.md` + `{skill-name}/eval-viewer/*` if present). Tier A/B/C compatible (no environment dependency).
3. **`scripts/quick_validate.py`** — adapted from upstream `quick_validate.py` for D1 dimension. Extends allowed frontmatter properties to include root.node `metadata` sub-fields (`author`, `version`, `predecessor`, `original-source`, `notes`, `discipline_post`). Tier A/B/C compatible.
4. **`scripts/aggregate_benchmark.py`** — adapted from upstream `aggregate_benchmark.py`. Preserves schema alignment with `agents/grader.md` output format. Tier A capability (requires grader subagent output to aggregate); Tier B/C produces no benchmark output.
5. **`scripts/generate_report.py`** — adapted from upstream `scripts/generate_report.py` (NOT to be confused with eval-viewer's `generate_review.py` — see §11B). Generates static HTML report from `description_optimizer.py` output showing per-iteration train/test results with check/x marks. Apply brand-cleanliness pass to embedded HTML strings per content class 2 + AEA §4.10. Tier A capability (consumes optimizer output); Tier B/C unused.
6. **`scripts/utils.py`** — ported from upstream `scripts/utils.py`. Provides `parse_skill_md()` shared utility used by SKILL.md parsing across the tooling layer. Content class 3 (structural-only — port verbatim, no tone adaptation needed). Tier A/B/C compatible.
7. **`scripts/__init__.py`** — empty Python package marker, ported from upstream as zero-byte file. Required so `scripts/` functions as a Python package for relative imports. Content class 3 (structural).

**Adaptation notes summary:** All 7 files port to `rootnode-skill-builder/scripts/`. The content-class policy from §7 governs verbatim-vs-adapted treatment per file. Tier compatibility documented in `references/multi-environment-adaptation.md` and `references/tooling-layer-overview.md`.

## 11B. New eval-viewer/ subdirectory (2 files)

(Added in rev3.4 — pre-launch verification revealed eval-viewer is a separate top-level subdirectory in upstream skill-creator, not part of `scripts/`.)

The eval-viewer is an **interactive HTTP-served review page** for browsing multiple eval runs with feedback collection. Distinct in purpose from `scripts/generate_report.py` (single-run static HTML report). Mirrors upstream structure as a sibling subdirectory to `scripts/`, `agents/`, and `references/`.

Port from `design/skill-creator/eval-viewer/` to `rootnode-skill-builder/eval-viewer/`:

1. **`eval-viewer/generate_review.py`** — ported from upstream `eval-viewer/generate_review.py`. Reads workspace directory, discovers runs (directories with outputs/), embeds output data into a self-contained HTML page, serves via tiny HTTP server with feedback auto-save. Preserves HTTP server logic and feedback-collection mechanism verbatim (content class 1: structural). Adapts docstrings, prose comments, and CLI help strings per content class 2 (tone-adapted). Tier A capability (requires Python execution + browser); Tier B/C unused.
2. **`eval-viewer/viewer.html`** — 45 KB HTML template used by `generate_review.py`. Apply brand-cleanliness pass per Q3 resolution (full neutral root.node branding replace). Content class breakdown:
   - HTML structural elements (DOM structure, semantic tags, JavaScript event handlers): **verbatim** (content class 1)
   - CSS class names that drive layout/behavior: **verbatim** (content class 1)
   - Page title, headers, branded copy, examples, comments: **tone-adapted** with full Anthropic-marker removal (content class 2)
   - Embedded JavaScript that handles feedback submission: **verbatim** (content class 1)

The eval-viewer's package_zip.py inclusion (§11 item 2) ensures these files ship in the deployable v3.0 zip alongside `scripts/`.

---

## 12. New agents/ directory (3 files)

(Unchanged from rev2.)

`agents/grader.md`, `agents/comparator.md`, `agents/analyzer.md`. All adaptations preserved.

---

## 13. Methodology preservation analysis

(Unchanged from rev2 except promotion provenance row addition.)

### 13.1 Preserved verbatim from v2.1

All seven existing reference files in unchanged sections; pre-build gate definitions; D1-D8 quality gate; conversion rules; build pipeline; Review Existing Skill procedure; existing examples and troubleshooting.

### 13.2 Evolved with warrant

D9 expansion + sub-level formalism; Description Refinement Loop methodology; Tier A/B/C degradation model; "Explain the why" calibration; Multi-environment adaptation; Tooling layer; **intelligent abstraction principle as primary design lens** (refinement of existing progressive disclosure, not new claim).

### 13.3 Promotion provenance row template

| Change type | Source of authority | Evidence type |
|---|---|---|
| D9 expansion + D9a/b/c formalism | Tier 1 + 4.6 analysis §5.2 + concrete gap analysis | Methodology evolution (Phase 32a KF §3.9 update) |
| Description Refinement Loop | Tier 1 + 4.6 analysis §6.3, §6.5, §6.6 + concrete gap analysis | Methodology evolution (Phase 32a KF new §9 addition; rev3.3 placement correction) |
| Tier A/B/C degradation model | 4.6 analysis §5.1 | Methodology evolution (Phase 32a KF new §10 addition; rev3.3 placement correction) |
| Triggering detection mechanism | 4.6 analysis §3.4 | Implementation pattern (preserved in `description_optimizer.py` port) |
| Grader design principles verbatim | 4.6 analysis §6.4 | Methodology evolution (incorporated into `references/behavioral-validation.md`) |
| Schemas verbatim | 4.6 analysis §6.1, §6.2, §6.3, §6.7, §6.8 | Reference content (incorporated into respective reference files) |
| "Explain the why" calibration | Tier 1 + production observation | Methodology evolution (Phase 32a AEA §4.X addition) |
| Multi-environment adaptation | Tier 2 + Anthropic environmental branching | Methodology evolution (Phase 32a AEA §4.Y addition) |
| Tooling layer (7 scripts in `scripts/`) | Tier 1 + user override on script inclusion in v3.0 + rev3.4 pre-launch verification | Production tooling adoption + override; rev3.4 corrected count from 5 to 7 (added `utils.py` shared utility, `__init__.py` package marker after upstream verification) |
| Eval viewer subdirectory (`eval-viewer/`: 1 .py + 1 .html) | Tier 1 + user override + rev3.4 pre-launch verification | Production tooling adoption; rev3.4 separated eval-viewer as its own subdirectory (mirrors upstream); generator (`generate_review.py`) is distinct from `scripts/generate_report.py` (per-iteration HTML report); `viewer.html` template under brand-cleanliness pass per Q3 |
| Subagent prompts (3 files) | Tier 1 + user override on comparator/analyzer | Production tooling adoption + override |
| Test prompt library | Production observation + 4.6 §6.3 | Methodology evolution (no KF change; reference-file addition) |
| Intelligent abstraction principle as primary design lens | User direction (rev3) | Refinement of existing KF §3.4 progressive disclosure principle (not new claim); applied as primary lens at design time |

---

## 14. Composition testing cases

(Unchanged from rev2.) Should-trigger / should-not-trigger / edge cases listed in §14 of rev2. All eight should-trigger cases, five should-not-trigger cases, and four edge cases preserved.

---

## 15. Quality gate verification plan

(Unchanged from rev2 except D4 strengthened.)

| Dimension | Verification approach |
|---|---|
| D1 — Spec compliance | `quick_validate.py` against built artifact. |
| D2 — Activation precision | Trigger eval set walkthrough; optionally run `description_optimizer.py` for one iteration if Tier A available. |
| D3 — Methodology preservation | Compare v3.0 SKILL.md sections to v2.1 sections per §13.1. |
| D4 — Progressive disclosure | **SKILL.md verified ~470-480 lines** (target reduction from rev2's 480-495 estimate). Each new SKILL.md section confirmed as routing surface (no procedural detail). Each new reference file referenced from SKILL.md with "when to read" guidance. New references over 300 lines have TOC. **Intelligent abstraction principle compliance check: walk each new SKILL.md section and verify it does not duplicate procedural content from its corresponding reference file.** |
| D5 — Standalone completeness | Cross-Skill references use "if available" language. |
| D6 — Auto-activation enforcement | Verb-based trigger language; no `disable-model-invocation`. |
| D7 — Anti-pattern catalog scan | Walk catalog. Particular attention to §3.4 Kitchen Sink (multiple workflows co-located — verify integration coherence). |
| D8 — 7-layer leak-check | Tooling layer verified as Skill-internal. |
| D9 — Behavioral validation (sub-level applies) | Determine which sub-level applies based on build-time environment; run iteration loop on v3.0 itself; capture tier + verdict in build summary. |

---

## 16. Audit artifacts produced by v3.0 build

(Unchanged from rev2.) Placement note (always); promotion provenance with two override notations and intelligent abstraction promotion row; AP-warning summary if D7 catches.

---

## 17. Build sequencing within v3.0 release

(Unchanged from rev2.) Reference file updates → new reference files → subagent prompts → Python scripts → SKILL.md v3.0 → quality gate → audit artifacts → packaging → install verification → build summary.

---

## 18. Risks and mitigations

### 18.1 SKILL.md exceeds 500 lines — RESOLVED

**Status:** Resolved by rev3's intelligent abstraction principle (scope-lock item 16). No longer a risk.

**Resolution:** All four new SKILL.md sections designed as routing surfaces from the design phase. Examples compressed to 5-line patterns. Estimated v3.0 total ~470-480 lines, under 500 with no compression-time discipline required. The 500-line ceiling now functions as a design-phase forcing function rather than a build-phase risk.

### 18.2 Description exceeds 1024 chars

**Risk likelihood:** Moderate. Draft estimated ~1015 chars.

**Mitigation:** YAML-parsed length verification at build time. If over, tighten by removing one trigger phrase per category.

### 18.3 Tooling layer drift from Anthropic source

**Risk likelihood:** High over time.

**Mitigation:** Drift detection discipline. Monthly comparison checklist; quarterly port decision.

### 18.4 Tier B/C fallback gaps

**Risk likelihood:** Moderate.

**Mitigation:** Each workflow's tier compatibility documented explicitly. Tier B/C fallbacks are manual procedures, not degraded automated procedures.

### 18.5 Self-bootstrap edge cases

**Risk likelihood:** Low.

**Mitigation:** Build mechanism is CC-driven; v2.1 methodology files are content reference only; v2.1's executable Skill machinery is not invoked during the build (per scope-lock item 14 clarification). No circular execution path possible.

### 18.6 Methodology preservation drift

**Risk likelihood:** Low if discipline applied.

**Mitigation:** §13.1 enumerates verbatim-preserved content.

### 18.7 D9 sub-level determination ambiguity

**Risk likelihood:** Low.

**Mitigation:** Decision logic in `references/multi-environment-adaptation.md`.

### 18.8 Routing-surface discipline drift in build

**Risk likelihood:** Low to moderate. Build CV may default to procedural depth in SKILL.md sections out of habit.

**Mitigation:** D4 verification step (per §15) explicitly checks for routing-surface compliance. Build behavioral calibration (§19) reinforces the principle.

### 18.9 Kitchen Sink false positive on D7 walk (rev3.1 addition)

**Risk likelihood:** Expected. D7 anti-pattern scan will flag multiple co-located workflows (Build, Review, Iterate, Optimize Description, Compare Versions, Multi-Environment Adaptation).

**Mitigation:** Explicit decomposition test applied during D7:

1. **Lifecycle coherence test:** Do the workflows form a sequential or iterative lifecycle (design → build → validate → iterate → optimize → compare), or could they operate independently? **Expected result:** lifecycle — every workflow requires the governance floor (gates, quality gate, methodology preservation).
2. **Governance duplication test:** Would splitting into separate Skills (e.g., `skill-builder` + `skill-tester`) require duplicating the governance floor or cross-Skill composition contracts? **Expected result:** yes — governance context is foundational to every workflow.
3. **Independent invocation test:** Would a user ever invoke one workflow without the others being available? **Expected result:** no — "test my Skill" requires the build governance context; "compare versions" requires the quality gate context.

If all three tests pass, D7 verdict is ACCEPTED (false positive — workflows are coherent lifecycle stages, not independent capabilities). The AP-warning summary documents the walk and disposition per KF §4 standard.

The coherence argument is also documented in §1.3 design philosophy as the architectural intent.

---

## 19. Build behavioral calibration notes

For the v3.0 build CV (Phase 32b):

- **Build mechanism awareness.** v2.1 is the methodology source — the CC agent reads v2.1's SKILL.md and reference files as content reference. v2.1 is NOT invoked as an executable Skill during the build. The build is CC-driven: CC agent + v3.0 design spec + v2.1 content reference + Anthropic skill-creator source → produces v3.0 artifacts. There is no self-invocation; "self-bootstrap" in earlier framing refers to v2.1's content informing v3.0's content, not v2.1's machinery executing.
- **"Explain the why" applied during build.** New SKILL.md content authored under v3.0 spec.
- **Tooling layer is content, not behavior.** Python scripts and subagent prompts are file content the build CV produces; build CV does not invoke them during the build.
- **Intelligent abstraction discipline.** When authoring new SKILL.md sections, default to routing-surface design. If a procedural step feels like it belongs in SKILL.md, ask: does it route to a tier or workflow? If yes, it's routing. Does it explain how to do something step-by-step? If yes, it belongs in a reference. The 500-line ceiling is a design-phase forcing function — design under it from the start, do not compress to fit.
- **Tier A/B/C determination is build-time.** When running self-validation (D9), determine which tier applies for the build environment.
- **Content-class policy for ported material.** Apply the three-class policy from §7: schemas verbatim, prose tone-adapted, structural content preserved exactly. When a build step says both "preserve verbatim" and "apply brand-cleanliness," resolve per content class — they do not conflict when classified correctly.

---

## 20. Open questions / decisions for user — RESOLVED (rev3.1)

All six open questions resolved at rev3.1 with the following decisions:

1. **AEA section numbering — RESOLVED.** §4.11 ("explain the why" calibration), §4.12 (multi-environment adaptation). Build CV must verify these section numbers are available in current AEA before edit; if §4.11 or §4.12 is taken (e.g., by an unanticipated Phase 31a addition), use next available numbers and document the reassignment in the change summary.
2. **Subagent prompt naming — RESOLVED.** Adopt `agents/grader.md`, `agents/comparator.md`, `agents/analyzer.md` per Anthropic precedent. Files live in the `agents/` subdirectory of the Skill.
3. **HTML eval viewer branding — RESOLVED.** Full replace with neutral root.node branding per AEA §4.10 brand-cleanliness discipline. No Anthropic markers retained in HTML, CSS, or copy. Build CV applies brand-cleanliness pass to the HTML template during Phase 32b.5 script porting.
4. **Drift-detection cadence — RESOLVED.** Monthly comparison checklist (compare adapted scripts and subagents against current Anthropic skill-creator source); quarterly port decision (decide whether material upstream changes warrant a v3.x update). Documented in `references/tooling-layer-overview.md` drift-detection section.
5. **Test prompt library placement — RESOLVED.** Fold into `references/auto-activation-discipline.md` as a new subsection. Total reference file count remains 12 (no new file created). Subsection covers: realistic test prompt patterns, query realism principles per 4.6 §6.3, should-trigger / should-not-trigger / edge-case templates.
6. **D9 sub-level requirement classification — RESOLVED.** All three sub-levels (D9a, D9b, D9c) remain RECOMMENDED, not REQUIRED. This preserves v2.1's stance and avoids hard halts on Skill builds in environments without D9 evidence infrastructure. The verdict per dimension specifies which sub-level applied.

---

## 21. Sequencing summary

```
Phase 32a (KF precondition CV — root_CC_skill_builder_v3_build.md)
├── Update root_SKILL_BUILD_DISCIPLINE.md → design/staging-kf/
│   ├── §3.4 progressive disclosure refinement (intelligent abstraction)
│   ├── §3.9 D9 expansion + D9a/D9b/D9c sub-levels
│   ├── §7.2 tone calibration addition
│   ├── §9 NEW description refinement loop discipline (top-level, post §8)
│   ├── §10 NEW environment-adaptive degradation discipline (top-level)
│   └── §11 RENUMBERED Where to go next (was §9)
└── Update root_AGENT_ENVIRONMENT_ARCHITECTURE.md → design/staging-kf/
    ├── §4.11 NEW "explain the why" calibration (per Q1 resolution)
    └── §4.12 NEW multi-environment adaptation discipline (per Q1 resolution)
        │
        ▼ (Phase 32a closes; user uploads to seed Project AND user signals continue)
        │
Phase 32b (Skill v3.0 build CV — root_CC_skill_builder_v3_build.md)
├── Pre-flight (incl. Skill-availability enumeration per L3)
├── canonical-kfs/ sync from staging-kf/ (per H1 — first step on release branch)
├── Pre-build gates verified (§2)
├── Reference file updates (§10)
├── New reference files (§9)
├── Subagent prompts (§12) — verbatim/brand-clean policy per M2
├── Python scripts ported (§11) — verbatim/brand-clean policy per M2
├── SKILL.md v3.0 assembled (§8) — routing-surface discipline applied throughout
├── Quality gate verified (§15) — D7 includes Kitchen Sink decomposition test per M1
├── Audit artifacts produced (§16)
├── Deployable zip packaged
└── PR created → HALT for user review + merge in browser
        │
        ▼ (user merges PR via GitHub UI; user tests v3.0; user signals continue to release prompt)
        │
Phase 32c (release CV — root_CC_skill_builder_v3_release.md, SEPARATE prompt per H3)
├── Pre-flight (verify v3.0 PR merged on main, build outputs exist, testing log)
├── Sync local main with merged PR
├── Tag v3.0
├── Push tag
├── Create GitHub release with attached zip
└── Final summary
        │
        ▼
v3.0 released
├── Personal install (separate decision)
├── rootnode-skills repo release v3.0 attached
└── v2.1 zip retained in research/ for rollback
```

**Two structural changes from rev3:**

- **canonical-kfs/ sync** is now an explicit Phase 32b first step (H1 fix). The CC build prompt copies `design/staging-kf/*.md` → `audit/canonical-kfs/*.md` and commits on the release branch before any methodology citation. This ensures Phase 32b reads v3 methodology, not v2.1.
- **Phase 32c is a separate prompt** (H3 fix). `root_CC_skill_builder_v3_release.md` is a distinct file invoked only after operator-confirmed v3.0 testing. Phase 32b's halt summary explicitly says "v3.0 release is a separate prompt — invoke when testing complete."

---

## 22. Approval gates before build

Before Phase 32a launches:

1. Aaron approves scope-lock items in §4 (16 items, three include user overrides — comparator/analyzer pair, scripts in v3.0, intelligent abstraction lens at item 16; plus item 14 clarified per L2).
2. Aaron's resolutions in §20 confirmed (all 6 RESOLVED at rev3.1).
3. Aaron acknowledges KF precondition.

Before Phase 32b launches:

1. Phase 32a closes with KF updates uploaded to seed Project AND copied to `audit/canonical-kfs/` (the latter via Phase 32b's first step per H1).
2. v2.1 content reference confirmed accessible.
3. Workspace prepared in `Projects/ROOT/research/v3-build/`.

Before Phase 32c launches (separate prompt invocation per H3):

1. v3.0 PR merged to main.
2. v3.0 build outputs verified (deployable zip exists; quality gate verdict captured).
3. Operator has tested v3.0 and confirms readiness for release tagging.

---

## 23. Deferred backlog items

Items raised during the design CV but explicitly deferred from the v3.0 release. Each carries a trigger condition for re-engagement.

### 23.1 Calibration Engine boundary and eval schema compatibility

**Background.** The Opus 4.6 competitive analysis raised (Q-6 in §7) the cross-project boundary question between skill-builder v3 and the Calibration Engine. Both projects test whether Skills behave correctly. The proposed boundary: skill-builder validates at *build time* (does this new Skill work?); Calibration Engine validates at *model-change time* (do existing Skills still work after a model update?).

**Open question:** Should the eval schemas adopted in v3.0 (eval schema, grading schema, trigger eval schema, comparison rubric, analyzer outputs — see §6.1-6.8 of 4.6 analysis) be designed for cross-project compatibility now, so test cases can flow between skill-builder and Calibration Engine when the latter is built?

**Decision (rev3):** **Deferred.** Calibration Engine is not on the immediate build roadmap. Designing eval schemas for cross-project compatibility now would be premature optimization without concrete Calibration Engine requirements to design against.

**Trigger condition for re-engagement:** When the Calibration Engine project's design CV begins, this backlog item must be retrieved and addressed as part of that CV's scope. The Calibration Engine design CV should:
1. Review v3.0 eval schemas and decide which fields/structures to preserve, extend, or replace for the regression-testing use case.
2. Identify any compatibility constraints that would require backwards-incompatible changes to skill-builder's schemas (would warrant a v3.x or v4.0 schema migration).
3. Document the boundary explicitly: which test cases live where, when test cases flow between systems, and what the synchronization discipline is.

**Project where this lives:** Calibration Engine project (when it exists). Until then, this design doc serves as the reminder.

**Build-context entry recommended:** When `root_build_context.md` receives its next CV update, add an open-items entry: "Calibration Engine boundary + eval schema compatibility (deferred from v3.0 design rev3) — re-engage at Calibration Engine design CV launch."

---

## Appendix A: Calibrated 1-10 scoring scale

(Unchanged from rev2.) Anchored at 5 (basic), 7 (solid methodology), 9 (production-validated). For future Skill comparison work.

---

*End of root_DS_skill_builder_v3.md (rev3.4).*
