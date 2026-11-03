# root.node Governance v6.0.0

Govern autonomous work: critic gate, mode router, handoff readiness check, session handoff, and profile builder.

Part of [root.node catalog v6.0](https://github.com/drayline/rootnode-skills/releases/tag/catalog-v6.0).

## Install

- **claude.ai:** **Customize > Plugins > Add > Add marketplace** → `drayline/rootnode-skills`, turn on **Sync automatically**, then add `rootnode-governance`.
- **Claude Code:** `claude plugin marketplace add drayline/rootnode-skills`, then `claude plugin install rootnode-governance@rootnode`.
- **Manual:** upload `rootnode-governance-v6.0.0.zip` from the assets below at **Customize > Plugins > Add > Upload plugin**.

Install once: on your account or locally in Claude Code, not both.

## Skills

| Skill | Was | Version |
|---|---|---|
| `rootnode-governance:critic-gate` | `rootnode-critic-gate` v5.0.1 | 6.0.0 |
| `rootnode-governance:handoff-trigger-check` | `rootnode-handoff-trigger-check` v5.0.1 | 6.0.0 |
| `rootnode-governance:mode-router` | `rootnode-mode-router` v5.0.1 | 6.0.0 |
| `rootnode-governance:profile-builder` | `rootnode-profile-builder` v5.0.0 | 6.0.0 |
| `rootnode-governance:session-handoff` | `rootnode-session-handoff` v5.0.0 | 6.0.0 |

## Changes in v6.0.0

- First release as a plugin. Skills renamed: the `rootnode-` prefix moved to the plugin. `metadata.version` 6.0.0 with `metadata.predecessor`.
- profile-builder example: schema lookup for plugin installs.

## Upgrading from v5.x

Turn off or delete the standalone `rootnode-*` Skills this plugin replaces, or both copies load.
