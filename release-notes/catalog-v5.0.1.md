Patch release for the rootnode-skills catalog. 12 of the 27 Skills move to 5.0.1; the other 15 stay at 5.0.0.

This umbrella frames the patch as one catalog. Each patched Skill has its own v5.0.1 release; the Skill links below point at each Skill's current release, so unchanged Skills link to v5.0.

## What's in v5.0.1

The patch follows the behavioral validation (D9a) of cc-design 5.0 and the open findings from the v5.0 release. Calibration is unchanged: dual-primary for Opus 5.5 + Sonnet 5.5.

Load-bearing changes:

- **Stop-hook bounds, cc-design.** The v5.0 sketch released on the first continued stop, so its block cap could never trigger. Hooks now scope the count to the stop chain with `stop_hook_active`, with a no-progress cap and a chain-total cap, and still release when `jq` is missing. The guidance pairs the no-progress cap with Claude Code's own stop-hook continuation cap.
- **Migration guard example, cc-design.** The example catches `find … -delete`, `cd migrations && rm …`, globs that can expand to the protected folder, and PowerShell deletes and moves. It also states what a guard that reads command text cannot see, and points to the Claude Code setting that enforces.
- **Prompt patterns, cc-design.** Autonomous prompt templates gain a resume line. The shell guidance adds lessons from this patch's own build: a git pathspec with a trailing slash matches nothing, an exclude pathspec does not stage an untracked folder, a prompt names its Python interpreter, and a `claude -p` worker's allow-list names every command it runs.
- **critic-gate output.** The JSON verdict carries `status: complete | blocked`, so "could not inspect" is never an empty findings list. The field is additive.
- **One effort rule per Skill.** The five high-effort Skills (context-budget, full-stack-audit, global-audit, project-audit, prompt-compilation) state one effort rule, matching their calibration line.
- **Naming and references.** Every reference to the readiness gate uses `rootnode-handoff-trigger-check`. Current-tier wording, one heading and cross-references are corrected where the v5.0 review found them stale.

Every patched Skill is at 5.0.1; tiers are unchanged at 13 / 7 / 7. See the [Model Compatibility](https://github.com/drayline/rootnode-skills#model-compatibility) section of the README for effort defaults by model and surface, fallback semantics, and per-tier definitions.

## Download

**All Skills, one download:** grab `rootnode-catalog-v5.0.1.zip` from the Assets below. It bundles all 29 packaged Skill files (24 chat-side `-cp` flat zips for Claude Projects, 5 Claude Code `-cc` wrapper zips): the 12 patched Skills at 5.0.1 and the other 15 at 5.0.0. Unzip it, then upload or install the Skills you want.

**Already uploaded to Claude.ai?** Replace only the 12 patched Skills. Skills uploaded to Claude.ai also load in Claude Code when it is signed in with the same account; see the README Quick Start before also installing `-cc` copies.

**Individual Skills:** use the links under Skills below — each Skill's own release carries its packaged zip.

GitHub auto-attaches "Source code (zip / tar.gz)" to every release; those are the raw repository, not the packaged Skills. Ignore them and use the bundle or the per-Skill zips.

## Skills

**Build (3)**
- [rootnode-prompt-compilation](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-prompt-compilation/v5.0.1)
- [rootnode-skill-builder](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-skill-builder/v5.0)
- [rootnode-cc-design](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-cc-design/v5.0.1)

**Diagnose (5)**
- [rootnode-project-audit](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-project-audit/v5.0.1)
- [rootnode-global-audit](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-global-audit/v5.0.1)
- [rootnode-anti-pattern-detection](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-anti-pattern-detection/v5.0)
- [rootnode-prompt-validation](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-prompt-validation/v5.0.1)
- [rootnode-repo-hygiene](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-repo-hygiene/v5.0)

**Optimize (3)**
- [rootnode-behavioral-tuning](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-behavioral-tuning/v5.0)
- [rootnode-memory-optimization](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-memory-optimization/v5.0)
- [rootnode-context-budget](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-context-budget/v5.0.1)

**Cross-Layer (1)**
- [rootnode-full-stack-audit](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-full-stack-audit/v5.0.1)

**Bridge (2)**
- [rootnode-project-brief](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-project-brief/v5.0)
- [rootnode-session-handoff](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-session-handoff/v5.0)

**Cross-Boundary (2)**
- [rootnode-handoff-trigger-check](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-handoff-trigger-check/v5.0.1)
- [rootnode-profile-builder](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-profile-builder/v5.0)

**Runtime (CC, 2)**
- [rootnode-critic-gate](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-critic-gate/v5.0.1)
- [rootnode-mode-router](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-mode-router/v5.0.1)

**Block Libraries (4)**
- [rootnode-block-selection](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-block-selection/v5.0)
- [rootnode-identity-blocks](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-identity-blocks/v5.0)
- [rootnode-reasoning-blocks](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-reasoning-blocks/v5.0)
- [rootnode-output-blocks](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-output-blocks/v5.0)

**Domain Packs (5)**
- [rootnode-domain-business-strategy](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-domain-business-strategy/v5.0)
- [rootnode-domain-software-engineering](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-domain-software-engineering/v5.0)
- [rootnode-domain-content-communications](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-domain-content-communications/v5.0)
- [rootnode-domain-research-analysis](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-domain-research-analysis/v5.0.1)
- [rootnode-domain-agentic-context](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-domain-agentic-context/v5.0.1)

## Architecture

Two surfaces, one mental model. Chat-side Claude Projects and Claude Code execution share a unified principle layer covering placement discipline, decomposition by mechanism, behavioral countermeasures, cross-Skill composition contracts, verification-instruction discipline (D4), and landscape-volatility discipline (D8).

## Site

[rootnode.design](https://rootnode.design/)
