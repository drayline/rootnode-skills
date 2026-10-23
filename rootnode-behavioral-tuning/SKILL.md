---
name: rootnode-behavioral-tuning
description: >-
  Diagnoses and fixes Claude behavioral issues in system prompts and
  Projects using tested countermeasure templates. Use when "Claude is too
  verbose," "keeps hedging," "agrees with everything," "claims it did
  something it didn't," "won't use a tool," "Claude stops halfway," "keeps
  double-checking," "spawns subagents for everything," "adds tests I didn't
  ask for," "fix Claude's output," "tune Claude's behavior," "Claude ignores
  my preferences," "adds unsolicited disclaimers," "uses too many lists."
  Covers fifteen tendencies — agreeableness, verbosity, tool miscalibration,
  editorial drift, self-referential fabrication — plus over-verification,
  scope expansion, subagent over-delegation, correction narration, early
  turn termination. Also use when auditing a system prompt for behavioral
  calibration or recalibrating a pre-5.5 prompt, and when users describe
  recurring output problems without naming a tendency. Do NOT use for scoring
  a prompt's overall quality — use rootnode-prompt-validation if available.
license: Apache-2.0
metadata:
  author: rootnode
  version: "5.0.0"
  original-source: "OPTIMIZATION_REFERENCE.md, CLAUDE_OPTIMIZATION_NOTES.md"
---

# Behavioral Tuning for Claude

> **Calibration:** Tier 2 (Sonnet-graceful) — designed against Opus 5.5 + Sonnet 5.5 dual-primary. Runs on Haiku 5.5 at `high` effort with less depth on multi-dimensional analysis; fallback-graceful on Opus 5 / Sonnet 5; legacy-graceful on Sonnet 4.6. Start at the model's default effort (`medium` on Opus 5.5 and Sonnet 5.5 in Claude Code; `high` for Sonnet 5.5 on the Claude API) and re-run an effort sweep on your own evals rather than carrying a setting over. See repository README for model compatibility.

**Version 5.0 — 15-tendency taxonomy, 5.5-generation calibration.**

## Purpose

Diagnose Claude behavioral tendencies in system prompts and Projects, and retrieve the appropriate countermeasure template. Covers fifteen tendencies, each with a symptom, a remediation pattern, and deployment-context conditioning: some countermeasures apply universally, others are calibrated for specific deployment contexts (chat interface, Claude Projects, Claude Code, API).

This Skill does not evaluate a prompt's overall quality — for that, use `rootnode-prompt-validation` if available. This Skill does not redesign a Project's architecture — for that, use `rootnode-project-audit` or `rootnode-full-stack-audit` if available. It focuses specifically on behavioral-layer countermeasure selection and application.

## Reasoning discipline

A defensible countermeasure recommendation shows its work. Observe the symptom in the user's specific language, identify which tendency it most closely matches against the catalog below, then apply the countermeasure template — compressing this into a direct recommendation makes the diagnosis harder to interrogate and easier to mis-route between adjacent tendencies (1a vs. 1b, 9 vs. 10, 12 vs. 15).

If the deployment context is unclear (is this a chat interface prompt? a Project CI? a Claude Code system prompt? an API integration?), confirm with the user before proceeding. Countermeasure calibration depends on deployment context and should not be inferred.

---

## The Fifteen Tendencies

Each tendency below is documented with (a) a short description, (b) its core symptom (the Diagnostic routing table is the full symptom surface), (c) the deployment contexts where it is most pronounced, and (d) a countermeasure that can be inserted into — or, for #11, removed from — a system prompt or Project CI.

Extended countermeasure variants (identity-level embedding, output-standards integration, stronger variants, worked examples) are in `references/countermeasure-templates.md`; section numbers there match the tendency numbers here.

### 1. Agreeableness bias

Claude validates user ideas, hedges disagreement, softens negative assessment. Reduced at the model level in Opus 4.7 but not eliminated.

**Facets:**
- **1a — Output-content agreeableness:** Validating user ideas in responses ("Great question!", "That's a solid approach"). Reduced in 4.7.
- **1b — Persistent-preference dilution:** Configured preferences (User Preferences, Project CI rules) are weighted less heavily against immediate-prompt framing as conversations extend. Emerged in 4.7 chat interface deployment.

