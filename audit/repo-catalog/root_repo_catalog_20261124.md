# rootnode-skills — Repo Catalog
_Generated 2026-11-24 (UTC) | HEAD 908a77108674ffcffbf8eeb37cc42a5440decaaf (chore/catalog-v6.1, branched from `main` at the v6.1 merge commit) | regenerated per playbook Post-verification step_

Regenerated 2026-11-24 after the catalog v6.1 release: PR #35 merged as `908a771`, six per-plugin releases (`<plugin>/v6.1.0` for five plugins, `rootnode-code/v6.2.0`) and the `catalog-v6.1` umbrella (Latest) created from that commit. Since the 2026-11-03 snapshot, PR #33 (marketplace sources) and PR #34 (`rootnode-code` 6.1.0, single-plugin release `rootnode-code/v6.1.0`) also merged. Every section below comes from the command named under its heading.

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
audit/repo-catalog/root_repo_catalog_20261102.md
audit/repo-catalog/root_repo_catalog_20261103.md
audit/repo-catalog/root_repo_catalog_20261124.md
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
audit/v6_0-release/release-notes-v6.0-config.py
audit/v6_1-release/d7-classification.md
audit/v6_1-release/fable51-classification.md
audit/v6_1-release/hook-tests/fixtures/all.json
audit/v6_1-release/hook-tests/fixtures/clamp.json
audit/v6_1-release/hook-tests/fixtures/enforce.json
audit/v6_1-release/hook-tests/fixtures/fail.json
audit/v6_1-release/hook-tests/fixtures/guard-off.json
audit/v6_1-release/hook-tests/fixtures/guard.json
audit/v6_1-release/hook-tests/fixtures/invalid.json
audit/v6_1-release/hook-tests/fixtures/own-evidence.json
audit/v6_1-release/hook-tests/fixtures/package.json
audit/v6_1-release/hook-tests/fixtures/remote.json
audit/v6_1-release/hook-tests/fixtures/watch.json
audit/v6_1-release/hook-tests/run.sh
audit/v6_1-release/kf-update-blocks.md
audit/v6_1-release/release-notes-v6.1-config.py
audit/v6_1-release/rigor-check/B1.txt
audit/v6_1-release/rigor-check/B2.txt
audit/v6_1-release/rigor-check/B3.txt
audit/v6_1-release/rigor-check/out/B1-6.2.0-fix.md
audit/v6_1-release/rigor-check/out/B1-6.2.0-fix.meta
audit/v6_1-release/rigor-check/out/B1-6.2.0.md
audit/v6_1-release/rigor-check/out/B1-6.2.0.meta
audit/v6_1-release/rigor-check/out/B1-control-6.1.0.md
audit/v6_1-release/rigor-check/out/B1-control-6.1.0.meta
audit/v6_1-release/rigor-check/out/B2-6.2.0-fix.md
audit/v6_1-release/rigor-check/out/B2-6.2.0-fix.meta
audit/v6_1-release/rigor-check/out/B2-6.2.0.md
audit/v6_1-release/rigor-check/out/B2-6.2.0.meta
audit/v6_1-release/rigor-check/out/B3-6.2.0-fix.md
audit/v6_1-release/rigor-check/out/B3-6.2.0-fix.meta
audit/v6_1-release/rigor-check/out/B3-6.2.0.md
audit/v6_1-release/rigor-check/out/B3-6.2.0.meta
audit/v6_1-release/rigor-check/results-v1.txt
audit/v6_1-release/rigor-check/results-v2.txt
audit/v6_1-release/rigor-check/results.md
audit/v6_1-release/rigor-check/run.sh
audit/v6_1-release/rigor-check/score.sh
build_release_artifacts.py
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
design/root_DESIGN_fable_5_2_alignment.md
design/root_DESIGN_plugin_packaging.md
design/root_DESIGN_verify_gate_fix.md
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
plugins/rootnode-code/scripts/gate-baseline.sh
plugins/rootnode-code/scripts/gate-lib.sh
plugins/rootnode-code/scripts/gate-status.sh
plugins/rootnode-code/scripts/guard-migrations.sh
plugins/rootnode-code/scripts/record-test-evidence.sh
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
release-notes/catalog-v6.0.md
release-notes/catalog-v6.1.md
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
release-notes/rootnode-code-v6.0.0.md
release-notes/rootnode-code-v6.1.0.md
release-notes/rootnode-code-v6.2.0.md
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
release-notes/rootnode-governance-v6.0.0.md
release-notes/rootnode-governance-v6.1.0.md
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
release-notes/rootnode-projects-v6.0.0.md
release-notes/rootnode-projects-v6.1.0.md
release-notes/rootnode-prompt-compilation-v3.1.md
release-notes/rootnode-prompt-compilation-v4.0.md
release-notes/rootnode-prompt-compilation-v5.0.1.md
release-notes/rootnode-prompt-compilation-v5.0.md
release-notes/rootnode-prompt-validation-v3.1.md
release-notes/rootnode-prompt-validation-v4.0.md
release-notes/rootnode-prompt-validation-v5.0.1.md
release-notes/rootnode-prompt-validation-v5.0.md
release-notes/rootnode-prompts-v6.0.0.md
release-notes/rootnode-prompts-v6.1.0.md
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
release-notes/rootnode-skill-builder-v6.0.0.md
release-notes/rootnode-skill-builder-v6.1.0.md
release-notes/rootnode-tuning-v6.0.0.md
release-notes/rootnode-tuning-v6.1.0.md
```
495 tracked files, including this snapshot as staged at the generation HEAD.

## canonical-kfs roster (7)
_Source: `git ls-files audit/canonical-kfs/`; count via `git ls-files audit/canonical-kfs/ | wc -l`; content changes via `git log --oneline 49ec22a..HEAD -- audit/canonical-kfs`_
```
audit/canonical-kfs/root_AGENT_ANTI_PATTERNS.md
audit/canonical-kfs/root_AGENT_ENVIRONMENT_ARCHITECTURE.md
audit/canonical-kfs/root_AUDIT_FRAMEWORK.md
audit/canonical-kfs/root_CC_ENVIRONMENT_GUIDE.md
audit/canonical-kfs/root_CLAUDE_OPTIMIZATION_NOTES.md
audit/canonical-kfs/root_OPTIMIZATION_REFERENCE.md
audit/canonical-kfs/root_SKILL_BUILD_DISCIPLINE.md
```
Commits touching this path since `49ec22a`: 4 (`f7c0850 fix: refuter findings on catalog v6.1`; `326ced8 feat: Skills for Fable 5.2 alignment and scale-fit rigor (catalog v6.1)`; `11c5d30 docs: knowledge files for Fable 5.2 alignment (catalog v6.1)`; `98941da docs: sync SBD and release playbook for the marketplace source rule`). All seven were edited by the catalog v6.1 spec's §7 KF route (repo copies first; the operator uploads them to the seed Project after the merge).

## audit/v6_1-release/ (v6.1 cycle directory (also holds the rootnode-code 6.1.0 hook harness))
_Source: `git ls-files audit/v6_1-release/`; count via `git ls-files audit/v6_1-release/ | wc -l`_
```
audit/v6_1-release/d7-classification.md
audit/v6_1-release/fable51-classification.md
audit/v6_1-release/hook-tests/fixtures/all.json
audit/v6_1-release/hook-tests/fixtures/clamp.json
audit/v6_1-release/hook-tests/fixtures/enforce.json
audit/v6_1-release/hook-tests/fixtures/fail.json
audit/v6_1-release/hook-tests/fixtures/guard-off.json
audit/v6_1-release/hook-tests/fixtures/guard.json
audit/v6_1-release/hook-tests/fixtures/invalid.json
audit/v6_1-release/hook-tests/fixtures/own-evidence.json
audit/v6_1-release/hook-tests/fixtures/package.json
audit/v6_1-release/hook-tests/fixtures/remote.json
audit/v6_1-release/hook-tests/fixtures/watch.json
audit/v6_1-release/hook-tests/run.sh
audit/v6_1-release/kf-update-blocks.md
audit/v6_1-release/release-notes-v6.1-config.py
audit/v6_1-release/rigor-check/B1.txt
audit/v6_1-release/rigor-check/B2.txt
audit/v6_1-release/rigor-check/B3.txt
audit/v6_1-release/rigor-check/out/B1-6.2.0-fix.md
audit/v6_1-release/rigor-check/out/B1-6.2.0-fix.meta
audit/v6_1-release/rigor-check/out/B1-6.2.0.md
audit/v6_1-release/rigor-check/out/B1-6.2.0.meta
audit/v6_1-release/rigor-check/out/B1-control-6.1.0.md
audit/v6_1-release/rigor-check/out/B1-control-6.1.0.meta
audit/v6_1-release/rigor-check/out/B2-6.2.0-fix.md
audit/v6_1-release/rigor-check/out/B2-6.2.0-fix.meta
audit/v6_1-release/rigor-check/out/B2-6.2.0.md
audit/v6_1-release/rigor-check/out/B2-6.2.0.meta
audit/v6_1-release/rigor-check/out/B3-6.2.0-fix.md
audit/v6_1-release/rigor-check/out/B3-6.2.0-fix.meta
audit/v6_1-release/rigor-check/out/B3-6.2.0.md
audit/v6_1-release/rigor-check/out/B3-6.2.0.meta
audit/v6_1-release/rigor-check/results-v1.txt
audit/v6_1-release/rigor-check/results-v2.txt
audit/v6_1-release/rigor-check/results.md
audit/v6_1-release/rigor-check/run.sh
audit/v6_1-release/rigor-check/score.sh
```
38 files.

## audit/v6_0-release/ (v6.0 cycle directory)
_Source: `git ls-files audit/v6_0-release/`; count via `git ls-files audit/v6_0-release/ | wc -l`_
```
audit/v6_0-release/release-notes-v6.0-config.py
```
1 file.

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
rootnode-code  version 6.2.0  license Apache-2.0  skills 2
rootnode-governance  version 6.1.0  license Apache-2.0  skills 5
rootnode-projects  version 6.1.0  license Apache-2.0  skills 7
rootnode-prompts  version 6.1.0  license Apache-2.0  skills 11
rootnode-skill-builder  version 6.1.0  license Apache-2.0  skills 1
rootnode-tuning  version 6.1.0  license Apache-2.0  skills 1
```

