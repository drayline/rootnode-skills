# rootnode-skills — Repo Catalog
_Generated 2026-11-02 | HEAD cb61ad916026607dca8dcbb2754adac992023640 (feat/plugin-packaging-v6.0, not yet merged) | regenerated per playbook Post-verification step_

Regenerated 2026-11-02 for the catalog v6.0 content PR, ahead of any release, so the PR carries the new layout. Tags and GitHub releases are unchanged from `root_repo_catalog_20261030.md` because no tag or release is part of this PR. The release prompt regenerates this file again after its verification. Section structure matches `root_repo_catalog_20261030.md`, with new Plugins and Marketplace sections, the Skills section moved to `plugins/*/skills/`, and the CATALOG_VERSION section replaced by the packager constants.

## Remote
_Source: `git remote -v`_
```
origin	git@github.com:drayline/rootnode-skills.git (fetch)
origin	git@github.com:drayline/rootnode-skills.git (push)
```

## Tracked file tree (git ls-files)
_Source: `git ls-files`; count via `git ls-files | wc -l`_
```
.claude-plugin/marketplace.json
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
audit/repo-catalog/root_repo_catalog_20261030.md
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
audit/v5_0_1-patch/refuter_brief_r3c1.md
audit/v5_0_1-patch/refuter_c1.json
audit/v5_0_1-patch/refuter_r2c1.json
audit/v5_0_1-patch/refuter_r3c1.json
audit/v5_0_1-patch/release-notes-v5.0.1-config.py
audit/v5_0_1-patch/session_report_20261030-0040Z.md
audit/v5_0_1-patch/session_report_20261030-0107Z.md
audit/v5_0_1-patch/session_report_20261030-0224Z.md
audit/v5_0_1-patch/session_report_20261030-0303Z.md
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
design/root_DESIGN_plugin_packaging.md
design/root_DS_cc_design_update_rev2.md
design/root_DS_skill_builder_v3_rev3.4.md
design/root_MODEL_LANDSCAPE_2026-10.md
design/root_skill_5gen_alignment_design.md
docs/root_SKILLS_RELEASE_PLAYBOOK.md
generate_release_notes.py
plugins/rootnode-code/.claude-plugin/plugin.json
plugins/rootnode-code/.gitattributes
plugins/rootnode-code/LICENSE
plugins/rootnode-code/README.md
plugins/rootnode-code/hooks/hooks.json
plugins/rootnode-code/scripts/guard-migrations.sh
plugins/rootnode-code/scripts/verify-tests.sh
plugins/rootnode-code/skills/cc-design/SKILL.md
plugins/rootnode-code/skills/cc-design/references/cc-anti-patterns.md
plugins/rootnode-code/skills/cc-design/references/cc-delegation-patterns.md
plugins/rootnode-code/skills/cc-design/references/cc-environment-design-patterns.md
plugins/rootnode-code/skills/cc-design/references/cc-methodology-patterns.md
plugins/rootnode-code/skills/cc-design/references/cc-prompt-design-patterns.md
plugins/rootnode-code/skills/cc-design/references/cc-session-reports.md
plugins/rootnode-code/skills/cc-design/references/cc-skills-and-hooks-composition.md
plugins/rootnode-code/skills/cc-design/references/chat-to-code-handoff-patterns.md
plugins/rootnode-code/skills/cc-design/references/remediate-mode-execution.md
plugins/rootnode-code/skills/cc-design/references/source-grading-and-tagging.md
plugins/rootnode-code/skills/cc-design/references/troubleshooting.md
plugins/rootnode-code/skills/cc-design/schema/cc-design-brief.schema.json
plugins/rootnode-code/skills/cc-design/schema/execution-plan.schema.json
plugins/rootnode-code/skills/repo-hygiene/SKILL.md
plugins/rootnode-code/skills/repo-hygiene/profiles/deep-audit.json
plugins/rootnode-code/skills/repo-hygiene/profiles/default.json
plugins/rootnode-code/skills/repo-hygiene/profiles/quick-scan.json
plugins/rootnode-code/skills/repo-hygiene/references/anti-pattern-catalog.md
plugins/rootnode-code/skills/repo-hygiene/references/cc-best-practices.md
plugins/rootnode-code/skills/repo-hygiene/references/execution-discipline.md
plugins/rootnode-code/skills/repo-hygiene/references/process-abstraction-detection.md
plugins/rootnode-code/skills/repo-hygiene/references/seven-layer-framework.md
plugins/rootnode-code/skills/repo-hygiene/references/sweep-categories.md
plugins/rootnode-code/skills/repo-hygiene/references/worked-example.md
plugins/rootnode-code/skills/repo-hygiene/schema/profile.schema.json
plugins/rootnode-governance/.claude-plugin/plugin.json
plugins/rootnode-governance/LICENSE
plugins/rootnode-governance/README.md
plugins/rootnode-governance/skills/critic-gate/SKILL.md
plugins/rootnode-governance/skills/critic-gate/examples/worked-example.md
plugins/rootnode-governance/skills/critic-gate/profiles/balanced.json
plugins/rootnode-governance/skills/critic-gate/profiles/lenient.json
plugins/rootnode-governance/skills/critic-gate/profiles/strict.json
plugins/rootnode-governance/skills/critic-gate/references/checks-detailed.md
plugins/rootnode-governance/skills/critic-gate/references/severity-coverage.md
plugins/rootnode-governance/skills/critic-gate/references/troubleshooting.md
plugins/rootnode-governance/skills/critic-gate/schema/profile.schema.json
plugins/rootnode-governance/skills/handoff-trigger-check/SKILL.md
plugins/rootnode-governance/skills/handoff-trigger-check/profiles/balanced.json
plugins/rootnode-governance/skills/handoff-trigger-check/profiles/lenient.json
plugins/rootnode-governance/skills/handoff-trigger-check/profiles/strict.json
plugins/rootnode-governance/skills/handoff-trigger-check/references/examples.md
plugins/rootnode-governance/skills/handoff-trigger-check/references/sensing-triggers-detailed.md
plugins/rootnode-governance/skills/handoff-trigger-check/references/troubleshooting.md
plugins/rootnode-governance/skills/handoff-trigger-check/schema/profile.schema.json
plugins/rootnode-governance/skills/mode-router/SKILL.md
plugins/rootnode-governance/skills/mode-router/configs/example-router.json
plugins/rootnode-governance/skills/mode-router/examples/routing-walkthrough.md
plugins/rootnode-governance/skills/mode-router/references/compound-trigger-semantics.md
plugins/rootnode-governance/skills/mode-router/references/trigger-types-detailed.md
plugins/rootnode-governance/skills/mode-router/references/troubleshooting.md
plugins/rootnode-governance/skills/mode-router/schema/router-config.schema.json
plugins/rootnode-governance/skills/profile-builder/SKILL.md
plugins/rootnode-governance/skills/profile-builder/examples/sample-interview-flow.md
plugins/rootnode-governance/skills/profile-builder/references/common-schema-shapes.md
plugins/rootnode-governance/skills/profile-builder/references/schema-walking-patterns.md
plugins/rootnode-governance/skills/profile-builder/references/troubleshooting.md
plugins/rootnode-governance/skills/session-handoff/SKILL.md
plugins/rootnode-governance/skills/session-handoff/references/closeout-checklist.md
plugins/rootnode-governance/skills/session-handoff/references/handoff-template.md
plugins/rootnode-projects/.claude-plugin/plugin.json
plugins/rootnode-projects/LICENSE
plugins/rootnode-projects/README.md
plugins/rootnode-projects/evals/no-trigger-general-coding/graders/criteria.md
plugins/rootnode-projects/evals/no-trigger-general-coding/graders/skill-not-fired.md
plugins/rootnode-projects/evals/no-trigger-general-coding/prompt.md
plugins/rootnode-projects/evals/no-trigger-prompt-scoring/graders/criteria.md
plugins/rootnode-projects/evals/no-trigger-prompt-scoring/graders/skill-not-fired.md
plugins/rootnode-projects/evals/no-trigger-prompt-scoring/prompt.md
plugins/rootnode-projects/evals/trigger-anti-pattern-detection/graders/criteria.md
plugins/rootnode-projects/evals/trigger-anti-pattern-detection/graders/skill-fired.md
plugins/rootnode-projects/evals/trigger-anti-pattern-detection/prompt.md
plugins/rootnode-projects/evals/trigger-global-audit/graders/criteria.md
plugins/rootnode-projects/evals/trigger-global-audit/graders/skill-fired.md
plugins/rootnode-projects/evals/trigger-global-audit/prompt.md
plugins/rootnode-projects/evals/trigger-project-audit/graders/criteria.md
plugins/rootnode-projects/evals/trigger-project-audit/graders/skill-fired.md
plugins/rootnode-projects/evals/trigger-project-audit/prompt.md
plugins/rootnode-projects/skills/anti-pattern-detection/SKILL.md
plugins/rootnode-projects/skills/context-budget/SKILL.md
plugins/rootnode-projects/skills/context-budget/references/compression-execution.md
plugins/rootnode-projects/skills/context-budget/references/content-routing.md
plugins/rootnode-projects/skills/context-budget/references/evaluation-rubric.md
plugins/rootnode-projects/skills/full-stack-audit/SKILL.md
plugins/rootnode-projects/skills/full-stack-audit/references/cross-layer-checks.md
plugins/rootnode-projects/skills/full-stack-audit/references/evolutionary-pathways.md
plugins/rootnode-projects/skills/full-stack-audit/references/global-layer-scorecard.md
plugins/rootnode-projects/skills/full-stack-audit/references/project-scorecard.md
plugins/rootnode-projects/skills/full-stack-audit/references/quality-criteria.md
plugins/rootnode-projects/skills/global-audit/SKILL.md
plugins/rootnode-projects/skills/global-audit/references/cross-layer-checks.md
plugins/rootnode-projects/skills/global-audit/references/evolutionary-pathways.md
plugins/rootnode-projects/skills/global-audit/references/global-layer-scorecard.md
plugins/rootnode-projects/skills/global-audit/references/preference-principles.md
plugins/rootnode-projects/skills/memory-optimization/SKILL.md
plugins/rootnode-projects/skills/memory-optimization/references/assessment-rubric.md
plugins/rootnode-projects/skills/memory-optimization/references/optimization-patterns.md
plugins/rootnode-projects/skills/project-audit/SKILL.md
plugins/rootnode-projects/skills/project-audit/references/cross-layer-basics.md
plugins/rootnode-projects/skills/project-audit/references/diagnostic-questions.md
plugins/rootnode-projects/skills/project-audit/references/quality-criteria.md
plugins/rootnode-projects/skills/project-brief/SKILL.md
plugins/rootnode-projects/skills/project-brief/references/brief-template.md
plugins/rootnode-prompts/.claude-plugin/plugin.json
plugins/rootnode-prompts/LICENSE
plugins/rootnode-prompts/README.md
plugins/rootnode-prompts/skills/block-selection/SKILL.md
plugins/rootnode-prompts/skills/block-selection/references/domain-pack-index.md
plugins/rootnode-prompts/skills/block-selection/references/identity-blocks.md
plugins/rootnode-prompts/skills/block-selection/references/output-blocks.md
plugins/rootnode-prompts/skills/block-selection/references/reasoning-blocks.md
plugins/rootnode-prompts/skills/domain-agentic-context/SKILL.md
plugins/rootnode-prompts/skills/domain-agentic-context/references/output-formats.md
plugins/rootnode-prompts/skills/domain-agentic-context/references/reasoning-approaches.md
plugins/rootnode-prompts/skills/domain-business-strategy/SKILL.md
plugins/rootnode-prompts/skills/domain-business-strategy/references/output-formats.md
plugins/rootnode-prompts/skills/domain-business-strategy/references/reasoning-approaches.md
plugins/rootnode-prompts/skills/domain-content-communications/SKILL.md
plugins/rootnode-prompts/skills/domain-content-communications/references/output-formats.md
plugins/rootnode-prompts/skills/domain-content-communications/references/reasoning-approaches.md
plugins/rootnode-prompts/skills/domain-research-analysis/SKILL.md
plugins/rootnode-prompts/skills/domain-research-analysis/references/examples.md
plugins/rootnode-prompts/skills/domain-research-analysis/references/output-formats.md
plugins/rootnode-prompts/skills/domain-research-analysis/references/reasoning-approaches.md
plugins/rootnode-prompts/skills/domain-software-engineering/SKILL.md
plugins/rootnode-prompts/skills/domain-software-engineering/references/output-formats.md
plugins/rootnode-prompts/skills/domain-software-engineering/references/reasoning-approaches.md
plugins/rootnode-prompts/skills/identity-blocks/SKILL.md
plugins/rootnode-prompts/skills/identity-blocks/references/communications-identities.md
plugins/rootnode-prompts/skills/identity-blocks/references/operations-identities.md
plugins/rootnode-prompts/skills/identity-blocks/references/research-identities.md
plugins/rootnode-prompts/skills/identity-blocks/references/strategic-identities.md
plugins/rootnode-prompts/skills/identity-blocks/references/technical-identities.md
plugins/rootnode-prompts/skills/output-blocks/SKILL.md
plugins/rootnode-prompts/skills/output-blocks/references/analytical-formats.md
plugins/rootnode-prompts/skills/output-blocks/references/executive-formats.md
plugins/rootnode-prompts/skills/output-blocks/references/operational-formats.md
plugins/rootnode-prompts/skills/output-blocks/references/technical-formats.md
plugins/rootnode-prompts/skills/prompt-compilation/SKILL.md
plugins/rootnode-prompts/skills/prompt-compilation/references/compilation-examples.md
plugins/rootnode-prompts/skills/prompt-compilation/references/five-layer-architecture.md
plugins/rootnode-prompts/skills/prompt-validation/SKILL.md
plugins/rootnode-prompts/skills/prompt-validation/references/diagnostic-flow.md
plugins/rootnode-prompts/skills/prompt-validation/references/symptom-fix-map.md
plugins/rootnode-prompts/skills/reasoning-blocks/SKILL.md
plugins/rootnode-prompts/skills/reasoning-blocks/references/analytical-reasoning.md
plugins/rootnode-prompts/skills/reasoning-blocks/references/comparative-reasoning.md
plugins/rootnode-prompts/skills/reasoning-blocks/references/creative-reasoning.md
plugins/rootnode-prompts/skills/reasoning-blocks/references/research-reasoning.md
plugins/rootnode-prompts/skills/reasoning-blocks/references/strategic-reasoning.md
plugins/rootnode-prompts/skills/reasoning-blocks/references/technical-reasoning.md
plugins/rootnode-skill-builder/.claude-plugin/plugin.json
plugins/rootnode-skill-builder/LICENSE
plugins/rootnode-skill-builder/README.md
plugins/rootnode-skill-builder/skills/skill-builder/SKILL.md
plugins/rootnode-skill-builder/skills/skill-builder/agents/analyzer.md
plugins/rootnode-skill-builder/skills/skill-builder/agents/comparator.md
plugins/rootnode-skill-builder/skills/skill-builder/agents/grader.md
plugins/rootnode-skill-builder/skills/skill-builder/eval-viewer/generate_review.py
plugins/rootnode-skill-builder/skills/skill-builder/eval-viewer/viewer.html
plugins/rootnode-skill-builder/skills/skill-builder/references/anti-pattern-catalog.md
plugins/rootnode-skill-builder/skills/skill-builder/references/auto-activation-discipline.md
plugins/rootnode-skill-builder/skills/skill-builder/references/behavioral-validation.md
plugins/rootnode-skill-builder/skills/skill-builder/references/conversion-guide.md
plugins/rootnode-skill-builder/skills/skill-builder/references/decomposition-framework.md
plugins/rootnode-skill-builder/skills/skill-builder/references/description-optimization.md
plugins/rootnode-skill-builder/skills/skill-builder/references/ecosystem-placement-decision.md
plugins/rootnode-skill-builder/skills/skill-builder/references/multi-environment-adaptation.md
plugins/rootnode-skill-builder/skills/skill-builder/references/skills-spec.md
plugins/rootnode-skill-builder/skills/skill-builder/references/tooling-layer-overview.md
plugins/rootnode-skill-builder/skills/skill-builder/references/version-comparison.md
plugins/rootnode-skill-builder/skills/skill-builder/references/warrant-check-criteria.md
plugins/rootnode-skill-builder/skills/skill-builder/scripts/__init__.py
plugins/rootnode-skill-builder/skills/skill-builder/scripts/aggregate_benchmark.py
plugins/rootnode-skill-builder/skills/skill-builder/scripts/description_optimizer.py
plugins/rootnode-skill-builder/skills/skill-builder/scripts/generate_report.py
plugins/rootnode-skill-builder/skills/skill-builder/scripts/package_zip.py
plugins/rootnode-skill-builder/skills/skill-builder/scripts/quick_validate.py
plugins/rootnode-skill-builder/skills/skill-builder/scripts/utils.py
plugins/rootnode-tuning/.claude-plugin/plugin.json
plugins/rootnode-tuning/LICENSE
plugins/rootnode-tuning/README.md
plugins/rootnode-tuning/skills/behavioral-tuning/SKILL.md
plugins/rootnode-tuning/skills/behavioral-tuning/references/countermeasure-templates.md
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
```
433 tracked files. The snapshot itself adds one when committed.

