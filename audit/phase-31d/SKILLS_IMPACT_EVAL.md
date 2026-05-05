# CC Ecosystem Analysis — Skills Impact Evaluation Brief

> **Purpose:** Claude Code design brief for evaluating and updating root.node Skills based on the CC ecosystem analysis of GSD v1.40.0 and Superpowers v5.1.0 (May 2026). Drop this file in the rootnode-skills repo and run the evaluation prompt below.
>
> **Source:** `root_CC_ECOSYSTEM_ANALYSIS.md` — full analysis with rationale, composition architecture, and KF impact assessment.

---

## Context

Two prominent CC frameworks were analyzed at source-code depth against root.node's methodology:

- **GSD v1.40.0** — heavyweight workflow orchestration (65 commands, 33 agents, 4.3M chars). Solves context rot via fresh-context subagents with persistent state management.
- **Superpowers v5.1.0** — lightweight behavioral methodology (14 skills, 616K chars, zero deps). Shapes agent discipline via persuasion psychology.

**Key finding:** Both systems compose with root.node's CC governance layer (critic-gate, mode-router, repo-hygiene) as documented in CC_ENVIRONMENT_GUIDE §8 — "thin governance over thick workflow systems." Zero CP overlap. Zero functionality conflict.

**Three KF changes have already been applied upstream (in the seed project):**

1. **D9 behavioral validation** added to `root_SKILL_BUILD_DISCIPLINE.md` — new quality gate dimension (RECOMMENDED, not REQUIRED) for pressure-testing Skill behavioral effectiveness.
2. **Persuasion-as-compliance note** added to `root_OPTIMIZATION_REFERENCE.md` — research grounding (Meincke et al. 2025, N=28,000) for countermeasure language design.
3. **MCP bloat expansion** in `root_AGENT_ANTI_PATTERNS.md` + cross-ref in `root_CC_ENVIRONMENT_GUIDE.md §1.6` — per-turn injection mechanism documentation.

This brief evaluates whether the shipped CC-side Skills need updating to reflect these upstream KF changes.

---

## Skills Under Evaluation

### 1. rootnode-skill-builder (v2.0)

**Evaluation question:** Does skill-builder's quality gate reference material need updating from 8 to 9 dimensions?

**Assessment:**
- skill-builder v2.0's references cite `root_SKILL_BUILD_DISCIPLINE.md` as the canonical source for the quality gate.
- The Skill's own `references/` files carry the quality gate dimensions.
- D9 was added upstream. skill-builder's references need to reflect D9.

**Required changes:**
- Update any reference file that lists the quality gate dimensions to include D9 (behavioral validation, RECOMMENDED).
- Update the SKILL.md body if it mentions "8 dimensions" or "8-dimension" — change to "9 dimensions" / "9-dimension."
- Update the description field if it mentions dimension count (check char budget — description is at 976/1024).
- D9 content to add: behavioral validation checks whether the Skill has been tested against at least one adversarial scenario. Three pass conditions (pressure scenario documented, baseline failure confirmed/credible, compliance confirmed/credible). Skip condition for reference-only/data-carrying Skills. RECOMMENDED classification.
- **Do NOT change the description field** if adding D9 would push past 1024 chars. The description triggers on build/review/revise — D9 is discoverable once the Skill is loaded.

**Verification:** After update, run a self-check — does the updated skill-builder pass its own 9-dimension quality gate?

### 2. rootnode-critic-gate (v1.0.2)

**Evaluation question:** Does the ecosystem analysis require any changes to critic-gate?

**Assessment:**
- Critic-gate's 4-check protocol (invariant compliance, scope authorization, detection narrowness, regression risk) is validated by the composition analysis — both GSD and Superpowers would benefit from critic-gate as a post-review safety layer.
- The persuasion-compliance research doesn't affect critic-gate — it's a structured gate, not a behavioral compliance mechanism.
- D9 doesn't affect critic-gate — D9 is about Skill build validation, not runtime gate operation.
- MCP bloat expansion doesn't affect critic-gate.

**Required changes:** None. Critic-gate v1.0.2 is current.

**Optional:** The composition seam documentation (how critic-gate integrates with GSD's execute-phase and Superpowers' SDD workflow) could be added to the troubleshooting reference as a "composition patterns" section. This is LOW priority and informational only.

### 3. rootnode-mode-router (v1.0.2)

**Evaluation question:** Does the ecosystem analysis require any changes to mode-router?