## Marketplace
_Source: `.claude-plugin/marketplace.json`_
```
name rootnode  (no pluginRoot)
rootnode-projects  source ./plugins/rootnode-projects  category audit
rootnode-code  source ./plugins/rootnode-code  category claude-code
rootnode-prompts  source ./plugins/rootnode-prompts  category prompting
rootnode-tuning  source ./plugins/rootnode-tuning  category behavior
rootnode-governance  source ./plugins/rootnode-governance  category runtime
rootnode-skill-builder  source ./plugins/rootnode-skill-builder  category authoring
```
The 2026-11-03 snapshot recorded `pluginRoot ./plugins` with bare sources; PR #33 replaced it with a `./plugins/<name>` source per plugin.

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
    25   version: "6.1.0"
     2   version: "6.2.0"
```
Predecessor lines per SKILL.md (count of files, lines per file):
```
    27 1
```

## docs/
_Source: `git ls-files docs/`_
```
docs/root_SKILLS_RELEASE_PLAYBOOK.md
```
Commits touching `docs/` since `49ec22a`: 2 (`11c5d30 docs: knowledge files for Fable 5.2 alignment (catalog v6.1)`; `98941da docs: sync SBD and release playbook for the marketplace source rule`).

## Repo-root scripts (2)
_Source: `git ls-files | grep -E '^[^/]+\.py$'`; count via same piped to `wc -l`_
```
build_release_artifacts.py
generate_release_notes.py
```
Unchanged this cycle: `git log --oneline 49ec22a..HEAD -- build_release_artifacts.py generate_release_notes.py` lists 0 commits.

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
design/root_DESIGN_fable_5_2_alignment.md
design/root_DESIGN_plugin_packaging.md
design/root_DESIGN_verify_gate_fix.md
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
908a771 Merge pull request #35 from drayline/release/v6.1
f7c0850 fix: refuter findings on catalog v6.1
7f29869 test: cc-design rigor check (spec 7.8) and its one fix pass
7ca8c99 docs: release notes, CHANGELOG and README for catalog v6.1
9aa09fd fix: hook harness hides one tool by a folder of links; verify-gate spec v1.1
326ced8 feat: Skills for Fable 5.2 alignment and scale-fit rigor (catalog v6.1)
11c5d30 docs: knowledge files for Fable 5.2 alignment (catalog v6.1)
07ae3fa Merge pull request #34 from drayline/fix/rootnode-code-6.1.0
5fb7b4b fix: rootnode-code 6.1.0 — opt-in, change-aware hooks (docs, refuter fixes)
e4adb89 fix: rootnode-code hooks opt-in and change-aware (scripts, harness)
8670edc Merge pull request #33 from drayline/fix/marketplace-sources
98941da docs: sync SBD and release playbook for the marketplace source rule
2879301 fix: explicit ./plugins sources in marketplace.json for claude.ai sync
288728b Merge pull request #32 from drayline/chore/catalog-v6.0
49ec22a chore(catalog): regenerate for v6.0
45cf2bd Merge pull request #31 from drayline/release/v6.0
4cce46d release: per-plugin release notes, umbrella notes and CHANGELOG for catalog v6.0
ea55a06 chore: packager clears stale zips and checks embedded copies; drop build_releases.py
7bd17b8 fix: align Skill content with the shipped plugin layout for v6.0
e42b662 docs: move CLAUDE.md and README to the plugin marketplace model
```