## canonical-kfs roster (7)
_Source: `git ls-files audit/canonical-kfs/`; count via `git ls-files audit/canonical-kfs/ | wc -l`; content changes via `git log --oneline 2c04b70..HEAD -- audit/canonical-kfs`_
```
audit/canonical-kfs/root_AGENT_ANTI_PATTERNS.md
audit/canonical-kfs/root_AGENT_ENVIRONMENT_ARCHITECTURE.md
audit/canonical-kfs/root_AUDIT_FRAMEWORK.md
audit/canonical-kfs/root_CC_ENVIRONMENT_GUIDE.md
audit/canonical-kfs/root_CLAUDE_OPTIMIZATION_NOTES.md
audit/canonical-kfs/root_OPTIMIZATION_REFERENCE.md
audit/canonical-kfs/root_SKILL_BUILD_DISCIPLINE.md
```
Commits touching this path since `2c04b70`: 0.

## audit/v5_0_1-patch/ (v5.0.1 cycle directory)
_Source: `git ls-files audit/v5_0_1-patch/`; count via `git ls-files audit/v5_0_1-patch/ | wc -l`_
```
audit/v5_0_1-patch/refuter_brief_c1.md
audit/v5_0_1-patch/refuter_brief_r2c1.md
audit/v5_0_1-patch/refuter_brief_r3c1.md
audit/v5_0_1-patch/refuter_c1.json
audit/v5_0_1-patch/refuter_r2c1.json
audit/v5_0_1-patch/refuter_r3c1.json
audit/v5_0_1-patch/release-notes-v5.0.1-config.py
audit/v5_0_1-patch/session_report_20261030-0040Z.md
audit/v5_0_1-patch/session_report_20261030-0107Z.md
audit/v5_0_1-patch/session_report_20261030-0224Z.md
audit/v5_0_1-patch/session_report_20261030-0303Z.md
```
11 files.

