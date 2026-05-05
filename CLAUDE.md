# Phase 31d Remediation — rootnode-skills

## R1. Mission

Apply two streams of changes to `drayline/rootnode-skills`. Stream B1: Phase 31c audit findings + amendment corrections. Stream B2: CC Ecosystem Skills Impact Eval. All work on branch `phase-31d-remediation` (created and staged by operator before this session). Sequential commits, one logical change per commit. Task specs in `WORK_QUEUE.md`.

Methodology grounding lives in the seed Project's canonical KFs (`root_*.md`). Operator pre-staged current versions at `audit/canonical-kfs/` for in-repo access. The agent reads these via `@audit/canonical-kfs/<filename>` references during execution.

## R2. Authority Matrix

| Tier | Content class | Authority |
|---|---|---|
| Tier 1 — Locked | Skill `name:` fields, folder names, canonical KF references | Must match exactly; never modify |
| Tier 2 — Constrained | `metadata.*` frontmatter fields, SKILL.md body text, reference-file content | Agent's authority within the constraints below |
| Tier 3 — Halt-to-operator | Brand-cleanliness anonymization wording (B1.3), description-field overflow on any Skill, skill-builder self-pass verdict (B2.1d) | Surface to operator; do not decide silently |

Constraints on Tier 2 edits:

- Description field: ≤ 1024 characters after any edit.
- SKILL.md body: ≤ 500 lines after any edit.
- Frontmatter: valid YAML after every edit.
- Reference files: additions and edits only as specified by the work queue item; no deletions of existing content unless the item explicitly authorizes.

Critic-gate composition: optional and **scoped to Tier 3 items**. Use `rootnode-critic-gate` semantics for B1.3 ambiguous-wording calls and B2.1(d) self-pass verdict. Mechanical Tier 2 edits with programmatic verification do not require critic.

## R3. Scope Authorization

**In-scope (autonomous):**

- Read any file in the repo, including `audit/canonical-kfs/*` for methodology grounding
- Edit `metadata:` frontmatter fields per work queue items
- Edit SKILL.md body text per work queue items
- Add or edit content in existing reference files per work queue items
- Create files under `audit/phase-31d/` (e.g., `B2_CONFIRMATIONS.md`)
- Git: `git add`, `git commit` on `phase-31d-remediation` only

**In-scope with notification (log in commit message):**

- Any edit to a SKILL.md body section beyond the specific fix named in the work queue item
- Any description-field edit (count chars before commit)

**Out-of-scope (halt and escalate):**

- `git push` to remote
- Merge to `main`
- Branch creation, switching, or deletion (operator pre-staged the feature branch)
- Edits on any branch other than `phase-31d-remediation`
- Edits outside Skill directories and `audit/`
- Edits inside `_v2_1_staging/`, `design_queue/`, `dist/`, `audit/build-artifacts/`, `audit/canonical-kfs/`, `assets/`, or `scripts/` (these are tooling, staging, and reference; not part of Phase 31d work)
- Deletions of existing content in reference files
- Creation of new Skills
- Folder rename `audit/build-artifacts/rootnode-handoff-trigger/` → `rootnode-handoff-trigger-check/` is **default-SKIP** per Q-31d-3 (operator override path documented in `WORK_QUEUE.md` B1.1)

## R4. Halt-and-Escalate Triggers

Halt and report current state if any of these occur. Do not auto-recover.

1. Pre-flight check fails (R5)
2. Description field would exceed 1024 chars after an edit
3. SKILL.md body would exceed 500 lines after an edit
4. Frontmatter edit produces invalid YAML (verify with a YAML parse)
5. A file specified in a work queue item does not exist at the expected path
6. Diff for a commit includes changes to files not named in the work queue item (scope-creep guardrail)
7. Brand-cleanliness replacement is ambiguous — no clear canonical KF, no clean anonymization, and not safe to remove
8. skill-builder self-pass check fails on any of the 9 dimensions after the B2.1 update
9. Test repo with 5+ MCP servers unavailable for B2.2 verification
10. Critic-gate (when invoked on a Tier 3 item) returns REJECT, or REQUEST_CHANGES cycle exceeds 3
11. `audit/canonical-kfs/` content appears stale — operator pre-prep was incomplete

## R5. Pre-flight Checklist

The operator pre-stages the feature branch, session scaffolding, input docs, and canonical KFs before invoking this CC session. Pre-flight verifies the prepared state.

Run before any work-queue items:

1. **Verify branch.** `git rev-parse --abbrev-ref HEAD` returns `phase-31d-remediation`. If this returns `main` or another branch, halt — operator pre-prep was incomplete.
2. **Verify clean working tree.** `git status --porcelain` returns empty. Any uncommitted changes mean operator pre-prep was incomplete or contaminated.
3. **Verify session scaffolding and input documents are present at expected paths:**
   - `CLAUDE.md` (this file, at repo root)
   - `WORK_QUEUE.md` (at repo root)
   - `audit/phase-31c/SKILLS_AUDIT_REPORT.md` (Phase 31c audit baseline — operator must upload; does not exist in main)
   - `audit/phase-31d/AMENDMENT.md` (Phase 31c verdict corrections + brand-cleanliness finding)
   - `audit/phase-31d/SKILLS_IMPACT_EVAL.md` (Stream B2 source)
4. **Verify canonical KFs are current at `audit/canonical-kfs/` (Move B + Phase 31a content):**
   - `root_SKILL_BUILD_DISCIPLINE.md` — `grep -c "discipline_post" audit/canonical-kfs/root_SKILL_BUILD_DISCIPLINE.md` returns ≥ 2 (§4.6 added in Move B; mentions on the field-name and retroactive-application lines).
   - `root_SKILL_BUILD_DISCIPLINE.md` — `grep -c "D9 — Behavioral validation" audit/canonical-kfs/root_SKILL_BUILD_DISCIPLINE.md` returns ≥ 1 (§3.9 D9 added in v2.1).
   - `root_AGENT_ANTI_PATTERNS.md` — `grep -c "Build-scaffolding leak" audit/canonical-kfs/root_AGENT_ANTI_PATTERNS.md` returns ≥ 1 (§3.6 added in Move B).
   - `root_AGENT_ENVIRONMENT_ARCHITECTURE.md` — `grep -c "Brand-cleanliness" audit/canonical-kfs/root_AGENT_ENVIRONMENT_ARCHITECTURE.md` returns ≥ 1 (§4.10 from Phase 31a).
   - `root_OPTIMIZATION_REFERENCE.md` — `grep -c "Meincke" audit/canonical-kfs/root_OPTIMIZATION_REFERENCE.md` returns ≥ 1 (persuasion-compliance note in §"Behavioral Tendencies and Countermeasures").
5. **Read `WORK_QUEUE.md`** in full.
6. **Confirm Skill directory count.** `ls -d rootnode-*/ | wc -l` returns 27.
7. **Report pre-flight status** with each check's pass/fail. Proceed only if all checks pass.

If any check fails, halt and report. Do not attempt to recover by creating missing files, switching branches, refreshing canonical-kfs from memory, or relaxing the clean-tree requirement. The Phase 31c precedent of inferring consent from artifact-directory population is **not repeated** here.
