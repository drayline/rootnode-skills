---
name: rootnode-behavioral-tuning
description: >-
  Diagnoses and fixes Claude behavioral issues in system prompts and Projects using tested countermeasure templates. Covers eight tendencies: agreeableness bias, hedging, verbosity drift, list overuse, fabricated precision, over-exploration, tool overtriggering, and LaTeX defaulting. Use when user says "Claude is too verbose," "Claude keeps hedging," "Claude agrees with everything," "make Claude more direct," "Claude uses too many lists," "Claude keeps searching when it doesn't need to," "tune Claude's behavior," "fix Claude's output," or describes any recurring behavioral problem in Claude's responses. Also use when auditing a system prompt for behavioral calibration issues or recalibrating a pre-4.6 prompt for current models. Do NOT use for evaluating or scoring a prompt's overall quality — use rootnode-prompt-validation for that if available.
license: Apache-2.0
metadata:
  author: rootnode
  version: "1.0"
  original-source: OPTIMIZATION_REFERENCE.md, CLAUDE_OPTIMIZATION_NOTES.md
---

# Behavioral Tuning for Claude

Diagnose and fix recurring behavioral problems in Claude's output by applying targeted countermeasures to system prompts and Project Custom Instructions. This Skill covers the eight known behavioral tendencies in Claude 4.6 models, their detection criteria, and tested countermeasure templates ready to paste into prompts.

## When to Use This Skill

Use this Skill when:

- A user reports a specific behavioral complaint about Claude's output (too verbose, too agreeable, too hedgy, too many lists, makes up numbers, over-explores, uses tools too aggressively, formats math in LaTeX when plain text is needed).
- A user wants to audit a system prompt or Project for behavioral calibration gaps.
- A user is migrating a prompt from an earlier Claude model and needs to recalibrate for Claude 4.6's changed behavioral profile.
- A user asks how to make Claude more direct, more concise, less agreeable, or otherwise adjust a specific behavioral dimension.

## Important: Calibration Context

Claude 4.6 (Opus 4.6, Sonnet 4.6, Haiku 4.5) has a meaningfully different behavioral profile than earlier models. It is naturally more concise, more direct, more action-oriented, and more aggressive about using tools. Three consequences for countermeasure selection:

1. **Some countermeasures are now conditional.** Verbosity countermeasures that were default-on for earlier models should only be applied when verbosity is actually observed in Claude 4.6. Applying them preemptively now risks over-correction (terse, incomplete responses).
2. **New tendencies have emerged.** Over-exploration, tool overtriggering, and LaTeX defaulting are new or significantly changed in 4.6 and require new countermeasure patterns.
3. **Instruction weight has changed.** Claude 4.6 follows instructions more precisely than earlier models. Emphatic language (MUST, ALWAYS, CRITICAL, NEVER) now causes over-compliance rather than ensuring compliance. All countermeasures should use normal-weight, calibrated language.

For detailed model-version calibration notes, see `references/4-6-calibration-notes.md`.

---

## The Eight Behavioral Tendencies

### 1. Agreeableness Bias

**Status:** Persistent across all model generations. Default-on countermeasure recommended.

**Detection criteria:** Claude agrees with the user's framing even when the framing is flawed. Accepts stated premises without examination. Validates the user's preferred approach rather than evaluating it objectively. In advisory contexts, recommends what the user seems to want rather than what the evidence supports.

**Domains most affected:** Advisory and strategy projects, evaluation projects, coaching projects — any context where users state a preferred direction and expect honest assessment.

**Countermeasure (concise):** Instruct Claude to identify and flag flawed premises, errors, or better alternative framings before executing a request. Instruct it to evaluate approaches on their merits, not on whether the user favors them.

**Placement:** Identity block or core rules — must be at a high-attention position to override Claude's default agreeableness. This is the most important countermeasure for advisory contexts.

For the ready-to-paste template, see `references/countermeasure-templates.md`, Section 1.

---

### 2. Hedging and Over-Qualification

**Status:** Persistent, slightly reduced in Claude 4.6. Default-on countermeasure recommended for affected domains.

