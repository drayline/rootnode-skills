# Skills and Hooks Composition

Patterns for designing Skills and hooks together. Skills are the unified extensibility model for reusable multi-step procedures (the layer that replaced commands). Hooks are the deterministic enforcement layer. They compose: hooks can auto-activate Skills, Skills can recommend hooks, and the boundary between them is the question "is failure annoying or unacceptable?"

This reference is for DESIGN mode when the deployment plan involves Skills, hooks, or both, and for EVOLVE mode when the friction is "the agent doesn't follow this rule" (often a sign that a CLAUDE.md preference should be promoted to a hook).

For the placement-rule context (when something belongs in Skills vs CLAUDE.md vs rules vs subagents), see `cc-environment-design-patterns.md`. For the anti-patterns this reference helps prevent, see `cc-anti-patterns.md` (especially §4.3, §4.4, §4.11, §4.12).

---

## Table of contents

1. The hooks-vs-Skills decision tree
2. Skills frontmatter reference
3. Skills auto-activation patterns
4. Hooks lifecycle reference (exit codes, JSON, config shape, events)
5. The verification iron law (as hook), bounded
6. Common composition patterns
7. The Skills/Commands legacy boundary

---

## 1. The hooks-vs-Skills decision tree

The boundary between Skills (preference layer) and hooks (enforcement layer) has three tiers, not two:

```
"What happens if Claude doesn't do X?"
│
├─ "Annoying / suboptimal / wastes time" → prompt, Skill, or CLAUDE.md preference (advisory, no guarantee)
│
├─ "Must be seen, but a person or a later gate decides" → advisory check (deterministic, never blocks)
│
└─ "Unacceptable / corrupts data / violates policy / breaks production" → blocking hook (exit 2, at a gate)
```

**The rule:** "if failure is annoying, prompt or skill; if failure is unacceptable, hook." **[obra/superpowers + rosmur convergence; Jose Parreño Garcia framing]**

**The advisory tier.** Deterministic, runs on write (a PostToolUse hook exiting 0), surfaces a finding, never blocks. A check whose tool was unavailable evaluated nothing and does not clear an earlier failure — it reports `NOT_RUN`. Overriding a blocking check is a logged operator decision, forbidden in unattended runs. `[practitioner: awslabs/aidlc-workflows 06-sensors.md]`

**Examples:**

| Want | Failure mode if missed | Mechanism | Fails |
|---|---|---|---|
| "Use 2-space indentation" | Code reviewer asks for re-indent | Skill or CLAUDE.md preference | — |
| "Add tests for new functions" | Coverage drops; tech debt | Skill + advisory coverage check | open |
| "Never delete `migrations/*.sql`" | Production data loss | PreToolUse hook, `exit 2` | closed |
| "Format Markdown with prettier" | Inconsistent formatting | PostToolUse hook running prettier | open |
| "Run tests before declaring done" | Bugs ship | Stop hook requiring test evidence, bounded (§5) | closed, bounded |
| "Don't commit secrets" | Credential leak | PreToolUse hook + gitleaks, `exit 2` | closed |

**The decision rule applied:** if a missed instruction has compounding cost (corrupts production, leaks credentials, irreversible), it's a hook. If the cost is bounded and recoverable, a Skill is sufficient.

**Fail direction and the stderr contract.** Every hook declares which way it fails. Observers fail open (`exit 0`). A guard that loses its own bookkeeping fails toward the last recorded instruction with a one-line note, never into a re-ask loop. Evidence binding a human decision never falls back to a guess. A blocking hook's stderr names the exact next step. Promote a prose rule to a hook only on observed evidence the prose lost; each such hook gets its own off-switch env var and an audit row per block. `[practitioner: aidlc AGENTS.md §Guards; aidlc-plan-approval-guard.ts header]`

---

## 2. Skills frontmatter reference

