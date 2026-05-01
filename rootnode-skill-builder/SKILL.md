---
name: rootnode-skill-builder
description: >-
  Builds deployment-ready Skill files (SKILL.md + references/) from design
  specifications. Use for building, packaging, converting, or reviewing Skills.
  Trigger on: "build this Skill," "build from this design spec," "convert this
  to a Skill," "package as a Skill," "review this Skill," "check spec
  compliance," "revise this Skill," "is my description under 1024 chars," "my
  SKILL.md is too long." Also trigger on symptom-phrased requests: "my Skill
  doesn't activate," "my Skill folder structure is wrong," "my description
  truncates in Claude Code." Also use when a design spec is in context and the
  user says "proceed with the build." Do NOT use when the user is designing
  Skill methodology itself (the content a Skill teaches, not its packaging) —
  that's design work. Do NOT use for prompt compilation, project auditing, or
  prompt scoring (use rootnode-prompt-compilation, rootnode-project-audit, or
  rootnode-prompt-validation respectively, if available).
license: Apache-2.0
metadata:
  author: rootnode
  version: "1.0"
  original-source: "Skills project CI + SKILLS_SPEC_REFERENCE.md + CONVERSION_REFERENCE.md"
---

# Skill Builder

> **Calibration:** Tier 2, Opus-primary. See repository README for model compatibility.

Build, review, and revise root.node Skills in the SKILL.md format for Anthropic's Claude Skills ecosystem. This Skill carries the complete build methodology — Agent Skills spec, conversion rules, progressive disclosure patterns, and quality gate.

Skills are built from design specifications produced during methodology design work. The design spec is the input — it contains the methodology, architectural decisions, description field draft, internal language adaptation notes, composition testing cases, and reference file structure. This Skill's job is construction, testing, and publication-readiness.

**Platform terminology note:** This Skill retains root.node terminology (Block, Block Library, Domain Pack, Compiler, Optimizer) by design. Unlike most rootnode Skills which strip internal language, this Skill operates ON root.node Skills as its subject matter — the conversion rules, concept mapping, and build pipeline all reference root.node concepts by name because those are the things being built.

## Important

**Description fields are everything.** Claude decides whether to load a Skill based almost entirely on the description field in YAML frontmatter. A Skill with perfect methodology and a vague description will never activate. Test every description: "If Claude sees this alongside 50 other descriptions, will it correctly activate this Skill and ONLY this Skill for the right tasks?"

**Preserve depth, adapt format.** The methodology is the differentiator. Every Skill retains the substantive instructions, reasoning patterns, and quality criteria from the source material. What changes is the packaging — frontmatter, progressive disclosure structure, activation descriptions — not the intellectual content.

**Spec compliance is non-negotiable.** Every Skill conforms to the Agent Skills specification. Name in kebab-case (max 64 chars), description under 1024 chars (always verify parsed YAML length, not raw text), no XML angle brackets in frontmatter, no README.md inside skill folders, SKILL.md body under 500 lines / ~5000 tokens.

**Standalone-first composition.** Every Skill delivers its complete value when installed alone. Cross-Skill references are soft pointers only ("for deeper specialization, see X if available"). Prefer a few hundred tokens of duplicated guidance over a dependency that breaks a Skill when installed alone.

**Complete file output.** Always output the complete file. Never diffs, patches, or partial sections.

---

## Reasoning discipline

Before declaring a Skill ready to ship, walk through the five-dimension quality gate explicitly. State each check, cite the specific evidence (character counts, section structure, activation triggers, cross-Skill references), then apply the pass/fail verdict. Do not compress this sequence into a summary judgment.

If the build scope is unclear (new build vs. review vs. revision, description constraints, reference file structure), confirm scope with the user before proceeding. Do not proceed on inferred assumptions.

---

## Build New Skill

When a design specification is present in context:

**Step 1 — Parse the design spec.** Identify: the methodology (what the Skill does), the reference file structure, the description field draft, the internal language adaptation notes, the composition testing cases, and any architectural decisions already made.

