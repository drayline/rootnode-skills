# rootnode-cc-design Placement Note

**Build event:** v2.0 release (predecessor `rootnode-cchq-design` v1.1.1)
**Build date:** 2026-05-05
**Build CV phase:** Phase 30 D-build
**Skill builder version:** rootnode-skill-builder v2.0
**Author:** rootnode

---

## Ecosystem placement

**Tier:** CC-side runtime tooling tier (`root_AGENT_ENVIRONMENT_ARCHITECTURE.md §6.2`).

**Surface coverage:** Dual — natural surface is CC for delivery-project work (especially REMEDIATE mode, which writes EXECUTION_PLAN.md to repo and executes against real files); secondary surface is CP for design conversations (DESIGN/EVOLVE/RESEARCH/TEMPLATE modes, plus REMEDIATE Phase 1 plan generation when working from pasted findings).

**Position in CC-side runtime tooling tier:** Second Skill to ship in this tier. Predecessor: `rootnode-repo-hygiene` v1.0.

## Composition lineage

**Producer→Consumer chain (upstream).**
- `rootnode-repo-hygiene` produces `HYGIENE_REPORT.md` (Phase 1 sweep + 7-layer leak check).
- `rootnode-cc-design` REMEDIATE mode consumes the report's Cat 11–14 structural findings and 7-layer leak findings.
- Cat 1–10 direct-cleanup findings route to repo-hygiene Phase 2, not REMEDIATE.

**Composition (lateral).**
- `rootnode-critic-gate` reviewed by REMEDIATE Phase 2 batches when `critic_gate_threshold: required` is set on the active profile.
- Field name and semantics align exactly with `rootnode-repo-hygiene §11.1` (`required` halts entry if critic-gate not installed; `optional` allows per-batch user choice).

**Producer→Consumer chain (downstream, deferred to v2.x).**
- REMEDIATE may surface methodology-generalizable patterns to `rootnode-skill-builder v2 Gate 2` (parallel to repo-hygiene's Cat 14 process-abstraction handoff). Not modeled in v2.0; document as roadmap item.

## Surface boundaries

**CP-side use of REMEDIATE:** allowed but produces only Phase 1 (plan generation as downloadable artifact). Phase 2 cannot execute without repo file access. Documented in SKILL.md as a workable but secondary path.

**CC-side use of all modes:** all five modes work in CC. REMEDIATE is the only mode whose Phase 2 has CC-specific requirements (repo file access for actual mutation).

**REMEDIATE input contract:** REMEDIATE consumes HYGIENE_REPORT.md format owned by `rootnode-repo-hygiene`. cc-design v2 cites repo-hygiene as authoritative rather than restating the format.

## Duplication audit (Gate 3 negative checks)

| Adjacent Skill | Differentiation |
|---|---|
| `rootnode-handoff-trigger-check` | Different mechanism: runtime gate (single-decision evaluation), not design methodology. Different invocation surface: applied at handoff moment, not design moment. |
| `rootnode-skill-builder` v2 | Different output class: skill-builder packages Skills; cc-design produces CC artifacts (CLAUDE.md drafts, EXECUTION_PLAN.md, agent topologies). |
| `rootnode-prompt-compilation` | Different surface: prompt-compilation is CP-only for chat prompt construction; cc-design is dual-surface with CC as natural surface. Different artifact class: prompts vs. CC environments. |
| `rootnode-repo-hygiene` | Different verb: hygiene scans for findings (Producer); cc-design consumes them (Consumer). Routing rule prevents miscalled invocations: Cat 1–10 → repo-hygiene Phase 2; Cat 11–14 + leaks → cc-design REMEDIATE. |
| `rootnode-project-audit` | Different surface: project-audit operates on Claude Projects (CP); cc-design's CC-side work operates on Claude Code repositories. The two never address the same artifact. |

No duplication catches. Placement is tight.

## Ship sequencing

v2.0 ships as the v2.3 standalone release (deferred from v2.2 paired ship of skill-builder v2 + repo-hygiene v1). The v2.2 paired ship is the upstream contract source; cc-design v2.0 is the downstream consumer alignment release.

---

*This placement note is produced as a Step 0 audit artifact during the v2.0 build CV. It documents the ecosystem-fit verdict (PASS) and serves as durable record of the v2.0 placement decision for future evolution. File to `Projects/ROOT/research/`.*
