---
name: rootnode-skill-builder
description: >-
  Builds, validates, and packages deployment-ready Skill files (SKILL.md +
  references/) from design specifications. Three pre-build gates (decomposition,
  warrant, ecosystem fit) plus an 8-dimension quality gate. Use for building,
  packaging, converting, reviewing, or revising Skills. Trigger on: "build this
  Skill," "build from this design spec," "convert this to a Skill," "package as
  a Skill," "review this Skill," "check spec compliance," "revise this Skill,"
  "is this actually a Skill," "does this belong in a hook instead," "should I
  build a paste-and-edit template first." Also trigger on symptom-phrased
  requests: "my Skill doesn't activate," "my SKILL.md is too long," "my
  description truncates." Do NOT use when the user is designing Skill
  methodology itself — that's design work, not packaging. Do NOT use for prompt
  compilation, project auditing, or prompt scoring (use
  rootnode-prompt-compilation, rootnode-project-audit, or
  rootnode-prompt-validation if available).
license: Apache-2.0
metadata:
  author: rootnode
  version: "2.0"
  predecessor: "rootnode-skill-builder v1.0"
  original-source: "root.node seed Project KFs (post-Phase 27/28 methodology absorption) + rootnode-skills repo v1 source files"
---

# Skill Builder

> **Calibration:** Tier 2, Opus-primary. See repository README for model compatibility.

> **Version 2.0:** Adds three pre-build gates (decomposition, warrant, ecosystem fit) before any build work begins. Expands the publication review from 5 to 8 dimensions (auto-activation enforcement, anti-pattern catalog scan, 7-layer leak-check). Adds three new build artifacts (placement note, promotion provenance, AP-warning summary). v1-built Skills continue to work unmodified; this Skill can review them advisorially against the new dimensions.

Build, review, and revise root.node Skills in the SKILL.md format for Anthropic's Claude Skills ecosystem. This Skill carries the complete build methodology — Agent Skills spec, conversion rules, progressive disclosure patterns, pre-build gates, and the 8-dimension quality gate.

Skills are built from design specifications produced during methodology design work. The design spec is the input — it contains the methodology, architectural decisions, description field draft, internal language adaptation notes, composition testing cases, and reference file structure. This Skill's job is gate-checking, construction, validation, and publication-readiness.

**Platform terminology note:** This Skill retains root.node terminology (Block, Block Library, Domain Pack, Compiler, Optimizer) by design. Unlike most rootnode Skills which strip internal language, this Skill operates ON root.node Skills as its subject matter — the conversion rules, concept mapping, and build pipeline all reference root.node concepts by name because those are the things being built.

## Important

**Description fields are everything.** Claude decides whether to load a Skill based almost entirely on the description field in YAML frontmatter. A Skill with perfect methodology and a vague description will never activate. Test every description: "If Claude sees this alongside 50 other descriptions, will it correctly activate this Skill and ONLY this Skill for the right tasks?"

**Preserve depth, adapt format.** The methodology is the differentiator. Every Skill retains the substantive instructions, reasoning patterns, and quality criteria from the source material. What changes is the packaging — frontmatter, progressive disclosure structure, activation descriptions — not the intellectual content.

**Spec compliance is non-negotiable.** Every Skill conforms to the Agent Skills specification. Name in kebab-case (max 64 chars), description under 1024 chars (always verify parsed YAML length, not raw text), no XML angle brackets in frontmatter, no README.md inside skill folders, SKILL.md body under 500 lines / ~5000 tokens.

**Standalone-first composition.** Every Skill delivers its complete value when installed alone. Cross-Skill references are soft pointers only ("for deeper specialization, see X if available"). Prefer a few hundred tokens of duplicated guidance over a dependency that breaks a Skill when installed alone.

**Pre-build gates run first.** Before parsing any design spec, walk the three pre-build gates explicitly. A Skill that should have been a hook, a template, or an extension of an existing Skill is worse than no Skill at all — it ships, looks reasonable, and silently fails to deliver value. Gates prevent that.