**Assessment:**
- Mode-router selects profiles for consuming Skills. No methodology changes from the ecosystem analysis affect profile selection logic.
- The composition with GSD (mode-router fires before phase starts) and Superpowers (mode-router selects strictness) validates the existing design without requiring changes.

**Required changes:** None. Mode-router v1.0.2 is current.

### 4. rootnode-repo-hygiene (v1.0)

**Evaluation question:** Does the MCP bloat expansion affect repo-hygiene's sweep categories?

**Assessment:**
- Repo-hygiene's `references/sweep-categories.md` already has MCP-related detection in its category set. The sweep maps to `root_AGENT_ANTI_PATTERNS.md §4.2`.
- The upstream expansion added per-turn injection mechanism detail and pre-phase audit guidance to the anti-pattern entry.
- Repo-hygiene reads the canonical anti-pattern catalog during sweeps — the expanded entry will be consumed automatically when the user has the updated KF.
- The Skill's own sweep-categories reference should be checked for consistency with the expanded canonical entry.

**Required changes:**
- Check `references/sweep-categories.md` for any MCP-related category. If it references the anti-pattern catalog entry, verify the reference is compatible with the expanded content. If the reference is by section number (§4.2), no change needed — the expansion is in-place.
- If the sweep category's detection rules could benefit from the per-turn injection detail (e.g., "flag servers whose tool schemas exceed X tokens" → now can note "this cost is per-turn, not per-invocation"), add a 1-sentence sharpening note to the detection focus.

**Verification:** Run the sweep category against a test repo with 5+ MCP servers. Confirm the expanded detection guidance produces actionable findings.

### 5. rootnode-cc-design (v2.0)

**Evaluation question:** Does the ecosystem analysis affect cc-design's modes?

**Assessment:**
- cc-design's DESIGN mode produces CC environments. The layer-fit boundary statement (§8 of CC_ENV_GUIDE) was validated by the analysis — "runtime Skills are thin governance over thick workflow systems." This is already documented.
- cc-design's RESEARCH mode could benefit from awareness that GSD and Superpowers are the two most prominent CC workflow systems, for context when evaluating CC tools/patterns.
- D9 doesn't affect cc-design — D9 is about Skill builds, not CC environment design.

**Required changes:** None mandatory. cc-design v2.0 is current.

**Optional (LOW):** Add a brief note in cc-design's RESEARCH mode reference material acknowledging GSD and Superpowers as the two most prominent CC execution frameworks, for context when researching CC patterns. This is informational scaffolding, not a methodology change.

### 6. rootnode-handoff-trigger-check (v1.0.1)

**Evaluation question:** Any impact?

**Assessment:** None. Handoff-trigger-check gates CP→CC readiness. The ecosystem analysis validates the handoff pattern (both GSD and Superpowers assume work has already been handed off to CC) but doesn't change the gate's 7 conditions.

**Required changes:** None.

### 7. rootnode-behavioral-tuning (v1.0.1)

**Evaluation question:** Does the persuasion-as-compliance research finding affect behavioral-tuning's countermeasure output?

