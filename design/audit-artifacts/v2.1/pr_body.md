## Summary

This PR will land `rootnode-cc-design` v2.1 on `main`. After merge, the cc-design Skill will carry:

- A refined frontmatter description (1009/1024 chars, 15 chars headroom) with three new prompt-specific triggers — `"build a CC prompt"`, `"design a CC prompt for X"`, `"write a session prompt"` — closing the activation gap surfaced 2026-05-06.
- A new section 10, "Output discipline for CC prompts," in `references/cc-prompt-design-patterns.md` with four empirically-grounded bullets: shell-agnostic command syntax, pre-flight Skill enumeration, continuation-phrase ambiguity gate, and forward-state-aware artifact authoring.
- A single Step 4 routing bullet in `SKILL.md` pointing to that section. Step 4 stays at six bullets total; procedural depth lives in references per the intelligent-abstraction principle (`audit/canonical-kfs/root_SKILL_BUILD_DISCIPLINE.md §3.4`).
- `metadata.version: "2.1"` and `metadata.predecessor: "rootnode-cc-design v2.0"`.

The build is purely additive — no v2.0 methodology was removed. Two REMEDIATE-mode triggers (`"fix the audit issues"`, `"close the loop on the report"`) were dropped to rebalance the description; the most semantically distinct REMEDIATE trigger (`"remediate the hygiene findings"`) was retained.

## Build path and provenance

Path B (CC session, single-phase). No `audit/canonical-kfs/` sync — cc-design v2.0 cites generic AEA/SBD principles, not the §4.11+/§10 content that the v3.0 release reshaped, so canonical-KF inheritance is clean.

- **Source spec:** `design/root_DS_cc_design_update_rev2.md` (committed in this PR).
- **Build CV:** rootnode-skill-builder v3.0.
- **Empirical grounding:** Phase 31d merge prompt execution (2026-05-06), Phase 32a/b v3.0 build execution (2026-05-07/08).
- **Build branch:** `feature/cc-design-v2.1`.

## Quality gate verdict

All nine D-dimensions PASS at Tier B (runnable execution, no subagents). No D7 anti-pattern catches. No 7-layer leaks. Cross-references verified against canonical KFs at authoring (R5 pre-flight checklist; AEA §4.7 halt-and-escalate). Two of the four new bullets carry inline `[generalizable: ...]` source tags rather than canonical-KF cross-refs because no canonical section yet codifies those disciplines — empirical grounding is sufficient.

D9 recorded at Tier B per locked design decision 8 — this CC session has runnable execution but does not invoke skill-builder's Tier A subagent pipeline.

Full per-dimension evidence in `design/audit-artifacts/v2.1/quality_gate_verdict.md`.

## Files changed

- `rootnode-cc-design/SKILL.md` — frontmatter description rewrite; metadata version + predecessor; one new Step 4 routing bullet.
- `rootnode-cc-design/references/cc-prompt-design-patterns.md` — TOC entry for section 10; new section 10 with four sub-bullets.
- `design/root_DS_cc_design_update_rev2.md` — source spec, committed in this PR.
- `design/audit-artifacts/v2.1/quality_gate_verdict.md` — D1–D9 verdicts.
- `design/audit-artifacts/v2.1/rootnode-cc-design_placement.md` — Gate 3 placement note.
- `design/audit-artifacts/v2.1/rootnode-cc-design_promotion_evidence.md` — Gate 2 warrant evidence.
- `design/audit-artifacts/v2.1/pr_body.md` — this body.
- `design/audit-artifacts/v2.1/rootnode-cc-design.zip` — wrapper-format zip (PR evidence; not a release asset — Phase 32c-equivalent for cc-design is a separate cycle).

`rootnode-cc-design_ap_warnings.md` is intentionally absent — D7 surfaced no catches.

## Test plan

- [x] D1 spec compliance — name format, description length, body length, no XML, no README, folder/name match, metadata fields.
- [x] D2 activation precision — 10 triggers; verb-based; explicit + symptom-phrased; negative triggers preserved; no collision with adjacent Skills.
- [x] D3 methodology preservation — additive build; v2.0 modes/protocols unchanged.
- [x] D4 progressive disclosure — depth in references §10; Step 4 routing surface only; cross-references resolve to verified canonical sections.
- [x] D5 standalone completeness — no new cross-Skill refs; existing soft pointers preserved.
- [x] D6 auto-activation enforcement — no `disable-model-invocation`; verb-based triggers.
- [x] D7 anti-pattern scan — no catches in new content.
- [x] D8 7-layer leak-check — new content lands in correct layer (Skill-level methodology, not CLAUDE.md/rules/hooks/MCP).
- [x] D9 Tier B qualitative review — new triggers pattern-match the empirical missed-activation phrasing; section content empirically grounded in dated sessions.

Operator-side post-merge actions (not part of this PR):

- Re-enable `rootnode-cc-design` in CC Settings → Skills.
- Reinstall the personal `~/.claude/skills/rootnode-cc-design/` from the v2.1 source (or from the wrapper-format zip in this PR's evidence directory).

## Halt-and-escalate triggers fired during build

None.
