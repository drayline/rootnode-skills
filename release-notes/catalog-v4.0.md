5-generation Claude alignment ship for the rootnode-skills system. 27 Skills recalibrated 2026-07-25.

This release coordinates the v4.0 catalog ship. Each Skill ships its own per-package release; this is the umbrella that frames the catalog as a unified system.

## What's in v4.0

27 Skills across 9 functional categories. Two surfaces: chat-side Claude Projects and Claude Code execution. Unified by a single principle layer governing both.

The v4.0 ship is the 5-generation alignment cycle triggered by Claude Opus 5 GA (2026-07-24). Calibration scope moves to **Opus 5 + Sonnet 5 dual-primary** (both default to `high` effort on Claude API and Claude Code), with Fable 5 integrated-aware, Opus 4.8 fallback-graceful (a model users are silently served on classifier-flagged requests — Skills must produce correct-shape output there), Sonnet 4.6 legacy-graceful, and Haiku 4.5 graceful-with-extended-thinking.

Load-bearing changes:

- **Effort inversion.** Default effort is `high`, not `xhigh`. Anthropic recommends starting at `high` and stepping up to `xhigh` for demanding coding/agentic work. `low`/`medium` are legitimate primary cost controls, not degraded modes.
- **D4 verification-instruction discipline.** New AEA §4.14 codifies the surface-invariant rule: remove self-directed re-checking instructions (Opus 5 already re-checks its own work; instructing it compounds into over-verification), keep external-artifact verification (evidence grounding against sources / files / tests / rendered pages) in imperative voice. Sweep patterns and per-hit classification procedure documented.
- **D5 prompt-compilation contract change.** Project Mode delivers scaffold artifacts as separate files on disk (Custom Instructions + each knowledge file, `{code}_` prefixed) rather than inline code blocks. Inline delivery remains as a runtime-constrained fallback, flagged when used.
- **D6 context-budget rebuild.** Automatic-RAG-by-window replaces the 200K-era fixed-threshold model. Fixed-token tier bands retired for qualitative window-relative bands; the ~66,500 measurement preserved as historical context; empirical measurement is the primary method for borderline projects.
- **Tendency taxonomy expansion.** 10 → 14 numbered entries. Verbosity refactored into a three-surface family (conversational / agentic narration / written deliverable). Four Opus 5-specific tendencies added: over-verification (REMOVAL countermeasure), scope expansion, subagent over-delegation, correction narration. Two prompt/environment-conditional defects treated separately (conservative-instruction literalism, thinking-disabled output artifacts).
- **D8 canonical-KF mirror completion.** `root_CLAUDE_OPTIMIZATION_NOTES.md` and `root_AUDIT_FRAMEWORK.md` added to `audit/canonical-kfs/`; the O10 staleness diff now covers 7 KFs rather than 5.

Every Skill's calibration marker is updated to the new dual-primary scheme; the T3 label retires "Opus-recommended" for "High-effort recommended." Six previously untagged Skills received markers. See the [Model Compatibility](https://github.com/drayline/rootnode-skills#model-compatibility) section of the README for the full effort ladder, fallback semantics, and per-tier definitions.

## Download

**All Skills, one download:** grab `rootnode-catalog-v4.0.zip` from the Assets below. It bundles all 29 packaged Skill files (24 chat-side `-cp` flat zips for Claude Projects, 5 Claude Code `-cc` wrapper zips). Unzip it, then upload or install the Skills you want.

**Individual Skills:** use the links under Skills below — each Skill's own release carries its packaged zip.

GitHub auto-attaches "Source code (zip / tar.gz)" to every release; those are the raw repository, not the packaged Skills. Ignore them and use the bundle or the per-Skill zips.

## Skills

**Build (3)**
- [rootnode-prompt-compilation](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-prompt-compilation/v4.0)
- [rootnode-skill-builder](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-skill-builder/v4.0)
- [rootnode-cc-design](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-cc-design/v4.0)

**Diagnose (5)**
- [rootnode-project-audit](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-project-audit/v4.0)
- [rootnode-global-audit](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-global-audit/v4.0)
- [rootnode-anti-pattern-detection](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-anti-pattern-detection/v4.0)
- [rootnode-prompt-validation](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-prompt-validation/v4.0)
- [rootnode-repo-hygiene](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-repo-hygiene/v4.0)

**Optimize (3)**
- [rootnode-behavioral-tuning](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-behavioral-tuning/v4.0)
- [rootnode-memory-optimization](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-memory-optimization/v4.0)
- [rootnode-context-budget](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-context-budget/v4.0)

**Cross-Layer (1)**
- [rootnode-full-stack-audit](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-full-stack-audit/v4.0)

**Bridge (2)**
- [rootnode-project-brief](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-project-brief/v4.0)
- [rootnode-session-handoff](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-session-handoff/v4.0)

**Cross-Boundary (2)**
- [rootnode-handoff-trigger-check](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-handoff-trigger-check/v4.0)
- [rootnode-profile-builder](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-profile-builder/v4.0)

**Runtime (CC, 2)**
- [rootnode-critic-gate](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-critic-gate/v4.0)
- [rootnode-mode-router](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-mode-router/v4.0)

**Block Libraries (4)**
- [rootnode-block-selection](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-block-selection/v4.0)
- [rootnode-identity-blocks](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-identity-blocks/v4.0)
- [rootnode-reasoning-blocks](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-reasoning-blocks/v4.0)
- [rootnode-output-blocks](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-output-blocks/v4.0)

**Domain Packs (5)**
- [rootnode-domain-business-strategy](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-domain-business-strategy/v4.0)
- [rootnode-domain-software-engineering](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-domain-software-engineering/v4.0)
- [rootnode-domain-content-communications](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-domain-content-communications/v4.0)
- [rootnode-domain-research-analysis](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-domain-research-analysis/v4.0)
- [rootnode-domain-agentic-context](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-domain-agentic-context/v4.0)

## Architecture

Two surfaces, one mental model. Chat-side Claude Projects and Claude Code execution share a unified principle layer covering placement discipline, decomposition by mechanism, behavioral countermeasures, cross-Skill composition contracts, verification-instruction discipline (D4), and landscape-volatility discipline (D8).

## Site

[rootnode.design](https://rootnode.design/)
