# root.node Code v6.2.0

Design and maintain Claude Code environments: environment design and remediation, repository hygiene scanning, plus a migration guard and a bounded test-evidence Stop hook.

Part of [root.node catalog v6.1](https://github.com/drayline/rootnode-skills/releases/tag/catalog-v6.1).

## Install

- **claude.ai:** **Customize > Plugins > Add > Add marketplace** → `drayline/rootnode-skills`, turn on **Sync automatically**, then add `rootnode-code`.
- **Claude Code:** `claude plugin marketplace add drayline/rootnode-skills`, then `claude plugin install rootnode-code@rootnode`.
- **Manual:** upload `rootnode-code-v6.2.0.zip` from the assets below at **Customize > Plugins > Add > Upload plugin**.

Install once: on your account or locally in Claude Code, not both.

## Skills

| Skill | Was | Version |
|---|---|---|
| `rootnode-code:cc-design` | `rootnode-cc-design` v5.0.1 | 6.2.0 |
| `rootnode-code:repo-hygiene` | `rootnode-repo-hygiene` v5.0.0 | 6.2.0 |

## Changes in v6.2.0

- cc-design: a design now carries a rigor level — `sprint`, `standard` or `strict` — set by a new `rigor` field in the design brief and a sixth interview question. Every DESIGN and TEMPLATE output opens with `Rigor: <level> — <reason>`, and the level decides the gates, review roles, digest binding and report depth. A brief with no level is `sprint` unless it names production data, an irreversible operation, or more than one contributor, which make it `standard`; `strict` is chosen explicitly. At `sprint` the output has no reviewer role and no phase gates.
- cc-design: halt triggers follow a stop rule — stop only when the next action cannot be undone, when a decision could reasonably go either way and only the operator can make it, or when a spend cap is reached — plus the project's own irreversible actions. The session-prompt and autonomous-prompt templates no longer stop on a failing test, an unavailable tool or ambiguous input; they work through it and report it. Every prompt lists the routine actions that need no approval.
- cc-design: token budgets are no longer written into prompts. Spend and context limits go in the brief (new `limits` field) and are enforced by mechanisms such as `--max-budget-usd`.
- cc-design: Fable 5.2 facts in the delegation reference (model tiers, effort, self-review subagents at `xhigh` and `max`); the brief interview asks for each authority constraint with its reason.
- Calibration lines updated for Claude Fable 5.2, which replaces Fable 5.1: Tier 1 Skills name Fable 5.2 beside Opus 5.5, Sonnet 5.5 and Haiku 5.5; Tier 2 Skills add that Fable 5.2 defaults to `high` and steps down to `medium` where the work holds; Tier 3 Skills name Fable 5.2 as a target for the hardest and longest runs instead of a reserve. Tier membership is unchanged (13 / 7 / 7).
- Hooks unchanged since 6.1.0: both stay opt-in per repository through `.claude/rootnode-gates.json`.

## Upgrading from v5.x

Turn off or delete the standalone `rootnode-*` Skills this plugin replaces, or both copies load.
