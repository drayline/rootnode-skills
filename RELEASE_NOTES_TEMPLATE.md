# Release Notes Template — root.node Skills v3.0

Source of truth for the 27 individual GitHub release notes blocks during the v3.0 catalog ship. Three template variants by install surface; per-Skill data populates the variants at release time.

**Tag pattern:** `<skill-name>/v3.0`
**Title pattern:** `<skill-name> v3.0`
**Notes:** assembled from variant + per-Skill data table below

---

## Variant A — Chat-Project only (22 Skills)

```markdown
{DESCRIPTION}

**Surface:** Chat-Project • **Tier:** {TIER_LABEL}

### Install

Download `{SKILL_NAME}-cp.zip` below, then upload it in **Settings → Capabilities → Skills**. No unzipping required.

### v3.0 Catalog Release

Part of the [root.node v3.0 catalog](https://github.com/drayline/rootnode-skills) — 27 Skills shipped simultaneously with normalized frontmatter and the three-tier model compatibility model codified. Calibrated against Claude Opus 4.7.
```

---

## Variant B — Claude Code only (3 Skills)

```markdown
{DESCRIPTION}

**Surface:** Claude Code • **Tier:** {TIER_LABEL}

### Install

Download `{SKILL_NAME}-cc.zip` below, extract it into `~/.claude/skills/` (user-level — available across every repo) or `.claude/skills/` (per-repo). The extracted folder name matches the Skill name.

### v3.0 Catalog Release

Part of the [root.node v3.0 catalog](https://github.com/drayline/rootnode-skills) — 27 Skills shipped simultaneously with normalized frontmatter and the three-tier model compatibility model codified. Calibrated against Claude Opus 4.7.
```

---

## Variant C — Dual-surface (2 Skills)

```markdown
{DESCRIPTION}

**Surface:** Chat-Project + Claude Code • **Tier:** {TIER_LABEL}

### Install

**Chat-Project:** Download `{SKILL_NAME}-cp.zip` below, then upload it in **Settings → Capabilities → Skills**. No unzipping required.

**Claude Code:** Download `{SKILL_NAME}-cc.zip` below, extract it into `~/.claude/skills/` (user-level) or `.claude/skills/` (per-repo). The extracted folder name matches the Skill name.

### v3.0 Catalog Release

Part of the [root.node v3.0 catalog](https://github.com/drayline/rootnode-skills) — 27 Skills shipped simultaneously with normalized frontmatter and the three-tier model compatibility model codified. Calibrated against Claude Opus 4.7.
```

---

## Tier label mapping

| Tier | Label |
|---|---|
| T1 | `Model-compatible (T1)` |
| T2 | `Sonnet-graceful (T2)` |
| T3 | `Opus-recommended (T3)` |

---

## Per-Skill Data Table

Substitution data for each of the 27 releases. `Variant` selects template; `Description` populates `{DESCRIPTION}`; `Tier` populates `{TIER_LABEL}` via the mapping above.

### Variant A — Chat-Project only (22)

