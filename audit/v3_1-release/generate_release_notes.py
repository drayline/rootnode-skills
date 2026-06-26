#!/usr/bin/env python3
"""Assemble v3.1 release notes from RELEASE_NOTES_TEMPLATE.md data table.

Parameterizes the v3.0 template to v3.1 + Opus 4.8 calibration line per
the v3.1 release session prompt. Per-Skill tier labels preserved as-is
(tier-matrix regen is v3.2, test-gated). Writes one file per Skill into
release-notes/<skill>-v3.1.md.

Counts: 22 Variant-A (cp) + 3 Variant-B (cc) + 2 Variant-C (dual) = 27.
"""
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = REPO_ROOT / "release-notes"

TIER_LABEL = {
    "T1": "Model-compatible (T1)",
    "T2": "Sonnet-graceful (T2)",
    "T3": "Opus-recommended (T3)",
}

# Per-Skill data from RELEASE_NOTES_TEMPLATE.md, exact text preserved.
VARIANT_A = [
    ("rootnode-prompt-compilation", "T3",
     "Four-stage pipeline (Parse, Select, Construct, Validate) that builds complete prompts and scaffolds entire Claude Projects — Custom Instructions, knowledge file architecture, and global layer advisory."),
    ("rootnode-prompt-validation", "T2",
     "Six-dimension Prompt Scorecard for evaluating prompts. Maps each weakness to a structural fix."),
    ("rootnode-project-audit", "T3",
     "Scores a Project on six dimensions with anchored 1-5 rubrics. Finds what's broken and prescribes targeted fixes."),
    ("rootnode-project-brief", "T1",
     "Generates a structured Project Brief — extracts goals, architecture, knowledge file inventory, Custom Instructions summary, Memory contents, current state, and key decisions from a Claude Project."),
    ("rootnode-anti-pattern-detection", "T2",
     "Detects seven structural patterns that cause ignored instructions and degraded output."),
    ("rootnode-behavioral-tuning", "T2",
     "Diagnoses ten Claude behavioral tendencies (verbosity, hedging, agreeableness, fabricated precision, and others) with countermeasure templates ready to deploy."),
    ("rootnode-memory-optimization", "T2",
     "Rebalances content across Memory, Custom Instructions, knowledge files, and User Preferences. Produces edit prescriptions and trimming recommendations."),
    ("rootnode-context-budget", "T3",
     "Full context budget analysis: two-pool architecture, per-file evaluation across six dimensions, content routing, growth trajectory assessment, retrieval quality audit, and phased optimization."),
    ("rootnode-global-audit", "T3",
     "Audits all five global layers (Preferences, Styles, Memory, Skills, Connectors) using a six-dimension scorecard. Detects cross-layer failure modes."),
    ("rootnode-full-stack-audit", "T3",
     "Runs Project audit + Global audit + Cross-Layer Alignment Check in a single pass. The most comprehensive diagnostic in the catalog."),
    ("rootnode-session-handoff", "T1",
     "Produces structured XML session continuation documents. Captures active work streams, decisions with rationale, and open items into an ingestion-optimized handoff file."),
    ("rootnode-handoff-trigger-check", "T1",
     "Evaluates whether work-in-design is ready to hand off from chat to autonomous execution. Runs a 7-condition gate and returns a structured JSON verdict."),
    ("rootnode-profile-builder", "T1",
     "Conversational profile builder. Reads a target JSON Schema, conducts a progressive-depth interview, validates answers, and writes the resulting profile to a destination path."),
    ("rootnode-identity-blocks", "T1",
     "8 identity approaches (Strategic Advisor, Technical Architect, Research Synthesist, and more)."),
    ("rootnode-reasoning-blocks", "T1",
     "18 reasoning variants across 6 categories (Analytical, Strategic, Creative, Technical, Research, Comparative)."),
    ("rootnode-output-blocks", "T1",
     "10 output format specifications (Executive Brief, Technical Design, Decision Matrix, and more)."),
    ("rootnode-block-selection", "T2",
     "Decision trees for choosing the right identity, reasoning, and output approach for any task type."),
    ("rootnode-domain-software-engineering", "T1",
     "Specialized methodology for system design, code review, incident response, security analysis, and API design."),
    ("rootnode-domain-business-strategy", "T1",
     "Specialized methodology for consulting, competitive analysis, corporate strategy, and M&A."),
    ("rootnode-domain-content-communications", "T1",
     "Specialized methodology for writing, editing, content strategy, copywriting, and persuasion."),
    ("rootnode-domain-research-analysis", "T1",
     "Specialized methodology for data analysis, policy research, evidence synthesis, and systematic review."),
    ("rootnode-domain-agentic-context", "T1",
     "Specialized methodology for AI agent design, tool interfaces, context architecture, and multi-agent coordination."),
]

