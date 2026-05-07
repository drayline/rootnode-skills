# Critic-Gate Availability Root Cause — Phase 31d

## Diagnostic results

- **1a User-level install path:** PRESENT — `~/.claude/skills/rootnode-critic-gate/` contains `SKILL.md`, `examples/`, `profiles/`, `references/`, `schema/`. Verified on 2026-05-05 from the running CC session.
- **1b Frontmatter disable flag:** ABSENT (default). `grep -n "disable-model-invocation" $HOME/.claude/skills/rootnode-critic-gate/SKILL.md` returns no matches (exit=1). Auto-invocation defaults to on.
- **1c In agent's available tools at this CC session:** YES. The `<system-reminder>` block at the start of the Phase 31d conversation enumerated user-invocable skills, and `rootnode-critic-gate` appeared in that list with its full description ("Independent re-derivation gate for proposed changes during autonomous execution. Evaluates a change … against the work's authority matrix and a 4-check protocol …"). All seven rootnode runtime/governance Skills (`behavioral-tuning`, `cc-design`, `critic-gate`, `domain-agentic-context`, `mode-router`, `repo-hygiene`, `skill-builder`) were in the same list.

## Classified root cause

**Agent reasoning error in the prior CC session.**

## Evidence

The Phase 31d agent (same conversation, prior turns) wrote in two locations:

1. B1.3 escalation: *"Critic-gate is not wired in this session (Skills are in repo but not installed/auto-activatable), so this is presented for direct operator approval."*
2. B2.1(d) self-pass surfacing: *"Critic-gate not installed in this CC harness (the Skill directory exists in the repo but isn't loaded as an invokable Skill in the running agent). Per CLAUDE.md R2 Tier 3 ('Surface to operator; do not decide silently'), I'm surfacing the self-pass verdict for direct operator approval before committing B2.1."*

Both claims were incorrect. At the time those statements were made:

- The Skill was installed at the canonical user-level path (`~/.claude/skills/rootnode-critic-gate/`) — verified now at 1a.
- `disable-model-invocation` was not set — verified now at 1b.
- The Skill was enumerated in the running agent's available-skills list at conversation start — confirmed by the visible `<system-reminder>` block content.

The agent inferred unavailability from a wrong signal — most plausibly the visible repo-side Skill directories (`rootnode-skills/rootnode-critic-gate/SKILL.md` etc.), confused with the user-level install path. The repo source presence is unrelated to whether the Skill is loadable as a tool invocation; the relevant signal is the agent's own loaded skill list, which the agent did not consult.

The R2 fallback ("Surface to operator; do not decide silently") absorbed the failure cleanly — both Tier 3 decisions resolved correctly via direct operator approval. But the fallback masked the true cause until post-hoc inspection.

## Prevention recommendation

Add an explicit Skill-availability enumeration step to the seed-Project's CC pre-flight discipline (e.g., `root_CC_ENVIRONMENT_GUIDE.md` R5 pre-flight checklist or its equivalent in repo-specific `CLAUDE.md` files): agents must verify that expected runtime tooling appears in their loaded available-tools list at session start, not infer availability or unavailability from repo source presence. For Phase-31d-style sessions that compose with `rootnode-critic-gate`, the pre-flight should fail fast if the Skill name isn't in the agent's enumerated tool list rather than letting the agent reason about availability mid-session.
