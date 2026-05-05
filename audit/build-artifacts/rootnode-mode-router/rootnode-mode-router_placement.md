# rootnode-mode-router_placement.md

**Skill:** rootnode-mode-router
**Version:** 1.0.2 (revision; predecessor 1.0.1)
**Build event:** 2026-05-05 brand-strip revision (Phase A of post-Phase-30 work plan)
**Reviewer:** rootnode-skill-builder v2.0 REVISE pathway

---

## Placement (unchanged from v1.0.1)

**Surface:** CC-side (Claude Code / autonomous orchestrator runtime).

**Role in runtime tooling map:** Profile selector. Sits upstream of consuming Skills (rootnode-handoff-trigger-check, rootnode-critic-gate, future profile-driven Skills). Resolves "which profile is active right now?" from triggering context (calendar, time window, geofence, manual override, custom signals). Returns a profile name; consuming Skill loads the named profile and applies it.

**Composition:**
- Authoring its own router config: composes with `rootnode-profile-builder` (soft pointer; user can hand-edit JSON if profile-builder unavailable).
- Output consumed by: `rootnode-handoff-trigger-check`, `rootnode-critic-gate` (and any future Skill following the profile-shaped configuration pattern).
- Cross-Skill negative triggers correctly point to handoff-trigger-check (work-readiness eval) and critic-gate (proposed-change eval) to prevent routing collisions.

**Duplication check:** No duplication with handoff-trigger-check (different surface — that's a runtime gate, this is a profile router). No duplication with critic-gate (same reasoning). No duplication with profile-builder (that's authoring; this is selection at runtime).

---

## Suggested KF update for `root_AGENT_ENVIRONMENT_ARCHITECTURE.md §6`

No change required. mode-router v1.0.2 is a behavior-identical brand-strip patch; placement and composition are unchanged from v1.0.1. The runtime tooling catalog entry (if present) does not need revision.

If the runtime tooling catalog at §6 does not yet list mode-router as a CC-side runtime Skill alongside handoff-trigger-check, critic-gate, and repo-hygiene, that's a separate gap — flag during a future catalog review, not as a v1.0.2 propagation requirement.

---

## Build note

This is a brand-strip revision per Phase 27/28 methodology absorption. The single change is body line 34: `cchq library's analog` → `rootnode runtime layer's analog`. No methodology, structural, or behavioral changes. The 8-dimension quality gate passed cleanly with all dimensions matching v1.0.1's prior review state. Description budget remains tight at 1006/1024 chars; symptom-trigger additions deferred per the predecessor eval recommendation.

---

*End of placement note. File to seed Project Drive at `Projects/ROOT/research/` for build provenance.*
