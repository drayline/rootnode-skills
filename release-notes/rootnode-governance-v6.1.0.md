# root.node Governance v6.1.0

Govern autonomous work: critic gate, mode router, handoff readiness check, session handoff, and profile builder.

Part of [root.node catalog v6.1](https://github.com/drayline/rootnode-skills/releases/tag/catalog-v6.1).

## Install

- **claude.ai:** **Customize > Plugins > Add > Add marketplace** → `drayline/rootnode-skills`, turn on **Sync automatically**, then add `rootnode-governance`.
- **Claude Code:** `claude plugin marketplace add drayline/rootnode-skills`, then `claude plugin install rootnode-governance@rootnode`.
- **Manual:** upload `rootnode-governance-v6.1.0.zip` from the assets below at **Customize > Plugins > Add > Upload plugin**.

Install once: on your account or locally in Claude Code, not both.

## Skills

| Skill | Was | Version |
|---|---|---|
| `rootnode-governance:critic-gate` | `rootnode-critic-gate` v5.0.1 | 6.1.0 |
| `rootnode-governance:handoff-trigger-check` | `rootnode-handoff-trigger-check` v5.0.1 | 6.1.0 |
| `rootnode-governance:mode-router` | `rootnode-mode-router` v5.0.1 | 6.1.0 |
| `rootnode-governance:profile-builder` | `rootnode-profile-builder` v5.0.0 | 6.1.0 |
| `rootnode-governance:session-handoff` | `rootnode-session-handoff` v5.0.0 | 6.1.0 |

## Changes in v6.1.0

- Calibration lines updated for Claude Fable 5.2, which replaces Fable 5.1: Tier 1 Skills name Fable 5.2 beside Opus 5.5, Sonnet 5.5 and Haiku 5.5; Tier 2 Skills add that Fable 5.2 defaults to `high` and steps down to `medium` where the work holds; Tier 3 Skills name Fable 5.2 as a target for the hardest and longest runs instead of a reserve. Tier membership is unchanged (13 / 7 / 7).
- handoff-trigger-check: context-window and effort-default facts name Fable 5.2.

## Upgrading from v5.x

Turn off or delete the standalone `rootnode-*` Skills this plugin replaces, or both copies load.
