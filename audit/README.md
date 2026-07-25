# audit/ — layout and conventions

The `audit/` tree holds two distinct kinds of content, and they follow different naming rules.

## Standing infrastructure directories

Content-typed directories that are not cycle-scoped. They persist across releases and are named for the content they hold.

| Directory | Purpose |
|---|---|
| `audit/canonical-kfs/` | Mirror of the approved seed-Project knowledge files. Synced by name (never by glob) on release branches. Tier 1 mirror-exact. Roster changes require explicit design authorization. |
| `audit/build-artifacts/` | Per-Skill build audit evidence carried forward from prior phases (placement notes, promotion evidence, anti-pattern warnings). |
| `audit/repo-catalog/` | Ground truth for repo contents. Regenerated as the last step of every catalog release (playbook Phase B post-verification). Named `root_repo_catalog_<YYYYMMDD>.md`. Also holds `REPO_CLAIM_RECONCILIATION.md` snapshots when a reconciliation cycle runs. |

Add a new standing infrastructure directory only when the content is genuinely long-lived and does not fit an existing one.

## Cycle-scoped directories

Everything else in `audit/` is scoped to a specific release cycle or alignment cycle. Going-forward naming: **`audit/v<N>_<M>-<kind>/`** where `<kind>` is one of:

| `<kind>` | Meaning |
|---|---|
| `alignment` | Methodology / model-calibration cycle (verification logs, sweep manifests, halt notes for the design-and-recalibrate pass that precedes the release) |
| `release` | Release-cycle scripts, drift audits, and one-off tooling for a specific catalog version |

Examples in this convention: `audit/v4_0-alignment/` (methodology work for the v4.0 catalog), `audit/v4_0-release/` (if release-cycle scripts land).

The version format matches the tag namespace (`catalog-v4.0`) and branch namespace (`release/v4.0`) — underscore-separated in directory names to avoid dot-in-path awkwardness.

## Existing directories that predate this convention

These directories were named under earlier conventions and remain as-is. **Do not rename them** — every doc, commit message, and prior audit artifact that references them would need to change, and the historical record of what was true at that time is a feature. New content follows the going-forward convention; old content stays where it lives.

| Existing dir | Prior convention |
|---|---|
| `audit/opus-4_8-alignment/` | cycle-target name (calibration cycle for Opus 4.8) — semantically equivalent to `v3_1-alignment` but predates the convention |
| `audit/phase-31c/`, `audit/phase-31d/` | phase-number scheme (deprecated) |
| `audit/v3_1-release/` | release-version scheme (aligns with going-forward pattern; retained as-is) |

## Where reconciliation output lives

Repo-reconciliation cycles (like the one 2026-07-25 that produced `REPO_CLAIM_RECONCILIATION.md`) write their output into `audit/repo-catalog/` alongside the catalog snapshots — reconciliation is a repo-catalog activity, not its own cycle-artifact class.
