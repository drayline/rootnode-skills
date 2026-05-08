# root_SKILL_BUILD_DISCIPLINE.md

The canonical home for rootnode Skill build methodology. Establishes the disciplines that govern how a rootnode Skill gets built from a design specification, validated, packaged, and shipped: pre-build gates, the 9-dimension quality gate, build-event audit artifacts, token-budget heuristics, version-and-lifecycle rules, methodology preservation across releases, design-spec consumption, description refinement loop discipline, and environment-adaptive degradation discipline.

This KF applies to Skills on both surfaces (CP-side methodology Skills and CC-side runtime Skills). Surface-invariant Skill-authoring principles live here. The build tool that operationalizes these disciplines is `rootnode-skill-builder` (currently v3.0, this release). The Skill's references cite this KF as the canonical source; the KF is the methodology, the Skill is the application.

When designing a new Skill, building a Skill from a design spec, reviewing an existing Skill, or planning a versioned successor, this is the first KF consulted. For surface-invariant principles that govern Skill behavior at runtime (placement discipline, source authority hierarchy, evidence grounding), see `root_AGENT_ENVIRONMENT_ARCHITECTURE.md`. For the unified anti-pattern catalog scanned by quality gate dimension 7, see `root_AGENT_ANTI_PATTERNS.md`.

---

## 1. Why these disciplines exist

A Skill that ships without these disciplines is worse than no Skill at all: it gets installed, occupies activation surface, and silently underperforms. The failure modes the disciplines prevent are well-documented from production builds:

**Misplaced content.** A Skill is built when the work belongs in a hook, a path-scoped rule, CLAUDE.md, MCP, settings, or a subagent. The Skill ships, looks reasonable, and silently fails to deliver the guarantee the user actually needed. Pre-Build Gate 1 (decomposition) prevents this.

**Premature abstraction.** A Skill is built for a pattern that has surfaced once or twice — speculative future demand, "I think we'll need this," anticipated rather than demonstrated need. The Skill is built, the build cost is paid, and the pattern never recurs. The Skill becomes maintenance debt. Pre-Build Gate 2 (warrant) prevents this.

**Routing collision.** A Skill is built that overlaps an existing Skill in the ecosystem. Both auto-activate on the same query; user gets unpredictable triggering. Pre-Build Gate 3 (ecosystem fit) prevents this.

**Spec drift.** A Skill is shipped with frontmatter that violates the Agent Skills spec — description over 1024 chars, body over 500 lines, XML in YAML, README inside the Skill folder, kebab-case violations. The Skill installs but auto-activation breaks. The 9-dimension quality gate (D1 spec compliance) catches this.

**Activation drift.** A Skill is shipped with a vague description that fails the 50-description competition test. Claude does not auto-activate. The Skill is invisible to its users. The quality gate (D2 activation precision, D6 auto-activation enforcement) catches this.

**Methodology drift.** A Skill is built from a design spec but loses substantive content during build — the description gets sharper but the methodology gets shallower. The Skill ships looking correct but underdelivers. The quality gate (D3 methodology preservation) catches this.

**Hidden dependencies.** A Skill is built that fails standalone — it requires another Skill to be installed for its core value. When installed alone, it produces incomplete output. The quality gate (D5 standalone completeness) catches this.

**Version collision.** A successor Skill is built with the same frontmatter `name:` as its predecessor. Both folders coexist in `~/.claude/skills/`. The auto-activation engine treats them as separate Skills with overlapping descriptions; triggering becomes unpredictable. The version-and-lifecycle discipline (§7) prevents this.

**Methodology corruption across releases.** A successor Skill drifts methodology in subtle ways under the framing of "rename + composition-alignment release." Future audits cannot tell what was inherited intact and what changed without warrant. The methodology preservation discipline (§8) prevents this.

The disciplines below are the operational expressions of the surface-invariant principles in `root_AGENT_ENVIRONMENT_ARCHITECTURE.md` (placement, decomposition, lean-over-comprehensive, source authority, evidence grounding) applied to the specific work of building rootnode Skills.

---

## 2. Pre-build gates

Three gates run before any Skill build work begins. Each gate has a pass condition, a halt action, and an exception. Pass all three before parsing a design spec or constructing files.

### 2.1 Gate 1 — Decomposition

**The question.** Where does this work fit in the 7-layer Claude Code mechanism framework? The mechanisms are CLAUDE.md (always-loaded), `.claude/rules/` (path-scoped), Skills (intent-triggered procedures), subagents (isolated context specialists), hooks (lifecycle guarantees), MCP (external integrations), and settings (trust/permissions). For the full mechanism semantics, see `root_CC_ENVIRONMENT_GUIDE.md §1`.

**Pass condition.** The work is a multi-step procedure or methodology, triggered by user intent expressed in language, that produces a coherent deliverable or analysis, and is reusable across contexts (different projects, different users, different inputs). All four criteria must hold.

**Halt action.** If the work fits a different mechanism, redirect with brief explanation. Do not build the Skill. The redirect language by mechanism is documented in skill-builder `references/decomposition-framework.md`. Common redirects: enforcement requests → hooks; file-pattern requests → `.claude/rules/`; always-loaded standing context → CLAUDE.md; isolated specialist tasks → subagents; external service integration → MCP; permission boundaries → settings.

**Exception: hybrid placements.** Some requests genuinely warrant a Skill *plus* a different mechanism. The Skill provides the procedure ("how to validate a release"); the hook provides enforcement ("always run release validation before tagging"). Build the Skill; flag the companion mechanism as a build-summary recommendation. The user adds the companion separately. Hybrid placements are not Gate 1 halts.

**Critical signal interpretation.** When the user describes the work in Skill-build language but the underlying need is different, listen for the underlying need. "I want a Skill that *always* runs before deploys" — `always` signals enforcement; redirect to hook. "I want a Skill that *watches* for X" — `watches` signals lifecycle; redirect to hook. "I want a Skill that *knows about* our project structure" — signals always-loaded context; redirect to CLAUDE.md.

### 2.2 Gate 2 — Warrant

**The question.** Has the work pattern surfaced 3+ times in real use, with traceable evidence?

**Pass condition.** Three conditions all hold:

1. The work pattern has surfaced 3+ times in actual use. Not theoretical use, not anticipated use — concrete occurrences the user can name and locate (a session, a CV, a document).
2. The pattern is structurally consistent across occurrences. Not "I did three roughly similar things" but "the same procedure with predictable variation in inputs."
3. The future demand is plausible. Not "I might need this someday" but "this pattern keeps coming up; I expect it to keep coming up."

**Halt action.** If the warrant is thin (1–2 occurrences, speculative future need, "I think we'll need this," "this would be cool to have"), recommend a paste-and-edit template instead of building a Skill. The template captures the work shape, lets the user iterate freely on each instance, and includes explicit promotion criteria so future-self knows when to upgrade. Naming convention per User Preferences: `{code}_template_{descriptor}.md`. The template structure (purpose, promotion criteria, last-used date, use count, body) is documented in skill-builder `references/warrant-check-criteria.md`.

