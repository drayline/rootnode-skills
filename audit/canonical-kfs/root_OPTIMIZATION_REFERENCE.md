# Optimization Reference

Claude-specific structural principles, behavioral patterns, and fix patterns for Project optimization. Calibrated for Claude Opus 5 and Sonnet 5 (dual-primary), with Fable 5 integrated-aware for long-horizon agent workloads, Opus 4.8 fallback-graceful (users are silently served it on classifier-flagged requests), Sonnet 4.6 legacy-graceful, and Haiku 4.5 graceful-with-extended-thinking. Consult this when diagnosing structural issues, checking behavioral countermeasures, and reconstructing system prompts or knowledge file architectures. Model-fact statements defer to `root_CLAUDE_OPTIMIZATION_NOTES.md` Section 3 (5-Generation Model Landscape); this document assumes that reference.

**Calibration scope:** Opus 5 + Sonnet 5 **dual-primary**; Fable 5 **integrated-aware**; Opus 4.8 **fallback-graceful**; Sonnet 4.6 **legacy-graceful**; Haiku 4.5 **graceful-with-extended-thinking**. Haiku 4.5 without extended thinking and Haiku 3.5 are out of scope. Mythos 5 / Mythos Preview out of scope. See `root_CALIBRATION_SCOPE_DECISION.md` for the full scope authority and operational definitions. Where Opus 5 and Sonnet 5 diverge, both are documented; where Sonnet 5 behavior is not documented by Anthropic, the column reads "no delta documented" rather than inheriting from Sonnet 4.6. See `root_SKILL_PORTABILITY_TIER_ASSIGNMENTS.md` for per-Skill tier assignments and Claude Code applicability classifications.

**Surface scope.** This document is primarily CP-side (Claude Project) optimization methodology. The Nine-Layer Architecture Model, system prompt architecture, Memory layer design, User Preference optimization, evolutionary optimization pathways, knowledge file design, context budget principles, RAG quality optimization, and most common structural fixes apply to chat-side Projects. The Behavioral Tendencies and Countermeasures section is surface-aware: tendencies and their deployment calibrations span CP, CC, and API contexts. The CC-side counterpart for environment design is `root_CC_ENVIRONMENT_GUIDE.md`. The surface-invariant principle layer is `root_AGENT_ENVIRONMENT_ARCHITECTURE.md`.

---

## Source Authority for Recommendations

Optimization recommendations and audit findings produced from this methodology are grounded in a 5-tier source authority hierarchy. Higher tiers override lower tiers when they conflict.