**Symptom:** responses open by validating the premise and soften disagreement under follow-up (1a); preferences such as "be direct" hold for the first few turns, then drift (1b).

**Deployment calibration:** Chat interface (Adaptive): HIGH for 1b, MEDIUM for 1a · Claude Projects: MEDIUM for 1b (CI partially mitigates), LOW for 1a · Claude Code (`medium` default on Opus 5.5 / Sonnet 5.5 / Haiku 5.5): LOW for both facets · API (effort ≥ high): LOW for both facets.

**Countermeasure template (for 1a):**
```
If the premise of a request contains errors, flawed assumptions, or a better
alternative framing, say so directly before proceeding. Do not execute a
flawed request without comment. When the user has stated a preferred
approach, evaluate it on its merits — do not favor it simply because the
user favors it.
```

**Countermeasure template (for 1b) — chat interface and Projects:**
```
Treat User Preferences and Project Custom Instructions as equal-priority
constraints to user messages. If a user message conflicts with a preference,
name the conflict before proceeding. Do not silently drop preferences over
a long conversation. At every turn, the full Preference and CI ruleset
applies.
```

**Placement:** 1a in identity block or core rules (high-attention position). 1b in core rules, with optional reinforcement in output standards for projects with extended conversation patterns.

### 2. Hedging

Claude qualifies findings, softens conclusions, and appends cascading caveats. Reduced on factual claims in 4.7; persistent on editorial framings.

**Symptom:** recommendations wrapped in "it depends" or "it's worth considering," and strong positions inverted into both-sides framings beyond what the evidence warrants.

**Deployment calibration:** Chat interface (Adaptive): MEDIUM on editorial framings; LOW on factual claims · Claude Projects: MEDIUM on editorial; LOW on factual · Claude Code (`medium` default on Opus 5.5 / Sonnet 5.5 / Haiku 5.5): LOW · API (effort ≥ high): LOW.

**Countermeasure template (editorial hedging):**
```
State conclusions directly. Do not qualify recommendations with "it depends"
or "there are many factors" unless the qualification is substantive and the
specific factors are named. When evidence supports a clear recommendation,
issue it. Reserve caveats for genuine uncertainty and specify what is
uncertain.
```

**Placement:** Core rules or output standards.

### 3. Verbosity drift — three surfaces

Claude produces longer-than-needed output. Since the v4.0 cycle this is a three-surface family; identify the surface before applying a template, because one countermeasure under-fits the others. (Since 4.7 the reverse problem — terse, incomplete answers on simple prompts — is also common; check which direction the output fails.)
- **3a — Conversational length:** chat responses restate the question, repeat analysis, pad with transitional framing. Effort controls thinking, not visible length — prompt for length.
- **3b — Agentic progress narration:** Claude Code and agent sessions announce each step and run long per message.
- **3c — Written-deliverable length:** files written to disk carry filler sections and redundant summaries. Fable 5.1 adds two token-cost facets: whole-file rewrites for small edits, and drafting a deliverable in thinking then again in the reply at `xhigh`/`max` (prefer `high`).

**Symptom:** simple questions get multi-paragraph answers (3a); every tool call is narrated (3b); a report file is twice the length the content needs (3c).

**Deployment calibration:** Chat interface (Adaptive): LOW to MEDIUM · Claude Projects: LOW to MEDIUM · Claude Code (`medium` default on Opus 5.5 / Sonnet 5.5 / Haiku 5.5): LOW (verbosity); MEDIUM (over-terse code explanations observed) · API (effort ≥ high): LOW.

**Countermeasure template (3a conversational; softer, 4.7-calibrated):**
```
Match response length to question complexity. For simple factual questions,
a sentence is sufficient. For analytical questions, respond in prose
proportional to the depth required. Do not restate the question. Do not
pad with transitional framing that adds no content.
```

3b and 3c templates and the Fable 5.1 facet lines are in reference Section 3.

**Placement:** Output standards (3a, 3c); agentic-context section of core rules (3b). Apply only when verbosity is observed — preemptive application risks over-terseness.

### 4. List overuse

Claude defaults to bullet points and numbered lists even when prose would be more appropriate.

**Symptom:** analytical reasoning fragmented into bullets, and headers on every response regardless of content type.

