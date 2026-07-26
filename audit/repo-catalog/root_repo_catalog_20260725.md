# rootnode-skills — Repo Catalog
_Generated 2026-07-25T23:52:00Z | branch main | HEAD 3bff810_

Regenerated 2026-07-25 (local) per playbook Phase B step 10 (post-release-verification catalog regeneration). Structure matches `root_repo_catalog_20260724.md` so the two are diffable. Snapshot captures the v4.0 catalog release: 27 per-Skill v4.0 tags + `catalog-v4.0` umbrella carrying Latest, canonical-KFs roster 5 → 7 (D8 mirror completion), repo-root scripts roster 2 → 3 (`generate_release_notes.py` added at repo root per D7 expansion), and the new tracked `audit/v4_0-alignment/` cycle directory.

## Remote
```
origin	git@github.com:drayline/rootnode-skills.git (fetch)
origin	git@github.com:drayline/rootnode-skills.git (push)
```
## Tracked file tree (git ls-files)
```
.gitignore
CHANGELOG.md
CLAUDE.md
CONTRIBUTING.md
LICENSE
README.md
RELEASE_NOTES_TEMPLATE.md
assets/claude-code-layer.svg
assets/conversation-layer.svg
assets/global-layer.svg
assets/project-layer.svg
assets/rootnode-logo-dark.svg
audit/README.md
audit/build-artifacts/rootnode-cc-design/rootnode-cc-design_ap_warnings.md
audit/build-artifacts/rootnode-cc-design/rootnode-cc-design_install_instructions.md
audit/build-artifacts/rootnode-cc-design/rootnode-cc-design_placement_note.md
audit/build-artifacts/rootnode-cc-design/rootnode-cc-design_promotion_provenance.md
audit/build-artifacts/rootnode-critic-gate/rootnode-critic-gate_placement.md
audit/build-artifacts/rootnode-handoff-trigger-check/rootnode-handoff-trigger-check_placement.md
audit/build-artifacts/rootnode-mode-router/rootnode-mode-router_placement.md
audit/build-artifacts/rootnode-profile-builder/rootnode-profile-builder_placement.md
audit/build-artifacts/rootnode-repo-hygiene/rootnode-repo-hygiene_ap_warnings.md
audit/build-artifacts/rootnode-repo-hygiene/rootnode-repo-hygiene_placement.md
audit/build-artifacts/rootnode-repo-hygiene/rootnode-repo-hygiene_promotion_evidence.md
audit/build-artifacts/rootnode-skill-builder/rootnode-skill-builder_ap_warnings.md
audit/build-artifacts/rootnode-skill-builder/rootnode-skill-builder_placement.md
audit/build-artifacts/rootnode-skill-builder/rootnode-skill-builder_promotion_evidence.md
audit/canonical-kfs/root_AGENT_ANTI_PATTERNS.md
audit/canonical-kfs/root_AGENT_ENVIRONMENT_ARCHITECTURE.md
audit/canonical-kfs/root_AUDIT_FRAMEWORK.md
audit/canonical-kfs/root_CC_ENVIRONMENT_GUIDE.md
audit/canonical-kfs/root_CLAUDE_OPTIMIZATION_NOTES.md
audit/canonical-kfs/root_OPTIMIZATION_REFERENCE.md
audit/canonical-kfs/root_SKILL_BUILD_DISCIPLINE.md
audit/opus-4_8-alignment/halt-log.md
audit/opus-4_8-alignment/session-handoff-v2-validation.md
audit/opus-4_8-alignment/status.md
audit/phase-31c/SKILLS_AUDIT_REPORT.md
audit/phase-31d/AMENDMENT.md
audit/phase-31d/B2_CONFIRMATIONS.md
audit/phase-31d/CRITIC_GATE_ROOT_CAUSE.md
audit/phase-31d/PR_DESCRIPTION.md
audit/phase-31d/SKILLS_IMPACT_EVAL.md
audit/repo-catalog/REPO_CLAIM_RECONCILIATION.md
audit/repo-catalog/root_repo_catalog_20260627.md
audit/repo-catalog/root_repo_catalog_20260627_post-merge.md
audit/repo-catalog/root_repo_catalog_20260724.md
audit/v3_1-release/create_releases.py
audit/v3_1-release/generate_release_notes.py
audit/v3_1-release/root_canonical_drift_remediation_CHANGES.md
audit/v4_0-alignment/5GEN_SWEEP_MANIFEST.md
audit/v4_0-alignment/5GEN_VERIFICATION_LOG.md
audit/v4_0-alignment/dryrun-v3.1-config.py
audit/v4_0-alignment/release-notes-v4.0-config.py
build_release_artifacts.py
build_releases.py
design/audit-artifacts/v2.1/pr_body.md
design/audit-artifacts/v2.1/quality_gate_verdict.md
design/audit-artifacts/v2.1/rootnode-cc-design.zip
design/audit-artifacts/v2.1/rootnode-cc-design_placement.md
design/audit-artifacts/v2.1/rootnode-cc-design_promotion_evidence.md
design/audit-artifacts/v3.0/PHASE_32B_HALT.md
design/audit-artifacts/v3.0/pr_body.md
design/audit-artifacts/v3.0/quality_gate_verdict.md
design/audit-artifacts/v3.0/rootnode-skill-builder.zip
design/audit-artifacts/v3.0/rootnode-skill-builder_ap_warnings.md
design/audit-artifacts/v3.0/rootnode-skill-builder_placement.md
design/audit-artifacts/v3.0/rootnode-skill-builder_promotion_evidence.md
design/root_DS_cc_design_update_rev2.md
design/root_DS_skill_builder_v3_rev3.4.md
design/root_skill_5gen_alignment_design.md
docs/root_SKILLS_RELEASE_PLAYBOOK.md
generate_release_notes.py
prompts/root_skill_4_8_alignment_rubric.md
release-notes/catalog-v3.1.md
release-notes/catalog-v4.0.md
release-notes/rootnode-anti-pattern-detection-v3.1.md
release-notes/rootnode-anti-pattern-detection-v4.0.md
release-notes/rootnode-behavioral-tuning-v3.1.md
release-notes/rootnode-behavioral-tuning-v4.0.md
release-notes/rootnode-block-selection-v3.1.md
release-notes/rootnode-block-selection-v4.0.md
release-notes/rootnode-cc-design-v3.1.md
release-notes/rootnode-cc-design-v4.0.md
release-notes/rootnode-context-budget-v3.1.md
release-notes/rootnode-context-budget-v4.0.md
release-notes/rootnode-critic-gate-v3.1.md
release-notes/rootnode-critic-gate-v4.0.md
release-notes/rootnode-domain-agentic-context-v3.1.md
release-notes/rootnode-domain-agentic-context-v4.0.md
release-notes/rootnode-domain-business-strategy-v3.1.md
release-notes/rootnode-domain-business-strategy-v4.0.md
release-notes/rootnode-domain-content-communications-v3.1.md
release-notes/rootnode-domain-content-communications-v4.0.md
release-notes/rootnode-domain-research-analysis-v3.1.md
release-notes/rootnode-domain-research-analysis-v4.0.md
release-notes/rootnode-domain-software-engineering-v3.1.md
release-notes/rootnode-domain-software-engineering-v4.0.md
release-notes/rootnode-full-stack-audit-v3.1.md
release-notes/rootnode-full-stack-audit-v4.0.md
release-notes/rootnode-global-audit-v3.1.md
release-notes/rootnode-global-audit-v4.0.md
release-notes/rootnode-handoff-trigger-check-v3.1.md
release-notes/rootnode-handoff-trigger-check-v4.0.md
release-notes/rootnode-identity-blocks-v3.1.md
release-notes/rootnode-identity-blocks-v4.0.md
release-notes/rootnode-memory-optimization-v3.1.md
release-notes/rootnode-memory-optimization-v4.0.md
release-notes/rootnode-mode-router-v3.1.md
release-notes/rootnode-mode-router-v4.0.md
release-notes/rootnode-output-blocks-v3.1.md
release-notes/rootnode-output-blocks-v4.0.md
release-notes/rootnode-profile-builder-v3.1.md
release-notes/rootnode-profile-builder-v4.0.md
release-notes/rootnode-project-audit-v3.1.md
release-notes/rootnode-project-audit-v4.0.md
release-notes/rootnode-project-brief-v3.1.md
release-notes/rootnode-project-brief-v4.0.md
release-notes/rootnode-prompt-compilation-v3.1.md
release-notes/rootnode-prompt-compilation-v4.0.md
release-notes/rootnode-prompt-validation-v3.1.md
release-notes/rootnode-prompt-validation-v4.0.md
release-notes/rootnode-reasoning-blocks-v3.1.md
release-notes/rootnode-reasoning-blocks-v4.0.md
release-notes/rootnode-repo-hygiene-v3.1.md
release-notes/rootnode-repo-hygiene-v4.0.md
release-notes/rootnode-session-handoff-v3.1.md
release-notes/rootnode-session-handoff-v4.0.md
release-notes/rootnode-skill-builder-v3.1.md
release-notes/rootnode-skill-builder-v4.0.md
rootnode-anti-pattern-detection/SKILL.md
rootnode-behavioral-tuning/SKILL.md
rootnode-behavioral-tuning/references/countermeasure-templates.md
rootnode-block-selection/SKILL.md
rootnode-block-selection/references/domain-pack-index.md
rootnode-block-selection/references/identity-blocks.md
rootnode-block-selection/references/output-blocks.md
rootnode-block-selection/references/reasoning-blocks.md
rootnode-cc-design/SKILL.md
rootnode-cc-design/references/cc-anti-patterns.md
rootnode-cc-design/references/cc-environment-design-patterns.md
rootnode-cc-design/references/cc-methodology-patterns.md
rootnode-cc-design/references/cc-prompt-design-patterns.md
rootnode-cc-design/references/cc-skills-and-hooks-composition.md
rootnode-cc-design/references/chat-to-code-handoff-patterns.md
rootnode-cc-design/references/remediate-mode-execution.md
rootnode-cc-design/references/source-grading-and-tagging.md
rootnode-cc-design/references/troubleshooting.md
rootnode-cc-design/schema/cc-design-brief.schema.json
rootnode-cc-design/schema/execution-plan.schema.json
rootnode-context-budget/SKILL.md
rootnode-context-budget/references/compression-execution.md
rootnode-context-budget/references/content-routing.md
rootnode-context-budget/references/evaluation-rubric.md
rootnode-critic-gate/SKILL.md
rootnode-critic-gate/examples/worked-example.md
rootnode-critic-gate/profiles/balanced.json
rootnode-critic-gate/profiles/lenient.json
rootnode-critic-gate/profiles/strict.json
rootnode-critic-gate/references/checks-detailed.md
rootnode-critic-gate/references/severity-coverage.md
rootnode-critic-gate/references/troubleshooting.md
rootnode-critic-gate/schema/profile.schema.json
rootnode-domain-agentic-context/SKILL.md
rootnode-domain-agentic-context/references/output-formats.md
rootnode-domain-agentic-context/references/reasoning-approaches.md
rootnode-domain-business-strategy/SKILL.md
rootnode-domain-business-strategy/references/output-formats.md
rootnode-domain-business-strategy/references/reasoning-approaches.md
rootnode-domain-content-communications/SKILL.md
rootnode-domain-content-communications/references/output-formats.md
rootnode-domain-content-communications/references/reasoning-approaches.md
rootnode-domain-research-analysis/SKILL.md
rootnode-domain-research-analysis/references/examples.md
rootnode-domain-research-analysis/references/output-formats.md
rootnode-domain-research-analysis/references/reasoning-approaches.md
rootnode-domain-software-engineering/SKILL.md
rootnode-domain-software-engineering/references/output-formats.md
rootnode-domain-software-engineering/references/reasoning-approaches.md
rootnode-full-stack-audit/SKILL.md
rootnode-full-stack-audit/references/cross-layer-checks.md
rootnode-full-stack-audit/references/evolutionary-pathways.md
rootnode-full-stack-audit/references/global-layer-scorecard.md
rootnode-full-stack-audit/references/project-scorecard.md
rootnode-full-stack-audit/references/quality-criteria.md
rootnode-global-audit/SKILL.md
rootnode-global-audit/references/cross-layer-checks.md
rootnode-global-audit/references/evolutionary-pathways.md
rootnode-global-audit/references/global-layer-scorecard.md
rootnode-global-audit/references/preference-principles.md
rootnode-handoff-trigger-check/SKILL.md
rootnode-handoff-trigger-check/profiles/balanced.json
rootnode-handoff-trigger-check/profiles/lenient.json
rootnode-handoff-trigger-check/profiles/strict.json
rootnode-handoff-trigger-check/references/examples.md
rootnode-handoff-trigger-check/references/sensing-triggers-detailed.md
rootnode-handoff-trigger-check/references/troubleshooting.md
rootnode-handoff-trigger-check/schema/profile.schema.json
rootnode-identity-blocks/SKILL.md
rootnode-identity-blocks/references/communications-identities.md
rootnode-identity-blocks/references/operations-identities.md
rootnode-identity-blocks/references/research-identities.md
rootnode-identity-blocks/references/strategic-identities.md
rootnode-identity-blocks/references/technical-identities.md
rootnode-memory-optimization/SKILL.md
rootnode-memory-optimization/references/assessment-rubric.md
rootnode-memory-optimization/references/optimization-patterns.md
rootnode-mode-router/SKILL.md
rootnode-mode-router/configs/example-router.json
rootnode-mode-router/examples/routing-walkthrough.md
rootnode-mode-router/references/compound-trigger-semantics.md
rootnode-mode-router/references/trigger-types-detailed.md
rootnode-mode-router/references/troubleshooting.md
rootnode-mode-router/schema/router-config.schema.json
rootnode-output-blocks/SKILL.md
rootnode-output-blocks/references/analytical-formats.md
rootnode-output-blocks/references/executive-formats.md
rootnode-output-blocks/references/operational-formats.md
rootnode-output-blocks/references/technical-formats.md
rootnode-profile-builder/SKILL.md
rootnode-profile-builder/examples/sample-interview-flow.md
rootnode-profile-builder/references/common-schema-shapes.md
rootnode-profile-builder/references/schema-walking-patterns.md
rootnode-profile-builder/references/troubleshooting.md
rootnode-project-audit/SKILL.md
rootnode-project-audit/references/cross-layer-basics.md
rootnode-project-audit/references/diagnostic-questions.md
rootnode-project-audit/references/quality-criteria.md
rootnode-project-brief/SKILL.md
rootnode-project-brief/references/brief-template.md
rootnode-prompt-compilation/SKILL.md
rootnode-prompt-compilation/references/compilation-examples.md
rootnode-prompt-compilation/references/five-layer-architecture.md
rootnode-prompt-validation/SKILL.md
rootnode-prompt-validation/references/diagnostic-flow.md
rootnode-prompt-validation/references/symptom-fix-map.md
rootnode-reasoning-blocks/SKILL.md
rootnode-reasoning-blocks/references/analytical-reasoning.md
rootnode-reasoning-blocks/references/comparative-reasoning.md
rootnode-reasoning-blocks/references/creative-reasoning.md
rootnode-reasoning-blocks/references/research-reasoning.md
rootnode-reasoning-blocks/references/strategic-reasoning.md
rootnode-reasoning-blocks/references/technical-reasoning.md
rootnode-repo-hygiene/SKILL.md
rootnode-repo-hygiene/profiles/deep-audit.json
rootnode-repo-hygiene/profiles/default.json
rootnode-repo-hygiene/profiles/quick-scan.json
rootnode-repo-hygiene/references/anti-pattern-catalog.md
rootnode-repo-hygiene/references/cc-best-practices.md
rootnode-repo-hygiene/references/execution-discipline.md
rootnode-repo-hygiene/references/process-abstraction-detection.md
rootnode-repo-hygiene/references/seven-layer-framework.md
rootnode-repo-hygiene/references/sweep-categories.md
rootnode-repo-hygiene/references/worked-example.md
rootnode-repo-hygiene/schema/profile.schema.json
rootnode-session-handoff/SKILL.md
rootnode-session-handoff/references/closeout-checklist.md
rootnode-session-handoff/references/handoff-template.md
rootnode-skill-builder/SKILL.md
rootnode-skill-builder/agents/analyzer.md
rootnode-skill-builder/agents/comparator.md
rootnode-skill-builder/agents/grader.md
rootnode-skill-builder/eval-viewer/generate_review.py
rootnode-skill-builder/eval-viewer/viewer.html
rootnode-skill-builder/references/anti-pattern-catalog.md
rootnode-skill-builder/references/auto-activation-discipline.md
rootnode-skill-builder/references/behavioral-validation.md
rootnode-skill-builder/references/conversion-guide.md
rootnode-skill-builder/references/decomposition-framework.md
rootnode-skill-builder/references/description-optimization.md
rootnode-skill-builder/references/ecosystem-placement-decision.md
rootnode-skill-builder/references/multi-environment-adaptation.md
rootnode-skill-builder/references/skills-spec.md
rootnode-skill-builder/references/tooling-layer-overview.md
rootnode-skill-builder/references/version-comparison.md
rootnode-skill-builder/references/warrant-check-criteria.md
rootnode-skill-builder/scripts/__init__.py
rootnode-skill-builder/scripts/aggregate_benchmark.py
rootnode-skill-builder/scripts/description_optimizer.py
rootnode-skill-builder/scripts/generate_report.py
rootnode-skill-builder/scripts/package_zip.py
rootnode-skill-builder/scripts/quick_validate.py
rootnode-skill-builder/scripts/utils.py
```
Total tracked files: 283.

