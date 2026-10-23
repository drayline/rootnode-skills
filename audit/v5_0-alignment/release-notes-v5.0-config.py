# v5.0 config for generate_release_notes.py.
# Per-cycle artifact — lives under audit/v5_0-alignment/ per the audit/README.md
# convention (standing tooling at root; cycle configs under audit/v<N>-*/).
# Modeled on audit/v4_0-alignment/release-notes-v4.0-config.py.

VERSION = "5.0"

# Tier names per catalog spec §3.1 (D3: tier structure unchanged; only the
# model column refreshes).
TIER_LABEL = {
    "T1": "Model-compatible (T1)",
    "T2": "Sonnet-graceful (T2)",
    "T3": "High-effort recommended (T3)",
}

CATALOG_RELEASE = (
    "Part of the [root.node v5.0 catalog](https://github.com/drayline/rootnode-skills) — "
    "27 Skills shipped simultaneously with the 5.5-generation Claude alignment. "
    "Calibrated dual-primary for Opus 5.5 + Sonnet 5.5 (Opus 5.5 is the Claude Code default; "
    "effort defaults to `medium` on the 5.5 models in Claude Code); integrated-aware for "
    "Fable 5.1; subagent-aware for Haiku 5.5; fallback-graceful for Opus 5 / Sonnet 5; "
    "legacy-graceful for Sonnet 4.6. See the [Model Compatibility](https://github.com/drayline/rootnode-skills#model-compatibility) "
    "section of the README for effort defaults by model and surface, fallback semantics, and per-tier definitions."
)

# Blurbs: the v4.0 function description carried forward, plus one v5.0 sentence
# computed from the catalog spec §4 row (L = calibration line only; L+ = row body
# edits; S = separate spec). Tiers per the §4 table with the block-selection
# correction (spec defect: row says T1, Skill is T2 — operator-confirmed
# 2026-10-22). Final: T1 = 13, T2 = 7, T3 = 7.

_L = " v5.0: calibration refreshed for the 5.5 generation; no functional change."

VARIANT_A = [
    ("rootnode-prompt-compilation", "T3",
     "Four-stage pipeline (Parse, Select, Construct, Validate) that builds complete prompts and scaffolds entire Claude Projects. v5.0 adds a reasoning-extraction check to Stage 4 Validate — instructions that ask the model to reproduce its internal reasoning in the response can be declined with `stop_reason: \"refusal\"` on every current model — and drops thinking-disabled mitigations from Project Mode scaffolds (thinking cannot be disabled on the primary tier)."),
    ("rootnode-prompt-validation", "T2",
     "Six-dimension Prompt Scorecard for evaluating prompts. Maps each weakness to a structural fix. v5.0 adds symptom-fix entries for `reasoning_extraction` refusals and for think-less instructions that do not reduce thinking (lower effort instead)."),
    ("rootnode-project-audit", "T3",
     "Scores a Project on six dimensions with anchored 1-5 rubrics. Finds what's broken and prescribes targeted fixes. v5.0 scores Dimension 6 against the 15-tendency behavioral taxonomy and refreshes effort guidance for the `medium`-default generation."),
    ("rootnode-project-brief", "T1",
     "Generates a structured Project Brief — extracts goals, architecture, knowledge file inventory, Custom Instructions summary, Memory contents, current state, and key decisions from a Claude Project." + _L),
    ("rootnode-anti-pattern-detection", "T2",
     "Detects seven structural patterns that cause ignored instructions and degraded output." + _L),
    ("rootnode-behavioral-tuning", "T2",
     "Diagnoses 15 Claude behavioral tendencies with countermeasure templates ready to deploy. v5.0 adds tendency #15, early turn termination (documented in all four 5.5-generation prompting guides), repairs the routing surface so tendencies 11–15 are reachable from SKILL.md, rebuilds the deployment-conditioning tables for the `medium`-default generation, and adds documented facets to existing tendencies (unrequested additions, reviewer-round launches at `xhigh`/`max`, tool-suppression carry-over)."),
    ("rootnode-memory-optimization", "T2",
     "Rebalances content across Memory, Custom Instructions, knowledge files, and User Preferences. Produces edit prescriptions and trimming recommendations." + _L),
    ("rootnode-context-budget", "T3",
     "Full context budget analysis under the current automatic-RAG-by-window model. Per-file evaluation across six dimensions, content routing, growth trajectory assessment, retrieval quality audit, and phased optimization. v5.0 makes 1M universal across the four current models (Haiku 4.5's 200K becomes a legacy note), refreshes tokenizer notes, and adds a cache-pricing budget note: compacting early to save cost may no longer be the right tradeoff."),
    ("rootnode-global-audit", "T3",
     "Audits all five global layers (Preferences, Styles, Memory, Skills, Connectors) using a six-dimension scorecard. Detects cross-layer failure modes. v5.0 refreshes effort guidance for the `medium`-default generation."),
    ("rootnode-full-stack-audit", "T3",
     "Runs Project audit + Global audit + Cross-Layer Alignment Check in a single pass. The most comprehensive diagnostic in the catalog. v5.0 refreshes effort guidance for the `medium`-default generation."),
    ("rootnode-session-handoff", "T1",
     "Produces structured XML session continuation documents. Captures active work streams, decisions with rationale, and open items into an ingestion-optimized handoff file." + _L),
    ("rootnode-handoff-trigger-check", "T1",
     "Evaluates whether work-in-design is ready to hand off from chat to autonomous execution. Runs a 7-condition gate and returns a structured JSON verdict. v5.0 updates condition 7 for 1M on all four current models, the `medium` Claude Code effort default, the Haiku 5.5 tokenizer, and Haiku 5.5's >100K-prompt price band."),
    ("rootnode-profile-builder", "T1",
     "Conversational profile builder. Reads a target JSON Schema, conducts a progressive-depth interview, validates answers, and writes the resulting profile to a destination path." + _L),
    ("rootnode-identity-blocks", "T1",
     "8 identity approaches (Strategic Advisor, Technical Architect, Research Synthesist, and more)." + _L),
    ("rootnode-reasoning-blocks", "T1",
     "18 reasoning variants across 6 categories (Analytical, Strategic, Creative, Technical, Research, Comparative). v5.0 sweeps every block for reproduce-your-reasoning phrasing (a `reasoning_extraction` refusal trigger) and rewrites hits to \"state the conclusion and a short rationale.\""),
    ("rootnode-output-blocks", "T1",
     "10 output format specifications (Executive Brief, Technical Design, Decision Matrix, and more)." + _L),
    ("rootnode-block-selection", "T2",
     "Decision trees for choosing the right identity, reasoning, and output approach for any task type." + _L),
    ("rootnode-domain-software-engineering", "T1",
     "Specialized methodology for system design, code review, incident response, security analysis, and API design. v5.0 replaces the Opus 5 cyber posture with a 5.5-generation one (finding vulnerabilities in source code is allowed; high-risk dual-use is not), adds Anthropic's \"run a real check that exercises the change\" block as the external-verification template for code tasks, and adds a surgical-edit token-cost rule."),
    ("rootnode-domain-business-strategy", "T1",
     "Specialized methodology for consulting, competitive analysis, corporate strategy, and M&A." + _L),
    ("rootnode-domain-content-communications", "T1",
     "Specialized methodology for writing, editing, content strategy, copywriting, and persuasion. v5.0 notes that v4.0-era anti-list countermeasures can over-correct on Fable 5.1 and prefers the conditional formulation."),
    ("rootnode-domain-research-analysis", "T1",
     "Specialized methodology for data analysis, policy research, evidence synthesis, and systematic review. v5.0 adds marked-quotation discipline (Fable 5.1 can reproduce source passages without quotation marks) and a search-triggering nudge for `low` effort."),
    ("rootnode-domain-agentic-context", "T1",
     "Specialized methodology for AI agent design, tool interfaces, context architecture, and multi-agent coordination. v5.0 rebuilds refusal and fallback semantics per model (Haiku 5.5 has no server-side fallback) and adds harness rules: never put user text in a `tool_result`, forced `tool_choice` removed, progress updates arrive in `thinking` blocks, advisory time budgets."),
]

