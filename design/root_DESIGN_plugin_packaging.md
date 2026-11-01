# root.node — Plugin packaging design

**Status:** v0.2 design, 2026-10-31. Track 2 step 1 of SH 103026-0635. v0.2 records the operator's decisions D1–D6 (§6) as taken; v0.1 listed defaults only.
**Evidence base:** Claude Code docs pages `skills`, `plugins/manifest-reference`, `plugins/marketplace-reference`, `plugins/install`, `plugin-evals`, and claude.com docs `plugins/overview`, `plugins/platform-support`, `plugins/build`, all fetched 2026-10-31. Every CLI flag, field name, limit, and version floor below is a product fact as of that fetch: `[PF]` = verify against the running Claude Code version at build time.
**Repo facts:** the current source-folder path for the 27 Skills, the packager internals, and tag/release counts are NOT restated here. `audit/repo-catalog/` is authoritative; the build prompt reads it. Placeholders: `{SKILLS_SRC}` = current source-folder root, `{REPO}` = `drayline/rootnode-skills`.

---

## 1. What the docs settle

| Question from SH step 1 | Answer | Source |
|---|---|---|
| Does one install reach every surface? | Yes. A plugin added at **Customize > Plugins** on claude.ai is saved to the account and loads in chat (web, desktop, mobile), Cowork, and Claude Code as a synced plugin at next session start. The reverse is not true: `claude plugin install` stays on that machine. | claude.com `plugins/overview` |
| Can a user add a Git marketplace on claude.ai? | Yes. **Add > Add marketplace** takes a repo URL or `owner/repo` for GitHub, GitHub Enterprise, and public GitLab/Bitbucket. A github.com marketplace can be set to **Sync automatically**. | `plugins/overview` |
| Do plugin skills load in web chat? | Yes. Skills and commands load on all three surfaces; in chat a command loads as a skill. | `platform-support` |
| Do hooks run on claude.ai? | No. Hooks and agents load in Cowork and Claude Code only; chat ignores them without error. `bin/` makes claude.ai and Cowork refuse the whole plugin. | `platform-support` |
| Does a plugin make the `-cp`/`-cc` zip split unnecessary? | For users, yes: one marketplace serves both. The `-cp` zips survive only as a fallback for people who upload by hand and for one transition cycle. Zip upload is still supported (**Add > Upload plugin**, requires `.claude-plugin/plugin.json` at zip root or one level down). | `plugins/overview`, `plugins/build` |
| Update and versioning | `plugin.json` `version` pins users until it changes; it is a free string, not semver-checked. On claude.ai, marketplace plugins update from source with nothing to accept; **Check for updates** pulls manually. On Claude Code, third-party marketplaces have auto-update **off by default**; `claude plugin update <plugin>@<marketplace>` updates one. Plugins from a claude.ai-hosted marketplace are not pinned by `version`. | `manifest-reference`, `install`, `plugins/overview` |
| Limits on claude.ai | 25 self-added marketplaces per account per org; 5,000 files and 200 MB per plugin; 200 MB max upload. | `platform-support` |
| Frontmatter in plugin skills | Claude Code accepts every field in plugin skills. The six-field restriction (`name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`) applies to claude.ai skill uploads, the Skills API, and `package_skill.py`. Whether claude.ai applies it to skills inside a marketplace plugin is **not stated** — verify with one test upload before relying on any Claude Code-only field. | Claude Code `skills` |
| Eval tooling | `claude plugin eval` (v2.1.269+) runs each case 3× with the plugin and 3× without, reports `WITH`, `W/OUT`, `Δ`, exits non-zero below `--threshold`. Suite lives in `evals/<case>/prompt.md` + `graders/*.md`. Six grader types; `tool_used: Skill` is reported but excluded from the score in two-arm runs so it cannot inflate Δ. | `plugin-evals` |
| Skill listing budget | The listing of skill names and descriptions costs context every turn; the budget is 1% of the model's context window and descriptions are dropped least-invoked-first on overflow; per-entry cap is 1,536 characters. `/doctor` estimates the cost; `/skill-doctor` (v2.1.252+) reports per-skill cost and use. | Claude Code `skills` |