**Detection criteria:** Every finding is qualified with cascading caveats. Conclusions are softened. Recommendations come wrapped in "it depends," "there are many factors," "this is just one perspective." Well-established best practices are presented as uncertain.

**Domains most affected:** Research and analysis, financial advisory, health-adjacent projects — any domain where Claude perceives liability risk or epistemic uncertainty.

**Countermeasure (concise):** Instruct Claude to state positions directly where evidence is clear. Reserve caveats for genuinely uncertain areas. When caveating, require specificity about what is uncertain and why — no blanket hedging on established facts.

**Placement:** Core rules or output standards. For research-heavy projects, reinforce in the identity block with language framing the role as one that states conclusions clearly and presents limitations in a dedicated section rather than qualifying every sentence.

For the ready-to-paste template, see `references/countermeasure-templates.md`, Section 2.

---

### 3. Verbosity Drift

**Status:** Reduced in Claude 4.6. **Conditional countermeasure — apply only when verbosity is observed, not preemptively.**

**Detection criteria:** Responses grow longer over a conversation. Unrequested sections appear (summaries, follow-up suggestions, background context). Paragraphs expand beyond what the content warrants. Simple questions receive multi-paragraph answers.

**Domains most affected:** Research projects, educational projects, any context where Claude enters "explain" mode. Worsens in longer conversations.

**Critical 4.6 note:** Claude 4.6 is naturally more concise. Preemptive verbosity countermeasures now risk over-correction — producing responses that feel terse or incomplete. Apply only when you observe actual verbosity in outputs. Some tasks may need the *reverse* countermeasure (Claude being too brief after tool use or skipping helpful summaries).

**Countermeasure (concise — when verbosity is observed):** Instruct Claude to respond only with what was requested. No unrequested sections, summaries, or follow-up suggestions unless critical. Match response length to task complexity.

**Reverse countermeasure (when Claude is too terse):** Instruct Claude to provide summaries after tool use and to aim for thoroughness in analysis — include supporting detail and reasoning, not just conclusions.

**Placement:** Output standards (closest to generation, where length decisions are made).

For both templates, see `references/countermeasure-templates.md`, Section 3.

---

### 4. List and Bullet Overuse

**Status:** Persistent across all model generations. Default-on countermeasure recommended.

**Detection criteria:** Claude converts narrative explanations into bullet points. Analytical prose becomes lists of discrete points. Every response defaults to structured formats even when connected prose would be more appropriate and readable.

**Domains most affected:** All domains, but especially problematic in content and communications projects (where prose quality matters), advisory projects (where nuanced argument matters), and research projects (where synthesis requires connected reasoning, not fragmented points).

**Countermeasure (concise):** Instruct Claude to write in connected prose paragraphs. Lists are appropriate only for genuinely discrete, parallel items. Narrative explanations, analytical reasoning, and recommendations should not be converted into bullet points.

**Placement:** Output standards. For content-focused projects, reinforce in the identity block.

For the ready-to-paste template, see `references/countermeasure-templates.md`, Section 4.

---

### 5. Fabricated Precision

**Status:** Persistent across all model generations. Default-on countermeasure recommended for affected domains.

**Detection criteria:** Claude generates specific statistics, percentages, or quantitative claims not grounded in provided data. Outputs contain authoritative-sounding numbers that were confabulated. Particularly dangerous because the output looks credible — a reader without independent knowledge may not question a specific-seeming figure.

**Domains most affected:** Research and analysis, financial analysis, health and medical — any domain where specific numbers carry weight and inform decisions.

**Countermeasure (concise):** Instruct Claude to use only data explicitly provided. If a specific number is unavailable, state what data would be needed instead of estimating. Never invent statistics or quantitative claims to fill information gaps. For research-heavy projects, add a secondary verification check in output standards: "Verify that every quantitative claim is sourced from provided data."

**Placement:** Core rules (this is typically a non-negotiable constraint). Secondary check in output standards for research-heavy projects.

For the ready-to-paste template, see `references/countermeasure-templates.md`, Section 5.

---

### 6. Over-Exploration and Overthinking

