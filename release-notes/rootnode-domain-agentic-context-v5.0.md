Specialized methodology for AI agent design, tool interfaces, context architecture, and multi-agent coordination. v5.0 rebuilds refusal and fallback semantics per model (Haiku 5.5 has no server-side fallback) and adds harness rules: never put user text in a `tool_result`, forced `tool_choice` removed, progress updates arrive in `thinking` blocks, advisory time budgets.

**Surface:** Chat-Project • **Tier:** Model-compatible (T1)

### Install

Download `rootnode-domain-agentic-context-cp.zip` below, then upload it in **Settings → Capabilities → Skills**. No unzipping required.

### v5.0 Catalog Release

Part of the [root.node v5.0 catalog](https://github.com/drayline/rootnode-skills) — 27 Skills shipped simultaneously with the 5.5-generation Claude alignment. Calibrated dual-primary for Opus 5.5 + Sonnet 5.5 (Opus 5.5 is the Claude Code default; effort defaults to `medium` on the 5.5 models in Claude Code); integrated-aware for Fable 5.1; subagent-aware for Haiku 5.5; fallback-graceful for Opus 5 / Sonnet 5; legacy-graceful for Sonnet 4.6. See the [Model Compatibility](https://github.com/drayline/rootnode-skills#model-compatibility) section of the README for effort defaults by model and surface, fallback semantics, and per-tier definitions.
