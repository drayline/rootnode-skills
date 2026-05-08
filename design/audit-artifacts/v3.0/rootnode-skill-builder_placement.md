# rootnode-skill-builder_placement.md

Placement note for `rootnode-skill-builder` v3.0. Always produced per `root_SKILL_BUILD_DISCIPLINE.md §4.1`.

Build date: 2026-05-08
Build agent: Claude Code Phase 32b
Predecessor: `rootnode-skill-builder` v2.1 (overwritten in place per KF §6.4 — same `name:` field, no rename rule triggered)

---

## CP/CC surface placement

**Surface: CP-side (chat-side Claude Project methodology Skill).**

The Skill operates as a build-time tool that takes design specifications as input and produces deployable Skill folders + audit artifacts. Its activation context is design conversations — when the user has a design spec in hand and wants the build executed.

v3.0 adds an executable layer (`scripts/`, `agents/`, `eval-viewer/`) that the methodology layer invokes when subagent execution and runnable environments are available. This expands tier compatibility to CC-side (where Tier A is feasible) and Cowork (where subagent execution is available). The methodology surface is unchanged — CP is still the canonical activation surface; CC and Cowork inherit the methodology when a Skill build runs in those environments.

---

## Composition lineage

**Producer for:** Deployable Skill zips (consumed by `~/.claude/skills/` install path or the `rootnode-skills` repo release pipeline).

**Composes with (lateral):**

- `rootnode-cc-design` — CC-side companion that designs CC environments and prompts; its output (design specs) becomes input to skill-builder when those designs include Skill artifacts.
- `rootnode-handoff-trigger-check` — autonomous-execution handoff gate; called in the chat→CC handoff before invoking skill-builder for delivery work.
- `rootnode-prompt-validation` — adjacent CP-side Skill that scores prompts; routing collision avoided via verb-class differentiation ("build" vs. "score") and explicit negative triggers in the description.
- `rootnode-project-audit` — adjacent CP-side Skill that audits Projects; routing collision avoided via vocabulary domain ("Skill" vs. "Project") and negative triggers.

**Producer→Consumer chain (formal contract):**

- `rootnode-repo-hygiene` Cat 14 process-abstraction findings → `rootnode-skill-builder` Gate 2 warrant evidence. The forward chain is implemented per `root_AGENT_ENVIRONMENT_ARCHITECTURE.md §5.4.3`; the v3.0 build inherits this contract from v2.1.

**No new cross-Skill contracts in v3.0.** v3.0 evolves D9 (sub-levels) and adds tooling-layer content; neither change introduces new fields, schemas, or composition semantics that downstream Consumers must align to. Existing contracts (the Producer→Consumer chain with repo-hygiene; Skills built per the build discipline that downstream Skills consume) remain unchanged.

---

## Duplication audit

| Adjacent Skill | Differentiation axis | Routing safe? |
|---|---|---|
| rootnode-prompt-validation | Verb class: "validate / score" vs. "build / package" | YES — non-overlapping verbs, explicit negative trigger in description |
| rootnode-project-audit | Vocabulary domain: "Project" vs. "Skill" | YES — explicit negative trigger in description |
| rootnode-prompt-compilation | Verb class: "compile" (prompt assembly) vs. "build" (Skill packaging) | YES — explicit negative trigger in description |
| rootnode-cc-design | Surface: CP design vs. CP build (same surface, distinct verbs) | YES — "design Skill methodology" excluded explicitly |
| rootnode-handoff-trigger-check | Verb class: "gate / check readiness" vs. "build / package" | YES — non-overlapping verbs |
| rootnode-block-selection | Vocabulary domain: "block" vs. "Skill" | YES — non-overlapping vocabulary |

All adjacent Skills route cleanly. v3.0's expanded description (967 chars) preserves the negative triggers from v2.1 verbatim and adds new trigger phrases for the new workflows (Iterate, Optimize Description, Compare Versions) without expanding into adjacent territory.

---

## Ship sequencing

`rootnode-skill-builder` v3.0 ships standalone — no upstream dependency on other v-bumps. Downstream Skills built via v3.0 inherit the `discipline_post: phase-30` marker and the routing-surface design pattern. Future Skill builds against the v3.0 methodology should:

- Use the new D9 sub-level architecture in their build summaries.
- Apply the intelligent abstraction principle as the primary design lens for new SKILL.md sections.
- Apply tone calibration ("explain the why") to new content per AEA §4.11.
- Declare per-workflow tier compatibility in references when tooling layers are present.

---

## Suggested entry for the runtime tooling catalog

For inclusion in `root_AGENT_ENVIRONMENT_ARCHITECTURE.md §6.1` (CP-side Skills table):

| Skill | Purpose | Implements pattern from |
|---|---|---|
| `rootnode-skill-builder` (v3.0) | Builds, validates, packages, tests, iterates, and optimizes deployment-ready Skill files (SKILL.md + references/ + scripts/ + agents/) from design specifications. Carries 9-dimension quality gate with D9a/b/c sub-levels, description refinement loop, blind version comparator. | Skill design and packaging discipline + behavioral validation methodology + multi-environment adaptation |

The Skill build does not auto-edit canonical KFs — methodology updates remain human-reviewed. This placement note surfaces the recommended entry for the seed Project review/update.

---

## Filing destination

This placement note is delivered to `design/audit-artifacts/v3.0/rootnode-skill-builder_placement.md` (within the rootnode-skills repo, alongside the deployable zip and other v3.0 audit artifacts). Operator may also file a copy at `Projects/ROOT/research/` per the canonical filing destination convention (KF §4.1).

---

*End of rootnode-skill-builder_placement.md.*
