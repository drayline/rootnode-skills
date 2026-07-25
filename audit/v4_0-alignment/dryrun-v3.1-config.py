# Dry-run config for generate_release_notes.py — reproduces v3.1 output.
# Values here mirror audit/v3_1-release/generate_release_notes.py verbatim,
# used only for the verification pass documented in v4.0 Phase 3.

VERSION = "3.1"

TIER_LABEL = {
    "T1": "Model-compatible (T1)",
    "T2": "Sonnet-graceful (T2)",
    "T3": "Opus-recommended (T3)",
}

CATALOG_RELEASE = (
    "Part of the [root.node v3.1 catalog](https://github.com/drayline/rootnode-skills) — "
    "27 Skills shipped simultaneously with normalized frontmatter and the three-tier "
    "model compatibility model codified. Calibrated against Claude Opus 4.8."
)

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

EXPECTED_COUNTS = {"A": 22, "B": 3, "C": 2, "total": 27}
