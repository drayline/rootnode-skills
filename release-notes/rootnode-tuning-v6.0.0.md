# root.node Tuning v6.0.0

Diagnose Claude behavioral tendencies and produce targeted countermeasures for prompts and Project instructions.

Part of [root.node catalog v6.0](https://github.com/drayline/rootnode-skills/releases/tag/catalog-v6.0).

## Install

- **claude.ai:** **Customize > Plugins > Add > Add marketplace** → `drayline/rootnode-skills`, turn on **Sync automatically**, then add `rootnode-tuning`.
- **Claude Code:** `claude plugin marketplace add drayline/rootnode-skills`, then `claude plugin install rootnode-tuning@rootnode`.
- **Manual:** upload `rootnode-tuning-v6.0.0.zip` from the assets below at **Customize > Plugins > Add > Upload plugin**.

Install once: on your account or locally in Claude Code, not both.

## Skills

| Skill | Was | Version |
|---|---|---|
| `rootnode-tuning:behavioral-tuning` | `rootnode-behavioral-tuning` v5.0.0 | 6.0.0 |

## Changes in v6.0.0

- First release as a plugin. Skills renamed: the `rootnode-` prefix moved to the plugin. `metadata.version` 6.0.0 with `metadata.predecessor`.

## Upgrading from v5.x

Turn off or delete the standalone `rootnode-*` Skills this plugin replaces, or both copies load.
