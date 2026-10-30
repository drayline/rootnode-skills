# v5.0.1 config for generate_release_notes.py.
# Per-cycle artifact — lives under audit/v5_0_1-patch/ per the audit/README.md
# convention (standing tooling at root; cycle configs under audit/v<N>-*/).
# Patch catalog release (playbook §1.6): only the 12 Skills that changed get
# per-Skill notes, so the variant lists and expected counts cover those 12.
# Function descriptions and tiers are carried from
# audit/v5_0-alignment/release-notes-v5.0-config.py; each Skill's v5.0 sentence
# is replaced by its v5.0.1 change, from design/root_DESIGN_catalog_v5.0.1_patch.md.

VERSION = "5.0.1"

TIER_LABEL = {
    "T1": "Model-compatible (T1)",
    "T2": "Sonnet-graceful (T2)",
    "T3": "High-effort recommended (T3)",
}

CATALOG_RELEASE = (
    "Part of the [root.node v5.0.1 patch](https://github.com/drayline/rootnode-skills/releases/tag/catalog-v5.0.1) — "
    "12 of the 27 Skills patched after the v5.0 behavioral validation of cc-design; the other 15 stay at v5.0. "
    "Calibration is unchanged from v5.0: dual-primary for Opus 5.5 + Sonnet 5.5. See the "
    "[Model Compatibility](https://github.com/drayline/rootnode-skills#model-compatibility) section of the README "
    "for effort defaults by model and surface, fallback semantics, and per-tier definitions."
)

_EFFORT = (" v5.0.1: the effort paragraph now states the same single effort rule as the calibration line; "
           "it had also said the Skill benefits from `high` or higher.")

VARIANT_A = [
    ("rootnode-prompt-compilation", "T3",
     "Four-stage pipeline (Parse, Select, Construct, Validate) that builds complete prompts and scaffolds entire Claude Projects." + _EFFORT),
    ("rootnode-prompt-validation", "T2",
     "Six-dimension Prompt Scorecard for evaluating prompts. Maps each weakness to a structural fix. v5.0.1: the symptom-fix map names Opus 5.5 + Sonnet 5.5 as the current tier; Opus 5 stays named only as the fallback."),
    ("rootnode-project-audit", "T3",
     "Scores a Project on six dimensions with anchored 1-5 rubrics. Finds what's broken and prescribes targeted fixes." + _EFFORT),
    ("rootnode-context-budget", "T3",
     "Full context budget analysis under the current automatic-RAG-by-window model. Per-file evaluation across six dimensions, content routing, growth trajectory assessment, retrieval quality audit, and phased optimization." + _EFFORT + " The price-band note now states only the landscape's ≤100K / >100K band fact."),
    ("rootnode-global-audit", "T3",
     "Audits all five global layers (Preferences, Styles, Memory, Skills, Connectors) using a six-dimension scorecard. Detects cross-layer failure modes." + _EFFORT),
    ("rootnode-full-stack-audit", "T3",
     "Runs Project audit + Global audit + Cross-Layer Alignment Check in a single pass. The most comprehensive diagnostic in the catalog." + _EFFORT),
    ("rootnode-handoff-trigger-check", "T1",
     "Evaluates whether work-in-design is ready to hand off from chat to autonomous execution. Runs a 7-condition gate and returns a structured JSON verdict. v5.0.1: the condition 7 heading drops its version label, and the Skill's own files no longer use the retired name `handoff-gate`."),
    ("rootnode-domain-research-analysis", "T1",
     "Specialized methodology for data analysis, policy research, evidence synthesis, and systematic review. v5.0.1: the examples pointer now says the examples file also holds one output-format fragment (Example 4)."),
    ("rootnode-domain-agentic-context", "T1",
     "Specialized methodology for AI agent design, tool interfaces, context architecture, and multi-agent coordination. v5.0.1: the reasoning-approaches reference names Opus 5.5 + Sonnet 5.5 as the current tier; Opus 5 stays named only as the fallback."),
]

VARIANT_B = [
    ("rootnode-critic-gate", "T2",
     "Profile-driven gate that evaluates work against configured thresholds before merge or handoff. Reads a critic profile produced by `profile-builder` and returns a structured verdict with rationale. v5.0.1: the output JSON carries `\"status\": \"complete\" | \"blocked\"`, with a `blocked_reason` when blocked (an additive field), and references to the readiness gate use `rootnode-handoff-trigger-check`."),
    ("rootnode-mode-router", "T1",
     "Profile-driven router that reads a mode configuration and routes work by strictness, scope, or context. The runtime counterpart to chat-side `block-selection`. v5.0.1: references to the readiness gate use its current name, `rootnode-handoff-trigger-check`; no functional change."),
]

VARIANT_C = [
    ("rootnode-cc-design", "T3",
     "Designs Claude Code environments. Five modes: design (new deployments), evolve (updates from friction), research (evaluate CC tools/patterns), template (reusable artifacts), remediate (consume hygiene findings → produce + execute plan). v5.0.1: Stop-hook bounds are scoped to the stop chain, with a no-progress cap and a chain-total cap, and the guidance pairs them with Claude Code's own continuation cap; the migration-guard example catches more delete forms (`find -delete`, globs, PowerShell) and states what a text-matching guard cannot see; autonomous prompt templates gain a resume line; the prompt-design patterns add shell lessons from this patch's build (git pathspecs, naming the Python interpreter, worker allow-lists); cross-references and counts are corrected."),
]

EXPECTED_COUNTS = {"A": 9, "B": 2, "C": 1, "total": 12}