## canonical-kfs roster (7)
```
audit/canonical-kfs/root_AGENT_ANTI_PATTERNS.md
audit/canonical-kfs/root_AGENT_ENVIRONMENT_ARCHITECTURE.md
audit/canonical-kfs/root_AUDIT_FRAMEWORK.md
audit/canonical-kfs/root_CC_ENVIRONMENT_GUIDE.md
audit/canonical-kfs/root_CLAUDE_OPTIMIZATION_NOTES.md
audit/canonical-kfs/root_OPTIMIZATION_REFERENCE.md
audit/canonical-kfs/root_SKILL_BUILD_DISCIPLINE.md
```
Delta from `root_repo_catalog_20260724.md`: roster grew from 5 to 7. `root_AUDIT_FRAMEWORK.md` and `root_CLAUDE_OPTIMIZATION_NOTES.md` added per v4.0 D8 (mirror completion — the O10 staleness diff now covers 7 KFs rather than 5).

## audit/v4_0-alignment/ (v4.0 cycle directory)
```
audit/v4_0-alignment/5GEN_SWEEP_MANIFEST.md
audit/v4_0-alignment/5GEN_VERIFICATION_LOG.md
audit/v4_0-alignment/dryrun-v3.1-config.py
audit/v4_0-alignment/release-notes-v4.0-config.py
```
New tracked cycle directory per `audit/README.md` naming convention (`audit/v<N>_<M>-<kind>/`). Holds the v4.0 alignment cycle's Phase 0 verification log, sweep manifest, generate_release_notes.py dry-run config (mirrors v3.1 for verification), and v4.0 config used to generate the 27 per-Skill notes.

