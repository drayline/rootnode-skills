# rootnode-skills — Repo Catalog
_Generated 2026-09-11 | HEAD a67a6ac00aaca1350238b67df4a08123edf50934 (MA) | regenerated per playbook Post-verification step_

Regenerated 2026-09-11 (local) per `docs/root_SKILLS_RELEASE_PLAYBOOK.md` §Post-verification (line 101). Section structure matches `root_repo_catalog_20260725.md` so the two are diffable. Snapshot captures the v4.1.0 single-Skill cut: `rootnode-cc-design v4.1` released off MA (PR #20 merge commit) with `-cp` + `-cc` zips; `catalog-v4.0` remains Latest (no umbrella recut this cycle); no canonical-KF changes; new tracked reference `rootnode-cc-design/references/cc-delegation-patterns.md`; new release-notes file `release-notes/rootnode-cc-design-v4.1.md`. Every section derives from a live command run at HEAD `a67a6ac`, named next to the section title.

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
release-notes/rootnode-cc-design-v4.1.md
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
rootnode-cc-design/references/cc-delegation-patterns.md
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
Total tracked files: 286 (from `git ls-files | wc -l`).

## canonical-kfs roster (7)
_Source: `git ls-files audit/canonical-kfs/`; count via `git ls-files audit/canonical-kfs/ | wc -l`_
```
audit/canonical-kfs/root_AGENT_ANTI_PATTERNS.md
audit/canonical-kfs/root_AGENT_ENVIRONMENT_ARCHITECTURE.md
audit/canonical-kfs/root_AUDIT_FRAMEWORK.md
audit/canonical-kfs/root_CC_ENVIRONMENT_GUIDE.md
audit/canonical-kfs/root_CLAUDE_OPTIMIZATION_NOTES.md
audit/canonical-kfs/root_OPTIMIZATION_REFERENCE.md
audit/canonical-kfs/root_SKILL_BUILD_DISCIPLINE.md
```
Delta from `root_repo_catalog_20260725.md`: unchanged (7 → 7). This cycle synced no KFs; `design/staging-kf/` is empty. Two KFs (`root_CC_ENVIRONMENT_GUIDE.md`, `root_OPTIMIZATION_REFERENCE.md`) received v4.1 methodology-delta content in the v4.1 build cycle (commit 2bfa3df on MA history) — the roster count is unchanged; only file contents.

## audit/v4_0-alignment/ (v4.0 cycle directory)
_Source: `git ls-files audit/v4_0-alignment/`; count via `git ls-files audit/v4_0-alignment/ | wc -l`_
```
audit/v4_0-alignment/5GEN_SWEEP_MANIFEST.md
audit/v4_0-alignment/5GEN_VERIFICATION_LOG.md
audit/v4_0-alignment/dryrun-v3.1-config.py
audit/v4_0-alignment/release-notes-v4.0-config.py
```
4 files (unchanged from `root_repo_catalog_20260725.md`). This cut did not create a `audit/v4_1-alignment/` cycle directory — v4.1.0 is a single-Skill notes-only release (no per-cycle config, no bundle recut); the v4.0 alignment directory remains the most recent tracked cycle dir.

## Skills (rootnode-*/ source folders)
_Source: `for d in rootnode-*/; do echo $d; find $d -maxdepth 1 -mindepth 1 -type d; done`; folder count via `ls -d rootnode-*/ | wc -l`_
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
Total: 27 Skill source folders (unchanged from prior snapshot). `rootnode-cc-design/` version bumped to 4.1.0; the other 26 Skills remain at 4.0.0. `rootnode-cc-design/references/cc-delegation-patterns.md` is a new tracked file this cycle (v4.1 build absorbing the orchestrator/worker delegation architecture).

## docs/
_Source: `git ls-files docs/`_
```
[tracked]
docs/root_SKILLS_RELEASE_PLAYBOOK.md
[on disk]
(none — no repo-root duplicate present)
```

## Repo-root scripts (3)
_Source: `git ls-files | grep -E '^[^/]+\.py$'`; count via same piped to `wc -l`_
```
build_release_artifacts.py     # release orchestrator (24 -cp flat + 5 -cc wrapper + bundle)
build_releases.py              # legacy flat-only half-tool (retained as reference)
generate_release_notes.py      # v-agnostic release-notes generator (added v4.0, per D7 expansion)
```
Roster unchanged from `root_repo_catalog_20260725.md` (3 → 3). Executable bits were not queried in this snapshot; the file contents themselves are unchanged.

## design/ structure
_Source: `find design -maxdepth 2 -type d` for directories; `git ls-files design/` for tracked files_
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
[staging-kf on disk: empty, gitignored per .gitignore:5 `/design/staging-kf/`]
[tracked at design/ root: root_DS_cc_design_update_rev2.md, root_DS_skill_builder_v3_rev3.4.md, root_skill_5gen_alignment_design.md]
```
Delta from `root_repo_catalog_20260725.md`: unchanged. 15 tracked design files (via `git ls-files design/ | wc -l`).

## Recent commits (20)
_Source: `git log --oneline -20`_
```
a67a6ac Merge pull request #20 from drayline/release/rootnode-cc-design-v4.1.0
a2a4032 release: rootnode-cc-design v4.1.0 notes
02ec81a Merge pull request #19 from drayline/feat/cc-design-v4.1-build
e4cc312 fix(cc-design): v4.1 — ultracode default stated in prose, not only by setting
3589750 feat(cc-design): v4.1 — competing hypotheses and instrument fit for diagnostic prompts
08cbbf7 fix(cc-design): v4.1 Test C fix pass 2 — marker on every mention, JSON placement, ultracode default unconditional
2bfa3df docs(canonical-kfs): sync CC_ENVIRONMENT_GUIDE and OPTIMIZATION_REFERENCE to v4.1 deltas
2246205 fix(cc-design): v4.1 Test C fixes — product-fact emission marker, digest-gate scope, role-table restraint
d3743c2 docs(cc-design): add end-state rationale to close SKILL.md forward-ref
bf226fa docs(cc-design): bind digest gates to LF-normalized content
51f7e64 feat(cc-design): v4.1.0 — delegation architecture + end-state assertion rule
6350e2b Merge pull request #18 from drayline/chore/aea-5.5-fourth-location
e6217cc docs: AEA 5.5 three-to-four landing locations (O11)
79e7fa4 Merge pull request #17 from drayline/chore/v4.0-catalog-regen
01ef63f chore(catalog): regenerate for v4.0 + correct two-script roster claims
3bff810 Merge pull request #16 from drayline/release/v4.0
a0f08e2 feat(release): v4.0 release notes — 27 per-Skill + catalog umbrella
0f4c00a chore(release): bump CATALOG_VERSION to v4.0 in build_release_artifacts.py
533cabb sync(canonical-kfs): v4.0 methodology updates + D8 mirror completion
65f6094 feat(release): W2c three-check corrections + version-agnostic release-notes generator
```

## Tags (91)
_Source: `git tag --list`; count via `git tag --list | wc -l`_
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
rootnode-cc-design/v4.1
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
Delta from `root_repo_catalog_20260725.md`: +1 tag (`rootnode-cc-design/v4.1`), 0 removed. Total 90 → 91. The two-part `vN.N` precision convention for `rootnode-<skill>/` tags is preserved (v4.1 matches v4.0 and v3.1 shape).

## GitHub releases
_Source: `gh release list --limit 100`; row count via `wc -l` (89 rows, <100 asserts non-truncated)_
```
rootnode-cc-design v4.1		rootnode-cc-design/v4.1	2026-09-11T17:10:08Z
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
Delta from `root_repo_catalog_20260725.md`: +1 release (`rootnode-cc-design v4.1` published 2026-09-11 pointing at MA). `catalog-v4.0` retains `Latest` marker (single-Skill cut used `--latest=false`; README `/releases/latest` links continue to resolve to the umbrella). No other release altered. Row count = 89 (< 100, so the `--limit 100` list is not truncated).

## release-notes/ v4.1 files
_Source: `ls release-notes/ | grep v4.1`; count via same piped to `wc -l`_
```
release-notes/rootnode-cc-design-v4.1.md
```
1 file added this cycle (single-Skill cut; no umbrella notes). Generated by hand from the release prompt's NOTES block, committed on `release/rootnode-cc-design-v4.1.0` at a2a4032 and landed on main via PR #20. v3.1 and v4.0 notes preserved (append-only for shipped releases).

## CATALOG_VERSION
_Source: `grep -n 'CATALOG_VERSION' build_release_artifacts.py`_
```
59:CATALOG_VERSION = "v4.0"
109:    bundle = DIST_DIR / f"rootnode-catalog-{CATALOG_VERSION}.zip"
176:              f"  -> upload to the catalog-{CATALOG_VERSION} release")
```
Unchanged (still `"v4.0"`) — this cycle did not cut a new catalog umbrella and did not touch the packager. Bundle output filename `rootnode-catalog-v4.0.zip` remains the packager's default artifact.

## Cycle-delta summary vs `root_repo_catalog_20260725.md`

- **Tracked files: 283 → 286 (+3).** Additions: `audit/repo-catalog/root_repo_catalog_20260725.md` (the prior snapshot's file was not in its own snapshot; landed via PR #17 shortly after the snapshot was produced), `release-notes/rootnode-cc-design-v4.1.md`, `rootnode-cc-design/references/cc-delegation-patterns.md`. Removals: 0.
- **canonical-kfs roster: 7 → 7 (unchanged).** No KF sync this cycle; two KFs received v4.1 methodology-delta content updates (roster unchanged).
- **Repo-root scripts: 3 → 3 (unchanged).**
- **audit/v4_0-alignment/: 4 → 4 (unchanged).** No `v4_1-alignment` directory created (single-Skill cut has no per-cycle config).
- **Skills folders: 27 → 27 (unchanged).** `rootnode-cc-design` bumped from 4.0.0 → 4.1.0.
- **design/: unchanged.** `design/staging-kf/` remains empty and gitignored.
- **Tags: 90 → 91 (+1).** New: `rootnode-cc-design/v4.1` pointing at MA (`a67a6ac`).
- **GitHub releases: +1.** New: `rootnode-cc-design v4.1` published 2026-09-11T17:10:08Z; assets `rootnode-cc-design-cp.zip` + `rootnode-cc-design-cc.zip`. `catalog-v4.0` retains `Latest`.
- **release-notes/: +1 file.** `rootnode-cc-design-v4.1.md`.
- **CATALOG_VERSION: unchanged (`"v4.0"`).** No umbrella cut this cycle.