**Deployment calibration:** Chat interface (Adaptive): MEDIUM · Claude Projects: MEDIUM · Claude Code (`medium` default on Opus 5.5 / Sonnet 5.5 / Haiku 5.5): LOW (code output is structurally formatted regardless) · API (effort ≥ high): MEDIUM.

**Countermeasure template:**
```
Default to prose explanations. Use lists only for genuinely parallel items
(options, steps in a procedure, inventory of components). Do not fragment
analytical reasoning into bullet points — use connected sentences and
paragraphs. Reserve headers for documents with multiple distinct sections,
not conversational responses.
```

**Over-correction on Fable 5.1:** Fable 5.1 formats less (less bold, fewer headers and lists) and writes denser prose by default, so this template and other v4.0-era anti-formatting rules can suppress structure the content needs. On Fable 5.1, replace blanket anti-list rules with the conditional formulation — "use lists… when the content is multifaceted enough that they help; plain prose in conversational exchanges" `[Anthropic docs]` — and use "remove all mannered prose" `[Anthropic docs]` for density. See reference Section 4.

**Placement:** Output standards.

### 5. Fabricated precision (external-fact)

Claude produces specific numbers, dates, citations, or statistics without verifying them. Reduced at the model level in 4.7 — narrowed to external-fact fabrication. **Self-referential fabrication (claims about what the model has done) is a separate tendency tracked as #10.** **Facet — unmarked quotations (Fable 5.1):** summaries reproduce source passages without quotation marks.

**Symptom:** plausible-sounding statistics, citations, or attributions that do not exist; quoted source text presented as the model's own words.

**Deployment calibration:** Chat interface (Adaptive): LOW to MEDIUM (4.7 improvements meaningful) · Claude Projects: LOW to MEDIUM · Claude Code (`medium` default on Opus 5.5 / Sonnet 5.5 / Haiku 5.5): LOW — v4.0 relied on `high`-effort mitigation; at the `medium` default it is weaker, so apply on observation rather than excluding by default · API (effort ≥ high): LOW.

**Countermeasure template (lighter touch for 4.7):**
```
When a specific number, date, or citation is not known with confidence,
say so and provide the range or approximation that is supported. Do not
invent statistics, sources, or attributions. "Approximately" is better
than a fabricated exact figure.
```

For unmarked quotations: require marked quotation in the Output layer and give one complete worked example (request → correct response → rationale) in the system prompt — shape in reference Section 5.

**Placement:** Core rules; the quotation rule and example in output standards.

### 6. Over-exploration

