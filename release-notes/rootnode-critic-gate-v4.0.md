Profile-driven gate that evaluates work against configured thresholds before merge or handoff. Reads a critic profile produced by `profile-builder` and returns a structured verdict with rationale.

**Surface:** Claude Code • **Tier:** Sonnet-graceful (T2)

### Install

Download `rootnode-critic-gate-cc.zip` below, extract it into `~/.claude/skills/` (user-level — available across every repo) or `.claude/skills/` (per-repo). The extracted folder name matches the Skill name.

### v4.0 Catalog Release

Part of the [root.node v4.0 catalog](https://github.com/drayline/rootnode-skills) — 27 Skills shipped simultaneously with the 5-generation Claude alignment. Calibrated dual-primary for Opus 5 + Sonnet 5 (both default to `high` effort on Claude API and Claude Code); integrated-aware for Fable 5; fallback-graceful for Opus 4.8; legacy-graceful for Sonnet 4.6; graceful-with-extended-thinking for Haiku 4.5. See the [Model Compatibility](https://github.com/drayline/rootnode-skills#model-compatibility) section of the README for full effort ladder, fallback semantics, and per-tier definitions.