**Step 2 — Build SKILL.md.** Implement the methodology from the design spec. Apply conversion rules (see references/conversion-guide.md): strip root.node internal language per adaptation notes, inline relevant behavioral countermeasures, convert quality gates to actionable verification steps. Structure: identity paragraph, Important/Critical section, core instructions, examples (2-3 input → output), When to Use section, Troubleshooting section. Verify body is under 500 lines. Verify description is under 1024 characters with trigger phrases and negative triggers.

**Step 2a — Description field construction.** The description is the highest-leverage artifact. Build it using the templates in references/conversion-guide.md. Structure: [What it does] + [When to use it] + [Trigger phrases] + [Negative triggers]. Claude has a bias toward undertriggering — make descriptions slightly "pushy" with trigger phrases covering both explicit and implicit user requests. When a Skill risks overtriggering, add explicit negative triggers ("Do NOT use for..."). Always verify the YAML-parsed character count is ≤1024 — measure parsed output, not raw text, because YAML block scalars can differ from source length.

**Step 3 — Build reference files.** Apply progressive disclosure — detailed content, rubrics, pattern libraries, extended examples, and edge cases go here. Each reference file must be referenced from SKILL.md with guidance on when to read it. Add table of contents for files over 300 lines. One level deep (no nested subdirectories within references/).

**Step 4 — Apply internal language adaptation.** Use the adaptation notes from the design spec. Default conversions (see references/conversion-guide.md for full table): "block" → "approach" or "methodology," "the Compiler" → "this Skill" or "the compilation process," "knowledge file" → "reference file" or "documentation." Exception: Skills that operate ON Claude Projects platform features (memory-optimization, context-budget, project-audit) retain platform terminology. If the design spec documents a terminology exception, follow it.

**Step 5 — Run five-dimension publication review.** Score each dimension pass/fail with evidence:

1. **Spec compliance:** Name format, description length (YAML-parsed ≤1024), body length (<500 lines), no XML in frontmatter, no README.md in folder, folder name matches `name` field.
2. **Activation precision:** Would this description trigger on the right tasks? Stay silent on wrong tasks? Compete with 50+ descriptions? Check for undertriggering (Claude's default bias) — descriptions should be slightly "pushy."
3. **Methodology preservation:** Has substantive content been lost? Are instructions still actionable and specific? Compare against design spec methodology sections.
4. **Progressive disclosure:** Is SKILL.md focused on core instructions? Is detailed documentation properly delegated to references/? Is any reference file unreferenced from SKILL.md?
5. **Standalone completeness:** Does the Skill deliver full value installed alone? Any hidden dependencies? All cross-Skill references use "if available" language?

**Step 6 — Present complete files for review.** Output each file in its own code block with filename and purpose. Follow with a build note (3-5 sentences) covering key adaptation decisions. Present the five-dimension review verdict.

### Build Behavioral Calibration

When producing SKILL.md bodies and reference files, match content density to the source methodology. Do not pad with explanatory context or transitional prose the source does not contain.

When building from a design spec, the design decisions are already made. Build what the spec says. If a design decision appears suboptimal, flag it as a build note after delivery — do not pause the build to explore alternatives.

---

## Review Existing Skill

When asked to review a Skill:

1. **Spec compliance:** Check name format, description length (YAML-parsed), body length, no XML in frontmatter, no README.md, folder/name match. See references/skills-spec.md for full constraints.
2. **Activation precision:** Evaluate description against the 50-description competition test. Check for both undertriggering and overtriggering. Check negative triggers against adjacent Skills.
3. **Methodology preservation:** Compare against source material (if available). Check for content loss, vague instructions, or missing quality criteria.
4. **Progressive disclosure:** SKILL.md should contain core instructions only. Detailed docs, extended examples, edge cases belong in references/. Check file references include "when to read" guidance.
5. **Standalone completeness:** Verify no hidden dependencies. Cross-Skill references must use "if available." Test: if this were the only rootnode Skill installed, would it still work?

Flag issues with specific fix recommendations. Do not pad with praise.

---

## Revise Existing Skill

When asked to revise a Skill:

1. Read current SKILL.md and reference files.
2. Apply requested changes while maintaining spec compliance, methodology preservation, and standalone completeness.
3. Output complete updated files (not diffs).
4. Present brief revision note (3-5 sentences) covering what changed and why.

---

## Key Spec Constraints

For the full specification, read references/skills-spec.md.

**YAML frontmatter:** `name` in kebab-case, max 64 chars, must match folder name. `description` max 1024 chars (verify YAML-parsed length), must include what + when + triggers. No XML angle brackets. Optional: `license` (Apache-2.0 for rootnode), `metadata` (author, version, original-source).

**SKILL.md body:** Under 500 lines, under ~5000 tokens. Core instructions only. Imperative form. Include 2-3 examples, When to Use section, Troubleshooting section.

**References:** One level deep. Each file referenced from SKILL.md with "when to read" guidance. TOC for files over 300 lines.

**Progressive disclosure:** Level 1 = frontmatter (always loaded, ~100 words). Level 2 = SKILL.md body (loaded on activation). Level 3 = references/ (loaded on demand).

**Folder structure:**
```
your-skill-name/
├── SKILL.md          # Required — main skill file
├── scripts/          # Optional — executable code
├── references/       # Optional — documentation loaded as needed
└── assets/           # Optional — templates, fonts, icons
```

**Naming rules:** SKILL.md must be exact case. Folder name in kebab-case, no spaces/underscores/capitals. No README.md inside skill folders. Names with "claude" or "anthropic" are reserved.

---

## Conversion Rules Quick Reference

For the full conversion guide including concept mapping, content adaptation patterns, standalone composition rules, and description templates, read references/conversion-guide.md.

### Default Language Adaptations

| Original (root.node) | Adapted (Skills) |
|---|---|
| "Select the Strategic Advisor identity block" | "Use the Strategic Advisor approach" |
| "Consult the Block Library for options" | "See references/identity-blocks.md for available approaches" |
| "The Compiler's Parse stage extracts..." | "Start by extracting from the task description..." |
| "Per the Optimization Notes..." | "Claude tends to..." |
| "The seed project demonstrates..." | [Remove — not relevant outside root.node] |

**Exception:** Skills that operate ON root.node concepts (this Skill) or ON Claude Projects platform features (memory-optimization, context-budget, project-audit) retain their domain-specific terminology. The design spec documents any exceptions.

### Countermeasure Handling

Behavioral countermeasures are inlined where they apply, not referenced as external instructions. Convert XML-tagged countermeasure sections into concrete inline instructions within the relevant workflow step. Exception: the behavioral tuning Skill retains the full countermeasure catalog because its purpose IS behavioral diagnosis.

### Cross-Skill References

All cross-Skill references must be soft pointers: "for deeper specialization, see X if available." The phrase "if available" (or equivalent) must always be present. No Skill may fail, produce incomplete output, or defer a user request because another Skill is not installed.

When the standalone constraint requires inlining shared methodology, inline the narrow slice each Skill needs. A few hundred tokens of duplicated guidance across Skills is acceptable. A Skill that fails when installed alone is not.

---

## Examples

### Example 1: Build from Design Spec

**Input:** User provides a design specification for `rootnode-context-budget` v5 with methodology, description draft, reference file structure, and adaptation notes.

**Actions:**
1. Parse the design spec — identify methodology (context budget analysis pipeline), reference structure (assessment-rubric.md, optimization-patterns.md), description draft, and adaptation notes.
2. Build SKILL.md — implement the pipeline as step-by-step instructions, inline the key spec constraints, add examples and troubleshooting.
3. Build reference files — move detailed rubrics and pattern libraries to references/.
4. Apply language adaptation — retain platform terminology per documented exception.
5. Run five-dimension review — verify spec compliance, activation precision, methodology preservation, progressive disclosure, standalone completeness.
6. Present complete files with build note and review verdict.

**Result:** Three deployment-ready files (SKILL.md + 2 reference files), a 3-5 sentence build note, and a pass/fail verdict on each review dimension.

### Example 2: Review Existing Skill

**Input:** User asks "Review the rootnode-output-blocks Skill for me."

**Actions:**
1. Read the Skill's SKILL.md and all reference files.
2. Check spec compliance: name format ✓, description at 1019/1024 chars (flagged as tight), body under 500 lines ✓.
3. Check activation precision: description includes catalog-specific triggers, negative triggers to validation and block-selection, forward pointer for uncertain users. Evaluate against 50-description competition.
4. Check methodology: verify all 10 output formats preserved in references/, selection guidance intact.
5. Check progressive disclosure: SKILL.md has selection logic, references/ has format specifications.
6. Check standalone: no hard dependencies, soft pointers use "if available."

**Result:** Review findings organized by dimension with specific fix recommendations.

### Example 3: Convert Informal Methodology

**Input:** "I have this methodology document. Convert this to a Skill."

**Actions:**
1. Treat the methodology document as an informal design spec.
2. Extract: what the Skill does, when it activates, what belongs in SKILL.md vs. references/.
3. Draft a description field with trigger phrases and negative triggers.
4. Build the SKILL.md and any reference files following the standard pipeline.
5. Flag any design decisions made during conversion (since no formal spec existed) in the build note.

**Result:** Deployment-ready Skill files with documented assumptions.

---

## Quality Gate

Before finalizing any build or revision:

- Does the description YAML-parse to ≤1024 chars?
- Is the SKILL.md body under 500 lines and ~5000 tokens?
- Does the name field conform (kebab-case, max 64 chars, no reserved words)?
- Has all substantive methodology been preserved from the design spec?
- Are root.node internal references adapted per conversion rules and design spec exceptions?
- Is progressive disclosure working — core instructions in SKILL.md, detailed docs in references/?
- Does the Skill work standalone without requiring other rootnode Skills?
- Are cross-Skill references soft pointers with "if available" language?
- Is metadata.original-source set for traceability?
- Are all output files complete (not diffs)?

---

## When to Use This Skill

Use this Skill when:
- A design specification is present in context and the user wants deployment-ready Skill files
- The user asks to build, convert, or package methodology into SKILL.md format
- The user asks to review an existing Skill for spec compliance, activation precision, or structural quality
- The user asks to revise an existing Skill's structure, description, or reference files
- The user asks about Agent Skills spec constraints (folder structure, YAML requirements, description limits)

Do NOT use this Skill when:
- The user wants to design Skill methodology (what the Skill does, how its pipeline works) — that's normal design work using the project's knowledge base
- The user wants to compile a prompt (use rootnode-prompt-compilation if available)
- The user wants to audit a Claude Project (use rootnode-project-audit if available)
- The user wants to evaluate a prompt's quality (use rootnode-prompt-validation if available)
- The user is working on composition testing or description optimization across the full Skill inventory — that workflow belongs in the Skills project

---

## Troubleshooting

**Skill doesn't trigger:** Description too vague. Check that it includes both what the Skill does AND when to use it. Add specific trigger phrases users would actually say. Claude has an undertriggering bias — make descriptions slightly "pushy."

**Skill triggers on wrong tasks:** Description too broad. Add negative triggers ("Do NOT use for..."). Check for vocabulary overlap with adjacent Skills in the inventory.

**Description over 1024 chars:** Consolidate negative triggers, tighten phrasing, compress trigger phrase lists. Never drop routing-critical content (negative triggers, domain boundary markers). Always re-measure parsed YAML length after edits — not raw text length.

**SKILL.md body too long:** Move detailed documentation to references/. Keep SKILL.md focused on the core workflow and instructions. Check for content that belongs in reference files: full rubrics, extended examples, edge case catalogs, pattern libraries.

**Instructions not followed at runtime:** Check for buried critical instructions (move to top), vague language (replace with specific checks), or excessive verbosity (concise lists beat long paragraphs for procedural instructions).

**Cross-Skill routing collision:** Two Skills activate on the same query. Compare both descriptions and identify the overlapping vocabulary. Add negative triggers to one or both. Use distinct vocabulary domains (e.g., "audit" vs. "optimize," "retrieve" vs. "choose").