| Skill | Tier | Description |
|---|---|---|
| `rootnode-prompt-compilation` | T3 | Four-stage pipeline (Parse, Select, Construct, Validate) that builds complete prompts and scaffolds entire Claude Projects — Custom Instructions, knowledge file architecture, and global layer advisory. |
| `rootnode-prompt-validation` | T2 | Six-dimension Prompt Scorecard for evaluating prompts. Maps each weakness to a structural fix. |
| `rootnode-project-audit` | T3 | Scores a Project on six dimensions with anchored 1-5 rubrics. Finds what's broken and prescribes targeted fixes. |
| `rootnode-project-brief` | T1 | Generates a structured Project Brief — extracts goals, architecture, knowledge file inventory, Custom Instructions summary, Memory contents, current state, and key decisions from a Claude Project. |
| `rootnode-anti-pattern-detection` | T2 | Detects seven structural patterns that cause ignored instructions and degraded output. |
| `rootnode-behavioral-tuning` | T2 | Diagnoses ten Claude behavioral tendencies (verbosity, hedging, agreeableness, fabricated precision, and others) with countermeasure templates ready to deploy. |
| `rootnode-memory-optimization` | T2 | Rebalances content across Memory, Custom Instructions, knowledge files, and User Preferences. Produces edit prescriptions and trimming recommendations. |
| `rootnode-context-budget` | T3 | Full context budget analysis: two-pool architecture, per-file evaluation across six dimensions, content routing, growth trajectory assessment, retrieval quality audit, and phased optimization. |
| `rootnode-global-audit` | T3 | Audits all five global layers (Preferences, Styles, Memory, Skills, Connectors) using a six-dimension scorecard. Detects cross-layer failure modes. |
| `rootnode-full-stack-audit` | T3 | Runs Project audit + Global audit + Cross-Layer Alignment Check in a single pass. The most comprehensive diagnostic in the catalog. |
| `rootnode-session-handoff` | T1 | Produces structured XML session continuation documents. Captures active work streams, decisions with rationale, and open items into an ingestion-optimized handoff file. |
| `rootnode-handoff-trigger-check` | T1 | Evaluates whether work-in-design is ready to hand off from chat to autonomous execution. Runs a 7-condition gate and returns a structured JSON verdict. |
| `rootnode-profile-builder` | T1 | Conversational profile builder. Reads a target JSON Schema, conducts a progressive-depth interview, validates answers, and writes the resulting profile to a destination path. |
| `rootnode-identity-blocks` | T1 | 8 identity approaches (Strategic Advisor, Technical Architect, Research Synthesist, and more). |
| `rootnode-reasoning-blocks` | T1 | 18 reasoning variants across 6 categories (Analytical, Strategic, Creative, Technical, Research, Comparative). |
| `rootnode-output-blocks` | T1 | 10 output format specifications (Executive Brief, Technical Design, Decision Matrix, and more). |
| `rootnode-block-selection` | T2 | Decision trees for choosing the right identity, reasoning, and output approach for any task type. |
| `rootnode-domain-software-engineering` | T1 | Specialized methodology for system design, code review, incident response, security analysis, and API design. |
| `rootnode-domain-business-strategy` | T1 | Specialized methodology for consulting, competitive analysis, corporate strategy, and M&A. |
| `rootnode-domain-content-communications` | T1 | Specialized methodology for writing, editing, content strategy, copywriting, and persuasion. |
| `rootnode-domain-research-analysis` | T1 | Specialized methodology for data analysis, policy research, evidence synthesis, and systematic review. |
| `rootnode-domain-agentic-context` | T1 | Specialized methodology for AI agent design, tool interfaces, context architecture, and multi-agent coordination. |

### Variant B — Claude Code only (3)

| Skill | Tier | Description |
|---|---|---|
| `rootnode-critic-gate` | T2 | Profile-driven gate that evaluates work against configured thresholds before merge or handoff. Reads a critic profile produced by `profile-builder` and returns a structured verdict with rationale. |
| `rootnode-mode-router` | T1 | Profile-driven router that reads a mode configuration and routes work by strictness, scope, or context. The runtime counterpart to chat-side `block-selection`. |
| `rootnode-repo-hygiene` | T3 | 14-category sweep + 7-layer leak check + anti-pattern detection across an existing Claude Code deployment. Produces `HYGIENE_REPORT.md` consumable by `cc-design` REMEDIATE mode. |

### Variant C — Dual-surface (2)

| Skill | Tier | Description |
|---|---|---|
| `rootnode-skill-builder` | T2 | Converts design specifications into deployment-ready Skill packages (SKILL.md + references/ + scripts/ + agents/). Six workflows: build, iterate, optimize, compare, review, revise. |
| `rootnode-cc-design` | T3 | Designs Claude Code environments. Five modes: design (new deployments), evolve (updates from friction), research (evaluate CC tools/patterns), template (reusable artifacts), remediate (consume hygiene findings → produce + execute plan). |

