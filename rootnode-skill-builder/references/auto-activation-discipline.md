# Auto-Activation Discipline

**Canonical sources:** `root_CC_ENVIRONMENT_GUIDE.md §1.3` (Skills section, auto-activation discipline subsection); `root_OPTIMIZATION_REFERENCE.md` (tool miscalibration — undertriggering and overtriggering tendencies); `root_CLAUDE_OPTIMIZATION_NOTES.md` (Skill activation patterns under Adaptive deployment).

This reference is a Skill-internal application of those canonicals. It establishes the discipline for writing `description:` fields and configuring invocation behavior so the Skill auto-activates on the right tasks and stays silent on the wrong ones. The Skill applies this discipline during validation dimension 6.

If the canonical sources evolve (description budget changes, new activation patterns documented), regenerate this reference. The cross-reference anchors above are the propagation hooks.

---

## The principle: auto-invocation is the default

A Skill that doesn't auto-activate is a Skill the user has to manually load every time. That defeats the central value proposition: Skills exist so methodology fires automatically when the relevant trigger surfaces in conversation. A Skill the user has to remember to invoke is a paste-and-edit template with extra steps.

Three structural facts make auto-activation the high-leverage focus:

1. **The description field is almost the entire activation surface.** Claude decides whether to load a Skill based on the description in YAML frontmatter, evaluated against the current conversation. The body of SKILL.md is invisible at activation time. A perfect methodology with a vague description never fires.

2. **Claude has an undertriggering bias.** Per `root_OPTIMIZATION_REFERENCE.md` (tool miscalibration), Claude defaults to not invoking tools/Skills unless the trigger signal is strong. "Slightly pushy" descriptions correct for this bias.

3. **Manual-only is an anti-pattern.** Per `root_AGENT_ANTI_PATTERNS.md §4.3`, `disable-model-invocation: true` requires explicit justification. The default is auto-invocation enabled.

---

## Description structure

A strong description has four components, in this order:

1. **What the Skill does** (one sentence, action-oriented). Lead with a verb. "Builds...," "Audits...," "Compiles...," "Generates...," "Detects...," "Optimizes..." Avoid "Helps with...," "Provides...," "Manages..." — passive verbs underspecify the trigger.

2. **When to use it** (one sentence, intent-framed). "Use when [user is doing X / facing Y / wants Z]." This anchors the activation context — Claude matches against the user's current intent, not against abstract topic keywords.

3. **Trigger phrases** (3-8 phrases users would actually say). Mix explicit triggers ("build me a Skill," "audit this prompt") with symptom-phrased triggers ("my Skill doesn't activate," "Claude ignores my instructions"). Symptom-phrased triggers catch users who don't know the Skill exists but describe the problem the Skill solves.

4. **Negative triggers** (when to NOT use). "Do NOT use for [adjacent Skill territory]. Use [other Skill] for that." Negative triggers prevent overtriggering and routing collisions with adjacent Skills. Critical for any Skill that operates in a populated ecosystem.

A description without all four components is incomplete. The fourth is most often missing — Skill builders know what their Skill does but don't think about what it shouldn't do.

---

## Trigger discipline

**Use verbs the user actually says, not technical jargon.** A user says "fix my prompt" or "make this prompt better," not "score the prompt against the validation rubric." A user says "I don't know which approach to use" or "my output feels generic," not "select an identity block." Trigger phrases should match the user's vocabulary, not the Skill's internal terminology.

**Mix explicit and implicit triggers.** Explicit: "build a Skill," "audit my project." Implicit (symptom-phrased): "my Skill won't activate," "Claude keeps making things up." Implicit triggers catch the larger user population — the explicit triggers catch users who already know the Skill's vocabulary.

**Cover both proactive and reactive surfaces.** Proactive: user is starting fresh and wants the Skill's output ("compile a prompt for X"). Reactive: user has output that's broken and wants the Skill to diagnose ("why isn't my prompt working"). Strong descriptions cover both surfaces.

**Negative triggers cite the alternative.** Don't just say "Do NOT use for prompt scoring." Say "Do NOT use for prompt scoring — use rootnode-prompt-validation if available." This routes the user to the right Skill instead of leaving them stranded after the negative trigger fires.

---

## Strong vs. weak examples

### Weak description

```
description: This Skill helps with Claude prompts.
```

Failures: passive verb ("helps with"), no trigger phrases, no negative triggers, no intent context. Won't auto-activate reliably; will overtrigger when it does fire.

### Slightly stronger but still weak

```
description: Use this Skill to work with prompts. Trigger when user
mentions prompts.
```

Failures: vague action verb ("work with"), trigger phrase too broad ("mentions prompts" matches almost any prompt-related conversation), no negative triggers. Will overtrigger heavily.

