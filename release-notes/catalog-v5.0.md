5.5-generation Claude alignment ship for the rootnode-skills system. 27 Skills recalibrated 2026-10-22.

This release coordinates the v5.0 catalog ship. Each Skill ships its own per-package release; this is the umbrella that frames the catalog as a unified system.

## What's in v5.0

27 Skills across 9 functional categories. Two surfaces: chat-side Claude Projects and Claude Code execution. Unified by a single principle layer governing both.

The v5.0 ship is the 5.5-generation alignment cycle triggered by four releases in five weeks: Fable 5.1, Opus 5.5, Sonnet 5.5, and Haiku 5.5. Calibration scope moves to **Opus 5.5 + Sonnet 5.5 dual-primary** (Opus 5.5 is the Claude Code default on every Anthropic-hosted plan), with Fable 5.1 integrated-aware, Haiku 5.5 subagent-aware, Opus 5 / Sonnet 5 fallback-graceful, and Sonnet 4.6 legacy-graceful. Haiku 4.5 leaves calibration scope; on third-party providers the `haiku` alias may still resolve to it — pin `claude-haiku-5-5` via `ANTHROPIC_DEFAULT_HAIKU_MODEL`.

Load-bearing changes:

- **Effort default moved.** Opus 5.5, Sonnet 5.5, and Haiku 5.5 default to `medium` in Claude Code (Sonnet 5.5 and Fable 5.1 default to `high` on the Claude API). Anthropic reports Opus 5.5 at `medium` matches or exceeds Opus 5 at `high`. Every calibration line is rewritten whole; `xhigh`/`max` are reserved for measured gains.
- **Thinking can no longer be disabled** on Opus 5.5, Sonnet 5.5, or Fable 5.1. Prompt scaffolds drop thinking-disabled mitigations, and instructions that ask the model to reproduce its reasoning in the response are flagged as a `reasoning_extraction` refusal trigger (prompt-compilation, prompt-validation, reasoning-blocks).
- **Tendency #15 — early turn termination.** The behavioral taxonomy grows 14 → 15 with the one behavior documented across all four 5.5-generation prompting guides: ending a turn with a summary and no tool call while work is still owed. behavioral-tuning also repairs its routing surface so tendencies 11–15 are reachable from SKILL.md, and carries Anthropic's countermeasure blocks verbatim.
- **Hook correctness fix (cc-design, repo-hygiene).** cc-design's hook reference taught `exit 1` as blocking and a `"matchers"` schema; enforcement requires `exit 2`, and config is a `matcher` string plus a `hooks` array. repo-hygiene gains the audit-side check that flags exit-1 enforcement as non-blocking.
- **Session reports and delegation hardening (cc-design).** A computed session-report schema, spec-digest-bound briefs, capped Builder→Refuter loops, and `status: blocked` as distinct from an empty findings list.
- **Per-model fallback semantics.** Server-side fallback is now per model — Haiku 5.5 has none; Sonnet 5.5 retries only `cyber` / `frontier_llm` declines on Sonnet 5 — and refusal billing changed 2026-09-24.

Every Skill moves to 5.0.0; tier structure (Model-compatible / Sonnet-graceful / High-effort recommended) is unchanged at 13 / 7 / 7. See the [Model Compatibility](https://github.com/drayline/rootnode-skills#model-compatibility) section of the README for effort defaults by model and surface, fallback semantics, and per-tier definitions.

## Download

**All Skills, one download:** grab `rootnode-catalog-v5.0.zip` from the Assets below. It bundles all 29 packaged Skill files (24 chat-side `-cp` flat zips for Claude Projects, 5 Claude Code `-cc` wrapper zips). Unzip it, then upload or install the Skills you want.

**Individual Skills:** use the links under Skills below — each Skill's own release carries its packaged zip.

GitHub auto-attaches "Source code (zip / tar.gz)" to every release; those are the raw repository, not the packaged Skills. Ignore them and use the bundle or the per-Skill zips.

## Skills

**Build (3)**
- [rootnode-prompt-compilation](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-prompt-compilation/v5.0)
- [rootnode-skill-builder](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-skill-builder/v5.0)
- [rootnode-cc-design](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-cc-design/v5.0)

**Diagnose (5)**
- [rootnode-project-audit](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-project-audit/v5.0)
- [rootnode-global-audit](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-global-audit/v5.0)
- [rootnode-anti-pattern-detection](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-anti-pattern-detection/v5.0)
- [rootnode-prompt-validation](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-prompt-validation/v5.0)
- [rootnode-repo-hygiene](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-repo-hygiene/v5.0)

**Optimize (3)**
- [rootnode-behavioral-tuning](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-behavioral-tuning/v5.0)
- [rootnode-memory-optimization](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-memory-optimization/v5.0)
- [rootnode-context-budget](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-context-budget/v5.0)

**Cross-Layer (1)**
- [rootnode-full-stack-audit](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-full-stack-audit/v5.0)

**Bridge (2)**
- [rootnode-project-brief](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-project-brief/v5.0)
- [rootnode-session-handoff](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-session-handoff/v5.0)

**Cross-Boundary (2)**
- [rootnode-handoff-trigger-check](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-handoff-trigger-check/v5.0)
- [rootnode-profile-builder](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-profile-builder/v5.0)

**Runtime (CC, 2)**
- [rootnode-critic-gate](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-critic-gate/v5.0)
- [rootnode-mode-router](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-mode-router/v5.0)

**Block Libraries (4)**
- [rootnode-block-selection](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-block-selection/v5.0)
- [rootnode-identity-blocks](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-identity-blocks/v5.0)
- [rootnode-reasoning-blocks](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-reasoning-blocks/v5.0)
- [rootnode-output-blocks](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-output-blocks/v5.0)

**Domain Packs (5)**
- [rootnode-domain-business-strategy](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-domain-business-strategy/v5.0)
- [rootnode-domain-software-engineering](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-domain-software-engineering/v5.0)
- [rootnode-domain-content-communications](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-domain-content-communications/v5.0)
- [rootnode-domain-research-analysis](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-domain-research-analysis/v5.0)
- [rootnode-domain-agentic-context](https://github.com/drayline/rootnode-skills/releases/tag/rootnode-domain-agentic-context/v5.0)

## Architecture

Two surfaces, one mental model. Chat-side Claude Projects and Claude Code execution share a unified principle layer covering placement discipline, decomposition by mechanism, behavioral countermeasures, cross-Skill composition contracts, verification-instruction discipline (D4), and landscape-volatility discipline (D8).

## Site

[rootnode.design](https://rootnode.design/)
