---
name: rootnode-context-budget
description: >-
  Analyzes Claude Project context budget under the automatic-RAG-by-window
  model: knowledge files vs. threshold-exempt overhead (Skills, MCPs, CI, Memory).
  Two modes: Quick Diagnostic and Full Budget Audit. Use when user says "check
  my context budget," "how much context am I using," "is my project too big,"
  "optimize my token usage," "tier my files," "optimize for RAG," "improve
  retrieval quality," "should I keep compressing," "am I over-compressing,"
  "should I accept RAG mode." Also trigger on context pressure symptoms: "Claude
  forgets my instructions," "responses getting generic," "content not found in
  my knowledge files." Also use when a project audit scores Knowledge
  Architecture ≤ 3. Do NOT use for content placement decisions (use
  rootnode-memory-optimization if available), full project audits (use
  rootnode-project-audit if available), or behavioral tuning (use
  rootnode-behavioral-tuning if available). Run on Opus 5 or Sonnet 5 at `high` effort (both defaults); depth
  reduces on legacy models.
license: Apache-2.0
metadata:
  author: rootnode
  version: "4.0.0"
  original-source: "root_OPTIMIZATION_REFERENCE.md"
---

# Context Budget Analysis

> **Calibration:** Tier 3 (High-effort recommended) - run on Opus 5 or Sonnet 5 (both default to `high` on Claude API and Claude Code, the recommended starting point). Step up to `xhigh` for long-horizon or particularly demanding runs. Quality degrades at `low` effort and on legacy models (Sonnet 4.6, Opus 4.8 fallback-graceful). See repository README for model compatibility.

Analyze Claude Project context budget health. Determine operating mode (full-context vs. retrieval). Produce tiered file placement recommendations with a strategy matched to the project's growth trajectory, work-phase timing, and content routing needs.

## Important

**Token estimates are inherently approximate.** Always label token counts as "estimated" and note a ±15% margin. Never state a precise token count as fact. Use `ls -la /mnt/project/` for byte counts and divide by 4 for rough token estimates.

**Evaluate files objectively.** Users may resist demoting files they authored or consider important. Score every file on the six dimensions regardless of stated preferences. If a file scores as Tier 3, say so clearly.

**Do not assume full-context is always the goal.** Under the current automatic-RAG-by-window model, many legitimate projects operate in retrieval mode by design. Assess the user's workload pattern before prescribing optimization strategy.

**Skills and MCPs cannot trigger RAG.** Do not recommend reducing Skills or disconnecting MCPs to recover knowledge file headroom. The two budget pools are independent for threshold purposes.

**Context quality degrades with total context size, not just at limits.** Even with tokens remaining, every token of overhead reduces the model's attention budget. Minimizing overhead improves output quality on every turn.

**Compression has a quality floor.** Not all content is equally compressible. Classify content type before recommending compression depth. See `references/compression-execution.md` for the Content-Type Classification (Type A prose vs. Type B precision reference) and structured off-ramps when compression stalls.

**Optimize for where the project is going, not just where it is.** A plan that restores full-context mode for one session before the next file addition pushes it back into RAG is a cleanup, not a strategy. Always assess growth trajectory before producing an optimization plan.

## Model requirements

This Skill performs per-file evaluation against the six File Evaluation Dimensions, growth trajectory analysis, content routing decisions, and phased optimization planning with compression safeguards. Run on Opus 5 or Sonnet 5 (both default to `high` on Claude API and Claude Code — the recommended starting point). Step up to `xhigh` for long-horizon or particularly demanding runs. Effort controls thinking depth, not visible output length — deep per-file evaluation benefits from `high` or higher.

On the dual-primary tier (Opus 5, Sonnet 5) at `high` effort the Skill runs with full depth. On Sonnet 4.6 (legacy-graceful) and Haiku 4.5 with extended thinking, expect compressed per-file evaluation, surface-level tier recommendations, and reduced synthesis across the growth trajectory. Quick Diagnostic mode degrades less than Full Budget Audit mode. Fallback-graceful on Opus 4.8 (classifier-flagged requests may route there silently). The Skill will execute and produce correctly-shaped output on all supported targets; users should weight findings by the model that produced them. Haiku 4.5 without extended thinking is out of scope.

