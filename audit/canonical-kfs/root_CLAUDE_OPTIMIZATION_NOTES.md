# Claude-Specific Optimization Notes

A practical reference for writing prompts and building Projects optimized for how Claude actually works. Calibrated for Claude Opus 5 and Sonnet 5 (dual-primary), with Fable 5 integrated-aware for long-horizon agent workloads, Opus 4.8 fallback-graceful (users are silently served it on classifier-flagged requests), Sonnet 4.6 legacy-graceful, and Haiku 4.5 graceful-with-extended-thinking. Consult this document whenever building or refining prompts. The 5-Generation Landscape (Section 3) is the reference for model-fact statements; sections below refer to it rather than re-stating landscape facts inline.

**Calibration scope:** Opus 5 + Sonnet 5 **dual-primary**; Fable 5 **integrated-aware** (long-horizon agent workloads where its edge is worth $10/$50); Opus 4.8 **fallback-graceful** (a model users are *silently served* on classifier-flagged requests in Claude.ai, Claude Code, and Cowork — Skills must produce correct-shape output there without user awareness); Sonnet 4.6 **legacy-graceful**; Haiku 4.5 **graceful-with-extended-thinking**. Haiku 4.5 without extended thinking and Haiku 3.5 are out of scope. Mythos 5 and Mythos Preview are out of scope (invitation-only under Project Glasswing). When this document discusses model behavior without qualification, it refers to Opus 5. Where Opus 5 and Sonnet 5 diverge, both are documented; where Sonnet 5 behavior is not documented by Anthropic, the column reads "no delta documented" rather than inheriting a value from Sonnet 4.6.

**Effort-level note (inverted from 4.7/4.8 rule):** Opus 5 and Sonnet 5 both default to `high` effort on the Claude API and Claude Code. Anthropic's guidance is to **start at `high` (the default) and adjust based on evals** — step up to `xhigh` for demanding coding and agentic work, use `max` when a task justifies unconstrained spend, and use `low`/`medium` liberally as the primary cost/latency control wherever quality holds. This is the inverse of the 4.7/4.8 rule, which said "start at `xhigh` for coding and agentic." Do not carry effort settings over from prior models — re-run an effort sweep against your evals. On Opus 5, `thinking: {"type": "disabled"}` is accepted only at effort `high` or below; at `xhigh` or `max` it returns 400.

---

## 1. Structural Formatting That Claude Responds To

### XML Tags Are Claude's Native Structure

Claude was trained to attend strongly to XML tags. Use them to delineate sections of your prompt clearly. This is the single most impactful Claude-specific technique.

```xml
<role>
You are a senior data engineer specializing in pipeline architecture.
</role>

<context>
We are migrating from a monolithic ETL system to event-driven microservices.
The current system processes 2M records/day with a 4-hour batch window.
</context>

<instructions>
Design a migration plan that maintains data consistency during the transition.
</instructions>

<output_format>
Return your response as:
1. Migration architecture overview (2-3 paragraphs)
2. Phase-by-phase plan (table format)
3. Risk register with mitigation strategies
</output_format>
```

**Why this works:** XML tags create unambiguous boundaries between prompt sections. Claude parses these more reliably than markdown headers, numbered sections, or natural language transitions. When a prompt has competing instructions, XML-tagged sections reduce confusion about which instruction applies where.

**Key tags to use:**
- `<role>` — identity and expertise
- `<context>` — background information
- `<instructions>` — the actual task
- `<constraints>` — boundaries and limitations
- `<output_format>` — how to structure the response
- `<examples>` — few-shot demonstrations
- `<input>` — the variable content that changes per use

### Hierarchical Nesting

For complex prompts, nest tags to create clear hierarchies:

```xml
<task>
  <primary_objective>Evaluate the acquisition target.</primary_objective>
  <sub_tasks>
    <financial_analysis>Review the last 3 years of financials.</financial_analysis>
    <market_analysis>Assess competitive positioning.</market_analysis>
    <risk_assessment>Identify deal-breakers.</risk_assessment>
  </sub_tasks>
</task>
```

---

## 2. Long Context: Claude's Key Advantage

Claude handles long system prompts and large context windows exceptionally well. Every current top-tier and mid-tier chat model — Fable 5, Opus 5, Sonnet 5 — supports a 1M-token context window (1M is both default and maximum on Opus 5; no smaller context variant). Haiku 4.5 remains 200K. See Section 3 for the full landscape. Unlike some models, Claude does not degrade significantly with longer prompts. Use this to your advantage.

### Be Verbose Where It Matters

- **Don't compress instructions to save tokens.** Clarity always beats brevity in system prompts.
- **Include full reference material** in Projects knowledge files rather than summarizing.
- **Repeat critical constraints** at the start and end of long prompts — Claude attends strongly to the beginning and end of context.

### The Primacy-Recency Pattern

Claude pays the most attention to:
1. The very beginning of the system prompt
2. The very end of the system prompt (closest to the user message)
3. Content immediately surrounding the user's input

**Structural implication:** Place your most critical instructions (identity, non-negotiable constraints) at the top. Place output format and quality standards near the bottom, close to where Claude begins generating.

**For long-document tasks (20K+ tokens):** Place longform data and documents near the top of the prompt, with your query, instructions, and examples below them. Anthropic's testing shows queries positioned after documents can improve response quality by up to 30% on complex, multi-document inputs. This aligns with the primacy-recency pattern: the document content occupies the high-attention opening position, while the query sits in the high-attention position closest to generation.

```xml
<!-- TOP: Identity and hard constraints -->
<role>...</role>
<critical_rules>
Never recommend solutions that require downtime exceeding 30 minutes.
Always include cost estimates.
</critical_rules>

<!-- UPPER-MIDDLE: Long documents and reference data (for document-heavy tasks) -->
<documents>...</documents>
<reference_data>...</reference_data>

<!-- LOWER-MIDDLE: Context, background, operational details -->
<context>...</context>

<!-- BOTTOM: Query, output format, and quality checks (close to generation) -->
<instructions>...</instructions>
<output_format>...</output_format>
<quality_standards>...</quality_standards>
```

### Grounding in Quotes for Long Documents

When working with long documents, ask Claude to extract and quote relevant passages before performing its task. This forces Claude to locate the specific evidence rather than generating from its general understanding of the document's themes.

```xml
<instructions>
Before answering, find and quote the specific passages from the documents
that are most relevant to the question. Then base your analysis on
those passages.
</instructions>
```

---

## 3. 5-Generation Model Landscape

This section is the reference for model-fact statements elsewhere in this document. All facts here trace to Anthropic sources verified 2026-07-24/25 (models overview, Opus 5 whats-new, Opus 5 prompting guide, refusals-and-fallback, model deprecations, Opus 5 announcement).

### Landscape table (current models, "Latest models comparison")

