# rootnode-skills

An architecture system for Claude Projects. 15 Skills that diagnose, build, and optimize every layer of a Claude Project. Install them all and activate what you need through keywords.

![Skills](https://img.shields.io/badge/Skills-15-CC8A0A) ![License](https://img.shields.io/badge/License-Apache_2.0-blue) ![Platform](https://img.shields.io/badge/Platform-Claude.ai_·_Claude_Code_·_API-8B929E)

---

## Understanding Claude Project Architecture

Claude Projects are comprised of a four-layer architecture, and how you distribute content across those layers determines whether Claude performs at its potential or works against itself.

| Layer | How It Works |
|---|---|
| **Custom Instructions** | Always-loaded behavioral architecture. Defines who Claude is in this Project, how it should behave, what files exist and when to use them, what output standards to follow. Loaded in full every conversation. This is the structural backbone. |
| **Knowledge Files** | Searchable reference depth. Holds detailed documentation, frameworks, procedures, data, and examples. Claude searches these on demand, only loaded when relevant to the current task. |
| **Memory** | Always-loaded orientation facts. Concise facts Claude needs in every conversation: current project phase, active constraints, key decisions, user context. Updated easily without editing files. |
| **Conversation** | Per-message working context. The actual back-and-forth. Everything above exists to make this layer more productive: less repetition, better first responses, consistent quality. |

These skills treat the whole Project as a system: scoring its architecture, detecting where content is misplaced across layers, diagnosing Claude's specific behavioral tendencies, and building Projects that fit correctly into the structure from the start.

The system is calibrated to how Claude actually works: the behavioral tendencies documented through extensive testing (verbosity drift, hedging, list overuse, agreeableness bias, and four others), the specific loading behavior of each Project layer, and the architectural patterns that align with Anthropic's guidelines for Claude Project design. Every block in the system has been tested against these behaviors. Every countermeasure targets a specific, documented tendency.

---

### How Skills Compose

> [!TIP]
> With all 15 installed, Skills compose naturally around the Project lifecycle. You don't need to manage which ones activate.

| Composition | How It Works |
|---|---|
| **Diagnose, fix, rebuild** | The Optimizer Skills chain as a diagnostic suite. Audit scores the architecture, anti-pattern detection finds structural failures, behavioral tuning fixes Claude's tendencies, memory optimization rebalances the layers. Use any combination or all four. |
| **Build, select, validate** | The Compiler Skills chain sequentially. Compilation builds the structure, block selection recommends the right approaches, validation scores the result. Each step hands off to the next. |
| **Domain Packs** | When a task is clearly domain-specific (business strategy, code review, agent design), the domain pack activates instead of generic block libraries. Specialized methodology without you needing to specify it. |
| **Block Libraries** | The compiler handles most builds with built-in selection logic. Libraries activate when you want to explore deeper ("show me all the reasoning approaches for technical tasks"). |

---

## How to Use These Skills

**Install all 15 Skills.** They don't compete. Each activates only for its specific task type. With all Skills enabled, you activate what you need through keyword phrases in your messages.

<details>
<summary><strong>Activation Table</strong> (click to expand)</summary>
<br>

| Skill | Keywords That Activate It |
|---|---|
| `rootnode-prompt-compilation` | `build me a prompt`<br>`build me a Claude Project`<br>`scaffold a Claude Project`<br>`design a prompt for` |
| `rootnode-project-audit` | `audit my project`<br>`score my project`<br>`why is my project underperforming`<br>`evaluate my Claude project` |
| `rootnode-anti-pattern-detection` | `what's wrong with my project`<br>`Claude ignores my instructions`<br>`diagnose my project`<br>`why is output inconsistent` |
| `rootnode-behavioral-tuning` | `Claude agrees with everything`<br>`make Claude more direct`<br>`Claude uses too many lists`<br>`tune Claude's behavior` |
| `rootnode-memory-optimization` | `optimize my memory`<br>`trim my knowledge files`<br>`reduce my context usage`<br>`rebalance my project` |
| `rootnode-block-selection` | `what approach should I use`<br>`which reasoning method`<br>`what identity fits this task`<br>`help me pick the right approach` |
| `rootnode-prompt-validation` | `review my prompt`<br>`score this prompt`<br>`why isn't my prompt working`<br>`improve my prompt` |
| `rootnode-identity-blocks` | `what role should Claude play`<br>`identity for my prompt`<br>`persona for this task`<br>`build a custom role` |
| `rootnode-reasoning-blocks` | `what reasoning approach should I use`<br>`how should Claude analyze this`<br>`which thinking method fits`<br>`recommend a reasoning pattern` |
| `rootnode-output-blocks` | `how should I structure this document`<br>`what format for a board update`<br>`format for a technical RFC`<br>`help me design an output format` |
| `rootnode-domain-business-strategy` | `business strategy prompt`<br>`competitive analysis`<br>`market entry strategy`<br>`investment case` |
| `rootnode-domain-software-engineering` | `code review prompt`<br>`system design prompt`<br>`security review prompt`<br>`API design prompt` |
| `rootnode-domain-content-communications` | `prompt for writing`<br>`content strategy`<br>`prompt for copywriting`<br>`prompt for blog posts` |
| `rootnode-domain-research-analysis` | `data analysis prompt`<br>`research prompt`<br>`policy brief prompt`<br>`literature review prompt` |
| `rootnode-domain-agentic-context` | `design an agent`<br>`agent system prompt`<br>`context window architecture`<br>`tool interface design` |

</details>

<details>
<summary><strong>Example Workflows</strong> (click to expand)</summary>
<br>

| You say | What happens |
|---|---|
| "Build me a Claude Project for our engineering team's code review workflow." | `rootnode-prompt-compilation` builds the structure, `rootnode-domain-software-engineering` provides specialized approaches. Produces a complete Project scaffold with Custom Instructions, knowledge file routing, and Memory recommendations. |
| "Build me a Claude Project for an agent that does research and writes reports." | `rootnode-prompt-compilation` builds the Project structure, `rootnode-domain-agentic-context` provides agent-specific methodology: identity approaches, tool interface design, context window architecture, failure mode planning, and output formats for agent system prompts. |
| "Scaffold a Claude Project for a content strategy team." | `rootnode-prompt-compilation` builds the structure, `rootnode-domain-content-communications` provides specialized approaches. Same compilation process, different keyword, same result. |
| "Audit my project. Output quality has been inconsistent." | `rootnode-project-audit` scores your Project across six architectural dimensions, detects anti-patterns, and produces prioritized fixes with evidence from your Project materials. |
| "Audit my project, then rebuild the Custom Instructions." | `rootnode-project-audit` runs a full evaluation. If critical findings are present, it offers Reconstruct mode, producing complete optimized Custom Instructions. Then `rootnode-memory-optimization` rebalances the context layers around the new architecture. |
| "What's wrong with my project? Claude keeps ignoring my instructions." | `rootnode-anti-pattern-detection` checks for seven structural patterns (Misaligned Hierarchy, Echo Chamber, Kitchen Sink, and four others). Every finding quotes the specific text causing the problem. |
| "Optimize my memory and trim my knowledge files. Context feels overloaded." | `rootnode-memory-optimization` audits each layer, then produces Memory edit prescriptions and knowledge file trimming recommendations with cascading dependency analysis. |
| "Claude keeps agreeing with everything and won't push back." | `rootnode-behavioral-tuning` diagnoses the specific tendencies and provides countermeasure templates you paste directly into Custom Instructions. |
| "Review this prompt and tell me how to improve it." | `rootnode-prompt-validation` scores the prompt on six dimensions, maps each weakness to a specific structural cause, and prescribes targeted fixes. |

</details>

---

## The Skills

### Optimizer (diagnose and improve existing Claude Projects)

| Skill | What it does |
|---|---|
| `rootnode-project-audit` | Scores Claude Projects on six dimensions using anchored 1-5 rubrics. Identifies what's broken and what to fix. |
| `rootnode-anti-pattern-detection` | Detects seven structural patterns that cause ignored instructions and degraded output. |
| `rootnode-behavioral-tuning` | Diagnoses eight Claude behavioral tendencies (verbosity, hedging, list overuse, etc.) with countermeasure templates ready to paste into system prompts. |
| `rootnode-memory-optimization` | Rebalances context across Memory, Custom Instructions, and knowledge files. Produces Memory edit prescriptions and knowledge file trimming recommendations. |

### Compiler (build well-structured Claude Projects)

| Skill | What it does |
|---|---|
| `rootnode-prompt-compilation` | Four-stage methodology for building Claude Projects and prompts: Parse, Select, Construct, Validate. |
| `rootnode-block-selection` | Selection decision trees for choosing the right identity, reasoning, and output approach for any task type. |
| `rootnode-prompt-validation` | Six-dimension Prompt Scorecard for evaluating existing prompts. Includes symptom-to-fix diagnostic map. |

### Block Libraries (deep catalogs of approaches)

| Skill | What it does |
|---|---|
| `rootnode-identity-blocks` | Eight tested identity approaches (Strategic Advisor, Technical Architect, Research Synthesist, etc.) with complete XML templates and selection guidance. |
| `rootnode-reasoning-blocks` | Eighteen reasoning variants across six categories (Analytical, Strategic, Creative, Technical, Research, Comparative) with complete XML specifications. |
| `rootnode-output-blocks` | Ten output format specifications (Executive Brief, Technical Design Document, Decision Matrix, etc.) with section-by-section length guidance. |

### Domain Packs (specialized methodology per domain)

| Skill | Domain |
|---|---|
| `rootnode-domain-business-strategy` | Consulting, competitive analysis, corporate strategy, strategic planning |
| `rootnode-domain-software-engineering` | System design, code review, incident response, security analysis, API design |
| `rootnode-domain-content-communications` | Writing, editing, content strategy, copywriting, persuasion |
| `rootnode-domain-research-analysis` | Data analysis, policy research, investigative research, systematic review |
| `rootnode-domain-agentic-context` | AI agent design, tool interfaces, context architecture, multi-agent coordination |

Each domain pack includes identity approaches, reasoning methods, and output formats tuned for that domain. Fully self-contained, no other Skills required.

---

## Installation

> [!NOTE]
> Install all 15 for the full system. Every Skill also delivers complete value when installed alone.

**Claude.ai:**

1. Download the skill folders (or clone the repo)
2. Zip each folder
3. Upload at Settings > Capabilities > Skills

**Claude Code:**
Place the skill folders in your Claude Code skills directory.

**API:**
Add to your Messages API request via the `container.skills` parameter (requires Code Execution Tool beta).

---

## Feedback

These Skills are being actively refined based on real-world usage. If something doesn't work the way you'd expect, if a Skill misses an edge case, or if there's a workflow you wish existed, [open an issue](https://github.com/drayline/rootnode-skills/issues). That feedback directly shapes what gets improved next.

---

## The Full System

These Skills are extracted from a larger system. The full root.node methodology includes the integrated Compiler and Optimizer pipelines, complete block libraries with worked examples, 14 end-to-end demonstrations, and the Project construction methodology.

Learn more at [rootnode.design](https://rootnode.design).

---

## License

Apache-2.0. See LICENSE.
