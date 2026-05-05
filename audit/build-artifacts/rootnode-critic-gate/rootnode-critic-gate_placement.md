# rootnode-critic-gate_placement.md

**Skill:** rootnode-critic-gate
**Version:** 1.0.2 (revision; predecessor 1.0.1)
**Build event:** 2026-05-05 activation-precision tuning (Phase C-2 of post-Phase-30 work plan)
**Reviewer:** rootnode-skill-builder v2.0 REVISE pathway

---

## Placement (unchanged from v1.0.1)

**Surface:** CC-side (Claude Code / autonomous orchestrator runtime).

**Role in runtime tooling map:** Independent re-derivation gate. Sits between change-author (Claude Code, autonomous engine, etc.) and change-application (merge, deploy, write). Evaluates a proposed change against the work's authority matrix and a 4-check protocol (invariant compliance, scope authorization, detection narrowness, regression risk) and returns a structured verdict (APPROVE / REQUEST_CHANGES / REJECT). Profile-driven thresholds calibrate strictness to availability mode.

**Composition (unchanged):**
- Composes WITH `rootnode-repo-hygiene` Phase 2 via the caller-side `critic_gate_threshold: required | optional` field on repo-hygiene's profile (verified contract-correct in `root_eval_4_cc_skills_phase30_review.md` §3 — caller-side and callee-side contracts are at distinct layers; critic-gate's existing severity routing handles invocation cleanly).
- Will compose WITH `rootnode-cc-design` v2 REMEDIATE Phase 2 via the same `critic_gate_threshold` mechanism once cc-design v2 ships (Phase 30 D-build queued).
- Soft-points TO `rootnode-profile-builder` (line 183) for profile authoring.
- Output schema mirrors `rootnode-handoff-trigger-check` shape for orchestrator parser reuse.

**Duplication check:** No duplication. critic-gate is the only proposed-change re-derivation gate in the runtime tooling map.

---

## Suggested KF update for `root_AGENT_ENVIRONMENT_ARCHITECTURE.md §6`

No change required. v1.0.2 is an activation-precision patch — same Skill role, same pipeline, same outputs, same composition contracts. The runtime tooling catalog entry (if present) does not need revision.

---

## Build note

Activation-precision tuning per the May 5 delta-eval's Q3 disposition. Three changes to the trigger surface, with offsetting compression to stay within the 1024-char budget:

1. **Consolidation:** "review this proposed change" + "approve this diff" → "review/approve this proposed change." Saves ~17 chars; preserves both invocation phrasings under one trigger phrase. "Proposed change" retained as the term-of-art the Skill uses internally.
2. **1st-person rephrase:** "should this land" → "should I let this land." Same activation intent, but Aaron's high-compression vocabulary skews 1st-person ("should I let X" vs imperative "should X"). +6 chars.
3. **New symptom trigger:** "is this safe to merge" added. Existing "is this change safe" frames the question abstractly; "is this safe to merge" frames it at the user's actual decision point (commit/merge moment). Different vocabulary surface, same Skill activation. +22 chars.

Char budget: description grew 996 → 1014 chars; 10-char headroom remains. The 8-dimension quality gate passed cleanly with one dimension (activation precision) materially improved. No methodology, schema, profile, workflow, or composition-contract changes — once the Skill activates, behavior is identical to v1.0.1.

The lead-verb tightening flagged in the predecessor eval ("Independent re-derivation gate" → "Evaluates proposed changes...") was not applied. "Independent re-derivation" is the term-of-art that distinguishes critic-gate from generic code review; substituting "Evaluates" loses that semantic precision in exchange for marginal verb-leading gains. Eval flagged it as "Could be tighter," not blocking; decision is to retain.

---

*End of placement note. File to seed Project Drive at `Projects/ROOT/research/` for build provenance.*
