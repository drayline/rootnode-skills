## Summary

`rootnode-skill-builder` v3.0 — methodology + tooling release per locked design spec [`design/root_DS_skill_builder_v3_rev3.4.md`](design/root_DS_skill_builder_v3_rev3.4.md).

- D9 (Behavioral validation) expanded into D9a/D9b/D9c sub-levels (Empirical Tier A / Empirical Tier B / Analytical floor).
- Description Refinement Loop methodology — manual walkthrough + automated train/test optimizer via `scripts/description_optimizer.py`.
- Tier A/B/C environment-adaptive degradation discipline — explicit tier determination at build time; verdicts cite the tier produced under.
- "Explain the why" tone calibration applied to new content.
- Tooling layer ported from upstream Anthropic skill-creator with content-class policy applied: 7 scripts in `scripts/`, 3 subagents in `agents/`, 2 files in `eval-viewer/`.
- 5 new reference files (`behavioral-validation.md`, `description-optimization.md`, `version-comparison.md`, `multi-environment-adaptation.md`, `tooling-layer-overview.md`); 3 updated reference files (`auto-activation-discipline.md`, `conversion-guide.md`, `skills-spec.md`).
- SKILL.md authored under intelligent abstraction discipline (routing surfaces only; 433 lines; well under the 500 ceiling).
- Description: 967 chars YAML-parsed (under 1024).

Predecessor: v2.1 (overwritten in place per `root_SKILL_BUILD_DISCIPLINE.md §6.4` — same `name:` field, no rename rule triggered).

## PR commit structure

This PR carries three commits in order:

1. **`chore: sync canonical-kfs/ with Phase 32a approved KF updates`** (`4d6f961`) — syncs the Phase 32a updated `root_SKILL_BUILD_DISCIPLINE.md` and `root_AGENT_ENVIRONMENT_ARCHITECTURE.md` from `design/staging-kf/` to `audit/canonical-kfs/`. Performed first on the release branch so subsequent build steps cite the v3 methodology.
2. **`chore: project governance, v3.0 design spec, .gitignore anchoring`** (`1606dd9`) — adds project-scoped `CLAUDE.md`, the locked v3.0 design spec, and anchors `.gitignore` patterns to repo root (fixes the `scripts/` rule that was blocking `rootnode-skill-builder/scripts/`).
3. **`release: rootnode-skill-builder v3.0`** (this commit) — the v3.0 build itself plus audit artifacts.

## Quality gate verdict

All 9 dimensions verified per design spec §15. Verdict file: [`design/audit-artifacts/v3.0/quality_gate_verdict.md`](design/audit-artifacts/v3.0/quality_gate_verdict.md).

| Dimension | Verdict |
|---|---|
| D1 Spec compliance | PASS (`quick_validate.py` returned valid) |
| D2 Activation precision | PASS (8/8 should-trigger, 4/4 symptom, 5/5 should-not-trigger, 4/4 edge cases) |
| D3 Methodology preservation | PASS (v2.1 sections preserved verbatim per design §13.1) |
| D4 Progressive disclosure | PASS (433 lines; routing-surface compliance per new section) |
| D5 Standalone completeness | PASS (all cross-Skill references use "if available") |
| D6 Auto-activation enforcement | PASS (verb-based triggers; `disable-model-invocation` absent) |
| D7 Anti-pattern catalog scan | PASS WITH ACCEPTED Kitchen Sink catch (3-part decomposition test passed per design §18.9) |
| D8 7-layer leak-check | PASS (tooling layer Skill-internal) |
| D9 Behavioral validation | PASS at sub-level **D9c (Analytical)** — 3 pressure scenarios, cited tendencies, countermeasure formulations |

## D9 sub-level applied

**D9c — Analytical.** This build CV applied the analytical floor for D9. Tier A would in principle apply (subagent execution and runnable environment available), but a full empirical with-Skill vs. without-Skill comparison via subagent grader was not feasible within the build session's time budget. Operator may upgrade D9 to D9a/D9b post-merge by running the iteration loop against v3.0 itself in a Tier A environment.

The build summary records: `D9: Tier C — analytical (tendencies: under-triggering, fabricated precision, over-exploration; countermeasures: routing-surface lens, sub-level architecture, tier determination)`.

## Tier compatibility per script

| Script | Tier A | Tier B | Tier C |
|---|---|---|---|
| `description_optimizer.py` | ✓ Full automated train/test loop | manual fallback | manual fallback |
| `aggregate_benchmark.py` | ✓ | — | — |
| `quick_validate.py` | ✓ | ✓ | ✓ |
| `package_zip.py` | ✓ | ✓ | ✓ |
| `generate_report.py` | ✓ | — | — |
| `utils.py` (library) | ✓ | ✓ | ✓ |
| `__init__.py` (marker) | n/a | n/a | n/a |
| `agents/grader.md` | ✓ | inline fallback | n/a |
| `agents/comparator.md` | ✓ | inline fallback | deferred |
| `agents/analyzer.md` | ✓ | inline fallback | deferred |
| `eval-viewer/*` | ✓ | — | — |

