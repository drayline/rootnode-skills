# rootnode-skills

An architecture system for Claude Projects. 15 Skills that diagnose, build, and optimize every layer of a Claude Project — install them all, activate what you need through keywords.

---

## Understanding Claude Project Architecture

A Claude Project isn't just a system prompt. It's a four-layer architecture, and how you distribute content across those layers determines whether Claude performs well or fights itself.

| Layer | What It Does | How It Works |
| --- | --- | --- |
| **Custom Instructions** | Always-loaded behavioral architecture | Defines who Claude is in this Project, how it should behave, what files exist and when to use them, what output standards to follow. Loaded in full every conversation. This is the structural backbone. |
| **Knowledge Files** | Searchable reference depth | Holds detailed documentation, frameworks, procedures, data, and examples. Claude searches these on demand — only loaded when relevant to the current task. The depth layer. |
| **Memory** | Always-loaded orientation facts | Concise facts Claude needs in every conversation: current project phase, active constraints, key decisions, user context. Updated easily without editing files. The orientation layer. |
| **Conversation** | Per-message working context | The actual back-and-forth. Everything above exists to make this layer more productive — less repetition, better first responses, consistent quality. |

Most people write a system prompt and stop. root.node Skills treat the whole Project as a system — scoring its architecture, detecting structural failures, rebalancing content across layers, and building prompts that fit correctly into the structure. The prompt engineering capabilities serve the architecture, not the other way around.

---

## How I Use These Skills

**Install all 15 Skills.** They don't compete — each activates only for its specific task type. With all Skills enabled, you have the full root.node methodology available on demand, and you activate what you need through keyword phrases in your messages.

### Activation Table

| Skill | What It Does | Keywords That Activate It |
| --- | --- | --- |
| `rootnode-project-audit` | Scores and diagnoses existing Claude Projects | "audit my project," "score my project," "review my custom instructions," "why is my project underperforming," "evaluate my Claude project" |
| `rootnode-anti-pattern-detection` | Detects structural mistakes causing ignored instructions | "what's wrong with my project," "Claude ignores my instructions," "diagnose my project," "why is output inconsistent" |
| `rootnode-behavioral-tuning` | Fixes Claude behavioral tendencies with countermeasure templates | "Claude is too verbose," "Claude keeps hedging," "Claude agrees with everything," "make Claude more direct," "Claude uses too many lists," "tune Claude's behavior" |
| `rootnode-memory-optimization` | Rebalances content across Memory, Custom Instructions, and knowledge files | "optimize my memory," "what should be in my memory," "trim my knowledge files," "reduce my context usage," "rebalance my project," "my project feels bloated" |
| `rootnode-prompt-compilation` | Builds complete Claude prompts and Project scaffolds | "build me a prompt," "create a system prompt," "write a Claude prompt," "design a prompt for," "scaffold a Claude Project" |
| `rootnode-block-selection` | Recommends the right identity, reasoning, and output approaches | "what approach should I use," "which reasoning method," "what identity fits this task," "which output format," "help me pick the right approach" |
| `rootnode-prompt-validation` | Evaluates and scores existing prompts with diagnostic fixes | "review my prompt," "score this prompt," "why isn't my prompt working," "what's wrong with my prompt," "improve my prompt" |
| `rootnode-identity-blocks` | Deep catalog of 8 tested identity approaches | "what role should Claude play," "identity for my prompt," "persona for this task," "pick an identity," "build a custom role" |
| `rootnode-reasoning-blocks` | Deep catalog of 18 reasoning variants across 6 categories | "what reasoning approach should I use," "how should Claude analyze this," "which thinking method fits," "recommend a reasoning pattern" |
| `rootnode-output-blocks` | Deep catalog of 10 output format specifications | "how should I structure this document," "what format for a board update," "format for a technical RFC," "help me design an output format" |
| `rootnode-domain-business-strategy` | Specialized approaches for consulting, M&A, corporate strategy | "build a prompt for M&A analysis," "due diligence prompt," "board narrative," "investment case," "market entry strategy" |
| `rootnode-domain-software-engineering` | Specialized approaches for system design, code review, architecture | "build a prompt for code review," "system design prompt," "security review prompt," "API design prompt," "RFC prompt" |
| `rootnode-domain-content-communications` | Specialized approaches for writing, editing, content strategy | "build a prompt for writing," "prompt for content strategy," "prompt for copywriting," "prompt for blog posts" |
| `rootnode-domain-research-analysis` | Specialized approaches for data analysis, policy, investigative research | "prompt for data analysis," "research prompt," "policy brief prompt," "literature review prompt" |
| `rootnode-domain-agentic-context` | Specialized approaches for AI agent design and context engineering | "design an agent," "agent system prompt," "context window architecture," "tool interface design," "multi-agent coordination" |