**Exception: upstream process-abstraction handoff.** When the user provides a process-abstraction handoff brief from an upstream Skill following the documented format (e.g., `rootnode-repo-hygiene` Cat 14 process-abstraction findings), the handoff brief is the warrant evidence. Gate 2 passes automatically. The handoff brief documents that the pattern has been observed and abstracted at the upstream layer; the Skill build formalizes it.

**Override mechanism.** A user can override Gate 2 with explicit reasoning ("I want this built despite thin warrant because [...]"). The override is captured in the promotion provenance audit artifact (§5). Future audits can see what was a warrant pass vs. an override.

### 2.3 Gate 3 — Ecosystem fit

**The question.** Where does this Skill belong in the rootnode runtime tooling map, and does it duplicate existing capability?

**Pass condition.** Three checks all pass:

1. **Surface placement is clear.** CP-side (runs in chat-side Projects) or CC-side (deploys to delivery project repositories) or both — and the placement is justified by the Skill's natural surface.
2. **Composition is documented.** Which existing rootnode Skills compose with this one (handoff-trigger-check, profile-builder, skill-builder, rootnode-cc-design, prompt-validation, project-audit, critic-gate, mode-router, repo-hygiene, etc.). Soft pointers only — the Skill works standalone.
3. **No duplication.** The Skill fills a clear gap, not a sliver of an existing Skill's domain. Vocabulary, surface, and verb-class differentiate from each adjacent Skill.

**Halt action.** If duplication is detected, surface to user. Ask whether to extend the existing Skill instead of building a duplicate. Building a duplicate creates routing collisions that are hard to undo. Vocabulary, surface, and verb-class are the disambiguation axes; check each.

**Output artifact.** Gate 3 produces the placement note (§5.1) regardless of pass/halt. On pass, the placement note documents the placement decision; on halt, the placement note documents what would have been built and why duplication blocked it (the user can revisit if the differentiation gets sharper).

For the full ecosystem placement decision logic — surface boundaries, composition lineage, duplication signals by Skill — see skill-builder `references/ecosystem-placement-decision.md`.

---

## 3. The 9-dimension quality gate

After the build pipeline produces SKILL.md and references, the Skill is scored across nine dimensions. Each dimension produces a pass/fail verdict with cited evidence. Dimensions 1–5 inherit from skill-builder v1 (production-validated through 21 v1.x Skill builds). Dimensions 6–8 are v2 additions (auto-activation enforcement, anti-pattern catalog scan, 7-layer leak-check) closing gaps surfaced during the Phase 27/28 methodology refresh. Dimension 9 (behavioral validation) was added after the CC ecosystem analysis (May 2026) identified pressure-testing as a methodology gap — the quality gate assessed Skill document architecture but not Skill behavioral effectiveness. v3.0 expands D9 into three sub-levels (D9a/D9b/D9c) tracking the empirical strength of the validation evidence at the build environment's tier.

### 3.1 D1 — Spec compliance

**Check.** Conformance to the Agent Skills specification: name in kebab-case (max 64 chars, no reserved words like "claude" or "anthropic"), description ≤ 1024 chars (always YAML-parsed length, not raw text), body under 500 lines and ~5000 tokens, no XML angle brackets in frontmatter, no README.md inside skill folder, folder name matches the `name:` field exactly, SKILL.md filename in exact case.

**Pass evidence.** Cite character counts, line counts, file structure listing, frontmatter parse result.

**Common catches.** Description over budget after YAML parse (block scalar expansion); body over 500 lines (move detail to references/); reserved-word collision in name; folder/name mismatch.

### 3.2 D2 — Activation precision

