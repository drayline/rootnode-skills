# root.node Prompts v6.0.0

Compile and score prompts: prompt compilation and validation, block selection, identity, reasoning, and output blocks, and five domain packs.

Part of [root.node catalog v6.0](https://github.com/drayline/rootnode-skills/releases/tag/catalog-v6.0).

## Install

- **claude.ai:** **Customize > Plugins > Add > Add marketplace** → `drayline/rootnode-skills`, turn on **Sync automatically**, then add `rootnode-prompts`.
- **Claude Code:** `claude plugin marketplace add drayline/rootnode-skills`, then `claude plugin install rootnode-prompts@rootnode`.
- **Manual:** upload `rootnode-prompts-v6.0.0.zip` from the assets below at **Customize > Plugins > Add > Upload plugin**.

Install once: on your account or locally in Claude Code, not both.

## Skills

| Skill | Was | Version |
|---|---|---|
| `rootnode-prompts:block-selection` | `rootnode-block-selection` v5.0.0 | 6.0.0 |
| `rootnode-prompts:domain-agentic-context` | `rootnode-domain-agentic-context` v5.0.1 | 6.0.0 |
| `rootnode-prompts:domain-business-strategy` | `rootnode-domain-business-strategy` v5.0.0 | 6.0.0 |
| `rootnode-prompts:domain-content-communications` | `rootnode-domain-content-communications` v5.0.0 | 6.0.0 |
| `rootnode-prompts:domain-research-analysis` | `rootnode-domain-research-analysis` v5.0.1 | 6.0.0 |
| `rootnode-prompts:domain-software-engineering` | `rootnode-domain-software-engineering` v5.0.0 | 6.0.0 |
| `rootnode-prompts:identity-blocks` | `rootnode-identity-blocks` v5.0.0 | 6.0.0 |
| `rootnode-prompts:output-blocks` | `rootnode-output-blocks` v5.0.0 | 6.0.0 |
| `rootnode-prompts:prompt-compilation` | `rootnode-prompt-compilation` v5.0.1 | 6.0.0 |
| `rootnode-prompts:prompt-validation` | `rootnode-prompt-validation` v5.0.1 | 6.0.0 |
| `rootnode-prompts:reasoning-blocks` | `rootnode-reasoning-blocks` v5.0.0 | 6.0.0 |

## Changes in v6.0.0

- First release as a plugin. Skills renamed: the `rootnode-` prefix moved to the plugin. `metadata.version` 6.0.0 with `metadata.predecessor`.

## Upgrading from v5.x

Turn off or delete the standalone `rootnode-*` Skills this plugin replaces, or both copies load.