## Skills (rootnode-*/ source folders)
```
rootnode-anti-pattern-detection/
  SKILL.md
rootnode-behavioral-tuning/
  SKILL.md
  references/
rootnode-block-selection/
  SKILL.md
  references/
rootnode-cc-design/
  SKILL.md
  references/
  schema/
rootnode-context-budget/
  SKILL.md
  references/
rootnode-critic-gate/
  SKILL.md
  examples/
  profiles/
  references/
  schema/
rootnode-domain-agentic-context/
  SKILL.md
  references/
rootnode-domain-business-strategy/
  SKILL.md
  references/
rootnode-domain-content-communications/
  SKILL.md
  references/
rootnode-domain-research-analysis/
  SKILL.md
  references/
rootnode-domain-software-engineering/
  SKILL.md
  references/
rootnode-full-stack-audit/
  SKILL.md
  references/
rootnode-global-audit/
  SKILL.md
  references/
rootnode-handoff-trigger-check/
  SKILL.md
  profiles/
  references/
  schema/
rootnode-identity-blocks/
  SKILL.md
  references/
rootnode-memory-optimization/
  SKILL.md
  references/
rootnode-mode-router/
  SKILL.md
  configs/
  examples/
  references/
  schema/
rootnode-output-blocks/
  SKILL.md
  references/
rootnode-profile-builder/
  SKILL.md
  examples/
  references/
rootnode-project-audit/
  SKILL.md
  references/
rootnode-project-brief/
  SKILL.md
  references/
rootnode-prompt-compilation/
  SKILL.md
  references/
rootnode-prompt-validation/
  SKILL.md
  references/
rootnode-reasoning-blocks/
  SKILL.md
  references/
rootnode-repo-hygiene/
  SKILL.md
  profiles/
  references/
  schema/
rootnode-session-handoff/
  SKILL.md
  references/
rootnode-skill-builder/
  SKILL.md
  agents/
  eval-viewer/
  references/
  scripts/
```
Total: 27 Skill source folders (unchanged from prior snapshot). All 27 bumped to version 4.0.0 in this cycle.

