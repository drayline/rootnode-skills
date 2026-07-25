Four-stage pipeline (Parse, Select, Construct, Validate) that builds complete prompts and scaffolds entire Claude Projects. In v4.0, Project Mode delivers scaffold artifacts as separate files on disk (Custom Instructions + each knowledge file) rather than inline code blocks — the D5 contract change simplifies the upload workflow.

**Surface:** Chat-Project • **Tier:** High-effort recommended (T3)

### Install

Download `rootnode-prompt-compilation-cp.zip` below, then upload it in **Settings → Capabilities → Skills**. No unzipping required.

### v4.0 Catalog Release

Part of the [root.node v4.0 catalog](https://github.com/drayline/rootnode-skills) — 27 Skills shipped simultaneously with the 5-generation Claude alignment. Calibrated dual-primary for Opus 5 + Sonnet 5 (both default to `high` effort on Claude API and Claude Code); integrated-aware for Fable 5; fallback-graceful for Opus 4.8; legacy-graceful for Sonnet 4.6; graceful-with-extended-thinking for Haiku 4.5. See the [Model Compatibility](https://github.com/drayline/rootnode-skills#model-compatibility) section of the README for full effort ladder, fallback semantics, and per-tier definitions.