## Core Concepts

### Operating Modes

Claude Projects operate in one of two modes:

- **Full-context mode:** All knowledge files loaded into context every turn. Default when total knowledge file tokens stay comfortably below the underlying model's context window.
- **Retrieval mode (RAG):** Knowledge files searched via `project_knowledge_search`; only relevant chunks loaded per turn. Activates automatically when the knowledge base approaches or exceeds the model's context window (per Anthropic's support article — see `root_OPTIMIZATION_REFERENCE.md` "Context Budget Principles").

**Detection:** Check whether `project_knowledge_search` is present in available tools. If present, retrieval mode is active. The "Indexing" label in the project UI files panel is also a visible indicator. Verify current mode by direct check, not by inference from token counts — the automatic-by-window rule means the same project may be in different modes under different models or plan states.

### Context window ≠ RAG threshold

Two conceptually distinct things that were numerically entangled in the 200K era:

- **Context window** — the model's maximum input capacity, measured in tokens per model. Currently 1M for Fable 5 / Opus 5 / Sonnet 5; 200K for Haiku 4.5. Plan-dependent for Anthropic Projects.
- **RAG threshold** — the platform-side decision point where Projects switch from full-context loading to retrieval mode. Now tracks the window (automatic per current article), rather than being a fraction of it.

State the two separately in analysis. Do not carry a fixed number forward as a live threshold; the threshold moves with the model, plan, and platform. See "Historical context" below for the Phase 22 measurement that produced the ~66,500 figure previously used as an anchor.

### The Two-Pool Budget Architecture

The knowledge-budget vs. conversation-budget distinction survives the platform change. The pools are functionally distinct: only the knowledge-file pool can trigger RAG activation; the conversation pool (platform overhead + Skills + MCPs + CI + Memory + Preferences + conversation history + responses) affects conversation quality but cannot cause a mode switch.

| Budget Pool | Contents | RAG Impact |
|---|---|---|
| Knowledge file budget | Knowledge files only (all types: .md, .pdf, .docx, .xlsx, .csv, .txt, images, GitHub-connected repos) | Approaching / exceeding the model's window triggers RAG |
| Conversation budget | Platform overhead, Skills, MCPs, CI, Memory, Preferences, conversation history, responses | Cannot trigger RAG regardless of size |

**Key implication (preserved from the 200K era, still true):** Adding Skills, connecting MCPs, or expanding Custom Instructions cannot trigger RAG mode. Conversely, reducing them cannot recover knowledge file headroom. The two pools are independent for threshold purposes.

Under 1M-window primary models the two pools sit further apart in absolute terms than they did under the 200K era — a project can be well below the RAG activation point while a long agentic conversation still triggers compaction. Under the 200K Haiku window, the two mechanisms sit closer together.

### Token Estimation

Estimate knowledge file tokens: run `ls -la /mnt/project/` for byte sizes, divide each by 4, sum.

Conversion rates: English prose ≈ 4 characters/token. Structured content (XML, code, tables) ≈ 3.25 characters/token. Mixed markdown ≈ 3.75 characters/token. Estimates are ±15% per file, ±10% for project totals.