## audit/v5_0-alignment/ (v5.0 cycle directory)
_Source: `git ls-files audit/v5_0-alignment/`; count via `git ls-files audit/v5_0-alignment/ | wc -l`_
```
audit/v5_0-alignment/5_5GEN_SWEEP_MANIFEST.md
audit/v5_0-alignment/d9a_cc-design_v5.0_20261029-1406Z.md
audit/v5_0-alignment/kf-update-blocks.md
audit/v5_0-alignment/pr_body.md
audit/v5_0-alignment/release-notes-v5.0-config.py
audit/v5_0-alignment/session_report_20261023-0042Z.md
```
6 files.

## audit/v4_0-alignment/ (v4.0 cycle directory)
_Source: `git ls-files audit/v4_0-alignment/`; count via `git ls-files audit/v4_0-alignment/ | wc -l`_
```
audit/v4_0-alignment/5GEN_SWEEP_MANIFEST.md
audit/v4_0-alignment/5GEN_VERIFICATION_LOG.md
audit/v4_0-alignment/dryrun-v3.1-config.py
audit/v4_0-alignment/release-notes-v4.0-config.py
```
4 files.

## Plugins (6)
_Source: `ls plugins`; version and license from each `.claude-plugin/plugin.json`; skill counts via `ls -d plugins/<plugin>/skills/*/ | wc -l`_
```
rootnode-code  version 6.0.0  license Apache-2.0  skills 2
rootnode-governance  version 6.0.0  license Apache-2.0  skills 5
rootnode-projects  version 6.0.0  license Apache-2.0  skills 7
rootnode-prompts  version 6.0.0  license Apache-2.0  skills 11
rootnode-skill-builder  version 6.0.0  license Apache-2.0  skills 1
rootnode-tuning  version 6.0.0  license Apache-2.0  skills 1
```

