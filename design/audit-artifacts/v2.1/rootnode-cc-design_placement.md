# rootnode-cc-design v2.1 — Ecosystem Placement Note

**Build CV:** rootnode-skill-builder v3.0
**Gate 3 evaluation:** ecosystem fit check
**Date authored:** 2026-05-08

---

## Placement decision

cc-design v2.1 occupies the **same ecosystem slot as v2.0** — this build is an additive refinement, not a re-placement.

**Surface:** dual (CP-side + CC-side). DESIGN, EVOLVE, RESEARCH, TEMPLATE modes operate in both. REMEDIATE mode is CC-native (consumes a `HYGIENE_REPORT.md` from the repo and writes `EXECUTION_PLAN.md` back to it; CP-only invocation requires pasted findings and produces plan without executing).

**Composition lineage:** unchanged from v2.0.

| Composes with | Direction | Contract |
|---|---|---|
| `rootnode-repo-hygiene` (CC) | upstream | Produces `HYGIENE_REPORT.md`; cc-design REMEDIATE consumes it. Cat 1–10 stay with repo-hygiene Phase 2; Cat 11–14 + 7-layer leaks route to cc-design REMEDIATE. |
| `rootnode-critic-gate` (CC) | optional | When `critic_gate_threshold: required` on a REMEDIATE plan step and critic-gate is installed, plan steps submit for APPROVE/REQUEST_CHANGES/REJECT. |
| `rootnode-handoff-trigger-check` (CC) | recommended | Pre-launch readiness check before autonomous CC execution that exceeds ~5 work items. |
| `rootnode-prompt-validation` (CP) | carve-out | Chat prompts route here, NOT cc-design. |
| `rootnode-prompt-compilation` (CP) | carve-out | Chat prompt scaffolding routes here, NOT cc-design. |
| `rootnode-project-audit` (CP) | carve-out | Chat Project audits route here, NOT cc-design. |

## Gate 3 — duplication check

No duplication detected. The new prompt-specific triggers (`"build a CC prompt"`, `"design a CC prompt for X"`, `"write a session prompt"`) target CC prompts specifically, distinct from chat prompts (rootnode-prompt-validation/compilation territory) and Skills (rootnode-skill-builder territory). The new output-discipline section deepens existing CC-prompt design coverage; it does not establish a new capability surface that overlaps another Skill.

## Gate 1 (decomposition) — confirmed

The four new disciplines (shell-agnostic, pre-flight Skill enumeration, continuation-phrase ambiguity gate, forward-state-aware authoring) are methodology guidance for produced CC prompts. They are NOT lifecycle guarantees (which would belong in hooks), NOT path-scoped rules (`.claude/rules/`), NOT always-loaded standing context (CLAUDE.md), NOT external API contracts (MCP). They are multi-step procedural guidance the agent applies when producing a CC prompt deliverable — Skills layer is correct.

## Suggested entry for runtime tooling catalog

No change to the canonical entry in `audit/canonical-kfs/root_AGENT_ENVIRONMENT_ARCHITECTURE.md §6` for v2.1 — the Skill's identity, surface, and composition contract are unchanged from v2.0. Version bump only.

## Ecosystem-fit verdict

PASS. cc-design v2.1 fills the same ecosystem slot as v2.0 with sharper activation surface (three new CC-prompt triggers) and deeper output discipline (four empirically-grounded bullets in the prompt-design references). No re-placement required.
