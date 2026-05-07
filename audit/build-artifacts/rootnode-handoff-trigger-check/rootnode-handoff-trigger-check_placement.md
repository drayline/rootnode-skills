# rootnode-handoff-trigger-check_placement.md

**Skill:** rootnode-handoff-trigger-check
**Version:** 1.1.2 (revision; predecessor 1.1.1)
**Build event:** 2026-05-05 activation-precision tuning (Phase C-1 of post-Phase-30 work plan)
**Reviewer:** rootnode-skill-builder v2.0 REVISE pathway

---

## Placement (unchanged from v1.1.1)

**Surface:** CP-side (chat design conversation; runs in Claude.ai Projects).

**Role in runtime tooling map:** Pre-handoff gate. Sits at the boundary between chat-led design work and autonomous execution. Evaluates work-in-design against 7 conditions (spec stability, verification surface, invariants, pump-primer, work decomposition, rollback cost, token budget headroom) and returns a structured verdict that the user (or upstream orchestrator) can act on. Three invocation modes (deliberate / proactive sensing / conversational walkthrough) preserved unchanged.

**Composition:**
- Soft-points TO `rootnode-profile-builder` (line 279) for profile authoring.
- Negative-trigger pointer to other Skills handles routing distinctions: not for completed-work evaluation, not for runtime selection (mode-router does that), not for prompt quality (prompt-validation does that).

**Duplication check:** No duplication. handoff-trigger-check is the only readiness gate for the chat→Code transition.

---

## Suggested KF update for `root_AGENT_ENVIRONMENT_ARCHITECTURE.md §6`

No change required. v1.1.2 is an activation-precision patch — same Skill role, same pipeline, same outputs. The runtime tooling catalog entry (if present) does not need revision.

---

## Build note

Activation-precision tuning per the May 5 delta-eval's Q3 disposition (revision warranted now that other Skills are also being touched in the same release window). Two symptom-phrased triggers added to the description: "are we ready to ship this" and "should I just hand this off." These cover the user-vocabulary surface that omits the word "handoff" — high-compression communicators are unlikely to use the literal "handoff check" phrasing in a live design conversation. The new triggers complement (not replace) the existing explicit triggers.

Char budget: description grew 934 → 994 chars (+60); 30-char headroom remains under the 1024 ceiling. The 8-dimension quality gate passed cleanly with one dimension (activation precision) materially improved. No methodology, schema, profile, or workflow changes — once the Skill activates, behavior is identical to v1.1.1.

The third candidate trigger flagged in the predecessor eval ("is the spec stable enough") was not added — it duplicates Condition 1 of the 7-condition gate as a trigger phrase, which would over-fit the activation surface to a single condition rather than the gate as a whole. Leave that to natural-language coverage by the existing "ready" / "handoff" triggers.

---

*End of placement note. File to seed Project Drive at `Projects/ROOT/research/` for build provenance.*
