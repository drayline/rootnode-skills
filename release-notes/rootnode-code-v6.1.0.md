# root.node Code v6.1.0

Design and maintain Claude Code environments: environment design and remediation, repository hygiene scanning, plus a migration guard and a bounded test-evidence Stop hook.

Single-plugin release. The current catalog umbrella stays [root.node catalog v6.0](https://github.com/drayline/rootnode-skills/releases/tag/catalog-v6.0).

## Install

- **claude.ai:** **Customize > Plugins > Add > Add marketplace** → `drayline/rootnode-skills`, turn on **Sync automatically**, then add `rootnode-code`.
- **Claude Code:** `claude plugin marketplace add drayline/rootnode-skills`, then `claude plugin install rootnode-code@rootnode`.
- **Manual:** upload `rootnode-code-v6.1.0.zip` from the assets below at **Customize > Plugins > Add > Upload plugin**.

Install once: on your account or locally in Claude Code, not both.

## Skills

| Skill | Version |
|---|---|
| `rootnode-code:cc-design` | 6.1.0 |
| `rootnode-code:repo-hygiene` | 6.0.0 (unchanged) |

## Changes in v6.1.0

In 6.0.0 both hooks acted in every folder on every surface the plugin reached, chat included, and the Stop hook blocked turns that changed nothing. 6.1.0 makes both hooks opt-in per repository and makes the Stop gate change-aware.

- **Opt-in.** A hook acts only in a git repository whose root holds `.claude/rootnode-gates.json` with that hook's section (`verify`, `migrations_guard`). Without it, the hook exits 0 and writes nothing.
- **Change-aware Stop gate.** A new `SessionStart` hook (`gate-baseline.sh`) records a fingerprint of the tree: `HEAD`, `git status`, `git diff HEAD`, and untracked file contents. The Stop gate does nothing while the fingerprint is unchanged. When the tree changed, including by a commit or push, it needs passing evidence recorded for the current fingerprint. The five-minute clock is gone.
- **Evidence written by the plugin.** `scripts/record-test-evidence.sh` runs `verify.command` and records the result with the fingerprint; the block message prints the exact command. A repository can name its own evidence file instead, which must carry the `fingerprint` field.
- **Watch mode by default.** `verify.mode` defaults to `watch`: the gate logs would-be blocks and never blocks. `enforce` blocks, capped per stop chain (default 2, clamped to `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP`) and per session (default 4, never reset).
- **Surfaces.** `verify.surfaces` defaults to `["local"]`; cloud sessions (`CLAUDE_CODE_REMOTE=true`) are gated only when it lists `"remote"`.
- **State out of the repository.** Baselines, counters, plugin-written evidence and the one log, `gates/gate.log`, live in the plugin's data folder (`CLAUDE_PLUGIN_DATA`). The guard no longer writes `.claude/guard.log`.
- **Status.** `scripts/gate-status.sh` prints per-gate counts of blocks, would-be blocks and releases, and the last five log lines.
- **Lockout-safe.** A hook that cannot read its input or its config, cannot run `git`, or cannot load its shared library (`scripts/gate-lib.sh`) does nothing. Without `jq` the Stop gate is inactive; an enabled guard falls back to blocking any call that mentions `migrations`, as in 6.0.0.
- **cc-design.** The hook reference embeds the new scripts and `gate-lib.sh` under `shipped:` markers, documents the config, and rewrites the Stop-hook caps as chain and session caps. The "rootnode-cc-design Skill" prose in `cc-anti-patterns.md` and `cc-design-brief.schema.json` now reads `cc-design`. The shell lessons add that `jq -r` on Windows emits CRLF.
- **Tests.** `audit/v6_1-release/hook-tests/run.sh` runs the acceptance matrix against the scripts.

## Breaking change

No repository is gated after this update until it adds `.claude/rootnode-gates.json`. An existing `.claude/state/last-test-evidence.json` no longer opts a repository in.

## Config example

```json
{
  "version": 1,
  "verify": {
    "mode": "watch",
    "command": "npm test",
    "surfaces": ["local"],
    "max_blocks_chain": 2,
    "max_blocks_session": 4
  },
  "migrations_guard": { "enabled": true }
}
```

Leave out `verify` or `migrations_guard` to keep that hook off. Switch `mode` to `enforce` once `gate-status.sh` shows the gate acting on the right turns.

## Upgrading from v6.0.0

- In each repository where 6.0.0 ran, delete `.claude/state/verify-gate.count`, `.claude/state/verify-gate.log` and `.claude/guard.log`. Delete `.claude/state/last-test-evidence.json` too, unless your own workflow uses it.
- A `VERIFY_GATE_OFF` setting added to work around 6.0.0 is no longer needed; the gate is off in any repository without the config. `VERIFY_GATE_MAX_BLOCKS` and `VERIFY_GATE_MAX_TOTAL` are replaced by `max_blocks_chain` and `max_blocks_session`.
- Add `.claude/rootnode-gates.json` only to repositories that want a gate.
- On a synced install, run `claude plugin update rootnode-code@rootnode` or wait for account sync, then `/reload-plugins`.