### Strong description (rootnode-skill-builder v1, the in-house example)

```
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
```

Why this works:

- **What:** "Builds deployment-ready Skill files (SKILL.md + references/) from design specifications." Lead verb, specific output, specific input.
- **When:** "Use for building, packaging, converting, or reviewing Skills." Four intent verbs covering the workflow surface.
- **Explicit triggers:** Nine explicit phrases, mixing happy-path ("build this Skill") with constraint-checking ("is my description under 1024 chars").
- **Symptom triggers:** Three implicit phrases ("my Skill doesn't activate") that catch users describing the problem instead of the solution.
- **Negative triggers:** Two — one carving off methodology design, one routing prompt/project work to the right Skills with "if available" qualifier.
- **Length:** 1003/1024 chars. Tight but compliant.

Failure modes this description avoids:
- Won't auto-activate on generic "prompt help" (no overlap vocabulary with prompt Skills — uses "Skill" specifically).
- Won't activate on Skill *design* conversations (negative trigger explicit).
- Won't activate on Project audits (negative trigger routes elsewhere).

---

## When `disable-model-invocation: true` is genuinely warranted

The directive disables auto-invocation entirely — the Skill ships, but Claude won't load it without explicit user request ("use the X Skill"). This is rare and requires justification.

Legitimate cases:

1. **Destructive operations.** Skill executes irreversible actions (file deletion, repo force-push, data drop). Auto-invocation could destroy work without explicit user consent.

2. **Multi-step workflows where auto-invocation skips a required earlier step.** Skill is the second half of a two-step process — invoking it without the first step produces broken output. Examples: a Skill that consumes a handoff brief from another Skill; a Skill that operates on artifacts produced by a prior Skill.

3. **Domain-isolated Skills that should only fire in specific projects.** A Skill that's installed globally but only relevant in one specific deployment context. Auto-invocation in unrelated projects produces noise.

4. **Workflow Skills with high token cost where the user should consciously opt in.** Skills that consume large context budgets and shouldn't fire opportunistically.

When the directive is set, `metadata.notes` must document the reasoning. The validation gate flags `disable-model-invocation: true` without notes as a warning.

When NOT to use the directive:
- "I don't want it to fire on the wrong tasks" → fix the description (negative triggers), don't disable invocation entirely.
- "The Skill is sensitive and I want to control when it fires" → manual-only is the wrong knob; the right knob is permissions/settings or a hook gate.
- "I'm not sure when it should fire" → the Skill isn't ready to ship. Auto-activation discipline requires knowing when the Skill should fire; if you don't know, the description hasn't been thought through.

---

## The 50-description competition test

Apply this test to every description before shipping:

> Imagine Claude has 50 Skill descriptions in scope. The user types a request. Will Claude correctly select THIS Skill — and only this Skill — for the right tasks? Will Claude correctly NOT select this Skill for adjacent tasks?

If the description doesn't pass this test, the failure mode is one of:

- **Description too generic** (overtriggering). Claude selects the Skill for any vaguely related conversation. Fix: add specificity to the "what" and add negative triggers.
- **Description too narrow** (undertriggering). Claude doesn't recognize the trigger surface. Fix: add symptom-phrased triggers; add implicit triggers users would actually say.
- **Description vocabulary collides with adjacent Skill** (routing collision). Claude can't disambiguate. Fix: distinguish vocabulary domains (e.g., "audit" vs. "optimize," "select" vs. "build"); add negative triggers citing the alternative.

The test isn't optional. Run it explicitly before shipping. State the outcome in the build summary.

---

## Length discipline

The description budget is 1024 YAML-parsed characters. Verify parsed length, not raw text length — YAML block scalars (`>-`, `|`, `|-`) handle whitespace differently from raw text.

When a description is over budget, **never drop routing-critical content** (negative triggers, domain boundary markers). Tighten phrasing instead:

- Compress trigger phrase lists (combine adjacent triggers under shared verbs).
- Tighten the "what" sentence (cut adjectives; lead with the action).
- Compress negative trigger structure (use "Do NOT use for X, Y, or Z" instead of separate sentences).

The description is the highest-leverage artifact in the entire Skill. It's worth multiple tightening passes.

---

## What this reference does not do

This reference doesn't teach the YAML spec — that's `references/skills-spec.md`. It applies the spec to description-writing decisions.

This reference doesn't replace the AP catalog scan for Pattern 5 (Manual-only Skills). The AP scan flags `disable-model-invocation: true` without `metadata.notes`. This reference establishes when notes are warranted in the first place.

This reference doesn't cover Skill ecosystem composition (how this Skill sits next to other rootnode Skills) — that's `ecosystem-placement-decision.md`. Routing discipline (negative triggers) is in scope here; ecosystem placement is in scope there.
