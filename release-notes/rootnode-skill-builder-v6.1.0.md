# root.node Skill Builder v6.1.0

Build, review, and evaluate Skills with warrant checks, description discipline, packaging, and eval tooling.

Part of [root.node catalog v6.1](https://github.com/drayline/rootnode-skills/releases/tag/catalog-v6.1).

## Install

- **claude.ai:** **Customize > Plugins > Add > Add marketplace** → `drayline/rootnode-skills`, turn on **Sync automatically**, then add `rootnode-skill-builder`.
- **Claude Code:** `claude plugin marketplace add drayline/rootnode-skills`, then `claude plugin install rootnode-skill-builder@rootnode`.
- **Manual:** upload `rootnode-skill-builder-v6.1.0.zip` from the assets below at **Customize > Plugins > Add > Upload plugin**.

Install once: on your account or locally in Claude Code, not both.

## Skills

| Skill | Was | Version |
|---|---|---|
| `rootnode-skill-builder:skill-builder` | `rootnode-skill-builder` v5.0.0 | 6.1.0 |

## Changes in v6.1.0

- Calibration lines updated for Claude Fable 5.2, which replaces Fable 5.1: Tier 1 Skills name Fable 5.2 beside Opus 5.5, Sonnet 5.5 and Haiku 5.5; Tier 2 Skills add that Fable 5.2 defaults to `high` and steps down to `medium` where the work holds; Tier 3 Skills name Fable 5.2 as a target for the hardest and longest runs instead of a reserve. Tier membership is unchanged (13 / 7 / 7).
- skill-builder: SKILL.md cites the 17-tendency taxonomy for D9c analytical validation. Three reference lines (`references/behavioral-validation.md` twice, `references/skills-spec.md` once) still say 15; they are fixed in the next patch.

## Upgrading from v5.x

Turn off or delete the standalone `rootnode-*` Skills this plugin replaces, or both copies load.
