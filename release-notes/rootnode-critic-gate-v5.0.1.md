Profile-driven gate that evaluates work against configured thresholds before merge or handoff. Reads a critic profile produced by `profile-builder` and returns a structured verdict with rationale. v5.0.1: the output JSON carries `"status": "complete" | "blocked"`, with a `blocked_reason` when blocked (an additive field), and references to the readiness gate use `rootnode-handoff-trigger-check`.

**Surface:** Claude Code • **Tier:** Sonnet-graceful (T2)

### Install

Download `rootnode-critic-gate-cc.zip` below, extract it into `~/.claude/skills/` (user-level — available across every repo) or `.claude/skills/` (per-repo). The extracted folder name matches the Skill name.

### v5.0.1 Catalog Release

Part of the [root.node v5.0.1 patch](https://github.com/drayline/rootnode-skills/releases/tag/catalog-v5.0.1) — 12 of the 27 Skills patched after the v5.0 behavioral validation of cc-design; the other 15 stay at v5.0. Calibration is unchanged from v5.0: dual-primary for Opus 5.5 + Sonnet 5.5. See the [Model Compatibility](https://github.com/drayline/rootnode-skills#model-compatibility) section of the README for effort defaults by model and surface, fallback semantics, and per-tier definitions.