One KF defect surfaced: Claude Code docs cite `package_skill.py` in `anthropics/skills` as a real packaging path. `root_SKILL_BUILD_DISCIPLINE.md` §4.7 and the CI call it a nonexistent upstream reference. Resolve against the `anthropics/skills` repo before the build; one of the two is wrong.

## 2. Repository shape

Target layout in `{REPO}` (every path below is proposed, not existing; the build verifies nothing collides via `audit/repo-catalog/`):

```
{REPO}/
├── .claude-plugin/
│   └── marketplace.json            # marketplace root = repo root
├── plugins/
│   ├── rootnode-projects/
│   │   ├── .claude-plugin/plugin.json
│   │   ├── skills/<skill>/SKILL.md   # moved from {SKILLS_SRC}
│   │   ├── evals/<case>/...          # claude plugin eval suite; evals/results/ gitignored
│   │   ├── README.md                 # ≥40 words; required for directory listing
│   │   └── LICENSE
│   ├── rootnode-code/
│   │   ├── ... as above
│   │   └── hooks/hooks.json          # the G5/G5b hooks; Cowork + Claude Code only
│   └── ...
├── audit/                            # unchanged
├── docs/                             # unchanged
└── build_release_artifacts.py        # updated: reads plugins/*/skills/*, still emits -cp zips
```

Why self-contained plugin directories rather than the documented "marketplace root as source with a `skills` list" shortcut: that shortcut avoids moving files, but `claude plugin eval .`, **Upload plugin**, and directory submission all assume a directory that holds its own `plugin.json`, `evals/`, README, and LICENSE. One layout serving every path beats two mechanisms. The cost is a one-time `git mv` of the source folders and a packager edit; both are mechanical.

### marketplace.json

```json
{
  "name": "rootnode",
  "owner": { "name": "Drayline LLC", "url": "https://rootnode.design" },
  "description": "root.node — the architecture system for Claude. Measured plugins for Project and global-layer audit, Claude Code environment design, prompt compilation, and behavioral tuning.",
  "metadata": { "pluginRoot": "./plugins" },
  "plugins": [
    { "name": "rootnode-projects", "source": "rootnode-projects", "category": "audit" },
    { "name": "rootnode-code",     "source": "rootnode-code",     "category": "claude-code" },
    { "name": "rootnode-prompts",  "source": "rootnode-prompts",  "category": "prompting" },
    { "name": "rootnode-tuning",   "source": "rootnode-tuning",   "category": "behavior" },
    { "name": "rootnode-governance","source": "rootnode-governance","category": "runtime" },
    { "name": "rootnode-skill-builder","source": "rootnode-skill-builder","category": "authoring" }
  ]
}
```

`metadata.pluginRoot` requires v2.1.239+ `[PF]`; bare names resolve under it. `rootnode` is not a reserved name and does not read as Anthropic's. Each plugin's `description`, `version`, `author`, and `license` live in its own `plugin.json` (the manifest wins over the entry for `version`).

### plugin.json (per plugin)

```json
{
  "name": "rootnode-projects",
  "displayName": "root.node Projects",
  "version": "6.0.0",
  "description": "Audit and optimize Claude Projects and the claude.ai global layer: Project scorecard, global-layer scorecard, full-stack audit, anti-pattern detection, memory and context-budget optimization, project brief.",
  "author": { "name": "Drayline LLC", "url": "https://rootnode.design" },
  "repository": "https://github.com/drayline/rootnode-skills",
  "license": "{LICENSE_SPDX — verify against the repo's LICENSE}",
  "keywords": ["claude-projects", "audit", "context-engineering"]
}
```

No `skills` key: the default `skills/` scan is enough. No `CLAUDE.md` at plugin root (not loaded; validator warns). `claude plugin validate ./plugins/<name> --strict` is the gate; it runs in CI.

## 3. Plugin grouping (v1, pre-consolidation)