## Tags (148)
_Source: `git tag --list` (after `git fetch --tags`); count via `git tag --list | wc -l`_
```
catalog-v3.0
catalog-v3.1
catalog-v4.0
catalog-v5.0
catalog-v5.0.1
catalog-v6.0
catalog-v6.1
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
rootnode-code/v6.0.0
rootnode-code/v6.1.0
rootnode-code/v6.2.0
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
rootnode-governance/v6.0.0
rootnode-governance/v6.1.0
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
rootnode-projects/v6.0.0
rootnode-projects/v6.1.0
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
rootnode-prompts/v6.0.0
rootnode-prompts/v6.1.0
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
rootnode-skill-builder/v6.0.0
rootnode-skill-builder/v6.1.0
rootnode-tuning/v6.0.0
rootnode-tuning/v6.1.0
skill-builder/v3.0
v1.0
v1.1
v1.2
v2.0.0
v2.1
```

## GitHub releases
_Source: `gh release list --limit 200`; row count via `wc -l` (146 rows, <200 asserts non-truncated)_
```
root.node catalog v6.1	Latest	catalog-v6.1	2026-11-24T21:52:25Z
rootnode-skill-builder v6.1.0		rootnode-skill-builder/v6.1.0	2026-11-24T21:52:16Z
rootnode-governance v6.1.0		rootnode-governance/v6.1.0	2026-11-24T21:52:13Z
rootnode-tuning v6.1.0		rootnode-tuning/v6.1.0	2026-11-24T21:52:10Z
rootnode-prompts v6.1.0		rootnode-prompts/v6.1.0	2026-11-24T21:52:07Z
rootnode-code v6.2.0		rootnode-code/v6.2.0	2026-11-24T21:52:04Z
rootnode-projects v6.1.0		rootnode-projects/v6.1.0	2026-11-24T21:52:01Z
rootnode-code v6.1.0		rootnode-code/v6.1.0	2026-11-24T16:25:34Z
root.node catalog v6.0		catalog-v6.0	2026-11-03T03:49:53Z
rootnode-skill-builder v6.0.0		rootnode-skill-builder/v6.0.0	2026-11-03T03:49:39Z
rootnode-governance v6.0.0		rootnode-governance/v6.0.0	2026-11-03T03:49:36Z
rootnode-tuning v6.0.0		rootnode-tuning/v6.0.0	2026-11-03T03:49:33Z
rootnode-prompts v6.0.0		rootnode-prompts/v6.0.0	2026-11-03T03:49:29Z
rootnode-code v6.0.0		rootnode-code/v6.0.0	2026-11-03T03:49:26Z
rootnode-projects v6.0.0		rootnode-projects/v6.0.0	2026-11-03T03:49:23Z
catalog-v5.0.1		catalog-v5.0.1	2026-10-30T12:58:51Z
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

## release-notes/ v6.1-cycle files
_Source: `git ls-files release-notes/ | grep -E 'v6\.(1|2)\.0|catalog-v6\.1'`_
```
release-notes/catalog-v6.1.md
release-notes/rootnode-code-v6.1.0.md
release-notes/rootnode-code-v6.2.0.md
release-notes/rootnode-governance-v6.1.0.md
release-notes/rootnode-projects-v6.1.0.md
release-notes/rootnode-prompts-v6.1.0.md
release-notes/rootnode-skill-builder-v6.1.0.md
release-notes/rootnode-tuning-v6.1.0.md
```
8 files: `rootnode-code-v6.1.0.md` (single-plugin release, PR #34), six catalog v6.1 per-plugin notes and the umbrella.

## Packager constants
_Source: `grep -nE 'EXPECTED_TOTAL|CATALOG_VERSION|SHIPPED_MARKER' build_release_artifacts.py`_
```
46:EXPECTED_TOTAL = 6
55:SHIPPED_MARKER = re.compile(r"<!--\s*shipped:\s*(\S+)\s*-->")
155:            m = SHIPPED_MARKER.search(line)
249:    if not specific and total != EXPECTED_TOTAL:
250:        problems.append(f"total {total} != {EXPECTED_TOTAL}")
```
Zip names come from each plugin's manifest.

## Cycle-delta summary vs `root_repo_catalog_20261103.md`

- **Tracked files: 442 → 495 (+53).** Base `49ec22a` (the commit that added the prior snapshot, 442 files). `git diff --cached --name-status -M 49ec22a` (the index at generation, so this snapshot counts): 53 A, 0 D, 59 M.
- **Added (53):** audit/repo-catalog/ 1, audit/v6_1-release/ 38, design/ 2, plugins/rootnode-code/scripts/ 4, release-notes/ 8. Full list: `git diff --cached --name-status -M 49ec22a | grep ^A`.
- **Deleted (0):** none.
- **Tags: 140 → 148 (+8).** New since `49ec22a`: `catalog-v6.1`, `rootnode-code/v6.1.0`, `rootnode-code/v6.2.0`, `rootnode-governance/v6.1.0`, `rootnode-projects/v6.1.0`, `rootnode-prompts/v6.1.0`, `rootnode-skill-builder/v6.1.0`, `rootnode-tuning/v6.1.0`.
- **GitHub releases: 138 → 146 (+8).** Latest: `catalog-v6.1`.
- **Marketplace:** `pluginRoot ./plugins` with bare sources → a `./plugins/<name>` source per plugin (PR #33).
- **canonical-kfs roster: 7 → 7.** All seven edited in this cycle; the playbook too.
- **Skills: 27 folders;** versions 25 at "6.1.0", 2 at "6.2.0". Plugins 6: five at 6.1.0, `rootnode-code` at 6.2.0.
- **Repo-root scripts: 2** (unchanged).
- **design/staging-kf/ (gitignored): 0 files on disk** (the eight v6.1 inputs were cleared after the sync).
