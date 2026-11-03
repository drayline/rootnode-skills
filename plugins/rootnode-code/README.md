# root.node Code

`rootnode-code` designs and maintains Claude Code environments. It is part of [root.node](https://rootnode.design), distributed through the `rootnode` marketplace in [drayline/rootnode-skills](https://github.com/drayline/rootnode-skills).

## Skills

- `cc-design`
- `repo-hygiene`

In Claude Code these list as `/rootnode-code:<skill>`.

The plugin also carries two hooks, which need `jq` on your PATH. Hooks run in Cowork and Claude Code only; chat loads the skills and ignores the hooks.

Both hooks apply in every repository where the plugin is enabled:

- **Migration guard.** Blocks Claude's file edits under any `migrations/` folder, and shell delete, move, or `find` commands that name one or use a wildcard that could match one, including `rm *` and a read-only `find . -name '*'`. It reads command text, so it is not a guarantee: a `cp` or shell redirect into `migrations/` passes. Without `jq`, it blocks anything that names `migrations` and allows everything else, so wildcard commands pass. To turn it off, set `MIGRATIONS_GUARD_OFF=1`.
- **Stop hook.** When Claude tries to stop, it looks for `.claude/state/last-test-evidence.json` containing `"pass": true`, written in the last five minutes. Without that, it sends Claude back to work up to twice on unchanged evidence, then releases the stop. Nothing in the plugin writes this file, so your test workflow has to. The hook keeps its own state under `.claude/state/`. To turn it off, for example in a repository without tests, set `VERIFY_GATE_OFF=1`.

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
