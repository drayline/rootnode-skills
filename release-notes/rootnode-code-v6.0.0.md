# root.node Code v6.0.0

Design and maintain Claude Code environments: environment design and remediation, repository hygiene scanning, plus a migration guard and a bounded test-evidence Stop hook.

Part of [root.node catalog v6.0](https://github.com/drayline/rootnode-skills/releases/tag/catalog-v6.0).

## Install

- **claude.ai:** **Customize > Plugins > Add > Add marketplace** → `drayline/rootnode-skills`, turn on **Sync automatically**, then add `rootnode-code`.
- **Claude Code:** `claude plugin marketplace add drayline/rootnode-skills`, then `claude plugin install rootnode-code@rootnode`.
- **Manual:** upload `rootnode-code-v6.0.0.zip` from the assets below at **Customize > Plugins > Add > Upload plugin**.

Install once: on your account or locally in Claude Code, not both.

## Skills

| Skill | Was | Version |
|---|---|---|
| `rootnode-code:cc-design` | `rootnode-cc-design` v5.0.1 | 6.0.0 |
| `rootnode-code:repo-hygiene` | `rootnode-repo-hygiene` v5.0.0 | 6.0.0 |

## Changes in v6.0.0

- First release as a plugin. Skills renamed: the `rootnode-` prefix moved to the plugin. `metadata.version` 6.0.0 with `metadata.predecessor`.
- Ships a migration guard (PreToolUse on Edit, Write, NotebookEdit, Bash, PowerShell; exit 2 blocks) and a bounded test-evidence Stop hook that exits 0 in a repo with no test command. Hooks run in every repository where the plugin is enabled; chat ignores them.
- cc-design: the hook reference carries the shipped scripts, checked by the packager; the guard-scope paragraph names the settings file for `denyWrite` (F-15); CR counting with a positive control (F-16); the execution-plan schema accepts `cc-design v…`.

## Upgrading from v5.x

Turn off or delete the standalone `rootnode-*` Skills this plugin replaces, or both copies load.
