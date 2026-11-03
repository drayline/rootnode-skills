"""Release-notes config for catalog v6.0 (plugin marketplace).

Consumed by the repo-root generate_release_notes.py:
    py -3 generate_release_notes.py --config audit/v6_0-release/release-notes-v6.0-config.py

Plugin order follows .claude-plugin/marketplace.json. Change bullets are
verbatim from the v6.0 release prompt (A10).
"""

CATALOG_RELEASE = "catalog-v6.0"

ALL_SIX = (
    "First release as a plugin. Skills renamed: the `rootnode-` prefix moved to the plugin. "
    "`metadata.version` 6.0.0 with `metadata.predecessor`."
)

PLUGINS = [
    {
        "name": "rootnode-projects",
        "version": "6.0.0",
        "summary": "Project and global-layer audit and optimization",
        "changes": [
            ALL_SIX,
            "First eval suite, 5 cases for `claude plugin eval` (kept in the repo, not in the zip). "
            "The first run showed no lift over the base model; graders are being rewritten.",
        ],
    },
    {
        "name": "rootnode-code",
        "version": "6.0.0",
        "summary": "Claude Code environment design, repo hygiene, two hooks",
        "changes": [
            ALL_SIX,
            "Ships a migration guard (PreToolUse on Edit, Write, NotebookEdit, Bash, PowerShell; exit 2 blocks) "
            "and a bounded test-evidence Stop hook that exits 0 in a repo with no test command. Hooks run in "
            "every repository where the plugin is enabled; chat ignores them.",
            "cc-design: the hook reference carries the shipped scripts, checked by the packager; the guard-scope "
            "paragraph names the settings file for `denyWrite` (F-15); CR counting with a positive control "
            "(F-16); the execution-plan schema accepts `cc-design v…`.",
        ],
    },
    {
        "name": "rootnode-prompts",
        "version": "6.0.0",
        "summary": "Prompt compilation, validation, block libraries, domain packs",
        "changes": [ALL_SIX],
    },
    {
        "name": "rootnode-tuning",
        "version": "6.0.0",
        "summary": "Behavioral-tendency countermeasures",
        "changes": [ALL_SIX],
    },
    {
        "name": "rootnode-governance",
        "version": "6.0.0",
        "summary": "Critic gate, mode router, handoff check, session handoff, profile builder",
        "changes": [
            ALL_SIX,
            "profile-builder example: schema lookup for plugin installs.",
        ],
    },
    {
        "name": "rootnode-skill-builder",
        "version": "6.0.0",
        "summary": "Skill build, review, and eval tooling",
        "changes": [
            ALL_SIX,
            "Path references updated to the plugin layout.",
        ],
    },
]

EXPECTED_COUNT = 6
