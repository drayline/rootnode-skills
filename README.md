# root.node Skills

**The architecture system for Claude Projects.**

21 Skills that diagnose, build, and optimize every layer of a Claude Project — from a single prompt to your entire Claude environment.

![Skills](https://img.shields.io/badge/Skills-21-CC8A0A) ![Version](https://img.shields.io/badge/Version-v2.1-CC8A0A) ![License](https://img.shields.io/badge/License-Apache_2.0-blue) ![Calibrated](https://img.shields.io/badge/Calibrated-Claude_Opus_4.7-8B929E)

---

## Quick Start

These Skills are designed for **Claude Projects** in the Claude.ai web app or Claude desktop app. Go to [Releases](https://github.com/drayline/rootnode-skills/releases), download the `.zip` files for the Skills you want, then upload them in **Settings → Capabilities → Skills**. No unzipping required.

Skills install once and become available across every Project in your Claude account. Activate them with natural language — no commands, no special syntax.

> [!NOTE]
> Install all 21 for the full system. Every Skill also works standalone.

> [!TIP]
> **Calibrated for Claude Opus 4.7.** Most Skills work fully on every Claude model; a few produce best results on Opus. See [Model Compatibility](#model-compatibility) for details.

Claude Code support arrives with the **Runtime layer in v2.2**. The current v2.1 catalog is sized for chat-based Project workflows; Runtime Skills (governance, gates, profile routing) will land in CC.

---

## Why Architecture Matters

Claude Projects have a layered architecture. How content is distributed across those layers determines whether Claude performs at its potential or works against itself.

The hard part isn't building a Project — it's seeing what's quietly working against you. Architectural inefficiencies don't announce themselves. They surface as vague symptoms: output that drifts, instructions that get ignored intermittently, quality that degrades over long conversations. These Skills surface those structural issues, triage them by impact, and produce targeted fixes.

The trap is that these symptoms look like behavior problems. They're not. A rule the user has rewritten five different ways still gets ignored because the layer it sits in is wrong, not because the rule is unclear. Cross-layer conflicts cause unpredictable output that no amount of prompt rewording will fix. Structural problems require structural solutions.

These Skills treat the entire architecture as a unified system — scoring each layer, detecting cross-layer conflicts, diagnosing behavioral tendencies, and building Projects that are structurally sound from the start. The system is calibrated to how Claude actually processes context: the behavioral tendencies documented through extensive testing, the loading behavior of each layer, and the architectural patterns that produce reliable output.

---

## The Architectural Layers

Four scopes, each with Skills that operate on it. Global layers form the foundation that spans every Project. Project layers shape behavior within a single Project. The Conversation layer is where you interact with the system. The Claude Code layer is where governance for autonomous execution will live in v2.2.

**One Skill spans every layer.** `rootnode-full-stack-audit` runs Project audit + Global audit + Cross-Layer Alignment in a single pass — the only Skill in the catalog that operates across scopes rather than within one. See [Cross-Layer](#cross-layer) in Core Skills for details.

### Global Scope

<div align="center">
  <img src="assets/global-layer.svg" alt="Global Scope architecture: 5 layers shared across all Projects" width="820">
</div>

<br>

Five layers shared across every Project: User Preferences, Styles, Global Memory, Skills, and MCP Connectors. These define the foundation Claude works with before any specific Project loads. Edits here cascade across your entire Claude environment, which is why structural problems at the Global level are some of the most consequential — and most invisible — issues a user can have.

### Project Scope

<div align="center">
  <img src="assets/project-layer.svg" alt="Project Scope architecture: 3 layers within each Claude Project" width="820">
</div>

<br>

Three layers that shape every conversation in a Project: Project Memory (orientation state), Custom Instructions (always-loaded behavioral architecture), and Knowledge Files (searchable reference depth). Most quality issues originate here — wrong content in wrong layer, instructions that fight each other, retrieval mode pressure from oversized Knowledge Files. The majority of root.node's Core Skills target this scope because it's where structure most directly determines output.

### Conversation Scope

<div align="center">
  <img src="assets/conversation-layer.svg" alt="Conversation Scope: where Skills activate, with bridge Skills for cross-Project and cross-Session continuity" width="820">
</div>

<br>

Where you interact with the Project. Most Skills activate here from natural language — block selection, domain packs, identity templates, reasoning approaches, output formats. Two Skills are bridges: `project-brief` captures Project context for use in other Projects; `session-handoff` preserves work state across separate conversations. Both produce artifacts designed to travel beyond the current exchange.

### Claude Code Scope

<div align="center">
  <img src="assets/claude-code-layer.svg" alt="Claude Code Scope: Runtime governance layer coming in v2.2" width="820">
</div>

<br>

The Runtime governance layer is in development and arrives in **v2.2**. Four Skills will provide profile-driven gates that control when work hands off to autonomous execution and which strictness applies per change. Two install to chat-Projects (CP-side); two install to the Claude Code environment (CC-side). The composition is cross-boundary by design — CP-side Skills decide when work is ready to enter execution; CC-side Skills govern execution while it runs.

---

## Model Compatibility

Skills are calibrated against Claude Opus 4.7 as the primary target. They use a three-tier compatibility model based on how each Skill behaves across model classes.

**Tier 1 — Model-compatible (10 Skills).** Catalog retrievals, template lookups, and selection logic. Work fully on Opus, Sonnet, and Haiku. Output quality is consistent across models because the Skill's job is structured retrieval, not multi-dimension analysis.

**Tier 2 — Sonnet-graceful (6 Skills).** Heavier analytical work that includes a token-budget awareness clause for graceful degradation. The Skill recognizes when running on a smaller model and adjusts depth without breaking. Output may be slightly less complete on Sonnet or Haiku, but every Skill component still produces.

**Tier 3 — Opus-recommended (5 Skills).** Multi-dimension analysis, full-Project audits, and complete prompt compilation. These Skills run cleanly on Opus 4.7. Sonnet output may be less complete; Haiku output may miss higher-order findings. Each T3 Skill prints an effort guidance note on activation when run on a non-Opus model so you know what to expect.

The tier values appear in every catalog table below. T1 and T2 Skills are safe to use on any model. T3 Skills are best on Opus when the deliverable is high-stakes — full Project audits, comprehensive Skill builds, complete prompt scaffolds.

---

## Core Skills

These operate directly on the architectural layers. They are the primary tools for building, diagnosing, and maintaining Claude Projects.

### Build

| Skill | Tier | What It Does |
|---|---|---|
| `rootnode-prompt-compilation` | T3 | Four-stage pipeline (Parse, Select, Construct, Validate) that builds complete prompts and scaffolds entire Claude Projects — Custom Instructions, knowledge file architecture, and global layer advisory. |
| `rootnode-skill-builder` | T2 | Converts design specifications into deployment-ready Skill packages (SKILL.md + references/). |

### Diagnose

| Skill | Tier | What It Does |
|---|---|---|
| `rootnode-project-audit` | T3 | Scores a Project on six dimensions with anchored 1-5 rubrics. Finds what's broken and prescribes targeted fixes. |
| `rootnode-global-audit` | T3 | Audits all five global layers (Preferences, Styles, Memory, Skills, Connectors) using a six-dimension scorecard. Detects cross-layer failure modes. |
| `rootnode-anti-pattern-detection` | T2 | Detects seven structural patterns that cause ignored instructions and degraded output. |
| `rootnode-prompt-validation` | T2 | Six-dimension Prompt Scorecard for evaluating prompts. Maps each weakness to a structural fix. |

### Optimize

| Skill | Tier | What It Does |
|---|---|---|
| `rootnode-behavioral-tuning` | T2 | Diagnoses ten Claude behavioral tendencies (verbosity, hedging, agreeableness, fabricated precision, and others) with countermeasure templates ready to deploy. |
| `rootnode-memory-optimization` | T2 | Rebalances content across Memory, Custom Instructions, knowledge files, and User Preferences. Produces edit prescriptions and trimming recommendations. |
| `rootnode-context-budget` | T3 | Full context budget analysis: two-pool architecture (~66,500 token RAG threshold), per-file evaluation across six dimensions, content routing by category, growth trajectory assessment, retrieval quality audit, and phased optimization with compression safeguards. |

### Cross-Layer

This Skill operates across the architecture rather than within a single scope. It runs every layer-level audit and the alignment check between layers in a single pass — the most comprehensive diagnostic in the catalog.

| Skill | Tier | What It Does |
|---|---|---|
| `rootnode-full-stack-audit` | T3 | Runs Project audit + Global audit + Cross-Layer Alignment Check in a single pass. Scores both Project and Global layers using their respective six-dimension scorecards, detects cross-layer failure modes that single-scope audits can't see, and produces a unified action plan ordered by impact. |

### Bridge

These Skills produce artifacts that travel between conversations and Projects. They are the only Skills in the catalog whose output is designed to be uploaded into a different context.

| Skill | Tier | What It Does |
|---|---|---|
| `rootnode-project-brief` | T1 | Generates a structured Project Brief — extracts goals, architecture, knowledge file inventory, Custom Instructions summary, Memory contents, current state, and key decisions from a Claude Project. Briefs serve as uploadable context for cross-Project work. |
| `rootnode-session-handoff` | T1 | Produces structured XML session continuation documents. Captures active work streams, decisions with rationale, uploaded file content, conversation knowledge, and open items into an ingestion-optimized handoff file. |

---

## Supporting Skills

These activate automatically in the background when Core Skills need them. They provide the specialized methodology that the Compiler and audit tools draw on during assembly and evaluation.

### Block Libraries

Deep catalogs of tested prompt approaches. The Compiler selects from these during prompt and Project assembly.

| Skill | Tier | Contents |
|---|---|---|
| `rootnode-block-selection` | T2 | Decision trees for choosing the right identity, reasoning, and output approach for any task type. The router for the libraries below. |
| `rootnode-identity-blocks` | T1 | 8 identity approaches (Strategic Advisor, Technical Architect, Research Synthesist, and more) |
| `rootnode-reasoning-blocks` | T1 | 18 reasoning variants across 6 categories (Analytical, Strategic, Creative, Technical, Research, Comparative) |
| `rootnode-output-blocks` | T1 | 10 output format specifications (Executive Brief, Technical Design, Decision Matrix, and more) |

### Domain Packs

Specialized identity, reasoning, and output approaches tuned for specific professional domains. The Compiler selects from these automatically when building domain-specific prompts or Projects.

| Skill | Tier | Domain |
|---|---|---|
| `rootnode-domain-business-strategy` | T1 | Consulting, competitive analysis, corporate strategy, M&A |
| `rootnode-domain-software-engineering` | T1 | System design, code review, incident response, security, API design |
| `rootnode-domain-content-communications` | T1 | Writing, editing, content strategy, copywriting, persuasion |
| `rootnode-domain-research-analysis` | T1 | Data analysis, policy research, evidence synthesis, systematic review |
| `rootnode-domain-agentic-context` | T1 | AI agent design, tool interfaces, context architecture, multi-agent coordination |

---

## How Skills Compose

With all 21 installed, Skills compose naturally around the Project lifecycle. Keyword phrases in your messages trigger the right combination automatically.

| You Say | What Happens |
|---|---|
| "Build me a Claude Project for our engineering team's code review workflow." | Compilation builds the full scaffold — Custom Instructions, knowledge file architecture, global layer advisory. The software engineering domain pack provides specialized approaches. |
| "Audit my project. Output quality has been inconsistent." | Project audit scores six dimensions, detects anti-patterns, and produces prioritized fixes grounded in evidence from your Project. |
| "Run a full stack audit of everything — my project and my global setup." | Full-stack audit runs both Project and Global scorecards, checks cross-layer alignment across all nine layers, and produces a unified action plan. |
| "Claude keeps agreeing with everything and won't push back." | Behavioral tuning diagnoses the specific tendencies and provides countermeasure templates to deploy in Custom Instructions. |
| "Run a context budget analysis." | Runs a full context budget analysis — per-file evaluation, content routing, retrieval quality — and recommends goal-informed optimizations for your Project. |
| "Capture this Project's context so I can use it in another Project." | Project brief generates a structured upload-ready document with the Project's goals, architecture, knowledge files, instructions summary, and key decisions. |
| "Wrap up this session. Build a handoff for the next conversation." | Session handoff captures active work streams, decisions with rationale, open items, and a starter prompt for the next conversation. |

<details>
<summary><strong>More examples</strong></summary>
<br>

| You Say | What Happens |
|---|---|
| "Build me a Claude Project for an agent that does research and writes reports." | Compilation builds the full scaffold. The agentic domain pack provides agent-specific methodology: tool interface design, context architecture, failure mode planning. |
| "What's wrong with my project? Claude keeps ignoring my instructions." | Anti-pattern detection checks for seven structural patterns. Every finding quotes the specific text causing the problem. |
| "Optimize my memory. I think it needs to be trimmed." | Memory optimization audits for redundancy and staleness, identifies what should be promoted to Preferences or demoted to knowledge files, and produces specific edit prescriptions. |
| "Review this prompt and tell me how to improve it." | Prompt validation scores six dimensions, maps each weakness to a structural cause, and prescribes targeted fixes. |
| "Build this Skill from my design spec." | Skill builder converts your spec into a deployment-ready SKILL.md + references/ package following the full Skills specification. |
| "Help me pick the right reasoning approach for this analytical task." | Block selection walks the decision tree across the 18 reasoning variants and recommends the best fit with rationale. |

</details>

---

## Roadmap

**v2.2 — Runtime layer for Claude Code.** Four Skills providing profile-driven gates that govern autonomous execution. Two install to chat-Projects (CP-side: handoff readiness, profile authoring), two install to Claude Code (CC-side: change safety review, mode-aware routing). Profile-portable across orchestrators.

This layer brings Claude Code support to root.node. The current v2.1 catalog is sized for Claude Project workflows — long conversational diagnostics, interactive scorecards, markdown deliverables that humans review. Runtime Skills will be sized for autonomous-execution governance — JSON in, JSON out, gate verdicts, no conversational scaffolding required.

No timeline commitment. The Runtime layer is in active design and will ship when it's ready.

---

## About

root.node is an open-source architecture system for Claude Projects. These Skills are its deployable layer. The framework documentation, architectural references, and worked examples live at **[rootnode.design](https://rootnode.design)**.

---

## Feedback

These Skills are actively refined based on real-world usage. If something doesn't work the way you'd expect, or there's a workflow you wish existed, [open an issue](https://github.com/drayline/rootnode-skills/issues).

---

## License

Apache-2.0. See [LICENSE](LICENSE).