**Status:** New in Claude 4.6. Conditional countermeasure — apply for focused tasks, not for complex research.

**Detection criteria:** Claude pursues too many lines of investigation before producing output. Reads many files, runs multiple searches, explores tangential angles, or adds features and improvements beyond what was asked. Causes unnecessary latency and token consumption on focused tasks. Particularly pronounced at higher effort settings.

**Domains most affected:** Agentic projects, research projects, software engineering projects (where Claude may refactor beyond the request) — any project where Claude has access to tools and files.

**When NOT to apply:** On genuinely complex tasks where broad exploration improves results. This countermeasure targets unnecessary exploration on focused tasks, not all exploration.

**Countermeasure (concise):** Instruct Claude to make only changes that are directly requested or clearly necessary. Keep solutions simple and focused. Do not add features, refactor code, or make improvements beyond what was asked. For reasoning-level control, instruct Claude to choose an approach and commit rather than weighing multiple options indefinitely.

**Placement:** Core rules or output standards. For projects with tool access, add specific guidance: "Use [tool] when it would enhance your understanding — not as a default action on every request."

For the ready-to-paste template, see `references/countermeasure-templates.md`, Section 6.

---

### 7. Tool Overtriggering

**Status:** New in Claude 4.6. This is a recalibration problem, not a new-countermeasure problem.

**Detection criteria:** Claude uses tools aggressively even when the task could be answered from existing context. Searches for well-known facts. Calls APIs unnecessarily. This is caused by system prompt instructions tuned for earlier models where undertriggering was the problem — emphatic tool-use language now causes the opposite behavior in 4.6's more responsive instruction following.

**Domains most affected:** Any project with tool access. Most problematic in projects whose system prompts were written for earlier Claude models and have not been recalibrated.

**Countermeasure (concise):** This is NOT a template to add — it is existing instructions to revise. Audit the system prompt for emphatic tool-use language (MUST, ALWAYS, CRITICAL, NEVER, "If in doubt, always...") and replace with calibrated conditional guidance. Replace "Default to using [tool]" with "Use [tool] when it would enhance your understanding of the problem." Replace "CRITICAL: You MUST use the search tool for ANY question" with "Use the search tool when the question requires current data that may have changed since your training."

**Placement:** Wherever tool-use instructions currently exist in the system prompt. The fix is recalibration of existing instructions, not addition of a new block.

For before/after examples, see `references/countermeasure-templates.md`, Section 7.

---

### 8. LaTeX Defaulting

**Status:** New in Claude 4.6 (primarily Opus 4.6). Conditional countermeasure — apply only when the output context does not render LaTeX.

**Detection criteria:** Claude defaults to LaTeX notation for mathematical expressions. Outputs contain `\frac{}{}`, `\sum`, `$...$`, and other LaTeX markup. Appropriate for academic and technical contexts, but problematic for plain-text outputs, non-technical audiences, or downstream systems that do not render LaTeX.

**Domains most affected:** Financial projects, educational projects for non-academic audiences, any project involving quantitative analysis where output is plain text or rendered in systems without LaTeX support.

**When NOT to apply:** For academic or technical projects where LaTeX is the expected format, this countermeasure is unnecessary.

**Countermeasure (concise):** Instruct Claude to format all mathematical expressions in plain text using standard characters (/ for division, * for multiplication, ^ for exponents). Explicitly prohibit LaTeX, MathJax, and markup notation.

**Placement:** Output standards.

For the ready-to-paste template, see `references/countermeasure-templates.md`, Section 8.

---

## Domain-Tendency Mapping

Use this table to identify which tendencies are most likely to affect a given project domain. Check the relevant tendencies and verify that appropriate countermeasures are present. Do not add countermeasures for tendencies the domain does not trigger — they are noise.