---

## Example assembled blocks

### Example: Variant A — `rootnode-prompt-compilation`

```markdown
Four-stage pipeline (Parse, Select, Construct, Validate) that builds complete prompts and scaffolds entire Claude Projects — Custom Instructions, knowledge file architecture, and global layer advisory.

**Surface:** Chat-Project • **Tier:** Opus-recommended (T3)

### Install

Download `rootnode-prompt-compilation-cp.zip` below, then upload it in **Settings → Capabilities → Skills**. No unzipping required.

### v3.0 Catalog Release

Part of the [root.node v3.0 catalog](https://github.com/drayline/rootnode-skills) — 27 Skills shipped simultaneously with normalized frontmatter and the three-tier model compatibility model codified. Calibrated against Claude Opus 4.7.
```

### Example: Variant B — `rootnode-repo-hygiene`

```markdown
14-category sweep + 7-layer leak check + anti-pattern detection across an existing Claude Code deployment. Produces `HYGIENE_REPORT.md` consumable by `cc-design` REMEDIATE mode.

**Surface:** Claude Code • **Tier:** Opus-recommended (T3)

### Install

Download `rootnode-repo-hygiene-cc.zip` below, extract it into `~/.claude/skills/` (user-level — available across every repo) or `.claude/skills/` (per-repo). The extracted folder name matches the Skill name.

### v3.0 Catalog Release

Part of the [root.node v3.0 catalog](https://github.com/drayline/rootnode-skills) — 27 Skills shipped simultaneously with normalized frontmatter and the three-tier model compatibility model codified. Calibrated against Claude Opus 4.7.
```

### Example: Variant C — `rootnode-skill-builder`

```markdown
Converts design specifications into deployment-ready Skill packages (SKILL.md + references/ + scripts/ + agents/). Six workflows: build, iterate, optimize, compare, review, revise.

**Surface:** Chat-Project + Claude Code • **Tier:** Sonnet-graceful (T2)

### Install

**Chat-Project:** Download `rootnode-skill-builder-cp.zip` below, then upload it in **Settings → Capabilities → Skills**. No unzipping required.

**Claude Code:** Download `rootnode-skill-builder-cc.zip` below, extract it into `~/.claude/skills/` (user-level) or `.claude/skills/` (per-repo). The extracted folder name matches the Skill name.

### v3.0 Catalog Release

Part of the [root.node v3.0 catalog](https://github.com/drayline/rootnode-skills) — 27 Skills shipped simultaneously with normalized frontmatter and the three-tier model compatibility model codified. Calibrated against Claude Opus 4.7.
```

---

## CC consumption pattern

The release CC prompt will read this template document and assemble per-Skill release notes via the following pattern:

1. For each Skill in the data table, select the matching variant.
2. Substitute `{SKILL_NAME}`, `{DESCRIPTION}`, and `{TIER_LABEL}` (tier label resolved via the mapping table).
3. Write the assembled block to `release-notes/<skill-name>-v3.0.md`.
4. Run `gh release create <skill-name>/v3.0 --title "<skill-name> v3.0" --notes-file release-notes/<skill-name>-v3.0.md <zip-files>`.

For the two existing releases (`skill-builder/v3.0` already exists with flat zip; `cc-design/v2.1` to be deleted and recut at v3.0), the CC prompt handles the transitions before the new release blast.

---

## Counts verification

- **Variant A (Chat-Project only):** 22 Skills ✓
- **Variant B (Claude Code only):** 3 Skills ✓
- **Variant C (Dual-surface):** 2 Skills ✓
- **Total:** 27 ✓

Zip artifacts at release time:
- 22 × `-cp.zip` (Variant A)
- 3 × `-cc.zip` (Variant B)
- 2 × `-cp.zip` + 2 × `-cc.zip` = 4 zips (Variant C)
- **Total:** 29 zip artifacts across 27 releases
