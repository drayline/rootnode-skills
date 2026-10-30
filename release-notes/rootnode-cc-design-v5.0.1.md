Designs Claude Code environments. Five modes: design (new deployments), evolve (updates from friction), research (evaluate CC tools/patterns), template (reusable artifacts), remediate (consume hygiene findings → produce + execute plan). v5.0.1: Stop-hook bounds are scoped to the stop chain, with a no-progress cap and a chain-total cap, and the guidance pairs them with Claude Code's own continuation cap; the migration-guard example catches more delete forms (`find -delete`, globs, PowerShell) and states what a text-matching guard cannot see; autonomous prompt templates gain a resume line; the prompt-design patterns add shell lessons from this patch's build (git pathspecs, naming the Python interpreter, worker allow-lists); cross-references and counts are corrected.

**Surface:** Chat-Project + Claude Code • **Tier:** High-effort recommended (T3)

### Install

**Chat-Project:** Download `rootnode-cc-design-cp.zip` below, then upload it in **Settings → Capabilities → Skills**. No unzipping required.

**Claude Code:** Download `rootnode-cc-design-cc.zip` below, extract it into `~/.claude/skills/` (user-level) or `.claude/skills/` (per-repo). The extracted folder name matches the Skill name.

### v5.0.1 Catalog Release

Part of the [root.node v5.0.1 patch](https://github.com/drayline/rootnode-skills/releases/tag/catalog-v5.0.1) — 12 of the 27 Skills patched after the v5.0 behavioral validation of cc-design; the other 15 stay at v5.0. Calibration is unchanged from v5.0: dual-primary for Opus 5.5 + Sonnet 5.5. See the [Model Compatibility](https://github.com/drayline/rootnode-skills#model-compatibility) section of the README for effort defaults by model and surface, fallback semantics, and per-tier definitions.
