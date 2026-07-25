Designs Claude Code environments. Five modes: design (new deployments), evolve (updates from friction), research (evaluate CC tools/patterns), template (reusable artifacts), remediate (consume hygiene findings → produce + execute plan). v4.0 adds subagent-delegation caps for Opus 5 CC deployments and the D4 verification-topology distinction (independent review of a different agent's work vs. self-directed re-checking).

**Surface:** Chat-Project + Claude Code • **Tier:** High-effort recommended (T3)

### Install

**Chat-Project:** Download `rootnode-cc-design-cp.zip` below, then upload it in **Settings → Capabilities → Skills**. No unzipping required.

**Claude Code:** Download `rootnode-cc-design-cc.zip` below, extract it into `~/.claude/skills/` (user-level) or `.claude/skills/` (per-repo). The extracted folder name matches the Skill name.

### v4.0 Catalog Release

Part of the [root.node v4.0 catalog](https://github.com/drayline/rootnode-skills) — 27 Skills shipped simultaneously with the 5-generation Claude alignment. Calibrated dual-primary for Opus 5 + Sonnet 5 (both default to `high` effort on Claude API and Claude Code); integrated-aware for Fable 5; fallback-graceful for Opus 4.8; legacy-graceful for Sonnet 4.6; graceful-with-extended-thinking for Haiku 4.5. See the [Model Compatibility](https://github.com/drayline/rootnode-skills#model-compatibility) section of the README for full effort ladder, fallback semantics, and per-tier definitions.
