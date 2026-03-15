# Claude 4.6 Calibration Notes

What changed between earlier Claude models and Claude 4.6, and how those changes affect countermeasure selection and system prompt design. Consult this when migrating a pre-4.6 prompt or when deciding whether a specific countermeasure should be applied by default.

---

## What Changed in Claude 4.6

Claude 4.6 models (Opus 4.6, Sonnet 4.6, Haiku 4.5) differ from earlier Claude models in five ways that directly affect behavioral tuning:

### 1. More Precise Instruction Following

Claude 4.6 follows system prompt instructions more precisely than earlier models. This is the single most important change for behavioral tuning. It has two consequences:

- **Instructions that needed emphasis before no longer do.** Emphatic language (MUST, ALWAYS, CRITICAL, NEVER) that was necessary to ensure compliance in earlier models now causes over-compliance. Claude follows the letter of the instruction too aggressively rather than applying judgment.
- **Every instruction counts more.** Noisy "just in case" instructions that were harmlessly ignored by earlier models are now followed precisely. This means unnecessary countermeasures actively degrade output quality rather than being neutral.

### 2. Naturally More Concise

Claude 4.6 produces more direct, grounded responses. It uses a more conversational register and may skip detailed summaries for efficiency. This makes preemptive anti-verbosity countermeasures counterproductive for most tasks.

### 3. More Aggressive Tool Use

Claude 4.6 is more proactive about using available tools. Combined with the more precise instruction following, system prompts with emphatic tool-use language from earlier models now cause tool overtriggering — Claude uses tools on every request, even when the task could be answered from existing context.

### 4. More Upfront Exploration

Opus 4.6 in particular does significantly more upfront exploration than earlier models, especially at higher effort settings. It may gather extensive context, pursue multiple research threads, or read many files before acting. This often improves results on complex tasks but wastes tokens on focused tasks.

### 5. LaTeX as Default Math Format

Opus 4.6 defaults to LaTeX notation for mathematical expressions. Earlier models used a mix of plain text and LaTeX depending on context. This is appropriate for academic and technical outputs but problematic elsewhere.

---

## Countermeasure Classification: Default-On vs. Conditional

Not all countermeasures should be applied to every project. The table below classifies each by whether it should be included by default for affected domains or only when the specific behavior is observed.

| Tendency | Classification | Rationale |
|---|---|---|
| Agreeableness Bias | **Default-on** for advisory/strategy/evaluation | Most persistent tendency. Subtle enough that users may not notice it without testing. Cost of not catching it (flawed advice) is high. |
| Hedging | **Default-on** for research/financial/health | Still significant in 4.6. Cost of unchecked hedging (unclear recommendations) is high in affected domains. |
| Verbosity Drift | **Conditional** — apply only when observed | Claude 4.6 is naturally more concise. Preemptive application risks over-correction (terse, incomplete output). |
| List Overuse | **Default-on** for all domains | Persistent tendency, unchanged in 4.6. Low cost of application even if not triggered. |
| Fabricated Precision | **Default-on** for quantitative domains | Dangerous tendency with high cost of failure. Better to have the guardrail even if rarely triggered. |
| Over-Exploration | **Conditional** — apply for focused-task projects | Exploration often helps on complex tasks. Apply only when users report unnecessary latency or scope creep. |
| Tool Overtriggering | **Conditional** — apply when tool-use language is emphatic | This is a recalibration task. Only needed when the system prompt contains pre-4.6 emphatic tool instructions. |
| LaTeX Defaulting | **Conditional** — apply when output is plain text | Unnecessary for academic/technical projects. Apply only when the output context does not render LaTeX. |

---

## Recalibration Checklist for Pre-4.6 Prompts

When a user has a system prompt written for an earlier Claude model, run this checklist to identify instructions that need recalibration for Claude 4.6.

### 1. Audit Emphatic Language

Search the system prompt for these patterns and replace with calibrated alternatives:

- `MUST` → Remove or replace with normal-weight directive
- `ALWAYS` → Replace with conditional ("when [condition]")
- `CRITICAL` → Remove the prefix; state the instruction normally
- `NEVER` → Replace with "Avoid" or conditional prohibition
- `If in doubt, always...` → Remove; Claude 4.6 has good default judgment
- `You are REQUIRED to...` → State as a normal instruction

**Example migration:**

Before:
```
CRITICAL: You MUST ALWAYS check the database before answering ANY customer question. NEVER rely on your own knowledge for customer-specific data.
```

After:
```
Check the database when the user asks about specific customer records or current account status. For general process questions, answer from your instructions directly.
```

### 2. Audit Verbosity Countermeasures

If the prompt contains anti-verbosity instructions, evaluate whether they are still needed:

- **Remove** preemptive verbosity limits if the project handles a mix of simple and complex tasks (Claude 4.6's natural calibration is usually appropriate).
- **Keep** verbosity limits if the project specifically produces long-form content where Claude demonstrably over-generates (test before deciding).
- **Consider adding** the reverse countermeasure if Claude is being too terse after tool use or in analytical contexts.

### 3. Audit Tool-Use Instructions

If the prompt contains tool-use guidance:

- Replace emphatic triggers with conditional language (see the before/after examples in `countermeasure-templates.md`, Section 7).
- Remove "always search first" and "never answer without [tool]" patterns.
- Add clear conditions for when each tool should and should not be used.

### 4. Check for Prefill Dependencies

Starting with Claude 4.6, prefilled assistant responses on the last turn are no longer supported. If the prompt relied on prefill for:

- **Format control** (e.g., starting with a JSON bracket) → Migrate to explicit format instructions in the prompt.
- **Preamble elimination** (e.g., prefilling "Here is the analysis:") → Add an instruction like "Begin your response with the analysis directly, without preamble."
- **Continuation** → Restructure as a new instruction referencing the previous output.

### 5. Evaluate Instruction Density

Claude 4.6's precise instruction following means every instruction has weight. Audit for:

- **Redundant instructions** that say the same thing in different ways → Consolidate to a single clear statement.
- **"Just in case" instructions** for rare edge cases → Remove or move to a reference file that Claude consults only when the edge case arises.
- **Contradictory instructions** (e.g., "be concise" in one section, "be thorough" in another) → Reconcile into a single, bounded instruction.

The target: a system prompt where every instruction earns its place and no instruction contradicts another. Claude 4.6 will follow all of them, including the noisy ones, so noise reduction matters more than in earlier models.

---

## Model-Specific Notes

### Opus 4.6

- Most affected by over-exploration and LaTeX defaulting.
- Default effort level is "high," which increases upfront exploration. If latency is a concern on focused tasks, either apply the over-exploration countermeasure or use a lower effort setting.
- Highest instruction-following fidelity — instruction quality matters most here.

### Sonnet 4.6

- More balanced between exploration and efficiency.
- For cost-sensitive applications, switching from adaptive thinking to extended thinking with a `budget_tokens` cap provides a hard ceiling on thinking costs.
- Less prone to LaTeX defaulting than Opus.

### Haiku 4.5

- Least affected by over-exploration (simpler reasoning by default).
- Instruction density matters most here — Haiku has less capacity to resolve conflicting or noisy instructions gracefully. Keep prompts clean and focused.
- Verbosity is less of a concern; terseness is more likely.