VARIANT_B = [
    ("rootnode-critic-gate", "T2",
     "Profile-driven gate that evaluates work against configured thresholds before merge or handoff. Reads a critic profile produced by `profile-builder` and returns a structured verdict with rationale. v5.0: a reviewer that could not inspect returns `status: blocked`, never an empty findings list; advisor-tool pairing rule (advisor at least as capable as the executor)."),
    ("rootnode-mode-router", "T1",
     "Profile-driven router that reads a mode configuration and routes work by strictness, scope, or context. The runtime counterpart to chat-side `block-selection`." + _L),
    ("rootnode-repo-hygiene", "T3",
     "14-category sweep + 7-layer leak check + anti-pattern detection across an existing Claude Code deployment. Produces `HYGIENE_REPORT.md` consumable by `cc-design` REMEDIATE mode. v5.0 adds the hook exit-code check: a `command` hook that enforces with exit 1 is non-blocking (only exit 2 blocks) — flagged as enforcement-as-preference — plus a hook-entry shape check."),
]

VARIANT_C = [
    ("rootnode-skill-builder", "T2",
     "Converts design specifications into deployment-ready Skill packages (SKILL.md + references/ + scripts/ + agents/). Six workflows: build, iterate, optimize, compare, review, revise. v5.0: D9a graders run on Opus 5.5 or Sonnet 5.5 (Opus 5 / Sonnet 5 valid fallback); D9c cites the 15-tendency taxonomy (fixes a v4.0 propagation miss that still said 10); Haiku 5.5 is a valid subject model, not a grader."),
    ("rootnode-cc-design", "T3",
     "Designs Claude Code environments. Five modes: design (new deployments), evolve (updates from friction), research (evaluate CC tools/patterns), template (reusable artifacts), remediate (consume hygiene findings → produce + execute plan). v5.0 fixes the hook reference (enforcement uses exit 2; exit 1 is non-blocking; correct `matcher` + `hooks` config shape), adds a computed session-report output standard, hardens delegation (spec-digest briefs, capped refute loops, `blocked` ≠ empty), and adds the early-stop countermeasure for unattended runs."),
]

EXPECTED_COUNTS = {"A": 22, "B": 3, "C": 2, "total": 27}