## docs/
```
[tracked]
docs/root_SKILLS_RELEASE_PLAYBOOK.md
[on disk]
(none — no repo-root duplicate present)
```

## Repo-root scripts (3)
```
build_release_artifacts.py*    # release orchestrator (24 -cp flat + 5 -cc wrapper + bundle)
build_releases.py              # legacy flat-only half-tool (retained as reference)
generate_release_notes.py*     # v-agnostic release-notes generator (added v4.0, per D7 expansion)
```
Delta from `root_repo_catalog_20260724.md`: roster grew from 2 to 3. `generate_release_notes.py` was added at repo root per v4.0 D7 expansion — takes VERSION, TIER_LABEL, CATALOG_RELEASE, VARIANT_A/B/C, and EXPECTED_COUNTS from a per-cycle config file at `audit/v<N>-*/`; the prior v3.1-hardcoded artifact at `audit/v3_1-release/generate_release_notes.py` remains as historical (correct where it sits). Any tracked doc asserting the "two-script" repo-root roster is now stale — verify and correct in a follow-up hygiene PR.

## design/ structure
```
design
design/audit-artifacts
design/audit-artifacts/v2.1
design/audit-artifacts/v3.0
design/skill-creator
design/skill-creator/agents
design/skill-creator/assets
design/skill-creator/eval-viewer
design/skill-creator/references
design/skill-creator/scripts
design/staging-kf
[staging-kf on disk: empty, gitignored]
[tracked at design/ root: root_DS_cc_design_update_rev2.md, root_DS_skill_builder_v3_rev3.4.md, root_skill_5gen_alignment_design.md]
```
Delta from `root_repo_catalog_20260724.md`: `design/root_skill_5gen_alignment_design.md` is now tracked (was untracked in prior snapshot; committed on `release/v4.0` at 687954f, landed on main via PR #16). `design/staging-kf/` cleared post-sync (Phase 3.2 step 4) and remains gitignored.

## Recent commits (20)
```
3bff810 Merge pull request #16 from drayline/release/v4.0
a0f08e2 feat(release): v4.0 release notes — 27 per-Skill + catalog umbrella
0f4c00a chore(release): bump CATALOG_VERSION to v4.0 in build_release_artifacts.py
533cabb sync(canonical-kfs): v4.0 methodology updates + D8 mirror completion
65f6094 feat(release): W2c three-check corrections + version-agnostic release-notes generator
3ec65c1 feat(catalog): W2c completion — revert cc-design tier, complete D6 rebuild in context-budget
b891832 feat(catalog): W2b body-level D2 sweep completion
4b9012b feat(catalog): v4.0 W3/W0 methodology in reference files
60fee80 feat(catalog): v4.0 dual-primary calibration — markers, README, versions, Class-A descriptions
366a79f docs(playbook): close §6 debt items resolved in the v4.0 cycle
30a1556 audit(v4.0): Phase 0 verification log + sweep manifest
687954f docs(design): 5-generation alignment design v2.0 (Opus 5 revision)
a80c61e Merge pull request #15 from drayline/chore/repo-reconciliation
7c0c125 chore(repo): track catalog, correct package_skill.py claims, add regen step
a148eb9 Merge pull request #14 from drayline/phase-v3.1-propagation
9dc32df chore: sync canonical SBD — 4.7 surface-mapped release packaging
f8e6671 docs: add release playbook (root_SKILLS_RELEASE_PLAYBOOK.md)
10b612f docs: reconcile repo CLAUDE.md — surface-mapped packaging + notes-plus-bundle release model
6a739be Merge pull request #13 from drayline/fix/catalog-v3.1-bundle-and-links
0187892 Catalog v3.1: all-Skills bundle + fix umbrella/README install links
```

## Tags (90)
```
catalog-v3.0
catalog-v3.1
catalog-v4.0
cc-design/v2.1
cc-design/v3.0
rootnode-anti-pattern-detection/v3.0
rootnode-anti-pattern-detection/v3.1
rootnode-anti-pattern-detection/v4.0
rootnode-behavioral-tuning/v3.0
rootnode-behavioral-tuning/v3.1
rootnode-behavioral-tuning/v4.0
rootnode-block-selection/v3.0
rootnode-block-selection/v3.1
rootnode-block-selection/v4.0
rootnode-cc-design/v3.1
rootnode-cc-design/v4.0
rootnode-context-budget/v3.0
rootnode-context-budget/v3.1
rootnode-context-budget/v4.0
rootnode-critic-gate/v3.0
rootnode-critic-gate/v3.1
rootnode-critic-gate/v4.0
rootnode-domain-agentic-context/v3.0
rootnode-domain-agentic-context/v3.1
rootnode-domain-agentic-context/v4.0
rootnode-domain-business-strategy/v3.0
rootnode-domain-business-strategy/v3.1
rootnode-domain-business-strategy/v4.0
rootnode-domain-content-communications/v3.0
rootnode-domain-content-communications/v3.1
rootnode-domain-content-communications/v4.0
rootnode-domain-research-analysis/v3.0
rootnode-domain-research-analysis/v3.1
rootnode-domain-research-analysis/v4.0
rootnode-domain-software-engineering/v3.0
rootnode-domain-software-engineering/v3.1
rootnode-domain-software-engineering/v4.0
rootnode-full-stack-audit/v3.0
rootnode-full-stack-audit/v3.1
rootnode-full-stack-audit/v4.0
rootnode-global-audit/v3.0
rootnode-global-audit/v3.1
rootnode-global-audit/v4.0
rootnode-handoff-trigger-check/v3.0
rootnode-handoff-trigger-check/v3.1
rootnode-handoff-trigger-check/v4.0
rootnode-identity-blocks/v3.0
rootnode-identity-blocks/v3.1
rootnode-identity-blocks/v4.0
rootnode-memory-optimization/v3.0
rootnode-memory-optimization/v3.1
rootnode-memory-optimization/v4.0
rootnode-mode-router/v3.0
rootnode-mode-router/v3.1
rootnode-mode-router/v4.0
rootnode-output-blocks/v3.0
rootnode-output-blocks/v3.1
rootnode-output-blocks/v4.0
rootnode-profile-builder/v3.0
rootnode-profile-builder/v3.1
rootnode-profile-builder/v4.0
rootnode-project-audit/v3.0
rootnode-project-audit/v3.1
rootnode-project-audit/v4.0
rootnode-project-brief/v3.0
rootnode-project-brief/v3.1
rootnode-project-brief/v4.0
rootnode-prompt-compilation/v3.0
rootnode-prompt-compilation/v3.1
rootnode-prompt-compilation/v4.0
rootnode-prompt-validation/v3.0
rootnode-prompt-validation/v3.1
rootnode-prompt-validation/v4.0
rootnode-reasoning-blocks/v3.0
rootnode-reasoning-blocks/v3.1
rootnode-reasoning-blocks/v4.0
rootnode-repo-hygiene/v3.0
rootnode-repo-hygiene/v3.1
rootnode-repo-hygiene/v4.0
rootnode-session-handoff/v3.0
rootnode-session-handoff/v3.1
rootnode-session-handoff/v4.0
rootnode-skill-builder/v3.1
rootnode-skill-builder/v4.0
skill-builder/v3.0
v1.0
v1.1
v1.2
v2.0.0
v2.1
```
Delta from `root_repo_catalog_20260724.md`: 28 new tags added (27 `rootnode-<skill>/v4.0` + `catalog-v4.0`). Total 90 (was 62). The uniform `rootnode-<skill>/v4.0` naming convention holds — no prefix-less variants at v4.0 (the historical v3.0 asymmetry with `skill-builder/v3.0` and `cc-design/v3.0` / `cc-design/v2.1` is closed and stays closed).

## GitHub releases
```
catalog-v4.0	Latest	catalog-v4.0	2026-07-25T23:35:30Z
rootnode-skill-builder/v4.0		rootnode-skill-builder/v4.0	2026-07-25T23:35:12Z
rootnode-session-handoff/v4.0		rootnode-session-handoff/v4.0	2026-07-25T23:35:10Z
rootnode-repo-hygiene/v4.0		rootnode-repo-hygiene/v4.0	2026-07-25T23:35:08Z
rootnode-reasoning-blocks/v4.0		rootnode-reasoning-blocks/v4.0	2026-07-25T23:35:06Z
rootnode-prompt-validation/v4.0		rootnode-prompt-validation/v4.0	2026-07-25T23:35:03Z
rootnode-prompt-compilation/v4.0		rootnode-prompt-compilation/v4.0	2026-07-25T23:35:01Z
rootnode-project-brief/v4.0		rootnode-project-brief/v4.0	2026-07-25T23:34:59Z
rootnode-project-audit/v4.0		rootnode-project-audit/v4.0	2026-07-25T23:34:57Z
rootnode-profile-builder/v4.0		rootnode-profile-builder/v4.0	2026-07-25T23:34:55Z
rootnode-output-blocks/v4.0		rootnode-output-blocks/v4.0	2026-07-25T23:34:52Z
rootnode-mode-router/v4.0		rootnode-mode-router/v4.0	2026-07-25T23:34:50Z
rootnode-memory-optimization/v4.0		rootnode-memory-optimization/v4.0	2026-07-25T23:34:48Z
rootnode-identity-blocks/v4.0		rootnode-identity-blocks/v4.0	2026-07-25T23:34:46Z
rootnode-handoff-trigger-check/v4.0		rootnode-handoff-trigger-check/v4.0	2026-07-25T23:34:44Z
rootnode-global-audit/v4.0		rootnode-global-audit/v4.0	2026-07-25T23:34:42Z
rootnode-full-stack-audit/v4.0		rootnode-full-stack-audit/v4.0	2026-07-25T23:34:40Z
rootnode-domain-software-engineering/v4.0		rootnode-domain-software-engineering/v4.0	2026-07-25T23:34:38Z
rootnode-domain-research-analysis/v4.0		rootnode-domain-research-analysis/v4.0	2026-07-25T23:34:36Z
rootnode-domain-content-communications/v4.0		rootnode-domain-content-communications/v4.0	2026-07-25T23:34:34Z
rootnode-domain-business-strategy/v4.0		rootnode-domain-business-strategy/v4.0	2026-07-25T23:34:32Z
rootnode-domain-agentic-context/v4.0		rootnode-domain-agentic-context/v4.0	2026-07-25T23:34:30Z
rootnode-critic-gate/v4.0		rootnode-critic-gate/v4.0	2026-07-25T23:34:28Z
rootnode-context-budget/v4.0		rootnode-context-budget/v4.0	2026-07-25T23:34:26Z
rootnode-cc-design/v4.0		rootnode-cc-design/v4.0	2026-07-25T23:34:24Z
rootnode-block-selection/v4.0		rootnode-block-selection/v4.0	2026-07-25T23:34:21Z
rootnode-behavioral-tuning/v4.0		rootnode-behavioral-tuning/v4.0	2026-07-25T23:34:19Z
rootnode-anti-pattern-detection/v4.0		rootnode-anti-pattern-detection/v4.0	2026-07-25T23:34:17Z
Catalog v3.1		catalog-v3.1	2026-06-26T06:08:13Z
rootnode-cc-design v3.1		rootnode-cc-design/v3.1	2026-06-26T05:24:16Z
rootnode-skill-builder v3.1		rootnode-skill-builder/v3.1	2026-06-26T05:24:14Z
rootnode-repo-hygiene v3.1		rootnode-repo-hygiene/v3.1	2026-06-26T05:24:12Z
rootnode-mode-router v3.1		rootnode-mode-router/v3.1	2026-06-26T05:24:10Z
rootnode-critic-gate v3.1		rootnode-critic-gate/v3.1	2026-06-26T05:24:08Z
rootnode-domain-agentic-context v3.1		rootnode-domain-agentic-context/v3.1	2026-06-26T05:24:06Z
rootnode-domain-research-analysis v3.1		rootnode-domain-research-analysis/v3.1	2026-06-26T05:24:04Z
rootnode-domain-content-communications v3.1		rootnode-domain-content-communications/v3.1	2026-06-26T05:24:02Z
rootnode-domain-business-strategy v3.1		rootnode-domain-business-strategy/v3.1	2026-06-26T05:24:00Z
rootnode-domain-software-engineering v3.1		rootnode-domain-software-engineering/v3.1	2026-06-26T05:23:58Z
rootnode-block-selection v3.1		rootnode-block-selection/v3.1	2026-06-26T05:23:56Z
rootnode-output-blocks v3.1		rootnode-output-blocks/v3.1	2026-06-26T05:23:54Z
rootnode-reasoning-blocks v3.1		rootnode-reasoning-blocks/v3.1	2026-06-26T05:23:51Z
rootnode-identity-blocks v3.1		rootnode-identity-blocks/v3.1	2026-06-26T05:23:49Z
rootnode-profile-builder v3.1		rootnode-profile-builder/v3.1	2026-06-26T05:23:47Z
rootnode-handoff-trigger-check v3.1		rootnode-handoff-trigger-check/v3.1	2026-06-26T05:23:45Z
rootnode-session-handoff v3.1		rootnode-session-handoff/v3.1	2026-06-26T05:23:43Z
rootnode-full-stack-audit v3.1		rootnode-full-stack-audit/v3.1	2026-06-26T05:23:41Z
rootnode-global-audit v3.1		rootnode-global-audit/v3.1	2026-06-26T05:23:39Z
rootnode-context-budget v3.1		rootnode-context-budget/v3.1	2026-06-26T05:23:36Z
rootnode-memory-optimization v3.1		rootnode-memory-optimization/v3.1	2026-06-26T05:23:34Z
rootnode-behavioral-tuning v3.1		rootnode-behavioral-tuning/v3.1	2026-06-26T05:23:32Z
rootnode-anti-pattern-detection v3.1		rootnode-anti-pattern-detection/v3.1	2026-06-26T05:23:30Z
rootnode-project-brief v3.1		rootnode-project-brief/v3.1	2026-06-26T05:23:28Z
rootnode-project-audit v3.1		rootnode-project-audit/v3.1	2026-06-26T05:23:26Z
rootnode-prompt-validation v3.1		rootnode-prompt-validation/v3.1	2026-06-26T05:23:24Z
rootnode-prompt-compilation v3.1		rootnode-prompt-compilation/v3.1	2026-06-26T05:23:22Z
Catalog v3.0		catalog-v3.0	2026-05-14T13:28:06Z
rootnode-repo-hygiene v3.0		rootnode-repo-hygiene/v3.0	2026-05-10T16:08:07Z
rootnode-mode-router v3.0		rootnode-mode-router/v3.0	2026-05-10T16:08:04Z
rootnode-critic-gate v3.0		rootnode-critic-gate/v3.0	2026-05-10T16:08:00Z
```
Delta from `root_repo_catalog_20260724.md`: `catalog-v4.0` created and marked Latest. `Catalog v3.1` no longer carries the Latest marker (correctly demoted when `--latest` moved to v4.0). All 27 per-Skill v4.0 releases created; none marked Latest.

## release-notes/ v4.0 files
```
release-notes/catalog-v4.0.md
release-notes/rootnode-anti-pattern-detection-v4.0.md
release-notes/rootnode-behavioral-tuning-v4.0.md
release-notes/rootnode-block-selection-v4.0.md
release-notes/rootnode-cc-design-v4.0.md
release-notes/rootnode-context-budget-v4.0.md
release-notes/rootnode-critic-gate-v4.0.md
release-notes/rootnode-domain-agentic-context-v4.0.md
release-notes/rootnode-domain-business-strategy-v4.0.md
release-notes/rootnode-domain-content-communications-v4.0.md
release-notes/rootnode-domain-research-analysis-v4.0.md
release-notes/rootnode-domain-software-engineering-v4.0.md
release-notes/rootnode-full-stack-audit-v4.0.md
release-notes/rootnode-global-audit-v4.0.md
release-notes/rootnode-handoff-trigger-check-v4.0.md
release-notes/rootnode-identity-blocks-v4.0.md
release-notes/rootnode-memory-optimization-v4.0.md
release-notes/rootnode-mode-router-v4.0.md
release-notes/rootnode-output-blocks-v4.0.md
release-notes/rootnode-profile-builder-v4.0.md
release-notes/rootnode-project-audit-v4.0.md
release-notes/rootnode-project-brief-v4.0.md
release-notes/rootnode-prompt-compilation-v4.0.md
release-notes/rootnode-prompt-validation-v4.0.md
release-notes/rootnode-reasoning-blocks-v4.0.md
release-notes/rootnode-repo-hygiene-v4.0.md
release-notes/rootnode-session-handoff-v4.0.md
release-notes/rootnode-skill-builder-v4.0.md
```
28 files added this cycle: 27 per-Skill v4.0 notes + 1 catalog umbrella (`catalog-v4.0.md`). Generated via `generate_release_notes.py` (per-Skill) + hand-authored umbrella. v3.1 notes preserved (append-only for shipped releases).

## CATALOG_VERSION
`build_release_artifacts.py:59` — `CATALOG_VERSION = "v4.0"` (was `"v3.1"` in prior snapshot; single-line change per D7 authorization; bundle output `dist/rootnode-catalog-v4.0.zip`).

## Cycle-delta summary vs `root_repo_catalog_20260724.md`

- **canonical-kfs roster: 5 → 7.** `root_AUDIT_FRAMEWORK.md` + `root_CLAUDE_OPTIMIZATION_NOTES.md` added (D8).
- **Repo-root scripts: 2 → 3.** `generate_release_notes.py` added (D7 expansion).
- **audit/v4_0-alignment/: newly tracked.** 2 logs + 2 configs.
- **design/root_skill_5gen_alignment_design.md: newly tracked.**
- **release-notes/: +28 files.** 27 per-Skill v4.0 + `catalog-v4.0.md` umbrella.
- **build_release_artifacts.py CATALOG_VERSION: `"v3.1"` → `"v4.0"`.**
- **Tags: 62 → 90 (+28).** 27 per-Skill `rootnode-<skill>/v4.0` + `catalog-v4.0`.
- **GitHub releases: `catalog-v4.0` Latest.** `catalog-v3.1` demoted. 27 per-Skill v4.0 releases.
- **design/staging-kf/: cleared post-sync, remains gitignored.**