### Example Workflows

**"Audit my project — output quality has been inconsistent"**
→ Activates `rootnode-project-audit`. Scores your Project across six architectural dimensions (Identity Precision, Instruction Clarity, Knowledge & Context Architecture, Mode Design, Output Standards, Behavioral Calibration), detects anti-patterns, and produces prioritized fixes with specific evidence from your Project materials.

**"What's wrong with my project? Claude keeps ignoring my instructions"**
→ Activates `rootnode-anti-pattern-detection`. Checks for seven structural patterns — Misaligned Hierarchy (behavioral rules buried in knowledge files), Echo Chamber (same instruction in multiple places with different wording), Kitchen Sink (too many low-priority rules diluting the important ones), and four others. Every finding quotes the specific text causing the problem.

**"My project feels bloated — optimize my memory and trim my knowledge files"**
→ Activates `rootnode-memory-optimization`. Assesses your project's mission first, then audits what's in each layer. Produces specific Memory edit prescriptions (add/remove/replace) and knowledge file trimming recommendations, showing the cascade: these Memory edits enable these knowledge file trims, recovering this much context budget.

**"Claude is too verbose and keeps using bullet points for everything"**
→ Activates `rootnode-behavioral-tuning`. Diagnoses verbosity drift and list overuse as specific Claude tendencies, then provides countermeasure templates — exact language you paste into your Custom Instructions to fix the behavior at the architectural level, not per-conversation.

**"Audit my project, then rebuild the Custom Instructions"**
→ First activates `rootnode-project-audit` for a full evaluation. If three or more critical findings are present, it offers Reconstruct mode — producing complete, optimized Custom Instructions using XML tag boundaries, primacy-recency ordering, and scoped behavioral countermeasures. Then `rootnode-memory-optimization` can rebalance the context layers around the new architecture.

**"Scaffold a Claude Project for our engineering team's code review workflow"**
→ Activates `rootnode-prompt-compilation` for the build structure and `rootnode-domain-software-engineering` for specialized engineering approaches. Produces a complete Project scaffold: Custom Instructions with identity, behavioral rules, knowledge file routing, and output standards — plus recommendations for what goes in knowledge files vs. Memory.

**"Design a system prompt for an agent that does research and writes reports"**
→ Activates `rootnode-domain-agentic-context`. Provides agent-specific methodology: identity approaches for agent designers, tool interface design patterns, context window architecture, failure mode planning, and output formats for agent system prompts and architecture blueprints.

**"Build me a prompt for M&A due diligence, then review it"**
→ Activates `rootnode-prompt-compilation` for the build, then `rootnode-prompt-validation` for the review. Compilation builds a structured prompt using the four-stage methodology; validation scores it on six dimensions and identifies any weaknesses before you deploy it.

### How Skills Compose

You don't need to think about which Skills to enable for which task. With all 15 installed, they compose naturally around the Project lifecycle:

**Diagnose → Fix → Rebuild.** The Optimizer Skills work together as a diagnostic suite. An audit scores the architecture. Anti-pattern detection finds the structural failures. Behavioral tuning fixes Claude's tendencies. Memory optimization rebalances the context layers. Use any combination — or all four for a comprehensive pass that covers every optimizable dimension.

