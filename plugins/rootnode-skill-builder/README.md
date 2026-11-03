# root.node Skill Builder

`rootnode-skill-builder` builds, reviews, and evaluates Skills. It is part of [root.node](https://rootnode.design), distributed through the `rootnode` marketplace in [drayline/rootnode-skills](https://github.com/drayline/rootnode-skills).

## Skills

- `skill-builder`

In Claude Code these list as `/rootnode-skill-builder:<skill>`.

Its scripts need Claude Code or Cowork. The methodology itself works on every surface.

## Install

Install in one place only: on your claude.ai account or locally in Claude Code, never both. A plugin added to your account syncs to Claude Code on its own, so installing it locally as well loads two copies.

**On claude.ai:** go to **Customize > Plugins > Add > Add marketplace**, enter `drayline/rootnode-skills`, and turn on **Sync automatically**. The plugin then reaches chat, Cowork, and Claude Code.

**On Claude Code:**

```
claude plugin install rootnode-skill-builder --marketplace drayline/rootnode-skills
```

## Updates

Auto-update is off by default for third-party marketplaces on Claude Code, so update by hand:

```
claude plugin update rootnode-skill-builder@rootnode
```

## License

Apache-2.0. See [LICENSE](LICENSE).
