# root.node Code

`rootnode-code` designs and maintains Claude Code environments. It is part of [root.node](https://rootnode.design), distributed through the `rootnode` marketplace in [drayline/rootnode-skills](https://github.com/drayline/rootnode-skills).

## Skills

- `cc-design`
- `repo-hygiene`

In Claude Code these list as `/rootnode-code:<skill>`.

The plugin also carries two hooks, which work best with `jq` on your PATH. Hooks run in Cowork and Claude Code only; chat loads the skills and ignores the hooks.

Both hooks apply in every repository where the plugin is enabled:

- **Migration guard, with `jq`.** Blocks Claude's file edits under any `migrations/` folder, and shell delete or move commands that name one. It also blocks `find` commands that delete or run a command over one, `find . -delete` and similar with no name filter, and any delete, move, or `find` command with a wildcard that could match one, including `rm *` and a read-only `find . -name '*'`.
- **Migration guard, without `jq`.** Does no parsing. It blocks any call to the five tools it gates — `Edit`, `Write`, `NotebookEdit`, `Bash`, and `PowerShell` — whose hook input contains `migrations` in any case, including a file's content or a path outside the target, and tells you to install `jq`. It allows everything else.
- **Migration guard, limits.** Blocks are logged to `.claude/guard.log` in that repository. The guard reads text, so it is not a guarantee. With `jq`, a `cp` or shell redirect into `migrations/`, a piped delete such as `ls migrations | xargs rm`, and a script that deletes all pass; without `jq` these are blocked, because the guard blocks any input that contains `migrations`, but wildcards and quote-split names such as `mig''rations` pass. A script that deletes passes either way. A repository that needs a guarantee should add the Edit deny rule `"permissions": { "deny": ["Edit(migrations/**)"] }` and `sandbox.filesystem.denyWrite`. To turn the guard off, set `MIGRATIONS_GUARD_OFF=1`.
- **Stop hook.** Does nothing in a repository where it detects no test command. It looks at the session's working directory for a line in `package.json` with a `"test":` key that is not npm's `no test specified` placeholder, a `test`, `tests`, `unittest`, or `unittests` target in a `Makefile`, `makefile`, or `GNUmakefile`, a `[tool.pytest` section in `pyproject.toml`, a `pytest.ini`, `tox.ini`, `noxfile.py`, `go.mod`, `Cargo.toml`, `pom.xml`, `build.gradle`, `build.gradle.kts`, or `mix.exs` file, a `.sln` or `.csproj` file, or a `tests`, `test`, or `spec` folder. Where it finds one, when Claude tries to stop, it looks for `.claude/state/last-test-evidence.json` containing `"pass": true`, written in the last five minutes. Without that, it sends Claude back to work up to twice on unchanged evidence and six times in one stop chain, then releases the stop. Without `jq` it cannot read the evidence or tell one stop chain from the next, so it blocks at most twice on unchanged evidence and six times in total per repository, until `.claude/state/verify-gate.count` is deleted. Nothing in the plugin writes the evidence file, so your test workflow has to; once the file exists, the hook checks it whatever else the repository contains. The hook keeps its own state under `.claude/state/`. To turn it off, set `VERIFY_GATE_OFF=1`.

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