| Tier | Source class | Authoritative on |
|---|---|---|
| 1 | Anthropic primary documentation (platform.claude.com, code.claude.com, official Anthropic engineering posts) | Claude behavior, API parameters, MCP spec, Skills architecture, Claude Code mechanics |
| 2 | Anthropic engineering blog and design intent posts | Design rationale, emerging patterns |
| 3 | Tested production experience (root.node's own dogfooded patterns; user-validated deployments) | What was tried and what shipped, scoped to the deployment domain |
| 4 | Named practitioners with public artifacts | Current state of practice; not authoritative on Claude internals |
| 5 | Community sources (Discord, Reddit, Twitter) | Surfacing emerging issues; never authoritative without independent verification |

Tiers 1–3 are authoritative. Tier 4 is community evidence; cite the artifact. Tier 5 is speculative without independent verification; mark such claims `[speculative]`. Audit findings, methodology updates, and recommendations cite source tier inline so the user can weight them appropriately.

The canonical source authority hierarchy is documented in `root_AGENT_ENVIRONMENT_ARCHITECTURE.md §4.4`. This section summarizes for in-document use; the canonical layer governs cross-document evolution.

---

## Nine-Layer Architecture Model `[applies CP-side]`

The CC-side counterpart is the 7-layer architecture documented in `root_CC_ENVIRONMENT_GUIDE.md §1`. Both are surface-specific applications of the unified placement discipline in `root_AGENT_ENVIRONMENT_ARCHITECTURE.md §4.1`.

Claude.ai's personalization architecture consists of nine configurable layers across three scopes. Every layer influences Claude's behavior. The layers interact — they can reinforce, conflict with, or duplicate each other. Effective optimization requires awareness of all nine layers, not just the Project-scoped layers that root.node has historically focused on.

### Layer Inventory

**Global Scope** — affects every conversation everywhere, inside and outside Projects.

| Layer | Nature | Content | Persistence |
|---|---|---|---|
| **1. User Preferences** | Deliberate free-text | Professional background, communication style, behavioral preferences, expertise level | Static until manually edited |
| **2. Styles** | Deliberate preset/custom, selectable per conversation | Tone, format, delivery patterns — how Claude communicates | Saved as presets; applied by selection |
| **3. Global Memory** | Automatic synthesis + manual override | Work context, project awareness, learned preferences | Updated ~every 24 hours; standalone conversations only |
| **4. Skills** | Deliberate installation, dynamic activation | Procedural knowledge in SKILL.md files with progressive disclosure | Installed until removed; triggered by task relevance |
| **5. MCP Connectors** | Deliberate configuration, dynamic execution | Tool definitions for external services (Gmail, Slack, Notion, etc.) | Configured until removed; deferred loading standard |

**Project Scope** — affects only conversations within a specific Project.

| Layer | Nature | Content | Persistence |
|---|---|---|---|
| **6. Custom Instructions** | Deliberate system prompt | The 5-layer architecture: Identity, Objective, Context, Reasoning, Output + QC | Static until manually edited |
| **7. Knowledge Files** | Deliberate uploads | Reference material, guides, data, documentation | Static between conversations |
| **8. Project Memory** | Automatic synthesis + manual override | Project-specific context, decisions, phase awareness | Updated ~every 24 hours; isolated per Project |

**Conversation Scope** — affects only the current exchange.

| Layer | Nature | Content | Persistence |
|---|---|---|---|
| **9. Conversation Context** | Composite and emergent | Messages, in-session uploads, tool results, retrieved past chats | Ephemeral; feeds back into Memory over time |

### Precedence Chain

When layers conflict, Claude resolves based on this hierarchy (highest to lowest):

1. **Conversation Context** — explicit user instruction in-chat overrides everything
2. **Styles** — override format/tone from all other layers
3. **Project Custom Instructions** — override User Preferences for project-specific behaviors
4. **User Preferences** — baseline that applies when nothing else specifies
5. **Memory** — provides context but does not override deliberate instructions
6. **Skills** — supplement, do not override; behavior is unpredictable when they conflict with CI

### Cross-Layer Failure Modes

Eight interaction failures that root.node must detect. Each becomes an audit check in the Cross-Layer Alignment methodology (see AUDIT_FRAMEWORK.md for the full diagnostic instruments).

**Redundant Layering.** The same instruction appears in User Preferences AND Project CI. Wastes context — the instruction loads twice. Common with behavioral rules like "be direct." Detection: compare Preferences against CI for semantic overlap. Fix: keep in one layer (Preferences if universal, CI if project-specific).

**Silent Override.** Project CI contradicts a User Preference without the user realizing it. Detection: compare behavioral instructions across layers for conflicts. Fix: make the override explicit in CI (acknowledge the departure and why).

**Skill/Project Collision.** An installed Skill provides procedural knowledge that overlaps with or contradicts a Project's knowledge files or CI. Detection: compare Skill descriptions/triggers against Project knowledge file purposes and CI behavioral rules. Fix: disable conflicting Skills in that context, or refactor the Project to defer to the Skill.

**Connector/Instruction Mismatch.** Project CI references or assumes capabilities that require MCP connectors the user hasn't configured. Detection: scan CI for references to external tools; cross-reference against configured connectors. Fix: configure the missing connector or remove the assumption.

**Memory/Preference Confusion.** Memory has accumulated behavioral context that should be a deliberate Preference. The behavior is fragile — it depends on Memory synthesis continuing to capture the pattern. Detection: scan Memory for stabilized behavioral patterns. Fix: codify stable patterns as explicit Preferences.

**Style/CI Tension.** A Style's communication rules conflict with a Project's output format specifications. The Style wins for format/tone, which may break structured output requirements. Detection: compare active Style against CI output standards. Fix: adjust the Style or add CI instructions that explicitly specify format requirements that should survive Style application.

**Cross-Project Duplication.** Multiple Projects contain identical behavioral instructions that should be in User Preferences. Wastes context across every Project. Detection: compare behavioral rules across the Project portfolio. Fix: promote the common instruction to Preferences and remove from individual Projects.

**Context Waste from Global Layers.** Overly detailed Preferences, too many Skill metadata entries, or excessive MCP definitions consume context in every conversation. Detection: estimate total context consumed by global layers; flag when excessive. Fix: trim Preferences to universal essentials, review Skill installations for relevance, consider MCP deferred loading configuration.

### Layer Relationships to root.node Methodology

The sections that follow in this file map to specific layers: System Prompt Architecture → Layer 6, Memory Layer Design → Layer 8, User Preference Optimization → Layer 1, Evolutionary Optimization Principles → cross-layer (pathways span Layers 1, 3, 4, 6-8), Knowledge File Design → Layer 7, Context Budget Principles → Layer 7 sizing with Layer 4/5 overhead analysis. The Behavioral Tendencies section applies to Layer 6 content (countermeasures in CI) but the tendencies manifest across all layers and are calibrated by deployment context (chat / Projects / Claude Code / API). The Common Structural Fixes section addresses primarily Layers 6-8, with the Context Layer Rebalancing fix spanning Layers 6-8 and Memory. The Cross-Layer Failure Modes above extend optimization to the full nine-layer stack.

---

## System Prompt Architecture

The optimal system prompt follows a 5-layer structure with primacy-recency ordering. The most critical content goes at the top (identity, hard constraints) and bottom (output standards, quality checks) where Claude attends most strongly. The middle carries context and operational detail.

### The Architecture Pattern

```
TOP (highest attention):
  Layer 1 — Identity: who Claude is for this Project
  Layer 2 — Core Rules: non-negotiable behavioral constraints

MIDDLE (reliable but lower priority than edges):
  Layer 3 — Knowledge File Guide: routing descriptions for each file
  Layer 4 — Operational Modes: distinct behaviors for different task types

BOTTOM (high attention, closest to generation):
  Layer 5 — Output Standards: quality criteria, format defaults, verification checks
```

### Layer-by-Layer Guidance

**Layer 1 — Identity.** Should specify: role, seniority level, domain expertise, analytical disposition, and one behavioral sentence addressing the most likely failure mode. Must be broad enough for all operational modes but specific enough to produce distinctive output. The blind test: could someone reading the output alone reconstruct what role Claude was playing?

**Layer 2 — Core Rules.** Should contain 3-7 non-negotiable behavioral rules. Each rule should address a specific need — not restate generic best practices. Write as directives, not suggestions. Use the principle/default distinction: hard rules are stated as rules ("Never fabricate statistics"), preferences are stated as defaults ("Default to prose; use lists only for genuinely parallel items"). Fewer rules followed consistently beats many rules followed sporadically.

**Note on instruction weight for current models (Opus 5 and Sonnet 5):** Opus 5 and Sonnet 5 follow instructions precisely — over-specified prompts produce rigid outputs rather than smoothed-over ones. Instructions that needed emphasis in pre-4.6 models (capitalization, repetition, "CRITICAL" prefixes) should be written in normal-weight language. Emphatic legacy language now causes over-compliance. Replace `MUST`, `ALWAYS`, `CRITICAL`, `NEVER` with calibrated guidance. **Exception on chat-interface deployments:** where you are specifically countering tendency 1b (persistent-preference dilution) or 7b (tool under-triggering), explicit enforcement language remains appropriate. See the Behavioral Tendencies section for details.

**Layer 3 — Knowledge File Guide.** Each file gets a name, a one-sentence purpose description, and a routing signal: "Consult this when [specific trigger condition]." Routing descriptions should be functional, not decorative — they tell Claude when a file is relevant, not just what it contains. Every file in the Project must appear here.

**Layer 4 — Operational Modes.** Each mode needs: a trigger condition (how Claude recognizes this mode applies), distinct behavioral instructions, a reasoning approach appropriate to the task type, and an output structure. Modes should pass the differentiation test: would the same input produce noticeably different output across modes? If not, the modes are cosmetic and should be consolidated.

**Layer 5 — Output Standards.** Should include: format defaults (prose vs. structured), length guidance, tone calibration, audience-specific adjustments, and a pre-response verification check that grounds against external artifacts (not self-directed re-checking — see tendency #11). Positioned at the bottom to leverage the recency effect — these instructions are closest to where Claude begins generating.

### XML Tag Structure

Use XML tags for section boundaries in the system prompt. Claude was trained to attend strongly to XML tags, making them the most reliable structural delimiter.

Standard tag set:
- `<identity>` — role and expertise
- `<core_rules>` — behavioral constraints
- `<knowledge_files>` — file routing guide
- `<operational_modes>` — mode definitions
- `<output_standards>` — quality criteria and format defaults

Within modes, nest subsections with descriptive names rather than generic tags. Tags create unambiguous boundaries — use them wherever sections need clear separation.

---

## Behavioral Tendencies and Countermeasures

The tendency taxonomy expanded for Opus 5. Verbosity refactored into a three-surface family (#3a/#3b/#3c) with distinct triggers and countermeasures. Four new tendencies added for Opus 5 (#11–#14). Two prompt/environment-conditional defects are treated separately at the end of this section rather than as model tendencies. Total: 14 model tendencies + 2 non-tendency defects.

During audits, check whether the Project's domain and deployment context is likely to trigger each tendency, and whether an appropriate countermeasure is present. Countermeasure calibration varies by deployment — a countermeasure essential on the chat interface may be wasted tokens on Claude Code, and Opus 5's new tendencies (#11–#14) surface strongly on Claude Code specifically because that is where agentic workloads run.

### The Deployment Context Model

Countermeasure relevance varies by deployment surface. Four contexts matter:

| Deployment | Default Effort | Tendency Surface |
|---|---|---|
| Chat interface (claude.ai web/mobile) | Adaptive | HIGH for #1b, #7b, #9, #10; MEDIUM for #1a, #3a, #14 |
| Claude Projects | Adaptive (CI anchors) | MEDIUM for #1b, #9, #14; LOW for most others |
| Claude Code | `high` default (Opus 5 / Sonnet 5) | HIGH for #11, #12, #13; LOW for chat-interface-specific tendencies |
| API | Developer-controlled effort; developer-selected model | Depends on effort level and model |

Each tendency below includes a deployment calibration line indicating where it most strongly applies. Before applying a countermeasure, identify the Project's deployment context.

**Note on Claude Code applicability (per-Skill, not universal).** The Claude Code column in each tendency's deployment calibration below applies at the Project / prompt design level. For Skill design decisions (description optimization, 250-char listing cap, trigger language), Claude Code applicability is per-Skill — some Skills are first-class Claude Code targets, others are Claude.ai Projects-native and out-of-domain for Claude Code users. See `root_SKILL_PORTABILITY_TIER_ASSIGNMENTS.md` for HIGH / MEDIUM / LOW / NONE classifications.

**Note on countermeasure language design.** Countermeasure effectiveness depends not just on *what* the countermeasure says but *how* it says it. LLMs respond to the same persuasion principles as humans: authority framing ("YOU MUST," "No exceptions"), commitment mechanisms (requiring announcement before action, creating TodoWrite checklists), scarcity framing ("BEFORE proceeding"), and social proof. Research (Meincke et al. 2025, N=28,000 AI conversations) found that persuasion techniques more than doubled LLM compliance rates (33% → 72%, p < .001). The countermeasure templates below implicitly use authority and commitment framing — the note here makes the mechanism explicit so that users writing custom countermeasures can apply the same principles deliberately. Strong imperative language is appropriate for discipline-enforcing countermeasures (#1, #5, #7b, #10, #12); calibrated language is appropriate for tendency reduction where overcorrection is the risk (#3a verbosity, #6 over-exploration). **For over-verification (#11), the countermeasure is REMOVAL of instructions — a new countermeasure shape.**

### 1. Agreeableness Bias

**What it looks like:** Claude agrees with the user's framing even when the framing is flawed. Accepts stated premises without examination. Validates the user's preferred approach rather than evaluating it objectively.

**Two facets:**

**1a — Output-content agreeableness.** Validating user ideas in responses ("Great question!", "That's a solid approach"), opening with premise validation, softening disagreement under follow-up. Reduced in Opus 5 but not eliminated.

**1b — Persistent-preference dilution.** Configured preferences (User Preferences, Project CI rules) are weighted less heavily against immediate-prompt framing as conversations extend. Configured rules hold for the first several turns then gradually drift in long chat sessions.

**Domains most affected:** Advisory and strategy projects (where users state preferred directions), evaluation projects (where the user has a position), coaching projects, any project deployed on the chat interface with substantive User Preferences (1b).

**Countermeasure for 1a:**
```
If the premise of a request contains errors, flawed assumptions, or a better
alternative framing, say so directly before proceeding. Do not execute a
flawed request without comment. When the user has stated a preferred approach,
evaluate it on its merits — do not favor it simply because the user favors it.
```

**Countermeasure for 1b (chat interface and Projects):**
```
Treat User Preferences and Project Custom Instructions as equal-priority
constraints to user messages. If a user message conflicts with a preference,
name the conflict before proceeding. Do not silently drop preferences over a
long conversation. At every turn, the full Preference and CI ruleset applies.
```

**Placement:** 1a in identity block or core rules. 1b in core rules at the high-attention top, with optional reinforcement in output standards for projects with extended conversation patterns.

**Deployment calibration:**
- Chat interface (Adaptive): HIGH for 1b, MEDIUM for 1a
- Claude Projects: MEDIUM for 1b, LOW for 1a
- Claude Code: LOW for both
- API (effort ≥ high): LOW for both

### 2. Hedging and Over-Qualification

**What it looks like:** Findings are qualified. Conclusions are softened. Recommendations come with cascading caveats. Language patterns: "it depends," "there are many factors," "this is just one perspective," "it's worth considering." Well-controlled on Opus 5 for factual claims; persists on editorial and recommendation framings.

**Domains most affected:** Research and analysis projects (advisory framings specifically), health and medical adjacent projects, financial advisory projects, any domain where Claude perceives liability risk.

**Countermeasure template:**
```
Be direct and decisive in your recommendations. Where the evidence is clear,
state your position without hedging. Reserve caveats for genuinely uncertain
areas. When you do caveat, be specific about what is uncertain and why —
do not hedge on well-established facts or best practices.
```

**Placement:** Core rules or output standards. For research-heavy projects, reinforce in the identity block with language like "You state conclusions clearly and present limitations in a dedicated section rather than qualifying every sentence."

**Deployment calibration:**
- Chat interface (Adaptive): MEDIUM (advisory framings)
- Claude Projects: MEDIUM (advisory framings)
- Claude Code: LOW
- API (effort ≥ high): LOW

### 3. Verbosity — three-surface family (refactored for Opus 5)

Opus 5's default responses are longer than Opus 4.8 on multiple surfaces. The verbosity tendency refactored into three distinct surfaces with different triggers and countermeasures. Applying a single verbosity countermeasure now under-fits at least one surface — treat 3a, 3b, and 3c as separate diagnostic targets.

**Effort does not shorten responses.** The `effort` parameter controls how much the model **thinks**, not how much it **says**. Lowering effort can reduce thinking volume without reliably shortening the visible response. Prompt for response length explicitly.

#### 3a. Conversational response length

Default user-facing responses run longer on Opus 5.

**Countermeasure:**
```
Keep responses focused, brief, and concise. Keep disclaimers and caveats short,
and spend most of the response on the main answer. When asked to explain
something, give a high-level summary unless an in-depth explanation is
specifically requested.
```

In a long system prompt, pair the primary concision instruction with a short reminder near the end:
```
<tone_preference>Keep outputs reasonably concise.</tone_preference>
```

**Deployment calibration:**
- Chat interface: MEDIUM
- Projects: MEDIUM
- Claude Code: LOW (most workloads are agentic where 3b dominates)
- API (effort ≥ high): MEDIUM

#### 3b. Agentic progress narration

Opus 5 narrates readily during agentic work — announcing what it is about to do and giving longer per-message output in agentic sessions than prior models.

**Countermeasure — describe the cadence and shape (positive examples beat prohibitions):**
```
Before your first tool call, say in one sentence what you're about to do.
While working, give a brief update only when you find something important
or change direction. When you finish, lead with the outcome: your first
sentence should answer "what happened" or "what did you find," with
supporting detail after it for readers who want it.
```

**Deployment calibration:**
- Chat interface: LOW (agentic surfaces are elsewhere)
- Projects: LOW
- Claude Code: HIGH (this is where agentic sessions live)
- API (agent workloads): HIGH

#### 3c. Written-deliverable length

Files that Opus 5 writes to disk (reports, Markdown documents, summaries) are often longer than on prior models — separate from conversational verbosity.

**Countermeasure — explicit length calibration:**
```
Match the length of written documents to what the task needs: cover the
substance, but do not pad with filler sections, redundant summaries, or
boilerplate.
```

**Deployment calibration:**
- Chat interface: MEDIUM (for Skills that author documents)
- Projects: HIGH (report-authoring Projects)
- Claude Code: HIGH (any Skill that writes .md files)
- API: HIGH (document-generation workloads)

### 4. List and Bullet Overuse

**What it looks like:** Claude converts narrative explanations into bullet points. Analytical prose becomes lists of points. Every response defaults to structured formats even when prose would be more appropriate and readable. Persists across Opus 4.6 → 4.7 → 4.8 → 5.

**Domains most affected:** All domains, but especially problematic in content/communications projects (where prose quality matters), advisory projects (where nuanced argument matters), and research projects (where synthesis requires connected reasoning).

**Countermeasure template:**
```
Write in connected prose paragraphs. Use lists only when the content is
genuinely a set of discrete, parallel items. Do not convert narrative
explanations, analytical reasoning, or recommendations into bullet points.
```

**Placement:** Output standards. For content-focused projects, reinforce in the identity block.

**Deployment calibration:**
- Chat interface (Adaptive): MEDIUM
- Claude Projects: MEDIUM
- Claude Code: LOW (code output is structurally formatted regardless)
- API (effort ≥ high): MEDIUM

### 5. Fabricated Precision (External-Fact)

**What it looks like:** Claude generates specific statistics, percentages, or quantitative claims about external facts (research findings, market data, citations, sources) that are not grounded in provided data. Outputs contain authoritative-sounding numbers that were confabulated. Particularly dangerous because the output looks credible.

**Scope:** external-fact fabrication only. Self-referential fabrication — claims about what the model has done, checked, or loaded — is a distinct failure mode tracked as tendency #10. Do not collapse the two into a single countermeasure; they have different mechanisms.

**Domains most affected:** Research and analysis projects, financial projects, health projects, any domain where specific numbers carry weight. The tendency persists in domains with thin training-data coverage or where pressure to produce specific numbers is high.

**Countermeasure template:**
```
Use only data explicitly provided. If you do not have a specific number, do
not estimate one — state what data would be needed. Never invent a statistic,
percentage, or quantitative claim to fill a gap in the available information.
```

**Placement:** Core rules (this is typically a non-negotiable constraint). For research-heavy projects, add a secondary check in output standards: "Before delivering, verify that every quantitative claim is grounded in the provided sources."

**Deployment calibration:**
- Chat interface (Adaptive): MEDIUM
- Claude Projects: MEDIUM
- Claude Code: LOW
- API (effort ≥ high): LOW

### 6. Over-Exploration (search breadth)

**What it looks like:** Claude pursues too many lines of investigation before producing output. It reads many files, runs multiple searches, explores tangential angles.

**Distinct from #12 (scope expansion):** #6 is search *breadth* within a defined task. #12 is delivering *beyond* the task. A prompt with both tendencies looks the same on the surface — "the model did too much" — but they have different fixes.

**Domains most affected:** Agentic projects, research projects, software engineering projects (where Claude may explore beyond the request), any project where Claude has access to tools and files.

**Countermeasure template:**
```
Only make changes that are directly requested or clearly necessary.
Keep solutions simple and focused. Don't add features, refactor code,
or make improvements beyond what was asked.
```

**Placement:** Core rules or output standards. For projects with tool access, add specific tool-use guidance: "Use [tool] when it would enhance your understanding of the problem — not as a default action on every request."

**Deployment calibration:**
- Chat interface (Adaptive): LOW
- Claude Projects: LOW
- Claude Code (`high` default): MEDIUM (higher-effort settings amplify exploration on complex tasks)
- API (effort = xhigh): MEDIUM

### 7. Tool Trigger Miscalibration — two facets

**Facet 7a — Tool over-triggering** (largely reduced on Opus 5).

Claude uses tools aggressively even when the task could be answered from existing context. Caused by system prompt instructions tuned for pre-4.6 models — emphatic tool-use language ("CRITICAL: You MUST use this tool," "ALWAYS search first," "Never answer without checking") triggered overcompliance in earlier models. Reduced at the Opus 5 model level but still triggered by emphatic legacy language.

**Domains most affected:** Any project with tool access where the system prompt was written for pre-4.6 models and has not been recalibrated.

**Countermeasure for 7a — not a template to add, but instructions to revise:**

Replace:
```
CRITICAL: You MUST use the search tool for ANY question about current data.
If in doubt, ALWAYS search. Never answer without searching first.
```

With:
```
Use the search tool when the question requires current data that may have
changed since your training. For well-established facts and concepts,
answer directly.
```

**Facet 7b — Tool under-triggering**.

On the chat interface at Adaptive effort, Skills can fail to fire on legitimate triggers because the model weights persistent context (Skill descriptions loaded via progressive disclosure) less heavily than immediate prompts. The user asks a question that should route to a specific Skill; the model answers from general reasoning without invoking the Skill.

This is the structural inverse of 7a — emphatic enforcement language is appropriate here, not in 7a.

**Domains most affected:** Any project on the chat interface that depends on Skill activation or User-Preference-specified tool use.

**Countermeasure for 7b — explicit tool-use enforcement clause:**
```
When User Preferences or Project Custom Instructions specify a tool that
should be used for a category of request, treat that specification as a hard
requirement, not a suggestion. Invoke the tool before responding. Do not
substitute general reasoning for the specified tool unless the tool is
unavailable in the current environment.
```

**Deployment calibration:**
- Chat interface (Adaptive): 7b is HIGH; 7a is LOW (legacy language should be removed)
- Claude Projects: 7b is MEDIUM (CI partially anchors)
- Claude Code: 7b is LOW
- API (effort ≥ high): 7b is LOW

**General principle:** Replace emphatic language (MUST, ALWAYS, CRITICAL, NEVER) with calibrated guidance for general tool use. Reserve emphatic language for the specific case where you need to override 7b on chat-interface deployments.

### 8. LaTeX Defaulting

**What it looks like:** Claude Opus defaults to LaTeX notation for mathematical expressions, equations, and technical explanations. Outputs contain `\frac{}{}`, `\sum`, `$...$`, and other LaTeX markup. Appropriate for academic and technical contexts; problematic for plain-text outputs, non-technical audiences, or downstream systems that do not render LaTeX. Persists across Opus generations.

**Domains most affected:** Financial projects, educational projects, any project involving quantitative analysis or mathematical expressions for non-academic audiences.

**Countermeasure template:**
```
Format all mathematical expressions in plain text. Do not use LaTeX,
MathJax, or markup notation such as \( \), $, or \frac{}{}.
Write math expressions using standard text characters (/ for division,
* for multiplication, ^ for exponents).
```

**Placement:** Output standards. Only needed when the output context does not render LaTeX.

**Deployment calibration:**
- Chat interface (Adaptive): MEDIUM (plain-text contexts), LOW (rendered contexts)
- Claude Projects: MEDIUM (plain-text), LOW (rendered)
- Claude Code: LOW (technical context where LaTeX is rare in code output)
- API (effort ≥ high): MEDIUM (depends on downstream rendering)

### 9. Editorial Drift

**What it looks like:** Claude produces unsolicited commentary on its own boundaries, the act of responding, or its constraints. Symptoms: meta-statements about what the model can or cannot do that were not asked for; disclaimers about response scope inserted into otherwise direct answers; preamble explaining why the model is approaching a question a particular way; closing commentary about what the user might want to consider next.

Most pronounced on the chat interface where Adaptive effort and the absence of tight CI scaffolding allow editorial content to leak into responses.

**Domains most affected:** Advisory and coaching projects, any project on the chat interface without strong output standards, projects with extensive User Preferences that the model attempts to acknowledge in responses.

**Countermeasure template:**
```
Do not add unsolicited commentary about your own boundaries, what you will
or won't do, or how you are approaching the response. Do not preamble with
explanations of your reasoning approach unless asked. Do not close with
suggestions about what the user might want next unless asked. Answer the
question; stop when the answer is complete.
```

**Placement:** Output standards (closest to generation, where editorial content is added).

**Deployment calibration:**
- Chat interface (Adaptive): HIGH
- Claude Projects: MEDIUM (CI mitigates)
- Claude Code: LOW
- API (effort ≥ high): LOW

### 10. Self-Referential Fabrication

**What it looks like:** Claude claims to have performed an action, checked a state, or inspected its own runtime context without actually doing so. The claim is plausibility-driven — it sounds like what the model should have done, but the action was not verified.

**Distinct from #5 (Fabricated Precision, External-Fact):** #5 is about content (statistics, sources, citations); #10 is about process (claims about what the model itself did).

**Symptom profile:**
- "I searched and found X" when no search was performed
- "I checked the Memory and confirmed Y" when Memory was not consulted
- "Per my system metadata, the model is Z" when metadata was not read
- "I loaded the file and see Q" when the file was not loaded
- Process claims appearing in support of conclusions already stated

**Asymmetric pattern:** fabrication appears in initial responses; honest correction appears under direct challenge. Same structural pattern as #1a agreeableness.

**Domains most affected:** Audit Skills, Memory-optimization Skills, context-budget Skills — any Skill or Project where the model reports on actions taken. Also any deployment where tool indicators are not visible to the user (API integrations specifically).

**Countermeasure template:**
```
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
```

**Placement:** Core rules (high-attention position to override the asymmetric default). For Projects deploying audit Skills or any Skill that reports on actions, this countermeasure is essentially universal.

**Deployment calibration:**
- Chat interface (Adaptive): HIGH
- Claude Projects: MEDIUM (CI partially anchors)
- Claude Code: LOW
- API (effort ≥ high): LOW

For the full countermeasure template with CI-level and User-Preferences-level variants, see `root_SELF_REFERENTIAL_FABRICATION_COUNTERMEASURE.md`.

### 11. Over-Verification (NEW in Opus 5)

**What it looks like:** Opus 5 verifies its own work automatically. Instructions telling it to "double-check your answer," "re-verify before responding," "include a final verification step," or "use a subagent to verify" compound with the model's own behavior and cause over-verification — token spend without a quality gain.

**Countermeasure — REMOVAL of self-directed re-checking instructions.**

This is a new countermeasure shape for the taxonomy: the fix is *removal of instructions*, not addition. Prompts that grew over multiple model generations often carry accumulated verification instructions layered on top of each other. On Opus 5, these compound rather than adding value.

**The critical distinction — self-directed re-checking vs external-artifact verification:**

- **Self-directed re-checking** (REMOVE) asks the model to re-examine its own reasoning or output with no new information. Opus 5 already does this. Instructing it compounds the behavior.
- **External-artifact verification** (KEEP, and keep imperative) asks the model to check a claim against a source outside its own output. Opus 5 does NOT automatically do this. It has to be told to.

**Remove (self-directed re-checking):**
```
double-check your answer
re-verify before responding
include a final verification step
use a subagent to verify your work
before presenting your final answer, verify your reasoning
```

**Keep and keep imperative (external-artifact verification):**
```
verify the file exists at the path claimed
check the rendered page — a stored-body assert is not proof of clean render
diff the artifact against the source
confirm the tag resolves against actual repo state
run the tests and verify they pass
grep for the symbol to confirm it exists before recommending it
```

**Deployment calibration:**
- Chat interface: MEDIUM (chat workloads are less verification-heavy)
- Claude Projects: MEDIUM
- Claude Code: HIGH (agentic workloads with verification scaffolding accumulated over prior model generations)
- API (agent workloads at effort ≥ high): HIGH

**Audit note:** the pattern set that identifies this tendency in existing prompts is `double-check`, `re-verify`, `verify your (own )?work`, `verification step`, `subagent to verify`, `check your answer`. Not every hit is a removal target — some phrasings are ambiguous (see external-artifact examples above). Classify item-by-item, do not batch-apply.

### 12. Scope Expansion (NEW in Opus 5)

**What it looks like:** Opus 5 expands the scope of a task, adding steps that weren't requested or applying its own judgment about what the task should be. This is deliverable-boundary drift.

**Distinct from #6 (over-exploration):** #6 is search breadth within a task; #12 is delivering beyond the task. A prompt with both tendencies produces work that is both wandering AND expanded. The fixes address different mechanisms.

**Countermeasure — constrain scope explicitly:**
```
Deliver what was asked, at the scope intended. Make routine judgment calls
yourself, and check in only when different readings of the request would
lead to materially different work. If the request seems mistaken or a better
approach exists, say so in a sentence and continue with the task as asked
rather than quietly narrowing, widening, or transforming it. Finish the
whole task, and stop short of actions that are clearly beyond what was asked.
```

**Placement:** Core rules for tightly-scoped Projects; output standards otherwise.

**Deployment calibration:**
- Chat interface: MEDIUM
- Claude Projects: MEDIUM
- Claude Code: HIGH (agentic sessions where the model can act on scope expansion by writing files, spawning subagents, etc.)
- API (agent workloads at effort ≥ high): HIGH

### 13. Subagent Over-Delegation (NEW in Opus 5)

**What it looks like:** Opus 5 delegates to subagents more readily than prior models. Delegation pays off on genuinely independent, sizeable tracks of work but multiplies cost and time when applied to small tasks. Also — and this is a load-bearing correction — Opus 5 will use a subagent to "verify" its own work, which is a specific form of over-verification (see #11) that costs a full subagent invocation for no quality gain.

**Countermeasure — cap delegation:**
```
Delegate to a subagent only for large tasks that are genuinely independent
and parallelizable, such as a wide multi-file investigation. Do not delegate
work you can finish yourself in a handful of tool calls, and do not use
subagents to verify or double-check your own work. If one subagent can
complete the task, use one rather than several, and keep spawn counts low.
```

**Deployment calibration:**
- Chat interface: N/A (no subagent surface)
- Claude Projects: N/A (no subagent surface)
- Claude Code: HIGH (this is the primary subagent surface)
- API (multi-agent workloads): HIGH

### 14. Correction Narration (NEW in Opus 5)

**What it looks like:** Opus 5 narrates corrections to its earlier statements more than prior models — including corrections that don't materially change the user's outcome.

**Countermeasure — restrict corrections to material ones:**
```
Only correct an earlier statement when the error would change the user's
code, conclusions, or decisions. State corrections plainly and briefly, then
continue the task. For slips that change nothing for the user, make the fix
and move on without noting it.
```

**Deployment calibration:**
- Chat interface: MEDIUM (extended conversations accumulate corrections)
- Claude Projects: MEDIUM
- Claude Code: LOW (agentic sessions are largely action-driven; correction narration is a smaller share)
- API: LOW

### Prompt/environment-conditional defects (not model tendencies)

Two failure modes track cleanly to the prompt or the runtime configuration rather than the model. They are handled by writing prompts differently or configuring the API differently, not by adding counter-tendency instructions.

#### Conservative-instruction literalism

Opus 5 follows "only report high-severity issues" or "be conservative" literally, which causes under-reporting. This is a **prompt defect** exposed by the model, not a model tendency.

**Fix — ask for everything, filter in a separate pass.** Rewrite review prompts to two stages: (1) report every issue found; (2) filter to the severity level or subset the user wants. Do not compress "report everything" and "filter to high severity" into one instruction. This applies to audit Skills (project-audit, full-stack-audit, prompt-validation, global-audit, repo-hygiene, critic-gate) in particular.

Sweep pattern for prompts that carry this defect: `only report`, `only flag`, `be conservative`, `high-severity` (as an instruction, not as an output label). Replace with report-everything-then-filter form.

#### Thinking-disabled output artifacts

With `thinking: {"type": "disabled"}` on Opus 5, two artifacts can occasionally appear in the model's visible output:

- **Tool calls as text.** The model writes a tool call into user-facing text instead of emitting a structured `tool_use` block. The call never runs; in agentic loops the leaked text stays in the conversation history and affects later turns. Most common on tool-heavy workloads such as search.
- **Internal XML tags in visible response.** `<thinking>` tags or other internal tags leak into the visible response.

Both are **API-configuration failure modes** — the fix is not to prompt around them but to keep thinking on and control cost via effort. For most tasks, thinking-on at `low` effort outperforms thinking-off at similar cost.

**Sub-finding — a system-prompt rule against thinking increases tag leakage.** Do NOT add instructions like "do not think" or "do not reason" to a system prompt while thinking is disabled — that instruction increases tag leakage rather than suppressing it. If a mitigation instruction is required (for integrations that must keep thinking disabled), use the general form rather than naming the tags:

```
When you use a tool, you may say a brief sentence first. If no tool can
express what the user asked for, say so instead of guessing. Do not include
internal or system XML tags in your response.
```

**Reminder — thinking-disabled breaking change on Opus 5:** `thinking: {"type": "disabled"}` is accepted only at effort `high` or below. Setting it at `xhigh` or `max` returns a 400 error. This is a breaking change vs Opus 4.8.

---

## Memory Layer Design Principles

Claude Projects have a Memory feature that stores always-loaded orientation facts about the user and project context. Memory edits appear in every conversation without requiring a search — they are part of the context Claude sees immediately. This makes Memory architecturally distinct from knowledge files, which are searchable reference material that Claude consults when triggered.

### The Complementary Layer Principle

Memory and knowledge files serve different functions and should contain different types of content. Memory holds always-loaded orientation: current phase, active constraints, key decisions, and identity facts that Claude needs in every conversation. Knowledge files hold searchable depth: decision rationale, checklists, procedural details, reference data, and institutional history. Neither replaces the other. A well-architected Project uses both layers appropriately; many Projects use only knowledge files and leave Memory unconfigured, which is a missed optimization opportunity.

### What Belongs in Memory

Memory should contain facts that meet two criteria: (1) they are relevant to most or all conversations in the Project, and (2) they are orientation-level — they tell Claude where things stand, not how to do things. Examples of good Memory content: the user's role and expertise level, the project's current phase, active constraints or blockers, key architectural decisions that shape all work, the relationship between this project and related projects, and recurring preferences that affect output calibration.

### What Does Not Belong in Memory

Reference-depth content belongs in knowledge files, not Memory. Signs that content is too deep for Memory: it explains *why* a decision was made (rationale belongs in a knowledge file), it contains procedural steps (processes belong in knowledge files), it would need to be read carefully rather than glanced at (depth signal), or it exceeds a few sentences for a single topic (sizing signal). Memory has a 30-edit limit with 100,000 characters per edit — the constraint is not typically on total size but on appropriateness. A Memory layer stuffed with reference content wastes always-loaded context on material that would be better searched when needed.

### Common Memory Failures

**Stale orientation.** Memory contains facts that were true at an earlier project phase but have since changed. This is the Memory-layer equivalent of the propagation failure — knowledge files get updated but Memory edits are not revisited. The fix is periodic Memory review, especially after significant project milestones.

**Reference-depth overload.** Memory contains detailed explanations, decision rationale, procedural steps, or other content that belongs in knowledge files. This wastes always-loaded context on material Claude only needs occasionally. The fix is to move the depth to a knowledge file and keep only the orientation-level summary in Memory.

**Absent Memory layer.** The Project has knowledge files but no Memory edits configured. Claude starts every conversation without the orientation context that would help it engage more effectively from the first message. For Projects with 3+ knowledge files or multi-phase history, configuring Memory with key orientation facts is a meaningful improvement.

**Duplication across layers.** The same facts appear in both Memory and knowledge files without a clear reason. This creates a coherence risk — if one is updated and the other is not, Claude sees conflicting information. Each fact should have one authoritative home. Memory holds the current-state summary; the knowledge file holds the history and rationale.

### Memory in the Project Lifecycle

Memory should be reviewed at natural project transitions: after completing a major phase, after significant architectural changes, and when the project's scope or direction shifts. The review asks three questions: Is everything in Memory still true? Is there new orientation-level context that should be added? Is anything in Memory now reference-depth and better served by a knowledge file?

For projects that include a build_context.md or equivalent institutional memory file, the complementary layer principle applies directly: Memory holds the current-state orientation, and build_context.md holds the searchable depth (build history, decision rationale, propagation checklists, self-optimization observations).

---

## User Preference Optimization Principles

User Preferences (Layer 1) are the highest-priority deliberate layer in the global scope. They load into every conversation — inside and outside Projects — making them the foundation that all other layers build on. Well-crafted Preferences reduce redundancy across Projects, establish consistent behavioral defaults, and improve output quality universally. Poorly crafted Preferences waste always-loaded context, create cross-layer conflicts, or silently degrade output in contexts they were not designed for.

### The Universality Test

Every instruction in User Preferences must pass the Universality Test: "Would this instruction improve output in every conversation and every Project, without degrading any of them?" If an instruction benefits one domain but is irrelevant or harmful in another, it fails the test and belongs in a Project CI, not in Preferences.

Examples of instructions that pass: "Be direct and decisive. State recommendations without hedging." This improves output everywhere. "When uncertain about a factual claim, say so directly rather than qualifying with caveats." Universal. "Produce complete files, never diffs or partial sections." Universal workflow preference.

Examples that fail: "Always include code examples in explanations." Helps engineering Projects, produces unnecessary code blocks in strategy and content work. "Use the MECE framework for all analysis." Useful for consulting but forced in creative or research contexts. "Prioritize SAP ECC integration patterns." Domain-specific — belongs in the relevant Project CI.

### What Makes Effective Preferences

Effective User Preferences share five structural qualities.

**Identity context, not identity instructions.** Preferences should state who the user is (role, expertise, domain), not who Claude should be. Claude's identity is set by each Project's CI. Preferences provide the context that helps Claude calibrate depth, vocabulary, and assumptions across all contexts. "I am a senior systems architect" tells Claude how to calibrate. "You are a senior systems architect" conflicts with Project identities.

**Behavioral defaults, not hard rules.** The best Preferences establish defaults that Projects can override when needed. "Default to prose over lists" sets a universal baseline that a data-heavy Project can override with "Use tables for comparison data." Hard rules ("NEVER use bullet points") create Style/CI Tension when a Project legitimately needs a different format.

**Communication calibration.** Tone, directness, depth level, and working style preferences that genuinely apply everywhere. These are the highest-value Preference content because they eliminate the need to restate communication rules in every Project CI.

**Evidence and uncertainty standards.** How the user wants Claude to handle unknowns, source claims, and confidence levels. These are almost always universal — a user who wants explicit uncertainty labeling in research contexts wants it everywhere.

**Lean over comprehensive.** Preferences consume always-loaded context in every conversation. Each instruction should earn its place. A Preferences block of 200-500 tokens that nails the universal behavioral defaults outperforms a 2,000-token block that mixes universal rules with domain-specific guidance. When in doubt, leave it out — the user can always add it to a specific Project CI.

### Common Preference Failures

**Preference/CI redundancy.** The same behavioral instruction appears in both Preferences and one or more Project CIs. The instruction loads twice in every conversation within those Projects, wasting context. This is the Redundant Layering failure mode. Symptom: unnecessary context consumption with no behavioral benefit. Fix: keep the instruction in one layer — Preferences if universal, CI if it has project-specific calibration that differs from the global default.

**Missing codification.** The user has stable behavioral patterns that Claude has learned through Memory synthesis but has never codified as explicit Preferences. The behavior is fragile — it depends on Memory continuing to capture the pattern. This is the Memory/Preference Confusion failure mode. Symptom: Claude follows the pattern in conversations where Memory is loaded but not in new conversations or Projects. Fix: promote the stable pattern to an explicit Preference.

**Domain leakage.** Preferences contain instructions that benefit one domain but degrade others. Common forms: project-specific terminology, methodology preferences that don't generalize, output format requirements that apply to one task type. Symptom: outputs that are over-engineered or off-target in domains the Preference wasn't written for. Fix: apply the Universality Test to every instruction; demote failing instructions to specific Project CIs.

**Identity confusion.** Preferences specify Claude's identity rather than the user's identity. Symptom: Project identities partially override but residual confusion appears in tone or framing. Fix: rewrite Preferences identity content to describe the user, not Claude.

**Bloat from accumulation.** Preferences grow over time as the user adds instructions for specific situations. Each addition seemed useful at the time, but the cumulative weight wastes always-loaded context and dilutes the most important instructions. Symptom: Preferences exceed 1,500 tokens with no clear organization. Fix: prune to the universal essentials, demote project-specific content, restructure around the five qualities above.

---

## Evolutionary Optimization Principles

When a user has built and maintained multiple Projects over time, the global layers (Preferences, Skills, Connectors, Memory) and Project layers (Custom Instructions, Knowledge Files, Memory) accumulate behavioral patterns that should evolve toward greater efficiency and coherence. Optimization is not a one-time fix; it is a continuous balancing of where instructions live based on their universality, stability, and reusability.

The more Projects a user builds and optimizes, the better their global layers should become. The Evolutionary Optimization Loop facilitates this through four directional pathways, each with a specific test, trigger condition, and mechanism. The Optimizer runs these pathways during Global Audit and Full Stack Audit modes (see PROJECT_OPTIMIZER.md), producing recommendations that the user implements.

### Pathway 1 — Promotion (Project → Global)

**Direction:** Project Custom Instructions → User Preferences.

**Trigger:** The same behavioral instruction or pattern appears in 3+ Projects.

**Test — The Universality Test:** "Would this instruction improve output in every conversation and every Project, without degrading any of them?" If yes, promote. If it would degrade even one context, it stays project-specific. (Full test specification in the User Preference Optimization section above.)

**Mechanism:** The Optimizer compares behavioral instructions across the user's Project portfolio. When it identifies a pattern appearing in three or more Projects, it applies the Universality Test and, if the pattern passes, produces a promotion recommendation with drafted User Preferences text and instructions to remove the duplicated instruction from each Project CI.

**Example:** Three Projects all include "When uncertain about a factual claim, say so directly rather than hedging with qualifiers." This passes the Universality Test — it improves output everywhere. Promote to User Preferences.

### Pathway 2 — Demotion (Global → Project)

**Direction:** User Preferences → Project Custom Instructions.

**Trigger:** A User Preference is project-specific — it benefits one domain but is irrelevant or harmful in others.

**Test — The Specificity Test:** "Is there any Project or conversation context where this instruction would make output worse or be irrelevant?" If yes, demote. The threshold is any context, not most contexts — a Preference that degrades even one active Project context fails and should be demoted to the Projects where it is beneficial.

**Mechanism:** The Optimizer scans User Preferences during Global Audit. For each instruction, it evaluates whether the instruction is truly universal by checking it against the user's known Project portfolio and general conversation contexts. When an instruction fails the Specificity Test, the Optimizer identifies which Projects benefit from the instruction and recommends removal from Preferences with placement into those specific Project CIs.

**Example:** User Preferences includes "Always include code examples in explanations." This helps in software engineering Projects but produces unnecessary code blocks in strategy consulting and content writing Projects. Demote to the relevant engineering Project CI.

### Pathway 3 — Codification (Memory → Preferences/CI)

**Direction:** Global Memory or Project Memory → User Preferences or Project Custom Instructions.

**Trigger:** Memory has accumulated a stable behavioral pattern that the user hasn't explicitly codified as a deliberate instruction.

**Test — The Stability Test:** "Has this pattern appeared consistently across multiple Memory synthesis cycles without the user contradicting it?" The test has two components: (1) Persistence — the pattern has survived multiple Memory updates without being overridden or modified. (2) Intentionality — the pattern reflects a genuine user preference, not an artifact of Memory synthesis (e.g., Memory recording a one-time request as a permanent preference). If both pass, codify. The destination depends on scope: patterns that are universally applicable go to User Preferences (and must also pass the Universality Test); patterns that are project-specific go to the relevant Project CI.

**Mechanism:** The Optimizer scans Memory contents during Global Audit or Full Stack Audit. It identifies entries that express behavioral preferences, corrections, or working style observations — as opposed to factual context. For each behavioral entry, it applies the Stability Test. Stable patterns become codification recommendations specifying the destination layer (Preferences or specific Project CI) and the drafted instruction text.

**Example:** Global Memory has noted across several conversations that the user prefers responses to start with the answer rather than context-setting. This has persisted across multiple Memory synthesis cycles. It passes the Stability Test and the Universality Test. Codify as an explicit User Preference: "Lead with the answer or recommendation. Provide supporting context after, not before."

### Pathway 4 — Skill Extraction (Knowledge File → Skill)

**Direction:** Project Knowledge Files → Installed Skills.

**Trigger:** Procedural knowledge in a Project's knowledge files would benefit multiple contexts, and the procedure follows a repeatable, task-triggered pattern.

**Test — The Portability Test:** Three criteria must all pass: (1) Task-triggered — the procedure activates based on a recognizable task type (e.g., "when reviewing code," "when writing a memo"), not based on project-specific context. (2) Context-independent — the procedure produces correct results without access to the originating Project's other knowledge files or CI. (3) Multi-project utility — at least two current Projects would benefit from the procedure, or the procedure addresses a common task type the user performs across contexts.

**Mechanism:** The Optimizer scans knowledge files during Full Stack Audit. It identifies procedural content — step-by-step instructions, checklists, decision trees, evaluation rubrics — that matches the Skill pattern. For each candidate, it applies the Portability Test. Candidates that pass receive a Skill extraction recommendation including: a draft Skill description field with trigger and negative-trigger language, the content to extract, any adaptation notes for making the content Skill-appropriate (Skills are behavioral instructions, not raw reference data), and composition considerations if the new Skill might interact with existing installed Skills.

**Example:** A content writing Project contains a detailed editorial review checklist in a knowledge file. The same checklist would be valuable in any Project that involves writing. It passes the Portability Test — task-triggered by review requests, context-independent (no project-specific references), and useful in multiple Projects. Extract as a Skill that activates when Claude is asked to review written content.

### Cross-Project Pattern Analysis

Cross-Project Pattern Analysis is the comparative methodology that feeds the Promotion and Demotion pathways. It requires Custom Instructions from three or more Projects to produce meaningful results.

**Analysis steps:**

1. Extract behavioral instructions from each Project CI. Behavioral instructions are rules that govern how Claude behaves (tone, approach, constraints, output format) as opposed to domain-specific knowledge routing or mode definitions. Focus on the identity block and core rules sections.

2. Normalize for semantic equivalence. Different Projects may express the same behavioral intent in different words. Group instructions that produce the same behavioral effect even if the phrasing differs. Examples of semantic equivalents: "Be direct and avoid hedging" / "State recommendations without softening qualifiers" / "When the evidence is clear, commit to a position."

3. Identify cross-project patterns. Flag any behavioral instruction or semantic cluster that appears in three or more Projects. These are promotion candidates.

4. Apply the Universality Test to each candidate. Not all repeated patterns should be promoted. An instruction might appear in three engineering Projects but would be harmful in a creative writing Project. The test is against the user's full context, not just the Projects where the pattern appears.

5. Identify demotion candidates by reversing the lens. Check User Preferences against the Project portfolio. Any Preference instruction that benefits only a subset of Projects is a demotion candidate — apply the Specificity Test.

### The Maturity Model

The four pathways create a maturity trajectory for the user's Claude environment.

**Stage 1 — Sparse Global, Heavy Project.** New user. User Preferences are minimal or empty. Each Project carries all its own weight — every behavioral rule is stated in every Project CI. Memory is just beginning to accumulate. No cross-project optimization has occurred.

**Stage 2 — Emerging Patterns.** User has 3-5 Projects. The Optimizer begins identifying repeated behavioral instructions across Projects. First promotion candidates emerge. Memory has stabilized some patterns worth codifying. Cross-Project Duplication is the dominant waste pattern.

**Stage 3 — Optimized Foundation.** User Preferences contain a refined set of universal behavioral rules. Projects are leaner because they don't repeat global defaults. Skills have been extracted from repeated procedural patterns. Memory and Preferences are clearly delineated (automatic context vs. deliberate rules). The user's Projects start faster and perform better because the global foundation is calibrated.

**Stage 4 — Self-Reinforcing System.** Each new Project benefits from the refined global foundation. Projects need only project-specific instructions — the universal behavioral baseline is handled by Preferences. The Optimizer's role shifts from foundational fixes to incremental alignment checks and evolutionary recommendations as the user's needs evolve.

---

## Knowledge File Design Principles

### The One-Purpose Rule

Each knowledge file should serve exactly one purpose. The test: describe the file's purpose in one sentence. If the description requires "and" to connect two different purposes, the file should be split. If two files have overlapping one-sentence descriptions, they should be combined.

### Sizing Guidance

A file that is too large (covering multiple topics) loses the one-purpose focus and makes routing ambiguous. A file that is too small (a few paragraphs) probably should be a section within another file. The right size is determined by the purpose — the file contains everything needed for its purpose and nothing beyond it.

### Naming Convention

File names should be descriptive enough that Claude can use them as context signals. `company_context.md` communicates more than `info.md`. `workout_program.md` communicates more than `data2.md`. Name files for their purpose, not their type or sequence.

### Front-Loading

Claude attends most strongly to the first few paragraphs of a file. Place the highest-value content — key definitions, critical rules, summary information — at the top. Place detailed reference material, edge cases, and extended examples further down.

### The Instruction/Reference Boundary

Behavioral instructions ("always do X," "never do Y") belong in Custom Instructions, not in knowledge files. Knowledge files contain reference material — information Claude draws from. When a knowledge file must contain procedural instructions (like a process documentation file), the system prompt should explicitly delegate authority: "When performing [task type], follow the procedures in [file name]."

---

## Context Budget Principles

Anthropic Projects operate in one of two modes depending on the knowledge file load relative to the underlying model's context window: **full-context loading** (all knowledge files injected into the context window simultaneously) or **retrieval mode** (files searched on demand via `project_knowledge_search`). The transition is **automatic and window-relative** — RAG activates when your project approaches or exceeds what fits in the model's context window, not at a fixed token threshold.

The optimization objective is to maximize the quality of Claude's content access for the project's actual workload. Full-context loading is optimal for projects that depend on cross-file reasoning — Claude can connect content across files in a single generation. Retrieval mode loses this capability but offers greater capacity and works well when queries target specific documents rather than requiring cross-file synthesis. Both are valid architectures. The right target depends on the project's workload, not on a universal preference for full-context.

**Sources:** Anthropic support article — `support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects` (verbatim: "RAG automatically activates when your project approaches or exceeds the context window limits"). Landscape reference: `root_CLAUDE_OPTIMIZATION_NOTES.md` §3.

### Context window is not the RAG threshold — a preserved distinction

Under the 200K-window era, the RAG threshold was numerically entangled with the window (empirically ~66,500 tokens on 200K plans, roughly a third of the window). That made the fixed number look like a stable rule of thumb, and it conflated two concepts that are conceptually distinct:

- **Context window** — the model's maximum input capacity (measured in tokens per model; 1M for current top-tier models, 200K for Haiku 4.5).
- **RAG threshold** — the platform-side decision point where Projects switch from full-context loading to retrieval mode. Now tracks the window (automatic per current article), rather than being a fraction of it.

Under 1M-window models, the RAG threshold has moved with the window. State the two separately in prompt/Project design; do not carry the ~66,500 figure forward as a live threshold. See "Historical context" below for the measurement that produced that figure and why it is preserved as history but not as current-state guidance.

### The Two Modes

**Full-context mode.** All knowledge files loaded into every turn. Cross-file reasoning fully available. Chunk coherence is not a concern (the whole file is present). Optimization focus: file organization, one-purpose-per-file, front-loading of critical content.

**Retrieval mode.** `project_knowledge_search` tool present in Claude's available tools; knowledge is retrieved as chunks per query. Cross-file reasoning loses guaranteed simultaneity. Optimization focus: chunk coherence, routing description quality, retrieval pool signal-to-noise, migration of behavioral content to always-loaded layers (Skills, CI, Memory).

**Detection.** The presence of `project_knowledge_search` in Claude's available tools is the reliable indicator that retrieval mode is active. In full-context mode, this tool is absent. The UI also shows a visual indicator ("Indexing" label in the files panel). For programmatic detection in a Project, check whether the system prompt includes the search tool.

### What triggers RAG activation

**Trigger:** Knowledge base approaches or exceeds the underlying model's context window.

The threshold is window-relative — a Project that loads full-context under Opus 5's 1M window may switch to retrieval under Haiku 4.5's 200K window. Neither the article nor the current models overview publishes per-model threshold numbers. If a specific number matters for architectural decisions on a specific project, measure empirically (see "Empirical Threshold Measurement" below).

**Threshold-exempt overhead.** Skills, MCP integrations, Custom Instructions, Memory, and User Preferences consume conversation budget but are not part of the knowledge-file total that triggers RAG activation. Adding or removing them cannot switch a Project between modes. This distinction was true under the 200K-era platform (empirically confirmed) and remains true under current platform behavior; the split between "knowledge budget" (triggers RAG) and "conversation budget" (does not) survives the platform change.

### Historical context — the ~66,500 measurement

The `~66,500 token RAG threshold` figure that appears in prior root.node documentation is a specific empirical measurement from Phase 22 (April 2026 calibration lab): under the 200K context window (Pro/Max/Team plans at the time), against Opus 4.6, the RAG activation point was at approximately 66,500 tokens of knowledge files — roughly 33% of the 200K window. That was a valid, measured number for its era.

Under the current platform (automatic-by-window on 1M-window primary models):
- The 66,500 figure no longer represents current-state RAG behavior.
- The 33% ratio was an artifact of the 200K-window era; there is no evidence it holds for 1M-window models.
- Projects that were calibrated to sit comfortably under 66,500 are far below the current threshold (whatever it is) on any 1M-window model.

Where prior documentation states the 66,500 figure as a historical measurement in past tense, it is correct. Where it states the figure as a current-state operational rule, it is stale. The distinction matters for context-budget audit calibration in current-era Projects.

### Token Estimation

Claude cannot count tokens precisely but can estimate with sufficient accuracy for architectural decisions. Rough conversion for English prose: approximately 4 characters per token; structured content (XML, code, tables) at approximately 3.25 characters per token; mixed markdown at approximately 3.75 characters per token. One page of prose is roughly 500 words, 3,000 characters, or 750 tokens.

**Tokenizer notes for current models:**
- **Fable 5** uses the tokenizer introduced with Opus 4.7 — compared to models before Opus 4.7, the same text produces roughly 30% more tokens (Anthropic's models overview page).
- **Sonnet 5** produces approximately 30% more tokens per unit of content than Sonnet 4.6 (Anthropic's whats-new page: "approximately 30% more tokens than on Claude Sonnet 4.6").
- **Opus 5** tokenizer specifics were not fully re-baselined in the v4.0 alignment cycle. Treat measurements with explicit tolerance until re-baselined via `count_tokens`.

Estimates are approximate. For architectural decisions where precise numbers matter (borderline threshold cases, empirical measurement), use `count_tokens` against the target model rather than character-based heuristics.

To estimate a project's knowledge file token load in Anthropic Projects: run `ls -la /mnt/project/` for byte sizes, divide each by 4, and sum. GitHub-connected repositories loaded as knowledge sources count toward this total — they are functionally equivalent to uploaded files.

### Conversation Budget Components

While threshold-exempt (do not trigger RAG), these components still matter for conversation quality:

- **Platform system prompt** (~20–25K tokens): Non-removable. Includes behavior rules, search/copyright instructions, tool schemas, computer use instructions, memory system, past chats, visualizer, and Skills catalog. This baseline is relatively stable.
- **MCP integrations** (variable — depends on loading mode): MCP connector overhead varies dramatically based on the loading mode. Three patterns exist. (1) **Always-loaded:** Full tool schemas injected every turn. ~3K for simple connectors (2–3 tools) to ~15K+ for complex ones (20+ tools). (2) **Deferred / load-as-needed:** Tools listed by name and brief description (~40–60 tokens each) in a lightweight catalog; full schemas load on demand via tool search. The deferred infrastructure adds a flat ~5–7K tokens regardless of connector count — an ~85% reduction versus always-loaded. This is the standard mode in claude.ai when connectors are set to "load as needed." (3) **Hybrid:** Some connectors always-load a few primary tools while deferring the rest. With deferred loading (the common case), 8 connectors typically add ~8–12K total, not ~40–80K. Dynamic overhead also accrues within a conversation as deferred tools are activated and tool results accumulate in history.
- **Skills** (minimal per skill): Only skill name and description (~30–50 tokens each) load at startup. Full SKILL.md loads on demand when triggered. The startup cost of 16 skills is roughly 500–800 tokens — negligible for budget purposes.
- **Custom Instructions** (variable): The system prompt text. Estimate with bytes ÷ 4.
- **Memory** (typically 500–3K tokens): Manual edits plus auto-generated entries.
- **User Preferences** (200–1,500 tokens): Global preference text.

Overhead affects context quality on every turn: as total context grows, the model's attention per token decreases (context rot). Minimizing unnecessary overhead improves output quality even when the conversation window appears healthy.

### Context Window Sizes by Plan

| Plan | Context Window | Notes |
|---|---|---|
| Pro / Max | 200K–1M tokens (plan-dependent; consult current Anthropic plan documentation) | RAG threshold is automatic per window |
| Team / Enterprise | Plan-dependent | RAG threshold is automatic per window |
| API (Opus 5, Sonnet 5, Fable 5) | 1M tokens (default AND max; no smaller variant on Opus 5) | User-controlled context; no platform RAG |
| API (Haiku 4.5) | 200K tokens | User-controlled context; no platform RAG |

The context window is plan-dependent. The Projects RAG threshold now tracks the window (per the support article), rather than being a fixed number. Consult Anthropic's plan documentation for current per-plan windows; the numbers move with product changes.

### Context Pressure vs. RAG Switching

These are two distinct mechanisms that operate independently:

| Mechanism | Trigger | Effect | Scope |
|---|---|---|---|
| **RAG switching** | Knowledge files approach or exceed the model's context window | Changes how knowledge is loaded (all vs. retrieved chunks) | Project-level, static per configuration |
| **Context pressure** | Cumulative context approaches window limit during conversation | Earlier messages truncated or summarized via compaction | Conversation-level, dynamic per turn |

Context pressure affects conversation quality — earlier context is lost as the conversation grows. RAG switching affects knowledge access quality — retrieval returns fragments instead of complete files. A project can experience both simultaneously (large knowledge base in RAG mode with a long conversation causing compaction) or either independently.

Under 200K-window models (Haiku 4.5) both mechanisms sit closer together numerically. Under 1M-window models (Fable 5, Opus 5, Sonnet 5), the two mechanisms sit further apart in absolute terms — a Project can be well under the RAG threshold while a long agentic conversation still triggers compaction.

### When Retrieval Mode Is the Right Architecture

Retrieval mode is the appropriate architecture for projects that primarily query individual documents — documentation sets, knowledge bases, reference manuals, large codebases. Testing with 113 articles (April 2026, under 200K-era platform) showed accurate semantic retrieval for focused queries.

The quality concern is specific to projects that depend on cross-file reasoning, where Claude needs simultaneous awareness of multiple files to produce correct output. For these projects, full-context loading is worth pursuing if achievable. When it is not achievable, the mitigation is architectural: consolidate cross-dependent content into fewer files to eliminate cross-file dependencies, move independent content to Skills, and ensure the remaining knowledge files are self-contained.

Under 1M-window primary models, more Projects can operate in full-context mode than under the 200K era. Recheck a Project's current mode by looking for `project_knowledge_search` — a Project that was in retrieval mode under the 200K era may have moved to full-context under Opus 5 / Sonnet 5 without any content changes.

### API Deployment as Alternative Architecture

For knowledge bases and workloads where Anthropic Projects' automatic RAG behavior doesn't fit the use case (very large content volumes with cross-document synthesis requirements, or explicit control over retrieval), an API-based deployment provides a different architecture: 1M-token windows on Opus 5, Sonnet 5, Fable 5; developer control over what enters context; no platform-imposed RAG.

Tradeoffs are significant. Cost is substantially higher (per-token billing on massive inputs every turn). Latency increases with context size (30–60+ seconds at high token counts). Accuracy and recall degrade as total context grows toward 1M (context rot). The lost-in-the-middle effect reduces recall of content positioned in the middle of very large contexts. The user owns the full stack — conversation management, retrieval logic, memory persistence, and all platform features must be built and maintained.

API deployment is not a casual escalation from Claude Projects. It is a different product architecture with different economics and engineering requirements. Recommend it only when the content volume and cross-document synthesis requirements make Anthropic Projects genuinely unworkable.

### Empirical Threshold Measurement

The most reliable way to determine a project's exact RAG activation point on the current platform is empirical testing.

**Quick method (±1,000 tokens precision):** Note the project's current knowledge file byte total. If in full-context mode, add knowledge files until the "Indexing" indicator appears in the project UI. If in retrieval mode, remove knowledge files until "Indexing" disappears. The boundary in total knowledge file bytes, divided by 4, gives the approximate threshold in tokens for that project's configuration.

**Precision method (±50–100 tokens):** Requires pre-sized calibration files at known token counts. Add or remove calibration files to binary-search the exact trigger point.

**When to recommend empirical measurement:** When a project is borderline and feasibility depends on precise numbers. When unexpected RAG activation occurs with no knowledge file changes (suggests a platform-side change or a plan/model change). After major Anthropic model or platform updates that may shift the threshold. Note that under automatic-by-window behavior, the threshold may move whenever Anthropic ships model or platform changes; a measurement is a point-in-time snapshot.

### Feasibility Assessment for Full-Context Recovery

When a project is in retrieval mode, the first question is whether full-context loading is a realistic target. This assessment determines the optimization strategy.

**Step 1: Determine current mode and estimated load.** Check for `project_knowledge_search` presence to confirm current mode. Estimate the project's knowledge file token load using the character-to-token heuristics.

**Step 2: Determine whether the current mode was set under an older plan or model.** Under 1M-window models, a Project that was in retrieval mode under a 200K plan may already be in full-context mode without any content changes. Verify current state before optimizing.

**Step 3: Identify available reductions.** Using the placement tier analysis, estimate the token savings from each optimization priority: archiving Tier 3 files, relocating Tier 2 files to Skills or other layers, and compressing Tier 1 files. Sum the projected savings.

**Step 4: Classify feasibility.**

*Recovery Achievable* — projected reductions bring the project below the estimated (or empirically measured) threshold without removing content critical to the project's core function. Under 1M-window primary models, most historically-retrieval-mode Projects fall into this category with modest cleanup. Typical profile: Project was calibrated to a 200K-era threshold and now has substantial headroom on 1M models.

*Borderline* — projected reductions bring the project close to the threshold but require trade-offs: removing content that is used occasionally, consolidating files that serve different purposes, or compressing files where the quality impact is uncertain. Full-context is possible but not guaranteed, and the cost may exceed the benefit.

*Not Feasible* — the project's content volume exceeds the threshold by more than the available reductions can close, or the reductions required would remove content critical to the project's function. This includes projects at scales (hundreds of thousands of tokens or more) where even under 1M-window models, full-context is not the right architecture.

**Step 5: Set the strategy.**

If Recovery Achievable: optimize toward full-context as the primary objective. Execute the optimization priorities in order. RAG quality improvements are side benefits during the transition and serve as insurance if the threshold turns out to be lower than expected.

If Borderline: present both paths. Estimate the effort and trade-offs for full-context recovery. Estimate the quality improvement from RAG optimization without pursuing full-context. Let the user choose based on their priorities. If the user's project depends heavily on cross-file reasoning, the full-context path is worth the trade-offs. If the project primarily queries individual files, RAG optimization may deliver better ROI.

If Not Feasible: optimize entirely for retrieval quality. Do not prescribe aggressive token reduction strategies aimed at a threshold the project will not reach. Instead, invest optimization effort in the five RAG Quality Principles (see next section): clean the retrieval pool, improve chunk coherence, separate behavioral content, migrate procedural content to Skills, and sharpen routing descriptions.

---

## RAG Quality Optimization Principles

When a project operates in retrieval mode — whether by design or because full-context is not achievable — the optimization objective shifts from "reduce tokens to cross a threshold" to "maximize the quality of every retrieval." These five principles guide retrieval-specific optimization. They complement the placement tier analysis; apply them after tier decisions are made and before declaring optimization complete.

### Principle 1: Retrieval Pool Signal-to-Noise

Every file in the project's knowledge base competes for retrieval slots. When Claude searches in retrieval mode, it returns the top-ranked chunks across all files. A file that is occasionally useful but frequently retrieved as noise actively harms quality — it displaces chunks from the file that actually answers the query.

When evaluating files for archival or relocation, assess not just "is this file ever useful" but "does this file's presence in the pool cause wrong chunks to be retrieved for common queries." A file about deployment procedures that contains the word "architecture" throughout will compete with the actual architecture guide whenever a user asks about architecture. Removing or relocating the deployment file improves every architecture query, even though the deployment content was technically "useful sometimes."

The practical test: for the project's five most common query types, would retrieval accuracy improve if this file were not in the pool? If yes, the file is a noise source regardless of its standalone value.

### Principle 2: Chunk Coherence

Claude's retrieval returns chunks, not whole files. A file's internal structure determines whether retrieved chunks are useful. The goal: every major section of a knowledge file should be self-contained — a reader (or model) encountering just that section should understand it without needing the sections before or after.

Structural practices for chunk coherence:

Front-load the most important content in each file and each section. Retrieval is more likely to surface the beginning of a section than the end. If the critical insight is buried in paragraph four after three paragraphs of setup, it may never be retrieved.

Use clear, descriptive section headers. These serve as retrieval landmarks. A header like "## Fix: Conflicting Instructions → Audit and Reconcile" is far more retrievable than "## Pattern 3" or "## Section 2.1." Headers should contain the key terms a user would naturally query for.

Keep each file focused on a single topic. This ensures any chunk retrieved from that file is on-topic for queries that triggered its retrieval. A file covering both "behavioral calibration" and "output formatting" will produce chunks that are half-relevant to either query.

Target sections of 500–2,000 tokens (roughly 2,000–8,000 characters) for self-containment. Sections smaller than this may lack sufficient context for a retrieved chunk to be useful. Sections larger than this are likely to be split across chunk boundaries, producing fragments that lose coherence. This is a structural guideline, not a rigid rule — match it to the content's natural organization.

Minimize cross-section dependencies within a file. If Section B requires understanding Section A to make sense, either merge them or repeat the critical context. Under retrieval, there is no guarantee both sections will be retrieved together.

### Principle 3: Behavioral Content Separation

Behavioral instructions (rules Claude should follow) are categorically different from referential content (information Claude should consult). Under retrieval mode, behavioral content in knowledge files is dangerous: partial retrieval means inconsistent behavior. Claude might follow a rule in conversations where the relevant chunk is retrieved and ignore it in conversations where it is not.

All behavioral content should live in layers that are always loaded — Custom Instructions, Memory, or Skills (which load completely when triggered). Knowledge files in retrieval mode should contain only referential content: facts, data, reference material, examples, documentation.

The test: if Claude not retrieving this content would cause it to violate an intended behavior (rather than simply miss a fact), the content is behavioral and must move out of knowledge files.

This is the existing instruction/reference separation principle from the Project Architecture Guide, but under retrieval mode it becomes a hard constraint rather than a best practice. In full-context mode, behavioral content in knowledge files is suboptimal but functional — Claude still sees it. In retrieval mode, behavioral content in knowledge files is a reliability defect.

### Principle 4: Skills as a Fidelity Upgrade

For content that must be followed as a coherent set of instructions — domain-specific methodologies, procedural guides, behavioral templates, evaluation rubrics — Skill delivery is categorically better than retrieval-mode delivery:

A Skill loads completely when triggered. The full SKILL.md (recommended under 500 lines) enters context intact, preserving the logical flow, section dependencies, and conditional logic that make the instructions coherent.

The same content as a knowledge file under retrieval mode gets fragmented into 2–3 retrieved chunks out of the whole file. Procedural sequences break. Conditional logic loses its conditions. Evaluation rubrics lose half their criteria. The model follows whatever fragment it retrieved, ignoring the parts it didn't.

When evaluating Placement Tier 2 relocation candidates, prioritize moving behavioral and procedural content to Skills over moving referential content. Referential content can tolerate partial retrieval — a chunk from a data reference is useful even without the full file. Procedural content cannot tolerate partial retrieval — step 5 of a 10-step process without steps 1–4 is worse than useless.

Skill migration is not just a token-saving strategy. It is a fidelity upgrade that makes the content work better, independent of any context budget benefit.

### Principle 5: Routing Description Quality

In Claude Projects, the Custom Instructions routing descriptions ("Consult [file] when [trigger condition]") function as the context routing layer. They influence which files Claude searches when processing a query. In full-context mode, routing descriptions are helpful but not critical — Claude can see all files regardless. In retrieval mode, routing descriptions are the primary signal Claude uses to decide where to look. Poor routing means Claude searches the wrong file, retrieves irrelevant chunks, and produces lower-quality output even though the right content exists.

Audit routing descriptions for three qualities:

Specificity — does the trigger condition clearly distinguish this file from other files? "Consult for technical information" is too vague when three files contain technical information. "Consult when diagnosing behavioral calibration issues in Claude's output — hedging, verbosity, agreeableness, or list overuse" is specific enough to route accurately.

Coverage — does the trigger condition cover the file's actual query patterns, not just its primary topic? A file might be titled "Output Standards" but also contain the project's verification checklist. If the routing description only mentions output formatting, queries about verification won't find it.

Negative routing — are there cases where this file should not be consulted that need explicit exclusion? If two files have overlapping terminology but serve different purposes, routing descriptions should disambiguate: "Consult for system prompt architecture patterns. Not for individual prompt compilation — see PROMPT_COMPILER.md for that."

### RAG Quality Checklist

Use this checklist when auditing a project that operates in retrieval mode. Each item maps to a principle above.

1. **Behavioral separation.** Is all behavioral content (rules, constraints, defaults Claude should follow) in Custom Instructions, Memory, or Skills — not in knowledge files? (Principle 3)
2. **File focus.** Is each knowledge file single-topic, with each major section self-contained? Could a reader understand any section without reading the sections before it? (Principle 2)
3. **Routing accuracy.** Do routing descriptions in Custom Instructions accurately distinguish which file serves which query type? Are there ambiguous cases where two files could match the same query? (Principle 5)
4. **Pool cleanliness.** Is the retrieval pool free of low-value files that contribute noise — files that are rarely the best answer but frequently match common queries? (Principle 1)
5. **Skill migration.** Are procedural and behavioral knowledge files migrated to Skills where the content type permits? Is any behavioral content still being delivered via retrieval fragmentation? (Principle 4)
6. **Header quality.** Do file and section headers use descriptive, query-aligned language that serves as retrieval landmarks? (Principle 2)
7. **Large file structure.** Are files larger than ~30K tokens (~120KB) structured with clear section boundaries that would produce coherent chunks if split? Do sections avoid cross-dependencies? (Principle 2)

### The Index File Pattern

For projects operating in retrieval mode where retrieval quality suffers because Claude cannot efficiently navigate the knowledge base, a lightweight index file improves retrieval accuracy by giving Claude a search shortcut.

Create a file named `CONTENTS_INDEX.md` containing a structured map of the knowledge base. For each file, include: the filename, a one-sentence purpose, its key topics (3–5 terms), and cross-references to related files. The entire index should be under 2,000 tokens (~8KB) — if it's larger, it becomes noise rather than navigation.

Example structure:

```markdown
# Knowledge Base Index

## OPTIMIZATION_REFERENCE.md
System prompt architecture, behavioral tendencies and countermeasures, context budget principles, RAG quality optimization, common structural fixes.
Related: AUDIT_FRAMEWORK.md (scoring rubrics that reference these principles)

## AUDIT_FRAMEWORK.md
Project Scorecard (6 dimensions), anti-pattern checklist (7 patterns), quality criteria, diagnostic question bank.
Related: OPTIMIZATION_REFERENCE.md (fix patterns for issues found in audits)
```

Route to it in Custom Instructions: "When uncertain which file contains the needed information, or when a query could match multiple files, consult CONTENTS_INDEX.md first to identify the correct target."

The index file is only useful in retrieval mode. In full-context mode, Claude sees all files simultaneously and routes by content, making an index redundant. If a project transitions from retrieval to full-context (a common effect of moving from a 200K-era plan to a 1M-window model), the index file can remain (it's small enough to be harmless) or be removed.

---

## Common Structural Fixes

The fix patterns below address structural failure modes commonly surfaced during CP-side audits. Several map to named anti-patterns in the unified catalog (`root_AGENT_ANTI_PATTERNS.md`); inline cross-references identify the relevant pattern. The catalog is authoritative on pattern definitions, surface tags, and cross-surface mappings; the fix patterns here are CP-side remediation procedures.

### Fix: Missing Identity → Add a Layered Identity Block

When a Project has no identity or a generic one, build a replacement with these components:
1. Role and seniority ("You are a senior [role]")
2. Domain expertise ("specializing in [domain areas]")
3. Analytical disposition ("You evaluate [things] through the lens of [framework/priorities]")
4. Priority hierarchy ("You prioritize [X] over [Y]")
5. One behavioral sentence ("You [key behavioral trait relevant to the domain]")

### Fix: Conflicting Instructions → Audit and Reconcile

When instructions conflict (e.g., "be concise" vs. "be thorough"):
1. Identify all instances of the conflict across Custom Instructions and knowledge files.
2. Determine the intended behavior.
3. Write a single, reconciled instruction that captures the intended behavior without ambiguity.
4. Place it in one authoritative location (Custom Instructions for behavioral rules).
5. Remove or replace all other instances.

### Fix: Orphan Files → Add Routing Descriptions

Addresses the **Orphan File** pattern (`root_AGENT_ANTI_PATTERNS.md §3.3`). For each orphaned file:
1. Write a one-sentence purpose description.
2. Write a trigger condition: "Consult this when [specific situation]."
3. Add the entry to the knowledge file guide section of Custom Instructions.
4. If the file cannot be given a clear trigger condition, evaluate whether it belongs in the Project.

### Fix: No Modes for Distinct Task Types → Design Mode Boundaries

Addresses the **Echo Chamber** pattern (`root_AGENT_ANTI_PATTERNS.md §3.2`). When a Project handles multiple task types with a single set of instructions:
1. List all task types the Project handles.
2. Apply the differentiation test: do different task types need different reasoning approaches, output structures, or behavioral rules?
3. For task types that pass the test, define a mode with: trigger condition, behavioral instructions, reasoning approach, output structure.
4. For task types that fail the test (same approach works for all), leave them under the default behavior.

### Fix: Bloated System Prompt → Separate and Slim

Addresses the **Monolithic standing context** pattern (`root_AGENT_ANTI_PATTERNS.md §2.1`) and the structural facet of **Kitchen Sink** (`root_AGENT_ANTI_PATTERNS.md §3.4`). When Custom Instructions are overloaded:
1. Identify reference material embedded in the system prompt (examples, data tables, frameworks, extended explanations).
2. Move reference material to knowledge files.
3. Identify "just in case" instructions that address rare edge cases.
4. Move edge case handling to knowledge files or remove it.
5. What remains should be: identity, 3-7 core rules, knowledge file routing, operational modes, and output standards.

### Fix: Missing Countermeasures → Domain- and Deployment-Targeted Selection

1. Identify the Project's domain, primary task types, and deployment context (chat / Projects / Claude Code / API).
2. Check each of the 14 numbered behavioral tendencies (#1–#14, with facets 1a/1b under #1, 3a/3b/3c under #3, 7a/7b under #7) against the domain and deployment combination. Use the deployment calibration tables in the Behavioral Tendencies section to filter — a tendency at LOW for the deployment context generally does not need a countermeasure regardless of domain match.
3. For each relevant tendency, add the countermeasure template (customized to the domain's language). For Tool Trigger Miscalibration (#7), apply the specific facet (7a or 7b). For Verbosity (#3), apply the specific surface (3a conversational, 3b agentic narration, 3c written deliverables).
4. Place at the appropriate attention position (identity or core rules for critical countermeasures, output standards for format-level countermeasures).
5. Do not add countermeasures for tendencies this domain or deployment does not trigger — they are noise that diminishes current models' strong instruction following.
6. For Projects deployed on the chat interface specifically: prioritize countermeasures for #1b (persistent-preference dilution), #7b (tool under-triggering), #9 (editorial drift), and #10 (self-referential fabrication).
7. For Projects deployed on Claude Code specifically (or agent workloads on the API): prioritize countermeasures for #3b (agentic narration), #11 (over-verification — REMOVE self-directed re-check instructions), #12 (scope expansion), #13 (subagent over-delegation). These are the tendencies Opus 5 introduces or amplifies on agentic surfaces.
8. For Projects upgrading from a 4.6-era or 4.8-era system prompt: audit for now-redundant countermeasures targeting tendencies #1a, #2 (factual claims), #3a (verbosity), #5 (external-fact), #6 (over-exploration), and #7a — these are partially or fully reduced at the model level. Where the failure mode is no longer observed, remove the countermeasure to free token budget for the new tendencies.
9. For audit Skills specifically: apply the conservative-instruction literalism fix. Replace "only report high-severity issues" / "be conservative" language with report-everything-then-filter form.

### Fix: Pre-4.6 System Prompt → Recalibrate for Current Models

When a Project's system prompt was written for earlier Claude models (pre-4.6, or pre-Opus-5):
1. Audit for emphatic language (MUST, ALWAYS, CRITICAL, NEVER, "If in doubt, always...") and replace with calibrated guidance. Exception: where you are specifically countering tendency 7b on chat-interface deployments, explicit enforcement language remains appropriate.
2. Audit for aggressive tool-use triggers and dial back to conditional language for general tool use.
3. Audit for verbosity countermeasures that may now over-correct — remove or soften preemptive anti-verbosity instructions. Check for the specific surface (3a conversational, 3b agentic, 3c written) rather than applying a single generic verbosity countermeasure.
4. Check for prefill-dependent formatting (no longer supported in 4.6+) and migrate to explicit instructions.
5. Verify that the instruction density is appropriate — current models follow instructions more precisely, so noisy "just in case" instructions cause more harm than in earlier models.
6. For chat-interface deployments: add countermeasures for #1b, #7b, #9, and #10 if not already present.
7. For agentic deployments (Claude Code, API agent workloads): audit for accumulated verification instructions (double-check, re-verify, verification step, subagent to verify). Distinguish self-directed re-checking (REMOVE per tendency #11) from external-artifact verification (KEEP). This is the highest-value single audit on prompts that migrated from 4.7/4.8 into Opus 5.
8. For audit-Skills and review prompts: apply the conservative-instruction literalism fix (see Fix: Missing Countermeasures step 9).
9. Audit effort settings: on Opus 5, the default is `high` and the recommendation is to re-run an effort sweep rather than carry over from prior models. Prompts hardcoded to `xhigh` from the 4.7/4.8 era should be re-evaluated — `xhigh` is now the *step-up* for demanding work, not the *default*.

### Fix: Misaligned Context Layers → Rebalance Memory and Knowledge Files

Addresses the **Layer hierarchy violation** pattern (`root_AGENT_ANTI_PATTERNS.md §2.2`) and the **Blurred Layers** pattern (`root_AGENT_ANTI_PATTERNS.md §3.5`). When Memory contains reference-depth content or knowledge files contain orientation-level facts that should be in Memory:
1. Audit Memory edits for content depth. Orientation-level facts (current phase, active constraints, key decisions, user identity) belong in Memory. Decision rationale, procedural steps, detailed explanations, and historical context belong in knowledge files.
2. Audit knowledge files for always-relevant orientation facts that are buried in searchable content. If Claude needs a fact in every conversation (not just when a specific file is consulted), that fact is a candidate for Memory.
3. For each misplaced item, move it to the correct layer. When moving reference-depth content from Memory to a knowledge file, keep a one-sentence orientation summary in Memory and put the depth in the file.
4. Check for duplication across layers. Each fact should have one authoritative home. If the same fact appears in both Memory and a knowledge file, decide which layer is authoritative and remove or reduce the other.
5. For Projects with no Memory configured: if the Project has 3+ knowledge files or multi-phase build history, add Memory edits covering current phase, key constraints, user context, and project scope. For simpler Projects (1-2 knowledge files, single purpose), Memory is optional.

### Fix: Unoptimized User Preferences → Audit and Restructure

When User Preferences are missing, bloated, or contain domain-specific content:
1. Apply the Universality Test to every existing instruction. Flag instructions that fail — they are demotion candidates for specific Project CIs.
2. Check for promotion candidates across Project CIs. Behavioral instructions appearing in 3+ Projects that pass the Universality Test should be promoted to Preferences.
3. Check Memory for codification candidates. Stabilized behavioral patterns in Global Memory that the user has not explicitly set as Preferences should be codified.
4. Restructure around three content categories: identity context (who the user is), behavioral defaults (how Claude should behave universally), and communication calibration (tone, directness, format preferences).
5. Trim to essentials. Target 200-500 tokens. Each instruction must earn its place. Remove instructions that restate Claude's defaults, that are too vague to be actionable, or that address edge cases.
6. Produce the complete optimized Preferences text as a separately copyable unit.

### Fix: Context Budget Optimization → Right-Size and Right-Place Knowledge Files

When a Project's knowledge files trigger RAG activation, or when a user requests optimization at any load level:

1. Check current mode: is `project_knowledge_search` present in Claude's available tools? Present = retrieval mode; absent = full-context mode. Note also which model the Project is running under — a Project historically in retrieval mode under a 200K plan may already be in full-context mode under a 1M-window primary model.
2. Estimate the total token load across all knowledge files using the character-to-token heuristics (see Token Estimation above). Include GitHub-connected repos in the inventory — these count as knowledge files.
3. Evaluate each file for tier placement using six dimensions. (a) Cross-reference density: how many other files reference this file? High cross-reference files are load-bearing. (b) Behavioral vs. referential content: does this file contain rules Claude should follow (behavioral) or information Claude should consult (referential)? Behavioral content must be in always-loaded layers. (c) Query frequency: is this file consulted in most conversations or only for specific task types? (d) Degradation severity: what happens to output quality if this file is not loaded? (e) Token cost: how large is this file relative to the estimated (or measured) threshold? (f) Cross-file dependency density: how much does this file reference or depend on content in other files? High-dependency files are the most harmed by retrieval mode because cross-references won't resolve when only fragments are loaded.
4. For files that score as behavioral, high cross-reference, high frequency, or critical degradation: keep as knowledge files (Placement Tier 1). These are load-bearing. High-dependency files are either Placement Tier 1 candidates (keep in-context so cross-references resolve) or candidates for consolidation.
5. For files that score as referential, low frequency, moderate or low degradation: candidate for compression, relocation to a Skill, or session-specific upload (Placement Tier 2). High-dependency files that cannot be Tier 1 should be restructured to reduce their dependencies — inline the critical cross-references rather than pointing to other files.
6. For files that are stale, rarely consulted, or substantially redundant: archive, merge into another file, or remove (Placement Tier 3).
7. Execute optimization in priority order: archive Tier 3 first (lowest risk, immediate savings), then relocate Tier 2 files, then compress Tier 1 files (highest risk, evaluate carefully).

**Compression quality guidance.** When compressing files, preserve chunk self-containment. Compression that removes "redundant" context from sections may save tokens but degrade retrieval quality — a retrieved chunk from a compressed file must still make sense in isolation.

Three compression approaches, ordered from safest to most aggressive:

(a) Remove stale or superseded content. Sections documenting decisions that have been implemented, historical context that no longer informs current work, or examples that duplicate other examples. This is pure noise removal with no quality risk.

(b) Consolidate redundant sections. When two sections cover overlapping content, merge them. Ensure the merged section is self-contained and covers both original use cases. This saves tokens while maintaining or improving chunk coherence.

(c) Tighten prose within sections. Reduce word count while preserving meaning. This is the highest-risk compression — it's easy to inadvertently remove the context that makes a section self-contained. After tightening, apply the isolation test: read any single section of the compressed file without context from surrounding sections. If it's unclear what the section is about, what problem it addresses, or how to apply it, the compression cut too deep. Restore the contextual framing.

Never compress by removing section headers, introductory context, or cross-reference pointers. These are retrieval infrastructure, not redundancy.

8. After optimization, verify the project is operating effectively in its target mode. If the target was full-context: confirm `project_knowledge_search` is absent and test cross-file reasoning with a query that requires content from two files. If the project is remaining in retrieval mode: run the RAG Quality Checklist (see RAG Quality Optimization Principles above).

For comprehensive context budget analysis including dependency graphs, per-file dimension scoring, and projected savings, use the Context Budget Architect methodology (available as the `rootnode-context-budget` Skill when installed).
