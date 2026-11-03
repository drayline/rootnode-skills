# root.node Prompts

`rootnode-prompts` compiles and scores prompts from a library of blocks and domain packs. It is part of [root.node](https://rootnode.design), distributed through the `rootnode` marketplace in [drayline/rootnode-skills](https://github.com/drayline/rootnode-skills).

## Skills

- `block-selection`
- `domain-agentic-context`
- `domain-business-strategy`
- `domain-content-communications`
- `domain-research-analysis`
- `domain-software-engineering`
- `identity-blocks`
- `output-blocks`
- `prompt-compilation`
- `prompt-validation`
- `reasoning-blocks`

In Claude Code these list as `/rootnode-prompts:<skill>`.

## Install

Install in one place only: on your claude.ai account or locally in Claude Code, never both. A plugin added to your account syncs to Claude Code on its own, so installing it locally as well loads two copies.

**On claude.ai:** go to **Customize > Plugins > Add > Add marketplace**, enter `drayline/rootnode-skills`, and turn on **Sync automatically**. The plugin then reaches chat, Cowork, and Claude Code.

**On Claude Code:**

```
claude plugin install rootnode-prompts --marketplace drayline/rootnode-skills
```

## Updates

Auto-update is off by default for third-party marketplaces on Claude Code, so update by hand:

```
claude plugin update rootnode-prompts@rootnode
```

## License

Apache-2.0. See [LICENSE](LICENSE).