Skills are folders with `SKILL.md` containing YAML frontmatter. The frontmatter controls activation behavior. **[Anthropic primary docs at https://code.claude.com/docs/en/skills]**

**Required fields:**

```yaml
---
name: skill-name              # kebab-case, max 64 chars, must match folder name
description: |                # max 1024 chars (YAML-parsed); see Step 2a in skill-builder
  What it does. When to use it. Trigger phrases users would say.
  Negative triggers when overlap with other Skills is possible.
---
```

**Activation-control optional fields:**

| Field | Effect |
|---|---|
| `disable-model-invocation: true` | Skill cannot be auto-activated; only explicit user invocation. Use for human-only operations (deploys, irreversible). |
| `user-invocable: false` | Skill is background knowledge only; never directly invoked. Used for Skills that compose with other Skills. |
| `context: fork` | When invoked, runs in a forked subagent context (isolation). Used when the Skill's context is heavy and shouldn't pollute the parent session. |

**Other useful frontmatter:**

```yaml
license: MIT                   # or Apache-2.0, etc.
metadata:
  author: <name>
  version: "1.0"
  original-source: <reference>
compatibility: |               # 1-500 chars; environment requirements
  Requires Python 3.11+, pdfplumber, Playwright.
```

**Skill folder layout:**

```
your-skill/
├── SKILL.md                   # required
├── references/                # optional; loaded on demand
│   └── *.md
├── scripts/                   # optional; executable code
│   └── *.py / *.sh
├── assets/                    # optional; templates, fonts, icons
└── (NO README.md)             # README.md inside skill folder is rejected
```

**Constraints:**
- `SKILL.md` filename is case-sensitive
- Skill folder name must match the `name:` field
- No README.md inside the skill folder (use SKILL.md or references/ for docs)
- Skill names containing "claude" or "anthropic" are reserved
- SKILL.md body should be < 500 lines / ~5000 tokens

---

## 3. Skills auto-activation patterns

**The strong practitioner consensus:** manual-only Skills are often ignored. **[rosmur "Critical Discovery: Skills need auto-activation"; convergence across multiple sources]**

Two activation mechanisms make Skills reliable:

### Mechanism A — Strong description-field auto-activation

Claude decides whether to load a Skill based almost entirely on the description field. A Skill with perfect methodology and a vague description will never activate.

**Description structure:**
```
[What the Skill does] + [When to use it] + [Trigger phrases] + [Negative triggers]
```

**Specificity rules:**
- Include trigger phrases users would actually say ("Use when user says 'audit my CLAUDE.md'")
- Cover both explicit and implicit user requests
- Be slightly "pushy" — Claude has an undertriggering bias
- Add explicit negative triggers when overlap with adjacent Skills is possible ("Do NOT use for X — use other-skill instead")

**Test the description with the 50-description competition test:** "If Claude sees this description alongside 50 other Skill descriptions, will it correctly activate this Skill (and ONLY this Skill) for the right tasks?"

### Mechanism B — Hook-driven activation

Hooks can inject Skill instructions into context regardless of description matching. The command filters the event JSON from stdin; its stdout is added to context (§4).

```json
{ "hooks": { "UserPromptSubmit": [ { "hooks": [ { "type": "command", "timeout": 10,
    "command": "jq -r .prompt | grep -qi audit && cat .claude/skills/audit-helper/SKILL.md; exit 0" } ] } ] } }
```

This is the "if this prompt looks like X, definitely load Skill Y" pattern. Use sparingly — over-injection bloats context — but when a Skill must activate on a specific signal, hook injection is more reliable than description matching alone.

**When to use which mechanism:**

| Scenario | Mechanism |
|---|---|
| Skill should activate for a broad range of related tasks | Description-field (Mechanism A) |
| Skill must activate on a specific signal that's hard to capture in description | Hook injection (Mechanism B) |
| Skill is critical and missing it is unacceptable | Hook injection + description-field (belt-and-suspenders) |
| Skill is for human-only operations (deploys) | `disable-model-invocation: true` (no auto-activation by design) |

**For the Skill description discipline at full depth, see `rootnode-skill-builder` if available** — it's the canonical reference for description-field construction, length validation, and the 5-dimension publication review.

---

## 4. Hooks lifecycle reference

Every fact in this section: `[Anthropic docs — hooks (https://code.claude.com/docs/en/hooks), verified 2026-10-22; re-verify on the running version]`. Names, fields, and budgets are product facts; a generated design that names one carries the `cc-delegation-patterns.md` §5 marker.

### Exit-code contract

| Exit code | Effect |
|---|---|
| `exit 0` | Success; JSON on stdout is parsed and applied (a UserPromptSubmit hook's plain stdout is added to context) |
| `exit 2` | Blocking error where the event can block: PreToolUse blocks the call; Stop prevents stopping; UserPromptSubmit blocks the prompt; PostToolUse only shows stderr (the tool already ran). Claude reads stderr as the reason |
| any other code | Non-blocking error — the action goes ahead |

The doc's own warning: "Exit code 1 without valid JSON output is a non-blocking error… If your hook is meant to enforce a policy, use `exit 2`". A guard using the conventional shell failure code enforces nothing (§4.4 enforcement-as-preference, inside a hook). A timed-out `command` hook does not block on PreToolUse unless `onFailure: "block"` is set.

### JSON contract (stdout, with `exit 0`)

- `{"decision": "block", "reason": "…"}` — `block` is the only `decision` value.
- PreToolUse: `hookSpecificOutput.permissionDecision` ∈ `allow` / `deny` / `ask` / `defer`, with `permissionDecisionReason`.
- Universal: `"continue": false` plus `stopReason` overrides everything else.
- With `exit 2`, even `permissionDecision: "allow"` does not let the action through.

### Configuration shape

`"hooks": {"<Event>": [{"matcher": "<exact | a|b | regex>", "hooks": [{"type": "command", "command": "…", "timeout": <seconds>}]}]}`. `matcher` is one string; there is no plural `matchers` array and no `tool_name` / `path_pattern` / `prompt_contains` matcher object — path and prompt filtering happen inside the script, which receives the event as JSON on stdin.

### Event set

| Group | Events |
|---|---|
| Session | `SessionStart`, `SessionEnd` (1.5 s shared budget, raisable to 60 s), `Setup` |
| Prompt | `UserPromptSubmit`, `UserPromptExpansion` |
| Tool | `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PostToolBatch`, `PermissionRequest`, `PermissionDenied` |
| Agent | `SubagentStart`, `SubagentStop`, `TeammateIdle`, `TaskCreated`, `TaskCompleted` |
| Stop | `Stop`, `StopFailure` |
| Context | `PreCompact`, `PostCompact` |
| Model | `PreModelSwitch`, `PostModelSwitch` |
| Environment | `ConfigChange`, `CwdChanged`, `DirectoryAdded`, `FileChanged`, `WorktreeCreate`, `WorktreeRemove`, `InstructionsLoaded` |
| UI | `Notification`, `MessageDisplay`, `Elicitation`, `ElicitationResult` |

**Common uses:**

- **`UserPromptSubmit`** — inject a Skill on a trigger; log prompts; reject a prompt missing a required spec reference.
- **`PreToolUse`** — block writes to sensitive paths (`migrations/**`, `.env*`); `ask` before destructive operations; modify inputs.
- **`PostToolUse`** — auto-format; lint; update a session log.
- **`Stop`** — verification iron law; coverage, lint, CHANGELOG gates. Always bounded (§5).
- **`SessionStart`** — re-inject standing context after resume or compaction.
- **`PreCompact`** — validate state (ledger written, scratch flushed).
- **`SubagentStop`** — keep an in-flight ledger so a Stop hook can wait on background agents without the orchestrator reading anything.
- **`PostToolUseFailure`** — record failed calls for the failure ladder and the session report.

**Authoring example**, `.claude/settings.json` (scripts below and in §5):

```json
{
  "hooks": {
    "PreToolUse": [
      { "matcher": "Edit|Write",
        "hooks": [ { "type": "command", "command": ".claude/hooks/guard-migrations.sh", "timeout": 10 } ] }
    ],
    "PostToolUse": [
      { "matcher": "Edit|Write",
        "hooks": [ { "type": "command", "command": ".claude/hooks/format-python.sh", "timeout": 60 } ] }
    ],
    "Stop": [
      { "hooks": [ { "type": "command", "command": ".claude/hooks/verify-tests.sh", "timeout": 120 } ] }
    ]
  }
}
```

```bash
#!/bin/bash
# guard-migrations.sh — guard; fails closed.
[ "${MIGRATIONS_GUARD_OFF:-0}" = "1" ] && exit 0      # off-switch; audit its use
FILE=$(jq -r '.tool_input.file_path // empty') || { echo "Input unreadable; rule holds. Next step: install jq." >&2; exit 2; }
case "$FILE" in migrations/*|*/migrations/*)
  echo "$(date -u +%FT%TZ) block $FILE" >> .claude/guard.log   # audit row
  echo "migrations/ is protected. Next step: use the migration tool, then stop for review." >&2
  exit 2 ;; esac
exit 0
```

---

## 5. The verification iron law (as hook)

The verification-before-completion pattern (named in obra/superpowers, Marc Nuri's writeup, and rosmur) is the highest-leverage hook to install in any CC project that has runnable tests.

**The pattern:** a `Stop` hook that blocks completion unless the agent provides evidence of test passage.

**Implementation sketch (`.claude/hooks/verify-tests.sh`):**

```bash
#!/bin/bash
# verify-tests.sh — Stop guard; fails closed; bounded.
[ "${VERIFY_GATE_OFF:-0}" = "1" ] && exit 0          # off-switch; audit its use
EV=.claude/state/last-test-evidence.json; CT=.claude/state/verify-gate.count
MAX="${VERIFY_GATE_MAX_BLOCKS:-2}"; mkdir -p .claude/state   # 2 interactive, 8 unattended
[ "$(jq -r '.stop_hook_active // false')" = "true" ] && exit 0   # bound 1
block() {  # $1 = on-task reason naming the next step
  KEY=$(sha256sum "$EV" 2>/dev/null | cut -c1-16); KEY=${KEY:-none}
  LAST=""; N=0; [ -f "$CT" ] && read -r LAST N < "$CT"
  if [ "$LAST" = "$KEY" ]; then N=$((N + 1)); else N=1; fi
  echo "$KEY $N" > "$CT"; echo "$(date -u +%FT%TZ) block $KEY $N" >> .claude/state/verify-gate.log
  [ "$N" -gt "$MAX" ] && exit 0                      # bound 2: release, logged
  echo "$1" >&2; exit 2
}
[ -f "$EV" ] || block "Next step: run the test suite and record the result to $EV."
AGE=$(($(date +%s) - $(stat -c %Y "$EV" 2>/dev/null || stat -f %m "$EV")))
[ "$AGE" -le 300 ] || block "Next step: re-run the test suite; the evidence is over 5 minutes old."
[ "$(jq -r '.pass' "$EV")" = "true" ] || block "Next step: fix the failures recorded in $EV and re-run the suite."
rm -f "$CT"; exit 0
```

**Combined with a CLAUDE.md prompt rule:**

```markdown
## Verification

Before declaring done, run the test suite. Record the result to
`.claude/state/last-test-evidence.json` in the format:
{ "pass": true|false, "tests_run": <n>, "duration_s": <n>, "timestamp": "<iso>" }

The Stop hook will block completion without fresh, passing evidence.
Banned phrases at completion: "should work", "probably fine", "looks good".
```

**Why both prompt and hook:** the prompt teaches the agent the evidence format and the convention; the hook enforces that the convention is followed even on adversarial or careless agent runs. Belt and suspenders. **[obra/superpowers iron law]**

### Bounded Stop hooks

"A stuck block is the ONE way to trap a session" `[practitioner: awslabs/aidlc-workflows core/hooks/aidlc-continue-workflow.ts header]`. Every iron-law hook this Skill emits has both bounds:

1. **Honor `stop_hook_active`** — when Claude is already continuing because of a stop hook, do not block again. `[Anthropic docs — hooks; verify the field name on the running version]`
2. **No-progress cap** — a state file counts blocks on unchanged evidence and releases after N (AI-DLC working values: 2 interactive, 8 unattended), resetting when the evidence changes. The release is logged; the session report records the gate `NOT_RUN`.

The block reason is an on-task continuation naming the missing evidence, never an override-shaped instruction.

### Health carrier for observer hooks

An observer that may legitimately do nothing writes a heartbeat every run (`.claude/hooks-health/<hook>.last`, or the repo's convention) — a formatter hook such as `format-python.sh` (not reproduced here) can open with `date -u +%FT%TZ > .claude/hooks-health/format-python.last` — so a doctor check can tell a healthy idle hook from a silent failure. `[practitioner: aidlc 06-hooks-and-tools.md §PostToolUse]`

### Spec-file tamper check

When a run is bound to a spec digest (brief field 9, `cc-delegation-patterns.md` §2), a PreToolUse guard (`exit 2`) refuses Edit|Write on the spec path, and the Stop hook recomputes the LF-sha256 and blocks on mismatch — the guard catches the agent's edits, the digest every other route. `[generalizable structure — derived from brief field 9 and receipt freeze; not yet observed]`

---

## 6. Common composition patterns

### Pattern A — Skill + auto-activation hook

A Skill that's critical for a class of work, plus a UserPromptSubmit hook that injects the Skill when the prompt matches a trigger.

**When to use:** the Skill's description-field auto-activation is unreliable (broad domain, vocabulary overlap with other Skills) but the activation needs to be near-deterministic.

### Pattern B — Skill + Stop hook

A Skill that defines a complex multi-step procedure, plus a Stop hook that enforces the procedure's completion criteria.

**When to use:** the Skill teaches HOW to do something; the hook enforces THAT it was done.

**Example:** a `release-checklist` Skill that walks the agent through pre-release steps; a Stop hook (`exit 2`, bounded per §5) that blocks completion until each checklist item has been recorded as complete in a state file.

### Pattern C — `.claude/rules/` + PreToolUse hook

A path-scoped rule file that loads when matching files are read, plus a PreToolUse hook that blocks edits to those files unless additional conditions are met.

**When to use:** the rule explains the policy; the hook enforces the boundary.

**Example:** `.claude/rules/security-sensitive.md` documents the security review requirements for `auth/` code; a PreToolUse hook (`exit 2`, matcher `Edit|Write`, path test in the script) blocks writes to `auth/**` unless a recent security review marker exists.

### Pattern D — Subagent + per-subagent MCP scoping

A custom subagent that needs a specific MCP server, with the MCP scoped to that subagent's frontmatter so it doesn't pollute the main session's context.

**When to use:** an MCP is needed only for a specific specialist role; loading it always costs main-session context budget.

**Example:** a `database-investigator` subagent with `mcpServers: ["postgres-mcp"]` in its frontmatter; main sessions don't see the postgres MCP tools unless they delegate to this subagent.

**Re-verify before designing on these** `[practitioner: aidlc 14-claude-features.md, 2.1.159-era spike — verify on the running version; not asserted as fact]`: a `tools:` allowlist in agent frontmatter drops inherited MCP tools unless fully-qualified names (`mcp__<server>__<tool>`) are listed; a bare `mcp__<server>` entry is not honored; a pinned `effort:` is a cap, not a floor.

---

## 7. The Skills/Commands legacy boundary

`.claude/commands/` was the predecessor to `.claude/skills/`. As of 2026, Skills replaced commands as the unified model. Both directories still work, but **new work goes in Skills**.

**Migration pattern:**

| Legacy commands behavior | Skills equivalent |
|---|---|
| Manual-only command (typed by user) | Skill with `disable-model-invocation: true` |
| Auto-suggested command | Skill with strong description-field |
| Command that runs a shell script | Skill that points to `scripts/{name}.sh` in the Skill's own folder |
| Project-scoped commands | Skills under `.claude/skills/` (project-scoped by default) |
| User-scoped commands | Skills under `~/.claude/skills/` (user-scoped) |

**The migration trigger:** if a project has both `.claude/commands/` and `.claude/skills/` with overlapping content, that's `cc-anti-patterns.md` §4.12. Migrate commands to Skills with appropriate frontmatter; delete the commands folder once migrated.

---

## End of Skills and Hooks composition reference