**Check.** The description triggers on the right tasks, stays silent on wrong tasks, and competes correctly when 50+ Skill descriptions are present in context. Test against both undertriggering (Claude's default bias on vague descriptions) and overtriggering (Claude pulling on adjacent-domain queries).

**Pass evidence.** Description includes verb-based trigger language (not just static descriptors), explicit trigger phrases the user would actually say, and negative triggers ("Do NOT use for...") at points where overlap with adjacent Skills is plausible. The 50-description competition test: walk a few adjacent Skills' descriptions; verify this Skill activates only on its territory.

**Common catches.** Vague trigger language ("for X-related tasks" without verbs); missing negative triggers; vocabulary overlap with adjacent Skills.

### 3.3 D3 — Methodology preservation

**Check.** Substantive content from the design spec is preserved in the built Skill. Instructions remain actionable and specific. No content loss disguised as compression.

**Pass evidence.** Compare against design spec methodology sections; verify each substantive claim, decision rubric, and quality criterion has a home in either SKILL.md or references/. Claims that were preserved verbatim per the spec's preservation discipline (§8 of this KF) remain verbatim.

**Common catches.** Vague paraphrases that lose specificity; missing reasoning behind a recommendation; quality criteria omitted as "implicit"; reference content that was supposed to be there but isn't.

### 3.4 D4 — Progressive disclosure

**Check.** SKILL.md contains the core workflow and instructions; reference files contain detailed rubrics, pattern libraries, extended examples, and edge cases. Each reference file is referenced from SKILL.md with guidance on when to read it. Reference files over ~300 lines have a table of contents. No nested subdirectories within `references/`.

**Pass evidence.** SKILL.md focused on the core decision-making sequence; references/ holds the depth. Cross-references resolve.

**Common catches.** Bloated SKILL.md with rubrics and pattern libraries inlined; orphaned reference files (not pointed at from SKILL.md); reference files referenced without "when to read" guidance; nested subdirectory structure.

**Intelligent abstraction principle (refinement of progressive disclosure).** The dimension's pass evidence above describes *what* good progressive disclosure looks like; the intelligent abstraction principle describes *how* to design for it from the start. SKILL.md sections that introduce new workflows are **routing surfaces** by default — they name the workflow, identify which tier or mechanism applies, and point to the reference where the procedural depth lives. SKILL.md does not duplicate procedural content from its references. The 500-line SKILL.md ceiling is not a constraint to compress around at build time; it is a **design-phase forcing function** that drives correct layer placement at authoring time. Applied this way, the ceiling raises architectural quality automatically rather than requiring compression-time discipline. The principle compounds — each Skill that enforces routing-surface discipline raises the architectural floor for downstream Skills built using the same methodology. This is a refinement of the long-standing progressive disclosure discipline canonicalized in this dimension, not a new methodology claim; what changes is that the principle is applied at design time as the primary lens rather than at build time as a fallback.

### 3.5 D5 — Standalone completeness

**Check.** The Skill delivers complete value when installed alone. Cross-Skill references are soft pointers only ("for deeper specialization, see X if available"). The Skill never fails, produces incomplete output, or defers a user request because another Skill is not installed.

**Pass evidence.** Search the SKILL.md and references/ for cross-Skill references; confirm "if available" language is consistently present. Test the standalone constraint mentally: if this were the only rootnode Skill installed, would it still produce its core deliverable?

**Common catches.** Hard cross-Skill imports ("invoke X to do Y"); references that assume another Skill's output schema is in scope; "see X" without "if available" qualifier.

### 3.6 D6 — Auto-activation enforcement (v2)

**Check.** The description contains verb-based triggering-context language (not just static descriptors). Auto-invocation defaults to on. If `disable-model-invocation: true` is set in frontmatter, explicit reasoning is captured in `metadata.notes` documenting why this Skill should be human-only.

**Pass evidence.** Description has triggering verbs that match user intent expressions ("build," "audit," "convert," "design"). Frontmatter inspection: `disable-model-invocation` either absent (default on) or accompanied by `metadata.notes` justification.

**Common catches.** Manual-only Skills without justification (the Manual-only Skills anti-pattern, `root_AGENT_ANTI_PATTERNS.md §4.3`). Static-descriptor descriptions without verbs ("for prompt-related tasks").

**Why v2 added this dimension.** v1 quality gate didn't enforce auto-activation as a positive discipline — it caught the failure mode (D2 catches missing triggers) but didn't enforce the principle. The Phase 27/28 cross-evaluation surfaced auto-activation discipline as a Skill-build first principle that warranted explicit enforcement. For full discipline see skill-builder `references/auto-activation-discipline.md`.

### 3.7 D7 — Anti-pattern catalog scan (v2)

**Check.** Scan the produced SKILL.md and references/ against the Skill-relevant subset of `root_AGENT_ANTI_PATTERNS.md`. Each detected pattern surfaces as an advisory warning with a section reference back to the catalog.

**Pass evidence.** Walk the catalog's Skill-relevant patterns explicitly. The Skill-relevant subset includes:

- `§2.1` Monolithic standing context (bloated SKILL.md, surface-invariant)
- `§3.4` Kitchen Sink (multiple semi-independent concerns co-located, structural CP-side)
- `§3.5` Blurred Layers (rules mixed with reference content, structural CP-side)
- `§3.6` Build-scaffolding leak in user-facing artifact (project-specific brief references in `metadata.original-source`, internal phase tags, brand-anchored examples — structural CP-side)
- `§4.3` Manual-only Skills without justification (CC-side)
- `§4.11` Verification-before-completion absent (CC-side)
- `§4.14` Stale content (CC-side)

For the Skill-internal scan procedure see skill-builder `references/anti-pattern-catalog.md`.

**Disposition.** Warnings are advisory, not blockers — patterns are sometimes intentional. Three dispositions per catch: REVISED (Skill changed to resolve the catch), ACCEPTED with reasoning (catch documented as deliberate; reasoning captured in the AP-warning audit artifact §5.3), or HALT (catch is severe enough to block release; user reviews and decides).

**Why v2 added this dimension.** v1 quality gate did not surface anti-pattern catches systematically. Several v1.x Skills shipped with §3.4 Kitchen Sink or §3.5 Blurred Layers patterns that were intentional but undocumented — future audits had no record of whether the pattern was a deliberate choice or oversight. D7 makes the choice explicit and durable.

### 3.8 D8 — 7-layer leak-check (v2)

**Check.** Scan produced content for material that should have been placed in another mechanism per the 7-layer framework. Common leaks:

- File-pattern rules in references/ → candidate for `.claude/rules/`
- Always-relevant facts the user must always know → candidate for CLAUDE.md
- Enforcement guarantees expressed as instructions ("always run X before Y") → candidate for hooks
- External integration logic with API calls expressed as procedural prose → candidate for MCP

**Pass evidence.** Walk each common-leak category explicitly. Surface candidates as warnings.

**Disposition.** Warnings are advisory. User decides whether to extract leaked content into the correct mechanism (and, if extracted, whether the Skill is still warranted standalone).

**Why v2 added this dimension.** v1 caught misplacement at Gate 1 (the entire Skill belongs in a different mechanism), but did not catch partial leakage (most of the Skill is correctly placed, but a section of it should have been a `.claude/rules/` file or a hook). D8 catches the partial-leak failure mode.

### 3.9 D9 — Behavioral validation (v2.1, expanded v3.0) `[RECOMMENDED]`

**Check.** Has the Skill been tested against at least one adversarial scenario where Claude would fail without it? The dimension assesses the Skill's behavioral effectiveness, not its document architecture (D1–D8 cover architecture).

D9 was a single-tier recommendation in v2.1. v3.0 expands D9 into three sub-levels — D9a / D9b / D9c — that reflect the empirical strength of the evidence captured at validation time. Each sub-level has its own pass conditions and tier of evidence; the **build summary records which sub-level was applied** so future audits can read the evidentiary basis for the D9 verdict. The dimension itself remains RECOMMENDED, not REQUIRED.

The sub-levels exist because validation infrastructure differs across build environments. Tier A environments (subagents available, runnable execution available) can run with-Skill vs. without-Skill comparison empirically. Tier B environments (execution available, no subagents) can confirm execution under realistic test prompts but cannot run baseline comparison. Tier C environments (neither subagents nor execution available) fall back to analytical reasoning grounded in the 10-tendency taxonomy. The three sub-levels are degradation paths, not parallel options — the build CV applies the strongest tier the environment supports. The environment-adaptive degradation discipline (§10) is the operational model that determines tier applicability; the description refinement loop discipline (§9) is the methodology that D9b/D9c invoke when generating the trigger eval set used to confirm execution.

#### 3.9a D9a — Empirical Tier A (strongest evidence)

**Pass conditions** (all must be met):

1. **With-Skill vs. without-Skill comparison run.** A representative scenario set is executed twice — once with the Skill loaded (GREEN), once without it loaded (RED). Both runs use the same trigger evaluations and the same downstream task.
2. **Outcomes graded via subagent grader.** Each run's output is scored by a grader subagent against rubric assertions (per `agents/grader.md` schema). The grader's pass/fail per assertion is the empirical evidence.
3. **GREEN/RED differential is materially positive.** The Skill-loaded run materially outperforms the baseline on the assertions the Skill is designed to enforce. "Material" means more than chance — pre-defined threshold per scenario.

**Required infrastructure.** Subagent execution available; execution environment available; trigger eval set generated per §9 procedure; rubric assertions defined per `references/behavioral-validation.md`.

**Pass evidence.** Cite the scenario set, the trigger evals run, the grader outputs (pass/fail per assertion for both GREEN and RED), and the differential analysis. Captured in the build summary as `D9: Tier A — empirical comparison (N scenarios, GREEN/RED differential = X%)`.

#### 3.9b D9b — Empirical Tier B (moderate evidence)

**Pass conditions** (all must be met):

1. **With-Skill execution confirmed via realistic test prompts.** The Skill is loaded into a runnable environment; representative trigger evaluations from the §9 generated set are executed; the Skill's auto-activation and procedural compliance are observed directly.
2. **Qualitative review of outputs.** Outputs from the test runs are reviewed by the build CV against the Skill's stated quality criteria. No subagent grader required; the review is qualitative but explicit.
3. **No baseline comparison required.** Tier B does not require a without-Skill RED run; the evidence rests on with-Skill behavioral confirmation alone.

**Required infrastructure.** Execution environment available; subagent execution NOT required; trigger eval set generated per §9 procedure.

**Pass evidence.** Cite the test prompts run, the observed activation and behavior, and the qualitative review verdict. Captured in the build summary as `D9: Tier B — empirical execution (N test prompts, qualitative compliance: pass/fail)`.

#### 3.9c D9c — Analytical (weakest evidence; valid floor)

**Pass conditions** (all must be met OR the skip condition applies):

1. **Pressure scenario documented.** At least one scenario is described where Claude, without the Skill loaded, would produce incorrect behavior the Skill is designed to prevent.
2. **Baseline failure credibly expected.** The expected without-Skill failure is grounded in a documented Claude behavioral tendency from the 10-tendency taxonomy or in production-observed failure modes. Citation required.
3. **Compliance with Skill credibly expected.** The Skill's countermeasure formulation is shown to address the identified tendency. The reasoning chain from tendency → countermeasure → expected compliance is explicit.

**Required infrastructure.** None — analytical reasoning only. Tier C is the fallback when neither subagent execution nor a runnable environment is available, and the discipline floor when validation infrastructure is absent.

**Pass evidence.** Cite the scenario, the behavioral tendency, the countermeasure mechanism, and the reasoning chain. Captured in the build summary as `D9: Tier C — analytical (tendency: <name>, countermeasure: <mechanism>)`. This was the v2.1 D9 pass standard; v3.0 keeps it as the analytical floor.

**Skip condition.** The Skill is reference-only, data-carrying, or configuration-driven — it has no behavioral compliance to test. Examples: context carriers, profile schemas, block libraries used by other Skills. Mark as `D9: SKIPPED — no behavioral compliance surface` with one-sentence justification. The skip condition applies regardless of which sub-level the build environment otherwise supports.

**Classification.** D9 remains RECOMMENDED, not REQUIRED. All three sub-levels carry the same dimensional weight; the verdict per dimension specifies which sub-level applied. A Skill that passes D1–D8 but lacks D9 validation is shippable. The sub-level architecture allows Skills to record the strongest evidence available without forcing build halts when stronger evidence cannot be produced.

**Cross-references.** The trigger eval set referenced by D9a/D9b is generated per the description refinement loop discipline (§9). The tier applicability decision is made per the environment-adaptive degradation discipline (§10).

**Disposition.** Advisory for v3.0. Future evolution may tighten D9a to REQUIRED for discipline-enforcing Skills (tendencies #1–#10 countermeasures) when subagent infrastructure is broadly available, while keeping the lower tiers as fallbacks.

**Source pattern.** The pressure-testing methodology was identified during the CC ecosystem analysis (May 2026) from Superpowers v5.1.0's `writing-skills` skill, which applies TDD to skill authoring — write pressure test scenarios with subagents, watch Claude fail without the skill, write the skill to address observed rationalizations, verify compliance. The Meincke et al. (2025, N=28,000) finding that persuasion techniques more than doubled LLM compliance rates (33% → 72%) provides the research grounding for why countermeasure language design matters enough to validate empirically. The Tier A/B/C sub-level formalism was added in v3.0 from the Opus 4.6 cross-pass analysis (§5.2) of Anthropic's `skill-creator` empirical pipeline.

---

## 4. Audit artifacts

Three artifacts are produced during a Skill build event. Each documents a specific gate's reasoning for durable record. Together they form the build provenance — future audits, future reviewers, future evolutions all read these artifacts to understand what was decided and why.

### 4.1 Placement note — ALWAYS produced

**File name.** `{skill-name}_placement.md` (or `{skill-name}_placement_note.md` per repo convention).

**Production timing.** Step 0 Gate 3 of the build pipeline. Produced regardless of Gate 3 verdict (pass or duplication-halt).

**Mandatory rule.** Always produced. Placement decisions are durable record even when nothing surfaces as a catch — they document which differentiation axes the user evaluated and which adjacent Skills were checked. Future Skills built into the same ecosystem read the prior placement notes to understand the differentiation landscape.

**Content.** CP/CC surface placement; composition lineage (Producer→Consumer chains, lateral composition with critic-gate or mode-router, downstream composition deferred to v2.x); duplication audit table (each adjacent Skill, the differentiation axis); ship sequencing if applicable; the suggested entry for the runtime tooling catalog in `root_AGENT_ENVIRONMENT_ARCHITECTURE.md §6` (the Skill build does not auto-edit canonical KFs — methodology updates remain human-reviewed; the placement note surfaces the recommended entry for human review).

**Filing destination.** `Projects/{CODE}/research/` (or per-project equivalent). Filed alongside the deployable zip but separate from it.

### 4.2 Promotion provenance — CONDITIONAL

**File name.** `{skill-name}_promotion_provenance.md` (or `{skill-name}_promotion_evidence.md`).

**Production timing.** Step 0 Gate 2 of the build pipeline.

**Mandatory rule.** Produced when Gate 2 warrant evidence is provided OR when Gate 2 is overridden with reasoning. Not produced when the build is a fresh build with implicit warrant (rare — most builds either have explicit evidence or an override). For successor Skills (v2+ from a v1 predecessor), the warrant is inherited from the predecessor and the promotion provenance documents the inheritance lineage rather than fresh evidence.

**Content.** For first builds with explicit evidence: the evidence (occurrences, sessions, dates, structural consistency claim, plausibility argument). For overrides: the override reasoning. For successor builds: the predecessor's warrant evidence (cited intact), what is preserved verbatim from the predecessor, what evolves and why, the source-of-authority for each evolution item (mechanical consequence / composition alignment / brand-surface cleanup / new claim with fresh warrant).

**Why successor builds need this.** Without explicit promotion provenance, future audits cannot tell which v2 changes were inherited intact and which were new claims. The provenance creates a durable record that supports the methodology preservation discipline (§8).

**Filing destination.** Same as placement note — `Projects/{CODE}/research/`.

### 4.3 AP-warning summary — CONDITIONAL

**File name.** `{skill-name}_ap_warnings.md`.

**Production timing.** Step 5 D7 of the build pipeline.

**Mandatory rule.** Produced when D7 surfaces any catches. Not produced when D7 finds no catches.

**Content.** Summary table of catches (pattern + surface tag + status: CATCH/REVISED/ACCEPTED/HALT). Per-catch detail section: pattern name and catalog reference (`root_AGENT_ANTI_PATTERNS.md §X.Y`); surface tag; catch context (where in the Skill the pattern surfaces); disposition with reasoning. For ACCEPTED dispositions, the reasoning section is load-bearing — it tells future audits what was a deliberate choice. For REVISED dispositions, the reasoning documents what changed.

**Why future audits read this.** When a Skill is reviewed for a v2 build, the AP-warning summary tells the v2 build whether existing patterns were deliberate (preserve) or oversights (revise). Without the summary, every catch becomes ambiguous on re-evaluation.

**Filing destination.** Same as the other two artifacts.

### 4.4 Separation from the deployable zip

All three artifacts ship as separate files OUTSIDE the deployable zip. The deployable zip contains exactly the runtime artifacts (`{skill-name}/SKILL.md` + `{skill-name}/references/*.md`); the audit artifacts are build-event metadata that the runtime never consumes. Mixing them inside the zip pollutes the deployable and confuses installers ("are these files part of the Skill?").

The build delivery sequence: zip first (drop-in ready for `~/.claude/skills/` or the rootnode-skills repo), audit artifacts second (filed separately to `Projects/{CODE}/research/`).

### 4.5 Retention discipline — MANDATORY

The §4.1–4.3 filing destinations are not advisory. Audit artifacts MUST be filed at `Projects/{CODE}/research/` (or per-project equivalent) at build closeout. Filing is part of the build CV — the build is not complete until artifacts are filed.

**Closeout obligation.** The build CV's closeout protocol verifies filing happened. If a build CV closes without artifact filing, the next session's audit cannot reconstruct provenance. The Phase 31c audit found this gap directly: 5 post-discipline Skills had artifacts existing somewhere (in operator memory, scattered downloads, undocumented locations) but not filed at the canonical destination. The audit could not verify them; the operator was not previously informed retention was a requirement.

**Why mandatory and not advisory.** The artifacts are the durable build provenance. Without them, future audits and v2.x builds cannot trace what was decided and why, what is preserved verbatim from a predecessor, what evolves and on what authority. The build can produce excellent runtime artifacts (zip) and still leave an unauditable methodology trail if the audit artifacts aren't filed. The Phase 31c experience proved this is a real failure mode, not theoretical.

**What the build's closeout looks like under this discipline.** The build CV's final action is artifact filing. Specifically: (1) zip is delivered to operator; (2) all three audit artifacts (or the conditional ones produced) are delivered to operator with explicit "file these at `Projects/{CODE}/research/`" instruction; (3) operator confirms filing or explicitly defers (deferral becomes a build-CV open item that future sessions track, not a forgotten obligation). The build is not "complete" until artifacts are at their filing destination.

**Retroactive application.** Skills built before this discipline was canonicalized (pre-Phase 31a) are not retroactively required to produce artifacts — they predate the requirement. Skills built post-Phase 31a where artifacts were produced but not filed are subject to the discipline retroactively: locate the artifacts and file them. If they cannot be located, document the gap explicitly in `root_build_context.md` so the unauditable trail is at least known.

### 4.6 Discipline-marker convention — frontmatter field

To make audit-time provenance discrimination unambiguous, post-discipline Skills carry an explicit frontmatter field in `metadata`. Future audits read this field as ground truth, not heuristic.

**Field name.** `metadata.discipline_post` (string value).

**Values (extensible enum).**

- `phase-30` — Skill was built under Phase 30 audit-artifact discipline (placement note + conditional promotion provenance + conditional AP warnings, filed at `Projects/{CODE}/research/`).
- Future phases may add values (`phase-31a` for the methodology centralization application; `phase-31x` for whatever a future cycle adds). Multiple values are not stacked — the field carries the most recent applicable phase and prior compliance is implied by phase ordering.

**When skill-builder emits this field.** Every Skill build under skill-builder current version or later. The field is not optional — it is part of the spec-compliance dimension D1. Skills built without it fail D1 going forward.

**What the field signals to audit Skills.** Provenance is post-discipline. The audit should expect artifacts at the filing destination per §4.1–4.3 and discriminate verdicts using the §3.7 D7 catalog as the substantive scan.

**What the field's absence signals.** Skill predates the discipline. Audit verdicts default to `N/A — predates discipline` for any audit dimension that requires post-discipline artifacts.

**Why heuristic discrimination by version field failed.** The Phase 31c audit relied on `metadata.version: "2.0"+` OR `metadata.predecessor:` as a provenance proxy. This produced misclassifications in both directions: high-version-number Skills that predate the discipline (false positives), and first-build-v1.0.x Skills built under the discipline with no predecessor (false negatives). Version numbers are per-Skill convention; they don't encode discipline state. The explicit marker corrects this.

**Retroactive application.** Skills built post-Phase 31a where the marker was not yet emitted are eligible for retroactive marker addition. The Phase 31d remediation cycle adds `metadata.discipline_post: phase-30` to the 7 confirmed post-Phase-30 Skills (cc-design v2, repo-hygiene v1, critic-gate, mode-router, handoff-trigger-check, profile-builder, skill-builder v2). Pre-discipline Skills do not receive the marker — their absence of it is the correct signal.

---

## 5. Token budget known-gap discipline

Reference files have a soft guideline of ≤5000 tokens each. The guideline supports D4 (progressive disclosure) — references should load productively in active context without crowding out the conversation budget. References at 5500–6500 tokens still load productively in most workflows; references > 7000 tokens warrant splitting along natural section boundaries.

### 5.1 Design-time estimation

At build time, the actual Opus 4.7 tokenizer is not always available locally. The design-time estimation discipline:

- **Lower bound:** chars / 4. Conservative estimate that holds for non-technical English.
- **Upper bound:** chars / 4 × 1.45 for technical/markdown content. The 1.45× multiplier comes from independent measurement on technical-markdown content (1.45–1.47× empirically observed; sourced as Tier 3 — tested production); Anthropic publishes a 1.0–1.35× tokenizer multiplier range in primary documentation (Tier 1), but markdown formatting overhead, code fence handling, and technical vocabulary push the effective multiplier higher.

For a 22,000-character reference: lower bound ~5,500 tokens, upper bound ~7,975 tokens. The lower-bound exceeds 5,000 — the reference is flagged for review. Whether to split depends on the upper-bound under actual measurement.

### 5.2 Install-time authoritative measurement

The actual Opus 4.7 tokenizer at install time is the authoritative measurement. The install-time discipline:

1. After install, verify the reference token counts against the actual tokenizer (e.g., via `count_tokens` API).
2. If a reference materially exceeds 5,000 tokens (rough threshold: 6,500+), consider splitting.
3. If a reference exceeds 7,000 tokens, the split is strongly recommended.
4. If the split is made, update SKILL.md's reference table accordingly.

### 5.3 Splitting strategy

When a reference is split, split along the natural section boundaries — the structural fix domains, the pattern categories, the workflow phases. Do not split arbitrarily or mid-section. The split files should each be standalone-readable; SKILL.md's reference table is updated to point at the new files with their respective "when to read" guidance.

### 5.4 Why this is a known-gap discipline

The discipline is documented as a "known gap" because the design-time estimation is a heuristic and the install-time measurement is sometimes deferred. The Skill builds successfully with a flagged-for-review token estimate; the actual measurement happens at install time. The AP-warning audit artifact (§4.3) records flagged references with their lower-bound estimates so the install-time review knows what to verify.

---

## 6. Version and lifecycle discipline

Successor Skills (v2+ from a v1 predecessor) follow a specific discipline to prevent version collision and preserve the build provenance.

### 6.1 When the rename rule applies

The rename rule applies when a successor changes the frontmatter `name:` field — typically because the Skill's scope, surface, or naming convention has shifted (e.g., `rootnode-cchq-design` → `rootnode-cc-design` after the cchq → root.node methodology absorption).

### 6.2 The rule

The successor cannot coexist with the predecessor in `~/.claude/skills/`. Both folders, both frontmatter `name:` fields, both descriptions present in the auto-activation index causes the platform to treat them as separate Skills with overlapping descriptions — auto-activation triggering becomes unpredictable.

The install discipline:

1. Remove the predecessor folder before installing the successor.
2. The successor's install instructions document this explicitly (Path A personal install, Path B GitHub release).
3. The rename is intentional, not a migration — the predecessor and successor are incompatible duplicates by design.

### 6.3 The predecessor metadata field

The successor's frontmatter carries `metadata.predecessor: "{predecessor-name} v{version}"` for traceability. This makes the inheritance lineage machine-readable and supports future audit: "which Skills are evolution lineages from a v1, and which are fresh builds?"

### 6.4 When the rename rule does NOT apply

Patch releases (v1.0.0 → v1.0.1) and minor releases (v1.0 → v1.1) within the same `name:` are routine version updates. The predecessor folder is overwritten by the successor in place; no removal step required. The rename rule is specific to `name:` field changes.

### 6.5 Rollback

Successor releases do not eliminate the predecessor's deployable artifact. The predecessor zip remains in `Projects/{CODE}/research/` as a durable archive; rollback is `rm -rf successor && unzip predecessor` — non-destructive.

---

## 7. Methodology preservation discipline

Successor Skills built as rename / composition-alignment / brand-surface-cleanup releases preserve the methodology framework verbatim. New methodology claims require fresh warrant evidence per Gate 2.

### 7.1 What "verbatim" means

The methodology framework is preserved without alteration to its substantive claims. Specifically preserved:

- The sourced-and-cited claims about Claude behavior, agent design, MCP capability, and Claude Code mechanics.
- The 5-tier source authority hierarchy and inline source-tag conventions.
- The 7-layer placement framework and decomposition discipline.
- The agent-warranted test, change_log discipline, halt-and-escalate trigger design, files-as-context discipline, additive evolution, generalizable-vs-project-specific tagging.
- Any tested production patterns inherited from the predecessor's warrant base.

### 7.2 What can change without warrant

Compatible with preservation:

- **Section structure.** Renumbering, restructuring for readability, table-of-contents adjustments.
- **Framing and preamble.** Updates to fit the successor's name, scope, or platform context.
- **Specific applications.** Per-mode adaptations, per-surface examples, internal cross-reference updates.
- **Filename references.** `cchq_*` → `root_*` prefix renames; `cchq-methodology-patterns.md` → `cc-methodology-patterns.md` rename.
- **Vocabulary alignment.** Term-for-term swaps where the underlying claim is unchanged (e.g., `addresses` → `addresses_finding` for terminology alignment with an upstream Producer Skill).
- **Cross-Skill contract alignments.** Updates that align field names, schema patterns, or composition semantics with a verified upstream Producer.
- **Brand-surface cleanups.** Anonymization that removes proprietary identifiers without altering methodology grounding.
- **Tone calibration.** Adjustments to prose voice consistent with the AEA "explain the why" principle (`root_AGENT_ENVIRONMENT_ARCHITECTURE.md §4.11`) — converting imperative-without-rationale phrasing to reasoned voice where the reasoning carries equal force, while preserving imperative voice for spec constraints, safety boundaries, and other places where reasoning would dilute the constraint. Substantive claims unchanged; only surface phrasing. Tone calibration is permitted within preservation because it affects how the methodology is communicated, not what the methodology claims.

### 7.3 What requires warrant

Incompatible with preservation (requires fresh Gate 2 evidence):

- **New substantive claims.** Adding a new pattern to the AP catalog; introducing a new agent design rule; adding a new tier to the source authority hierarchy; documenting a new placement mechanism.
- **Modified substantive claims.** Changing an existing claim's scope, criteria, or applicability.
- **New behavioral countermeasures.** Adding to the 10-tendency taxonomy, modifying countermeasure templates with new evidence.
- **New cross-Skill contracts.** Introducing a new field, threshold, or composition pattern that downstream consumers must align to.

For each item in this category, the promotion provenance audit artifact (§4.2) carries a row documenting the warrant evidence (or override reasoning).

### 7.4 The audit trail in promotion provenance

The promotion provenance documents the evolution-source for every change in the successor:

| Change type | Source of authority | Evidence type |
|---|---|---|
| Mechanical consequence of locked decision | Scope-lock or design spec | Documentation alignment |
| Composition-alignment to verified Producer | Upstream Producer Skill's built artifact | Cross-Skill contract alignment |
| Brand-surface cleanup | Hyge-anonymization discipline (`root_AGENT_ENVIRONMENT_ARCHITECTURE.md §4.10`) | Brand-surface cleanliness |
| Tone calibration | "Explain the why" principle (`root_AGENT_ENVIRONMENT_ARCHITECTURE.md §4.11`) | Surface-phrasing alignment |
| New claim with fresh warrant | New Tier 1–4 evidence | Methodology evolution (requires Gate 2) |

If a row would land in the fifth category, the v2 release is no longer rename + composition-alignment + brand-surface — it is methodology evolution. The build CV halts and surfaces the methodology evolution to the user; the canonical KF is updated in a separate human-reviewed cycle before the v2 release continues.

---

## 8. Design-spec consumption discipline

Build CVs consume design specs produced by upstream design CVs. Two principles govern how the build CV handles findings that surface during the build itself.

### 8.1 Within-scope-lock material findings

**Definition.** A finding that surfaces during the build CV that is additive within the scope-lock document's locked decisions, locked changes, and locked dispositions, and does not contradict any locked intent.

**Rule.** Incorporate the finding into the build without amending the scope-lock document. Surface the finding in the build_context.md entry as a "within-scope-lock material findings" subsection so future audits can trace what was added beyond the explicit scope-lock list.

**Test.** Would this finding require revisiting any of the locked decisions? If no, it's within scope-lock. If yes, halt the build and request a scope-lock v2.

**Examples (from Phase 30 D-design CV).**

- **Finding-ID schema pattern alignment** (`^F-\d+$` → `^F-\d+\.\d+$`): within scope-lock decision 7 (cross-Skill contract alignment with repo-hygiene's `F-{cat}.{n}` finding ID format). Locked intent was contract alignment; the specific regex pattern is a mechanical consequence.
- **Schema field rename** (`addresses` → `addresses_finding`): within §2.9 locked intent (terminology consistency with repo-hygiene's "finding ID" language). Locked intent was terminology consistency; the specific field rename is the application.
- **Citation precision in catalog table** (`§1.1` → `§2.4`): within canonical AP cross-reference intent. Locked intent was canonical numbering; the specific section number is the corrected citation.

In all three cases, the build CV incorporated the finding directly. No scope-lock v2 was issued.

**Why this matters.** Without an explicit "within-scope-lock material findings" pattern, builds either (a) over-faithfully halt at every finding and request scope-lock amendments, producing build-CV thrash, or (b) silently incorporate findings without surfacing them, producing scope drift. The pattern names the legitimate middle ground.

### 8.2 Implementation-surface vs. methodology-correction

**Definition.** When a build CV surfaces something that needs change, identify the right level. There are two:

- **Implementation surface:** the Skill's own files (SKILL.md, references/*.md, schema/*.json). The build CV can edit these directly.
- **Methodology correction:** a canonical KF (`root_AGENT_ENVIRONMENT_ARCHITECTURE.md`, `root_CC_ENVIRONMENT_GUIDE.md`, `root_AGENT_ANTI_PATTERNS.md`, this KF, etc.). The build CV does NOT auto-edit canonical KFs — methodology updates remain human-reviewed.

**Rule.** Edit the implementation surface as part of the build CV. Surface methodology corrections as recommendations in the build summary; the canonical KF is edited in a separate human-reviewed cycle before the recommendation is incorporated.

**Test.** Is this change to the Skill (instruction, reference, schema, description, frontmatter), or to the surface-invariant principle that governs Skills? If the former: implementation surface. If the latter: methodology correction.

**Example.** A build CV surfaces a Skill's reference file that uses an outdated section number for an anti-pattern. Two cases:

- *The reference's citation is wrong; the canonical section number in `root_AGENT_ANTI_PATTERNS.md` is correct.* Implementation-surface fix: update the reference's citation. Build CV proceeds.
- *The reference's citation is correct; the canonical section number in `root_AGENT_ANTI_PATTERNS.md` was changed in an interim refactor and is now wrong.* Methodology correction: the canonical KF needs a fix. Build CV surfaces the recommendation; user reviews and updates the KF separately.

**Why this matters.** Without the discipline, build CVs either (a) auto-edit canonical KFs in the build flow, breaking the "methodology updates remain human-reviewed" invariant, or (b) treat every methodology-corrective recommendation as a build halt, slowing builds unnecessarily.

### 8.3 The Q-B3 origin

This discipline emerged from the Phase 30 D-build CV under the question "Q-B3: when a build surfaces something that requires methodology correction, where is the surface boundary?" The discipline is the answer: implementation surface = build CV scope; methodology correction = recommendation surface only.

---

## 9. Description refinement loop discipline

The 1024-character description field is the highest-leverage surface in a Skill — it is the auto-activation index entry that determines whether the Skill triggers on a user query. A description that fails to trigger renders every other discipline (build gates, quality gate, methodology preservation) inert; the Skill exists but the user never reaches it. The description refinement loop is the methodology that hardens a description against under-triggering and over-triggering through evidence-based iteration rather than authorial heuristic.

Two reasons this discipline lives at the methodology layer rather than as a Skill-specific procedure: it generalizes across every Skill build, not just `rootnode-skill-builder`'s — any future build CV that produces a description benefits from the same iteration shape — and the train/test split discipline that prevents overfitting is methodology-grade, not implementation detail. The reference application lives in `rootnode-skill-builder/references/description-optimization.md`; the canonical home for the discipline is here.

### 9.1 Trigger eval generation

Generate a corpus of realistic user-voice queries the Skill *should* trigger on (positive set) and a corpus of adjacent or distractor queries the Skill *should not* trigger on (negative set). Realism is load-bearing — synthetic queries written by the build CV in declarative voice ("a query about building a Skill") under-test the description because users do not phrase requests that way. The query corpus must mirror the way users actually phrase requests: incomplete sentences, context-laden references, ambiguous noun forms, copy-pasted error messages, casual register.

The minimum viable corpus: 8–12 should-trigger queries, 5–8 should-not-trigger queries, 2–4 edge cases (queries that could plausibly trigger either way). Larger corpora reduce variance per iteration; smaller corpora over-fit faster. Edge cases earn their place — they are the queries where the description's precision matters most.

### 9.2 Manual walkthrough discipline (Tier B/C floor)

The simplest form of the discipline is a manual walkthrough: read each query in the corpus, reason about whether the description's verbs, nouns, and trigger phrases would index that query, and note where the description misses or where adjacent Skills match more cleanly. Refine the description against the observations; repeat until the corpus stabilizes.

The manual walkthrough is the floor — every build CV runs at least this. It is the only form available when no execution environment is present (Tier C per §10). It is the moderate evidentiary form when execution is available but subagent grading is not (Tier B). The walkthrough is not a degraded automation; it is a different evidentiary form. Manual reasoning grounded in 50-description competition logic produces credible verdicts without infrastructure.

### 9.3 Automated optimization via `description_optimizer.py` (Tier A)

When subagent execution is available, the description refinement loop runs as an automated 5-iteration train/test loop:

1. Split the trigger eval corpus into a train set (used to drive description revisions) and a held-out test set (used to score each iteration without bleeding into the revision signal).
2. Run the current description against the train set; surface miss/false-positive cases.
3. Generate a revised description that addresses the train-set misses without obviously over-fitting (the revision prompt structure is documented verbatim in `references/description-optimization.md`).
4. Score the revised description against the held-out test set.
5. Repeat for N iterations; select the revision with the highest test-set score, not the highest train-set score — train-set wins are ambiguous between true improvement and overfitting.

The reference implementation is `rootnode-skill-builder/scripts/description_optimizer.py`. The build CV's role is to generate the trigger eval corpus and review the optimizer's iteration outputs; the optimizer's role is to mechanize the iteration loop and surface the per-iteration train/test scores for review.

### 9.4 Anti-overfitting principle

A description that scores 100% on the train set but degrades on the held-out test set has overfit to the train corpus's idiosyncrasies — the revision learned the corpus's shape rather than the underlying user-intent pattern. The discipline: evaluate every revision against the held-out test set as the primary signal; treat train-set wins as supportive evidence only. If train-set and test-set scores diverge by more than ~15%, the revision is likely overfit and should be discarded in favor of the prior iteration.

The held-out discipline is the structural reason the corpus is split rather than evaluated as a single set. Without the split, every iteration sees every query, the description is gradually bent toward the corpus shape, and the Skill triggers reliably on the corpus while degrading on out-of-corpus queries that share the underlying intent. The split makes overfitting detectable; without it, overfitting is invisible until the Skill ships and fails in production.

### 9.5 Triggering detection mechanism

The auto-activation engine signals a Skill trigger via the model's stream-event protocol: a `content_block_start` event with type `tool_use` and the Skill's name in the tool field. The triggering detection mechanism — the procedure that determines whether a given query triggered the Skill — monitors the stream for this event pattern and records the trigger result per query. The detection mechanism is preserved verbatim in `rootnode-skill-builder/scripts/description_optimizer.py` and documented in `references/description-optimization.md`.

The detection is critical because manual inspection of conversational output cannot reliably tell whether the Skill was invoked or whether the model simply produced output similar to what the Skill would have produced. The stream-event signal is the only ground-truth source. Refinement loops that score by output similarity rather than by trigger-event detection produce false positives (the model produced Skill-like output without triggering) and false negatives (the Skill triggered but the output didn't visibly differ).

### 9.6 Cross-references

The description refinement loop is invoked by D9 sub-levels:

- D9a (Tier A) uses the automated optimizer (§9.3) as part of empirical comparison.
- D9b (Tier B) uses the manual walkthrough (§9.2) or scoped automation that does not require subagents.
- D9c (Tier C) uses the manual walkthrough (§9.2) only.

The trigger eval corpus generated for description refinement is the same corpus used by D9a/D9b for behavioral validation. Generating one corpus serves both dimensions; this is intentional, not duplication. Tier applicability is determined per the environment-adaptive degradation discipline (§10).

For full procedural detail (eval query schema verbatim, query realism principles, train/test split mechanics, optimization prompt structure, run mechanics), see `rootnode-skill-builder/references/description-optimization.md`.

---

## 10. Environment-adaptive degradation discipline

Build CVs do not always run in the same environment. Some run with subagent execution available, full Anthropic SDK access, and runnable Skills under test. Others run in chat-side surfaces where neither subagents nor a runnable environment exists. The same Skill build methodology must produce credible verdicts across this range without either pretending capabilities it lacks or refusing to verify what it can. The environment-adaptive degradation discipline is the operational model that names the three tiers, specifies what each tier verifies, and defines the fallback paths between them.

The three tiers are degradation paths, not parallel options. The build CV applies the strongest tier the environment supports; lower tiers remain available as fallbacks when individual evaluation steps fail infrastructurally.

### 10.1 Tier A — full empirical pipeline

**Capabilities.** Subagent execution available; runnable Skill environment available; tooling layer (`scripts/`, `agents/`) invocable.

**What Tier A verifies.** Full behavioral validation per D9a — with-Skill vs. without-Skill comparison via subagent grader. Description refinement via automated train/test optimizer (§9.3). Version comparison via blind A/B with subagent comparator and analyzer (when applicable).

**Verdict format.** `D9: Tier A — empirical comparison (N scenarios, GREEN/RED differential = X%)`, with grader output and differential analysis captured in the build summary.

### 10.2 Tier B — empirical execution without subagents

**Capabilities.** Runnable Skill environment available; subagent execution NOT available.

**What Tier B verifies.** With-Skill execution confirmed via realistic test prompts per D9b. Description refinement via manual walkthrough (§9.2) or scoped scripts that do not require subagents. Version comparison via inline manual blind procedure.

**Verdict format.** `D9: Tier B — empirical execution (N test prompts, qualitative compliance: pass/fail)`, with test prompts and qualitative review captured.

### 10.3 Tier C — analytical floor

**Capabilities.** Neither subagents nor a runnable Skill environment.

**What Tier C verifies.** Behavioral validation per D9c — pressure scenario documented, baseline failure credibly expected from a cited Claude behavioral tendency, compliance credibly expected from the Skill's countermeasure formulation. Description refinement via manual walkthrough only. Version comparison documented as a deferred verification.

**Verdict format.** `D9: Tier C — analytical (tendency: <name>, countermeasure: <mechanism>)`, with cited tendency and countermeasure mechanism captured.

### 10.4 Tier determination

The build CV determines tier applicability at build time, not at design time. The decision rule:

1. Is subagent execution available in this environment? If yes, Tier A applies (assuming a runnable environment is also present).
2. If subagent execution is not available, is a runnable Skill environment available? If yes, Tier B applies.
3. If neither is available, Tier C applies.

The build CV records the determination explicitly in the build summary — which tier was selected and why. A build CV cannot claim Tier A evidence when Tier A infrastructure was unavailable; the discipline is "use the strongest tier the environment supports, no more." Pretending capabilities the environment lacks produces unauditable verdicts; refusing to verify what the environment can produces a discipline floor that under-rewards available infrastructure. The tier model resolves both failure modes by binding the verdict to the infrastructure.

### 10.5 Fallback paths

Each tier has an explicit fallback to the next lower tier when an evaluation step fails infrastructurally — for example, a subagent timeout in Tier A. The fallback rule: reattempt with extended budget; if still failing, fall back to the next-lower tier for that step only. Fallbacks are per-step, not per-build — a build can run most of D9 at Tier A and fall back to Tier B for one scenario without dropping the whole verdict. The build summary records both the headline tier and any per-step fallbacks so future audits can trace the evidentiary basis at the granularity it was produced.

### 10.6 Cross-references

Tier applicability gates the D9 sub-level (§3.9): D9a requires Tier A; D9b requires Tier B or Tier A; D9c is always available as the analytical floor. The description refinement loop (§9) uses the same tier model — Tier A invokes the automated optimizer, Tier B/C falls back to the manual walkthrough. Other empirical workflows (version comparison, benchmark aggregation) follow the same tier pattern.

For per-script tier compatibility tables and detailed fallback patterns, see `rootnode-skill-builder/references/multi-environment-adaptation.md`.

---

## 11. Where to go next

For surface-invariant principles that govern Skill behavior at runtime:

- **Layered context architecture and placement discipline:** `root_AGENT_ENVIRONMENT_ARCHITECTURE.md`. This KF is the surface-invariant principle layer; the build disciplines documented here apply those principles to Skill construction.
- **CC-side environment design (7-layer model that Gate 1 grounds against):** `root_CC_ENVIRONMENT_GUIDE.md §1`.

For the unified anti-pattern catalog:

- **Skill-relevant patterns scanned by D7:** `root_AGENT_ANTI_PATTERNS.md`. The full catalog with surface tags.

For the build tool itself:

- **The rootnode-skill-builder Skill (currently v3.0, this release):** the operational application of these disciplines. Its references (`decomposition-framework.md`, `warrant-check-criteria.md`, `ecosystem-placement-decision.md`, `auto-activation-discipline.md`, `anti-pattern-catalog.md`, `conversion-guide.md`, `skills-spec.md`) cite back to this KF as the canonical methodology. When this KF evolves, skill-builder's references regenerate against the new canonical.

For Project-level context budget (different concern):

- **Two-pool budget architecture and the ~66,500 token RAG threshold:** `root_OPTIMIZATION_REFERENCE.md` (context budget principles section). That KF covers Project-level token economy. This KF's §5 covers Skill-internal token discipline at the reference-file level.

For the broader Skill ecosystem evolution narrative:

- **Phase 27 cchq → root.node methodology absorption:** `root_build_context.md` Phase 27/28 entries.
- **Phase 29/30 build CVs that surfaced these disciplines:** `root_build_context.md` Phase 29/30 entries plus the Phase 30 D-build audit artifacts in Drive `Projects/ROOT/research/`.

---

*End of root_SKILL_BUILD_DISCIPLINE.md.*
