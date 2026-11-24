root.node catalog v6.1: the 27 Skills are calibrated for Claude Fable 5.2, and `cc-design` now sizes the stops and gates it designs to the size of the project.

## What's in v6.1

- **Two behavior changes.** First, `cc-design` now sizes stops and gates to a rigor level — sprint, standard or strict — and a small project with one contributor, no production data and nothing irreversible gets `sprint` by default: no reviewer role, no phase gates, and a session that stops only when the next step cannot be undone, when only you can make a decision, or when a spend cap is reached. Second, the `rootnode-code` hooks are opt-in since `rootnode-code` 6.1.0: they act only in a repository that adds `.claude/rootnode-gates.json`, and do nothing elsewhere.
- **Fable 5.2.** Claude Fable 5.2 replaces Fable 5.1. Opus 5.5 + Sonnet 5.5 stay the dual-primary pair for Tier 1 and Tier 2 Skills; Fable 5.2 becomes a named target for Tier 3 Skills — start at its `high` default and step down to `medium` where your evals hold. It costs about twice Opus 5.5 per token, so choose it for the hardest and longest runs. Tiers are unchanged: T1 13 / T2 7 / T3 7.
- **Seventeen tendencies.** `behavioral-tuning` adds #16 caution accumulation (the agent asks permission for routine steps because cautions piled up in memory, notes and instruction files) and #17 silent long runs, plus a fifth conditional defect: a token budget shown in the prompt raises spending.
- **Budgets out of prompts.** `cc-design` records spend and context limits in the design brief and enforces them with mechanisms such as `--max-budget-usd`, not with text in the prompt.
- **Stale cautions.** `memory-optimization` checks Memory, Custom Instructions and knowledge files for cautions whose reason no longer holds and proposes removal or a scoped rewrite.
- **Still unmeasured.** The eval suites have not been rerun this cycle. Treat all plugins as unmeasured until the next cycle's graders land.

## Install

- **claude.ai (recommended):** **Customize > Plugins > Add > Add marketplace** → `drayline/rootnode-skills`, turn on **Sync automatically**, then add the plugins you want.
- **Claude Code with an API key:** `claude plugin marketplace add drayline/rootnode-skills`, then `claude plugin install <plugin>@rootnode`. Run `claude plugin update` for new versions.
- If synced plugins do not appear in a Claude Code session that was already open, run `/reload-plugins` or restart Claude Code.
- Install each plugin once: on your account or locally, not both.

## Download

The six plugin zips are attached below. Upload one at **Customize > Plugins > Add > Upload plugin**. A manual upload does not update itself; the marketplace does.

GitHub auto-attaches "Source code (zip / tar.gz)" to every release; those are the raw repository, not the plugins. Ignore them.

## Plugins

### [rootnode-projects v6.1.0](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-projects/v6.1.0)

Audit and optimize Claude Projects and the claude.ai global layer. New in 6.1.0: a stale-caution check in `memory-optimization`.

Skills: `anti-pattern-detection`, `context-budget`, `full-stack-audit`, `global-audit`, `memory-optimization`, `project-audit`, `project-brief`.

### [rootnode-code v6.2.0](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-code/v6.2.0)

Design and maintain Claude Code environments. New in 6.2.0: rigor levels, the stop rule and positive scope in `cc-design`; budgets as mechanisms. The hooks are unchanged from 6.1.0 and stay opt-in.

Skills: `cc-design`, `repo-hygiene`.

### [rootnode-prompts v6.1.0](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-prompts/v6.1.0)

Compile and score prompts. New in 6.1.0: the example identity trait asks for the grounds of each conclusion instead of reasoning in the response; agent harness designs keep token budgets out of the agent's prompt.

Skills: `block-selection`, `domain-agentic-context`, `domain-business-strategy`, `domain-content-communications`, `domain-research-analysis`, `domain-software-engineering`, `identity-blocks`, `output-blocks`, `prompt-compilation`, `prompt-validation`, `reasoning-blocks`.

### [rootnode-tuning v6.1.0](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-tuning/v6.1.0)

Diagnose Claude behavioral tendencies and produce countermeasures. New in 6.1.0: tendencies #16 and #17, the prompt-visible budget defect, and Fable 5.2 facets on #11, #12, #13 and #15.

Skills: `behavioral-tuning`.

### [rootnode-governance v6.1.0](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-governance/v6.1.0)

Govern autonomous work: critic gate, mode router, handoff readiness check, session handoff, and profile builder. New in 6.1.0: Fable 5.2 calibration and model facts.

Skills: `critic-gate`, `handoff-trigger-check`, `mode-router`, `profile-builder`, `session-handoff`.

### [rootnode-skill-builder v6.1.0](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-skill-builder/v6.1.0)

Build, review, and evaluate Skills. New in 6.1.0: Fable 5.2 calibration.

Skills: `skill-builder`.

## Site

[rootnode.design](https://rootnode.design/)
