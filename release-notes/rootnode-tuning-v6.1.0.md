# root.node Tuning v6.1.0

Diagnose Claude behavioral tendencies and produce targeted countermeasures for prompts and Project instructions.

Part of [root.node catalog v6.1](https://github.com/drayline/rootnode-skills/releases/tag/catalog-v6.1).

## Install

- **claude.ai:** **Customize > Plugins > Add > Add marketplace** → `drayline/rootnode-skills`, turn on **Sync automatically**, then add `rootnode-tuning`.
- **Claude Code:** `claude plugin marketplace add drayline/rootnode-skills`, then `claude plugin install rootnode-tuning@rootnode`.
- **Manual:** upload `rootnode-tuning-v6.1.0.zip` from the assets below at **Customize > Plugins > Add > Upload plugin**.

Install once: on your account or locally in Claude Code, not both.

## Skills

| Skill | Was | Version |
|---|---|---|
| `rootnode-tuning:behavioral-tuning` | `rootnode-behavioral-tuning` v5.0.0 | 6.1.0 |

## Changes in v6.1.0

- behavioral-tuning: seventeen tendencies. New #16 caution accumulation (the agent asks approval for routine steps or stops at the first error because cautions piled up) and #17 silent long runs (long stretches of tool calls with no user-facing text), each with routing rows, deployment calibration and a template in the reference.
- behavioral-tuning: a fifth conditional defect, a token budget shown in the prompt, which raises spending on Fable 5.2.
- behavioral-tuning: Fable 5.2 facets — on #11, "treat that answer as done" lines reduce the model's willingness to flag its own mistakes; on #12, ownership framing is a costed lever; on #13, self-review subagents at `xhigh` and `max`; on #15, effort conditioning and the finishing block's cost.
- Calibration lines updated for Claude Fable 5.2, which replaces Fable 5.1: Tier 1 Skills name Fable 5.2 beside Opus 5.5, Sonnet 5.5 and Haiku 5.5; Tier 2 Skills add that Fable 5.2 defaults to `high` and steps down to `medium` where the work holds; Tier 3 Skills name Fable 5.2 as a target for the hardest and longest runs instead of a reserve. Tier membership is unchanged (13 / 7 / 7).

## Upgrading from v5.x

Turn off or delete the standalone `rootnode-*` Skills this plugin replaces, or both copies load.
