# rootnode-skills

Claude Skills built from the root.node prompt engineering system. Install any combination — each Skill works standalone.

**14 Skills across 4 layers:**

---

## Where to Start

**New to root.node Skills?** Install one of the domain packs for your primary work type. Each is self-contained.

**Building or improving Claude prompts?** Start with the Compiler layer (Skills 4–6).

**Diagnosing a Claude Project that isn't working?** Start with the Optimizer layer (Skills 1–3).

**Want the full system?** Enable all 14 Skills. They compose additively — each adds specialized depth without interfering with the others.

---

## The Skills

### Layer 1 — Optimizer (diagnose and improve existing Claude Projects)

| Skill | What it does |
|---|---|
| `rootnode-project-audit` | Scores Claude Projects on six dimensions using anchored 1–5 rubrics. Identifies what's broken and what to fix. |
| `rootnode-anti-pattern-detection` | Detects six structural patterns that cause ignored instructions and degraded output. |
| `rootnode-behavioral-tuning` | Diagnoses eight Claude behavioral tendencies (verbosity, hedging, list overuse, etc.) with countermeasure templates ready to paste into system prompts. |

### Layer 2 — Compiler (build well-structured Claude prompts)

| Skill | What it does |
|---|---|
| `rootnode-prompt-compilation` | Four-stage methodology for building Claude prompts: Parse → Select → Construct → Validate. |
| `rootnode-block-selection` | Selection decision trees for choosing the right identity, reasoning, and output approach for any task type. |
| `rootnode-prompt-validation` | Six-dimension Prompt Scorecard for evaluating existing prompts. Includes symptom-to-fix diagnostic map. |

### Layer 3 — Block Libraries (deep catalogs of approaches)

| Skill | What it does |
|---|---|
| `rootnode-identity-blocks` | Eight tested identity approaches (Strategic Advisor, Technical Architect, Research Synthesist, etc.) with complete XML templates and selection guidance. |
| `rootnode-reasoning-blocks` | Eighteen reasoning variants across six categories (Analytical, Strategic, Creative, Technical, Research, Comparative) with complete XML specifications. |
| `rootnode-output-blocks` | Ten output format specifications (Executive Brief, Technical Design Document, Decision Matrix, etc.) with section-by-section length guidance. |

### Layer 4 — Domain Packs (specialized methodology per domain)

| Skill | Domain |
|---|---|
| `rootnode-domain-business-strategy` | Consulting, M&A, corporate strategy, strategic planning |
| `rootnode-domain-software-engineering` | System design, code review, incident response, security analysis, API design |
| `rootnode-domain-content-communications` | Writing, editing, content strategy, copywriting, persuasion |
| `rootnode-domain-research-analysis` | Data analysis, policy research, investigative research, systematic review |
| `rootnode-domain-agentic-context` | AI agent design, tool interfaces, context architecture, multi-agent coordination |

Each domain pack includes identity approaches, reasoning methods, and output formats tuned for that domain — fully self-contained, no other Skills required.

---

## Installation

**Claude.ai:**
1. Download the skill folder you want (or clone the repo)
2. Zip the folder
3. Upload at Settings → Capabilities → Skills

**Claude Code:**
Place the skill folder in your Claude Code skills directory.

**API:**
Add to your Messages API request via the `container.skills` parameter (requires Code Execution Tool beta).

You can install any subset. Every Skill delivers complete value when installed alone.

---

## Composition

When multiple Skills are installed, they compose additively:

- **Optimizer + Compiler:** Audit an existing Project, then rebuild the system prompt using the compilation methodology.
- **Compiler + Block Libraries:** Build prompts using the compilation workflow; use library Skills for deeper catalog exploration on follow-up requests.
- **Compiler + Domain Pack:** Domain packs provide specialized approaches for the Select stage when the task is clearly domain-specific.
- **All 14:** Full root.node methodology available on demand. No Skills compete — each activates for its specific task type.

---

## The Full System

These Skills are extracted from the root.node prompt engineering system — a complete architecture for building, testing, and maintaining high-performance Claude Projects. The full system includes the integrated Compiler and Optimizer pipelines, the complete block library with worked examples, and the Project construction methodology.

Available at [rootnode.design](https://rootnode.design).

---

## License

Apache-2.0. See LICENSE.
