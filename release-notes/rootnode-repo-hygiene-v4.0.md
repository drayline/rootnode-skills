14-category sweep + 7-layer leak check + anti-pattern detection across an existing Claude Code deployment. Produces `HYGIENE_REPORT.md` consumable by `cc-design` REMEDIATE mode.

**Surface:** Claude Code • **Tier:** High-effort recommended (T3)

### Install

Download `rootnode-repo-hygiene-cc.zip` below, extract it into `~/.claude/skills/` (user-level — available across every repo) or `.claude/skills/` (per-repo). The extracted folder name matches the Skill name.

### v4.0 Catalog Release

Part of the [root.node v4.0 catalog](https://github.com/drayline/rootnode-skills) — 27 Skills shipped simultaneously with the 5-generation Claude alignment. Calibrated dual-primary for Opus 5 + Sonnet 5 (both default to `high` effort on Claude API and Claude Code); integrated-aware for Fable 5; fallback-graceful for Opus 4.8; legacy-graceful for Sonnet 4.6; graceful-with-extended-thinking for Haiku 4.5. See the [Model Compatibility](https://github.com/drayline/rootnode-skills#model-compatibility) section of the README for full effort ladder, fallback semantics, and per-tier definitions.
