# root.node Projects v6.0.0

Audit and optimize Claude Projects and the claude.ai global layer: Project scorecard, global-layer scorecard, full-stack audit, anti-pattern detection, memory and context-budget optimization, project brief.

Part of [root.node catalog v6.0](https://github.com/drayline/rootnode-skills/releases/tag/catalog-v6.0).

## Install

- **claude.ai:** **Customize > Plugins > Add > Add marketplace** → `drayline/rootnode-skills`, turn on **Sync automatically**, then add `rootnode-projects`.
- **Claude Code:** `claude plugin marketplace add drayline/rootnode-skills`, then `claude plugin install rootnode-projects@rootnode`.
- **Manual:** upload `rootnode-projects-v6.0.0.zip` from the assets below at **Customize > Plugins > Add > Upload plugin**.

Install once: on your account or locally in Claude Code, not both.

## Skills

| Skill | Was | Version |
|---|---|---|
| `rootnode-projects:anti-pattern-detection` | `rootnode-anti-pattern-detection` v5.0.0 | 6.0.0 |
| `rootnode-projects:context-budget` | `rootnode-context-budget` v5.0.1 | 6.0.0 |
| `rootnode-projects:full-stack-audit` | `rootnode-full-stack-audit` v5.0.1 | 6.0.0 |
| `rootnode-projects:global-audit` | `rootnode-global-audit` v5.0.1 | 6.0.0 |
| `rootnode-projects:memory-optimization` | `rootnode-memory-optimization` v5.0.0 | 6.0.0 |
| `rootnode-projects:project-audit` | `rootnode-project-audit` v5.0.1 | 6.0.0 |
| `rootnode-projects:project-brief` | `rootnode-project-brief` v5.0.0 | 6.0.0 |

## Changes in v6.0.0

- First release as a plugin. Skills renamed: the `rootnode-` prefix moved to the plugin. `metadata.version` 6.0.0 with `metadata.predecessor`.
- First eval suite, 5 cases for `claude plugin eval` (kept in the repo, not in the zip). The first run showed no lift over the base model; graders are being rewritten.

## Upgrading from v5.x

Turn off or delete the standalone `rootnode-*` Skills this plugin replaces, or both copies load.