Claude pursues too many investigative threads or runs excessive tool calls within a task. (Delivering beyond the task — unrequested features — is #12.) Reduced at the model level in 4.7 on focused tasks; persistent on complex agentic workflows at higher effort.

**Symptom:** many files read when one would do, and simple questions turned into multi-step research.

**Deployment calibration:** Chat interface (Adaptive): LOW (model calibrates well at Adaptive) · Claude Projects: LOW to MEDIUM · Claude Code (`medium` default on Opus 5.5 / Sonnet 5.5 / Haiku 5.5): MEDIUM (`xhigh` and `max` amplify exploration on complex tasks) — v4.0 relied on `high`-effort mitigation; at the `medium` default it is weaker, so apply on observation rather than excluding by default · API (effort ≥ high): MEDIUM on complex tasks.

**Countermeasure template (softened for 4.7):**
```
Scope work to what was requested. Do not add features, options, or
analysis beyond the stated task. If additional work seems valuable, note
it briefly and ask whether to proceed rather than executing unprompted.
```

**Inverse on Opus 5.5 multi-app workflows:** Opus 5.5 "tends to get to work quickly" `[Anthropic docs]` — it under-explores. There the countermeasure runs the other way ("Before taking any action, explore broadly with tool calls…" `[Anthropic docs]`); keep the #6 template for `xhigh`/`max` runs where excess breadth is observed.

**Placement:** Core rules.

### 7. Tool trigger miscalibration — two facets

#### 7a — Over-triggering (reduced in 4.7)

Claude invokes tools when the task doesn't require them — searches on questions answerable from training, reads files already in context.

**Deployment calibration:** Chat interface (Adaptive): LOW · Claude Code (`medium` default on Opus 5.5 / Sonnet 5.5 / Haiku 5.5): LOW — v4.0 relied on `high`-effort mitigation, but the 5.5-generation guides document the opposite failure (under-search, 7b), so 7a stays LOW · API: LOW.

**Countermeasure template (softened):**
```
Invoke tools only when the task requires information not in the current
context. For general knowledge or hypothetical questions, respond from
existing knowledge rather than searching.
```

Apply only on observed over-triggering: this is tool-discouraging language, which on the 5.5 generation produces 7b.

#### 7b — Under-triggering (NEW in 4.7 chat interface; fix direction flipped on the 5.5 generation)

Claude fails to fire tools even when user preferences or Project CI require them, because persistent-context instructions are weighted lower than immediate prompts. On Sonnet 5.5, Haiku 5.5, and Fable 5.1, tool-suppressing language carried over from older prompts now causes under-search, and at `low` effort the model answers from memory.

**Symptom:** a search or file consultation required by Preferences or CI is silently skipped, and the answer comes from training.

**Deployment calibration:** Chat interface (Adaptive): HIGH · Claude Projects: MEDIUM · Claude Code (`medium` default on Opus 5.5 / Sonnet 5.5 / Haiku 5.5): LOW; MEDIUM at `low` or when tool-suppressing language is present (Sonnet 5.5 / Haiku 5.5 / Fable 5.1 guides) · API (effort ≥ high): LOW.

**Countermeasure, step 1 — remove suppression, then nudge.** "First, check your prompt for language that discourages tool use, such as "only use tools when strictly necessary" or "minimize tool calls," and remove it." `[Anthropic docs]` Then add the search nudge `[Anthropic docs — Sonnet 5.5 guide]`:
```
Use the search tool to check specifics that may have changed since your training, such as what is allowed, required or charged, even when you feel confident. For researched work such as a report or a comparison, gather current sources rather than writing from your training knowledge.
```
Give the current date (Haiku 5.5). On Fable 5.1 at `low`, raise effort for affected turns or add a name-verification nudge. Do not add blanket "always search" instructions — the Haiku 5.5 guide reports more searching on prompts that needed none, with no accuracy gain.

**Countermeasure, step 2 — explicit enforcement** (when Preferences or CI name a required tool):
```
When User Preferences or Project Custom Instructions specify that a tool
MUST be used for a given task type, invoking that tool is mandatory, not
optional. If [specific tool, e.g., web_search] is configured as required
for [specific task type, e.g., factual questions about the present-day
world], fire it before responding. Do not silently skip a required tool.
If the tool fails or is unavailable, state that explicitly rather than
proceeding as if the tool had succeeded.
```

**Placement:** 7a — wherever tool-use instructions appear (recalibrate existing instructions). 7b — core rules or User Preferences, naming the tools observed to under-fire. This is the one context in current-era prompt design where emphatic language (MUST) is the right answer.

### 8. LaTeX defaulting

Claude formats mathematical expressions in LaTeX even when plain text would be more appropriate for the rendering environment.

**Symptom:** raw `$...$` syntax in Slack, plain email, or Markdown that does not render math, including for simple ratios and percentages.

**Deployment calibration:** Chat interface (Adaptive): MEDIUM · Claude Projects: MEDIUM · Claude Code (`medium` default on Opus 5.5 / Sonnet 5.5 / Haiku 5.5): LOW · API (effort ≥ high): MEDIUM (depends on rendering environment).

**Countermeasure template:**
```
Use plain text for mathematical expressions unless the rendering
environment explicitly supports LaTeX. Ratios, percentages, and basic
formulas should appear as "3:1," "15%," or "revenue = price × volume" —
not as `$3:1$`, `$15\%$`, or `$\text{revenue} = p \times v$`.
```

**Placement:** Output standards.

### 9. Editorial drift (NEW in 4.7)

Claude produces unsolicited commentary on its own boundaries, the act of responding, or its constraints. Distinct from hedging — hedging qualifies the content of the response; editorial drift adds meta-content about the response itself.

**Symptom:** preambles about how the model will answer, unasked-for scope disclaimers, and closing notes on what the user might also consider.

**Deployment calibration:** Chat interface (Adaptive): HIGH · Claude Projects: MEDIUM (CI partially anchors) · Claude Code (`medium` default on Opus 5.5 / Sonnet 5.5 / Haiku 5.5): LOW — v4.0 relied on `high`-effort mitigation; at the `medium` default it is weaker, so apply on observation rather than excluding by default · API (effort ≥ high): LOW.

**Countermeasure template:**
```
Do not produce unsolicited commentary on your own response, your
constraints, or your approach. Do not open with framing about how you
will answer; begin with the answer. Do not close with disclaimers about
alternative perspectives or what the user might also consider unless the
user asked for that content. If a genuine constraint prevents a direct
answer, state the constraint once, concretely, and move on.
```

**Placement:** Output standards or core rules. High-attention position for chat interface deployments.

### 10. Self-referential fabrication (NEW in 4.7)

Claude claims to have performed an action, checked a state, or inspected its own runtime context without doing so. The claim is plausibility-driven. Distinct from #5: #5 is the content of the response; #10 is claims about the process of producing it. Asymmetric: fabrication appears in initial responses; honest correction appears under direct challenge.

**Symptom:** "I searched and found X," "I checked the Memory," or "I loaded the file" when no such action ran.

**Deployment calibration:** Chat interface (Adaptive): HIGH · Claude Projects: MEDIUM (CI partially anchors; verified via seed-project self-observation) · Claude Code (`medium` default on Opus 5.5 / Sonnet 5.5 / Haiku 5.5): LOW · API (effort ≥ high): LOW.

**Countermeasure template:**
```
Before asserting that an action has been performed or that a state has
been verified, confirm the action's observable effect. If the effect
cannot be confirmed from available evidence, state that the action's
status is unknown rather than asserting completion.

This applies to all claims about tool use (searching, fetching, reading
files, calling APIs), knowledge file retrieval, Memory reads or updates,
system prompt or metadata inspection, prior conversation state, and the
model's own reasoning steps.

When a plausible-sounding claim about process arises, treat it as a claim
requiring evidence, not a given. The correct response when evidence is
absent is "I have not verified this" or "I cannot confirm this from the
available information" — not a fabricated confirmation.

Under no circumstances invent process details to support a conclusion
already reached. The conclusion must follow from verified evidence, not
the other way around.
```

**Placement:** Core rules. Universal across deployment contexts; apply whenever the Project involves reporting on actions performed (audit Skills, memory-optimization work, file consultation workflows, diagnostic invocations). In the Claude.ai GUI, tool indicators ("Searched the web") provide external verification that API deployments lack — make this distinction explicit when the Project spans multiple surfaces.

### 11. Over-verification (REMOVAL shape)

Claude verifies its own work automatically; prompts that accumulated self-directed re-check instructions ("double-check your answer," "re-verify before responding," "use a subagent to verify") compound with that and spend tokens without a quality gain. The 5.5 generation extends the pattern to thinking instructions ("think carefully before answering," "re-verify earlier answers") — effort is the control. **Effort-conditioned facet:** at `xhigh`/`max`, Sonnet 5.5 starts its own review rounds.

**Symptom:** Claude keeps re-checking its work, or a prompt that says "double-check" made output slower, not better.

**Deployment calibration:** Chat interface (Adaptive): MEDIUM · Claude Projects: MEDIUM · Claude Code (`medium` default on Opus 5.5 / Sonnet 5.5 / Haiku 5.5): HIGH · API (agent workloads, effort ≥ high): HIGH.

**Countermeasure:** REMOVAL — delete the self-directed re-check and think-harder lines; do not insert a counter-instruction. Keep external-artifact checks (run the tests, inspect the rendered page, confirm the file exists) — they are the keep class, not this tendency. Sweep patterns, preservation patterns, and procedure: reference Section 11. At `xhigh`/`max`, add the review-round block in #13. For chat only, an optional "treat earlier answers as settled" line; not for agentic work, where later steps can reveal earlier mistakes. Removal applies wherever the lines live (system prompt, CLAUDE.md, Skill bodies).

### 12. Scope expansion

Claude delivers beyond the task — extra steps, features, or its own reading of what the task should be. Distinct from #6 (search breadth within a task); the opposite of #15. **Facet — unrequested additions:** tests, docs, and small supporting files that fit repo conventions, at every effort level and more at higher (Sonnet 5.5, Haiku 5.5, Fable 5.1); open-ended "show me what you can do" requests get built rather than answered.

**Symptom:** Claude adds things nobody asked for, or builds a whole feature when asked for options.

**Deployment calibration:** Chat interface (Adaptive): MEDIUM · Claude Projects: MEDIUM · Claude Code (`medium` default on Opus 5.5 / Sonnet 5.5 / Haiku 5.5): HIGH · API (agent workloads, effort ≥ high): HIGH.

**Countermeasure:** the second paragraph of the #15 default block (it ships with the first, because a prompt that only says "keep working" invites scope expansion). For open-ended requests, add `[Anthropic docs — Sonnet 5.5 guide]`:
```
When the user asks for ideas, options or a plan, give them that and stop. Don't start building or changing anything until they say to go ahead.
```
The `<scope>` template, the stronger CC variant, and the Fable 5.1 pre-existing-bug rule for coding are in reference Section 12.

**Placement:** Core rules for agentic deployments; output standards otherwise.

### 13. Subagent over-delegation

Claude delegates to subagents more readily than earlier generations. Delegation pays off on genuinely independent, sizeable tracks; on small tasks it multiplies cost and time. Includes spawning a subagent to verify its own work (a subagent instance of #11). **Effort-conditioned facet:** at `xhigh`/`max`, Sonnet 5.5 launches reviewer subagents on its own.

**Symptom:** Claude spawns subagents for tiny tasks, or every subagent runs on the expensive model.

**Deployment calibration:** Chat interface / Claude Projects: N/A (no subagent surface) · Claude Code (`medium` default on Opus 5.5 / Sonnet 5.5 / Haiku 5.5): HIGH · API (multi-agent workloads): HIGH.

**Countermeasure, first line** `[Anthropic docs — Sonnet 5.5 guide]` — this paragraph "stopped reviewer subagent launches and cut session cost by about a third, with no change in quality":
```
When the work the user asked for is done and its checks pass, stop and report. Don't start extra rounds of review or hardening on your own, and don't launch reviewer sub-agents unless the user asked for a review. If you think a deeper review is worth doing, say so at the end.
```
Then the `<subagent_delegation>` template and the cap / subagent-model mechanism (reference Section 13; `CLAUDE_CODE_*` names are dated product facts — verify on the running Claude Code version).

**Placement:** CLAUDE.md or system-prompt core rules.

### 14. Correction narration

Claude narrates corrections to its earlier statements, including corrections that change nothing for the user.

**Symptom:** Claude narrates every correction, however small.

**Deployment calibration:** Chat interface (Adaptive): MEDIUM (extended conversations accumulate corrections) · Claude Projects: MEDIUM · Claude Code (`medium` default on Opus 5.5 / Sonnet 5.5 / Haiku 5.5): LOW · API: LOW.

**Countermeasure:** correct an earlier statement only when the error would change the user's code, conclusions, or decisions; fix other slips without noting them — `<correction_policy>` template in reference Section 14. **Placement:** Output standards.

### 15. Early turn termination (NEW in v5.0)

Claude ends its turn while requested work is still owed: a summary that announces the next step with no tool call; an offer to continue; a list of decisions for the user when none blocks the remaining work; a report because the turn ran long or a milestone is done; at low effort, pausing to confirm a plan or asking a question it could answer itself; in long agent prompts, handing the task back. Distinct from #12 (too much) and #6 (search breadth) — #15 is too little, and its countermeasure runs opposite to #12's. Documented in all four current Anthropic prompting guides (Opus 5.5, Sonnet 5.5, Haiku 5.5, Fable 5.1).

**Symptom:** Claude stops mid-task to ask for confirmation, or writes the next step without doing it.

**Deployment calibration:** Chat interface (default effort): LOW — a chat turn is supposed to end · Claude Code (`medium` default on Opus 5.5 / Sonnet 5.5 / Haiku 5.5): MEDIUM at `medium`, HIGH at `low`; LOW at `high` and above; long system prompts raise it (Haiku 5.5 guide) · API agentic (developer-controlled effort): as Claude Code by effort level; HIGH for fully unattended loops with no harness continuation · Cowork / scheduled runs: HIGH — no operator present to send the continuation.

**Countermeasure — first lever is effort.** At `low`/`medium`, try raising effort before adding the block; the block lengthens output and costs more at low effort (Sonnet 5.5 guide). Then the default block `[Anthropic docs — Sonnet 5.5 / Haiku 5.5 guides]`:
```
Keep working until everything the user asked for is done, and only stop to ask when you can't go on without the user or before a risky step.

When the work the user asked for is done and checked, stop and report. Don't add features, tests, files, docs or refactors that weren't asked for. If you think one would help, mention it at the end instead of doing it.
```
This is a turn-boundary instruction, not a self-verification instruction (AEA §4.14 keep class) — a D7 self-verification scan must not flag it. The fully-unattended variant (Opus 5.5 guide) and the harness complement are in reference Section 15.

**Placement:** Core rules. Fully-unattended variant at the end of the system prompt from the first request; never in human-in-the-loop applications.

---

## Diagnostic routing

Match the user's described symptom against the patterns below. If multiple tendencies are plausible, prioritize by deployment context — a chat-interface issue more likely maps to 1b, 9, or 10; a Claude Code issue more likely maps to 11–13 or 15.

| Symptom pattern | Likely tendency |
|---|---|
| "Claude validates everything I say" | 1a |
| "Claude stops following my preferences over time" | 1b |
| "Claude ignores my Preferences in long conversations" | 1b |
| "Claude hedges on opinions or recommendations" | 2 |
| "Claude is too long-winded" | 3a |
| "Claude narrates every step while it works" | 3b |
| "The report files Claude writes are bloated" / "rewrites the whole file for a one-line edit" | 3c |
| "Claude uses bullet points for everything" | 4 |
| "Claude makes up statistics or sources" | 5 |
| "Claude explores too many options" | 6 |
| "Claude uses tools unnecessarily" | 7a |
| "Claude won't use a tool I told it to use" | 7b |
| "Claude keeps skipping web search even though I require it" | 7b |
| "Claude uses math notation unnecessarily" | 8 |
| "Claude adds unsolicited boundary commentary" | 9 |
| "Claude adds disclaimers I didn't ask for" | 9 |
| "Claude claims it did something it didn't" | 10 |
| "Claude says it searched but didn't" | 10 |
| "Claude says it read the file but clearly didn't" | 10 |
| "Claude keeps re-checking / re-verifying its work" | 11 |
| "The prompt says double-check and output got slower" | 11 |
| "Claude adds things I didn't ask for" / "adds tests I didn't ask for" | 12 |
| "Claude built a whole feature when I asked for options" | 12 |
| "Claude spawns subagents for tiny tasks" | 13 |
| "Every subagent runs on the expensive model" | 13 |
| "Claude narrates every correction" | 14 |
| "Claude stops and asks me to confirm mid-task" | 15 |
| "Claude writes a summary and a next step but doesn't do the step" | 15 |
| "The agent hands the task back half-done" | 15 |
| "Claude offers to continue instead of continuing" | 15 |
| "Claude ignores messages I send while it's working" | Conditional defect: mid-turn user text misread as injection |
| "Claude refuses when I ask it to show its reasoning" | Conditional defect: reasoning-extraction refusal |

When the symptom could plausibly match multiple tendencies, ask the user for a concrete example. Apply the countermeasure for the tendency the example best matches.

**Conditional defects (not tendencies).** Four failure modes track to the prompt or the runtime rather than the model, and are fixed by rewriting the prompt or harness, not by adding a counter-instruction: conservative-review literalism; thinking-disabled output artifacts (now documented only on Haiku 5.5, plus Sonnet 5.5 `between_tools` with a "don't think" line left in place); mid-turn user text misread as injection (a harness fix — design detail in `rootnode-domain-agentic-context` if available); and reasoning-extraction refusal. See the reference appendix.

---

## Deployment conditioning

Not all countermeasures apply equally across deployment contexts. Before applying a countermeasure, confirm the deployment target:

- **Chat interface (Adaptive effort):** Tendencies 1b, 7b, 9, and 10 are most pronounced here. Strong countermeasures recommended. The Adaptive effort default weights persistent context lower than immediate prompts — the primary driver of 1b, 7b, 9, and 10. Tendency 15 is LOW: a chat turn is supposed to end.
- **Claude Projects:** Tendencies 1b and 9 are mitigated by strong Custom Instructions but not eliminated. Moderate countermeasures appropriate. Tendency 10 is also MEDIUM here — verified via seed-project self-observation.
- **Claude Code (`medium` default on Opus 5.5 / Sonnet 5.5 / Haiku 5.5):** Tendencies 11, 12, and 13 are HIGH; 15 is MEDIUM at `medium` and HIGH at `low`. v4.0 treated countermeasures for 5, 6, 7a, and 9 as generally unnecessary because `high` effort mitigated them; at the `medium` default that mitigation is weaker, so apply them on observation rather than excluding them by default. The default is a capability choice, not a degraded mode: Opus 5.5 at `medium` "matches or exceeds Opus 5 at `high` on coding and knowledge-work evaluations" `[Anthropic docs]`. Applicability of this Skill itself is per-Skill: not all rootnode Skills are first-class Claude Code targets.
- **API (developer-controlled effort):** API defaults differ from Claude Code — Opus 5.5 `medium`, Sonnet 5.5 `high`, Fable 5.1 `high` (dated landscape block `root_MODEL_LANDSCAPE_2026-10`; see repository README). At `high` or above, behaves similarly to Claude Code at `high`; at lower effort, closer to the chat interface, and 7b and 15 rise. Raising effort is the first lever for both. Re-run an effort sweep on your own evals rather than carrying a setting over.

When in doubt, apply the universal countermeasures (1a, 4, 8, 10 — #4 in its conditional form on Fable 5.1) and confirm deployment context before applying the conditional ones.

---

## Self-application

This Skill, when running on the current dual-primary tier (Opus 5.5 / Sonnet 5.5) at chat-interface Adaptive effort, is itself subject to tendencies 1b (persistent-preference dilution) and 10 (self-referential fabrication). When using this Skill, if Claude claims to have applied a countermeasure or completed a diagnosis, verify the output explicitly rather than accepting the claim. The Skill's own output is subject to the tendencies it diagnoses.

---

## When to Use This Skill

Use this Skill when:
- A user reports a specific behavioral complaint about Claude's output
- A user wants to audit a system prompt or Project for behavioral calibration gaps
- A user is migrating a prompt from an earlier Claude generation (pre-4.7 emphatic language; pre-5.5 tool-suppression, thinking-disabled mitigations, or `high`-effort assumptions) and needs to recalibrate
- A user asks how to make Claude more direct, more concise, less agreeable, more persistent, or otherwise adjust a specific behavioral dimension
- A user describes recurring output problems without naming a specific tendency

Do NOT use this Skill when:
- The user wants to evaluate a prompt's overall quality (use `rootnode-prompt-validation` if available)
- The user wants a full Project audit (use `rootnode-project-audit` or `rootnode-full-stack-audit` if available)
- The user wants to redesign Memory or knowledge file placement (use `rootnode-memory-optimization` if available)
- The user wants to compile a new prompt from scratch (use `rootnode-prompt-compilation` if available)

---

## Troubleshooting

**Symptom maps to multiple tendencies:** Ask the user for a concrete example. The specific phrasing of the example usually disambiguates.

**Countermeasure doesn't stick:** Check placement. Agreeableness and persistent-preference countermeasures need high-attention positions (identity block or core rules at the top). Placing them in the middle of a long system prompt reduces effect.

**Over-correction:** If applying a countermeasure introduces the reverse problem (too terse after a verbosity fix, too blunt after an agreeableness fix, too little structure on Fable 5.1 after an anti-list fix), soften the language or scope the countermeasure to specific contexts.

**Pre-4.7 prompts with emphatic language:** Opus 4.7 responds more to normal-weight language than to MUST / ALWAYS / CRITICAL. The exception is tendency #7b where explicit enforcement is the right answer. For other tendencies, rewrite emphatic language as calibrated guidance.

**Pre-5.5 prompts with thinking-disabled mitigations or tool-suppression language:** remove them (tendencies 7b, 11).

**Extended countermeasure variants:** See `references/countermeasure-templates.md` for identity-level embedding, output-standards integration, and stronger-variant options per tendency, plus worked examples (symptom routing, self-referential fabrication, deployment disambiguation, early turn termination).

---

## Quality Gate

Before finalizing a countermeasure recommendation:

- Has the deployment context been confirmed?
- Has the symptom been matched to a specific tendency (or tendencies), with evidence?
- Is the countermeasure template the one appropriate for this tendency in this deployment context?
- Is placement specified (identity block, core rules, output standards)?
- For tendencies with reduced 4.7 manifestation (#1a, #2 on factual, #3, #5, #6, #7a), has the user actually observed the failure mode, or would applying the countermeasure be preemptive?
- Did the countermeasure set exclude a tendency on the assumption of `high` effort when the deployment runs at `medium`?
