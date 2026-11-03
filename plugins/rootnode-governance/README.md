# root.node Governance

`rootnode-governance` governs autonomous work with review gates, routing, and handoffs. It is part of [root.node](https://rootnode.design), distributed through the `rootnode` marketplace in [drayline/rootnode-skills](https://github.com/drayline/rootnode-skills).

## Skills

- `critic-gate`
- `handoff-trigger-check`
- `mode-router`
- `profile-builder`
- `session-handoff`

In Claude Code these list as `/rootnode-governance:<skill>`.

## Install

Install in one place only: on your claude.ai account or locally in Claude Code, never both. A plugin added to your account syncs to Claude Code on its own, so installing it locally as well loads two copies.

**On claude.ai:** go to **Customize > Plugins > Add > Add marketplace**, enter `drayline/rootnode-skills`, and turn on **Sync automatically**. The plugin then reaches chat, Cowork, and Claude Code.

**On Claude Code:**

```
claude plugin install rootnode-governance --marketplace drayline/rootnode-skills
```

## Updates

Auto-update is off by default for third-party marketplaces on Claude Code, so update by hand:

```
claude plugin update rootnode-governance@rootnode
```

## License

Apache-2.0. See [LICENSE](LICENSE).