**The deliverable is a packaged zip plus separated audit artifacts.** Never deliver Skill files individually for the user to assemble. Build the deployable as `{skill-name}.zip` containing `{skill-name}/SKILL.md` + `{skill-name}/references/*.md` — drop-in ready for the user's local install path or the rootnode-skills repo. Audit artifacts (placement note, promotion provenance, AP-warning summary) ship as separate files OUTSIDE the zip — they document the build event, not runtime behavior, and don't belong inside the deployable folder. Assembly is the Skill's job, not the user's.

**Complete file output.** Always output the complete file. Never diffs, patches, or partial sections.

---

## Reasoning discipline

Before declaring a Skill ready to ship, walk through the eight-dimension quality gate explicitly. State each check, cite the specific evidence (character counts, section structure, activation triggers, cross-Skill references, AP catches, layer leaks), then apply the pass/fail verdict. Do not compress this sequence into a summary judgment.

If the build scope is unclear (new build vs. review vs. revision, description constraints, reference file structure), confirm scope with the user before proceeding. Do not proceed on inferred assumptions.

---

## Pre-Build Gates

Before parsing any design spec or building any Skill files, walk three gates explicitly. Each gate has a specific decision and a specific halt condition. Pass all three before proceeding to "Build New Skill."

### Gate 1 — Decomposition check

Where does this work fit in the 7-layer Claude Code mechanism framework? The mechanisms are: CLAUDE.md (always-loaded standing context), `.claude/rules/` (path-scoped on-demand rules), Skills (.claude/skills/ — multi-step procedures), subagents (focused specialists with isolated context), hooks (lifecycle guarantees), MCP (external data/APIs), settings (trust/permission boundaries).

For full framework guidance, read references/decomposition-framework.md.

If the work fits "Skills" cleanly: proceed to Gate 2.

If the work fits a different mechanism: redirect the user with brief explanation. Do NOT build a Skill that should have been a hook, a rule, CLAUDE.md content, etc. Misplaced content is the dominant failure mode in CC deployments.

### Gate 2 — Warrant check

Has the work pattern surfaced 3+ times in real use, with evidence?

If yes (3+ occurrences with traceable evidence): proceed to Gate 3.

If no (1-2 occurrences, speculative future need, "I think we'll need this"): recommend building a paste-and-edit template first. Use the user's project prefix convention (project files use `{code}_` prefix per User Preferences). Document explicit promotion criteria inline (when does this template earn promotion to a Skill?). Skill build is premature.

For full warrant guidance, read references/warrant-check-criteria.md.

**Exception:** when the user provides a process-abstraction handoff brief from rootnode-repo-hygiene (or another upstream Skill following the same format), the brief is the warrant evidence. Gate 2 passes automatically; proceed to Gate 3.

### Gate 3 — Ecosystem fit check

Where does this Skill belong in the rootnode runtime tooling map? Check:

1. CP-side (runs in chat-side Projects) or CC-side (deploys to delivery project repositories)?
2. Composes with which existing rootnode Skills (handoff-trigger-check, profile-builder, skill-builder, rootnode-cc-design, prompt-validation, project-audit, critic-gate, mode-router, repo-hygiene)?
3. Fills a clear gap, or duplicates existing capability?

If clear gap: proceed to "Build New Skill." Surface the placement decision and suggested entry for the runtime tooling catalog (`root_AGENT_ENVIRONMENT_ARCHITECTURE.md §6`) in the build summary so the user can update the canonical KF.

If duplication detected: surface to user. Ask whether to extend the existing Skill instead. Building a duplicate Skill creates routing collisions.

For full ecosystem guidance, read references/ecosystem-placement-decision.md.

---

## Build New Skill

When the three pre-build gates have passed and a design specification is present in context:

**Step 1 — Parse the design spec.** Identify: the methodology (what the Skill does), the reference file structure, the description field draft, the internal language adaptation notes, the composition testing cases, and any architectural decisions already made.

**Step 2 — Build SKILL.md.** Implement the methodology from the design spec. Apply conversion rules (see references/conversion-guide.md): strip root.node internal language per adaptation notes, inline relevant behavioral countermeasures, convert quality gates to actionable verification steps. Structure: identity paragraph, Important/Critical section, core instructions, examples (2-3 input → output), When to Use section, Troubleshooting section. Verify body is under 500 lines. Verify description is under 1024 characters with trigger phrases and negative triggers.