## Marketplace
_Source: `.claude-plugin/marketplace.json`_
```
name rootnode  pluginRoot ./plugins
rootnode-projects  source rootnode-projects  category audit
rootnode-code  source rootnode-code  category claude-code
rootnode-prompts  source rootnode-prompts  category prompting
rootnode-tuning  source rootnode-tuning  category behavior
rootnode-governance  source rootnode-governance  category runtime
rootnode-skill-builder  source rootnode-skill-builder  category authoring
```

## Skills (plugins/*/skills/ source folders)
_Source: `for d in plugins/*/skills/*/; do echo $d; find $d -maxdepth 1 -mindepth 1 -type d; done`; folder count via `ls -d plugins/*/skills/*/ | wc -l`; versions via `grep -h -m1 -E '^\s+version:' plugins/*/skills/*/SKILL.md | sort | uniq -c`_
```
plugins/rootnode-code/skills/cc-design/
  references
  schema
plugins/rootnode-code/skills/repo-hygiene/
  profiles
  references
  schema
plugins/rootnode-governance/skills/critic-gate/
  examples
  profiles
  references
  schema
plugins/rootnode-governance/skills/handoff-trigger-check/
  profiles
  references
  schema
plugins/rootnode-governance/skills/mode-router/
  configs
  examples
  references
  schema
plugins/rootnode-governance/skills/profile-builder/
  examples
  references
plugins/rootnode-governance/skills/session-handoff/
  references
plugins/rootnode-projects/skills/anti-pattern-detection/
plugins/rootnode-projects/skills/context-budget/
  references
plugins/rootnode-projects/skills/full-stack-audit/
  references
plugins/rootnode-projects/skills/global-audit/
  references
plugins/rootnode-projects/skills/memory-optimization/
  references
plugins/rootnode-projects/skills/project-audit/
  references
plugins/rootnode-projects/skills/project-brief/
  references
plugins/rootnode-prompts/skills/block-selection/
  references
plugins/rootnode-prompts/skills/domain-agentic-context/
  references
plugins/rootnode-prompts/skills/domain-business-strategy/
  references
plugins/rootnode-prompts/skills/domain-content-communications/
  references
plugins/rootnode-prompts/skills/domain-research-analysis/
  references
plugins/rootnode-prompts/skills/domain-software-engineering/
  references
plugins/rootnode-prompts/skills/identity-blocks/
  references
plugins/rootnode-prompts/skills/output-blocks/
  references
plugins/rootnode-prompts/skills/prompt-compilation/
  references
plugins/rootnode-prompts/skills/prompt-validation/
  references
plugins/rootnode-prompts/skills/reasoning-blocks/
  references
plugins/rootnode-skill-builder/skills/skill-builder/
  agents
  eval-viewer
  references
  scripts
plugins/rootnode-tuning/skills/behavioral-tuning/
  references
```
27 folders. SKILL.md versions:
```
     15   version: "5.0.0"
     12   version: "5.0.1"
```

