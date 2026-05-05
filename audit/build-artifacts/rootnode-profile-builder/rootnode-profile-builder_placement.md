# rootnode-profile-builder_placement.md

**Skill:** rootnode-profile-builder
**Version:** 1.0.2 (revision; predecessor 1.0.1)
**Build event:** 2026-05-05 brand-strip revision (Phase B of post-Phase-30 work plan)
**Reviewer:** rootnode-skill-builder v2.0 REVISE pathway

---

## Placement (unchanged from v1.0.1)

**Surface:** CP-side (Claude.ai Project / chat surface).

**Role in runtime tooling map:** Universal profile authoring tool. Walks any rootnode Skill's JSON Schema and produces validated profile JSON via plain-language interview. Schema-agnostic by design — every consuming Skill (handoff-trigger-check, critic-gate, mode-router, future Skills) uses this single builder rather than each Skill forking its own authoring flow.

**Composition:**
- Soft-pointed FROM: `rootnode-handoff-trigger-check` (line 279), `rootnode-critic-gate` (line 183), `rootnode-mode-router` (line 224 — for router config schema). All three consuming Skills reference profile-builder with "if available" language; profile-builder's absence does not block any of them (users can hand-edit JSON against the schema instead).
- Soft-points TO: none. Profile-builder is the leaf node of the authoring chain — it reads schemas, conducts interviews, writes files. No downstream rootnode dependencies.

**Default output path change (this revision):** `~/.cchq/profiles/{schema-name}/{profile-name}.json` → `~/.rootnode/profiles/{schema-name}/{profile-name}.json`. This is a runtime-observable change for users who relied on the v1.0.1 default path. Migration: existing files at `~/.cchq/profiles/...` continue to work (the schema and profile contents are unchanged); v1.0.2 simply writes new files to the new default. Users who want consistency can move existing files manually or pass an explicit destination override.

**Duplication check:** No duplication with any existing rootnode Skill. Profile authoring is its single concern.

---

## Suggested KF update for `root_AGENT_ENVIRONMENT_ARCHITECTURE.md §6`

No change required. profile-builder v1.0.2 is a behavior-preserving brand-strip patch with one runtime-observable side effect (default path change). The runtime tooling catalog entry (if present) does not need revision; the catalog describes the Skill's role, not its default path.

If the tooling catalog at §6 documents path conventions for rootnode runtime data (under `~/.rootnode/`), a passing mention that profile JSONs default to `~/.rootnode/profiles/` may be worth adding during a future catalog review — flagged here as forward-looking, not a v1.0.2 propagation requirement.

---

## Build note

Brand-strip revision per Phase 27/28 methodology absorption + the codified discipline lesson surfaced in `root_eval_4_cc_skills_phase30_review.md` (the brand-strip pass operates on the entire Skill folder, not just SKILL.md). Total scope: 9 mentions across SKILL.md (6 — description, body lines 29, 31, 53, 154, 157) and `examples/sample-interview-flow.md` (4 — lines 135, 136, 146, 147). All replaced with rootnode framing. The 8-dimension quality gate passed cleanly with all dimensions matching v1.0.1's prior review state. Description grew 938 → 942 chars (still 82 chars under the 1024 ceiling). Symptom-trigger additions deferred per the predecessor eval recommendation.

The 3 reference files (`schema-walking-patterns.md`, `common-schema-shapes.md`, `troubleshooting.md`) were inspected by full-folder grep and confirmed clean. The discipline lesson now has a confirmation point: full-folder scan caught zero additional surfaces beyond what the delta-eval flagged, which validates that future brand-strip revisions can proceed with the SKILL.md + named-folder-files scope rather than requiring deep reads of every reference.

---

*End of placement note. File to seed Project Drive at `Projects/ROOT/research/` for build provenance.*
