# v4.0 config for generate_release_notes.py.
# Per-cycle artifact — lives under audit/v4_0-alignment/ per the audit/README.md
# convention (standing tooling at root; cycle configs under audit/v<N>-*/).

VERSION = "4.0"

TIER_LABEL = {
    "T1": "Model-compatible (T1)",
    "T2": "Sonnet-graceful (T2)",
    "T3": "High-effort recommended (T3)",  # D2: retired "Opus-recommended" label
}

CATALOG_RELEASE = (
    "Part of the [root.node v4.0 catalog](https://github.com/drayline/rootnode-skills) — "
    "27 Skills shipped simultaneously with the 5-generation Claude alignment. "
    "Calibrated dual-primary for Opus 5 + Sonnet 5 (both default to `high` effort on "
    "Claude API and Claude Code); integrated-aware for Fable 5; fallback-graceful for "
    "Opus 4.8; legacy-graceful for Sonnet 4.6; graceful-with-extended-thinking for "
    "Haiku 4.5. See the [Model Compatibility](https://github.com/drayline/rootnode-skills#model-compatibility) "
    "section of the README for full effort ladder, fallback semantics, and per-tier definitions."
)

# Descriptions updated where v4.0 changes are substantive; carried forward from
# v3.1 where the Skill's function is unchanged. Tier assignments per the v4.0
# calibration markers (final: T1=13, T2=7, T3=7).

VARIANT_A = [
    ("rootnode-prompt-compilation", "T3",
     "Four-stage pipeline (Parse, Select, Construct, Validate) that builds complete prompts and scaffolds entire Claude Projects. In v4.0, Project Mode delivers scaffold artifacts as separate files on disk (Custom Instructions + each knowledge file) rather than inline code blocks — the D5 contract change simplifies the upload workflow."),
    ("rootnode-prompt-validation", "T2",
     "Six-dimension Prompt Scorecard for evaluating prompts. Maps each weakness to a structural fix."),
    ("rootnode-project-audit", "T3",
     "Scores a Project on six dimensions with anchored 1-5 rubrics. Finds what's broken and prescribes targeted fixes. v4.0 anchors updated for the 14-tendency behavioral taxonomy and Opus 5's new tendencies."),
    ("rootnode-project-brief", "T1",
     "Generates a structured Project Brief — extracts goals, architecture, knowledge file inventory, Custom Instructions summary, Memory contents, current state, and key decisions from a Claude Project."),
    ("rootnode-anti-pattern-detection", "T2",
     "Detects seven structural patterns that cause ignored instructions and degraded output."),
    ("rootnode-behavioral-tuning", "T2",
     "Diagnoses 14 Claude behavioral tendencies with countermeasure templates ready to deploy. v4.0 taxonomy expanded from 10: verbosity refactored into a three-surface family (conversational, agentic narration, written deliverables) and four Opus 5-specific tendencies added (over-verification, scope expansion, subagent over-delegation, correction narration). Over-verification uses a new REMOVAL countermeasure shape — audit and delete accumulated self-directed re-check instructions."),
    ("rootnode-memory-optimization", "T2",
     "Rebalances content across Memory, Custom Instructions, knowledge files, and User Preferences. Produces edit prescriptions and trimming recommendations."),
    ("rootnode-context-budget", "T3",
     "Full context budget analysis under the current automatic-RAG-by-window model. Per-file evaluation across six dimensions, content routing, growth trajectory assessment, retrieval quality audit, and phased optimization. v4.0 rebuilt for the 1M-window primary landscape; fixed-token tier bands retired for qualitative window-relative bands; historical 200K-era measurements preserved as context."),
    ("rootnode-global-audit", "T3",
     "Audits all five global layers (Preferences, Styles, Memory, Skills, Connectors) using a six-dimension scorecard. Detects cross-layer failure modes."),
    ("rootnode-full-stack-audit", "T3",
     "Runs Project audit + Global audit + Cross-Layer Alignment Check in a single pass. The most comprehensive diagnostic in the catalog."),
    ("rootnode-session-handoff", "T1",
     "Produces structured XML session continuation documents. Captures active work streams, decisions with rationale, and open items into an ingestion-optimized handoff file."),
    ("rootnode-handoff-trigger-check", "T1",
     "Evaluates whether work-in-design is ready to hand off from chat to autonomous execution. Runs a 7-condition gate and returns a structured JSON verdict. v4.0 updates condition 7 token-headroom math for 1M-window primary models."),
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
     "Specialized methodology for system design, code review, incident response, security analysis, and API design. v4.0 adds Opus 5 cyber classifier posture — source-code vulnerability finding permitted; conservative-review-instruction fix (report-everything-then-filter) documented."),
    ("rootnode-domain-business-strategy", "T1",
     "Specialized methodology for consulting, competitive analysis, corporate strategy, and M&A."),
    ("rootnode-domain-content-communications", "T1",
     "Specialized methodology for writing, editing, content strategy, copywriting, and persuasion."),
    ("rootnode-domain-research-analysis", "T1",
     "Specialized methodology for data analysis, policy research, evidence synthesis, and systematic review."),
    ("rootnode-domain-agentic-context", "T1",
     "Specialized methodology for AI agent design, tool interfaces, context architecture, and multi-agent coordination. v4.0 adds refusal-fallback semantics for Opus 5 and Fable 5 (5 refusal categories, fallback content-block shape, usage.iterations accounting, refusals-as-observability-signal pattern)."),
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
     "Converts design specifications into deployment-ready Skill packages (SKILL.md + references/ + scripts/ + agents/). Six workflows: build, iterate, optimize, compare, review, revise. D9a grader runs on Opus 5 or Sonnet 5 (dual-primary tier)."),
    ("rootnode-cc-design", "T3",
     "Designs Claude Code environments. Five modes: design (new deployments), evolve (updates from friction), research (evaluate CC tools/patterns), template (reusable artifacts), remediate (consume hygiene findings → produce + execute plan). v4.0 adds subagent-delegation caps for Opus 5 CC deployments and the D4 verification-topology distinction (independent review of a different agent's work vs. self-directed re-checking)."),
]

EXPECTED_COUNTS = {"A": 22, "B": 3, "C": 2, "total": 27}
