root.node catalog v6.0: the 27 Skills now ship as six plugins from one marketplace. Install once on your claude.ai account and the Skills load in chat, Cowork, and Claude Code, with updates through the marketplace.

## What's in v6.0

- **Plugins, not zips.** Six plugins grouped by job replace the 29 per-Skill zips. The repo is a plugin marketplace named `rootnode`.
- **New names.** The `rootnode-` prefix moved from each Skill to its plugin: `rootnode-project-audit` is now `rootnode-projects:project-audit`.
- **Hooks.** `rootnode-code` ships a migration guard and a bounded test-evidence Stop hook. They run in every repository where the plugin is enabled.
- **First eval suite.** `rootnode-projects` ships 5 eval cases for `claude plugin eval`. The first run showed no lift over the base model: every case scored the same with and without the plugin, because the graders did not test anything the base model misses. Treat all plugins as unmeasured until the next cycle's graders land.
- **Calibration unchanged** from v5.0: Opus 5.5 + Sonnet 5.5 dual-primary; tiers T1 13 / T2 7 / T3 7.

## Install

- **claude.ai (recommended):** **Customize > Plugins > Add > Add marketplace** → `drayline/rootnode-skills`, turn on **Sync automatically**, then add the plugins you want.
- **Claude Code with an API key:** `claude plugin marketplace add drayline/rootnode-skills`, then `claude plugin install <plugin>@rootnode`. Run `claude plugin update` for new versions.
- Install each plugin once: on your account or locally, not both.

## Upgrading from v5.x

After you add the plugins, turn off or delete the old `rootnode-*` Skills where you uploaded them, and remove any `rootnode-*` folders from `~/.claude/skills/`. Otherwise both copies load.

## Download

The six plugin zips are attached below. Upload one at **Customize > Plugins > Add > Upload plugin**. A manual upload does not update itself; the marketplace does.

GitHub auto-attaches "Source code (zip / tar.gz)" to every release; those are the raw repository, not the plugins. Ignore them.

## Plugins

### [rootnode-projects v6.0.0](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-projects/v6.0.0)

Audit and optimize Claude Projects and the claude.ai global layer: Project scorecard, global-layer scorecard, full-stack audit, anti-pattern detection, memory and context-budget optimization, project brief.

Skills: `anti-pattern-detection`, `context-budget`, `full-stack-audit`, `global-audit`, `memory-optimization`, `project-audit`, `project-brief`.

### [rootnode-code v6.0.0](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-code/v6.0.0)

Design and maintain Claude Code environments: environment design and remediation, repository hygiene scanning, plus a migration guard and a bounded test-evidence Stop hook.

Skills: `cc-design`, `repo-hygiene`.

### [rootnode-prompts v6.0.0](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-prompts/v6.0.0)

Compile and score prompts: prompt compilation and validation, block selection, identity, reasoning, and output blocks, and five domain packs.

Skills: `block-selection`, `domain-agentic-context`, `domain-business-strategy`, `domain-content-communications`, `domain-research-analysis`, `domain-software-engineering`, `identity-blocks`, `output-blocks`, `prompt-compilation`, `prompt-validation`, `reasoning-blocks`.

### [rootnode-tuning v6.0.0](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-tuning/v6.0.0)

Diagnose Claude behavioral tendencies and produce targeted countermeasures for prompts and Project instructions.

Skills: `behavioral-tuning`.

### [rootnode-governance v6.0.0](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-governance/v6.0.0)

Govern autonomous work: critic gate, mode router, handoff readiness check, session handoff, and profile builder.

Skills: `critic-gate`, `handoff-trigger-check`, `mode-router`, `profile-builder`, `session-handoff`.

### [rootnode-skill-builder v6.0.0](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-skill-builder/v6.0.0)

Build, review, and evaluate Skills with warrant checks, description discipline, packaging, and eval tooling.

Skills: `skill-builder`.

## Architecture

Two surfaces, one mental model. Chat-side Claude Projects and Claude Code execution share a unified principle layer covering placement discipline, decomposition by mechanism, behavioral countermeasures, cross-Skill composition contracts, verification-instruction discipline (D4), and landscape-volatility discipline (D8).

## Site

[rootnode.design](https://rootnode.design/)
