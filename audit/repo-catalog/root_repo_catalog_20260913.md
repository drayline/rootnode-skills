# rootnode-skills — Repo Catalog
_Generated 2026-09-13 | HEAD 4ecaa7fc71807632170a4fe2fdb816e08a9b130f (MM) | regenerated per playbook Post-verification step_

Regenerated 2026-09-13 (local) per `docs/root_SKILLS_RELEASE_PLAYBOOK.md` §Post-verification (line 114). Section structure matches `root_repo_catalog_20260911.md` so the two are diffable. Snapshot captures the v4.2.0 single-Skill cut per playbook §1.5: `rootnode-cc-design v4.2.0` released off MM (PR #23 merge commit) with `-cp` + `-cc` zips, `--latest=false` restored on the release via `gh release edit catalog-v4.0 --latest` after an initial auto-promotion (see cycle-delta summary). No new tracked files in the Skill this cycle; three canonical-KF/doc files received methodology-delta content (D7 to `root_SKILL_BUILD_DISCIPLINE.md`, D10 to `root_CC_ENVIRONMENT_GUIDE.md`, D9 to `docs/root_SKILLS_RELEASE_PLAYBOOK.md`). No release-notes file was added this cycle — the release used inline `--notes` rather than a `release-notes/` file. Every section derives from a live command run at HEAD `4ecaa7f`, named next to the section title.

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
Total tracked files: 287 (from `git ls-files | wc -l`).

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
Delta from `root_repo_catalog_20260911.md`: roster unchanged (7 → 7). Two mirror KFs updated in-place this cycle by the v4.2 build's KF mirror deltas: `root_SKILL_BUILD_DISCIPLINE.md` (KF Delta 7 — §3.9 D9a arm hygiene reason replaced) and `root_CC_ENVIRONMENT_GUIDE.md` (KF Delta 10 — new §5.9 turn-economy rule appended to §5). No staged KFs at `design/staging-kf/`.

## audit/v4_0-alignment/ (v4.0 cycle directory)
_Source: `git ls-files audit/v4_0-alignment/`; count via `git ls-files audit/v4_0-alignment/ | wc -l`_
```
audit/v4_0-alignment/5GEN_SWEEP_MANIFEST.md
audit/v4_0-alignment/5GEN_VERIFICATION_LOG.md
audit/v4_0-alignment/dryrun-v3.1-config.py
audit/v4_0-alignment/release-notes-v4.0-config.py
```
4 files (unchanged from `root_repo_catalog_20260911.md`). v4.2.0 is a single-Skill cut per playbook §1.5: no per-cycle config, no bundle recut, no new alignment directory. The v4.0 alignment directory remains the most recent tracked cycle dir.

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
Total: 27 Skill source folders (unchanged from prior snapshot). `rootnode-cc-design/` version bumped to 4.2.0; the other 26 Skills remain at 4.0.0. No new tracked reference files this cycle — the v4.2 build extended existing references (cc-anti-patterns.md grew by two entries + TOC, cc-delegation-patterns.md grew by orchestration-primitives §9 and CLAUDE_CODE_* version annotations, cc-methodology-patterns.md grew by the Routines section) and shrank `rootnode-cc-design/SKILL.md` via the Phase A extraction pass (description trim, changelog extraction, metadata trim, dedup against references).

## docs/
_Source: `git ls-files docs/`_
```
[tracked]
docs/root_SKILLS_RELEASE_PLAYBOOK.md
[on disk]
(none — no repo-root duplicate present)
```
The playbook received the KF Delta 9 addition this cycle — a new §1.5 documenting the single-Skill cut as a supported release shape (per-Skill release only, no umbrella, `catalog-vN` retains `--latest`, condition list, promote-to-full triggers, anti-churn on Latest flip).

## Repo-root scripts (3)
_Source: `git ls-files | grep -E '^[^/]+\.py$'`; count via same piped to `wc -l`_
```
build_release_artifacts.py     # release orchestrator (24 -cp flat + 5 -cc wrapper + bundle)
build_releases.py              # legacy flat-only half-tool (retained as reference)
generate_release_notes.py      # v-agnostic release-notes generator (added v4.0, per D7 expansion)
```
Roster unchanged from `root_repo_catalog_20260911.md` (3 → 3). The v4.2 cycle did not touch the packager or the notes generator; the single-Skill cut was executed manually via `python build_release_artifacts.py rootnode-cc-design` and `gh release create` (see release cut prompt for the specific invocation).

## design/ structure
_Source: `find design -maxdepth 2 -type d` for directories; `git ls-files design/` for tracked files_
```
design
design/audit-artifacts
design/audit-artifacts/v2.1
design/audit-artifacts/v3.0
design/audit-artifacts/v4.2                     # NEW on disk, untracked (v4.2 build audit artifacts)
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
Delta from `root_repo_catalog_20260911.md`: `design/audit-artifacts/v4.2/` present on disk (untracked). Contains the v4.2 build inputs — `root_CC_DESIGN_v42_spec.md`, `root_CC_LANDSCAPE_20260911.md`, `v42_inventory_report.md`, and a `scratch/` subdirectory. Tracked design-file count unchanged at 15 (via `git ls-files design/ | wc -l`).

## Recent commits (20)
_Source: `git log --oneline -20`_
```
4ecaa7f Merge pull request #23 from drayline/feat/cc-design-v4.2-build
d3303eb E4: version bump to 4.2.0
b646607 E3: playbook — single-Skill cut shape (KF Delta 9)
cf77633 E2: CC_EG mirror — turn-economy rule §5.9 (KF Delta 10)
2c6a6da E1: SBD mirror — D9a arm hygiene reason (KF Delta 7)
e219a76 C: fix mode-to-reference routing
1c4efc1 B10: version-annotate all CLAUDE_CODE_* variables
891eb7e B9: add orchestration taxonomy
b9e0a2a B8: ratify qualitative orchestrator hygiene
c7d3a02 B7: Builder tier-switch mechanism
b990c64 B6: update layer-fit framing
ec9cba1 B5: add written-deliverable length rule
c494736 B4: add thinking:disabled xhigh/max 400 reminder
cfe9371 B3: add TOC to cc-anti-patterns.md
df9dfc3 B2: add verification-instruction-accumulation and conservative-review-literalism anti-patterns
ac17a92 B1: add Routines coverage
0aa024a A4: deduplicate SKILL.md body against references
bfdb415 A3: trim metadata.original-source
9f592a8 A2: extract v4.0/v4.1 changelog to references
7d8ef2e A1: shrink description, move triggers to body activation table
```

## Tags (92)
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
rootnode-cc-design/v4.2
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
Delta from `root_repo_catalog_20260911.md`: +1 tag (`rootnode-cc-design/v4.2`), 0 removed. Total 91 → 92. The uniform `rootnode-<skill>/vN.N` convention holds; the two-part precision (`v4.2`, matching `v4.0` / `v4.1` / `v3.1`) is preserved.

## GitHub releases
_Source: `gh release list --limit 100`; row count via `wc -l` (90 rows, <100 asserts non-truncated)_
```
rootnode-cc-design v4.2.0		rootnode-cc-design/v4.2	2026-09-13T07:11:02Z
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
Delta from `root_repo_catalog_20260911.md`: +1 release (`rootnode-cc-design v4.2.0` published 2026-09-13T07:11:02Z pointing at MM `4ecaa7f`); assets `rootnode-cc-design-cp.zip` + `rootnode-cc-design-cc.zip`. **`Latest` remains on `catalog-v4.0`** — an initial auto-promotion of `rootnode-cc-design/v4.2` to `Latest` (the release cut command did not pass `--latest=false`) was corrected mid-session by `gh release edit catalog-v4.0 --latest`. Row count = 90 (< 100, so the `--limit 100` list is not truncated).

## release-notes/ v4.1 / v4.2 files
_Source: `ls release-notes/ | grep -E 'v4\.[12]'`_
```
release-notes/rootnode-cc-design-v4.1.md
```
0 new files added this cycle. The v4.2 release used inline `--notes "..."` in the `gh release create` invocation rather than a `release-notes/` file; per the single-Skill cut shape, no catalog umbrella notes were produced either. v3.1, v4.0, and v4.1 notes preserved (append-only for shipped releases).

## CATALOG_VERSION
_Source: `grep -n 'CATALOG_VERSION' build_release_artifacts.py`_
```
59:CATALOG_VERSION = "v4.0"
109:    bundle = DIST_DIR / f"rootnode-catalog-{CATALOG_VERSION}.zip"
176:              f"  -> upload to the catalog-{CATALOG_VERSION} release")
```
Unchanged (still `"v4.0"`) — this cycle did not cut a new catalog umbrella and did not touch the packager. Bundle output filename `rootnode-catalog-v4.0.zip` remains the packager's default artifact.

## Cycle-delta summary vs `root_repo_catalog_20260911.md`

- **Tracked files: 286 → 287 (+1).** Additions: `audit/repo-catalog/root_repo_catalog_20260911.md` (the prior snapshot's file was not in its own snapshot; landed via that snapshot's follow-up hygiene PR). Removals: 0.
- **canonical-kfs roster: 7 → 7 (unchanged).** No KF sync this cycle; two mirrors received methodology-delta content updates in place: `root_SKILL_BUILD_DISCIPLINE.md` (Delta 7 — §3.9 D9a arm hygiene reason: "Skills load at launch" → "hot-reload is confirmed on Claude Code 2.1.136, but installing before launch removes the question from the run") and `root_CC_ENVIRONMENT_GUIDE.md` (Delta 10 — new §5.9 turn-economy rule appended to §5).
- **Repo-root scripts: 3 → 3 (unchanged).**
- **audit/v4_0-alignment/: 4 → 4 (unchanged).** No `v4_2-alignment` directory created (single-Skill cut has no per-cycle config).
- **Skills folders: 27 → 27 (unchanged).** `rootnode-cc-design` bumped from 4.1.0 → 4.2.0. No new tracked reference files this cycle. `rootnode-cc-design/SKILL.md` shrank from 36,751 → 31,931 bytes (−13.1%); `rootnode-cc-design/references/cc-anti-patterns.md` grew (Phase B2 added §10a and §10b, Phase B3 added TOC); `rootnode-cc-design/references/cc-delegation-patterns.md` grew (Phase B4 thinking:disabled reminder, B7 Builder tier-switch mechanism, B8 orchestrator hygiene threshold note, B9 §9 orchestration-primitives taxonomy, B10 CLAUDE_CODE_* version annotations, plus the Fable/Opus5/Sonnet5 selection tradeoff added in A2's Phase-A pre-work); `rootnode-cc-design/references/cc-methodology-patterns.md` grew (Phase B1 Routines-as-CC-deployment-surface section).
- **docs/: content change to `root_SKILLS_RELEASE_PLAYBOOK.md`.** New §1.5 "Alternate release shape — the single-Skill cut" documents this cycle's release shape as a first-class option distinct from the full-catalog release; conditions and anti-churn on Latest flip preserved.
- **design/: `design/audit-artifacts/v4.2/` present on disk (untracked).** Contains v4.2 build inputs — `root_CC_DESIGN_v42_spec.md`, `root_CC_LANDSCAPE_20260911.md`, `v42_inventory_report.md`, and a `scratch/` subdirectory. Tracked design-file count unchanged (15).
- **Tags: 91 → 92 (+1).** New: `rootnode-cc-design/v4.2` pointing at MM (`4ecaa7f`).
- **GitHub releases: +1.** New: `rootnode-cc-design v4.2.0` published 2026-09-13T07:11:02Z; assets `rootnode-cc-design-cp.zip` + `rootnode-cc-design-cc.zip`. `catalog-v4.0` retains `Latest` (single-Skill cut shape per playbook §1.5; an initial auto-promotion of the v4.2 release to Latest was corrected mid-session via `gh release edit catalog-v4.0 --latest`).
- **release-notes/: no new files.** The v4.2 release used inline `--notes` in the `gh release create` invocation.
- **CATALOG_VERSION: unchanged (`"v4.0"`).** No umbrella cut this cycle.