**Tokenizer notes for current models:**
- Fable 5 uses the tokenizer introduced with Opus 4.7 — same text produces roughly 30% more tokens than models before Opus 4.7 (Anthropic's models overview page).
- Sonnet 5 produces approximately 30% more tokens per unit of content than Sonnet 4.6 (Anthropic's whats-new-sonnet-5 page).
- Opus 5 tokenizer specifics were not fully re-baselined in the v4.0 alignment cycle — treat measurements with explicit tolerance until re-baselined via `count_tokens`.

**Important:** Include ALL knowledge file sources: uploaded files (all types), GitHub-connected repositories, and any other connected content sources. Include the tokenizer multiplier where the target model is known.

For borderline projects where the exact number matters, measure empirically (see "Empirical Threshold Measurement" below). Do not assume a fixed threshold.

### Threshold-Exempt Overhead

Skills, MCPs, and other non-knowledge-file components are threshold-exempt. They affect conversation runway and attention quality but cannot trigger RAG. Key overhead sources: platform system prompt (~20–25K tokens), Custom Instructions (bytes ÷ 4), Memory (typically 500–3K tokens).

**MCP loading modes:** MCP overhead varies dramatically by loading mode. Deferred/load-as-needed (the claude.ai default) adds ~40–60 tokens per connector via a lightweight catalog plus ~5–7K flat for the deferred infrastructure — ~85% less than always-loaded mode (~3K–15K per connector). When the loading mode is unknown, note the estimate as a range and flag the uncertainty. See `references/compression-execution.md` for detailed overhead estimation.

Conversation runway is window-dependent: under a 200K plan against a lean project, runway is ~105K–110K tokens; under a 1M-window plan, runway is substantially larger. Estimate conversation runway as (context window − platform overhead − knowledge files if full-context − threshold-exempt overhead), not against a fixed floor.

### Context Window Sizes — Cited Values Only

Per-plan windows for claude.ai Projects (Pro / Max / Team / Enterprise) are not enumerated by a current Anthropic source available to this Skill. Prior root.node documentation carried plan-tier window numbers on recollection; those numbers are removed for v4.0 rather than asserted without citation. **Consult Anthropic's current plan documentation for per-plan window values.** The values below are cited to sources verified during the v4.0 alignment cycle (2026-07-24/25):

| Model / Surface | Context Window | RAG Behavior | Source |
|---|---|---|---|
| Fable 5, Opus 5, Sonnet 5 (API) | 1M tokens (default AND max on Opus 5; no smaller variant) | User-controlled context; no platform RAG (API-side has no Projects mode) | Anthropic models overview page — `platform.claude.com/docs/en/about-claude/models/overview` |
| Haiku 4.5 (API) | 200K tokens | User-controlled context; no platform RAG | Same |
| claude.ai Projects (any current-generation model on Anthropic Projects) | Plan-dependent (consult Anthropic plan documentation) | **Automatic** when knowledge base approaches or exceeds the model's context window | Support article: `support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects` — verbatim: "RAG automatically activates when your project approaches or exceeds the context window limits." |

The support article does not publish per-model or per-plan threshold numbers. Under the automatic-by-window model, the specific RAG activation point for a project depends on the model / plan / platform state; **measure empirically when the number matters** (see the "Empirical Threshold Measurement" section).

### Historical context — the ~66,500 measurement

The `~66,500 token RAG threshold` figure that appears in prior root.node documentation is a specific empirical measurement from Phase 22 (April 2026 calibration lab): under the 200K context window (Pro / Max / Team plans at the time), against Opus 4.6, the RAG activation point was at approximately 66,500 tokens of knowledge files — roughly 33% of the 200K window. That was a valid, measured number for its era.

Under the current platform (automatic-by-window on 1M-window primary models):
- The 66,500 figure no longer represents current-state RAG behavior.
- The 33% ratio was an artifact of the 200K-window era; there is no evidence it holds for 1M-window models.
- Projects that were calibrated to sit comfortably under 66,500 are far below the current threshold (whatever it is) on any 1M-window model.

Where prior documentation states the 66,500 figure as a historical measurement in past tense, it is correct. Where it states the figure as a current-state operational rule, it is stale. This Skill treats the figure as historical; it does not use it as an operational anchor for current audits.

### Operating Tiers (qualitative, window-relative)

Fixed-token tier bands (v3-era: "under 30K", "30K–50K", "50K–66K", "66K–500K", "over 500K") are retired for v4.0 because they were derived from the fixed ~66,500 anchor. Under automatic-by-window RAG, tier classification is qualitative and window-relative. **The bands below carry no specific % boundaries** — the v4.0 alignment cycle deliberately did not invent replacement percentages, because a plausible-sounding number would inherit the same environment-boundedness that made the ~66,500 anchor stale. When a project's classification is close to a boundary, route to the Empirical Threshold Measurement procedure rather than reading a percentage from this table.

| Tier | State | Description |
|:----:|---|---|
| 1 | Comfortable | Knowledge base sits well below the model's context window with ample headroom. Full-context loading. Focus on structural quality. |
| 2 | Moderate | Knowledge base occupies a meaningful share of the window but is not approaching it. Full-context loading with headroom. Optimization beneficial but not urgent. Monitor growth trajectory. |
| 3 | Approaching | Knowledge base is close enough to the window that the automatic RAG activation is plausible or imminent. Proactive optimization recommended. Any planned content additions should be evaluated against projected growth. Measure empirically if the number matters. |
| 4 | Retrieval | Retrieval mode active (`project_knowledge_search` present in tools). Cross-file reasoning loses guaranteed simultaneity. Optimize for retrieval quality; if the gap to full-context is small, recovery may be achievable. |
| 5 | Heavy retrieval | Retrieval mode active with a knowledge base substantially larger than the model's window. Retrieval precision degrades with volume. Optimize entirely for retrieval quality; surface API deployment as an alternative architecture for workloads requiring cross-document synthesis. |

Tier classification for a specific project uses two signals: (1) whether `project_knowledge_search` is present (definitively separates tiers 1–3 from 4–5) and (2) how close the knowledge-file total is to the model's context window (separates 1 from 2 from 3, qualitatively). For borderline calls, **measure empirically** — see "Empirical Threshold Measurement" below.

File count is not a factor in RAG activation. Optimize file count for content organization and retrieval quality.

### Empirical Threshold Measurement

The most reliable way to determine a project's current RAG-activation point is empirical testing (this is unchanged from the 200K era; only the number moves).

**Quick method (±1,000 tokens precision):** Note the project's current knowledge file byte total. If in full-context mode, add knowledge files until the "Indexing" indicator appears in the project UI. If in retrieval mode, remove knowledge files until "Indexing" disappears. The boundary in total knowledge file bytes, divided by 4, gives the approximate RAG activation point in tokens for that project's configuration under the current model / plan.

**When to recommend empirical measurement:** When a project is borderline and feasibility depends on precise numbers. When unexpected RAG activation occurs with no knowledge file changes (suggests a platform-side or plan/model change). After major Anthropic model or platform updates that may shift the RAG activation point. Note that under automatic-by-window behavior, the RAG activation point may move whenever Anthropic ships model or platform changes — a measurement is a point-in-time snapshot for the current configuration.

### Context Pressure vs. RAG Switching

Two independent mechanisms. RAG switching is project-level and static (knowledge files approach/exceed the model's window). Context pressure is conversation-level and dynamic (conversation approaches the window limit). A project can experience both, either, or neither.

Diagnostic shortcuts: "Claude forgot my instructions" → context pressure OR RAG (behavioral rules not retrieved). "Claude can't find content in my files" → RAG (content not retrieved) OR context pressure (compacted). "Responses getting shorter/weaker" → context pressure.

In full-context mode, compaction summarizes conversation history but leaves knowledge files intact. In retrieval mode, knowledge files load fresh each turn via search (not subject to compaction) but conversation history still compacts. Under 1M-window primary models, the two mechanisms sit further apart in absolute terms than they did under the 200K era; context pressure typically arrives later in a conversation.

### Placement Tiers

Files are classified into three tiers based on six evaluation dimensions (see `references/evaluation-rubric.md` for detailed scoring criteria):

- **Tier 1 — Must Keep:** High cross-reference density, behavioral content, high query frequency, severe degradation if absent.
- **Tier 2 — Optimize or Relocate:** Moderate scores. Candidates for compression, relocation, or restructuring.
- **Tier 3 — Archive or Remove:** Low scores. Stale, rarely consulted, duplicated, or retrievable on demand.

## Mode 1: Quick Diagnostic

Fast health check. Answers: Is this project at risk? What operating mode is it in? What's the right optimization strategy?

**When to use:** Quick questions about context budget health — "am I in danger?", "how big is my project?", "is my project too big?"

### Pipeline

**Step 1 — Assess project goals and use pattern.** Before calculating budgets, understand how the project is used: primary query pattern (cross-document synthesis vs. single-document retrieval), session pattern (short targeted vs. long working), content growth trajectory (stable vs. actively growing), and upcoming work phases (what's the next 1–2 quarters of work).

This determines whether full-context or optimized retrieval better serves the project. Cross-document synthesis + short sessions → full-context strongly preferred. Single-document queries → retrieval mode appropriate. Actively growing → design for retrieval from the start.

**Step 2 — Detect operating mode.** Check for `project_knowledge_search` in available tools.

**Step 3 — Inventory.** Run `ls -la /mnt/project/`. Record file names, byte sizes, estimated tokens. Count files.

**Step 4 — Calculate budget.** Sum estimated knowledge file tokens. Classify the project into a qualitative operating tier (1–5, see "Operating Tiers" above) using the ratio of knowledge tokens to the model's context window — or, for borderline cases, an empirical measurement. Do not classify against the historical ~66,500 anchor; use window-relative bands. Estimate conversation runway separately: (context window − platform overhead − knowledge files if full-context − threshold-exempt overhead). Determine MCP loading mode before estimating overhead. Confirm the target model / plan before classifying, because the RAG activation point moves with the model.

**Step 5 — Assess feasibility (retrieval mode only).** Calculate gap. Quick-scan for available reductions (Tier 3 candidates, behavioral content in knowledge files, compressible files). Factor in growth trajectory — will projected additions re-cross the RAG activation point? Classify: Recovery Achievable / Borderline / Not Feasible.

**Step 6 — Deliver.** Output adapts to operating mode and feasibility:

```
Context Budget Status: Tier [N]
— Knowledge files: ~[X]K tokens across [M] files
— Headroom / Gap: ~[H]K [remaining / over] vs. the project's measured or window-derived RAG activation point (state the basis: empirical measurement, window-relative estimate, or platform-current unknown)
— MCP loading mode: [deferred / always-loaded / unknown]
— Conversation runway: ~[R]K tokens estimated
— Approximate session depth: [S] substantive turns

[If retrieval mode: Recovery verdict — Achievable / Borderline / Not Feasible]
[If Tier 2+: top risk factor and recommended next step]
[If growth trajectory identified: note projected ceiling]
```

Quick Diagnostic does NOT evaluate individual files, produce per-file tier classifications, build dependency graphs, run the RAG Quality Checklist, model growth trajectory in detail, or produce phased optimization plans.

## Mode 2: Full Budget Audit

Comprehensive analysis producing per-file evaluations, growth trajectory, work-phase heat map, content routing assessment, and a phased optimization plan.

**When to use:** Detailed analysis — "audit my context budget," "which files should I keep?", "help me reduce my knowledge file size," "tier my files," "improve my retrieval quality."

### Pipeline

**Step 1 — Assess project goals and use pattern.** Same as Quick Diagnostic Step 1, but probe deeper: identify specific upcoming work phases by name (e.g., "CRM build sprint," "website rebuild," "campaign launch") and their approximate timing.

**Step 2 — Inventory and estimate.** List all knowledge files with estimated token counts. Include all file types and GitHub repos. Estimate threshold-exempt overhead separately (determine MCP loading mode first). Produce the context budget breakdown showing both pools.

**Step 3 — Evaluate each file.** Score every knowledge file on six dimensions (see `references/evaluation-rubric.md`). Ground every score in specific evidence. Additionally, classify each file's content using both frameworks: Type A/B distribution (compression depth — see `references/compression-execution.md`) and Category 1–4 classification (storage routing — see `references/content-routing.md`).

| Dimension | What It Measures |
|-----------|-----------------|
| Cross-Reference Density | How many other files or CI sections reference this file |
| Behavioral vs. Referential | Whether the file contains rules/instructions or reference information |
| Query Frequency | How often this file is consulted across typical conversations |
| Degradation Severity | What breaks or degrades if this file is absent |
| Token Cost | Size relative to total budget — absolute and proportional |
| Cross-File Dependency Density | How much this file depends on content in other files |

**Step 4 — Growth Trajectory Assessment.** Before producing any optimization plan, model where the project is heading:

1. **Planned additions:** What files, content, or capabilities are expected in the next 1–2 quarters? Estimate token counts.
2. **Active growth files:** Which files are actively growing (campaign content, competitor intelligence, expanding guides) vs. stable reference?
3. **Seasonal rotation:** Which files have temporal decay (campaign playbooks, seasonal content) that will naturally free budget?
4. **Planning ceiling:** Current tokens + projected additions + projected growth = the number the optimization must create headroom beneath, not just the current RAG activation point.

If the user does not volunteer growth information and it cannot be inferred from project content, ask.

**Step 5 — Work-Phase Heat Map.** Map file relevance to upcoming work phases:

1. Identify the user's next 2–3 major project phases from Step 1.
2. For each file, assess: HOT (primary working reference during this phase), WARM (occasionally consulted), or COLD (not needed).
3. Use the heat map to time optimization actions — compress files during their cold phase, protect hot-phase files from disruption.

**Step 6 — Build the dependency graph.** Map explicit references between files. Map CI references to each file. Identify clusters, hub files, and mutual dependencies.

**Step 7 — Classify tiers.** Apply the tier decision matrix from `references/evaluation-rubric.md`. When dimension scores conflict, explain tiebreaker reasoning.

**Step 8 — Run feasibility assessment.** Same methodology as Quick Diagnostic Step 5, but with precise per-file data. Factor in the planning ceiling from Step 4 — optimize against the projected total, not just the current total.

**Step 9 — RAG Quality Assessment (retrieval mode only).** Run the seven-item RAG Quality Checklist from `references/evaluation-rubric.md`. Score each item pass/fail with evidence. Prescribe targeted fixes for failures.

**Step 10 — Produce the phased optimization plan.** For each Tier 2 and Tier 3 file, recommend a specific action:

- **Archive:** Remove from active knowledge files. Content outdated or not consulted.
- **Remove redundancy:** Delete duplicated or superseded content sections.
- **Compress:** Reduce token count. Include content-type distribution (Type A% / Type B%). Set conservative targets for Type B-heavy files. See `references/compression-execution.md`.
- **Relocate to CI/Memory/Skill:** Move behavioral rules to CI, orientation facts to Memory, standalone methodologies to Skills.
- **Data split (Category 3):** Migrate structured reference data to an external store via MCP. See `references/content-routing.md` for the full data split pattern, MCP infrastructure assessment, and fallback guidance.
- **Merge:** Combine related files to reduce cross-file dependency overhead.
- **Flag structural opportunity (Category 4):** When structured data would benefit from a queryable store but no MCP infrastructure is available, note the opportunity in the plan.

**Order by composite priority**, not raw token savings:
1. **Strategic constraints** — protect files entering their hot phase; defer optimization of files the user needs this week.
2. **Effort level** — archives and redundancy removal before compression before restructuring before data splits.
3. **Disruption cost** — cold-phase files before hot-phase files (reference the Work-Phase Heat Map).
4. **Token yield** — higher savings as tiebreaker when effort and disruption are equal.

**Structure the plan in three phases:**

**Phase 1 — Zero-Effort (execute now):** Archives, redundancy removal, section deletion. No rewriting required. Include cumulative savings, projected tier, and what the headroom enables.

**Phase 2 — High-Yield Optimization (execute during next cold phase):** Largest optimization targets that are currently cold. Includes both compression of Category 2 content AND data splits for Category 3 content. Include cumulative savings, projected tier, and phase transition timing referencing the heat map.

**Phase 3 — Reserve (execute when needed):** Moderate targets to deploy if growth exceeds projections or Phase 2 savings are lower than estimated. Include projected impact.

**Step 11 — Validate.** Verify the plan does not remove content critical to core function. If full-context recovery was the target, verify projected post-optimization state is within the RAG activation point AND within the planning ceiling. Verify compression of Type B content has proportionate savings-to-risk ratio.

### Output Format

```
# Context Budget Audit: [Project Name]

## Budget Overview
[Two-pool breakdown. Operating tier. Mode status.]

## Use-Case Assessment
[Query pattern, session pattern, growth trajectory, upcoming phases.]

## Growth Trajectory
— Planned additions: [files with estimated token counts]
— Active growth files: [files and projected growth]
— Seasonal rotation: [files with known expiration dates]
— Planning ceiling: ~[current + projected]K tokens
— Required headroom: ~[planning ceiling − RAG activation point]K tokens

## Work-Phase Heat Map
| File | Phase 1: [name] | Phase 2: [name] | Phase 3: [name] |
|---|---|---|---|
| [file] | HOT | WARM | COLD |
...
Compression timing: [which files to compress now vs. defer]

## Feasibility Assessment
[Recovery verdict against planning ceiling, not just current state]

## File Evaluation
[Per-file table: file name, estimated tokens, six dimension scores,
content-type (A/B%), content category (1–4), placement tier, key evidence]

## Dependency Graph
[File-to-file reference map. Hubs, clusters, mutual dependencies.]

## Content Routing Summary
[Per file with mixed categories:]
— Category 1 (behavioral): [X]% → Relocate to CI/Memory
— Category 2 (strategic): [Y]% → Retain in KF (compress Type A)
— Category 3 (structured, MCP available): [Z]% → Migrate to [store]
— Category 4 (structured, no MCP): [W]% → RAG-optimize (flag opportunity)
— Net KF reduction: ~[S]K tokens

## RAG Quality Assessment (retrieval mode only)
[Seven-item checklist with pass/fail and fixes.]

## Optimization Plan

### Phase 1 — Zero-Effort [execute now]
[Actions. Cumulative savings: ~XK. Projected tier: N. Headroom: ~HK.]

### Phase 2 — High-Yield Optimization [execute during Phase [name]]
[Actions including data splits. Cumulative savings: ~XK. Projected tier: N.]

### Phase 3 — Reserve [execute if needed]
[Actions. Projected impact if deployed.]

## Post-Optimization Projection
[Projected state after each phase. Verification against planning ceiling.]
```

## Content Classification Framework

Knowledge file content falls into four categories that determine the optimal storage and access pattern. Type A/B classification (see `references/compression-execution.md`) determines compression depth for content staying in knowledge files. Category 1–4 classification determines whether content should stay in knowledge files at all. Apply both: Type A/B for compression, Category 1–4 for routing.

- **Category 1 — Behavioral/Instructional:** Rules, constraints, workflow instructions. Must be in always-present layers (CI, Memory, Tier 1 KF). Never place behind a tool call.
- **Category 2 — Strategic/Analytical:** Positioning analysis, opportunity matrices, design rationale. Benefits from passive awareness. Keep in knowledge files; compress Type A portions.
- **Category 3 — Structured Reference Data WITH MCP:** Tabular data with natural key-value structure where a queryable store is available via MCP. Strictly better than RAG for this content type — deterministic retrieval, structural integrity, permanent budget relief. See `references/content-routing.md` for the data split pattern.
- **Category 4 — Structured Reference Data WITHOUT MCP:** Same data types as Category 3, but no external store available. RAG-optimize as fallback. Flag the structural opportunity for future resolution.

For detailed guidance on each category, MCP infrastructure assessment, data split execution, fallback patterns, and retrieval quality tradeoffs, read `references/content-routing.md`.

### API Deployment as Alternative Architecture

When knowledge file requirements and cross-document synthesis needs exceed what Anthropic Projects can serve — very large content volumes that require cross-file reasoning that retrieval mode cannot preserve — surface API-based deployment. Context window: 1M tokens on Opus 5 / Sonnet 5 / Fable 5 (Opus 5's 1M is default AND max; no smaller variant), 200K on Haiku 4.5. Tradeoffs: per-token billing on massive inputs, higher latency (30–60+ seconds at high token counts), context rot at scale, full stack ownership (conversation management, retrieval, memory — all custom). API deployment is a different product architecture, not a casual upgrade. Recommend only when content volume and cross-document synthesis genuinely require it, and the user has engineering capacity for the integration. Do NOT recommend for projects that simply approach the current RAG activation point on their plan — most such projects benefit more from RAG quality optimization or a higher-window plan than from API-mode reconstruction.

## Empirical Threshold Measurement (procedural detail)

The "Core Concepts" section above summarizes the empirical measurement procedure. Additional detail:

**Precision method (±50–100 tokens):** Requires pre-sized calibration files at known token counts. Add or remove calibration files to binary-search the exact trigger point. See the Context Budget Calibration Lab methodology.

**Observable RAG indicators:** "Indexing" label in project UI files panel (visible without starting a conversation). `project_knowledge_search` tool present in available tools (definitive).

**When empirical measurement is worth the effort:** borderline projects where feasibility depends on precise numbers; unexpected RAG activation with no content changes (suggests a platform-side or plan/model change); after major Anthropic model or platform updates that may shift the RAG activation point. A measurement is a point-in-time snapshot for the current configuration — under automatic-by-window behavior, the number moves when Anthropic ships model or platform changes.

## When to Use This Skill

Use this Skill when:
- The user asks about context budget health, token usage, or project size
- The user reports context pressure symptoms: forgetting instructions, generic responses, inconsistency, content not found
- A project audit scores Knowledge Architecture ≤ 3 and the issue appears budget-related
- The user wants to understand retrieval mode or optimize for RAG quality
- The user is mid-compression and asks whether to continue or accept RAG mode

Do NOT use when:
- Content placement across layers — use rootnode-memory-optimization if available
- Overall project architecture quality — use rootnode-project-audit if available
- Claude behavioral tendencies — use rootnode-behavioral-tuning if available
- Building or revising a prompt — this Skill analyzes context economics, not prompt quality

## Troubleshooting

**User reports context pressure but project is Tier 1.** The issue is structural, not budget-related. Recommend rootnode-project-audit or rootnode-anti-pattern-detection if available.

**Feasibility says "Achievable" but gap is very tight.** Present as Borderline. Build in a 10–15% buffer. Check growth trajectory — if planned additions would re-cross the RAG activation point within a quarter, the recovery is temporary and the plan should account for it.

**User wants full-context but project is Tier 5.** Be direct: full-context recovery would remove core functionality. Optimize for retrieval quality. If cross-document synthesis at >500K tokens is required, surface the API path.

**Behavioral content in knowledge files (retrieval mode).** Highest-impact retrieval quality fix. Behavioral rules in knowledge files are intermittent in RAG mode. Move to CI or Memory. Recommend rootnode-behavioral-tuning if available for countermeasure calibration.

**Memory carrying reference-depth content.** Most common cross-project context issue. When Memory exceeds ~2K tokens, recommend rootnode-memory-optimization if available.

**Unexpected RAG activation with no knowledge file changes.** Check GitHub repo growth, uncounted file types (PDFs, images, DOCX). If no changes, platform update may have shifted the RAG activation point — recommend empirical measurement.

**MCP overhead estimates seem too high.** Check whether connectors use deferred loading. Prior estimates assuming always-loaded overstate overhead by 3–5x. Recalculate with correct loading mode.

**Compression has stalled or diminishing returns.** Run the Diminishing Returns Checkpoint from `references/compression-execution.md`. If remaining targets are predominantly Type B, present the RAG-Acceptance Decision Point. Do not compress precision reference content to reach the RAG activation point.

**User asks "should I accept RAG mode?"** Direct trigger for the RAG-Acceptance Decision Point in `references/compression-execution.md`. Determine whether optimization has been attempted first — if not, run a Quick Diagnostic before accepting.

**Optimization plan restores full-context mode (headroom below the RAG activation point) but growth will re-cross it.** This is the Gap 1 scenario. The plan targeted the current state, not the planning ceiling. Re-run Step 4 (Growth Trajectory) and revise the plan against the projected total. The user needs a strategy, not a cleanup.

**File contains mixed structured + strategic content.** Apply the Content Classification Framework. Split the file conceptually: strategic/analytical portions stay in the knowledge file, structured/tabular portions are data split candidates (Category 3) or RAG-optimization targets (Category 4). See `references/content-routing.md`.

## Reference Files

- **`references/evaluation-rubric.md`** — Read when performing a Full Budget Audit (Mode 2, Steps 3 and 7). Contains: six evaluation dimensions with detailed scoring criteria, tier decision matrix with tiebreaker logic, compression risk assessment, and seven-item RAG Quality Checklist.

- **`references/compression-execution.md`** — Read when recommending or executing compression. Contains: Content-Type Classification (Type A/B), compression tiers (safe/moderate/aggressive), MCP overhead estimation detail, sequencing rules, Diminishing Returns Checkpoint, RAG-Acceptance Decision Point, and budget-constrained project guidance.

- **`references/content-routing.md`** — Read when a file contains structured reference data or mixed content categories. Contains: Category 1–4 detailed descriptions, Data Split Pattern (Category 3) with MCP infrastructure assessment and platform dependency considerations, fallback pattern, retrieval quality tradeoff, and Structural Opportunity Flag (Category 4).