**Assessment:**
- Behavioral-tuning is the Skill that diagnoses behavioral tendencies and produces countermeasure recommendations. It is the only Skill that generates countermeasure *language* as its deliverable.
- The upstream KF change (persuasion-compliance note in OPTIMIZATION_REFERENCE) documents that imperative framing (authority + commitment principles) measurably outperforms suggestive framing for LLM behavioral compliance — Meincke et al. (2025, N=28,000) found persuasion techniques more than doubled compliance rates (33% → 72%, p < .001).
- Behavioral-tuning's countermeasure templates already use imperative framing implicitly ("If the premise contains errors, say so directly"). The research note makes the mechanism explicit. The question is whether behavioral-tuning's reference material should carry guidance on *language calibration* for countermeasures it recommends — specifically, when to use strong imperative language (discipline-enforcing tendencies: #1, #5, #7b, #10) vs. calibrated language (tendencies where overcorrection is the risk: #3 verbosity, #6 over-exploration).
- Other Skills that touch countermeasures (prompt-validation scores whether they exist; prompt-compilation assembles them) do not produce countermeasure language — they consume templates already formulated. Only behavioral-tuning authors new countermeasure text tailored to the diagnosed tendency.

**Required changes:**
- Add a brief note (3-5 sentences) to behavioral-tuning's reference material on countermeasure language calibration. The note should cover: (1) research grounding — cite Meincke et al. 2025 finding; (2) the calibration principle — imperative framing for discipline-enforcing countermeasures, calibrated framing for overcorrection-risk countermeasures; (3) cross-reference to the persuasion-compliance note in `root_OPTIMIZATION_REFERENCE.md` for the full reasoning.
- This is a reference-material addition, not a SKILL.md body change. The Skill's methodology (diagnose tendency → select countermeasure → customize to domain) is unchanged. What changes is the *language design guidance* available when the Skill produces its output.
- Check description field char budget before considering any description update. The persuasion research is discoverable via the reference material once the Skill is loaded — it does not need to be in the description trigger language.

**Verification:** After update, produce a test countermeasure for tendency #5 (fabricated precision) and verify the output uses imperative framing ("Run the verification command. Read the output. THEN claim the result.") rather than suggestive framing ("Consider running verification before making claims.").

---

## D9 Retroactive Assessment — Existing 21 Skills

The D9 dimension is RECOMMENDED, so existing Skills don't need to be rebuilt. However, for planning purposes, here is the retroactive assessment:

| Skill | D9 Status | Rationale |
|-------|-----------|-----------|
| skill-builder | PASS (credible) | Built via TDD-inspired methodology; v1→v2 evolution validated against real build sessions |
| cc-design | PASS (credible) | Designed against observed CC deployment friction; 5 modes validated in production |
| critic-gate | PASS (credible) | 4-check protocol designed against observed autonomous engine evolution failures |
| mode-router | PASS (credible) | Routing logic designed against observed profile selection failures |
| repo-hygiene | PASS (tested) | Production-validated against CC deployment sweep (23 findings, 14 categories) |
| handoff-trigger-check | PASS (credible) | 7 conditions designed against observed premature handoff failures |
| prompt-compilation | PASS (credible) | 4-stage pipeline validated across 14+ worked examples |
| prompt-validation | PASS (credible) | 6-dimension scorecard validated against real prompt reviews |
| project-audit | PASS (credible) | 6-dimension scorecard + 7 anti-patterns validated across 8+ project audits |
| behavioral-tuning | PASS (credible) | 10-tendency taxonomy designed against observed Claude behavioral failures |
| anti-pattern-detection | PASS (credible) | 7 patterns designed against observed project structure failures |
| memory-optimization | PASS (credible) | Designed against observed Memory misuse (cross-project audit finding) |
| context-budget | PASS (credible) | Two-pool architecture validated in Calibration Lab |
| global-audit | PASS (credible) | 6-dimension scorecard for global layers; designed against observed cross-project drift |
| full-stack-audit | PASS (credible) | Composite of project-audit + global-audit; inherits both validations |
| block-selection | PASS (credible) | Decision tree validated across block library usage |
| profile-builder | SKIP | Schema-driven configuration tool; no behavioral compliance surface |
| session-handoff | SKIP | Structured document generation; no behavioral compliance surface |
| project-brief | SKIP | Structured document generation; no behavioral compliance surface |
| drayline-ecosystem | SKIP | Context carrier; no behavioral compliance surface |
| Block/domain libraries (8) | SKIP | Reference material; no behavioral compliance surface |

**Summary:** 16 PASS (credible), 5 SKIP. Zero FAIL. No Skills require retroactive D9 remediation. The existing Skills were all designed against observed failure modes — they were pressure-tested implicitly even though D9 didn't exist as a formal dimension.

---

## Execution Prompt for Claude Code

```
Read the CC Ecosystem Analysis Skills Impact Evaluation Brief. For each
Skill listed under evaluation:

1. Read the Skill's SKILL.md and relevant reference files.
2. Compare against the assessment in the brief.
3. If "Required changes" lists specific updates, apply them.
4. If "None," confirm no change needed and move to the next Skill.

Priority order: skill-builder first (it carries the quality gate that
references D9), then repo-hygiene (MCP detection sharpening), then
behavioral-tuning (persuasion-compliance language calibration note),
then confirm no-change for the remaining four.

After all evaluations, produce a summary of changes made and Skills
confirmed current.
```

---

## Files Referenced

- `root_CC_ECOSYSTEM_ANALYSIS.md` — full analysis report (combined GSD + Superpowers + root.node)
- `root_SKILL_BUILD_DISCIPLINE.md` — updated with D9 (upstream, in seed project KFs)
- `root_OPTIMIZATION_REFERENCE.md` — updated with persuasion note (upstream)
- `root_AGENT_ANTI_PATTERNS.md` — updated with MCP expansion (upstream)
- `root_CC_ENVIRONMENT_GUIDE.md` — updated with MCP cross-ref (upstream)
