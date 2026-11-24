# rootnode-code 6.1.0 — KF update blocks

Surfaced, not applied (CLAUDE.md, *Knowledge-file change surfacing*). Apply to the seed-Project KF first, stage to `design/staging-kf/`, then sync to `audit/canonical-kfs/` as a release-branch precondition. Source of the change: `design/root_DESIGN_verify_gate_fix.md` (LF sha256 `cddfbd46cffe0b809e0826458ef2facabfcd902baeb56e34fb36a1d0587328b3`), §3 D1, §1 fact 6.

## 1. SKILL_BUILD_DISCIPLINE — hooks paragraph

- **Target KF:** `root_SKILL_BUILD_DISCIPLINE.md` (mirror `audit/canonical-kfs/root_SKILL_BUILD_DISCIPLINE.md`, line 351 at `8670edc`)
- **Action:** REVISE
- **Current text (first two sentences):** "A hook declared in `plugins/<plugin>/hooks/hooks.json` runs in every repository where the plugin is enabled; chat ignores hooks and agents."
- **Block:**

> **Hooks ship with the plugin.** A hook declared in `plugins/<plugin>/hooks/hooks.json` runs wherever the plugin loads, chat sessions that open a repository included; it does not stay out of chat on its own. A shipped hook that can block therefore opts in per repository: it acts only where the repository adds a config file (for `rootnode-code`, `.claude/rootnode-gates.json`), keeps its state in `CLAUDE_PLUGIN_DATA` rather than the repository, and exits 0 when it cannot read its input, config or tools. A Skill reference that embeds a shipped script must match the shipped file byte for byte after LF normalization. The packager enforces this and fails the build on drift (check added in the v6.0 release PR), because the v6.0 build left the cc-design composition reference carrying the pre-ship sketches.

- **Rationale:** the "chat ignores hooks" statement was false. Three chat sessions were blocked by the 6.0.0 Stop hook (design spec §1 fact 6). The opt-in rule is the v6.1.0 fix and a standing rule for any plugin that ships a blocking hook.

## 2. Build context — hook checks gap (design spec §3a A4)

- **Target KF:** `root_build_context.md` (seed Project; not mirrored in this repository)
- **Action:** ADD (closeout entry and observation)
- **Block:**

> **rootnode-code 6.1.0 (2026-11-24).** The 6.0.0 Stop hook was never run from the synced install before release (Current State item 3, "Hook checks not yet run"). The 6.0.0 defect is that gap: the hooks acted in every folder on every surface and blocked chat and read-only sessions in three projects. 6.1.0 makes both hooks opt-in through `.claude/rootnode-gates.json`, binds evidence to a tree fingerprint, and ships `audit/v6_1-release/hook-tests/run.sh`. Observation: a shipped hook is not verified until it has run from the install path users get (synced plugin, chat surface included); a harness run from the repository does not cover that path.

- **Rationale:** design spec §3a A4 asks for this record; the build context is a seed-Project file this session cannot edit.