Grouping is by job so that a user who wants one job installs one plugin and pays only that listing cost. Skill folders move and drop the `rootnode-` prefix; the `name:` field changes to match (D3). Under SBD §6 this is a rename event: the old names retire in this release. Cross-Skill references inside Skill content use the bare new name (`project-audit`); the plugin-qualified form `/rootnode-projects:project-audit` is how Claude Code lists it, and the bare form also invokes it unless another command takes the name.

| Plugin | Skills (27 → 6 plugins) | Surfaces where the full plugin works | Notes |
|---|---|---|---|
| rootnode-projects | project-audit, global-audit, full-stack-audit, anti-pattern-detection, memory-optimization, context-budget, project-brief | all | The moat per the research; first candidate for the directory |
| rootnode-code | cc-design, repo-hygiene | Cowork, Claude Code (hooks); chat gets skills only | Carries `hooks/hooks.json` (bounded Stop hook, migration guard) |
| rootnode-prompts | prompt-compilation, prompt-validation, block-selection, identity-blocks, reasoning-blocks, output-blocks, 5 domain packs | all | 11 skills; the consolidation target once evals run |
| rootnode-tuning | behavioral-tuning | all | Flagship; add generation-delta eval cases |
| rootnode-governance | critic-gate, mode-router, handoff-trigger-check, session-handoff, profile-builder | all | mode-router and handoff-trigger-check are review candidates; grouping keeps them out of the audit plugin's listing cost |
| rootnode-skill-builder | skill-builder | all; scripts need Claude Code or Cowork | Keep separate: its `scripts/` and eval tooling are heavy |

Count: 7 + 2 + 11 + 1 + 5 + 1 = 27. Namespacing: in Claude Code a plugin skill lists as `/<plugin>:<skill>`, so `/rootnode-projects:project-audit`.

## 4. Evals

Each plugin ships `evals/`. Bootstrap with `claude plugin eval init` from the plugin root (interactive; proposes should-trigger and should-not-trigger cases). Hand-write the rest to the layout:

```
evals/<case>/prompt.md        # frontmatter: max_turns, allowed_tools: [Read, Glob, Grep, Skill]; body: user phrasing, never the skill name
evals/<case>/graders/result.md     # type: llm (short outputs) or regex over {source: file, path} (long outputs)
evals/<case>/graders/skill-fired.md # type: tool_used, tool: Skill, input_match on the skill name — indicator only, not scored
```

Rules the docs make explicit and the design adopts: one grader on the result and one on the steps per case; `regex` over file contents for long outputs because `llm` judges drift with length; pin `--model` and `--judge-model` in CI so a model rollout is not read as a plugin regression; `--threshold` set below 1.0 deliberately; `--max-cost-usd` on every CI run; `evals/results/` gitignored.

The research report's "collapse test" (does one line of CLAUDE.md do as well as the Skill?) is not a native arm. Implement it as a third run of the same cases with `--ablation none` and `append_system_prompt` set to the one-line guidance in `prompt.md`; compare its `SCORE` to the two-arm `WITH`. A Skill whose Δ over the one-liner is within run-to-run noise is a consolidation candidate, per the JetBrains variance finding.

Minimum cost model: cases × 3 runs × 2 arms, plus judge calls. Start with 5 cases per plugin on `rootnode-projects` and `rootnode-prompts` to get a cost figure before scaling to 27 Skills × 3 models.

## 5. Release and distribution

