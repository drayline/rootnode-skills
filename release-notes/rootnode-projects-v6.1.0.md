# root.node Projects v6.1.0

Audit and optimize Claude Projects and the claude.ai global layer: Project scorecard, global-layer scorecard, full-stack audit, anti-pattern detection, memory and context-budget optimization, project brief.

Part of [root.node catalog v6.1](https://github.com/drayline/rootnode-skills/releases/tag/catalog-v6.1).

## Install

- **claude.ai:** **Customize > Plugins > Add > Add marketplace** → `drayline/rootnode-skills`, turn on **Sync automatically**, then add `rootnode-projects`.
- **Claude Code:** `claude plugin marketplace add drayline/rootnode-skills`, then `claude plugin install rootnode-projects@rootnode`.
- **Manual:** upload `rootnode-projects-v6.1.0.zip` from the assets below at **Customize > Plugins > Add > Upload plugin**.

Install once: on your account or locally in Claude Code, not both.

## Skills

| Skill | Was | Version |
|---|---|---|
| `rootnode-projects:anti-pattern-detection` | `rootnode-anti-pattern-detection` v5.0.0 | 6.1.0 |
| `rootnode-projects:context-budget` | `rootnode-context-budget` v5.0.1 | 6.1.0 |
| `rootnode-projects:full-stack-audit` | `rootnode-full-stack-audit` v5.0.1 | 6.1.0 |
| `rootnode-projects:global-audit` | `rootnode-global-audit` v5.0.1 | 6.1.0 |
| `rootnode-projects:memory-optimization` | `rootnode-memory-optimization` v5.0.0 | 6.1.0 |
| `rootnode-projects:project-audit` | `rootnode-project-audit` v5.0.1 | 6.1.0 |
| `rootnode-projects:project-brief` | `rootnode-project-brief` v5.0.0 | 6.1.0 |

## Changes in v6.1.0

- Calibration lines updated for Claude Fable 5.2, which replaces Fable 5.1: Tier 1 Skills name Fable 5.2 beside Opus 5.5, Sonnet 5.5 and Haiku 5.5; Tier 2 Skills add that Fable 5.2 defaults to `high` and steps down to `medium` where the work holds; Tier 3 Skills name Fable 5.2 as a target for the hardest and longest runs instead of a reserve. Tier membership is unchanged (13 / 7 / 7).
- memory-optimization: a new audit step (Stage 2d) checks Memory, Custom Instructions and knowledge files for cautions whose reason no longer holds, lines written for an older model, and absolute rules without scope. The fix is removal or a scoped rewrite, proposed to the user, never applied silently.
- context-budget: model facts refreshed for Fable 5.2 (1M context, Opus 4.7-era tokenizer, cache reads at $0.20 per million tokens).
- project-audit: the behavioral taxonomy count reads seventeen.

## Upgrading from v5.x

Turn off or delete the standalone `rootnode-*` Skills this plugin replaces, or both copies load.
