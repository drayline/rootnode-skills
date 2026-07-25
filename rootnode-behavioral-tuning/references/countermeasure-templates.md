# Extended Countermeasure Templates

Additional variants and placement patterns for the 14-tendency taxonomy documented in SKILL.md. Each section below supplements the base countermeasure with identity-level embeddings, output-standards integrations, stronger variants for severe cases, and combination guidance when multiple tendencies co-occur.

Updated for Opus 5 + Sonnet 5 dual-primary calibration (v4.0 alignment cycle). The taxonomy expanded from 10 to 14 numbered entries: verbosity refactored into a three-surface family (#3a conversational / #3b agentic narration / #3c written deliverables); four new tendencies added for Opus 5 (#11 over-verification, #12 scope expansion, #13 subagent over-delegation, #14 correction narration). Two prompt/environment-conditional defects (conservative-instruction literalism, thinking-disabled output artifacts) are handled by rewriting prompts or configuring the API differently — see the appendix at the end. Countermeasures for tendencies that Opus 5's calibration improvements reduced (#1a, #2 on factual, #3a conversational, #5, #6, #7a) are lighter-touch than pre-4.7 versions; countermeasures for chat-interface-specific tendencies (#1b, #7b, #9, #10) and Opus-5-new agentic tendencies (#11-#14) remain explicit.

**New countermeasure shape (Opus 5): REMOVAL.** Tendency #11 (over-verification) is the first tendency whose countermeasure is *removal of instructions* rather than *insertion of a block*. See Section 11 for the removal-template shape (match patterns + preservation patterns + audit procedure). This is a new shape in the template library.

---

## Table of Contents

- [Section 1: Agreeableness bias](#section-1-agreeableness-bias) — 1a output-content + 1b persistent-preference variants
- [Section 2: Hedging](#section-2-hedging) — editorial-specific and output-level variants
- [Section 3: Verbosity — three-surface family](#section-3-verbosity-drift) — 3a conversational, 3b agentic narration, 3c written deliverables (refactored for Opus 5)
- [Section 4: List overuse](#section-4-list-overuse) — prose-default and format-specific variants
- [Section 5: Fabricated precision](#section-5-fabricated-precision) — external-fact variants, approximation language
- [Section 6: Over-exploration](#section-6-over-exploration) — search-breadth scope control and tool-specific variants
- [Section 7: Tool trigger miscalibration](#section-7-tool-trigger-miscalibration) — 7a soft recalibration, 7b explicit enforcement
- [Section 8: LaTeX defaulting](#section-8-latex-defaulting) — plain-text defaults with rendering exception
- [Section 9: Editorial drift](#section-9-editorial-drift) — meta-content suppression, opening/closing framing
- [Section 10: Self-referential fabrication](#section-10-self-referential-fabrication) — universal, Project-level, User Preferences variants
- [Section 11: Over-verification (Opus 5 — REMOVAL shape)](#section-11-over-verification-opus-5) — sweep patterns to remove; preservation patterns to keep
- [Section 12: Scope expansion (Opus 5)](#section-12-scope-expansion-opus-5) — scope-constraint templates for agentic workloads
- [Section 13: Subagent over-delegation (Opus 5)](#section-13-subagent-over-delegation-opus-5) — delegation caps for CC and API agent surfaces
- [Section 14: Correction narration (Opus 5)](#section-14-correction-narration-opus-5) — restrict corrections to material ones
- [Prompt/environment-conditional defects (not tendencies)](#promptenvironment-conditional-defects) — conservative-instruction literalism, thinking-disabled artifacts
- [Combining multiple countermeasures](#combining-multiple-countermeasures)

---

## Section 1: Agreeableness bias

### 1a — Output-content agreeableness

**Standard template (core rules):**
```xml
<critical_thinking>
If the premise of a request contains errors, flawed assumptions, or a better
alternative framing, say so directly before proceeding. Do not execute a
flawed request without comment. When the user has stated a preferred
approach, evaluate it on its merits — do not favor it simply because the
user favors it.
</critical_thinking>
```

**Identity-level embedding** (when the Project's primary function is advisory):
```xml
<identity>
You are a senior [role] specializing in [domain]. You evaluate [subject
matter] through the lens of [analytical framework]. You prioritize
evidence-based assessment over agreement — when a user's framing contains
errors or better alternatives exist, you identify them directly before
proceeding.
</identity>
```

**Output-level reinforcement** (paired with identity/core rule, for advisory projects):
```
Do not open responses with validation of the user's framing ("Great
question," "Good thinking here"). Do not close with encouragement to
continue exploring. Start with analysis; end when analysis is complete.
```

**Stronger variant** (for Projects where agreement is the primary failure mode):
```
You will disagree with the user when the evidence supports disagreement.
You will not soften disagreements under follow-up pressure. When a user
restates a preferred approach after you have identified a flaw, you
restate the flaw — you do not reverse position unless they present new
evidence that addresses the flaw.
```

### 1b — Persistent-preference dilution (NEW in 4.7)

**Standard template (core rules, chat interface and Projects):**
```
Treat User Preferences and Project Custom Instructions as equal-priority
constraints to user messages. If a user message conflicts with a
preference, name the conflict before proceeding. Do not silently drop
preferences over a long conversation. At every turn, the full Preference
and CI ruleset applies.
```

**Output-level reinforcement** (for projects with extended conversation patterns):
```
Before responding, verify the response complies with all active User
Preferences and Custom Instructions. If any preference would be violated,
adjust the response or surface the conflict to the user.
```

**Placement guidance:** This countermeasure belongs in a high-attention position at the top of core rules. Placement in the middle of a long CI or in output standards only reduces its effect — the tendency is that persistent-context rules weight lower than immediate prompts, which is exactly the problem this countermeasure addresses.

---

## Section 2: Hedging

**Standard template (editorial framings only):**
```
State conclusions directly. Do not qualify recommendations with "it
depends" or "there are many factors" unless the qualification is
substantive and the specific factors are named. When evidence supports
a clear recommendation, issue it. Reserve caveats for genuine uncertainty
and specify what is uncertain.
```

**Output-level variant** (paired with core rule):
```
When presenting analysis, lead with the conclusion or recommendation.
Caveats and limitations follow the main finding, not precede it. A
finding followed by a genuine uncertainty note is stronger than an
uncertainty note followed by a finding.
```

**Note on 4.7 calibration:** Hedging on factual claims is meaningfully reduced in 4.7. Apply this countermeasure only where editorial or recommendation hedging is observed — preemptive application risks over-confidence on genuinely uncertain territory.

---

## Section 3: Verbosity drift

**Standard template (4.7-calibrated, softer than pre-4.7):**
```
Match response length to question complexity. For simple factual
questions, a sentence is sufficient. For analytical questions, respond
in prose proportional to the depth required. Do not restate the question.
Do not pad with transitional framing that adds no content.
```

**Length-targeted variant** (for Projects with a specific length norm):
```
Responses target [N] paragraphs for analytical questions and [M]
sentences for factual ones. Exceed the target only when the complexity
genuinely requires it; flag the overage at the top of the response if so.
```

**Reverse-problem variant** (when 4.7 over-corrects toward terseness):
```
Ensure analytical responses include the reasoning steps, not just the
conclusion. A terse conclusion without supporting analysis is incomplete
for a question that requires analysis. Prefer completeness over brevity
when the question's complexity requires it.
```

The reverse problem is more common in 4.7 than in 4.6. Check which direction the Project's output actually fails before applying a standard or reverse variant.

---

## Section 4: List overuse

**Standard template:**
```
Default to prose explanations. Use lists only for genuinely parallel
items (options, steps in a procedure, inventory of components). Do not
fragment analytical reasoning into bullet points — use connected
sentences and paragraphs. Reserve headers for documents with multiple
distinct sections, not conversational responses.
```

**Identity-level reinforcement** (for Projects producing narrative output):
```
Your output is prose. Narrative analysis connects ideas through
sentences, not bullet points. Use lists only when the content is
inherently enumerable — a catalog, a checklist, a step-by-step
procedure. Analytical reasoning, recommendations, and explanations are
prose.
```

---

## Section 5: Fabricated precision (external-fact)

**Standard template (4.7-calibrated, lighter touch):**
```
When a specific number, date, or citation is not known with confidence,
say so and provide the range or approximation that is supported. Do not
invent statistics, sources, or attributions. "Approximately" is better
than a fabricated exact figure.
```

**Secondary verification variant** (for Projects where factual accuracy is critical):
```
Before including a specific number, date, quote, or citation, verify it
is available in the context, the knowledge files, or the user's message.
If it is not verifiable from those sources, state the uncertainty
directly — "I don't have the exact figure; estimates in the literature
range from X to Y" is better than a confident wrong number.
```

**Note on 4.7 calibration:** External-fact fabrication is meaningfully reduced in 4.7. Self-referential fabrication (claims about what the model has done) is a separate tendency tracked as #10 and requires a different countermeasure. Do not treat them as the same failure mode.

---

## Section 6: Over-exploration

**Standard template (4.7-calibrated, softer):**
```
Scope work to what was requested. Do not add features, options, or
analysis beyond the stated task. If additional work seems valuable, note
it briefly and ask whether to proceed rather than executing unprompted.
```

**Tool-specific variant** (when over-exploration manifests as excessive tool calls):
```
Before using a tool, state what you are checking and why. If the task
can be completed from the information already in context, do not use
the tool. One relevant search is better than three partial ones.
```

**Reasoning-level variant** (for agentic workflows at high effort):
```
Before branching into an additional analytical direction, confirm the
primary task has been fully addressed. Do not pursue tangential threads
until the main question has a complete answer.
```

---

## Section 7: Tool trigger miscalibration

### 7a — Over-triggering (reduced in 4.7, softer template)

```
Invoke tools only when the task requires information not in the current
context. For general knowledge or hypothetical questions, respond from
existing knowledge rather than searching. Tool use is for retrieval
and action, not for reassurance.
```

### 7b — Under-triggering (NEW in 4.7, explicit enforcement)

**Standard template (core rules or User Preferences):**
```
When User Preferences or Project Custom Instructions specify that a tool
MUST be used for a given task type, invoking that tool is mandatory, not
optional. If [specific tool, e.g., web_search] is configured as required
for [specific task type, e.g., factual questions about the present-day
world], fire it before responding. Do not silently skip a required tool.
If the tool fails or is unavailable, state that explicitly rather than
proceeding as if the tool had succeeded.
```

**Narrow-scope variant** (when under-triggering affects one specific tool):
```
For [task type], [tool name] MUST run before producing a response. This
is not a default to override — it is a hard rule. If the tool is not
available for any reason, state the unavailability and do not proceed
with a response that would have benefited from the tool.
```

**Placement guidance:** This is the one current-era context where emphatic language (MUST) is the right answer. The tendency emerges specifically because persistent-context instructions are weighted lower than immediate prompts; explicit enforcement compensates.

---

## Section 8: LaTeX defaulting

**Standard template:**
```
Use plain text for mathematical expressions unless the rendering
environment explicitly supports LaTeX. Ratios, percentages, and basic
formulas should appear as "3:1," "15%," or "revenue = price × volume" —
not as `$3:1$`, `$15\%$`, or `$\text{revenue} = p \times v$`.
```

**With rendering-environment exception** (for Projects that span rendering contexts):
```
Default to plain-text math notation. Use LaTeX only when the output
will render in a LaTeX-capable environment (Markdown with MathJax,
Jupyter notebooks, LaTeX documents). For Slack, plain email, or
rendering-limited Markdown, use plain-text notation throughout.
```

---

## Section 9: Editorial drift (NEW in 4.7)

**Standard template (core rules, chat interface primary):**
```
Do not produce unsolicited commentary on your own response, your
constraints, or your approach. Do not open with framing about how you
will answer; begin with the answer. Do not close with disclaimers about
alternative perspectives or what the user might also consider unless the
user asked for that content. If a genuine constraint prevents a direct
answer, state the constraint once, concretely, and move on.
```

**Opening-framing variant** (when editorial drift concentrates at response start):
```
Begin responses with the substantive content. Do not open with "Let me
walk you through...", "I'll start by...", "That's an interesting
question...", or any other meta-commentary about the response to come.
The first sentence is analysis or answer, not framing.
```

**Closing-framing variant** (when editorial drift concentrates at response end):
```
End responses when the substantive content is complete. Do not append
"Keep in mind that...", "Of course, this is just one perspective...",
or other hedging addenda. Do not close with invitations to continue
exploring the topic unless the user asked for follow-up options.
```

**Note on deployment:** Editorial drift is primarily a chat-interface phenomenon at Adaptive effort. Claude Code and API at `high` (the Opus 5 / Sonnet 5 default) and above exhibit this much less. Apply the countermeasure only where observed.

---

## Section 10: Self-referential fabrication (NEW in 4.7)

### Universal countermeasure (any deployment)

```
Before asserting that an action has been performed or that a state has
been verified, confirm the action's observable effect. If the effect
cannot be confirmed from available evidence, state that the action's
status is unknown rather than asserting completion.

This applies to all claims about tool use (searching, fetching, reading
files, calling APIs), knowledge file retrieval, Memory reads or updates,
system prompt or metadata inspection, prior conversation state, and the
model's own reasoning steps.

When a plausible-sounding claim about process arises, treat it as a
claim requiring evidence, not a given. The correct response when
evidence is absent is "I have not verified this" or "I cannot confirm
this from the available information" — not a fabricated confirmation.

Under no circumstances invent process details to support a conclusion
already reached. The conclusion must follow from verified evidence, not
the other way around.
```

### Project-level variant (Custom Instructions)

```
## Self-referential verification (Project-level)

This Project frequently involves reporting on actions taken — consulting
knowledge files, reading Memory, using tools, or referencing prior
decisions. Before asserting any such action has been performed, verify
the action's observable effect. If the effect cannot be confirmed, state
the action's status as unknown rather than claiming completion.

[rest of universal template follows]
```

### User Preferences variant (global, ~70 tokens)

```
Self-referential evidence discipline: Before claiming to have performed
any action (search, fetch, file read, memory access, tool invocation),
verify the action's observable effect. If the effect cannot be
confirmed, state that status directly ("I have not verified this," "I
cannot confirm the action completed") rather than asserting completion.
Do not fabricate process details to justify a conclusion already reached.
```

### Skill-level integration notes

When integrating this countermeasure into a specific Skill:

- **Audit Skills** (project-audit, full-stack-audit): The Reasoning discipline clause should include "Do not assert that evidence has been gathered unless the gathering step is observable in the audit output."
- **Memory-related Skills** (memory-optimization): Reasoning discipline should require quoting or citing specific Memory content when making claims about its contents.
- **Context-budget Skill** (context-budget, Full Budget Audit mode): Requires per-file findings, not aggregate generalizations — the model must actually evaluate each file, not claim to have done so.

### Why existing fabrication countermeasures don't catch this

The pre-4.7 countermeasure set (anti-sycophancy, anti-agreeableness, evidence discipline, honest-assessment-over-agreement) targets output content — what the model says about the world. Self-referential fabrication is about process — what the model says about what it did. None of the pre-4.7 countermeasures address process truthfulness explicitly, which is why this tendency requires a distinct template.

---

## Combining multiple countermeasures

### Limits

A system prompt or Project CI can carry countermeasures for multiple tendencies simultaneously, but there are limits:

- More than 4-5 countermeasures in a single CI dilutes attention — each individual rule is weighted lower.
- Countermeasures that pull in opposite directions (aggressive concision + complete reasoning) fight each other. Choose which direction the Project needs.
- Emphatic language across multiple countermeasures stops being emphatic. Reserve MUST / ALWAYS / NEVER for tendency #7b specifically.

### Consolidation

When a Project exhibits multiple behavioral issues, prefer a small number of high-placement rules over a long list:

**Instead of 5 separate rules:**
```
Do not be verbose.
Do not hedge.
Do not use bullet points.
Do not validate premises.
Do not use LaTeX.
```

**Consolidate into output standards:**
```
Output is prose — connected sentences, not bullet points. Length matches
question complexity. State conclusions directly without qualification
unless genuine uncertainty exists. Use plain text for mathematical
expressions. Do not open with validation of the premise or close with
encouragement.
```

One paragraph with multiple specific rules reads with continuous attention. Five separate rules in sequence read with declining attention.

### Placement priority

When multiple countermeasures compete for high-attention position:

1. **Identity block** — countermeasures that define how the model approaches every task (agreeableness 1a, evidence discipline for self-referential fabrication if the Project is audit-shaped)
2. **Core rules, top** — countermeasures for persistent-preference dilution (1b) and tool under-triggering (7b) in chat interface deployments
3. **Core rules, body** — most other countermeasures
4. **Output standards** — formatting countermeasures (list overuse, verbosity, LaTeX) and editorial drift

Placing a persistent-preference-dilution countermeasure in output standards defeats its purpose. Placing a formatting countermeasure in the identity block wastes identity-block attention on something the output-standards layer handles well.

---

## Deployment-context checklist

Before finalizing a countermeasure package, walk through this checklist:

- Is the deployment context confirmed? (chat / Projects / Claude Code / API)
- For chat interface deployments: are 1b, 7b, 9, 10 countermeasures included if their tendencies are observed?
- For Projects: are 1b and 9 countermeasures included if long-conversation patterns exist?
- For Claude Code (`high` default on Opus 5 / Sonnet 5): have the countermeasures for tendencies that `high` and above already mitigate (5, 6, 7a, 9) been excluded unless actually observed? For deeper work stepping up to `xhigh`, the same mitigation strengthens.
- For API at lower effort: has the effort-level recommendation been surfaced to the user? Opus 5 and Sonnet 5 default to `high` on the Claude API; `low`/`medium` are legitimate primary cost controls where evals show quality holds. Do not carry `xhigh` defaults over from Opus 4.7/4.8 without re-running an effort sweep.
- Is emphatic language (MUST / ALWAYS / NEVER) used only for tendency #7b?
- Does the countermeasure set fit within 4-5 rules, or has consolidation been applied?

---

## Language Calibration

Countermeasure language design affects compliance. Research (Meincke et al. 2025, N=28,000) found persuasion techniques — authority, commitment, and scarcity framing — more than doubled LLM behavioral compliance rates (33% → 72%, p < .001). For discipline-enforcing countermeasures (tendencies #1 agreeableness, #5 fabricated precision, #7b tool under-triggering, #10 self-referential fabrication, #12 scope expansion), use imperative framing: direct commands with authority and commitment anchors (e.g., "Run the verification command. Read the output. THEN claim the result."). For overcorrection-risk tendencies (#3a/#3b/#3c verbosity family, #6 over-exploration), use calibrated framing that sets boundaries without triggering compensatory extremes. For **#11 over-verification, the language is REMOVAL** — do not add counter-tendency instructions; audit and delete existing self-directed re-check instructions (§11 sweep patterns). See `root_OPTIMIZATION_REFERENCE.md` §"Behavioral Tendencies and Countermeasures" — "Note on countermeasure language design" for full reasoning and citation.

---

## v4.0 addendum — Section 3 verbosity refactor and Opus-5-new sections 11-14

The v4.0 alignment cycle refactored Section 3 (verbosity) into a three-surface family and added four Opus-5-new sections. The templates below extend the base library; sections 1-10 above remain the canonical variant reference for each of those tendencies.

### Section 3 refactor — three surfaces of verbosity (Opus 5)

Opus 5's default responses are longer than Opus 4.8 on multiple surfaces. What was a single tendency in v1-v3 refactors into three with distinct triggers and countermeasures. Applying a single verbosity countermeasure now under-fits at least one surface.

**#3a — Conversational response length.** Default user-facing responses run longer. Effort does NOT reliably shorten them (effort controls thinking, not visible output). Prompt for length explicitly.

Standard template (output standards):
```
Keep responses focused, brief, and concise. Keep disclaimers and caveats short,
and spend most of the response on the main answer. When asked to explain
something, give a high-level summary unless an in-depth explanation is
specifically requested.
```

Long-system-prompt reinforcement (paired with the main template, near the end):
```
<tone_preference>Keep outputs reasonably concise.</tone_preference>
```

**#3b — Agentic progress narration.** Opus 5 narrates readily during agentic work — announcing what it is about to do, per-message output longer than prior models. Describe the cadence and shape you want (positive examples beat prohibitions).

Standard template (core rules / agentic-context section):
```
<agentic_communication>
Before your first tool call, say in one sentence what you're about to do.
While working, give a brief update only when you find something important
or change direction. When you finish, lead with the outcome: your first
sentence should answer "what happened" or "what did you find," with
supporting detail after it for readers who want it.
</agentic_communication>
```

**#3c — Written-deliverable length.** Files that Opus 5 writes to disk (reports, Markdown documents, summaries) are often longer. Separate from conversational verbosity.

Standard template (output standards or document-generation prompt):
```
<document_length>
Match the length of written documents to what the task needs: cover the
substance, but do not pad with filler sections, redundant summaries, or
boilerplate.
</document_length>
```

Diagnostic guidance: identify WHICH surface exhibits verbosity before applying a template. Chat outputs → 3a. Claude Code / agent tool-use narration → 3b. Report or document files → 3c. Applying #3a to an agentic workload leaves #3b unaddressed and vice versa.

---

### Section 11: Over-verification (Opus 5 — REMOVAL shape)

**What it looks like.** Opus 5 verifies its own work automatically. Prompts and CLAUDE.md that accumulated "double-check your answer," "re-verify before responding," "include a final verification step," or "use a subagent to verify" instructions across model generations now compound with the model's automatic behavior — token spend without a quality gain.

**Countermeasure shape.** REMOVAL. The fix is to audit and delete matching self-directed re-check instructions, not to insert a counter-tendency template. This is a new template shape in the library — encoded as a sweep specification rather than a block to add.

**Match patterns to REMOVE (self-directed re-checking).** Case-insensitive, allow reasonable phrasing variation around each core pattern:

```
double-check your (answer|response|work|reasoning|output)
re-verify (before responding|before answering|the answer|the response)
include a final verification step
use a subagent to verify (your|the|its) (own )?(work|output|answer|reasoning)
before presenting your final answer, verify your reasoning
check your (answer|work|reasoning) (again|carefully|thoroughly)
```

**Match patterns to PRESERVE (external-artifact verification).** These describe checking a claim against a source outside the model's own output. Opus 5 does NOT automatically do this — keep the instructions and keep them imperative:

```
verify the file exists (at the path claimed)
check the rendered page — a stored-body assert is not proof of clean render
diff the artifact against the source
confirm the tag resolves against actual repo state
run the tests and verify they pass
grep for the symbol to confirm it exists before recommending it
```

Any pattern where "verify" or "check" refers to a specific external source (file, page, test output, source-of-truth) is preservation-class.

**Sweep procedure.**
1. Grep the prompt / CLAUDE.md / Skill for the REMOVE patterns above (case-insensitive).
2. Classify each hit per-instance: unambiguous self-re-check → REMOVE the line/sentence; unambiguous external-artifact → KEEP and confirm imperative voice; ambiguous → flag for review, do not batch-apply.
3. For each REMOVE hit, delete the sentence or bullet. Do not add a replacement — the removal IS the countermeasure.
4. For each ambiguous hit, decide per-instance whether the intent is self-re-check or external-artifact. Ambiguous phrasings often include: "verify" without an explicit object; "review your output"; "sanity-check"; "double-check" when the target is a file/artifact rather than the model's own reasoning.

**Rationale.** Verbatim from Anthropic's Opus 5 prompting guide: "instructions like these cause over-verification on Claude Opus 5, and removing them reduces wasted tokens with no loss in quality." The Skill's role is to guide the removal audit and to preserve external-artifact verification the model does NOT do automatically. See also `root_AGENT_ENVIRONMENT_ARCHITECTURE.md` §4.14 (verification-instruction discipline, surface-invariant).

**Deployment calibration.**
- Chat interface: MEDIUM (chat workloads are less verification-heavy)
- Claude Projects: MEDIUM
- Claude Code: HIGH (agentic workloads with verification scaffolding accumulated over prior model generations)
- API (agent workloads at effort ≥ high): HIGH

---

### Section 12: Scope expansion (Opus 5)

**What it looks like.** Opus 5 expands the scope of a task, adding steps that weren't requested or applying its own judgment about what the task should be. Distinct from #6 over-exploration — #6 is search breadth within a defined task; #12 is delivering beyond the task.

**Standard template (core rules for tightly-scoped Projects; output standards otherwise):**
```
<scope>
Deliver what was asked, at the scope intended. Make routine judgment calls
yourself, and check in only when different readings of the request would
lead to materially different work. If the request seems mistaken or a better
approach exists, say so in a sentence and continue with the task as asked
rather than quietly narrowing, widening, or transforming it. Finish the
whole task, and stop short of actions that are clearly beyond what was asked.
```

**Stronger variant (for CC deployments where scope expansion is a recurring failure):**
```
Complete only the requested task. Do not add steps, features, refactors, or
subsystems that were not asked for. If you believe a broader change is
warranted, describe it in one sentence at the end and let the operator decide
— do not proceed with it on your own judgment.
```

**Deployment calibration.**
- Chat interface: MEDIUM
- Claude Projects: MEDIUM
- Claude Code: HIGH (agentic sessions where the model can act on scope expansion by writing files, spawning subagents, etc.)
- API (agent workloads at effort ≥ high): HIGH

---

### Section 13: Subagent over-delegation (Opus 5)

**What it looks like.** Opus 5 delegates to subagents more readily than prior models. Delegation pays off on genuinely independent, sizeable tracks of work but multiplies cost and time when applied to small tasks. Also — a specific form: Opus 5 will spawn a subagent to "verify" its own work, which is a subagent instance of tendency #11.

**Standard template (CLAUDE.md core rules for CC deployments):**
```
<subagent_delegation>
Delegate to a subagent only for large tasks that are genuinely independent
and parallelizable, such as a wide multi-file investigation. Do not delegate
work you can finish yourself in a handful of tool calls, and do not use
subagents to verify or double-check your own work. If one subagent can
complete the task, use one rather than several, and keep spawn counts low.
</subagent_delegation>
```

**Stronger variant (for cost-sensitive deployments):**
```
Cap subagent spawns at [N] per session unless the operator explicitly
authorizes more. Every subagent spawn compounds cost; account for it before
delegating.
```

**Deployment calibration.**
- Chat interface: N/A (no subagent surface)
- Claude Projects: N/A (no subagent surface)
- Claude Code: HIGH (this is the primary subagent surface)
- API (multi-agent workloads): HIGH

---

### Section 14: Correction narration (Opus 5)

**What it looks like.** Opus 5 narrates corrections to its earlier statements more than prior models — including corrections that don't materially change the user's outcome.

**Standard template (output standards):**
```
<correction_policy>
Only correct an earlier statement when the error would change the user's
code, conclusions, or decisions. State corrections plainly and briefly, then
continue the task. For slips that change nothing for the user, make the fix
and move on without noting it.
</correction_policy>
```

**Deployment calibration.**
- Chat interface: MEDIUM (extended conversations accumulate corrections)
- Claude Projects: MEDIUM
- Claude Code: LOW (agentic sessions are largely action-driven; correction narration is a smaller share)
- API: LOW

---

## Prompt/environment-conditional defects (not tendencies)

Two failure modes track to the prompt or the runtime configuration rather than the model. They are handled by writing prompts differently or configuring the API differently, not by adding counter-tendency instructions.

### Conservative-instruction literalism

Opus 5 follows "only report high-severity issues" or "be conservative" literally, which causes under-reporting. This is a prompt defect exposed by the model, not a model tendency.

**Fix — rewrite to two-stage form.** Report everything, then filter in a separate pass.

Do NOT use:
```
Only report high-severity issues.
Be conservative in your findings.
```

Do use:
```
Report every issue you find, categorized by severity. In a separate pass at
the end, filter to [severity threshold] and list only those in the final
report. Include the full list in an appendix so the operator can review the
filtered items.
```

**Application surface.** Audit and review Skills specifically: project-audit, full-stack-audit, prompt-validation, global-audit, repo-hygiene, critic-gate. Sweep pattern for prompts that carry this defect: `only report`, `only flag`, `be conservative`, `high-severity` (as an instruction, not as an output label).

### Thinking-disabled output artifacts

With `thinking: {"type": "disabled"}` on Opus 5, two artifacts can occasionally appear in the model's visible output: tool calls as text (the model writes a tool call into user-facing text instead of emitting a structured `tool_use` block, and the call never runs), and internal XML tags (`<thinking>` tags or other internal tags leak into the visible response).

**Fix — keep thinking on and control cost via effort.** For most tasks, thinking-on at `low` effort outperforms thinking-off at similar cost.

**Sub-finding — do NOT add "do not think" instructions.** A system-prompt rule instructing Opus 5 not to think or not to reason INCREASES `<thinking>` tag leakage rather than suppressing it. If a mitigation instruction is required for integrations that must keep thinking disabled, use the general form:

```
<output_hygiene>
When you use a tool, you may say a brief sentence first. If no tool can
express what the user asked for, say so instead of guessing. Do not include
internal or system XML tags in your response.
</output_hygiene>
```

**Reminder — thinking-disabled breaking change on Opus 5.** `thinking: {"type": "disabled"}` is accepted only at effort `high` or below. Setting it at `xhigh` or `max` returns a 400 error.

---

*End of extended templates.*
