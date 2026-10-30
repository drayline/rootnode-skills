# rootnode-skills — Repo Catalog
_Generated 2026-10-30 | HEAD 2c04b7035f438609360f60c599e8f3e599bb8ec8 (merge of PR #28, release/v5.0.1) | regenerated per playbook Post-verification step_

Regenerated 2026-10-30 per `docs/root_SKILLS_RELEASE_PLAYBOOK.md` §Post-verification, after Phase B of the catalog v5.0.1 patch cut (playbook §1.6 patch shape). Section structure matches `root_repo_catalog_20261023.md` so the two are diffable; the cycle-directory sections add `audit/v5_0_1-patch/` (new) and keep `audit/v5_0-alignment/` and `audit/v4_0-alignment/`, and the release-notes section tracks v5.0.1 files. This snapshot captures the patch cut: 12 per-Skill releases `rootnode-<skill>/v5.0.1` (`--latest=false`) for the Skills that changed, and the `catalog-v5.0.1` umbrella (`--latest`, bundle `rootnode-catalog-v5.0.1.zip` carrying all 29 artifacts at their current versions), all tagged at the merge commit. The 15 unchanged Skills keep their `/v5.0` releases. Every section derives from a live command run at HEAD `2c04b70`, named next to the section title; deltas are against `root_repo_catalog_20261023.md` (HEAD `12e9c2f`).

## Remote
_Source: `git remote -v`_
```
origin	git@github.com:drayline/rootnode-skills.git (fetch)
origin	git@github.com:drayline/rootnode-skills.git (push)
```

## Tracked file tree (git ls-files)
_Source: `git ls-files`; count via `git ls-files | wc -l`_
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
audit/repo-catalog/root_repo_catalog_20260725.md
audit/repo-catalog/root_repo_catalog_20260911.md
audit/repo-catalog/root_repo_catalog_20260913.md
audit/repo-catalog/root_repo_catalog_20261023.md
audit/v3_1-release/create_releases.py
audit/v3_1-release/generate_release_notes.py
audit/v3_1-release/root_canonical_drift_remediation_CHANGES.md
audit/v4_0-alignment/5GEN_SWEEP_MANIFEST.md
audit/v4_0-alignment/5GEN_VERIFICATION_LOG.md
audit/v4_0-alignment/dryrun-v3.1-config.py
audit/v4_0-alignment/release-notes-v4.0-config.py
audit/v5_0-alignment/5_5GEN_SWEEP_MANIFEST.md
audit/v5_0-alignment/d9a_cc-design_v5.0_20261029-1406Z.md
audit/v5_0-alignment/kf-update-blocks.md
audit/v5_0-alignment/pr_body.md
audit/v5_0-alignment/release-notes-v5.0-config.py
audit/v5_0-alignment/session_report_20261023-0042Z.md
audit/v5_0_1-patch/refuter_brief_c1.md
audit/v5_0_1-patch/refuter_brief_r2c1.md
audit/v5_0_1-patch/refuter_c1.json
audit/v5_0_1-patch/refuter_r2c1.json
audit/v5_0_1-patch/release-notes-v5.0.1-config.py
audit/v5_0_1-patch/session_report_20261030-0040Z.md
audit/v5_0_1-patch/session_report_20261030-0107Z.md
audit/v5_0_1-patch/session_report_20261030-0224Z.md
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
design/audit-artifacts/v4.2/root_CC_DESIGN_v42_spec.md
design/audit-artifacts/v4.2/root_CC_LANDSCAPE_20260911.md
design/audit-artifacts/v4.2/v42_inventory_report.md
design/audit-artifacts/v5.0/d9a/d9a_runner.py
design/audit-artifacts/v5.0/d9a/out/exec.json
design/audit-artifacts/v5.0/d9a/out/grading/C1.json
design/audit-artifacts/v5.0/d9a/out/grading/C2.json
design/audit-artifacts/v5.0/d9a/out/grading/C3.json
design/audit-artifacts/v5.0/d9a/out/grading/C4.json
design/audit-artifacts/v5.0/d9a/out/grading/C5.json
design/audit-artifacts/v5.0/d9a/out/grading/C6.json
design/audit-artifacts/v5.0/d9a/out/probe.json
design/audit-artifacts/v5.0/d9a/out/runs/v4.2/C1.json
design/audit-artifacts/v5.0/d9a/out/runs/v4.2/C1.md
design/audit-artifacts/v5.0/d9a/out/runs/v4.2/C2.json
design/audit-artifacts/v5.0/d9a/out/runs/v4.2/C2.md
design/audit-artifacts/v5.0/d9a/out/runs/v4.2/C3.json
design/audit-artifacts/v5.0/d9a/out/runs/v4.2/C3.md
design/audit-artifacts/v5.0/d9a/out/runs/v4.2/C4.json
design/audit-artifacts/v5.0/d9a/out/runs/v4.2/C4.md
design/audit-artifacts/v5.0/d9a/out/runs/v4.2/C5.json
design/audit-artifacts/v5.0/d9a/out/runs/v4.2/C5.md
design/audit-artifacts/v5.0/d9a/out/runs/v4.2/C6.json
design/audit-artifacts/v5.0/d9a/out/runs/v4.2/C6.md
design/audit-artifacts/v5.0/d9a/out/runs/v5.0/C1.json
design/audit-artifacts/v5.0/d9a/out/runs/v5.0/C1.md
design/audit-artifacts/v5.0/d9a/out/runs/v5.0/C2.json
design/audit-artifacts/v5.0/d9a/out/runs/v5.0/C2.md
design/audit-artifacts/v5.0/d9a/out/runs/v5.0/C3.json
design/audit-artifacts/v5.0/d9a/out/runs/v5.0/C3.md
design/audit-artifacts/v5.0/d9a/out/runs/v5.0/C4.json
design/audit-artifacts/v5.0/d9a/out/runs/v5.0/C4.md
design/audit-artifacts/v5.0/d9a/out/runs/v5.0/C5.json
design/audit-artifacts/v5.0/d9a/out/runs/v5.0/C5.md
design/audit-artifacts/v5.0/d9a/out/runs/v5.0/C6.json
design/audit-artifacts/v5.0/d9a/out/runs/v5.0/C6.md
design/audit-artifacts/v5.0/d9a/out/setup.json
design/audit-artifacts/v5.0/d9a/out/summary.json
design/audit-artifacts/v5.0/d9a/root_CC_d9a_cc-design_v5.0.md
design/audit-artifacts/v5.0/d9a/run.log
design/root_DESIGN_behavioral-tuning_v5.md
design/root_DESIGN_catalog_v5.0.1_patch.md
design/root_DESIGN_catalog_v5_model_alignment.md
design/root_DESIGN_cc-design_v5.md
design/root_DS_cc_design_update_rev2.md
design/root_DS_skill_builder_v3_rev3.4.md
design/root_MODEL_LANDSCAPE_2026-10.md
design/root_skill_5gen_alignment_design.md
docs/root_SKILLS_RELEASE_PLAYBOOK.md
generate_release_notes.py
prompts/root_skill_4_8_alignment_rubric.md
release-notes/catalog-v3.1.md
release-notes/catalog-v4.0.md
release-notes/catalog-v5.0.1.md
release-notes/catalog-v5.0.md
release-notes/rootnode-anti-pattern-detection-v3.1.md
release-notes/rootnode-anti-pattern-detection-v4.0.md
release-notes/rootnode-anti-pattern-detection-v5.0.md
release-notes/rootnode-behavioral-tuning-v3.1.md
release-notes/rootnode-behavioral-tuning-v4.0.md
release-notes/rootnode-behavioral-tuning-v5.0.md
release-notes/rootnode-block-selection-v3.1.md
release-notes/rootnode-block-selection-v4.0.md
release-notes/rootnode-block-selection-v5.0.md
release-notes/rootnode-cc-design-v3.1.md
release-notes/rootnode-cc-design-v4.0.md
release-notes/rootnode-cc-design-v4.1.md
release-notes/rootnode-cc-design-v5.0.1.md
release-notes/rootnode-cc-design-v5.0.md
release-notes/rootnode-context-budget-v3.1.md
release-notes/rootnode-context-budget-v4.0.md
release-notes/rootnode-context-budget-v5.0.1.md
release-notes/rootnode-context-budget-v5.0.md
release-notes/rootnode-critic-gate-v3.1.md
release-notes/rootnode-critic-gate-v4.0.md
release-notes/rootnode-critic-gate-v5.0.1.md
release-notes/rootnode-critic-gate-v5.0.md
release-notes/rootnode-domain-agentic-context-v3.1.md
release-notes/rootnode-domain-agentic-context-v4.0.md
release-notes/rootnode-domain-agentic-context-v5.0.1.md
release-notes/rootnode-domain-agentic-context-v5.0.md
release-notes/rootnode-domain-business-strategy-v3.1.md
release-notes/rootnode-domain-business-strategy-v4.0.md
release-notes/rootnode-domain-business-strategy-v5.0.md
release-notes/rootnode-domain-content-communications-v3.1.md
release-notes/rootnode-domain-content-communications-v4.0.md
release-notes/rootnode-domain-content-communications-v5.0.md
release-notes/rootnode-domain-research-analysis-v3.1.md
release-notes/rootnode-domain-research-analysis-v4.0.md
release-notes/rootnode-domain-research-analysis-v5.0.1.md
release-notes/rootnode-domain-research-analysis-v5.0.md
release-notes/rootnode-domain-software-engineering-v3.1.md
release-notes/rootnode-domain-software-engineering-v4.0.md
release-notes/rootnode-domain-software-engineering-v5.0.md
release-notes/rootnode-full-stack-audit-v3.1.md
release-notes/rootnode-full-stack-audit-v4.0.md
release-notes/rootnode-full-stack-audit-v5.0.1.md
release-notes/rootnode-full-stack-audit-v5.0.md
release-notes/rootnode-global-audit-v3.1.md
release-notes/rootnode-global-audit-v4.0.md
release-notes/rootnode-global-audit-v5.0.1.md
release-notes/rootnode-global-audit-v5.0.md
release-notes/rootnode-handoff-trigger-check-v3.1.md
release-notes/rootnode-handoff-trigger-check-v4.0.md
release-notes/rootnode-handoff-trigger-check-v5.0.1.md
release-notes/rootnode-handoff-trigger-check-v5.0.md
release-notes/rootnode-identity-blocks-v3.1.md
release-notes/rootnode-identity-blocks-v4.0.md
release-notes/rootnode-identity-blocks-v5.0.md
release-notes/rootnode-memory-optimization-v3.1.md
release-notes/rootnode-memory-optimization-v4.0.md
release-notes/rootnode-memory-optimization-v5.0.md
release-notes/rootnode-mode-router-v3.1.md
release-notes/rootnode-mode-router-v4.0.md
release-notes/rootnode-mode-router-v5.0.1.md
release-notes/rootnode-mode-router-v5.0.md
release-notes/rootnode-output-blocks-v3.1.md
release-notes/rootnode-output-blocks-v4.0.md
release-notes/rootnode-output-blocks-v5.0.md
release-notes/rootnode-profile-builder-v3.1.md
release-notes/rootnode-profile-builder-v4.0.md
release-notes/rootnode-profile-builder-v5.0.md
release-notes/rootnode-project-audit-v3.1.md
release-notes/rootnode-project-audit-v4.0.md
release-notes/rootnode-project-audit-v5.0.1.md
release-notes/rootnode-project-audit-v5.0.md
release-notes/rootnode-project-brief-v3.1.md
release-notes/rootnode-project-brief-v4.0.md
release-notes/rootnode-project-brief-v5.0.md
release-notes/rootnode-prompt-compilation-v3.1.md
release-notes/rootnode-prompt-compilation-v4.0.md
release-notes/rootnode-prompt-compilation-v5.0.1.md
release-notes/rootnode-prompt-compilation-v5.0.md
release-notes/rootnode-prompt-validation-v3.1.md
release-notes/rootnode-prompt-validation-v4.0.md
release-notes/rootnode-prompt-validation-v5.0.1.md
release-notes/rootnode-prompt-validation-v5.0.md
release-notes/rootnode-reasoning-blocks-v3.1.md
release-notes/rootnode-reasoning-blocks-v4.0.md
release-notes/rootnode-reasoning-blocks-v5.0.md
release-notes/rootnode-repo-hygiene-v3.1.md
release-notes/rootnode-repo-hygiene-v4.0.md
release-notes/rootnode-repo-hygiene-v5.0.md
release-notes/rootnode-session-handoff-v3.1.md
release-notes/rootnode-session-handoff-v4.0.md
release-notes/rootnode-session-handoff-v5.0.md
release-notes/rootnode-skill-builder-v3.1.md
release-notes/rootnode-skill-builder-v4.0.md
release-notes/rootnode-skill-builder-v5.0.md
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
rootnode-cc-design/references/cc-delegation-patterns.md
rootnode-cc-design/references/cc-environment-design-patterns.md
rootnode-cc-design/references/cc-methodology-patterns.md
rootnode-cc-design/references/cc-prompt-design-patterns.md
rootnode-cc-design/references/cc-session-reports.md
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
Total tracked files: 390 (from `git ls-files | wc -l`).

## canonical-kfs roster (7)
_Source: `git ls-files audit/canonical-kfs/`; count via `git ls-files audit/canonical-kfs/ | wc -l`; content changes via `git log --oneline 12e9c2f..HEAD -- audit/canonical-kfs`_
```
audit/canonical-kfs/root_AGENT_ANTI_PATTERNS.md
audit/canonical-kfs/root_AGENT_ENVIRONMENT_ARCHITECTURE.md
audit/canonical-kfs/root_AUDIT_FRAMEWORK.md
audit/canonical-kfs/root_CC_ENVIRONMENT_GUIDE.md
audit/canonical-kfs/root_CLAUDE_OPTIMIZATION_NOTES.md
audit/canonical-kfs/root_OPTIMIZATION_REFERENCE.md
audit/canonical-kfs/root_SKILL_BUILD_DISCIPLINE.md

[commits touching the mirror since 12e9c2f]
7b22885 fix: catalog v5.0.1 rev 3 — host-cap guidance names N, guard ../ candidate and scope note, spec erratum
0cab5c8 fix: catalog v5.0.1 rev 2 — host Stop cap, handoff-trigger-check naming, guard gaps, prompt shell lessons, KF and docs sync
a88d449 fix: catalog v5.0.1 patch — Stop-hook chain bounds, resume rule, 16 v5.0 findings, KF mirror sync
5cf0592 docs(canonical-kfs): v5.0 seed sync — 5.5-generation alignment

[files changed since 12e9c2f]
M	audit/canonical-kfs/root_AGENT_ANTI_PATTERNS.md
M	audit/canonical-kfs/root_AGENT_ENVIRONMENT_ARCHITECTURE.md
M	audit/canonical-kfs/root_AUDIT_FRAMEWORK.md
M	audit/canonical-kfs/root_CC_ENVIRONMENT_GUIDE.md
M	audit/canonical-kfs/root_CLAUDE_OPTIMIZATION_NOTES.md
M	audit/canonical-kfs/root_OPTIMIZATION_REFERENCE.md
M	audit/canonical-kfs/root_SKILL_BUILD_DISCIPLINE.md
```
Delta from `root_repo_catalog_20261023.md`: roster unchanged (7 → 7). All 7 mirrors changed content: PR #27 (`5cf0592`) applied the v5.0 seed sync, and PR #28 (v5.0.1) re-synced CC_EG (rev 1, 2, 3), AAP and SBD (rev 1) and AEA (rev 2) from `design/staging-kf/` — the approved sync path under repo halt #5. Staged KFs at `design/staging-kf/` at generation time: this cycle's files, deleted at Phase C close (listed in the v5.0.1 session report).

## audit/v5_0_1-patch/ (v5.0.1 cycle directory)
_Source: `git ls-files audit/v5_0_1-patch/`; count via `git ls-files audit/v5_0_1-patch/ | wc -l`_
```
audit/v5_0_1-patch/refuter_brief_c1.md
audit/v5_0_1-patch/refuter_brief_r2c1.md
audit/v5_0_1-patch/refuter_c1.json
audit/v5_0_1-patch/refuter_r2c1.json
audit/v5_0_1-patch/release-notes-v5.0.1-config.py
audit/v5_0_1-patch/session_report_20261030-0040Z.md
audit/v5_0_1-patch/session_report_20261030-0107Z.md
audit/v5_0_1-patch/session_report_20261030-0224Z.md
```
8 files (NEW this cycle): the three build reports (rev 1 0040Z, the halted 0107Z run, rev 2 0224Z), the rev 1 and rev 2 Refuter briefs and verdicts, and the release-notes config. The release session's report and its rev 3 Refuter brief and verdict land with this catalog PR.

## audit/v5_0-alignment/ (v5.0 cycle directory)
_Source: `git ls-files audit/v5_0-alignment/`; count via `git ls-files audit/v5_0-alignment/ | wc -l`; changes via `git diff --name-status 12e9c2f HEAD -- audit/v5_0-alignment/`_
```
audit/v5_0-alignment/5_5GEN_SWEEP_MANIFEST.md
audit/v5_0-alignment/d9a_cc-design_v5.0_20261029-1406Z.md
audit/v5_0-alignment/kf-update-blocks.md
audit/v5_0-alignment/pr_body.md
audit/v5_0-alignment/release-notes-v5.0-config.py
audit/v5_0-alignment/session_report_20261023-0042Z.md

[changed since 12e9c2f]
A	audit/v5_0-alignment/d9a_cc-design_v5.0_20261029-1406Z.md
M	audit/v5_0-alignment/session_report_20261023-0042Z.md
```
6 files (was 5): +1 the cc-design v5.0 D9a report (PR #28, rev 1); the v5.0 session report modified since the prior snapshot by two commits (`c5933a2` catalog regeneration, `2c47114` rendered-umbrella operator verification).

## audit/v4_0-alignment/ (v4.0 cycle directory)
_Source: `git ls-files audit/v4_0-alignment/`; count via `git ls-files audit/v4_0-alignment/ | wc -l`_
```
audit/v4_0-alignment/5GEN_SWEEP_MANIFEST.md
audit/v4_0-alignment/5GEN_VERIFICATION_LOG.md
audit/v4_0-alignment/dryrun-v3.1-config.py
audit/v4_0-alignment/release-notes-v4.0-config.py
```
4 files (unchanged).

## Skills (rootnode-*/ source folders)
_Source: `for d in rootnode-*/; do echo $d; find $d -maxdepth 1 -mindepth 1 -type d; done`; folder count via `ls -d rootnode-*/ | wc -l`; versions via `grep -h -m1 -E '^\s+version:' rootnode-*/SKILL.md | sort | uniq -c`; file changes via `git diff --name-status 12e9c2f HEAD -- ':(glob)rootnode-*/**'` (pathspec match count 25)_
```
rootnode-anti-pattern-detection/
rootnode-behavioral-tuning/
  references
rootnode-block-selection/
  references
rootnode-cc-design/
  references
  schema
rootnode-context-budget/
  references
rootnode-critic-gate/
  examples
  profiles
  references
  schema
rootnode-domain-agentic-context/
  references
rootnode-domain-business-strategy/
  references
rootnode-domain-content-communications/
  references
rootnode-domain-research-analysis/
  references
rootnode-domain-software-engineering/
  references
rootnode-full-stack-audit/
  references
rootnode-global-audit/
  references
rootnode-handoff-trigger-check/
  profiles
  references
  schema
rootnode-identity-blocks/
  references
rootnode-memory-optimization/
  references
rootnode-mode-router/
  configs
  examples
  references
  schema
rootnode-output-blocks/
  references
rootnode-profile-builder/
  examples
  references
rootnode-project-audit/
  references
rootnode-project-brief/
  references
rootnode-prompt-compilation/
  references
rootnode-prompt-validation/
  references
rootnode-reasoning-blocks/
  references
rootnode-repo-hygiene/
  profiles
  references
  schema
rootnode-session-handoff/
  references
rootnode-skill-builder/
  agents
  eval-viewer
  references
  scripts

[versions]
     15   version: "5.0.0"
     12   version: "5.0.1"

[Skills at 5.0.1]
rootnode-cc-design
rootnode-context-budget
rootnode-critic-gate
rootnode-domain-agentic-context
rootnode-domain-research-analysis
rootnode-full-stack-audit
rootnode-global-audit
rootnode-handoff-trigger-check
rootnode-mode-router
rootnode-project-audit
rootnode-prompt-compilation
rootnode-prompt-validation

[files changed under rootnode-*/ since 12e9c2f]
M	rootnode-cc-design/SKILL.md
M	rootnode-cc-design/references/cc-anti-patterns.md
M	rootnode-cc-design/references/cc-environment-design-patterns.md
M	rootnode-cc-design/references/cc-prompt-design-patterns.md
M	rootnode-cc-design/references/cc-session-reports.md
M	rootnode-cc-design/references/cc-skills-and-hooks-composition.md
M	rootnode-cc-design/references/troubleshooting.md
M	rootnode-context-budget/SKILL.md
M	rootnode-critic-gate/SKILL.md
M	rootnode-critic-gate/references/checks-detailed.md
M	rootnode-domain-agentic-context/SKILL.md
M	rootnode-domain-agentic-context/references/reasoning-approaches.md
M	rootnode-domain-research-analysis/SKILL.md
M	rootnode-full-stack-audit/SKILL.md
M	rootnode-global-audit/SKILL.md
M	rootnode-handoff-trigger-check/SKILL.md
M	rootnode-handoff-trigger-check/references/examples.md
M	rootnode-handoff-trigger-check/references/troubleshooting.md
M	rootnode-mode-router/SKILL.md
M	rootnode-mode-router/references/trigger-types-detailed.md
M	rootnode-mode-router/references/troubleshooting.md
M	rootnode-project-audit/SKILL.md
M	rootnode-prompt-compilation/SKILL.md
M	rootnode-prompt-validation/SKILL.md
M	rootnode-prompt-validation/references/symptom-fix-map.md
```
Total: 27 Skill source folders (unchanged). 12 at `5.0.1`, 15 at `5.0.0`. Skill-file rows since 12e9c2f: 25 (25 M, 0 A, 0 D); no file added or removed under rootnode-*/.

## docs/
_Source: `git ls-files docs/`; repo-root duplicate check via `ls root_SKILLS_RELEASE_PLAYBOOK.md`_
```
[tracked]
docs/root_SKILLS_RELEASE_PLAYBOOK.md
[on disk]
(none — no repo-root duplicate present)
```
`docs/root_SKILLS_RELEASE_PLAYBOOK.md` changed this cycle (PR #28 rev 2: §1.2 install note, new §1.6 patch catalog release).

## Repo-root scripts (3)
_Source: `git ls-files | grep -E '^[^/]+\.py$'`; count via same piped to `wc -l`_
```
build_release_artifacts.py
build_releases.py
generate_release_notes.py
```
Roster unchanged (3 → 3). `build_release_artifacts.py` changed one line (`CATALOG_VERSION` → `"v5.0.1"`, spec §8.3); `generate_release_notes.py` unchanged, run with `audit/v5_0_1-patch/release-notes-v5.0.1-config.py`.

## design/ structure
_Source: `find design -maxdepth 2 -type d` for directories; `git ls-files design/` for tracked files_
```
design
design/audit-artifacts
design/audit-artifacts/v2.1
design/audit-artifacts/v3.0
design/audit-artifacts/v4.2
design/audit-artifacts/v5.0
design/skill-creator
design/skill-creator/agents
design/skill-creator/assets
design/skill-creator/eval-viewer
design/skill-creator/references
design/skill-creator/scripts
design/staging-kf
[staging-kf on disk: 10 files at generation time, gitignored per .gitignore `/design/staging-kf/`]
[tracked at design/ root:
design/root_DESIGN_behavioral-tuning_v5.md
design/root_DESIGN_catalog_v5.0.1_patch.md
design/root_DESIGN_catalog_v5_model_alignment.md
design/root_DESIGN_cc-design_v5.md
design/root_DS_cc_design_update_rev2.md
design/root_DS_skill_builder_v3_rev3.4.md
design/root_MODEL_LANDSCAPE_2026-10.md
design/root_skill_5gen_alignment_design.md
]
[tracked under design/audit-artifacts/ by version:
      5 v2.1
      7 v3.0
      3 v4.2
     37 v5.0
]
```
Delta from `root_repo_catalog_20261023.md`: tracked design files 19 → 60 (+41): +1 spec `design/root_DESIGN_catalog_v5.0.1_patch.md`; +37 under `design/audit-artifacts/v5.0/d9a/` (the D9a evidence; the raw `*.jsonl` streams stay untracked); +3 under `design/audit-artifacts/v4.2/` (inventory report, v4.2 spec, v4.2 landscape). `design/audit-artifacts/v4.2/scratch/` remains on disk, untracked.

## Recent commits (20)
_Source: `git log --oneline -20`_
```
2c04b70 Merge pull request #28 from drayline/release/v5.0.1
d991e02 docs(audit): v5.0.1 build reports and review files; v4.2 design records
05e30d9 docs: v5.0.1 release notes, umbrella notes, changelog
7b22885 fix: catalog v5.0.1 rev 3 — host-cap guidance names N, guard ../ candidate and scope note, spec erratum
4538de0 docs(audit): v5.0.1 build report and review files; v4.2 inventory report
0cab5c8 fix: catalog v5.0.1 rev 2 — host Stop cap, handoff-trigger-check naming, guard gaps, prompt shell lessons, KF and docs sync
6a257f9 docs(audit): catalog v5.0.1 spec and cc-design v5.0 D9a evidence
a88d449 fix: catalog v5.0.1 patch — Stop-hook chain bounds, resume rule, 16 v5.0 findings, KF mirror sync
e336bce Merge pull request #27 from drayline/docs/kf-sync-v5.0
5cf0592 docs(canonical-kfs): v5.0 seed sync — 5.5-generation alignment
1a8cb74 Merge pull request #26 from drayline/chore/catalog-regen-v5.0
2c47114 docs: v5.0 session report — rendered umbrella page operator-verified
c5933a2 chore(catalog): regenerate for v5.0
12e9c2f Merge pull request #25 from drayline/release/v5.0
b8a8755 feat: rootnode-cc-design 5.0.0 — close spec items D8, A6, E3 + guard notes
ca92813 docs: v5.0 audit — repair control byte in report addendum
3eeaa89 docs: v5.0 audit — operator rulings appended
32d4650 docs: track v5.0 design specs
07f9542 release: bump packager CATALOG_VERSION to v5.0
c4a23ea docs: v5.0 notes, README, changelog, audit
```

## Tags (133)
_Source: `git tag --list`; count via `git tag --list | wc -l`_
```
catalog-v3.0
catalog-v3.1
catalog-v4.0
catalog-v5.0
catalog-v5.0.1
cc-design/v2.1
cc-design/v3.0
rootnode-anti-pattern-detection/v3.0
rootnode-anti-pattern-detection/v3.1
rootnode-anti-pattern-detection/v4.0
rootnode-anti-pattern-detection/v5.0
rootnode-behavioral-tuning/v3.0
rootnode-behavioral-tuning/v3.1
rootnode-behavioral-tuning/v4.0
rootnode-behavioral-tuning/v5.0
rootnode-block-selection/v3.0
rootnode-block-selection/v3.1
rootnode-block-selection/v4.0
rootnode-block-selection/v5.0
rootnode-cc-design/v3.1
rootnode-cc-design/v4.0
rootnode-cc-design/v4.1
rootnode-cc-design/v4.2
rootnode-cc-design/v5.0
rootnode-cc-design/v5.0.1
rootnode-context-budget/v3.0
rootnode-context-budget/v3.1
rootnode-context-budget/v4.0
rootnode-context-budget/v5.0
rootnode-context-budget/v5.0.1
rootnode-critic-gate/v3.0
rootnode-critic-gate/v3.1
rootnode-critic-gate/v4.0
rootnode-critic-gate/v5.0
rootnode-critic-gate/v5.0.1
rootnode-domain-agentic-context/v3.0
rootnode-domain-agentic-context/v3.1
rootnode-domain-agentic-context/v4.0
rootnode-domain-agentic-context/v5.0
rootnode-domain-agentic-context/v5.0.1
rootnode-domain-business-strategy/v3.0
rootnode-domain-business-strategy/v3.1
rootnode-domain-business-strategy/v4.0
rootnode-domain-business-strategy/v5.0
rootnode-domain-content-communications/v3.0
rootnode-domain-content-communications/v3.1
rootnode-domain-content-communications/v4.0
rootnode-domain-content-communications/v5.0
rootnode-domain-research-analysis/v3.0
rootnode-domain-research-analysis/v3.1
rootnode-domain-research-analysis/v4.0
rootnode-domain-research-analysis/v5.0
rootnode-domain-research-analysis/v5.0.1
rootnode-domain-software-engineering/v3.0
rootnode-domain-software-engineering/v3.1
rootnode-domain-software-engineering/v4.0
rootnode-domain-software-engineering/v5.0
rootnode-full-stack-audit/v3.0
rootnode-full-stack-audit/v3.1
rootnode-full-stack-audit/v4.0
rootnode-full-stack-audit/v5.0
rootnode-full-stack-audit/v5.0.1
rootnode-global-audit/v3.0
rootnode-global-audit/v3.1
rootnode-global-audit/v4.0
rootnode-global-audit/v5.0
rootnode-global-audit/v5.0.1
rootnode-handoff-trigger-check/v3.0
rootnode-handoff-trigger-check/v3.1
rootnode-handoff-trigger-check/v4.0
rootnode-handoff-trigger-check/v5.0
rootnode-handoff-trigger-check/v5.0.1
rootnode-identity-blocks/v3.0
rootnode-identity-blocks/v3.1
rootnode-identity-blocks/v4.0
rootnode-identity-blocks/v5.0
rootnode-memory-optimization/v3.0
rootnode-memory-optimization/v3.1
rootnode-memory-optimization/v4.0
rootnode-memory-optimization/v5.0
rootnode-mode-router/v3.0
rootnode-mode-router/v3.1
rootnode-mode-router/v4.0
rootnode-mode-router/v5.0
rootnode-mode-router/v5.0.1
rootnode-output-blocks/v3.0
rootnode-output-blocks/v3.1
rootnode-output-blocks/v4.0
rootnode-output-blocks/v5.0
rootnode-profile-builder/v3.0
rootnode-profile-builder/v3.1
rootnode-profile-builder/v4.0
rootnode-profile-builder/v5.0
rootnode-project-audit/v3.0
rootnode-project-audit/v3.1
rootnode-project-audit/v4.0
rootnode-project-audit/v5.0
rootnode-project-audit/v5.0.1
rootnode-project-brief/v3.0
rootnode-project-brief/v3.1
rootnode-project-brief/v4.0
rootnode-project-brief/v5.0
rootnode-prompt-compilation/v3.0
rootnode-prompt-compilation/v3.1
rootnode-prompt-compilation/v4.0
rootnode-prompt-compilation/v5.0
rootnode-prompt-compilation/v5.0.1
rootnode-prompt-validation/v3.0
rootnode-prompt-validation/v3.1
rootnode-prompt-validation/v4.0
rootnode-prompt-validation/v5.0
rootnode-prompt-validation/v5.0.1
rootnode-reasoning-blocks/v3.0
rootnode-reasoning-blocks/v3.1
rootnode-reasoning-blocks/v4.0
rootnode-reasoning-blocks/v5.0
rootnode-repo-hygiene/v3.0
rootnode-repo-hygiene/v3.1
rootnode-repo-hygiene/v4.0
rootnode-repo-hygiene/v5.0
rootnode-session-handoff/v3.0
rootnode-session-handoff/v3.1
rootnode-session-handoff/v4.0
rootnode-session-handoff/v5.0
rootnode-skill-builder/v3.1
rootnode-skill-builder/v4.0
rootnode-skill-builder/v5.0
skill-builder/v3.0
v1.0
v1.1
v1.2
v2.0.0
v2.1
```
Delta from `root_repo_catalog_20261023.md`: +13 tags (12 `rootnode-<skill>/v5.0.1` + `catalog-v5.0.1`), 0 removed. Total 120 → 133. All 13 v5.0.1 tags resolve to `2c04b7035f438609360f60c599e8f3e599bb8ec8` (`git tag --list '*v5.0.1' | while read t; do git rev-list -n1 $t; done | sort -u`). None of the 15 unchanged Skills has a `v5.0.1` tag.

## GitHub releases
_Source: `gh release list --limit 200`; row count via `wc -l` (131 rows, <200 asserts non-truncated)_
```
catalog-v5.0.1	Latest	catalog-v5.0.1	2026-10-30T12:58:51Z
rootnode-cc-design/v5.0.1		rootnode-cc-design/v5.0.1	2026-10-30T12:58:43Z
rootnode-mode-router/v5.0.1		rootnode-mode-router/v5.0.1	2026-10-30T12:58:39Z
rootnode-critic-gate/v5.0.1		rootnode-critic-gate/v5.0.1	2026-10-30T12:58:36Z
rootnode-prompt-validation/v5.0.1		rootnode-prompt-validation/v5.0.1	2026-10-30T12:58:32Z
rootnode-prompt-compilation/v5.0.1		rootnode-prompt-compilation/v5.0.1	2026-10-30T12:58:28Z
rootnode-project-audit/v5.0.1		rootnode-project-audit/v5.0.1	2026-10-30T12:58:24Z
rootnode-handoff-trigger-check/v5.0.1		rootnode-handoff-trigger-check/v5.0.1	2026-10-30T12:58:21Z
rootnode-global-audit/v5.0.1		rootnode-global-audit/v5.0.1	2026-10-30T12:58:17Z
rootnode-full-stack-audit/v5.0.1		rootnode-full-stack-audit/v5.0.1	2026-10-30T12:58:13Z
rootnode-domain-research-analysis/v5.0.1		rootnode-domain-research-analysis/v5.0.1	2026-10-30T12:58:10Z
rootnode-domain-agentic-context/v5.0.1		rootnode-domain-agentic-context/v5.0.1	2026-10-30T12:58:06Z
rootnode-context-budget/v5.0.1		rootnode-context-budget/v5.0.1	2026-10-30T12:58:03Z
catalog-v5.0		catalog-v5.0	2026-10-23T01:20:53Z
rootnode-skill-builder/v5.0		rootnode-skill-builder/v5.0	2026-10-23T01:20:47Z
rootnode-session-handoff/v5.0		rootnode-session-handoff/v5.0	2026-10-23T01:20:44Z
rootnode-repo-hygiene/v5.0		rootnode-repo-hygiene/v5.0	2026-10-23T01:20:42Z
rootnode-reasoning-blocks/v5.0		rootnode-reasoning-blocks/v5.0	2026-10-23T01:20:39Z
rootnode-prompt-validation/v5.0		rootnode-prompt-validation/v5.0	2026-10-23T01:20:36Z
rootnode-prompt-compilation/v5.0		rootnode-prompt-compilation/v5.0	2026-10-23T01:20:34Z
rootnode-project-brief/v5.0		rootnode-project-brief/v5.0	2026-10-23T01:20:31Z
rootnode-project-audit/v5.0		rootnode-project-audit/v5.0	2026-10-23T01:20:29Z
rootnode-profile-builder/v5.0		rootnode-profile-builder/v5.0	2026-10-23T01:20:26Z
rootnode-output-blocks/v5.0		rootnode-output-blocks/v5.0	2026-10-23T01:20:24Z
rootnode-mode-router/v5.0		rootnode-mode-router/v5.0	2026-10-23T01:20:21Z
rootnode-memory-optimization/v5.0		rootnode-memory-optimization/v5.0	2026-10-23T01:20:18Z
rootnode-identity-blocks/v5.0		rootnode-identity-blocks/v5.0	2026-10-23T01:20:16Z
rootnode-handoff-trigger-check/v5.0		rootnode-handoff-trigger-check/v5.0	2026-10-23T01:20:13Z
rootnode-global-audit/v5.0		rootnode-global-audit/v5.0	2026-10-23T01:20:11Z
rootnode-full-stack-audit/v5.0		rootnode-full-stack-audit/v5.0	2026-10-23T01:20:08Z
rootnode-domain-software-engineering/v5.0		rootnode-domain-software-engineering/v5.0	2026-10-23T01:20:06Z
rootnode-domain-research-analysis/v5.0		rootnode-domain-research-analysis/v5.0	2026-10-23T01:20:04Z
rootnode-domain-content-communications/v5.0		rootnode-domain-content-communications/v5.0	2026-10-23T01:20:01Z
rootnode-domain-business-strategy/v5.0		rootnode-domain-business-strategy/v5.0	2026-10-23T01:19:59Z
rootnode-domain-agentic-context/v5.0		rootnode-domain-agentic-context/v5.0	2026-10-23T01:19:56Z
rootnode-critic-gate/v5.0		rootnode-critic-gate/v5.0	2026-10-23T01:19:53Z
rootnode-context-budget/v5.0		rootnode-context-budget/v5.0	2026-10-23T01:19:50Z
rootnode-cc-design/v5.0		rootnode-cc-design/v5.0	2026-10-23T01:19:48Z
rootnode-block-selection/v5.0		rootnode-block-selection/v5.0	2026-10-23T01:19:45Z
rootnode-behavioral-tuning/v5.0		rootnode-behavioral-tuning/v5.0	2026-10-23T01:19:43Z
rootnode-anti-pattern-detection/v5.0		rootnode-anti-pattern-detection/v5.0	2026-10-23T01:19:40Z
rootnode-cc-design v4.2.0		rootnode-cc-design/v4.2	2026-09-13T07:11:02Z
rootnode-cc-design v4.1		rootnode-cc-design/v4.1	2026-09-11T17:10:08Z
catalog-v4.0		catalog-v4.0	2026-07-25T23:35:30Z
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
rootnode-session-handoff v3.0		rootnode-session-handoff/v3.0	2026-05-10T16:07:57Z
rootnode-reasoning-blocks v3.0		rootnode-reasoning-blocks/v3.0	2026-05-10T16:07:53Z
rootnode-prompt-validation v3.0		rootnode-prompt-validation/v3.0	2026-05-10T16:07:49Z
rootnode-prompt-compilation v3.0		rootnode-prompt-compilation/v3.0	2026-05-10T16:07:46Z
rootnode-project-brief v3.0		rootnode-project-brief/v3.0	2026-05-10T16:07:42Z
rootnode-project-audit v3.0		rootnode-project-audit/v3.0	2026-05-10T16:07:38Z
rootnode-profile-builder v3.0		rootnode-profile-builder/v3.0	2026-05-10T16:07:35Z
rootnode-output-blocks v3.0		rootnode-output-blocks/v3.0	2026-05-10T16:07:31Z
rootnode-memory-optimization v3.0		rootnode-memory-optimization/v3.0	2026-05-10T16:07:28Z
rootnode-identity-blocks v3.0		rootnode-identity-blocks/v3.0	2026-05-10T16:07:24Z
rootnode-handoff-trigger-check v3.0		rootnode-handoff-trigger-check/v3.0	2026-05-10T16:07:21Z
rootnode-global-audit v3.0		rootnode-global-audit/v3.0	2026-05-10T16:07:17Z
rootnode-full-stack-audit v3.0		rootnode-full-stack-audit/v3.0	2026-05-10T16:07:14Z
rootnode-domain-software-engineering v3.0		rootnode-domain-software-engineering/v3.0	2026-05-10T16:07:10Z
rootnode-domain-research-analysis v3.0		rootnode-domain-research-analysis/v3.0	2026-05-10T16:07:07Z
rootnode-domain-content-communications v3.0		rootnode-domain-content-communications/v3.0	2026-05-10T16:07:03Z
rootnode-domain-business-strategy v3.0		rootnode-domain-business-strategy/v3.0	2026-05-10T16:06:59Z
rootnode-domain-agentic-context v3.0		rootnode-domain-agentic-context/v3.0	2026-05-10T16:06:56Z
rootnode-context-budget v3.0		rootnode-context-budget/v3.0	2026-05-10T16:06:52Z
rootnode-block-selection v3.0		rootnode-block-selection/v3.0	2026-05-10T16:06:49Z
rootnode-behavioral-tuning v3.0		rootnode-behavioral-tuning/v3.0	2026-05-10T16:06:45Z
rootnode-anti-pattern-detection v3.0		rootnode-anti-pattern-detection/v3.0	2026-05-10T16:06:41Z
rootnode-cc-design v3.0		cc-design/v3.0	2026-05-10T16:06:00Z
rootnode-skill-builder v3.0		skill-builder/v3.0	2026-05-09T17:49:39Z
v2.1		v2.1	2026-05-01T23:13:42Z
v2.0.0		v2.0.0	2026-04-14T03:30:54Z
v1.2: README rebuild		v1.2	2026-03-24T12:53:45Z
Initial Release		v1.0	2026-03-15T01:19:49Z
```
Delta from `root_repo_catalog_20261023.md`: +13 releases (12 per-Skill `rootnode-<skill>/v5.0.1`, `--latest=false`; `catalog-v5.0.1` umbrella, `--latest`, carrying the single bundle asset `rootnode-catalog-v5.0.1.zip`). Total 118 → 131. **`Latest` is `catalog-v5.0.1`** (only row marked Latest; `gh api repos/drayline/rootnode-skills/releases/latest` → `catalog-v5.0.1`). `rootnode-cc-design/v5.0.1` carries both `-cp` and `-cc` zips; `rootnode-critic-gate/v5.0.1` and `rootnode-mode-router/v5.0.1` carry `-cc`; the other 9 carry `-cp`.

## release-notes/ v5.0.1 files
_Source: `git ls-files release-notes/ | grep -E 'v5\.0\.1'`_
```
release-notes/catalog-v5.0.1.md
release-notes/rootnode-cc-design-v5.0.1.md
release-notes/rootnode-context-budget-v5.0.1.md
release-notes/rootnode-critic-gate-v5.0.1.md
release-notes/rootnode-domain-agentic-context-v5.0.1.md
release-notes/rootnode-domain-research-analysis-v5.0.1.md
release-notes/rootnode-full-stack-audit-v5.0.1.md
release-notes/rootnode-global-audit-v5.0.1.md
release-notes/rootnode-handoff-trigger-check-v5.0.1.md
release-notes/rootnode-mode-router-v5.0.1.md
release-notes/rootnode-project-audit-v5.0.1.md
release-notes/rootnode-prompt-compilation-v5.0.1.md
release-notes/rootnode-prompt-validation-v5.0.1.md
```
13 new files: 12 per-Skill notes (generated by `generate_release_notes.py` from `audit/v5_0_1-patch/release-notes-v5.0.1-config.py`, counts 9 + 2 + 1 = 12) + the `catalog-v5.0.1` umbrella notes. Applied via `--notes-file`. Prior notes preserved (append-only).

## CATALOG_VERSION
_Source: `grep -n 'CATALOG_VERSION' build_release_artifacts.py`_
```
59:CATALOG_VERSION = "v5.0.1"
109:    bundle = DIST_DIR / f"rootnode-catalog-{CATALOG_VERSION}.zip"
176:              f"  -> upload to the catalog-{CATALOG_VERSION} release")
```
Bumped `"v5.0"` → `"v5.0.1"` this cycle (PR #28, spec §8.3). Full build from merged main wrote `dist/rootnode-catalog-v5.0.1.zip` (1023257 bytes; 29 zips), uploaded to `catalog-v5.0.1`.

## Cycle-delta summary vs `root_repo_catalog_20261023.md`

- **Tracked files: 326 → 390 (+64; removals 0).** Additions since the prior snapshot's HEAD `12e9c2f` (`git diff --name-status --diff-filter=A 12e9c2f HEAD`, 64 rows): `audit/repo-catalog/` 1 (the prior snapshot itself), `audit/v5_0-alignment/` 1, `audit/v5_0_1-patch/` 8, `design/audit-artifacts/` 40, `design/` spec 1, `release-notes/` 13 → 1 + 1 + 8 + 40 + 1 + 13 = 64. Modified (`--diff-filter=M`, 38 rows): `rootnode-*/` 25, `audit/canonical-kfs/` 7, `audit/v5_0-alignment/` 1, `CHANGELOG.md` 1, `README.md` 1, `build_release_artifacts.py` 1, `design/root_DESIGN_catalog_v5_model_alignment.md` 1, `docs/root_SKILLS_RELEASE_PLAYBOOK.md` 1 → 25 + 7 + 1 + 1 + 1 + 1 + 1 + 1 = 38. All diff rows: 64 + 38 = 102 (`git diff --name-status 12e9c2f HEAD | wc -l`).
- **Skills folders: 27 → 27 (unchanged); 12 at 5.0.1, 15 at 5.0.0.** Skill-file rows: 25 M, 0 A, 0 D.
- **canonical-kfs roster: 7 → 7; all 7 mirrors changed content** (PR #27 v5.0 seed sync; PR #28 CC_EG, AAP, SBD, AEA re-syncs from staging).
- **Cycle directories: +`audit/v5_0_1-patch/` (8 files).** `audit/v5_0-alignment/` 5 → 6; `audit/v4_0-alignment/` unchanged (4).
- **Repo-root scripts: 3 → 3 (unchanged roster).** Packager `CATALOG_VERSION` bumped to `"v5.0.1"`.
- **design/: 19 → 60 tracked.** `design/audit-artifacts/v4.2/scratch/` still untracked on disk.
- **Tags: 120 → 133 (+13).** 12 `rootnode-<skill>/v5.0.1` + `catalog-v5.0.1`, all at `2c04b70`.
- **GitHub releases: 118 → 131 (+13).** 12 per-Skill releases + `catalog-v5.0.1` umbrella. **`catalog-v5.0.1` is Latest** (was `catalog-v5.0`).
- **release-notes/: +13 files** (12 per-Skill + umbrella).
- **README:** version badge v5.0.1, calibration badge Opus 5.5 + Sonnet 5.5, version-free bundle name, account-sync caveat (PR #28 rev 2). Install links point at `/releases/latest` (2 occurrences), which now resolves to `catalog-v5.0.1`.
