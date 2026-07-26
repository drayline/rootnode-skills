# CLAUDE.md — rootnode-skills repo

Project-scoped CLAUDE.md for the rootnode-skills repository. Overrides `~/.claude/CLAUDE.md` fallback defaults for sessions in this repo.

---

## Mission

Public Skill catalog for the root.node ecosystem. Skills are versioned, packaged as zips, and released via GitHub releases at `github.com/drayline/rootnode-skills`. Substantive work in this repo (release builds, audits, hygiene sweeps, KF sync operations) happens via **session prompts** — each session prompt carries its own identity, scope authorization, halt triggers, and work queue.

This CLAUDE.md provides repo-level governance that applies to ALL sessions. Session prompts override these defaults for the session's specific scope.

---

## Authority matrix

Three tiers based on what content represents:

**Tier 1 — Mirror-exact (sync from authoritative source only):**
- `audit/canonical-kfs/*.md` — synced from approved seed Project KFs only (Phase 32a-style staging review required upstream)
- `rootnode-*/SKILL.md`, `rootnode-*/references/*.md`, `rootnode-*/scripts/*`, `rootnode-*/agents/*` — modified ONLY via session prompts that reference an approved design spec
- `LICENSE`, `README.md` — modified ONLY with explicit operator approval

**Tier 2 — In-scope-with-notification:**
- `design/` working files (drafts, specs, working notes) — free-design except where a design spec is explicitly locked
- `audit/` outputs (reports, hygiene scans, halt summaries) — append-only per Drayline-pattern discipline
- repo-root tooling scripts — modify with notification

**Tier 3 — Free-design:**
- `.gitignore`, `.editorconfig`, similar dev-only config — modify as needed
- `design/staging-kf/` — staging area for KF updates pending review
- `design/audit-artifacts/` subdirectories for in-progress sessions

---

## Scope authorization

**With a session prompt:** The session prompt is the controlling spec. Its in-scope and out-of-scope lists override this CLAUDE.md's defaults. Examples of session prompts: `root_CC_skill_builder_v3_build.md`, `root_CC_skill_builder_v3_release.md`, `root_CC_phase31d_*.md`. Follow the session prompt's scope authorization literally; surface gaps to operator rather than improvising.

**Without a session prompt:** Treat work as exploratory:
- Do not modify Tier 1 content
- Do not push to any branch
- Surface intent and request explicit scope authorization before action
- Apply `~/.claude/CLAUDE.md` fallback defaults

---

## Halt-and-escalate triggers

In addition to `~/.claude/CLAUDE.md` universal halt triggers, halt for any of these in this repo:

1. **Direct push to main blocked.** `main` is branch-protected; never attempt direct push. PRs are the only path to main.
2. **Force-push to any branch.** Halt; never force-push without explicit operator scope-expansion authorization.
3. **Skill source modification outside an approved session prompt.** `rootnode-*/` content changes require a session prompt referencing a locked design spec.
4. **Tag or release operations outside a release prompt.** Tagging and GitHub release creation belong to dedicated release prompts (e.g., `root_CC_skill_builder_v3_release.md`); do not improvise.
5. **Modification of `audit/canonical-kfs/` outside an approved sync precondition step.** These files mirror approved seed Project KFs; only sync from `design/staging-kf/` as part of an approved release branch precondition (Phase 32b §32b.1.5 pattern). Do not hand-edit them, even to fix a KF drift you notice mid-session — surface the change instead (see *Knowledge-file change surfacing* below).
6. **Build prompt halt summary instructs continuation phrase mismatch.** If a session prompt specifies an exact continuation phrase to signal next phase (e.g., `"Phase 32a closed; proceed with Phase 32b."`) and operator response is ambiguous or different, halt and ask one targeted clarifying question.

---

## Pre-flight checklist

Before any substantive work in this repo:

1. Read this CLAUDE.md fully.
2. Identify whether a session prompt is governing this work. If yes, the session prompt is the controlling spec. If no, treat work as exploratory per scope authorization above.
3. Confirm `git branch --show-current` matches the expected branch for the session. `main` is read-only via PR-only workflow.
4. For session prompts that modify Skill content: verify the referenced design spec exists at the path the session prompt cites.
5. For session prompts that touch `audit/canonical-kfs/`: verify the corresponding `design/staging-kf/` files exist and reflect the expected v3 (or whichever version) methodology.
6. Confirm `gh auth status` shows authenticated GitHub CLI access for sessions that involve PRs or releases.

---

## Knowledge-file change surfacing

When a session's edits to Skill content (or any repo content that mirrors seed-Project methodology) imply a change to a knowledge file, **surface the KF-update block — do not silently skip it, and do not directly edit `audit/canonical-kfs/`.**

Write the surfaced change to the session's audit artifact (e.g., `audit/<session>/kf-update-blocks.md`) as a delta: target KF, action (ADD / REVISE), the block, and the rationale. The seed Project is the authoritative source for KF content; surfaced blocks are applied to the seed-Project KFs first, staged to `design/staging-kf/`, then synced to `audit/canonical-kfs/` as a release-branch precondition (the sync path halt #5 authorizes).

