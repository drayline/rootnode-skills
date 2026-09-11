# rootnode-cc-design v4.1.0

Adds an orchestrator/worker delegation architecture to CC designs and makes generated session prompts assert end states instead of starting conditions.

## What's new

- **Delegation patterns.** New reference `references/cc-delegation-patterns.md`. Role-tiered delegation, where a reviewer is never weaker than the builder. A Builder-to-Refuter loop is the default coding topology, with the Refuter spawned without the builder's context. The delegation cap is enforced by mechanism, not by prose. Oversized results route to a scratch file, not into the orchestrator's context. The role table is a menu, not a roster; integration stays with the orchestrator.
- **End-state assertion rule.** Starting conditions are report-only. Halts bind to post-action digests over LF-normalized content, and only over files whose bytes the prompt author holds. Generated changes are asserted by the check that defines done.
- **Product-fact markers.** Every `CLAUDE_CODE_*` setting a design names carries a dated marker to verify against the running Claude Code version.
- **Ultracode.** Designs default it off and state the per-task opt-in path in prose.
- **Diagnostic prompts.** Candidate causes are structured as competing hypotheses, and each named instrument must pass an instrument-fit test before it is used.

## Install

- **Claude.ai / Projects:** upload the `-cp` zip.
- **Claude Code:** extract the `-cc` zip into `~/.claude/skills/`. It creates the `rootnode-cc-design/` folder. Skills load when a session starts, so start a new session after install.