**Step 2a — Description field construction.** The description is the highest-leverage artifact. Build it using the templates in references/conversion-guide.md and the discipline in references/auto-activation-discipline.md. Structure: [What it does] + [When to use it] + [Trigger phrases] + [Negative triggers]. Claude has a bias toward undertriggering — make descriptions slightly "pushy" with trigger phrases covering both explicit and implicit user requests. When a Skill risks overtriggering, add explicit negative triggers ("Do NOT use for..."). Always verify the YAML-parsed character count is ≤1024 — measure parsed output, not raw text, because YAML block scalars can differ from source length.

**Step 3 — Build reference files.** Apply progressive disclosure — detailed content, rubrics, pattern libraries, extended examples, and edge cases go here. Each reference file must be referenced from SKILL.md with guidance on when to read it. Add table of contents for files over 300 lines. One level deep (no nested subdirectories within references/).

**Step 4 — Apply internal language adaptation.** Use the adaptation notes from the design spec. Default conversions (see references/conversion-guide.md for full table): "block" → "approach" or "methodology," "the Compiler" → "this Skill" or "the compilation process," "knowledge file" → "reference file" or "documentation." Exception: Skills that operate ON Claude Projects platform features (memory-optimization, context-budget, project-audit) retain platform terminology. If the design spec documents a terminology exception, follow it.

**Step 5 — Run eight-dimension publication review.** Score each dimension pass/fail with evidence:

1. **Spec compliance:** Name format, description length (YAML-parsed ≤1024), body length (<500 lines), no XML in frontmatter, no README.md in folder, folder name matches `name` field.
2. **Activation precision:** Would this description trigger on the right tasks? Stay silent on wrong tasks? Compete with 50+ descriptions? Check for undertriggering (Claude's default bias) — descriptions should be slightly "pushy."
3. **Methodology preservation:** Has substantive content been lost? Are instructions still actionable and specific? Compare against design spec methodology sections.
4. **Progressive disclosure:** Is SKILL.md focused on core instructions? Is detailed documentation properly delegated to references/? Is any reference file unreferenced from SKILL.md?
5. **Standalone completeness:** Does the Skill deliver full value installed alone? Any hidden dependencies? All cross-Skill references use "if available" language?
6. **Auto-activation enforcement:** Description includes verb-based triggering-context language (not just static descriptors). Auto-invocation defaults to on. If `disable-model-invocation: true` is set, explicit reasoning is captured in `metadata.notes`. Per the auto-activation discipline in `root_CC_ENVIRONMENT_GUIDE.md §1.3` and the Manual-only Skills anti-pattern (`root_AGENT_ANTI_PATTERNS.md §4.3`): manual-only Skills are an anti-pattern unless the Skill genuinely should be human-only. For full discipline, see references/auto-activation-discipline.md.
7. **Anti-pattern catalog scan:** Scan produced SKILL.md and references/ against the Skill-relevant subset of the structural anti-pattern catalog (references/anti-pattern-catalog.md). Each detected pattern surfaces as a warning with a section reference to `root_AGENT_ANTI_PATTERNS.md`. Warnings are advisory, not blockers — patterns are sometimes intentional. User accepts (with reasoning captured) or revises. Common catches: §2.1 Monolithic standing context (bloated SKILL.md), §3.5 Blurred Layers (rules mixed with reference), §4.3 Manual-only Skills (weak description), §4.11 Verification-before-completion absent, §4.14 Stale content.
8. **7-layer leak-check:** Scan produced content for material that should have been placed in another mechanism per the 7-layer framework. Common leaks:
   - File-pattern rules in references/ → candidate for `.claude/rules/`
   - Always-relevant facts → candidate for CLAUDE.md
   - Enforcement guarantees in instructions → candidate for hooks
   - External integration logic → candidate for MCP

   Surface as warnings; user decides whether to extract.

**Step 6 — Package the deployable Skill and deliver alongside separated audit artifacts.** The deliverable is two distinct things: (1) a single zip file containing the deployable Skill folder, ready to drop into the user's local install path or upload to the Skills repo without further assembly; (2) the audit artifacts, delivered as separate files outside the zip. Never require the user to assemble the package themselves — packaging is the Skill's responsibility, not the user's.

**Deployable zip (`{skill-name}.zip`):** Contains exactly the Skill folder structure — `{skill-name}/SKILL.md` plus `{skill-name}/references/*.md`. Root entry inside the zip MUST be the named Skill folder itself (so `unzip` produces `{skill-name}/...`, matching the standard rootnode-skills repo layout). No audit artifacts inside the zip. No README inside the Skill folder (per spec). Verify zip contents before delivery: list the archive, confirm structure, confirm file count matches the build (1 SKILL.md + N references).

**Audit artifacts (delivered as separate files, NOT inside the zip):**

- **Ecosystem placement note** (`{skill-name}_placement.md`) — always produced. Documents CP/CC placement, composition with existing rootnode Skills, and the suggested entry for the runtime tooling catalog in `root_AGENT_ENVIRONMENT_ARCHITECTURE.md §6`. Surfaces as a build-summary recommendation; the user updates the canonical KF in a separate edit. This Skill does not auto-edit canonical KFs — methodology updates remain human-reviewed. Format spec in references/ecosystem-placement-decision.md.
- **Promotion provenance** (`{skill-name}_promotion_evidence.md`) — produced when Gate 2 warrant evidence was provided OR when Gate 2 was overridden with reasoning. Captures the evidence (or the override reasoning) for audit trail. Format spec in references/warrant-check-criteria.md.
- **AP-warning summary** (`{skill-name}_ap_warnings.md`) — produced when validation dimension 7 surfaces warnings. Lists each warning, the user's accept/revise decision, and the reasoning when accepted. Future maintainers can see what was a deliberate choice vs. an oversight.

**Delivery format:** Use the present_files tool (or equivalent file-presentation mechanism in the runtime) to surface the zip first, then the audit artifacts. The zip is the primary deliverable; the audit artifacts are secondary. Follow the file presentation with a build note (3-5 sentences) covering key adaptation decisions and the eight-dimension review verdict. The user should be able to install the Skill from the zip immediately, and file the audit artifacts separately to their build provenance location (typically `Projects/{CODE}/research/` or equivalent).

**Why separation matters:** Audit artifacts are about the build event (placement reasoning, warrant evidence, AP catches). The Skill folder is about runtime behavior (instructions, references). Mixing them inside the zip pollutes the deployable with build-time metadata that the runtime never consumes — and creates confusion when the user installs ("are these audit files part of the Skill?"). Separation keeps each concern clean.

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
6. **Auto-activation enforcement:** Description has verb-based triggers, both explicit and symptom-phrased. `disable-model-invocation: true` (if set) has `metadata.notes` justification. See references/auto-activation-discipline.md.
7. **Anti-pattern catalog scan:** Run the AP catalog scan from references/anti-pattern-catalog.md. Surface catches as advisory warnings.
8. **7-layer leak-check:** Scan for material that belongs in CLAUDE.md, `.claude/rules/`, hooks, or MCP rather than in the Skill.

For v1-built Skills, dimensions 6-8 surface as advisory warnings only — do not break a working v1 Skill automatically. The user decides whether to revise based on the warnings.

Flag issues with specific fix recommendations. Do not pad with praise.

---

## Revise Existing Skill

When asked to revise a Skill:

1. Read current SKILL.md and reference files.
2. Apply requested changes while maintaining spec compliance, methodology preservation, and standalone completeness.
3. Run the eight-dimension review against the revised version.
4. Output complete updated files (not diffs).
5. Present brief revision note (3-5 sentences) covering what changed and why.

---

## Key Spec Constraints

For the full specification, read references/skills-spec.md.

**YAML frontmatter:** `name` in kebab-case, max 64 chars, must match folder name. `description` max 1024 chars (verify YAML-parsed length), must include what + when + triggers. No XML angle brackets. Optional: `license` (Apache-2.0 for rootnode), `metadata` (author, version, predecessor, original-source, notes).

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
1. Walk pre-build gates: Gate 1 (Skill mechanism — yes, multi-step procedure with intent triggers); Gate 2 (warrant — design spec exists, implies recurring need); Gate 3 (ecosystem fit — composes with project-audit; clear gap).
2. Parse the design spec — identify methodology (context budget analysis pipeline), reference structure (assessment-rubric.md, optimization-patterns.md), description draft, and adaptation notes.
3. Build SKILL.md — implement the pipeline as step-by-step instructions, inline the key spec constraints, add examples and troubleshooting.
4. Build reference files — move detailed rubrics and pattern libraries to references/.
5. Apply language adaptation — retain platform terminology per documented exception.
6. Run eight-dimension review — verify all 8 dimensions; surface AP catches and 7-layer leaks as advisory warnings.
7. Present complete files with build note, review verdict, placement note, and AP-warning summary if applicable.

**Result:** A deployable zip (`rootnode-context-budget.zip`) containing the Skill folder structure (SKILL.md + 2 reference files), delivered first. Three audit artifacts delivered separately outside the zip: ecosystem placement note, AP-warning summary if catches occurred, promotion provenance if warrant evidence was provided. A 3-5 sentence build note and an 8-dimension review verdict accompany the delivery. The user installs the zip directly with no manual assembly; files the audit artifacts to their build provenance location.

### Example 2: Review Existing Skill

**Input:** User asks "Review the rootnode-output-blocks Skill for me."

**Actions:**
1. Read the Skill's SKILL.md and all reference files.
2. Check spec compliance: name format ✓, description at 1019/1024 chars (flagged as tight), body under 500 lines ✓.
3. Check activation precision: description includes catalog-specific triggers, negative triggers to validation and block-selection, forward pointer for uncertain users. Evaluate against 50-description competition.
4. Check methodology: verify all 10 output formats preserved in references/, selection guidance intact.
5. Check progressive disclosure: SKILL.md has selection logic, references/ has format specifications.
6. Check standalone: no hard dependencies, soft pointers use "if available."
7. Check auto-activation enforcement: verb-based triggers present; `disable-model-invocation` not set (default on, correct).
8. Run AP catalog scan: no §2.1 Monolithic catches; §3.5 Blurred Layers — warning on lines 80-95 where reference content appears in SKILL.md (advisory).
9. Run 7-layer leak-check: no leaks detected.

**Result:** Review findings organized by dimension with specific fix recommendations. AP-warning summary surfaces the §3.5 catch for user disposition.

### Example 3: Convert Informal Methodology

**Input:** "I have this methodology document. Convert this to a Skill."

**Actions:**
1. Walk pre-build gates: Gate 1 confirm Skill is the right mechanism (not a hook, rule, or CLAUDE.md addition); Gate 2 ask for evidence of recurring use; Gate 3 check ecosystem fit.
2. Treat the methodology document as an informal design spec.
3. Extract: what the Skill does, when it activates, what belongs in SKILL.md vs. references/.
4. Draft a description field with trigger phrases and negative triggers.
5. Build the SKILL.md and any reference files following the standard pipeline.
6. Run the eight-dimension review.
7. Flag any design decisions made during conversion (since no formal spec existed) in the build note.

**Result:** A deployable zip with the Skill folder, delivered first. Audit artifacts (placement note, promotion provenance, AP-warning summary as applicable) delivered separately outside the zip. The 8-dimension review verdict and a build note flag any design decisions made during conversion (since no formal spec existed).

### Example 4: Build with Pre-Build Gates Triggered

**Input:** User says "I want to build a Skill that always runs pytest before declaring a task complete in our Python projects."

**Actions:**
1. Gate 1 (decomposition): This is a lifecycle guarantee — runs on Stop trigger. Belongs in a hook, not a Skill. Redirect: "This work fits the hook mechanism (PreToolUse/Stop hook), not a Skill. Hooks provide enforcement; Skills provide on-demand procedures. The Enforcement-as-preference anti-pattern (`root_AGENT_ANTI_PATTERNS.md §4.4`) describes exactly this failure mode — prompt-level rules that need deterministic enforcement. See references/decomposition-framework.md for the framework. Want help drafting a hook config instead?"
2. Halt — no Skill built.

**Result:** Correct redirect. Skill mechanism mismatched the work shape; the gate caught it before producing a Skill that would silently fail to enforce.

---

## Quality Gate

Before finalizing any build or revision:

- Have the three pre-build gates been walked explicitly (decomposition, warrant, ecosystem fit)?
- Does the description YAML-parse to ≤1024 chars?
- Is the SKILL.md body under 500 lines and ~5000 tokens?
- Does the name field conform (kebab-case, max 64 chars, no reserved words)?
- Has all substantive methodology been preserved from the design spec?
- Are root.node internal references adapted per conversion rules and design spec exceptions?
- Is progressive disclosure working — core instructions in SKILL.md, detailed docs in references/?
- Does the Skill work standalone without requiring other rootnode Skills?
- Are cross-Skill references soft pointers with "if available" language?
- Is metadata.original-source set for traceability? (And `metadata.predecessor` if this is a versioned successor?)
- Are all output files complete (not diffs)?
- Has the auto-activation enforcement check passed?
- Has the anti-pattern catalog scan completed (warnings reviewed and accepted/revised)?
- Has the 7-layer leak-check completed (leaks reviewed and extracted/accepted)?
- Has the deployable zip been assembled with the correct folder structure (`{skill-name}/SKILL.md` + `{skill-name}/references/*.md`) and no audit artifacts inside?
- Have the audit artifacts been produced as separate files outside the zip (placement note always; promotion provenance when warrant evidence/override; AP-warning summary when dim 7 catches)?
- Has zip contents been verified by listing the archive before delivery?

---

## When to Use This Skill

Use this Skill when:
- A design specification is present in context and the user wants deployment-ready Skill files
- The user asks to build, convert, or package methodology into SKILL.md format
- The user asks whether something should be a Skill at all ("is this actually a Skill," "does this belong in a hook instead")
- The user asks whether to build a Skill or a paste-and-edit template first
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

**Skill doesn't trigger:** Description too vague. Check that it includes both what the Skill does AND when to use it. Add specific trigger phrases users would actually say. Claude has an undertriggering bias — make descriptions slightly "pushy." See references/auto-activation-discipline.md for the full discipline.

**Skill triggers on wrong tasks:** Description too broad. Add negative triggers ("Do NOT use for..."). Check for vocabulary overlap with adjacent Skills in the inventory.

**Description over 1024 chars:** Consolidate negative triggers, tighten phrasing, compress trigger phrase lists. Never drop routing-critical content (negative triggers, domain boundary markers). Always re-measure parsed YAML length after edits — not raw text length.

**SKILL.md body too long:** Move detailed documentation to references/. Keep SKILL.md focused on the core workflow and instructions. Check for content that belongs in reference files: full rubrics, extended examples, edge case catalogs, pattern libraries.

**Instructions not followed at runtime:** Check for buried critical instructions (move to top), vague language (replace with specific checks), or excessive verbosity (concise lists beat long paragraphs for procedural instructions).

**Cross-Skill routing collision:** Two Skills activate on the same query. Compare both descriptions and identify the overlapping vocabulary. Add negative triggers to one or both. Use distinct vocabulary domains (e.g., "audit" vs. "optimize," "retrieve" vs. "choose"). See references/ecosystem-placement-decision.md for the duplication detection signals.

**User asks for a Skill that should be a hook / rule / CLAUDE.md content:** Walk Gate 1 (decomposition) explicitly. Use the redirect language in references/decomposition-framework.md. Do not build the Skill — redirect to the correct mechanism with a 2-3 sentence pivot prompt.

**User asks for a Skill but can name only 1-2 occurrences:** Walk Gate 2 (warrant) explicitly. Recommend a paste-and-edit template (`{code}_template_{descriptor}.md`) with promotion criteria. Do not build the Skill prematurely. See references/warrant-check-criteria.md for the template structure.

**Disable-model-invocation flag set without justification:** Validation dimension 6 catches this. Either remove the flag (default to auto-invocation) or add `metadata.notes` documenting the human-only reasoning. Manual-only Skills are an anti-pattern unless the Skill genuinely warrants human-only invocation.