**Surfacing is not editing.** The no-direct-edit rule (halt #5) protects mirror integrity — the seed-vs-canonical staleness diff (Observation O10) only catches drift if `canonical-kfs/` is a controlled mirror of the approved seed KFs. The surfacing discipline ensures a needed KF update is captured and routed, never lost. A session that recalibrates Skills and notices a parallel KF line (e.g., a model-calibration line that also lives in the seed KFs and the mirror) surfaces the block; it does not reach into `canonical-kfs/` to fix it in place.

---

## Repo conventions

- **File naming.** Project-internal files use `{code}_` prefix (`root_`, etc.). Cross-project shared files use `shared_` prefix. No session numbers in filenames.
- **Branch naming.** Release branches: `release/v{N}.{N}` (e.g., `release/v3.0`). Phase work: `phase-{N}-{descriptor}` (e.g., `phase-31d-remediation`).
- **Commit messages.** Conventional-commit subject (`<type>: <scope>`) with body for context. Types: `release`, `feat`, `fix`, `docs`, `chore`, `phase-XX`.
- **Audit artifact paths.** `design/audit-artifacts/v{N}.{N}/` for release-specific artifacts; `audit/phase-XX/` for phase-specific work.
- **Shell.** CC harness defaults to bash on Windows (Git Bash). Operator's interactive shell is PowerShell. Session prompts that include command blocks should provide bash primary + PowerShell variants where commands diverge.

---

## Repo-fact authority

`audit/repo-catalog/` is the ground truth for repo contents — tracked files, packagers, canonical-KF roster, cycle directories, tags, releases. Consult it before asserting any repo-content fact in a session, a doc edit, or a PR body. Where this CLAUDE.md, the release playbook, or a session's recollection disagrees with the catalog, the catalog wins and the disagreeing document is a defect to fix. The catalog is regenerated as the last step of every catalog release (playbook Phase B post-verification). Cycle-directory naming convention lives at `audit/README.md`.

---

## Packaging conventions

Two zip shapes, one per surface. The source folder on disk (`rootnode-<skill>/`) is **un-suffixed**; the `-cp`/`-cc` suffix is a packaging-output naming convention applied to the zip, never to the source folder.

- **`-cp` = flat.** Zip contents sit at the root — `SKILL.md`, `references/`, `agents/`, etc. directly, with no wrapper folder — because CP (Claude.ai Projects) Skill upload reads `SKILL.md` from the zip root.
- **`-cc` = wrapper.** Zip contains a nested `rootnode-<skill>/` folder with the contents inside it. CC keeps each Skill as a folder at `~/.claude/skills/rootnode-<skill>/`, so the wrapper exists *so that extracting the zip yields the ready-named folder to drop in*. A flat `-cc` zip would extract loose files with no folder and break the install.

Surface → shape → release artifact:

- cp-only Skills → flat → `rootnode-<skill>-cp.zip` — **22**
- cc-only Skills → wrapper → `rootnode-<skill>-cc.zip` — **3**
- dual-surface Skills (`skill-builder`, `cc-design`) → both → `-cp.zip` + `-cc.zip` — **2 × 2 = 4**
- **29 release artifacts from 27 source folders.**

Shipping a CC Skill flat, or a CP Skill wrapped, is an install failure — not a cosmetic mismatch.

**Release packaging:** `build_release_artifacts.py` is the single entry point. It reads the surface map (`CC_ONLY` = critic-gate / mode-router / repo-hygiene; `DUAL` = skill-builder / cc-design; all other `rootnode-*` = cp-only), emits flat for each `-cp` and wrapper for each `-cc`, applies the suffix, and self-asserts the 24 `-cp` + 5 `-cc` = 29 total. Both shape emitters live inside the orchestrator; wrapper-shape logic was ported from Anthropic's upstream `package_skill.py` (not tracked in this repo — see `build_release_artifacts.py:7` and `:61`). Two tracked sibling scripts at repo root: `build_releases.py` (flat shape only, superseded — legacy reference) and `generate_release_notes.py` (version-agnostic release-notes generator added in the v4.0 alignment cycle per D7 expansion; takes `VERSION`, `TIER_LABEL`, `CATALOG_RELEASE`, and Skill data from a per-cycle Python config file under `audit/v<N>-*/`). Repo-root script roster is **three**. For the authoritative packager inventory, see `audit/repo-catalog/`.

Canonical methodology lives in **SBD §4.7** (surface-mapped model, reconciled in the v3.1 propagation cycle): §4.7 frames the release as shipping *both* shapes surface-mapped (superseding the earlier "flat = the release form" framing). Note: the `skill-builder` Skill's internal `scripts/package_zip.py` is a *separate* build-pipeline packager (adapted from upstream `package_skill.py` for `.zip` + `eval-viewer/` inclusion) — not the release-time packager, and not to be conflated with the orchestrator.

---

## Releases

Before cutting a catalog release, read `docs/root_SKILLS_RELEASE_PLAYBOOK.md`. It carries the release model (27 per-Skill releases + a notes-plus-bundle `catalog-vN` umbrella marked `--latest` — catalog-index notes plus a `rootnode-catalog-vN.zip` bundle of all 29 artifacts), the two-phase branch-protection-aware process (content PR → operator merge → tags/releases off merged `main`), the packaging convention, tag naming, and the anti-churn rules. The executable step-by-step is the versioned release prompt (e.g. `root_CC_PROMPT_v3_1_release.md`); the playbook is the model and the standing rules behind it.

---

## When this CLAUDE.md is insufficient

If a session reaches a decision point that this file does not address AND no session prompt provides explicit authorization, halt and ask Aaron for a decision rather than guessing. The cost of one round-trip is far less than a confident wrong action.

Append-only discipline applies to audit and decision artifacts in this repo per `~/.claude/CLAUDE.md` Drayline-pattern discipline.

---

*End of project-scoped CLAUDE.md.*
