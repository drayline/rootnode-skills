"""Release-notes config for catalog v6.1 (Fable 5.2 alignment and scale-fit rigor).

Consumed by the repo-root generate_release_notes.py:
    py -3 generate_release_notes.py --config audit/v6_1-release/release-notes-v6.1-config.py

Plugin order follows .claude-plugin/marketplace.json. Build spec:
design/root_DESIGN_fable_5_2_alignment.md v1.0 (LF sha256 8e9722a2...b1fdb).
Five plugins go to 6.1.0 and rootnode-code to 6.2.0.
"""

CATALOG_RELEASE = "catalog-v6.1"

CALIBRATION = (
    "Calibration lines updated for Claude Fable 5.2, which replaces Fable 5.1: Tier 1 Skills name Fable 5.2 "
    "beside Opus 5.5, Sonnet 5.5 and Haiku 5.5; Tier 2 Skills add that Fable 5.2 defaults to `high` and steps "
    "down to `medium` where the work holds; Tier 3 Skills name Fable 5.2 as a target for the hardest and "
    "longest runs instead of a reserve. Tier membership is unchanged (13 / 7 / 7)."
)

PLUGINS = [
    {
        "name": "rootnode-projects",
        "version": "6.1.0",
        "summary": "Fable 5.2 calibration; stale-caution check in memory-optimization",
        "changes": [
            CALIBRATION,
            "memory-optimization: a new audit step (Stage 2d) checks Memory, Custom Instructions and knowledge "
            "files for cautions whose reason no longer holds, lines written for an older model, and absolute "
            "rules without scope. The fix is removal or a scoped rewrite, proposed to the user, never applied "
            "silently.",
            "context-budget: model facts refreshed for Fable 5.2 (1M context, Opus 4.7-era tokenizer, cache "
            "reads at $0.20 per million tokens).",
            "project-audit: the behavioral taxonomy count reads seventeen.",
        ],
    },
    {
        "name": "rootnode-code",
        "version": "6.2.0",
        "summary": "cc-design sizes stops and gates to a rigor level; stop rule; budgets as mechanisms",
        "changes": [
            "cc-design: a design now carries a rigor level — `sprint`, `standard` or `strict` — set by a new "
            "`rigor` field in the design brief and a sixth interview question. Every DESIGN and TEMPLATE output "
            "opens with `Rigor: <level> — <reason>`, and the level decides the gates, review roles, digest "
            "binding and report depth. A brief with no level is `sprint` unless it names production data, an "
            "irreversible operation, or more than one contributor, which make it `standard`; `strict` is chosen "
            "explicitly. At `sprint` the output has no reviewer role and no phase gates.",
            "cc-design: halt triggers follow a stop rule — stop only when the next action cannot be undone, "
            "when a decision could reasonably go either way and only the operator can make it, or when a spend "
            "cap is reached — plus the project's own irreversible actions. The session-prompt and "
            "autonomous-prompt templates no longer stop on a failing test, an unavailable tool or ambiguous "
            "input; they work through it and report it. Every prompt lists the routine actions that need no "
            "approval.",
            "cc-design: token budgets are no longer written into prompts. Spend and context limits go in the "
            "brief (new `limits` field) and are enforced by mechanisms such as `--max-budget-usd`.",
            "cc-design: Fable 5.2 facts in the delegation reference (model tiers, effort, self-review subagents "
            "at `xhigh` and `max`); the brief interview asks for each authority constraint with its reason.",
            CALIBRATION,
            "Hooks unchanged since 6.1.0: both stay opt-in per repository through `.claude/rootnode-gates.json`.",
        ],
    },
    {
        "name": "rootnode-prompts",
        "version": "6.1.0",
        "summary": "Fable 5.2 calibration; reasoning-trait rewrite; token budgets out of agent prompts",
        "changes": [
            CALIBRATION,
            "identity-blocks and block-selection: the example behavioral sentence no longer asks the model to "
            "explain its reasoning in the response; it now asks for the grounds of each conclusion.",
            "domain-agentic-context: a fifth harness rule keeps token budgets out of the agent's prompt (the "
            "per-zone token plan stays in the design document); refusal, fallback and forced `tool_choice` "
            "facts name Fable 5.2.",
            "prompt-compilation: the `reasoning_extraction` note names Fable 5.2.",
        ],
    },
    {
        "name": "rootnode-tuning",
        "version": "6.1.0",
        "summary": "Taxonomy 15 -> 17: caution accumulation, silent long runs, budget defect",
        "changes": [
            "behavioral-tuning: seventeen tendencies. New #16 caution accumulation (the agent asks approval for "
            "routine steps or stops at the first error because cautions piled up) and #17 silent long runs (long "
            "stretches of tool calls with no user-facing text), each with routing rows, deployment calibration "
            "and a template in the reference.",
            "behavioral-tuning: a fifth conditional defect, a token budget shown in the prompt, which raises "
            "spending on Fable 5.2.",
            "behavioral-tuning: Fable 5.2 facets — on #11, \"treat that answer as done\" lines reduce the model's "
            "willingness to flag its own mistakes; on #12, ownership framing is a costed lever; on #13, "
            "self-review subagents at `xhigh` and `max`; on #15, effort conditioning and the finishing block's "
            "cost.",
            CALIBRATION,
        ],
    },
    {
        "name": "rootnode-governance",
        "version": "6.1.0",
        "summary": "Fable 5.2 calibration and model facts",
        "changes": [
            CALIBRATION,
            "handoff-trigger-check: context-window and effort-default facts name Fable 5.2.",
        ],
    },
    {
        "name": "rootnode-skill-builder",
        "version": "6.1.0",
        "summary": "Fable 5.2 calibration; taxonomy count",
        "changes": [
            CALIBRATION,
            "skill-builder: SKILL.md cites the 17-tendency taxonomy for D9c analytical validation. Three reference lines "
            "(`references/behavioral-validation.md` twice, `references/skills-spec.md` once) still say 15; they are "
            "fixed in the next patch.",
        ],
    },
]

EXPECTED_COUNT = 6
