Converts design specifications into deployment-ready Skill packages (SKILL.md + references/ + scripts/ + agents/). Six workflows: build, iterate, optimize, compare, review, revise. v5.0: D9a graders run on Opus 5.5 or Sonnet 5.5 (Opus 5 / Sonnet 5 valid fallback); D9c cites the 15-tendency taxonomy (fixes a v4.0 propagation miss that still said 10); Haiku 5.5 is a valid subject model, not a grader.

**Surface:** Chat-Project + Claude Code • **Tier:** Sonnet-graceful (T2)

### Install

**Chat-Project:** Download `rootnode-skill-builder-cp.zip` below, then upload it in **Settings → Capabilities → Skills**. No unzipping required.

**Claude Code:** Download `rootnode-skill-builder-cc.zip` below, extract it into `~/.claude/skills/` (user-level) or `.claude/skills/` (per-repo). The extracted folder name matches the Skill name.

### v5.0 Catalog Release

Part of the [root.node v5.0 catalog](https://github.com/drayline/rootnode-skills) — 27 Skills shipped simultaneously with the 5.5-generation Claude alignment. Calibrated dual-primary for Opus 5.5 + Sonnet 5.5 (Opus 5.5 is the Claude Code default; effort defaults to `medium` on the 5.5 models in Claude Code); integrated-aware for Fable 5.1; subagent-aware for Haiku 5.5; fallback-graceful for Opus 5 / Sonnet 5; legacy-graceful for Sonnet 4.6. See the [Model Compatibility](https://github.com/drayline/rootnode-skills#model-compatibility) section of the README for effort defaults by model and surface, fallback semantics, and per-tier definitions.