VARIANT_B = [
    ("rootnode-critic-gate", "T2",
     "Profile-driven gate that evaluates work against configured thresholds before merge or handoff. Reads a critic profile produced by `profile-builder` and returns a structured verdict with rationale."),
    ("rootnode-mode-router", "T1",
     "Profile-driven router that reads a mode configuration and routes work by strictness, scope, or context. The runtime counterpart to chat-side `block-selection`."),
    ("rootnode-repo-hygiene", "T3",
     "14-category sweep + 7-layer leak check + anti-pattern detection across an existing Claude Code deployment. Produces `HYGIENE_REPORT.md` consumable by `cc-design` REMEDIATE mode."),
]

VARIANT_C = [
    ("rootnode-skill-builder", "T2",
     "Converts design specifications into deployment-ready Skill packages (SKILL.md + references/ + scripts/ + agents/). Six workflows: build, iterate, optimize, compare, review, revise."),
    ("rootnode-cc-design", "T3",
     "Designs Claude Code environments. Five modes: design (new deployments), evolve (updates from friction), research (evaluate CC tools/patterns), template (reusable artifacts), remediate (consume hygiene findings → produce + execute plan)."),
]

CATALOG_RELEASE = (
    "Part of the [root.node v3.1 catalog](https://github.com/drayline/rootnode-skills) — "
    "27 Skills shipped simultaneously with normalized frontmatter and the three-tier "
    "model compatibility model codified. Calibrated against Claude Opus 4.8."
)


def variant_a(name, tier, desc):
    return f"""{desc}

**Surface:** Chat-Project • **Tier:** {TIER_LABEL[tier]}

### Install

Download `{name}-cp.zip` below, then upload it in **Settings → Capabilities → Skills**. No unzipping required.

### v3.1 Catalog Release

{CATALOG_RELEASE}
"""


def variant_b(name, tier, desc):
    return f"""{desc}

**Surface:** Claude Code • **Tier:** {TIER_LABEL[tier]}

### Install

Download `{name}-cc.zip` below, extract it into `~/.claude/skills/` (user-level — available across every repo) or `.claude/skills/` (per-repo). The extracted folder name matches the Skill name.

### v3.1 Catalog Release

{CATALOG_RELEASE}
"""


def variant_c(name, tier, desc):
    return f"""{desc}

**Surface:** Chat-Project + Claude Code • **Tier:** {TIER_LABEL[tier]}

### Install

**Chat-Project:** Download `{name}-cp.zip` below, then upload it in **Settings → Capabilities → Skills**. No unzipping required.

**Claude Code:** Download `{name}-cc.zip` below, extract it into `~/.claude/skills/` (user-level) or `.claude/skills/` (per-repo). The extracted folder name matches the Skill name.

### v3.1 Catalog Release

{CATALOG_RELEASE}
"""


def main():
    OUT_DIR.mkdir(exist_ok=True)
    counts = {"A": 0, "B": 0, "C": 0}
    for entry in VARIANT_A:
        name, tier, desc = entry
        (OUT_DIR / f"{name}-v3.1.md").write_text(variant_a(name, tier, desc), encoding="utf-8")
        counts["A"] += 1
    for entry in VARIANT_B:
        name, tier, desc = entry
        (OUT_DIR / f"{name}-v3.1.md").write_text(variant_b(name, tier, desc), encoding="utf-8")
        counts["B"] += 1
    for entry in VARIANT_C:
        name, tier, desc = entry
        (OUT_DIR / f"{name}-v3.1.md").write_text(variant_c(name, tier, desc), encoding="utf-8")
        counts["C"] += 1
    total = sum(counts.values())
    print(f"Wrote: Variant A={counts['A']}, B={counts['B']}, C={counts['C']}, total={total}")
    assert counts["A"] == 22, f"Variant A expected 22, got {counts['A']}"
    assert counts["B"] == 3, f"Variant B expected 3, got {counts['B']}"
    assert counts["C"] == 2, f"Variant C expected 2, got {counts['C']}"
    assert total == 27, f"Total expected 27, got {total}"
    print("Counts ✓")


if __name__ == "__main__":
    main()