| Domain | Primary Tendencies | Secondary Tendencies |
|---|---|---|
| Advisory / Strategy | Agreeableness, Hedging | List Overuse, Verbosity |
| Research / Analysis | Hedging, Fabricated Precision | Verbosity, Over-Exploration |
| Financial | Fabricated Precision, Hedging | LaTeX Defaulting |
| Health / Medical | Hedging, Fabricated Precision | Verbosity |
| Content / Communications | List Overuse, Verbosity | Agreeableness |
| Software Engineering | Over-Exploration, Tool Overtriggering | Verbosity |
| Agentic / Tool-Heavy | Tool Overtriggering, Over-Exploration | Verbosity |
| Educational | Verbosity, LaTeX Defaulting | List Overuse, Hedging |
| Coaching / Personal | Agreeableness, Hedging | Verbosity |
| Quantitative / Technical | LaTeX Defaulting, Fabricated Precision | Over-Exploration |

---

## How to Apply Countermeasures

### Step 1: Identify the Problem

Start with the user's complaint. Map it to one or more of the eight tendencies above. If the complaint is vague ("Claude's output isn't great"), use the domain-tendency mapping to generate hypotheses, then ask for a specific output example to confirm.

### Step 2: Check Existing Instructions

Before adding a countermeasure, audit the system prompt for:
- **Conflicting instructions** that may be causing the behavior (e.g., "be thorough" causing verbosity).
- **Emphatic language** from pre-4.6 prompts that may be causing over-compliance (e.g., "ALWAYS search first" causing tool overtriggering).
- **Missing identity clarity** that leaves Claude without a strong behavioral anchor.

Sometimes the fix is removing or softening existing instructions, not adding new ones. This is especially true for tool overtriggering and verbosity in 4.6-era projects.

### Step 3: Select and Place the Countermeasure

Retrieve the appropriate template from `references/countermeasure-templates.md`. Customize the template language to match the project's domain terminology. Place it at the correct attention position:

- **Identity block (highest attention):** Agreeableness bias — must override Claude's deepest default.
- **Core rules (high attention):** Fabricated precision, over-exploration — non-negotiable constraints.
- **Output standards (closest to generation):** Verbosity, list overuse, LaTeX defaulting — format-level controls.
- **Inline with existing tool instructions:** Tool overtriggering — recalibrate, do not add separately.

### Step 4: Verify — Do Not Over-Apply

After applying countermeasures:
- Test with representative inputs to confirm the behavior is corrected.
- Watch for over-correction (e.g., verbosity countermeasure making Claude too terse).
- Do not add countermeasures for tendencies the domain does not trigger. Each unnecessary countermeasure is noise that dilutes the instructions Claude follows most precisely.

---

## Troubleshooting

**Countermeasure applied but behavior persists:** The countermeasure may be placed in a low-attention position. Move it higher — from output standards to core rules, or from core rules to the identity block. Also check for conflicting instructions elsewhere in the prompt that are overriding the countermeasure.

**Countermeasure causes over-correction:** The language may be too aggressive for Claude 4.6. Soften emphatic terms. Replace "Never" with "Avoid unless clearly appropriate." Replace "Only respond with X" with "Default to X; expand when the task warrants it." See `references/4-6-calibration-notes.md` for recalibration guidance.

**Multiple tendencies present simultaneously:** Apply countermeasures for the primary tendency first and test. Often fixing the primary tendency reduces the secondary one. If not, add the secondary countermeasure. Avoid applying more than 3-4 countermeasures at once — instruction density reduces compliance with each one.

**User describes a problem that doesn't match any tendency:** The issue may be structural (missing identity, conflicting instructions, orphan knowledge files) rather than behavioral. For deeper structural analysis, consider a full project audit if the `rootnode-project-audit` Skill is available, or examine the system prompt architecture manually — check for a clear identity block, 3-7 non-negotiable core rules, knowledge file routing, operational modes, and output standards.

---

## Reference Files

- **`references/countermeasure-templates.md`** — Full ready-to-paste countermeasure code blocks for all eight tendencies, including standard and reverse variants. Consult this when the user needs the actual template text to insert into their system prompt.
- **`references/4-6-calibration-notes.md`** — Detailed notes on what changed between earlier Claude models and Claude 4.6, which countermeasures are now conditional vs. default-on, and a recalibration checklist for migrating pre-4.6 prompts. Consult this when the user is upgrading a prompt from an earlier model or when deciding whether a countermeasure should be applied by default.
