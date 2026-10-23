Four-stage pipeline (Parse, Select, Construct, Validate) that builds complete prompts and scaffolds entire Claude Projects. v5.0 adds a reasoning-extraction check to Stage 4 Validate — instructions that ask the model to reproduce its internal reasoning in the response can be declined with `stop_reason: "refusal"` on every current model — and drops thinking-disabled mitigations from Project Mode scaffolds (thinking cannot be disabled on the primary tier).

**Surface:** Chat-Project • **Tier:** High-effort recommended (T3)

### Install

Download `rootnode-prompt-compilation-cp.zip` below, then upload it in **Settings → Capabilities → Skills**. No unzipping required.

### v5.0 Catalog Release

Part of the [root.node v5.0 catalog](https://github.com/drayline/rootnode-skills) — 27 Skills shipped simultaneously with the 5.5-generation Claude alignment. Calibrated dual-primary for Opus 5.5 + Sonnet 5.5 (Opus 5.5 is the Claude Code default; effort defaults to `medium` on the 5.5 models in Claude Code); integrated-aware for Fable 5.1; subagent-aware for Haiku 5.5; fallback-graceful for Opus 5 / Sonnet 5; legacy-graceful for Sonnet 4.6. See the [Model Compatibility](https://github.com/drayline/rootnode-skills#model-compatibility) section of the README for effort defaults by model and surface, fallback semantics, and per-tier definitions.