**Build → Select → Validate.** The Compiler Skills chain sequentially when you're constructing new prompts or Project scaffolds. Compilation builds the structure → block selection recommends the right approaches → validation scores the result. Each step hands off cleanly to the next.

**Domain Packs override generic approaches.** When your task is clearly in a specific domain (M&A analysis, code review, agent design), the domain pack activates instead of the generic block libraries — giving you specialized methodology without you needing to specify it.

**Block Libraries add depth on demand.** The compiler handles most builds with its built-in selection logic. When you want to explore options deeper ("show me all the reasoning approaches for technical tasks"), the library Skills activate with their full catalogs.

---

## The Skills

### Layer 1 — Optimizer (diagnose and improve existing Claude Projects)

| Skill | What it does |
| --- | --- |
| `rootnode-project-audit` | Scores Claude Projects on six dimensions using anchored 1–5 rubrics. Identifies what's broken and what to fix. |
| `rootnode-anti-pattern-detection` | Detects seven structural patterns that cause ignored instructions and degraded output. |
| `rootnode-behavioral-tuning` | Diagnoses eight Claude behavioral tendencies (verbosity, hedging, list overuse, etc.) with countermeasure templates ready to paste into system prompts. |
| `rootnode-memory-optimization` | Rebalances context across Memory, Custom Instructions, and knowledge files. Produces Memory edit prescriptions and knowledge file trimming recommendations. |

### Layer 2 — Compiler (build well-structured Claude prompts)

| Skill | What it does |
| --- | --- |
| `rootnode-prompt-compilation` | Four-stage methodology for building Claude prompts: Parse → Select → Construct → Validate. |
| `rootnode-block-selection` | Selection decision trees for choosing the right identity, reasoning, and output approach for any task type. |
| `rootnode-prompt-validation` | Six-dimension Prompt Scorecard for evaluating existing prompts. Includes symptom-to-fix diagnostic map. |

### Layer 3 — Block Libraries (deep catalogs of approaches)

| Skill | What it does |
| --- | --- |
| `rootnode-identity-blocks` | Eight tested identity approaches (Strategic Advisor, Technical Architect, Research Synthesist, etc.) with complete XML templates and selection guidance. |
| `rootnode-reasoning-blocks` | Eighteen reasoning variants across six categories (Analytical, Strategic, Creative, Technical, Research, Comparative) with complete XML specifications. |
| `rootnode-output-blocks` | Ten output format specifications (Executive Brief, Technical Design Document, Decision Matrix, etc.) with section-by-section length guidance. |

### Layer 4 — Domain Packs (specialized methodology per domain)

| Skill | Domain |
| --- | --- |
| `rootnode-domain-business-strategy` | Consulting, M&A, corporate strategy, strategic planning |
| `rootnode-domain-software-engineering` | System design, code review, incident response, security analysis, API design |
| `rootnode-domain-content-communications` | Writing, editing, content strategy, copywriting, persuasion |
| `rootnode-domain-research-analysis` | Data analysis, policy research, investigative research, systematic review |
| `rootnode-domain-agentic-context` | AI agent design, tool interfaces, context architecture, multi-agent coordination |

Each domain pack includes identity approaches, reasoning methods, and output formats tuned for that domain — fully self-contained, no other Skills required.

---

## Installation

**Claude.ai:**

1. Download the skill folders (or clone the repo)
2. Zip each folder
3. Upload at Settings → Capabilities → Skills

**Claude Code:**
Place the skill folders in your Claude Code skills directory.

**API:**
Add to your Messages API request via the `container.skills` parameter (requires Code Execution Tool beta).

Install all 15 for the full system. Every Skill also delivers complete value when installed alone.

---

## The Full System

These Skills were designed and built by the root.node project — a complete architecture for building, testing, and maintaining high-performance Claude Projects. The full system includes the integrated Compiler and Optimizer pipelines, the complete block library with worked examples, and the Project construction methodology.

Learn more at: [rootnode.design](https://rootnode.design).

---

## License

Apache-2.0. See LICENSE.
