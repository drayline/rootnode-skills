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
5. **Modification of `audit/canonical-kfs/` outside an approved sync precondition step.** These files mirror approved seed Project KFs; only sync from `design/staging-kf/` as part of an approved release branch precondition (Phase 32b §32b.1.5 pattern).
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

## Repo conventions

- **File naming.** Project-internal files use `{code}_` prefix (`root_`, etc.). Cross-project shared files use `shared_` prefix. No session numbers in filenames.
- **Branch naming.** Release branches: `release/v{N}.{N}` (e.g., `release/v3.0`). Phase work: `phase-{N}-{descriptor}` (e.g., `phase-31d-remediation`).
- **Commit messages.** Conventional-commit subject (`<type>: <scope>`) with body for context. Types: `release`, `feat`, `fix`, `docs`, `chore`, `phase-XX`.
- **Audit artifact paths.** `design/audit-artifacts/v{N}.{N}/` for release-specific artifacts; `audit/phase-XX/` for phase-specific work.
- **Shell.** CC harness defaults to bash on Windows (Git Bash). Operator's interactive shell is PowerShell. Session prompts that include command blocks should provide bash primary + PowerShell variants where commands diverge.

---

## When this CLAUDE.md is insufficient

If a session reaches a decision point that this file does not address AND no session prompt provides explicit authorization, halt and ask Aaron for a decision rather than guessing. The cost of one round-trip is far less than a confident wrong action.

Append-only discipline applies to audit and decision artifacts in this repo per `~/.claude/CLAUDE.md` Drayline-pattern discipline.

---

*End of project-scoped CLAUDE.md.*
