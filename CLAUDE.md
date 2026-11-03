# CLAUDE.md — rootnode-skills repo

Project-scoped CLAUDE.md for the rootnode-skills repository. Overrides `~/.claude/CLAUDE.md` fallback defaults for sessions in this repo.

---

## Mission

Public plugin marketplace for the root.node ecosystem. The 27 Skills ship in six plugins under `plugins/`, listed by `.claude-plugin/marketplace.json`; merging a raised `plugin.json` version to `main` publishes it, and GitHub releases at `github.com/drayline/rootnode-skills` record each version. Substantive work in this repo (release builds, audits, hygiene sweeps, KF sync operations) happens via **session prompts** — each session prompt carries its own identity, scope authorization, halt triggers, and work queue.

This CLAUDE.md provides repo-level governance that applies to ALL sessions. Session prompts override these defaults for the session's specific scope.

---

## Authority matrix

Three tiers based on what content represents:

**Tier 1 — Mirror-exact (sync from authoritative source only):**
- `audit/canonical-kfs/*.md` — synced from approved seed Project KFs only (Phase 32a-style staging review required upstream)
- `plugins/*/skills/*/SKILL.md`, `plugins/*/skills/*/references/*.md`, `plugins/*/skills/*/scripts/*`, `plugins/*/skills/*/agents/*` — modified ONLY via session prompts that reference an approved design spec
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
3. **Skill source modification outside an approved session prompt.** `plugins/*/skills/*/` content changes require a session prompt referencing a locked design spec.
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

One artifact shape: one zip per plugin. A Skill's source folder is `plugins/<plugin>/skills/<name>/`, where `<name>` matches its SKILL.md `name:`; installed, it appears as `<plugin>:<name>`.

- **Zip:** `dist/<plugin>-v<version>.zip`, with `<version>` read from `plugins/<plugin>/.claude-plugin/plugin.json` and `.claude-plugin/plugin.json` at the zip root (the shape claude.ai **Upload plugin** takes). `evals/` is left out at the plugin root and at each Skill root. Shell scripts are stored LF with mode 0755.
- **Count:** six plugins, six zips. `build_release_artifacts.py` asserts it on a full build and exits non-zero on a mismatch.
- **Stale output:** a full build clears `dist/*.zip` first. Release steps name each asset path; never upload `dist/*.zip`.
- **Embedded copies:** a Skill reference that embeds a shipped script marks the block with `<!-- shipped: <repo path> -->`; the packager fails the build when the block and the file differ after LF normalization.
- **Validation:** `claude plugin validate .` and `claude plugin validate ./plugins/<plugin> --strict` pass before a release.

The `-cp` flat and `-cc` wrapper zips and the `rootnode-catalog-vN.zip` bundle retired at v6.0; they remain on the v3.0–v5.0.1 releases as history. Repo-root script roster is **two**: `build_release_artifacts.py` (the release packager) and `generate_release_notes.py` (per-plugin release notes from a per-cycle config under `audit/v<N>_<M>-release/`). Anthropic's `package_skill.py` (upstream at `anthropics/skills`, `skills/skill-creator/scripts/package_skill.py`) and skill-builder's internal `scripts/package_zip.py` are single-Skill packagers, not release tools. For the authoritative packager inventory, see `audit/repo-catalog/`. Canonical methodology: SBD §4.7 (layout and packager) and §6.6 (versioning).

---

## Releases

Before cutting a catalog release, read `docs/root_SKILLS_RELEASE_PLAYBOOK.md`. It carries the release model (merging a raised plugin version to `main` publishes it; per-plugin releases tagged `<plugin>/v<version>` (the plugin name carries the `rootnode-` prefix) record it; a `catalog-vN.N` umbrella marked `--latest` carries the six plugin zips and the catalog index), the two-phase branch-protection-aware process (content PR → operator merge → tags/releases off merged `main`), tag naming, and the anti-churn rules. The executable step-by-step is the versioned release prompt; the playbook is the model and the standing rules behind it.

---

## When this CLAUDE.md is insufficient

If a session reaches a decision point that this file does not address AND no session prompt provides explicit authorization, halt and ask Aaron for a decision rather than guessing. The cost of one round-trip is far less than a confident wrong action.

Append-only discipline applies to audit and decision artifacts in this repo per `~/.claude/CLAUDE.md` Drayline-pattern discipline.

---

*End of project-scoped CLAUDE.md.*