## docs/
_Source: `git ls-files docs/`_
```
docs/root_SKILLS_RELEASE_PLAYBOOK.md
```
Unchanged since `2c04b70`. The playbook still describes the retired zip shapes.

## Repo-root scripts (3)
_Source: `git ls-files | grep -E '^[^/]+\.py$'`; count via same piped to `wc -l`_
```
build_release_artifacts.py
build_releases.py
generate_release_notes.py
```
`build_release_artifacts.py` now emits six plugin zips. `build_releases.py` is superseded and left unchanged; it scans the repo root for `rootnode-*` folders, which no longer exist. `generate_release_notes.py` is unchanged.

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
[staging-kf on disk: 0 files at generation time, gitignored per .gitignore `/design/staging-kf/`]
[tracked at design/ root:
design/root_DESIGN_behavioral-tuning_v5.md
design/root_DESIGN_catalog_v5.0.1_patch.md
design/root_DESIGN_catalog_v5_model_alignment.md
design/root_DESIGN_cc-design_v5.md
design/root_DESIGN_plugin_packaging.md
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

## Recent commits (20)
_Source: `git log --oneline -20`_
```
cb61ad9 fix: harden hooks and packager after review
a056e19 feat: ship the migration guard and bounded Stop hook in rootnode-code
8d6fcc7 feat: add a five-case eval suite to rootnode-projects
1228d47 feat: reduce the packager to six plugin zips
99ca01a feat: add plugin manifests, READMEs, and root marketplace
f34b7ac feat: move 27 Skills into plugin directories and drop the rootnode- prefix
85bc364 docs: add plugin packaging design spec v0.2
e8c64ed Merge pull request #29 from drayline/chore/catalog-v5.0.1
895f7b8 chore(catalog): regenerate for v5.0.1
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
No release notes were added. They ride the release prompt.

## Packager constants
_Source: `grep -nE 'EXPECTED_TOTAL|CATALOG_VERSION' build_release_artifacts.py`_
```
38:EXPECTED_TOTAL = 6
155:    if not specific and total != EXPECTED_TOTAL:
156:        problems.append(f"total {total} != {EXPECTED_TOTAL}")
```
`CATALOG_VERSION` is gone with the catalog bundle. Zip names come from each plugin's manifest.

## Cycle-delta summary vs `root_repo_catalog_20261030.md`

- **Tracked files: 390 → 433 (+43).** `git diff --name-status -M 2c04b70 HEAD`: 43 A, 155 R, 2 M, 0 D. The snapshot itself adds one more when committed.
- **Added files (43):** 6 outside `plugins/` (`.claude-plugin/marketplace.json`, `audit/repo-catalog/root_repo_catalog_20261030.md`, `audit/v5_0_1-patch/refuter_brief_r3c1.md`, `audit/v5_0_1-patch/refuter_r3c1.json`, `audit/v5_0_1-patch/session_report_20261030-0303Z.md`, `design/root_DESIGN_plugin_packaging.md`); 18 per-plugin manifests, READMEs, and LICENSE copies; 4 `rootnode-code` hook files; 15 eval files.
- **Skills folders: 27 → 27, all moved to `plugins/*/skills/`.** Tracked files left at root `rootnode-*/` paths: 0.
- **Plugins: 0 → 6.** Marketplace added at `.claude-plugin/marketplace.json`.
- **Modified:** `.gitignore`, `build_release_artifacts.py`.
- **canonical-kfs, docs/, release-notes/, CHANGELOG.md:** unchanged. Tags 133 and GitHub releases 131: unchanged.
- **design/:** `design/audit-artifacts/v4.2/scratch/` is no longer on disk; the operator moved it out of the repo.
