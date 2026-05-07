# Promotion Evidence — rootnode-repo-hygiene v1.0

Documentation of warrant evidence supporting promotion of this Skill from design to deployable v1.0. Tracks the skill-builder v2 Gate 2 evidence chain and the 8-dimension validation outcomes.

## Build provenance

**Built via:** rootnode-skill-builder v2.0 (frontmatter version "2.0", confirmed at session start)  
**Build date:** 2026-05-05  
**Design spec source:** root_design_repo_hygiene_skill.md (v2.0 root.node-framed; 743 lines)  
**Build mode:** Pass-through (user authorized full build with no halt-at-each-step)

## Gate 2 warrant evidence

Per skill-builder v2 Gate 2, warrant evidence is required to promote design to deployable. For rootnode-repo-hygiene, the evidence consists of 9 design lineage artifacts:

1. **`root_design_cc_methodology_skills.md` Section 3** — initial methodology Skill design enumerating CC-side audit needs.
2. **`root_design_cc_methodology_skills.md` Section 5** — extracted scope for repo-hygiene as a separate Skill from cc-design.
3. **`root_OPTIMIZATION_REFERENCE.md`** — 14-category catalog grounding (the categories enumerated in this Skill trace to optimization patterns documented here).
4. **`root_AGENT_ANTI_PATTERNS.md`** — canonical anti-pattern catalog (15 patterns scanned by this Skill, plus 5 explicitly not-scanned CP-only patterns).
5. **`root_CC_ENVIRONMENT_GUIDE.md`** — 7-layer model + discipline practices + hooks-vs-prompts boundary (the audit standard).
6. **`root_AGENT_ENVIRONMENT_ARCHITECTURE.md`** — surface-invariant placement discipline + chat→Code round-trip (Pattern 11) + files-as-context (Pattern 2).
7. **`root_design_repo_hygiene_skill.md` v1.0** — initial skill design (pre-rebrand to root.node framing).
8. **`root_design_repo_hygiene_skill.md` v2.0** — current design spec consumed by this build.
9. **Production validation 2026-05-04** — CC deployment sweep surfacing 23 findings across 14 categories with three-form authorization use and Path 3 commit-plan adaptation accepted as defer-to-downstream. Validation is cited in metadata.original-source and is the basis for the worked-example.md walkthrough.

**Gate 2 verdict:** PASS. The 9-artifact lineage exceeds the 3+ occurrence + design lineage standard.

## Composition relationships established

Three composition relationships documented in SKILL.md:

1. **With `rootnode-critic-gate` (Phase 2 batch review).** Documented in "Composition" section. Verdict handling (APPROVE / REQUEST_CHANGES with 3-cycle cap / REJECT) and threshold modes (`required` vs `optional`) specified. Profile field `critic_gate_threshold` controls the composition.

2. **With `rootnode-cc-design` REMEDIATE (downstream Producer→Consumer).** Documented in "Composition" section. Cat 11-14 findings + 7-layer leak findings route to REMEDIATE. The "Routing recommendations" section in the Phase 1 report names the handoff explicitly when `remediate_routing: true`.

3. **As Producer for `rootnode-skill-builder` v2 Gate 2.** Documented in "Composition" section + "Process-abstraction candidates" section. Methodology-generalizable Cat 14 candidates use the 8-field block format compatible with skill-builder v2's Gate 2 exception clause. The user uploads the candidate block as a process-abstraction handoff brief; skill-builder accepts it as warrant evidence without requiring the standard 3+ occurrence proof.

The third composition is reciprocal: this Skill is BUILT BY skill-builder v2 (Producer for skill-builder consumption) AND it PRODUCES warrant evidence for future skill-builder v2 invocations. The reciprocity is documented in process-abstraction-detection.md "Format compatibility" subsection.

## 8-dimension validation outcomes

| # | Dimension | Outcome | Notes |
|---|---|---|---|
| 1 | Spec compliance | PASS | All frontmatter, structural, and content fidelity checks pass; see placement.md |
| 2 | Activation precision | PASS | Description vocabulary unique in rootnode catalog ("rootnode-cc-design REMEDIATE", "rootnode-critic-gate", 14 specific hygiene categories); 4 negative triggers explicitly disambiguate against adjacent Skills |
| 3 | Methodology preservation | PASS | All 6 locked decisions (D6-D11) preserved across SKILL.md + references; verified via content fidelity table in placement.md |
| 4 | Progressive disclosure | PASS | SKILL.md (235 lines) carries activation + principles; references load on-demand; cross-references are file-to-file pointers, not duplicate content |
| 5 | Standalone completeness | PASS | All 3 compositions documented; Skill operates standalone when critic-gate threshold is `optional`; no hard dependencies on cc-design or skill-builder for Phase 1/2 execution |
| 6 | Auto-activation enforcement | PASS | 8 verb-based triggers in description + symptom triggers in "When to use" + 4 negative triggers; no `disable-model-invocation` flag set |
| 7 | Anti-pattern catalog scan (Skill itself) | PASS | Skill content respects the patterns it teaches: scope is bounded (CC-only), content layered (SKILL.md + references), no transcript-shape content, no enforcement-as-preference language about itself |
| 8 | 7-layer leak check (Skill itself) | PASS | Skill content respects the layers it teaches: principles in always-relevant layer (Important section), procedures in references (Skill content layer), composition partners named (subagent / specialist references), halt-on-failure as enforced discipline (lifecycle guarantees layer); no leaks |

## Risks tracked from session handoff

- **R1 — v2 not installed:** RESOLVED at session start (v2.0 confirmed in /mnt/skills/user/rootnode-skill-builder/SKILL.md frontmatter)
- **R2 — Description char overflow:** RESOLVED. First draft was 1383 chars; tightened to 1018 chars (under 1024 cap) while preserving all 8 explicit triggers + 4 negative triggers
- **R3 — Process-abstraction format drift:** RESOLVED. Cat 14 candidate format in process-abstraction-detection.md uses 8-field block matching design spec §10; format compatibility with skill-builder v2 Gate 2 documented explicitly
- **R4 — Single-CV budget overrun:** RESOLVED. Per-file create_file calls put content on disk rather than in chat context
- **R5 — Composition test gap:** RESOLVED. All 3 compositions verified during Dim 5 (cc-design REMEDIATE, critic-gate, skill-builder v2 Producer)
- **R6 — First non-self use of v2 may surface v2 issues:** No issues surfaced. Build completed cleanly; no workarounds required; pre-build gates and 8-dim validation worked as designed.

## Public ship status

**Recommendation:** Per Phase 29 entry, public ship deferred to v2.2 paired with skill-builder v2 release. The deferral is intentional — skill-builder v2 is a prerequisite for any user attempting to build their own version of this Skill (per the Producer relationship), and shipping repo-hygiene without skill-builder v2 in the public catalog would create a build-tooling gap.

**Local install timing:** Aaron's v2.1 personal Skills install timing is open per memory entry 6; this v1.0 build adds repo-hygiene to that install queue alongside skill-builder v2.

**Distribution package:** rootnode-repo-hygiene-v1.zip produced this session; ready for v2.2 paired ship.

## Approvals

Warrant evidence: PASS (9 artifacts)  
Composition relationships: PASS (3 documented)  
8-dim validation: PASS (all 8)  
Risk resolution: PASS (all 6 from SH §10)  
Promotion to v1.0: APPROVED