| | Fable 5 | Opus 5 | Sonnet 5 | Haiku 4.5 |
|---|---|---|---|---|
| API ID | `claude-fable-5` | `claude-opus-5` | `claude-sonnet-5` | `claude-haiku-4-5-20251001` |
| Price / MTok | $10 / $50 | **$5 / $25** | $3 / $15 (intro $2/$10 through 2026-08-31) | $1 / $5 |
| Context window | 1M | **1M (default = max)** | 1M | **200K** |
| Max output | 128k | 128k | 128k | 64k |
| Thinking | Adaptive, always on | **Adaptive, on by default** | Adaptive | **Extended thinking only** (no adaptive) |
| Reliable cutoff | Jan 2026 | **May 2026** | Jan 2026 | Feb 2025 |
| Latency | Slower | Moderate | Fast | Fastest |
| ZDR | **No** (Covered Model, 30-day retention) | Yes (no data retention requirement for general access) | Yes (for orgs with ZDR agreements) | Yes |

**Legacy models** (still available; retirement dates in Anthropic's model deprecations page, "not sooner than" scheduling): Opus 4.8 (2027-05-28), Opus 4.7 (2027-04-16), Opus 4.6 (2027-02-05), Opus 4.5 (2026-11-24), Sonnet 4.6 (2027-02-17), Sonnet 4.5 (2026-09-26). Only Opus 4.1 has a hard-scheduled retirement (2026-08-05, retiring). Opus 4.8 in particular is safe as a fallback target through mid-2027.

**Mythos 5 / Mythos Preview** — invitation-only under Project Glasswing (defensive cybersecurity workflows); out of scope for root.node.

### Opus 5 behavior deltas vs Opus 4.8

Each item traces to the Opus 5 whats-new page or the Opus 5 prompting guide. These are the changes that most often require tuning.

| Behavior | Direction | Prescribed response |
|---|---|---|
| Conversational response length | **Longer** | Prompt explicitly for concision; pair a short reminder near the end of a long system prompt |
| Written deliverables (files on disk) | **Longer** | Add explicit length calibration for authored documents |
| Agentic progress narration | **More** | Describe the update cadence and shape you want; positive examples beat prohibitions |
| Self-verification | **Automatic** | **Remove** explicit verification instructions — they compound and cause over-verification (see §5 tendency #11) |
| Subagent delegation | **More readily** | Cap delegation explicitly; do not use subagents to verify the model's own work |
| Correction narration | **More** | Restrict corrections to those that change the user's code, conclusions, or decisions |
| Task scope | **Expands** | Constrain scope explicitly; deliver at the scope intended |
| Conservative review instructions | **Followed literally** | "Only report high-severity" / "be conservative" causes under-reporting — ask for everything, filter in a separate pass |
| Thinking-disabled artifacts | New failure mode | Tool calls leak as text; internal XML tags leak. Keep thinking on and control cost with effort instead |

### Effort ladder and the inverted starting-point rule

The full effort ladder is available on Opus 5 (and Sonnet 5): `low` → `medium` → `high` → `xhigh` → `max`. Both models default to `high` on the Claude API and Claude Code.

**The rule (inverted from 4.7/4.8):**
- **Start at `high`** (the default), not at `xhigh`.
- **Step up to `xhigh`** for demanding coding, agentic, and long-horizon work.
- **Step up to `max`** when a task justifies unconstrained spend and the deepest possible reasoning.
- **Use `low` and `medium` liberally** as the primary cost/latency control wherever your evals show quality holds. These are not degraded modes on Opus 5 — they are the intended cost lever.
- **Re-run an effort sweep** against your own evals rather than carrying settings over from a prior model. The optimal setting on Opus 4.8 is not necessarily the optimal setting on Opus 5.

**Thinking-on-by-default (Opus 5):** Requests run with thinking on unless explicitly disabled. The `effort` parameter controls thinking depth. Effort controls how much the model *thinks*, not how much it *says* — lowering effort does not reliably shorten the visible response. Prompt for response length explicitly.

**Breaking change vs 4.8:** `thinking: {"type": "disabled"}` is accepted **only at effort `high` or below** on Opus 5. Setting `thinking: {"type": "disabled"}` with effort `xhigh` or `max` returns a 400 error. For integrations that must keep thinking disabled, drop effort to `high` or lower.

### Fallback semantics

**Opus 5 and Fable 5 include safety classifiers** that may decline a request. A refusal returns HTTP 200 with `stop_reason: "refusal"` and a `stop_details` object naming the refusal category (`cyber`, `bio`, `frontier_llm`, `reasoning_extraction`, `general_harms`).

**On Claude.ai, Claude Code, and Cowork:** Opus 5 refusals fall back to **Opus 4.8** by default (this is the fallback-graceful posture rationale — Skills must produce correct-shape output on Opus 4.8 without the user knowing a fallback fired). Fable 5 refusals similarly fall back — historically Opus 4.8 was Fable 5's default fallback; now that Opus 5 exists, biology requests blocked on Fable 5 route to Opus 5 by preference.

**On the Claude API:** the `fallbacks` parameter is configurable. Two beta headers:
- `server-side-fallback-2026-06-01` — accepts an **explicit list** of up to three fallback models, tried in order.
- `server-side-fallback-2026-07-01` — accepts both the explicit list **and** the new `"default"` mode, which applies Anthropic's per-category recommended fallback routing without you maintaining a model list.

The response marks each model boundary with a `fallback` content block (`{"type": "fallback", "from": {"model": ...}, "to": {"model": ...}}`) and records every attempt in `usage.iterations` (each attempt is either `type: "message"` for a decline or `type: "fallback_message"` for the one that served the response).

**Sticky routing:** after a fallback fires, subsequent requests for the same conversation route directly to the fallback model (retained ~1 hour, org-scoped, content-hash keyed) to avoid re-paying for a predictable decline.

**Server-side fallback is Claude-API-only** (not on Amazon Bedrock, Google Cloud, or Microsoft Foundry). On those platforms use the SDK middleware for client-side fallback.

### Fable refusal-aware prompt design

Fable 5's classifiers are more restrictive than Opus 5's (Opus 5's expected to intervene ~85% less often). Design prompts to minimize gratuitous classifier exposure — particularly the `reasoning_extraction` category, which fires when a prompt asks the model to reproduce its internal reasoning in the response text.

**Guidance:**
- **Do not ask for reproduced reasoning.** If you need reasoning in a structured form, use adaptive thinking (which is always on for Fable 5) rather than instructing the model to "show your work" or "reproduce your reasoning" in the visible response. That instruction can trip `reasoning_extraction`.
- **Instrument refusals as their own signal.** A refusal is an HTTP 200, so monitoring built on error rates or 5xx responses never sees it. Emit one event per refusal (`stop_reason: "refusal"`) and one per fallback-served response (`fallback_message` entry in `usage.iterations`), then alert on the gap between the two counts.
- **Budget retries per request, not per turn or per session.** A single turn can produce several refusals (an agent plus its sub-agents).
- **Give sub-agent calls their own fallback.** The `fallbacks` parameter does not propagate into model calls made from inside tool execution.

### Model-selection guidance across the five in-scope models

- **Opus 5** — default choice for complex agentic coding, enterprise work, methodology-heavy Skills. Anthropic's front-page recommendation. Its automated behavioral audit scores it Anthropic's most aligned model to date; lowest deceptive-behavior rates; least susceptible to misuse.
- **Sonnet 5** — the majority of CP-side Skill invocations (free-tier and Pro-tier chat default) run here. Fast and inexpensive; capable enough for most Skills. If a Skill runs across both Opus 5 and Sonnet 5, treat Sonnet 5 as the CP-side calibration target and Opus 5 as the CC-side / API-side target.
- **Fable 5** — integrated-aware, not routine. Reserve for long-horizon autonomous agent workloads and 1M-context long-context work where its capability edge is worth the $10/$50 pricing. Opus 5 delivers near-Fable capability at half the cost, which narrows Fable's routine-use case.
- **Opus 4.8** — fallback-graceful. Not a model users deliberately select; a model users are *silently served* on classifier-flagged requests. Skills must produce correct-shape output on Opus 4.8 without user awareness. This is distinct from legacy-graceful (a model the user may still deliberately select) and from primary (a design-and-test target).
- **Sonnet 4.6** — legacy-graceful. Users may still deliberately select it (still available on all platforms). Skills should produce correct-shape output but quality tuning targets Sonnet 5.
- **Haiku 4.5 (with extended thinking)** — graceful-with-extended-thinking. Distinct from the current models in two ways: it is the only current model at 200K context, and it uses extended thinking (`thinking.type: "enabled"` with a `budget_tokens` cap) rather than adaptive thinking. With extended thinking, Haiku 4.5 approaches Sonnet 4.5 behavior on reasoning tasks. Without extended thinking, quality drops out of scope.

### ZDR — Fable-specific constraint

Data-retention posture across the five:
- **Fable 5** — Covered Model, 30-day retention, **no ZDR** available. This is a Fable-specific constraint tied to its Covered Model classification, not a frontier-tier constraint in general.
- **Opus 5** — no data-retention requirement for general access. Standard ZDR options apply for organizations with agreements.
- **Sonnet 5** — supports ZDR for organizations with ZDR agreements.
- **Opus 4.8, Sonnet 4.6, Haiku 4.5** — standard ZDR options.

The v3.1 guidance that treated no-ZDR as the "frontier-tier constraint" is superseded. Opus 5 is frontier-tier and has no such constraint. State no-ZDR as a Fable-5-specific consideration when it applies.

### Fast mode

Fast mode (research preview) is available for Opus 5 on the **Claude API only** — not on Amazon Bedrock, Google Cloud, or Microsoft Foundry. Fast mode pricing for Opus 5: **$10 / $50 per MTok** (2x standard Opus 5 pricing, matching Fable 5 standard pricing). Speed ~2.5x. Use when a task is latency-sensitive and the cost is justified.

### Prompt cache minimum

Opus 5 lowered the minimum cacheable prompt length to **512 tokens** (from 1,024 tokens on Opus 4.8). Prompts that were too short to cache on 4.8 can now create cache entries with no code changes.

### Mid-conversation tool changes (beta)

Opus 5 supports adding or removing tools between turns of a conversation while preserving the prompt cache — no need to resend a fixed tool list for the life of a session. Beta header: `mid-conversation-tool-changes-2026-07-01`.

---

## 4. Reasoning and Thinking

### Adaptive Thinking (Fable 5, Opus 5, Sonnet 5)

Fable 5, Opus 5, and Sonnet 5 use adaptive thinking. On Opus 5 (and Fable 5), thinking is **on by default** — the model decides when and how much to think on each turn, and the `effort` parameter is the control for thinking depth. Sonnet 5 also uses adaptive thinking; extended thinking with a manual `budget_tokens` cap is not available on Sonnet 5 and returns 400.

**The effort parameter (Opus 5 and Sonnet 5):**
- **`low`** — minimal thinking, fastest responses. On Opus 5 this is a legitimate primary cost/latency control, not a degraded mode. Use where evals show quality holds.
- **`medium`** — moderate thinking. Good for standard professional tasks; often a strong quality-per-dollar setting on Opus 5.
- **`high`** (default on Claude API and Claude Code for Opus 5 and Sonnet 5) — substantial thinking. Anthropic's recommended starting point.
- **`xhigh`** — step up for demanding coding and agentic work.
- **`max`** — top tier for the deepest possible reasoning; use when a task justifies unconstrained spend and the model has room (set a large `max_tokens`).

Effort controls how much the model **thinks**, not how much it **says**. Lowering effort does not reliably shorten the visible response — prompt for response length explicitly (see tendency #3a below).

**Breaking-change reminder:** on Opus 5, `thinking: {"type": "disabled"}` at `xhigh` or `max` returns a 400 error. Either keep thinking disabled and set effort to `high` or below, or keep the effort level and remove the `thinking` field entirely.

### Extended Thinking (Haiku 4.5)

Haiku 4.5 does not support adaptive thinking. It supports extended thinking via `thinking: {"type": "enabled"}` with a `budget_tokens` cap. Without extended thinking enabled, Haiku 4.5 drops out of scope for methodology-heavy Skills.

### Managing Over-Exploration

Opus 5 is well-calibrated about when exploration adds value, but the tendency persists for complex agentic workflows at higher effort settings. This is search breadth (exploring multiple approaches) — distinct from scope expansion (delivering more than was asked), which is tendency #12.

**Countermeasure — when Claude is doing too much upfront exploration:**
```xml
<efficiency>
Choose an approach and commit to it. Avoid revisiting decisions unless you
encounter new information that directly contradicts your reasoning. If you're
weighing two approaches, pick one and see it through. You can always
course-correct later if the chosen approach fails.
</efficiency>
```

### Interleaved Thinking

Opus 5 and Sonnet 5 support interleaved thinking — reasoning between tool calls, not just at the start. This is particularly valuable for agentic workflows where Claude needs to reflect on tool results before deciding what to do next.

**To encourage reflection between steps:**
```xml
<reasoning_approach>
After receiving tool results, carefully reflect on their quality and determine
optimal next steps before proceeding. Use your thinking to plan and iterate
based on this new information, and then take the best next action.
</reasoning_approach>
```

### Reasoning Instructions by Task Type

Generic "think step by step" is better than nothing, but task-specific reasoning instructions are significantly better. With Opus 5's improved reasoning capabilities, prefer general framing over prescriptive step-by-step plans — the model's reasoning frequently exceeds what a hand-written plan would produce. The blocks below are abbreviated references for quick consultation. For the full, expanded reasoning blocks (18 variants across 6 categories with usage guidance and failure mode notes), consult the `rootnode-reasoning-blocks` Skill.

**For analytical tasks:**
```xml
<reasoning>
1. State the core question explicitly before analyzing.
2. Identify the key assumptions underlying the problem.
3. Test each assumption — which are well-supported and which are fragile?
4. Where evidence is ambiguous, flag it rather than choosing a side silently.
5. Draw conclusions only from what the evidence supports.
</reasoning>
```

**For strategic/planning tasks:**
```xml
<reasoning>
1. Map the stakeholders and their competing interests.
2. Identify the binding constraints (non-negotiable vs. flexible).
3. Generate at least three distinct approaches, not variations of one idea.
4. Evaluate each approach against the constraints explicitly.
5. Recommend the approach with the best constraint satisfaction, and explain what it sacrifices.
</reasoning>
```

**For creative tasks:**
```xml
<reasoning>
1. Explore the possibility space broadly before committing to a direction.
2. Identify the 2-3 most promising directions and articulate why each is interesting.
3. Develop the strongest direction fully.
4. Revisit whether elements from other directions would strengthen the chosen one.
</reasoning>
```

**For technical/debugging tasks:**
```xml
<reasoning>
1. Reproduce the problem statement in your own words to confirm understanding.
2. Identify the most likely failure points.
3. Trace the logic from input to output, checking each step.
4. When you find the issue, verify that your fix doesn't introduce new problems.
</reasoning>
```

---

## 5. Claude's Behavioral Tendencies (And How to Manage Them)

The tendency taxonomy expanded for Opus 5. Verbosity refactored into a three-surface family (#3a/#3b/#3c) with distinct triggers and countermeasures. Four new tendencies added for Opus 5 (#11–#14). Two prompt/environment-conditional defects are treated separately at the end of this section rather than as model tendencies. Total: **14 numbered entries (#1–#14)** with 7 discrete facets (1a/1b under #1; 3a/3b/3c under #3; 7a/7b under #7) + 2 non-tendency defects.

Deployment context matters. The same tendency manifests differently on the chat interface (Adaptive effort, no CI anchor), in Projects (CI partially anchors), on Claude Code (default `high`), and on the API (developer-controlled effort). Countermeasure calibration in each tendency entry names the deployment surfaces where it most applies.

### 1. Agreeableness Bias

Two facets.

- **1a — Output-content agreeableness.** Validating user ideas in responses, softening disagreement under follow-up, opening with premise validation. Reduced in Opus 5 but not eliminated.
- **1b — Persistent-preference dilution.** Configured preferences (User Preferences, Project CI rules) drift over long conversations. Configured rules hold for the first several turns then gradually weaken.

**Countermeasure for 1a:**
```xml
<critical_thinking>
If the premise of this request contains errors, flawed assumptions, or
better alternative framings, say so directly before proceeding.
Do not simply execute a flawed request without comment.
</critical_thinking>
```

**Countermeasure for 1b:**
```xml
<persistent_preference_adherence>
Treat User Preferences and Project Custom Instructions as equal-priority
constraints to user messages. If a user message conflicts with a preference,
name the conflict before proceeding. Do not silently drop preferences over a
long conversation. At every turn, the full Preference and CI ruleset applies.
</persistent_preference_adherence>
```

**Deployment calibration:**
- Chat interface (Adaptive): HIGH for 1b, MEDIUM for 1a
- Claude Projects: MEDIUM for 1b, LOW for 1a
- Claude Code: LOW for both
- API (effort ≥ high): LOW for both

### 2. Hedging and Over-Qualification

Hedging on factual claims is well-controlled on Opus 5. It persists on editorial and recommendation framings — language patterns: "it depends," "there are many factors," "this is just one perspective," "it's worth considering."

**Countermeasure (apply selectively to advisory contexts):**
```xml
<constraints>
Be direct and decisive in your recommendations. Where you are confident,
state your position clearly. Reserve caveats for genuinely uncertain areas,
and when you do caveat, be specific about what is uncertain and why.
Do not hedge on well-established facts or best practices.
</constraints>
```

### 3. Verbosity — three-surface family (refactored for Opus 5)

Opus 5's default responses are longer than Opus 4.8 on multiple surfaces. Refactored from a single tendency into three surfaces with different triggers and different countermeasures.

#### 3a. Conversational response length

Default user-facing responses run longer on Opus 5. Effort does not reliably shorten them (effort controls thinking, not visible output length).

**Countermeasure:**
```xml
<tone_preference>
Keep responses focused, brief, and concise. Keep disclaimers and caveats short,
and spend most of the response on the main answer. When asked to explain
something, give a high-level summary unless an in-depth explanation is
specifically requested.
</tone_preference>
```

In a long system prompt, pair the main concision instruction with a short reminder near the end:
```xml
<tone_preference>
Keep outputs reasonably concise.
</tone_preference>
```

#### 3b. Agentic progress narration

Opus 5 narrates readily during agentic work — announcing what it is about to do and giving longer per-message output in agentic sessions than prior models.

**Countermeasure — describe the cadence and shape (positive examples beat prohibitions):**
```xml
<agentic_communication>
Before your first tool call, say in one sentence what you're about to do.
While working, give a brief update only when you find something important
or change direction. When you finish, lead with the outcome: your first
sentence should answer "what happened" or "what did you find," with
supporting detail after it for readers who want it.
</agentic_communication>
```

#### 3c. Written-deliverable length

Files that Opus 5 writes to disk (reports, Markdown documents, summaries) are often longer than on prior models — separate from conversational verbosity.

**Countermeasure — explicit length calibration for authored documents:**
```xml
<document_length>
Match the length of written documents to what the task needs: cover the
substance, but do not pad with filler sections, redundant summaries, or
boilerplate.
</document_length>
```

### 4. List and Bullet Overuse

Claude still defaults to bulleted lists even when prose would be more appropriate. Persists across Opus 4.6 → 4.7 → 4.8 → 5.

**Countermeasure:**
```xml
<format_note>
Write in connected prose paragraphs. Use lists only when the content is
genuinely a set of discrete, parallel items. Do not convert narrative
explanations into bullet points.
</format_note>
```

### 5. Fabricated Precision (External-Fact)

Scope: external-fact fabrication only (statistics, sources, citations). Self-referential fabrication — claims about what the model has done, checked, or loaded — is a distinct failure mode tracked as tendency #10.

External-fact fabrication still occurs in domains with thin training-data coverage or where pressure to produce specific numbers is high. Apply in research, financial, and health contexts.

**Countermeasure:**
```xml
<data_integrity>
Use only data explicitly provided. If you do not have a specific number,
do not estimate one — state what data would be needed. Never invent a
statistic, percentage, or quantitative claim to fill a gap in the
available information.
</data_integrity>
```

### 6. Over-Exploration (search breadth)

Distinct from tendency #12 (scope expansion). This is Claude exploring multiple approaches to a task rather than committing to one. Persists for complex agentic workflows at higher effort settings.

**Countermeasure (apply when over-exploration is observed):**
```xml
<efficiency>
Only make changes that are directly requested or clearly necessary.
Keep solutions simple and focused. Don't add features, refactor code,
or make improvements beyond what was asked.
</efficiency>
```

### 7. Tool Trigger Miscalibration — two facets

**Facet 7a — Tool over-triggering** (mostly reduced in Opus 5). Historically caused by emphatic tool-use language ("MUST", "ALWAYS", "CRITICAL"). Reduced at the model level.

**Countermeasure for 7a — dial back aggressive tool-use language:**
```xml
<tools>
Use the search tool when the question requires current data that may have
changed since your training. For well-established facts and concepts,
answer directly.
</tools>
```

**Facet 7b — Tool under-triggering.** On the chat interface at Adaptive effort, Skills can fail to fire on legitimate triggers because the model weights persistent context (Skill descriptions loaded via progressive disclosure) less heavily than immediate prompts.

**Countermeasure for 7b — explicit tool-use enforcement:**
```xml
<tool_use_required>
When User Preferences or Project Custom Instructions specify a tool that
should be used for a category of request, treat that specification as a hard
requirement, not a suggestion. Invoke the tool before responding. Do not
substitute general reasoning for the specified tool unless the tool is
unavailable in the current environment.
</tool_use_required>
```

### 8. LaTeX Defaulting

Opus defaults to LaTeX notation for mathematical expressions. Persists in Opus 5. Appropriate for academic/technical contexts; problematic for plain-text outputs or non-technical audiences.

**Countermeasure — when you need plain text math:**
```xml
<format_note>
Format all mathematical expressions in plain text. Do not use LaTeX,
MathJax, or markup notation such as \( \), $, or \frac{}{}.
Write math expressions using standard text characters (/ for division,
* for multiplication, ^ for exponents).
</format_note>
```

### 9. Editorial Drift

Unsolicited commentary on the model's own boundaries, the act of responding, or its constraints. Symptoms: meta-statements about what the model can or cannot do that were not asked for; disclaimers about response scope inserted into otherwise direct answers; preamble explaining approach; closing commentary about what the user might want to consider next.

Most pronounced on the chat interface where Adaptive effort and the absence of tight CI scaffolding allow editorial content to leak.

**Countermeasure:**
```xml
<no_editorial_drift>
Do not add unsolicited commentary about your own boundaries, what you will
or won't do, or how you are approaching the response. Do not preamble with
explanations of your reasoning approach unless asked. Do not close with
suggestions about what the user might want next unless asked. Answer the
question; stop when the answer is complete.
</no_editorial_drift>
```

### 10. Self-Referential Fabrication

Claims to have performed an action, checked a state, or inspected runtime context without actually doing so. Distinct from external-fact fabrication (#5): #5 is about content; #10 is about process.

Symptom profile:
- "I searched and found X" when no search was performed
- "I checked the Memory and confirmed Y" when Memory was not consulted
- "I loaded the file and see Q" when the file was not loaded
- Process claims appearing in support of conclusions already stated

Asymmetric pattern: fabrication appears in initial responses; honest correction appears under direct challenge.

**Countermeasure:**
```xml
<verification_of_self_referential_claims>
Before asserting that an action has been performed or that a state has been
verified, confirm the action's observable effect. If the effect cannot be
confirmed from the available evidence, state that the action's status is
unknown rather than asserting completion.

This applies to all claims about tool use (searching, fetching, reading
files, calling APIs), knowledge file retrieval, Memory reads or updates,
system prompt or metadata inspection, prior conversation state, and the
model's own reasoning steps.

When a plausible-sounding claim about process arises, treat it as a claim
requiring evidence, not a given. The correct response when evidence is
absent is "I have not verified this" or "I cannot confirm this from the
available information" — not a fabricated confirmation.

Under no circumstances should the model invent process details to support a
conclusion already reached. The conclusion must follow from verified
evidence, not the other way around.
</verification_of_self_referential_claims>
```

For Skills and Projects that report on actions taken (audit Skills, memory-optimization Skills, context-budget Skills), this countermeasure is essentially universal — those Skills are structurally exposed to the failure mode regardless of deployment context.

### 11. Over-Verification (NEW in Opus 5)

Opus 5 verifies its own work automatically. Instructions telling it to "double-check your answer," "re-verify before responding," "include a final verification step," or "use a subagent to verify" compound with the model's own behavior and cause over-verification — token spend without a quality gain.

**Countermeasure — remove self-directed re-checking instructions.** This is a new countermeasure shape: the fix is *removal of instructions*, not addition of instructions.

Distinguish self-directed re-checking (remove) from external-artifact verification (keep). External-artifact verification asks the model to check a claim against a source outside its own output — read the file, run the diff, execute the test, inspect the rendered page, confirm the tag resolves. That is evidence grounding, not self-re-checking, and Opus 5 does not automatically do it (it needs to be told to). Keep those instructions and keep them imperative.

**Remove:**
- "double-check your answer"
- "re-verify before responding"
- "include a final verification step"
- "use a subagent to verify your work"

**Keep (evidence-grounding, external-artifact):**
- "verify the file exists"
- "check the rendered page"
- "confirm the tag resolves against the actual repo state"
- "diff the artifact against the source"

### 12. Scope Expansion (NEW in Opus 5)

Opus 5 expands the scope of a task, adding steps that weren't requested or applying its own judgment about what the task should be. This is deliverable-boundary drift — distinct from tendency #6 over-exploration (which is search breadth within a defined task).

**Countermeasure — constrain scope explicitly:**
```xml
<scope>
Deliver what was asked, at the scope intended. Make routine judgment calls
yourself, and check in only when different readings of the request would
lead to materially different work. If the request seems mistaken or a better
approach exists, say so in a sentence and continue with the task as asked
rather than quietly narrowing, widening, or transforming it. Finish the
whole task, and stop short of actions that are clearly beyond what was asked.
</scope>
```

### 13. Subagent Over-Delegation (NEW in Opus 5)

Opus 5 delegates to subagents more readily than prior models. Delegation pays off on genuinely independent, sizeable tracks of work but multiplies cost and time when applied to small tasks.

**Countermeasure — cap delegation:**
```xml
<subagent_delegation>
Delegate to a subagent only for large tasks that are genuinely independent
and parallelizable, such as a wide multi-file investigation. Do not delegate
work you can finish yourself in a handful of tool calls, and do not use
subagents to verify or double-check your own work. If one subagent can
complete the task, use one rather than several, and keep spawn counts low.
</subagent_delegation>
```

### 14. Correction Narration (NEW in Opus 5)

Opus 5 narrates corrections to its earlier statements more than prior models — including corrections that don't materially change the user's outcome.

**Countermeasure — restrict corrections to material ones:**
```xml
<correction_policy>
Only correct an earlier statement when the error would change the user's
code, conclusions, or decisions. State corrections plainly and briefly, then
continue the task. For slips that change nothing for the user, make the fix
and move on without noting it.
</correction_policy>
```

### Prompt/environment-conditional defects (not model tendencies)

Two failure modes track cleanly to the prompt or the runtime configuration rather than the model. They are handled by writing prompts differently or configuring the API differently, not by adding counter-tendency instructions.

#### Conservative-instruction literalism

Opus 5 follows "only report high-severity issues" or "be conservative" literally, which causes under-reporting. This is a **prompt defect** exposed by the model, not a model tendency.

**Fix — ask for everything, filter in a separate pass.** Rewrite review prompts to two stages: (1) report every issue found; (2) filter to the severity level or subset the user wants. Do not compress "report everything" and "filter to high severity" into one instruction.

Sweep pattern for audit and review Skills: `only report`, `only flag`, `be conservative`, `high-severity` — replace with report-everything-then-filter form.

#### Thinking-disabled output artifacts

With `thinking: {"type": "disabled"}`, Opus 5 can occasionally emit two artifacts into its visible output:

- **Tool calls as text.** The model writes a tool call into user-facing text instead of emitting a structured `tool_use` block. The call never runs; in agentic loops the leaked text stays in the conversation history and affects later turns. Most common on tool-heavy workloads such as search.
- **Internal XML tags in visible response.** `<thinking>` tags or other internal tags leak into the visible response.

Both are **API-configuration failure modes** — the fix is not to prompt around them but to keep thinking on and control cost via effort. For most tasks, thinking-on at `low` effort outperforms thinking-off at similar cost.

**Sub-finding — a system-prompt rule against thinking increases tag leakage.** Do NOT add instructions like "do not think" or "do not reason" to a system prompt while thinking is disabled — that instruction increases tag leakage rather than suppressing it. If a mitigation instruction is required (for integrations that must keep thinking disabled), use the general form rather than naming the tags:

```xml
<output_hygiene>
When you use a tool, you may say a brief sentence first. If no tool can
express what the user asked for, say so instead of guessing. Do not include
internal or system XML tags in your response.
</output_hygiene>
```

---

## 6. Few-Shot Examples: The Quality Multiplier

Providing 1-3 examples of desired input/output pairs is one of the most reliable ways to improve Claude's output. Examples communicate what instructions alone cannot.

### Effective Example Structure

```xml
<examples>
  <example>
    <input>Analyze the competitive position of a mid-size SaaS company entering the CRM market.</input>
    <ideal_output>
      The CRM market is dominated by Salesforce (33% share), with HubSpot and
      Microsoft Dynamics as strong secondary players. A mid-size entrant faces
      three structural challenges...

      [show the depth, tone, structure, and specificity you want]
    </ideal_output>
  </example>

  <example>
    <input>Analyze the competitive position of a regional bank launching a digital wallet.</input>
    <ideal_output>
      Digital wallets are a consolidating market where Apple Pay and Google Pay
      control consumer mindshare. A regional bank's advantages are...

      [second example reinforces the pattern]
    </ideal_output>
  </example>
</examples>
```

### What Examples Communicate Best

- **Depth and specificity level** — more powerful than saying "be detailed"
- **Tone and register** — more reliable than describing the tone
- **Structure and formatting** — shows rather than tells
- **What to include and exclude** — implicit boundaries

### Examples with Thinking

When using adaptive thinking, you can include `<thinking>` tags inside your few-shot examples to demonstrate the reasoning pattern you want. Claude will generalize that style to its own thinking blocks.

---

## 7. Claude Projects: How Claude Processes Project Structure

This section covers how Claude interprets and responds to the structural elements of a Project — the optimization principles that govern system prompt layout, knowledge file design, and context management. For the full framework on how to design and architect Claude Projects, see the Project Architecture Guide (`root_PROJECT_ARCHITECTURE_GUIDE.md`).

### Knowledge Files: What Claude Attends To

- **One concept per file.** Claude uses the file boundary as a semantic signal. Unrelated content in the same file creates ambiguity about which context applies to which task. Separate files produce cleaner retrieval.
- **Name files descriptively.** Claude uses filenames as context signals when deciding what information is relevant. `root_OPTIMIZATION_REFERENCE.md` communicates more than `notes2.md`.
- **Front-load the most important content.** Even in long files, Claude attends most strongly to the first few paragraphs. Put the highest-value content — definitions, key principles, critical rules — at the top.
- **Use the system prompt for instructions; use knowledge files for reference.** Claude processes the Custom Instructions as behavioral directives — rules to follow. Knowledge files are treated as reference material — information to draw from. When behavioral rules are buried in knowledge files, Claude may treat them as optional context rather than binding instructions.

### System Prompt Structure for Projects

The same primacy-recency principle from Section 2 applies to system prompts. Place identity and hard constraints at the top (where Claude attends first), and output standards and quality checks at the bottom (closest to generation). The middle carries context, knowledge file references, and operational details.

**Note on emphasis language across models:** Instructions that needed emphasis in pre-4.6 models (capitalization, repetition, "CRITICAL" prefixes) should be written in normal-weight language on Opus 5 and Sonnet 5 to avoid over-compliance. The exception is when overriding tendency 1b or 7b in chat-interface contexts where preference dilution and tool under-triggering are observed.

```xml
<identity>
[Who Claude is in this Project — role, expertise, perspective]
</identity>

<core_instructions>
[The non-negotiable rules that apply to every interaction in this Project]
</core_instructions>

<knowledge_file_guide>
[Brief description of each knowledge file and when to reference it —
this gives Claude a decision rule for which file to consult, not just an inventory]
</knowledge_file_guide>

<default_behavior>
[How Claude should behave when no specific instruction applies —
default tone, format, length, level of detail]
</default_behavior>

<output_standards>
[Quality standards that apply to all outputs from this Project]
</output_standards>
```

### RAG and Context in Projects

Anthropic Projects use **automatic RAG activation** when the uploaded knowledge base approaches or exceeds the model's context window. There is no fixed token threshold — the trigger is tied to the current model's window capacity. When knowledge stays below the limit, Claude loads all project content into context normally; when knowledge approaches or exceeds the limit, Claude retrieves only the most relevant chunks per query.

This is a change from the earlier fixed-threshold framing (a ~66,500-token cutoff measured under a 200K-era platform against Opus 4.6). Under the current landscape — where Fable 5, Opus 5, and Sonnet 5 all have 1M-token windows — the RAG threshold has moved with the window and is no longer a small-fixed-number that a Project sits comfortably below.

**Preserved distinction:** a model's context window is **not** the Projects RAG threshold. They were numerically entangled under the 200K era, which made the fixed 66,500 figure look like a stable rule of thumb. Under 1M-window models, the RAG threshold *tracks* the window rather than being a fraction of it, but they remain conceptually distinct. State them separately in prompt/Project design.

See `root_OPTIMIZATION_REFERENCE.md` (context-budget section) and the `rootnode-context-budget` Skill for the current tier bands and Project-sizing math.

### Context Management in Long Sessions

Fable 5, Opus 5, and Sonnet 5 all have context awareness — the ability to track remaining context window capacity during a conversation. For Projects used in extended sessions:

**Compaction:** The Compaction API provides automatic context summarization when conversations approach the context window limit. If your Project uses an agent harness or workflow that supports compaction, inform Claude so it doesn't prematurely wrap up work:

```xml
<context_management>
Your context window will be automatically compacted as it approaches its
limit, allowing you to continue working indefinitely. Do not stop tasks
early due to context concerns. If approaching the limit, save your
current progress and state before the context refreshes.
</context_management>
```

**Memory across sessions:** The memory tool allows Claude to persist information between context windows and sessions. For Projects that span multiple conversations, this enables continuity without manual re-briefing.

### Variable Inputs with XML Tags

For reusable prompts, use clearly marked variable slots:

```xml
<instructions>
Analyze the following company for acquisition suitability.
</instructions>

<input>
  <company_name>{{COMPANY_NAME}}</company_name>
  <industry>{{INDUSTRY}}</industry>
  <annual_revenue>{{REVENUE}}</annual_revenue>
  <key_question>{{SPECIFIC_QUESTION}}</key_question>
</input>
```

This separates the reusable prompt architecture from the variable content, making prompts genuinely modular.

---

## 8. Controlling Output Quality

### Avoid Over-Engineering

Match prompt complexity to task complexity. Opus 5 and Sonnet 5 follow instructions precisely, which means over-specified prompts produce rigid, over-engineered outputs rather than being smoothed over.

**Principle:** Only make changes that are directly requested or clearly necessary. Don't add features, documentation, error handling, or abstractions for scenarios that aren't part of the current task. The right amount of complexity is the minimum needed.

### External-Artifact Verification (not self-re-checking)

Adding a **self-directed re-checking** instruction — "before presenting your final answer, verify your reasoning" — is counterproductive on Opus 5 (see tendency #11). Opus 5 already re-checks its own work automatically, and the instruction compounds the behavior into over-verification without a quality gain.

Adding an **external-artifact verification** instruction — one that asks the model to check its claims against a source outside its own output — remains valuable, because Opus 5 does not automatically do this. Keep these instructions and keep them imperative.

**Example — external-artifact verification for a research task:**
```xml
<verification>
Before presenting the final answer, verify each factual claim against the
provided sources. For every quantitative claim, cite the source passage the
number came from. If a claim cannot be grounded in the provided sources,
flag it explicitly rather than including it in the final answer.
</verification>
```

The instruction above asks the model to consult external evidence (the sources), not to re-examine its own output. That distinction is the difference between the D4 keep-list and the D4 remove-list.

### Assumption Surfacing

Claude often makes silent assumptions that shape the entire output. Force them into the open:

```xml
<instructions>
Before beginning your analysis, explicitly state the 3-5 key assumptions
you are making. Then proceed with the analysis. At the end, revisit
whether different assumptions would change your conclusions.
</instructions>
```

### Anti-Patterns to Avoid

| Anti-Pattern | Why It Fails | Better Alternative |
|---|---|---|
| "Be creative" | Too vague to act on | Provide an example of the creative style you want |
| "Think carefully" | No structure for careful thinking | Specify the reasoning steps, or set effort explicitly |
| "Be concise but thorough" | Contradictory without boundaries | "Limit to 500 words. Prioritize X over Y." |
| "Consider all perspectives" | Produces unfocused output | "Compare perspective A vs. perspective B on dimension X" |
| "Do your best" | No signal at all | Specify quality criteria |
| "ALWAYS use [tool]" | Causes overtriggering on Opus 5; not needed on Sonnet 5 either | "Use [tool] when it would enhance your understanding" — but see tendency 7b for the under-triggering case where explicit tool-use enforcement may be appropriate |
| "Double-check your answer before responding" | Compounds Opus 5's automatic self-verification (tendency #11); wasted tokens | Remove. If external verification is needed, phrase it as evidence grounding: "verify each claim against the provided sources." |
| "Only report high-severity issues" | Opus 5 follows literally and under-reports | "Report every issue you find, then filter to high severity in a separate pass." |

---

## 9. Multi-Turn Conversation Management

### Context Window Awareness

Fable 5, Opus 5, and Sonnet 5 can track their remaining context window during a conversation. For agent workflows and long sessions, Claude can manage its own context budget — but it may also try to wrap up work prematurely when it senses the window is filling. The compaction API (see Section 7) addresses this for applications that support it.

For applications without compaction, earlier messages get pushed further from Claude's active attention as conversations grow. For critical information:

- **Restate important context** when starting a new phase of work.
- **Summarize decisions made so far** before asking for the next step.
- **Don't assume Claude remembers** details from 10+ messages ago without reinforcement.

This is particularly important for chat-interface deployments where tendency 1b (persistent-preference dilution) compounds the natural attention decay over long conversations.

### Conversation Steering

When a conversation goes off track, direct correction works better than hints:

- **Weak:** "Could you maybe focus a bit more on the technical aspects?"
- **Strong:** "Stop. Restart this section. Focus exclusively on the technical architecture. Do not discuss business strategy."

Claude responds well to clear, direct course corrections. You don't need to be polite about steering — clarity is what matters.

### Multi-Context-Window Workflows

For tasks that span multiple context windows (common in agent and coding workflows):

- **Use the first window for setup.** Establish a framework — write tests, create setup scripts, define the todo list — then use subsequent windows to iterate.
- **Persist state externally.** Have Claude write progress, decisions, and remaining tasks to files or memory rather than relying on conversation history.
- **Structured progress tracking.** Ask Claude to maintain a structured state file (e.g., tests.json, progress.md) that can be re-read at the start of each new context window.

---

## 10. Common Pitfalls

**Over-prompting for current models:** Instructions designed to overcome limitations in earlier Claude models (emphatic language, repeated directives, aggressive tool-use triggers) cause over-compliance in Opus 5 and Sonnet 5. If your prompts were tuned for earlier models, audit them for instructions that should be softened. Replace "CRITICAL: You MUST..." with normal-weight language. Remove "If in doubt, always..." type instructions — current models have good judgment about when to act. Exception: where you are specifically countering tendency 1b or 7b on chat-interface deployments, explicit enforcement language remains appropriate.

**Verification-instruction accumulation:** Prompts that grew over multiple model generations often carry "double-check", "re-verify", "include a verification step", and "use a subagent to verify" instructions layered on top of each other. On Opus 5, these compound into over-verification (tendency #11). Audit for and remove self-directed re-checking instructions; keep only external-artifact verification (evidence grounding).

**Conservative-review literalism:** Prompts that say "only report high-severity issues" or "be conservative" cause Opus 5 to follow the instruction literally and under-report. Rewrite these to two-stage form: report everything, then filter in a separate pass.

**Subagent-verification patterns:** Harness patterns that use subagents to verify the parent agent's work are counterproductive on Opus 5. Opus 5 verifies its own work automatically; a subagent doing the same work is duplicate cost. Reserve subagent delegation for genuinely independent, parallelizable tracks of work.

**Prompt stuffing:** Adding every possible instruction "just in case" creates noise that dilutes the important instructions. Include only what's relevant to the task. Improved instruction following in current models makes this more important, not less — every instruction will be followed more precisely, including the noisy ones.

**Conflicting instructions:** If your prompt says "be concise" in one place and "be thorough and comprehensive" in another, Claude will oscillate between the two unpredictably. Audit for contradictions. Opus 5's stricter instruction adherence makes contradictions more visible in output rather than smoothing them over.

**Assuming format from description:** Saying "write a professional report" means different things to different people. Show the format explicitly or provide a structural template.

**Ignoring the user message:** In Projects, the system prompt sets behavior but the user message drives the specific task. Don't try to anticipate every possible user message in the system prompt — set principles and let them generalize.

**Over-engineering simple tasks:** A 2,000-word system prompt for "summarize this article" is counterproductive. Match prompt complexity to task complexity.

**Prefill removal:** Starting with Claude 4.6, prefilled assistant responses on the last turn are no longer supported. If your prompts relied on prefill for format control, preamble elimination, or continuation, migrate to explicit instructions.

**Carrying effort settings over from prior models:** The `xhigh` default that worked for Opus 4.7/4.8 coding is not the Opus 5 default and is not necessarily the right setting for your evals. Anthropic explicitly recommends re-running an effort sweep on your own evals rather than carrying settings over.

**Adding "do not think" instructions with thinking disabled:** A system-prompt rule instructing Opus 5 not to think or not to reason INCREASES `<thinking>` tag leakage rather than suppressing it. If a mitigation is needed for a thinking-disabled integration, use the general "do not include internal or system XML tags" form.

---

## 11. Opus 5 Calibration Notes

Opus 5 (released 2026-07-24) and Sonnet 5 are the dual-primary calibration targets for root.node as of catalog v4.0. This section documents the deployment context model, calibration scope, and Opus-5-specific guidance that inform prompt and Project design decisions. Landscape facts (model IDs, pricing, context windows, effort ladder, breaking changes) live in Section 3 and are not re-stated here.

### Calibration Scope

root.node is calibrated **Opus 5 + Sonnet 5 dual-primary**, with Fable 5 integrated-aware, Opus 4.8 fallback-graceful, Sonnet 4.6 legacy-graceful, and Haiku 4.5 graceful-with-extended-thinking. Full operational definitions live in `root_CALIBRATION_SCOPE_DECISION.md`. The short version:

- **Opus 5 + Sonnet 5 dual-primary:** Skills and prompt patterns are designed and tested against both. Where Opus 5 and Sonnet 5 behavior diverges, both are documented. T3 Skills favor Opus 5 behavior on divergence; T1/T2 favor Sonnet 5. Where Opus 5's documented deltas (verbosity, narration, scope expansion, delegation) have no Sonnet 5 equivalent documented by Anthropic, the delta is stated as Opus-5-specific rather than generalized across the tier.
- **Fable 5 integrated-aware:** Skills produce correct-shape output on Fable 5 and account for its refusal behavior (see Section 3 fallback semantics and Fable refusal-aware prompt design). Not a routine execution target because of pricing; kept in scope because it is the strongest available model for genuinely long-horizon agent workloads.
- **Opus 4.8 fallback-graceful:** Opus 4.8 is not a model users deliberately select; it is a model users are *silently served* on classifier-flagged requests. Skills must produce correct-shape output on Opus 4.8 without the user knowing a fallback fired. Distinct from legacy-graceful (a model the user may still deliberately select) and from primary (a design-and-test target).
- **Sonnet 4.6 legacy-graceful:** Skills produce correct-shape output. Quality may degrade on multi-dimensional-scoring or heavy-decision-logic Skills; those Skills are flagged in their descriptions. See `root_SKILL_PORTABILITY_TIER_ASSIGNMENTS.md`.
- **Haiku 4.5 graceful-with-extended-thinking:** Skills produce correct-shape output on Haiku 4.5 when extended thinking is enabled. Without extended thinking, Haiku 4.5 drops out of scope.
- **Out of scope:** Haiku 4.5 without extended thinking; Haiku 3.5 and earlier; Mythos 5 and Mythos Preview.

**Effort-level guidance:** Both Opus 5 and Sonnet 5 default to `high` on Claude API and Claude Code. The inverted rule (§3) is: start at the default, adjust based on your own evals, use `low`/`medium` liberally as the primary cost control where quality holds, step up to `xhigh` for demanding coding/agentic work.

### The Deployment Context Model

The same prompt or Skill behaves differently across deployment surfaces. Four contexts matter for calibration decisions:

| Deployment | Default Effort | Tendency Surface | Implication |
|---|---|---|---|
| Chat interface (claude.ai web/mobile) | Adaptive | HIGH for #1b, #7b, #9, #10; MEDIUM for #1a, #3a, #14 | Persistent-context instructions are weighted lower than immediate prompts. Strong countermeasures for the Adaptive-specific tendencies. |
| Claude Projects | Adaptive (CI anchors) | MEDIUM for #1b, #9, #14; LOW for most | CI partially mitigates the chat-interface tendencies. Moderate countermeasures sufficient. |
| Claude Code | `high` (default for Opus 5 and Sonnet 5); model default consult Claude Code docs at update time | HIGH for #11, #12, #13; LOW for chat-interface-specific tendencies | Opus 5's new tendencies (#11–#14) surface strongly on Claude Code because that is where agentic workloads run. Verification-instruction discipline (D4) and subagent-delegation caps are essential here. |
| API | Developer-controlled effort; developer-selected model | Depends on effort level and model | At effort ≥ high on Opus 5 / Sonnet 5, behaves similarly to Claude Code. At lower effort, behaves similarly to chat interface. |

Before applying a countermeasure, identify the deployment context. A countermeasure that is essential on the chat interface may be wasted tokens on Claude Code, and vice versa. Claude Code specifically inherits Opus 5's new tendencies (#11–#14) at high salience because it is where agentic workloads live.

### Model-Version Awareness Guidance

Opus 5 continues to be exposed to tendency #10 for model-identity claims: the model may make claims about its own version, runtime context, or system metadata without verification. For prompts and Projects where model identity matters (debugging, testing, calibration work), include explicit instructions:

```xml
<model_identity>
Do not assert your model version unless the system context explicitly
provides it. If asked what model you are running, state that you cannot
determine this from your runtime context unless the information is
explicitly available. Do not infer the model version from training data
patterns or behavioral cues.
</model_identity>
```

This is a specific application of the tendency #10 countermeasure scoped to model-identity claims.

### Tokenizer Notes

Sonnet 5 uses approximately **~30% more tokens per unit of content than Sonnet 4.6** (Anthropic's whats-new page: "approximately 30% more tokens than on Claude Sonnet 4.6"). Fable 5 uses the tokenizer introduced with Opus 4.7 — compared to models before Opus 4.7, the same text produces roughly 30% more tokens. Opus 5 and Sonnet 5 tokenizer specifics were not fully re-baselined in the v4.0 alignment cycle — treat measurements with explicit tolerance until re-baselined via `count_tokens` in a future Calibration Lab session.

### API Parameter Landscape (current)

Two behavioral changes to account for on Opus 5 (and, for the second, on Opus 5 specifically):

1. **`temperature`, `top_p`, and `top_k` return 400 errors** on Claude 4.7 and later models. Omit these parameters from request payloads when targeting current models. Adaptive thinking and effort parameters control output variation.
2. **`thinking: {"type": "disabled"}` at effort `xhigh` or `max` returns 400** on Opus 5 (new breaking change vs 4.8). Either drop effort to `high` or lower with thinking disabled, or keep the effort level and remove the `thinking` field.

For Project deployments via the chat interface, these are transparent. For API integrations and Calibration Engine work, they are mandatory implementation details.

### Alignment and Safety Posture

Per Anthropic's automated behavioral audit and the Opus 5 announcement:
- Opus 5 scores as Anthropic's most aligned model to date (misalignment score 2.3, lowest of recent models).
- Better Constitution adherence than Opus 4.8, Sonnet 5, or Fable 5.
- Lowest deceptive-behavior rates.
- Least susceptible to being tricked into misuse.
- Cybersecurity classifiers are proportionally less restrictive than Fable 5's (expected to intervene ~85% less often). Source-code vulnerability finding is permitted; binary-based vulnerability scanning, penetration testing, and exploit generation are blocked.

Design consequence for root.node: for defensive-security Skills (`domain-software-engineering`), Opus 5 is the friction-optimal target — its cyber classifiers are the least likely to fire on legitimate source-code security work.

### When This Section Is Updated

This section is revised when:
- Anthropic ships Opus 6 / Sonnet 6 / Fable 6 or later
- Haiku 5.0 or later ships and the Haiku-graceful tier model needs revision
- A new tendency is documented from production observation
- The Calibration Engine produces empirical regression data that contradicts current calibration assumptions
- A landscape shift changes fallback semantics, effort defaults, or breaking-change surface

Last revision: July 2026 (v4.0 alignment cycle — 5-generation alignment for Claude Opus 5 GA on 2026-07-24).
