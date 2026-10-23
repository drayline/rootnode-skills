Evaluates whether work-in-design is ready to hand off from chat to autonomous execution. Runs a 7-condition gate and returns a structured JSON verdict. v5.0 updates condition 7 for 1M on all four current models, the `medium` Claude Code effort default, the Haiku 5.5 tokenizer, and Haiku 5.5's >100K-prompt price band.

**Surface:** Chat-Project • **Tier:** Model-compatible (T1)

### Install

Download `rootnode-handoff-trigger-check-cp.zip` below, then upload it in **Settings → Capabilities → Skills**. No unzipping required.

### v5.0 Catalog Release

Part of the [root.node v5.0 catalog](https://github.com/drayline/rootnode-skills) — 27 Skills shipped simultaneously with the 5.5-generation Claude alignment. Calibrated dual-primary for Opus 5.5 + Sonnet 5.5 (Opus 5.5 is the Claude Code default; effort defaults to `medium` on the 5.5 models in Claude Code); integrated-aware for Fable 5.1; subagent-aware for Haiku 5.5; fallback-graceful for Opus 5 / Sonnet 5; legacy-graceful for Sonnet 4.6. See the [Model Compatibility](https://github.com/drayline/rootnode-skills#model-compatibility) section of the README for effort defaults by model and surface, fallback semantics, and per-tier definitions.