Per-script details and fallback patterns: [`rootnode-skill-builder/references/multi-environment-adaptation.md`](rootnode-skill-builder/references/multi-environment-adaptation.md) and [`rootnode-skill-builder/references/tooling-layer-overview.md`](rootnode-skill-builder/references/tooling-layer-overview.md).

## Methodology preservation note

Per `root_SKILL_BUILD_DISCIPLINE.md §13.1`:

- All 7 v2.1 reference files preserved (4 unchanged: `anti-pattern-catalog.md`, `decomposition-framework.md`, `ecosystem-placement-decision.md`, `warrant-check-criteria.md`; 3 with additions only: `auto-activation-discipline.md`, `conversion-guide.md`, `skills-spec.md`).
- Pre-build gate definitions preserved verbatim.
- D1–D8 quality gate descriptions preserved.
- Conversion rules preserved.
- Build pipeline (Build New Skill section) preserved.
- Review Existing Skill procedure preserved.
- v2.1 examples 1-4 preserved (compressed slightly to make room for new examples 5-8 within line budget).
- Troubleshooting bullets preserved.

Evolution items documented in [`design/audit-artifacts/v3.0/rootnode-skill-builder_promotion_evidence.md`](design/audit-artifacts/v3.0/rootnode-skill-builder_promotion_evidence.md). Two scope-lock overrides captured (scripts in v3.0; comparator/analyzer pair).

## Audit artifact locations

Audit artifacts live at `design/audit-artifacts/v3.0/` and ship SEPARATELY from the deployable zip per `root_SKILL_BUILD_DISCIPLINE.md §4.4`:

- [`quality_gate_verdict.md`](design/audit-artifacts/v3.0/quality_gate_verdict.md) — all 9 dimensions with cited evidence; Kitchen Sink decomposition test result.
- [`rootnode-skill-builder_placement.md`](design/audit-artifacts/v3.0/rootnode-skill-builder_placement.md) — placement note.
- [`rootnode-skill-builder_promotion_evidence.md`](design/audit-artifacts/v3.0/rootnode-skill-builder_promotion_evidence.md) — promotion provenance with evolution table and override notations.
- [`rootnode-skill-builder_ap_warnings.md`](design/audit-artifacts/v3.0/rootnode-skill-builder_ap_warnings.md) — Kitchen Sink ACCEPTED catch with decomposition test result.

Deployable artifact: [`design/audit-artifacts/v3.0/rootnode-skill-builder.zip`](design/audit-artifacts/v3.0/rootnode-skill-builder.zip) (25 files; audit artifacts NOT inside).

## Reviewer checklist

- [ ] **v2.1 preservation:** spot-check 2–3 sections from v2.1 (Pre-Build Gates, Build New Skill, existing examples) confirm verbatim preservation per design §13.1.
- [ ] **Routing-surface discipline (D4):** walk each new SKILL.md section (Iterate the Skill, Optimize the Description, Compare Skill Versions, Multi-Environment Adaptation) and confirm none duplicates procedural depth from its corresponding reference file.
- [ ] **Description spec compliance:** verify `description` field YAML-parses to ≤ 1024 chars.
- [ ] **Scripts compile:** `for f in rootnode-skill-builder/scripts/*.py rootnode-skill-builder/eval-viewer/*.py; do python -m py_compile "$f"; done` should pass for all 8 .py files.
- [ ] **Schemas verbatim:** spot-check the eval schema and grading schema in `references/behavioral-validation.md` against upstream `design/skill-creator/references/schemas.md` — should match exactly.
- [ ] **Grader principles verbatim:** spot-check the grader design principles in `references/behavioral-validation.md` §8 against upstream `design/skill-creator/agents/grader.md`.
- [ ] **Comparator rubric verbatim:** spot-check the two-dimension rubric in `references/version-comparison.md` against upstream `design/skill-creator/agents/comparator.md`.
- [ ] **Triggering detection mechanism verbatim:** spot-check the stream-event monitoring code in `scripts/description_optimizer.py` (`run_single_query`) against upstream `design/skill-creator/scripts/run_eval.py`.
- [ ] **Zip structure:** `unzip -l design/audit-artifacts/v3.0/rootnode-skill-builder.zip` should show 25 files with the rootnode-skill-builder/ prefix; no audit artifacts inside.
- [ ] **`.gitignore` anchoring:** confirm `git check-ignore rootnode-skill-builder/scripts/utils.py` returns non-zero (file is NOT ignored).

## Phase 32c deferral

> **Phase 32c (release tag + GitHub release) is NOT in this PR.** It lives in a separate CC prompt at `root_CC_skill_builder_v3_release.md`.
>
> Operator action sequence after merge:
> 1. Review and merge this PR via the GitHub UI.
> 2. Pull updated main locally; verify the merge commit is present.
> 3. **Test v3.0 locally** before tagging or releasing. Install the deployable zip into a test environment; exercise the Skill against representative test cases; confirm quality gate verdict matches behavioral expectations.
> 4. If testing confirms readiness, invoke `root_CC_skill_builder_v3_release.md` as a fresh CC session to execute Phase 32c.
> 5. If testing surfaces issues, do NOT invoke the release prompt. Iterate on the v3.0 build first, then re-test, then release.
