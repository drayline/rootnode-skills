Profile-driven gate that evaluates work against configured thresholds before merge or handoff. Reads a critic profile produced by `profile-builder` and returns a structured verdict with rationale. v5.0: a reviewer that could not inspect returns `status: blocked`, never an empty findings list; advisor-tool pairing rule (advisor at least as capable as the executor).

**Surface:** Claude Code • **Tier:** Sonnet-graceful (T2)

### Install

Download `rootnode-critic-gate-cc.zip` below, extract it into `~/.claude/skills/` (user-level — available across every repo) or `.claude/skills/` (per-repo). The extracted folder name matches the Skill name.

### v5.0 Catalog Release

Part of the [root.node v5.0 catalog](https://github.com/drayline/rootnode-skills) — 27 Skills shipped simultaneously with the 5.5-generation Claude alignment. Calibrated dual-primary for Opus 5.5 + Sonnet 5.5 (Opus 5.5 is the Claude Code default; effort defaults to `medium` on the 5.5 models in Claude Code); integrated-aware for Fable 5.1; subagent-aware for Haiku 5.5; fallback-graceful for Opus 5 / Sonnet 5; legacy-graceful for Sonnet 4.6. See the [Model Compatibility](https://github.com/drayline/rootnode-skills#model-compatibility) section of the README for effort defaults by model and surface, fallback semantics, and per-tier definitions.