| Concern | Decision |
|---|---|
| Versioning unit | Plugin-level `version` in `plugin.json`, raised on every release of that plugin. Per-Skill versions in SKILL.md frontmatter continue per SBD §6 for the catalog record. Per-Skill GitHub releases stop; per-plugin tags `rootnode-<plugin>/vN` replace them. The umbrella `catalog-vN` release stays as the notes-plus-assets release and carries the six plugin zips as its assets; the `-cp`, `-cc`, and catalog-bundle zip shapes retire (D5). This is a playbook change (§1.5/§1.6 and the packaging convention). |
| Install, claude.ai | **Customize > Plugins > Add > Add marketplace** → `drayline/rootnode-skills`; turn on **Sync automatically**. README install section says exactly this. |
| Install, Claude Code | `claude plugin install rootnode-projects --marketplace drayline/rootnode-skills` (v2.1.292+ `[PF]`), or `claude plugin marketplace add drayline/rootnode-skills` then `claude plugin install rootnode-projects@rootnode`. |
| Double-loading | A plugin installed on the account syncs to Claude Code as `<name>@synced`; installing the same plugin locally loads two copies. README says: install on claude.ai *or* locally, not both. Same lesson as the SBD §3.9 sync-isolation clause. |
| Auto-update on Claude Code | Off by default for third-party marketplaces. README states it and shows `claude plugin update`. |
| Directory | Later. Requires README ≥40 words, LICENSE, portal validation and review. Submit `rootnode-projects` first after its evals publish. |
| Website | rootnode.design install instructions change to the marketplace path; the open website sync (v3.0 → current) folds into this cycle rather than preceding it. |

## 6. Decisions for the operator

Taken 2026-10-31. These are the lock for the build.

| # | Decision | Taken | Why |
|---|---|---|---|
| D1 | Move source folders into `plugins/<name>/skills/` vs. root-as-source shortcut | Move | One layout serves eval, upload, and directory paths (§2) |
| D2 | Six plugins as grouped in §3 | Yes | By job; consolidation changes the contents, not the grouping |
| D3 | Drop the `rootnode-` prefix from skill directory and `name:` in this build | Yes | One rename event now rather than a second one at consolidation; the plugin namespace carries the brand |
| D4 | Drop per-Skill releases for per-plugin releases | Yes | Anti-churn; the plugin is the install unit now |
| D5 | Retire `-cp`, `-cc`, and catalog-bundle zips now; packager emits six plugin zips only | Yes | The zip path has no telemetry or update channel; **Upload plugin** takes a plugin-folder zip, so hand-upload is still covered |
| D6 | Catalog version for this release | 6.0 | Repo layout, names, and distribution unit change |

## 7. Build handoff (chat → Code)

One CC DESIGN-mode cycle in `{REPO}`, self-sufficient per CC_EG §5.7. Work queue, in order:

1. Read `audit/repo-catalog/` and report the current source-folder root, packager path, and whether `plugins/` or `.claude-plugin/` already exists. Report-only; halt on collision.
2. `git mv` the 27 source folders into `plugins/<plugin>/skills/` per §3. Add `plugin.json`, README, LICENSE per plugin. Add `.claude-plugin/marketplace.json`. Add `evals/results/` to `.gitignore`.
3. Update `build_release_artifacts.py` to read the new paths; the `-cp` count assertion stays at 24 for this cycle; the `-cc` wrapper shape is retired (the plugin replaces it) — confirm against the playbook before deleting.
4. `claude plugin validate .` and `claude plugin validate ./plugins/<each> --strict`; all pass.
5. `claude --plugin-dir ./plugins/rootnode-projects` smoke test: skills list as `/rootnode-projects:<skill>`.
6. `claude plugin eval init` on `rootnode-projects`; 5 cases; one two-arm run; record cost and Δ in the session report.
7. Move `hooks/hooks.json` fixtures into `rootnode-code`; live-hook test in a session (the v5.0.1 report lists this as unverified).
8. Test upload of one plugin zip to claude.ai (operator step; the session produces the zip and halts): confirm the skill loads in chat and whether any Claude Code-only frontmatter field is rejected. This closes the frontmatter gap in §1.
9. Regenerate `audit/repo-catalog/` and enumerate the expected deltas (folders moved, files added).
10. Session report with every digest computed in-turn.

Return to chat when: the frontmatter test rejects a field root.node Skills use; eval cost for 5 cases exceeds what 27 × 3 models can afford; or the packager change touches the release playbook beyond §1.5/§1.6.

## 8. Propagation triggers

`root_SKILLS_RELEASE_PLAYBOOK.md` §1 (release unit), §4.7 of `root_SKILL_BUILD_DISCIPLINE.md` (packaging shapes and the `package_skill.py` line), the CI `<knowledge_files>` entries that state "24 + 5 = 29", `root_build_context.md`, RAM, and the website. The CI is the first trigger.
