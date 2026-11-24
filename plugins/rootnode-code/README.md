# root.node Code

`rootnode-code` designs and maintains Claude Code environments. It is part of [root.node](https://rootnode.design), distributed through the `rootnode` marketplace in [drayline/rootnode-skills](https://github.com/drayline/rootnode-skills).

## Skills

- `cc-design`
- `repo-hygiene`

In Claude Code these list as `/rootnode-code:<skill>`.

## Hooks

The plugin carries a migration guard and a test-evidence Stop gate, plus a `SessionStart` hook that records where the Stop gate starts from. They work best with `jq` on your PATH. Plugin hooks run wherever the plugin loads, chat sessions that open a repository included, so both gates are off until a repository asks for them.

**Opt in per repository.** A gate acts only in a git repository whose root holds `.claude/rootnode-gates.json` with that gate's section. Without the file or the section, the hook exits 0 and writes nothing. `cc-design` adds the file when it designs an environment that wants a gate.

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

- **Stop gate (`verify`).** When the session starts, the plugin records a fingerprint of the repository: `HEAD`, `git status`, `git diff HEAD`, and the contents of untracked files. When Claude tries to stop, the gate does nothing if the fingerprint is unchanged, so a turn that only answers passes. If the tree changed, including by a commit or a push, it looks for passing test evidence recorded for the tree as it now stands. Its block message names the repository, the reason, and the command to run: `bash "<plugin>/scripts/record-test-evidence.sh" "<repo root>" "<evidence file>"`. That script runs `verify.command` at the repository root and records the result with the fingerprint. Evidence goes stale when the tree changes again; there is no clock.
- **Watch, then enforce.** `mode` defaults to `watch`: the gate logs each stop it would have blocked and never blocks. Set `"mode": "enforce"` once the log shows it acting on the right turns. In enforce mode it sends Claude back at most `max_blocks_chain` times in one stop chain (default 2, never above `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP`, default 8) and `max_blocks_session` times in a session (default 4), then releases the stop and logs the release.
- **Surfaces.** `surfaces` defaults to `["local"]`. Add `"remote"` to gate cloud sessions (`CLAUDE_CODE_REMOTE=true`) too, for a repository whose tests can run there.
- **Your own evidence file.** A repository that already records its test result can set `"evidence": {"path": ".claude/state/last-verify.json", "pass_field": "pass"}`; `command` is then optional. The file passes only when it carries a `fingerprint` field for the current tree, which `record-test-evidence.sh` writes.
- **Migration guard (`migrations_guard`).** With `"enabled": true` and `jq`, it blocks Claude's file edits under any `migrations/` folder, and shell delete or move commands that name one. It also blocks `find` commands that delete or run a command over one, `find . -delete` and similar with no name filter, and any delete, move, or `find` command with a wildcard that could match one, including `rm *` and a read-only `find . -name '*'`. Without `jq` it does no parsing: it blocks any call to the five tools it gates — `Edit`, `Write`, `NotebookEdit`, `Bash`, and `PowerShell` — whose hook input contains `migrations` in any case, and tells you to install `jq`.
- **Migration guard, limits.** The guard reads text, so it is not a guarantee. With `jq`, a `cp` or shell redirect into `migrations/`, a piped delete such as `ls migrations | xargs rm`, and a script that deletes all pass; without `jq` these are blocked, but wildcards and quote-split names such as `mig''rations` pass. A script that deletes passes either way. A repository that needs a guarantee should add the Edit deny rule `"permissions": { "deny": ["Edit(migrations/**)"] }` and `sandbox.filesystem.denyWrite`.
- **State and status.** The hooks keep their state in the plugin's data folder (`CLAUDE_PLUGIN_DATA`), never in your repository. One log, `gates/gate.log` there, records every block, would-be block, release, and guard block. `bash "<plugin>/scripts/gate-status.sh" --state "<plugin data folder>" [repo root]` prints the counts per gate and the last five log lines.
- **When a gate stays quiet.** A gate that cannot read its input, its config, or `git` does nothing. Without `jq` the Stop gate is inactive and says so on stderr. The baseline is taken when the session starts, or at the first stop in a repository the session entered later, so edits made there before that stop are not gated.
- **Off-switches.** `VERIFY_GATE_OFF=1` turns off the Stop gate and its baseline; `MIGRATIONS_GUARD_OFF=1` turns off the guard. Removing the section from `.claude/rootnode-gates.json` turns a gate off for everyone who uses the repository.

## Install

Install in one place only: on your claude.ai account or locally in Claude Code, never both. A plugin added to your account syncs to Claude Code on its own, so installing it locally as well loads two copies.

**On claude.ai:** go to **Customize > Plugins > Add > Add marketplace**, enter `drayline/rootnode-skills`, and turn on **Sync automatically**. The plugin then reaches chat, Cowork, and Claude Code.

**On Claude Code:**

```
claude plugin install rootnode-code --marketplace drayline/rootnode-skills
```

## Updates

Auto-update is off by default for third-party marketplaces on Claude Code, so update by hand:

```
claude plugin update rootnode-code@rootnode
```

## License

Apache-2.0. See [LICENSE](LICENSE).
