# root.node Code

`rootnode-code` designs and maintains Claude Code environments. It is part of [root.node](https://rootnode.design), distributed through the `rootnode` marketplace in [drayline/rootnode-skills](https://github.com/drayline/rootnode-skills).

## Skills

- `cc-design`
- `repo-hygiene`

In Claude Code these list as `/rootnode-code:<skill>`.

The plugin also carries two hooks: a guard that blocks edits to protected migration paths, and a bounded Stop hook that requires test evidence. Hooks run in Cowork and Claude Code only; chat loads the skills and ignores the hooks.

Both hooks apply in every repository where the plugin is enabled. The Stop hook needs test evidence at `.claude/state/last-test-evidence.json`, and writes its state under `.claude/state/`. In a repository without tests, set `VERIFY_GATE_OFF=1`. To turn off the migration guard, set `MIGRATIONS_GUARD_OFF=1`.

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
