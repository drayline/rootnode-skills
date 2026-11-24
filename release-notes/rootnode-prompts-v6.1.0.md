# root.node Prompts v6.1.0

Compile and score prompts: prompt compilation and validation, block selection, identity, reasoning, and output blocks, and five domain packs.

Part of [root.node catalog v6.1](https://github.com/drayline/rootnode-skills/releases/tag/catalog-v6.1).

## Install

- **claude.ai:** **Customize > Plugins > Add > Add marketplace** → `drayline/rootnode-skills`, turn on **Sync automatically**, then add `rootnode-prompts`.
- **Claude Code:** `claude plugin marketplace add drayline/rootnode-skills`, then `claude plugin install rootnode-prompts@rootnode`.
- **Manual:** upload `rootnode-prompts-v6.1.0.zip` from the assets below at **Customize > Plugins > Add > Upload plugin**.

Install once: on your account or locally in Claude Code, not both.

## Skills

| Skill | Was | Version |
|---|---|---|
| `rootnode-prompts:block-selection` | `rootnode-block-selection` v5.0.0 | 6.1.0 |
| `rootnode-prompts:domain-agentic-context` | `rootnode-domain-agentic-context` v5.0.1 | 6.1.0 |
| `rootnode-prompts:domain-business-strategy` | `rootnode-domain-business-strategy` v5.0.0 | 6.1.0 |
| `rootnode-prompts:domain-content-communications` | `rootnode-domain-content-communications` v5.0.0 | 6.1.0 |
| `rootnode-prompts:domain-research-analysis` | `rootnode-domain-research-analysis` v5.0.1 | 6.1.0 |
| `rootnode-prompts:domain-software-engineering` | `rootnode-domain-software-engineering` v5.0.0 | 6.1.0 |
| `rootnode-prompts:identity-blocks` | `rootnode-identity-blocks` v5.0.0 | 6.1.0 |
| `rootnode-prompts:output-blocks` | `rootnode-output-blocks` v5.0.0 | 6.1.0 |
| `rootnode-prompts:prompt-compilation` | `rootnode-prompt-compilation` v5.0.1 | 6.1.0 |
| `rootnode-prompts:prompt-validation` | `rootnode-prompt-validation` v5.0.1 | 6.1.0 |
| `rootnode-prompts:reasoning-blocks` | `rootnode-reasoning-blocks` v5.0.0 | 6.1.0 |

## Changes in v6.1.0

- Calibration lines updated for Claude Fable 5.2, which replaces Fable 5.1: Tier 1 Skills name Fable 5.2 beside Opus 5.5, Sonnet 5.5 and Haiku 5.5; Tier 2 Skills add that Fable 5.2 defaults to `high` and steps down to `medium` where the work holds; Tier 3 Skills name Fable 5.2 as a target for the hardest and longest runs instead of a reserve. Tier membership is unchanged (13 / 7 / 7).
- identity-blocks and block-selection: the example behavioral sentence no longer asks the model to explain its reasoning in the response; it now asks for the grounds of each conclusion.
- domain-agentic-context: a fifth harness rule keeps token budgets out of the agent's prompt (the per-zone token plan stays in the design document); refusal, fallback and forced `tool_choice` facts name Fable 5.2.
- prompt-compilation: the `reasoning_extraction` note names Fable 5.2.

## Upgrading from v5.x

Turn off or delete the standalone `rootnode-*` Skills this plugin replaces, or both copies load.
