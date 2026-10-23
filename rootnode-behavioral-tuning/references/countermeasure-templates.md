# Extended Countermeasure Templates

Additional variants and placement patterns for the 15-tendency taxonomy documented in SKILL.md. Each section below supplements the base countermeasure with identity-level embeddings, output-standards integrations, stronger variants for severe cases, and combination guidance when multiple tendencies co-occur. Section numbers match the tendency numbers in SKILL.md. Updated for Opus 5.5 + Sonnet 5.5 dual-primary calibration (v5.0 alignment cycle). History: the v4.0 cycle (Opus 5 generation) refactored verbosity into a three-surface family (#3a conversational / #3b agentic narration / #3c written deliverables) and added #11 over-verification, #12 scope expansion, #13 subagent over-delegation, and #14 correction narration. The v5.0 cycle adds #15 early turn termination, adds 5.5-generation facets to #3c, #4, #5, #6, #7, #11, #12, and #13, and moves sections 11–14 out of the former addendum into first-class sections. Four prompt/environment-conditional defects are handled by rewriting prompts or harnesses, not by counter-instructions — see the appendix at the end.

Effort context for every deployment note below: the Claude Code default is `medium` on Opus 5.5 / Sonnet 5.5 / Haiku 5.5 (Fable 5.1: `high`); API defaults are Opus 5.5 `medium`, Sonnet 5.5 `high`, Fable 5.1 `high` (dated landscape block `root_MODEL_LANDSCAPE_2026-10`). Countermeasures that v4.0 excluded on the strength of `high`-effort mitigation are applied on observation at `medium`, not excluded by default. **Two countermeasure shapes run opposite to insertion.** #11 over-verification is fixed by REMOVAL of instructions (Section 11). #15 early turn termination is fixed first by raising effort, then by a turn-boundary block (Section 15). Anthropic-derived text is tagged `[Anthropic docs]`; untagged templates are rootnode-authored.

---

## Table of Contents

- [Section 1: Agreeableness bias](#section-1-agreeableness-bias) — 1a output-content + 1b persistent-preference variants
- [Section 2: Hedging](#section-2-hedging) — editorial-specific and output-level variants
- [Section 3: Verbosity — three-surface family](#section-3-verbosity--three-surface-family) — 3a conversational, 3b agentic narration, 3c written deliverables (+ Fable 5.1 facets)
- [Section 4: List overuse](#section-4-list-overuse) — prose-default variants; Fable 5.1 over-correction
- [Section 5: Fabricated precision](#section-5-fabricated-precision-external-fact) — external-fact variants; unmarked-quotation facet
- [Section 6: Over-exploration](#section-6-over-exploration) — search-breadth scope control; Opus 5.5 inverse note
- [Section 7: Tool trigger miscalibration](#section-7-tool-trigger-miscalibration) — 7a soft recalibration, 7b suppression removal + explicit enforcement
- [Section 8: LaTeX defaulting](#section-8-latex-defaulting) — plain-text defaults with rendering exception
- [Section 9: Editorial drift](#section-9-editorial-drift-new-in-47) — meta-content suppression, opening/closing framing
- [Section 10: Self-referential fabrication](#section-10-self-referential-fabrication-new-in-47) — universal, Project-level, User Preferences variants
- [Section 11: Over-verification (REMOVAL shape)](#section-11-over-verification-removal-shape) — sweep patterns to remove; preservation patterns to keep
- [Section 12: Scope expansion](#section-12-scope-expansion) — scope-constraint templates; unrequested additions
- [Section 13: Subagent over-delegation](#section-13-subagent-over-delegation) — reviewer-launch block; delegation caps for CC and API agent surfaces
- [Section 14: Correction narration](#section-14-correction-narration) — restrict corrections to material ones
- [Section 15: Early turn termination](#section-15-early-turn-termination) — effort first; default block; unattended variant; harness complement
- [Worked examples](#worked-examples)
- [Combining multiple countermeasures](#combining-multiple-countermeasures)
- [Deployment-context checklist](#deployment-context-checklist)
- [Language Calibration](#language-calibration)
- [Prompt/environment-conditional defects (not tendencies)](#promptenvironment-conditional-defects-not-tendencies) — conservative-review literalism, thinking-disabled artifacts, mid-turn injection misread, reasoning-extraction refusal

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

## Section 3: Verbosity — three-surface family

What was a single tendency through v3 is three surfaces with distinct triggers and countermeasures (refactored in the v4.0 cycle). Identify WHICH surface exhibits verbosity before applying a template: chat outputs → 3a; Claude Code / agent tool-use narration → 3b; report or document files → 3c. Applying #3a to an agentic workload leaves #3b unaddressed and vice versa.

### 3a — Conversational response length

Default user-facing responses run longer than needed. Effort does NOT reliably shorten them (effort controls thinking, not visible output). Prompt for length explicitly.

**Standard template (4.7-calibrated, softer than pre-4.7):**
```
Match response length to question complexity. For simple factual
questions, a sentence is sufficient. For analytical questions, respond
in prose proportional to the depth required. Do not restate the question.
Do not pad with transitional framing that adds no content.
```

**Concise-default variant** (output standards; from the v4.0 cycle):
```
Keep responses focused, brief, and concise. Keep disclaimers and caveats short,
and spend most of the response on the main answer. When asked to explain
something, give a high-level summary unless an in-depth explanation is
specifically requested.
```

**Long-system-prompt reinforcement** (paired with the main template, near the end):
```
<tone_preference>Keep outputs reasonably concise.</tone_preference>
```

**Length-targeted variant** (for Projects with a specific length norm):
```
Responses target [N] paragraphs for analytical questions and [M]
sentences for factual ones. Exceed the target only when the complexity
genuinely requires it; flag the overage at the top of the response if so.
```

**Reverse-problem variant** (when the model over-corrects toward terseness):
```
Ensure analytical responses include the reasoning steps, not just the
conclusion. A terse conclusion without supporting analysis is incomplete
for a question that requires analysis. Prefer completeness over brevity
when the question's complexity requires it.
```

The reverse problem has been more common since 4.7. Check which direction the Project's output actually fails before applying a standard or reverse variant.

### 3b — Agentic progress narration

The model narrates readily during agentic work — announcing what it is about to do, with long per-message output. Describe the cadence and shape you want (positive examples beat prohibitions).

**Standard template (core rules / agentic-context section):**
```
<agentic_communication>
Before your first tool call, say in one sentence what you're about to do.
While working, give a brief update only when you find something important
or change direction. When you finish, lead with the outcome: your first
sentence should answer "what happened" or "what did you find," with
supporting detail after it for readers who want it.
</agentic_communication>
```

### 3c — Written-deliverable length

Files the model writes to disk (reports, Markdown documents, summaries) are often longer than the content needs. Separate from conversational verbosity.

**Standard template (output standards or document-generation prompt):**
```
<document_length>
Match the length of written documents to what the task needs: cover the
substance, but do not pad with filler sections, redundant summaries, or
boilerplate.
</document_length>
```

**Facet — whole-file rewrites for small edits (Fable 5.1; token cost, not quality).** Fable 5.1 tends to rewrite an entire file for a small change. Add the Fable 5.1 guide's instruction to "surgically edit a file rather than rewrite the entire thing" `[Anthropic docs]` to the coding or file-editing section of the prompt. CC-relevant.

**Facet — drafting twice at `xhigh`/`max` (Fable 5.1; effort-conditioned).** At `xhigh`/`max`, Fable 5.1 may draft the deliverable in thinking and then write it again in the reply. First lever: prefer `high`. For prose that still reads padded, "remove all mannered prose" `[Anthropic docs]` targets density, not length; do not stack a v4.0-era anti-formatting rule on top (Section 4). Where `xhigh`/`max` is needed, add the max_tokens-aware block (replace `[max_tokens]` with the deployment's limit) `[Anthropic docs — Prompting Claude Fable 5.1, fetched 2026-10-22]`:
```text
Everything produced in one reply, including any reasoning or drafting done before the reply, counts toward a single limit of about [max_tokens] tokens. If that limit is reached before the reply is finished, the person receives a cut-off response and has to start over. Composing an entire output or deliverable in full as reasoning and then again as a reply would double the length of the turn without improving the result, so don't do that.

Instead, when the person has asked for a long or effort-intensive deliverable such as a multi-section document, a large table or dataset, or a complete code file, spend extra effort on understanding the request, checking the inputs the answer depends on, settling the structure and other difficult decisions, and otherwise using the reasoning space to reason and the output space to write an output. Usually it is not needed to draft an output multiple times.
```

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

**Over-correction warning (Fable 5.1).** Fable 5.1 formats less (less bold, fewer headers and lists) and writes denser prose by default. The two templates above — and any v4.0-era anti-formatting rule in an existing prompt — can now suppress structure the content needs. On Fable 5.1, remove blanket anti-list rules and use the conditional formulation instead: "use lists… when the content is multifaceted enough that they help; plain prose in conversational exchanges" `[Anthropic docs]`. Apply the standard template only where list overuse is actually observed on the model in use.

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

**Facet — unmarked quotations (Fable 5.1).** Fable 5.1 summaries can reproduce source passages without quotation marks, so source wording reads as the model's own. The fix the Fable 5.1 guide documents is one complete worked example in the system prompt, plus a marked-quotation rule in the Output layer. The shape below is rootnode-authored; fill the brackets from the deployment's own sources.

**Output-layer rule:**
```
When your response reuses wording from a source, put the reused words in
quotation marks and name the source. Paraphrase everything else in your
own words.
```

**Worked-example shape** (one complete example in the system prompt — request, correct response, rationale):
```
<example>
Request: Summarize [source document] for [audience].
Correct response: [Summary in the model's own words, with any reused
source phrase in quotation marks and attributed, e.g., The report calls
the change "[exact phrase from source]" ([source name]).]
Why this is correct: reused wording is marked and attributed; everything
unmarked is paraphrase.
</example>
```

---

## Section 6: Over-exploration

#6 is search breadth within a task. Delivering beyond the task (unrequested features, files, tests) is #12. **Standard template (4.7-calibrated, softer):**
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

**Inverse note — Opus 5.5 multi-app workflows.** The Opus 5.5 guide documents the opposite failure: in multi-app workflows Opus 5.5 "tends to get to work quickly" `[Anthropic docs]` — it under-explores. Keep the #6 templates above for `xhigh`/`max` runs where excess breadth is observed, and never apply both directions to one deployment. On multi-app tasks the countermeasure runs the other way — because it tells the model to act on what it finds, keep untrusted content out of the records it searches `[Anthropic docs — Prompting Claude Opus 5.5, fetched 2026-10-22]`:
```text
Before taking any action, explore broadly with tool calls: list and open the emails, documents, spreadsheet tabs and records across the available apps that could be relevant to this task, including ones the task does not explicitly mention, and use what you find.
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

**5.5-generation caution.** This template is tool-discouraging language. The Sonnet 5.5, Haiku 5.5, and Fable 5.1 guides document that such language now causes under-search (7b). Apply 7a only on observed over-triggering, scoped to the tool that over-fires. Claude Code likelihood: LOW.

### 7b — Under-triggering (NEW in 4.7; fix direction flipped on the 5.5 generation)

Two drivers. In chat, persistent-context instructions are weighted lower than immediate prompts, so a required tool is skipped. On Sonnet 5.5, Haiku 5.5, and Fable 5.1, tool-suppressing language carried over from older prompts causes under-search, and at `low` effort the model answers from memory. The v4.0-era fix direction ("stop over-calling") is now usually the wrong one.

**Step 1 — remove suppression.** "First, check your prompt for language that discourages tool use, such as "only use tools when strictly necessary" or "minimize tool calls," and remove it." `[Anthropic docs]` **Step 2 — search nudge** `[Anthropic docs — Sonnet 5.5 guide]`:
```text
Use the search tool to check specifics that may have changed since your training, such as what is allowed, required or charged, even when you feel confident. For researched work such as a report or a comparison, gather current sources rather than writing from your training knowledge.
```

**Step 3 — model-specific additions.** Haiku 5.5: give the current date in the system prompt. Do NOT add blanket "always search" instructions — per the Haiku 5.5 guide, a blanket instruction made the model search on about half of the prompts that needed no search, with no accuracy gain. Fable 5.1 at `low`: raise effort for the affected turns, or add the name-verification nudge `[Anthropic docs — Prompting Claude Fable 5.1, fetched 2026-10-22]`:
```text
When a query centers on a name you do not confidently recognize, or recognize from a fast-moving area like AI models and developer tools where the landscape shifts within months, the name itself is the thing to verify: search before answering, and include the name as the user wrote it in at least one query alongside any reformulations. This holds even when you have some background on it — partial background is exactly what makes an out-of-date answer sound authoritative, so familiarity is not a reason to skip the search.
```

**Step 4 — explicit enforcement** (chat Preferences or CI that name a required tool):
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

**Placement guidance:** Explicit enforcement is the one current-era context where emphatic language (MUST) is the right answer — it is scoped to a named tool and task type, which is what separates it from a blanket "always search" rule.

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

**Note on deployment:** Editorial drift is primarily a chat-interface phenomenon at Adaptive effort. v4.0 treated Claude Code and API at `high` and above as exhibiting it much less; at the Claude Code `medium` default (Opus 5.5 / Sonnet 5.5 / Haiku 5.5) that mitigation is weaker. Apply the countermeasure on observation rather than excluding it by default.

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

## Section 11: Over-verification (REMOVAL shape)

**What it looks like** (added in the v4.0 cycle; extended in v5.0). The model verifies its own work automatically. Prompts and CLAUDE.md files that accumulated "double-check your answer," "re-verify before responding," "include a final verification step," or "use a subagent to verify" instructions across model generations now compound with that automatic behavior — token spend without a quality gain. On the 5.5 generation the same applies to thinking instructions: "think carefully before answering" and "re-verify earlier answers" lines in chat system prompts are removal targets, and effort is the control (Opus 5.5 guide). Prompt-level think-less instructions do not work either: "Asking it in the system prompt to think less doesn't reliably reduce its thinking." `[Anthropic docs — Sonnet 5.5 guide]` — lower effort instead. **Effort-conditioned facet:** at `xhigh`/`max`, Sonnet 5.5 starts its own review and hardening rounds — counter it with the review-round block in Section 13, which covers both review rounds and reviewer-subagent launches.

**Countermeasure shape — REMOVAL.** Audit and delete matching self-directed re-check instructions; do not insert a counter-tendency template. Encoded as a sweep specification rather than a block to add.

**Match patterns to REMOVE (self-directed re-checking and think-harder lines).** Case-insensitive, allow reasonable phrasing variation around each core pattern:

```
double-check your (answer|response|work|reasoning|output)
re-verify (before responding|before answering|the answer|the response|earlier answers)
include a final verification step
use a subagent to verify (your|the|its) (own )?(work|output|answer|reasoning)
before presenting your final answer, verify your reasoning
check your (answer|work|reasoning) (again|carefully|thoroughly)
think (carefully|step by step) before (answering|responding)
```

**Match patterns to PRESERVE (external-artifact verification).** These describe checking a claim against a source outside the model's own output. The model does NOT do this automatically — keep the instructions and keep them imperative:

```
verify the file exists (at the path claimed)
check the rendered page — a stored-body assert is not proof of clean render
diff the artifact against the source
confirm the tag resolves against actual repo state
run the tests and verify they pass
grep for the symbol to confirm it exists before recommending it
```

**Preservation-class template for code tasks.** Any pattern where "verify" or "check" refers to a specific external source (file, page, test output, source-of-truth) is preservation-class. The block below is an external-verification instruction (AEA §4.14 keep class), not a self-verification instruction; a D7 self-verification scan must not flag it. Relevant where Sonnet 5.5 at `low` and Haiku 5.5 at `low`/`medium` report a change done without running a real check `[Anthropic docs — Sonnet 5.5 guide]`:
```text
When you change code that can be run, built, or type-checked, run a real check that exercises the change before reporting it done: the project's tests, type-checker, or build, or the changed command itself. A syntax-only check, or a check command that failed to start, does not count; if all that is missing is the project's declared dependencies, install them with its own package manager and lockfile (e.g. npm install, pip install -r requirements.txt), never via sudo or the system package manager, unless told not to. Only if no real check can run here, say which one you did not run and why instead of reporting the change as done.
```

**Sweep procedure.**
1. Grep the prompt / CLAUDE.md / Skill for the REMOVE patterns above (case-insensitive).
2. Classify each hit per-instance: unambiguous self-re-check or think-harder line → REMOVE the line/sentence; unambiguous external-artifact → KEEP and confirm imperative voice; ambiguous → flag for review, do not batch-apply.
3. For each REMOVE hit, delete the sentence or bullet. Do not add a replacement — the removal IS the countermeasure.
4. For each ambiguous hit, decide per-instance whether the intent is self-re-check or external-artifact. Ambiguous phrasings often include: "verify" without an explicit object; "review your output"; "sanity-check"; "double-check" when the target is a file/artifact rather than the model's own reasoning.

**Rationale.** From Anthropic's Opus 5 prompting guide (v4.0 cycle): "instructions like these cause over-verification on Claude Opus 5, and removing them reduces wasted tokens with no loss in quality." `[Anthropic docs]` The 5.5-generation guides extend the removal to thinking instructions. The Skill's role is to guide the removal audit and to preserve external-artifact verification the model does NOT do automatically. See also `root_AGENT_ENVIRONMENT_ARCHITECTURE.md` §4.14 (verification-instruction discipline, surface-invariant).

**Optional chat-only line** `[Anthropic docs — Prompting Claude Opus 5.5, fetched 2026-10-22]` — chat only; leave it out of long analyses and agentic tasks, where a later step can reveal an earlier mistake; it may make the model less likely to volunteer a mistake in an earlier answer, so test before adopting:
```text
Once you have answered something, treat that answer as done. On later turns, focus your thinking on what the user is asking now, and don't go back over an earlier answer unless the user asks about it or points out a problem with it.
```

**Deployment calibration.** Chat interface: MEDIUM (chat workloads are less verification-heavy) · Claude Projects: MEDIUM · Claude Code (`medium` default on Opus 5.5 / Sonnet 5.5 / Haiku 5.5): HIGH (agentic workloads with verification scaffolding accumulated over prior model generations) · API (agent workloads at effort ≥ high): HIGH.

---

## Section 12: Scope expansion

**What it looks like** (added in the v4.0 cycle; extended in v5.0). The model expands the scope of a task, adding steps that weren't requested or applying its own judgment about what the task should be. Distinct from #6 over-exploration — #6 is search breadth within a defined task; #12 is delivering beyond the task. The opposite of #15 (too little). **Facet — unrequested additions (Sonnet 5.5, Haiku 5.5, Fable 5.1):** Tests, docs, refactors, and small supporting files that fit the repo's conventions, at every effort level and more at higher effort. Open-ended "show me what you can do" requests get built rather than answered.

**Default template** `[Anthropic docs — Sonnet 5.5 guide]` — the second paragraph of the #15 default block. Ship it with the first paragraph (Section 15): a prompt that only says "keep working" invites scope expansion, and a prompt that only says "don't add" invites early stops. Turn-boundary instruction, not a self-verification instruction (AEA §4.14 keep class) — a D7 self-verification scan must not flag it.
```text
When the work the user asked for is done and checked, stop and report. Don't add features, tests, files, docs or refactors that weren't asked for. If you think one would help, mention it at the end instead of doing it.
```

**Open-ended requests** `[Anthropic docs — Sonnet 5.5 guide]`:
```text
When the user asks for ideas, options or a plan, give them that and stop. Don't start building or changing anything until they say to go ahead.
```

**Coding — pre-existing bugs and extras (Fable 5.1)** `[Anthropic docs — Prompting Claude Fable 5.1, fetched 2026-10-22]` — report a pre-existing bug as a follow-up rather than fixing it in the current change:
```text
If, while working or testing, you find a pre-existing bug, a performance concern, or behavior the task doesn't mention, don't fix, optimize or extend it in this change unless the requested behavior cannot work without it; report it as a follow-up in your summary. Where the task is ambiguous, implement the reading its wording and the surrounding code most directly support, state that assumption in your summary, and don't build for the other readings as well. Verify your work however you like; scratch scripts and quick checks need not be kept. Commit tests only where the task asks for them or this repository already keeps tests for this kind of change, sized like the neighboring test files — roughly one focused test per stated behavior — and don't turn scratch checks into additional permanent test files. This is about extras only: implement every behavior the task asks for, completely.
```

**Scope template (v4.0; core rules for tightly-scoped Projects, output standards otherwise):**
```
<scope>
Deliver what was asked, at the scope intended. Make routine judgment calls
yourself, and check in only when different readings of the request would
lead to materially different work. If the request seems mistaken or a better
approach exists, say so in a sentence and continue with the task as asked
rather than quietly narrowing, widening, or transforming it. Finish the
whole task, and stop short of actions that are clearly beyond what was asked.
</scope>
```

**Stronger variant (for CC deployments where scope expansion is a recurring failure):**
```
Complete only the requested task. Do not add steps, features, refactors, or
subsystems that were not asked for. If you believe a broader change is
warranted, describe it in one sentence at the end and let the operator decide
— do not proceed with it on your own judgment.
```

**Deployment calibration.** Chat interface: MEDIUM · Claude Projects: MEDIUM · Claude Code (`medium` default on Opus 5.5 / Sonnet 5.5 / Haiku 5.5): HIGH (agentic sessions where the model can act on scope expansion by writing files, spawning subagents, etc.) · API (agent workloads at effort ≥ high): HIGH.

---

## Section 13: Subagent over-delegation

**What it looks like** (added in the v4.0 cycle; extended in v5.0). The model delegates to subagents more readily than earlier generations. Delegation pays off on genuinely independent, sizeable tracks of work but multiplies cost and time when applied to small tasks. A specific form: spawning a subagent to "verify" its own work, which is a subagent instance of tendency #11. **Effort-conditioned facet (Sonnet 5.5):** At `xhigh`/`max`, Sonnet 5.5 launches reviewer subagents on its own. The guide reports that the paragraph below "stopped reviewer subagent launches and cut session cost by about a third, with no change in quality" `[Anthropic docs]`.

**First-line countermeasure** `[Anthropic docs — Sonnet 5.5 guide]` — apply before any cap mechanism:
```text
When the work the user asked for is done and its checks pass, stop and report. Don't start extra rounds of review or hardening on your own, and don't launch reviewer sub-agents unless the user asked for a review. If you think a deeper review is worth doing, say so at the end.
```

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

**Mechanism (Claude Code).** Dated product facts — verify every name and default on the running Claude Code version before relying on it:
- Subagent model: per-invocation `model` → definition `model` frontmatter (`inherit` selects the main model) → `CLAUDE_CODE_SUBAGENT_MODEL` → main conversation's model; `CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1` overrides all `[v2.1.257+ — verify on running version]`. Haiku 5.5 is positioned for subagent tasks — route small tracks to it instead of letting every subagent inherit the main model.
- `CLAUDE_CODE_WORKFLOW_SUBAGENT_MODEL` runs every workflow agent on one model `[v2.1.296+ — verify on running version]`.
- Agent tool `effort` parameter sets a subagent's effort per invocation `[v2.1.292+ — verify on running version]`.
- `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` (default 20) `[v2.1.217+ — verify on running version]`; `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` (default 3; `1` turns nesting off) `[verify on running version]`.

**Deployment calibration.** Chat interface: N/A (no subagent surface) · Claude Projects: N/A (no subagent surface) · Claude Code (`medium` default on Opus 5.5 / Sonnet 5.5 / Haiku 5.5): HIGH (this is the primary subagent surface) · API (multi-agent workloads): HIGH.

---

## Section 14: Correction narration

**What it looks like** (added in the v4.0 cycle). The model narrates corrections to its earlier statements more than earlier generations — including corrections that don't materially change the user's outcome.

**Standard template (output standards):**
```
<correction_policy>
Only correct an earlier statement when the error would change the user's
code, conclusions, or decisions. State corrections plainly and briefly, then
continue the task. For slips that change nothing for the user, make the fix
and move on without noting it.
</correction_policy>
```

**Deployment calibration.** Chat interface: MEDIUM (extended conversations accumulate corrections) · Claude Projects: MEDIUM · Claude Code (`medium` default on Opus 5.5 / Sonnet 5.5 / Haiku 5.5): LOW (agentic sessions are largely action-driven; correction narration is a smaller share) · API: LOW.

---

## Section 15: Early turn termination

**What it looks like** (added in the v5.0 cycle). The model ends its turn while work it was asked for is still owed: a summary that closes by announcing the next step, with no tool call; an offer to continue "unless you'd prefer otherwise"; a list of decisions for the user when none of them blocks the remaining work; a report because the turn has been long or a milestone is done; at low effort, pausing to confirm a plan or asking a question it could answer itself; in long agent prompts, handing the task back. Distinct from #12 scope expansion (the model does too much) and #6 over-exploration (search breadth within a task). #15 is too little, and its countermeasure runs in the opposite direction from #12's — which is why it is a separate tendency, not a #12 facet.

**Warrant.** Documented with a prompt-level countermeasure in all four current Anthropic prompting guides: Opus 5.5 ("Unattended agentic runs"), Sonnet 5.5 ("Carrying work through" at `low`/`medium`), Haiku 5.5 ("Early stopping" — raising `low` → `medium` "roughly halved early stopping" `[Anthropic docs]`), and Fable 5.1 ("Finishing the whole task").

**Deployment calibration** (D9c analytical from the guides; not measured): Chat interface (default effort): LOW — a chat turn is supposed to end · Claude Code (`medium` default on Opus 5.5 / Sonnet 5.5 / Haiku 5.5): MEDIUM at `medium`, HIGH at `low`; LOW at `high` and above; long system prompts raise it (Haiku 5.5 guide) · API agentic (developer-controlled effort): as Claude Code by effort level; HIGH for fully unattended loops with no harness continuation · Cowork / scheduled runs: HIGH — no operator present to send the continuation.

**Label for scanners.** Every template in this section is a turn-boundary instruction, not a self-verification instruction (AEA §4.14 keep class). It governs when a turn ends, not whether the model re-checks its work. A D7 self-verification scan must not flag it.

**Lever 1 — effort.** At `low`/`medium`, try raising effort before adding a block. The Sonnet 5.5 guide notes the block lengthens output and costs more at low effort. Raising Haiku 5.5 from `low` to `medium` "roughly halved early stopping" `[Anthropic docs]`.

**Lever 2 — default block (Sonnet 5.5 / Haiku 5.5 guides).** `[Anthropic docs — Sonnet 5.5 guide]` — place in core rules. The second paragraph is the #12 countermeasure; the two ship together because a prompt that only says "keep working" invites scope expansion.
```text
Keep working until everything the user asked for is done, and only stop to ask when you can't go on without the user or before a risky step.

When the work the user asked for is done and checked, stop and report. Don't add features, tests, files, docs or refactors that weren't asked for. If you think one would help, mention it at the end instead of doing it.
```

**Lever 3 — fully-unattended variant (Opus 5.5 guide).** For loops with no human in the turn `[Anthropic docs — Prompting Claude Opus 5.5, fetched 2026-10-22]`. Turn-boundary instruction (AEA §4.14 keep class). Place at the end of the system prompt from the first request (adding it mid-session changes `system`); not for human-in-the-loop applications; keep your own confirmation step for risky actions; set `thinking.display: "updates"` to receive the status notes:
```text
A standing instruction from the user, the person you are working for. It is about how your turns end. A message with no tool call in it ends your turn, and the work stops there until you are asked to continue. The user has seen you end turns in four ways while work they asked for was still owed, and does not want any of them. One: a long summary of what was done that closes by announcing the next step and has no tool call, so the next thing never starts. Two: an offer to carry on with something unless the user would prefer otherwise, which stops to wait for an answer the user was not going to give. Three: a list of decisions for the user when, by your own account, none of them blocks the rest of the work. Four: deciding that this is a good place to report, because the turn has been long or a milestone is done. Status notes are welcome, and so are your recommendations on open decisions, but put them in the same message as your next tool call and carry on with whatever does not depend on the user's answer. If you notice yourself inviting the user to redirect you or offering to wait, delete it and do the next thing. The stops the user does want are the ones where nothing can move without them, or where the thing blocking you is deliberately protected from you. This does not override the need for confirmation on risky or destructive actions.
```

**Lever 4 — harness complement.** The harness, not the prompt, decides whether a turn that ended is actually finished:
- Treat a text-only end of turn "as a report rather than as proof the task is done" `[Anthropic docs — Opus 5.5 guide]`.
- When open items remain, send a continuation message naming them. Cap continuations at two or three per task.
- If something the model started is still running (a background command, a subagent), the task is not done — wait, and return its output as the next user message.

---

## Worked examples

### Example 1: Symptom-to-tendency routing

**Input:** "Claude keeps adding disclaimers about what it will and won't do, even when my preferences say to be direct."

**Actions:**
1. Match the symptom: "adds unsolicited boundary commentary" maps to #9 (editorial drift).
2. Secondary match: "ignores my preferences" suggests co-occurring #1b (persistent-preference dilution).
3. Confirm deployment context — which surface is this (chat, Projects, Claude Code, API)?
4. Apply the #9 countermeasure primary; add the #1b countermeasure if context is chat or Projects with long conversations.

**Result:** Two countermeasure templates with placement guidance, plus the deployment calibration note that chat-interface deployment is HIGH risk for both.

### Example 2: Self-referential fabrication

**Input:** "I asked Claude to check something and it said it had searched, but I don't think it actually did."

**Actions:**
1. Match the symptom: "says it searched but didn't" maps to #10 (self-referential fabrication).
2. Confirm deployment context — Claude.ai GUI has tool indicators; API does not. Different verification methods.
3. Apply the full #10 countermeasure template.
4. Recommend verification method based on surface (GUI "Searched the web" indicator vs. API response inspection).

### Example 3: Deployment context disambiguation

**Input:** "Claude is too verbose."

**Actions:**
1. Match the symptom: #3 (verbosity drift). Identify the surface — chat replies (3a), agent narration (3b), or files written to disk (3c).
2. Deployment context not stated — before applying the countermeasure, confirm: chat? Projects? Claude Code? API?
3. Upon answer, apply the calibrated countermeasure. On Claude Code (`medium` default on Opus 5.5 / Sonnet 5.5 / Haiku 5.5), conversational verbosity is LOW — check first whether verbosity is actually observed, and on which surface.

### Example 4: Early turn termination vs. scope expansion

**Input:** "My Claude Code agent writes a nice summary that ends with 'Next I'll update the tests' — and then stops."

**Actions:**
1. Match the symptom: summary-plus-next-step with no tool call maps to #15 (early turn termination), not #12 (that would be doing too much).
2. Confirm the effort level and whether the run is attended. At `low`/`medium`, raise effort first.
3. If the stops persist, add the Section 15 default block — both paragraphs, so the fix for #15 does not open #12; for unattended runs, add the harness continuation (capped at two or three) and consider the Opus 5.5 fully-unattended variant.

---

## Combining multiple countermeasures

### Limits

A system prompt or Project CI can carry countermeasures for multiple tendencies simultaneously, but there are limits:

- More than 4-5 countermeasures in a single CI dilutes attention — each individual rule is weighted lower.
- Countermeasures that pull in opposite directions (aggressive concision + complete reasoning; "keep working" without "don't add") fight each other or open the opposite failure. Choose which direction the Project needs, and pair #15 with #12.
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

One paragraph with multiple specific rules reads with continuous attention. Five separate rules in sequence read with declining attention. (On Fable 5.1, drop the "not bullet points" clause in favor of the conditional formulation in Section 4.)

### Placement priority

When multiple countermeasures compete for high-attention position:

1. **Identity block** — countermeasures that define how the model approaches every task (agreeableness 1a, evidence discipline for self-referential fabrication if the Project is audit-shaped)
2. **Core rules, top** — countermeasures for persistent-preference dilution (1b) and tool under-triggering (7b) in chat interface deployments
3. **Core rules, body** — most other countermeasures, including the #15/#12 default block in agentic deployments
4. **Output standards** — formatting countermeasures (list overuse, verbosity, LaTeX) and editorial drift
5. **End of system prompt** — the #15 fully-unattended variant only

Placing a persistent-preference-dilution countermeasure in output standards defeats its purpose. Placing a formatting countermeasure in the identity block wastes identity-block attention on something the output-standards layer handles well.

---

## Deployment-context checklist

Before finalizing a countermeasure package, walk through this checklist:

- Is the deployment context confirmed? (chat / Projects / Claude Code / API)
- For chat interface deployments: are 1b, 7b, 9, 10 countermeasures included if their tendencies are observed?
- For Projects: are 1b and 9 countermeasures included if long-conversation patterns exist?
- For Claude Code (`medium` default on Opus 5.5 / Sonnet 5.5 / Haiku 5.5): v4.0 excluded countermeasures for 5, 6, 7a, and 9 on the strength of `high`-effort mitigation. At the `medium` default that mitigation is weaker — apply them on observation rather than excluding them by default. Are 11, 12, 13, and 15 addressed for agentic runs?
- For API: has the effort level been surfaced? Defaults differ — Opus 5.5 `medium`, Sonnet 5.5 `high`, Fable 5.1 `high`. `low`/`medium` are legitimate primary cost controls where evals show quality holds, but 7b and 15 rise there; raising effort is the first lever for both. Do not carry effort settings over from earlier generations without re-running an effort sweep.
- Has tool-suppressing language from older prompts been removed (7b), and have think-harder / re-verify lines been removed (11)?
- Is emphatic language (MUST / ALWAYS / NEVER) used only for tendency #7b?
- Does the countermeasure set fit within 4-5 rules, or has consolidation been applied?

---

## Language Calibration

Countermeasure language design affects compliance. Research (Meincke et al. 2025, N=28,000) found persuasion techniques — authority, commitment, and scarcity framing — more than doubled LLM behavioral compliance rates (33% → 72%, p < .001). For discipline-enforcing countermeasures (tendencies #1 agreeableness, #5 fabricated precision, #7b tool under-triggering, #10 self-referential fabrication, #12 scope expansion), use imperative framing: direct commands with authority and commitment anchors (e.g., "Run the verification command. Read the output. THEN claim the result."). For overcorrection-risk tendencies (#3a/#3b/#3c verbosity family, #6 over-exploration), use calibrated framing that sets boundaries without triggering compensatory extremes. For **#11 over-verification, the language is REMOVAL** — do not add counter-tendency instructions; audit and delete existing self-directed re-check instructions (§11 sweep patterns). For **#15 early turn termination, use Anthropic's block as written** — do not intensify it; raise effort first. See `root_OPTIMIZATION_REFERENCE.md` §"Behavioral Tendencies and Countermeasures" — "Note on countermeasure language design" for full reasoning and citation.

---

## Prompt/environment-conditional defects (not tendencies)

Four failure modes track to the prompt, the harness, or the runtime configuration rather than the model. They are handled by writing prompts differently or configuring the API or harness differently, not by adding counter-tendency instructions.

### Conservative-review literalism

Carried from the Opus 5 generation (not re-documented for 5.5). The model follows "only report high-severity issues" or "be conservative" literally, which causes under-reporting. This is a prompt defect exposed by the model, not a model tendency.

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

### Thinking-disabled output artifacts (narrowed in v5.0)

Thinking cannot be disabled on Opus 5.5, Sonnet 5.5, or Fable 5.1. The artifacts — reasoning leaking into visible text, tool calls written as text instead of a structured `tool_use` block, internal XML tags in the response — are now documented only on Haiku 5.5 at `low` effort or with thinking off, and on Sonnet 5.5 at `between_tools` when a "don't think" instruction is left in the prompt. **Fix:** use adaptive thinking at `medium` and control cost through effort. Remove any "do not think" line.

**Sub-finding (stands from v4.0) — do NOT add "do not think" instructions.** A system-prompt rule telling the model not to think or not to reason INCREASES `<thinking>` tag leakage rather than suppressing it. If an integration must keep Haiku 5.5 thinking disabled and needs a mitigation instruction, use the general form:

```
<output_hygiene>
When you use a tool, you may say a brief sentence first. If no tool can
express what the user asked for, say so instead of guessing. Do not include
internal or system XML tags in your response.
</output_hygiene>
```

**API rule.** `thinking: {"type": "disabled"}` is accepted only on Haiku 5.5, at effort `high` or below. On Opus 5.5, Sonnet 5.5, and Fable 5.1 it returns 400; Sonnet 5.5's floor is `between_tools` (at `high` or below).

### Mid-turn user text misread as injection (NEW in v5.0)

Sonnet 5.5 and Haiku 5.5 treat user text placed inside `tool_result` blocks, per-step harness notices, and token countdowns as possible prompt injection, and may ignore them. Symptom: "Claude ignores messages I send while it's working." Harness design detail lives in `rootnode-domain-agentic-context` (if available); this Skill carries the symptom row.

**Fix — harness, not prompt** `[Anthropic docs — Sonnet 5.5 guide]`:
- Never put user text inside a `tool_result` block. The model misreads that placement most often.
- Deliver mid-turn user input as a user turn. Append the user's words as a text block in the user message that carries the `tool_result` blocks, after the last `tool_result`.
- Keep harness notices, such as reminders, in a separate mid-conversation system message after the user's words. Never put a notice and the user's words in the same block.
- In interactive sessions where users can type mid-turn, don't add your own token or budget countdown after tool results.

### Reasoning-extraction refusal (NEW in v5.0)

On all four current models, prompts that ask the model to reproduce its internal reasoning in the response can be declined with `stop_reason: "refusal"`, category `reasoning_extraction`. Symptom: "Claude refuses when I ask it to show its reasoning." **Fix** `[Anthropic docs — Sonnet 5.5 guide]`: "If your prompts ask the model to include its reasoning in the response, remove those instructions, because they invite `reasoning_extraction` declines. With adaptive thinking, read the reasoning from summarized thinking blocks instead (`display: "summarized"`). You can still ask for a short explanation of the answer or a summary of the actions taken"

---

*End of extended templates.*
