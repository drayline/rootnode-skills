# Claude Code Platform Landscape — dated 2026-09-11

> **Sweep scope:** Routines, subagents & delegation, agent teams, worktrees, dynamic workflows, hooks, plan mode, settings & managed policy.
> **Sources:** code.claude.com/docs (official), Anthropic blog, GitHub issues, practitioner posts. All facts below are from the official docs unless noted otherwise.
> **Operator's CC version:** 2.1.136. Minimum-version requirements are tagged inline.
> **Revision triggers:** a Claude Code major release, a change to any `CLAUDE_CODE_*` variable default, a new hook event type, or a new orchestration primitive.

---

## 1. Routines

Launched 2026-04-14 as research preview. A routine is a saved CC configuration (prompt + repos + connectors) that runs on Anthropic-managed cloud infrastructure or a self-hosted environment.

**Trigger types (combinable on a single routine):**

| Trigger | Mechanism |
|---|---|
| Scheduled | Hourly, nightly, weekly, or once at a future time |
| API | Per-routine HTTPS endpoint + bearer token; POST fires a session |
| GitHub | Webhook on repo events (PR opened, release, etc.); one session per PR, with follow-up events fed into the same session |

**Operational facts:**

- Available on Pro, Max, Team, Enterprise with CC-on-the-web enabled.
- Daily limits: Pro 5, Max 15, Team/Enterprise 25. Extra usage beyond limits.
- Routines run as full CC cloud sessions — no permission-mode picker, no approval prompts during the run.
- Sessions can run shell commands, use Skills committed to the cloned repo, and call included connectors.
- Create/manage at claude.ai/code/routines, Desktop app (sidebar → Routines → New → Remote), or CLI `/schedule`.
- Team/Enterprise admins disable with the Routines toggle at claude.ai/admin-settings/claude-code.
- Cloud environment configuration (network access, env vars, setup scripts) applies.

**Adjacent scheduling surfaces (not Routines):**

| Surface | Scope | Persistence |
|---|---|---|
| Desktop scheduled tasks | Local machine; fires while app is open | Survives restarts |
| CLI `/loop` + cron tools | Session-scoped; dies when session exits | 7-day auto-expiry on recurring tasks |
| `/goal` | Session-scoped; continues until condition met | Session only |

**Version requirements:** Scheduled tasks require v2.1.72+. Routines are cloud-side and version-independent for the operator's CLI, but creation via `/schedule` requires the CLI to support it.

---

## 2. Subagents & Delegation

### 2.1 Delegation limits

| Variable | Default | Since | Notes |
|---|---|---|---|
| `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` | **20** | v2.1.217 | Ultracode sessions exempt. Blocks Agent tool only; `/subtask` forks and resumes bypass |
| `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` | **3** | v2.1.219 | Was 5 (v2.1.172–216), then 1 (v2.1.217–218), then 3 |
| `CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION` | **200** | v2.1.212 | Per-session cumulative. `/clear` resets. Not documented in env-vars page (confirmed open issue) |

All three are configurable via `settings.json` `env` block or shell export.

### 2.2 Subagent model resolution

Order (v2.1.251+): per-invocation parameter → frontmatter `model` → `CLAUDE_CODE_SUBAGENT_MODEL` → main conversation's model.

Before v2.1.251, `CLAUDE_CODE_SUBAGENT_MODEL` was first and overrode everything.

`CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1` (v2.1.257+): forces all subagents, teammates, and workflow agents onto `CLAUDE_CODE_SUBAGENT_MODEL` (or main model if that is unset). Forks and `model: inherit` skills still use main model.

### 2.3 Built-in subagents

| Agent | Model | Tools | Loads CLAUDE.md? |
|---|---|---|---|
| Explore | Inherits main, capped at Opus on Anthropic API (v2.1.198+; was Haiku before) | Read-only | No |
| Plan | Inherits main | Read-only | No |
| General-purpose | Model order | All subagent tools | Yes |
| claude | Model order | All subagent tools | Yes |
| statusline-setup | Sonnet | — | — |
| claude-code-guide | Haiku | — | — |

Disable built-ins: `CLAUDE_CODE_DISABLE_EXPLORE_PLAN_AGENTS=1` (v2.1.198+) removes Explore and Plan. `permissions.deny: ["Agent(Explore)"]` blocks specific types. `CLAUDE_AGENT_SDK_DISABLE_BUILTIN_AGENTS=1` removes all in `-p` mode.

### 2.4 Subagent frontmatter fields

Required: `name`, `description`. Optional: `tools`, `disallowedTools`, `model`, `permissionMode`, `maxTurns` (partial output marking v2.1.246+), `skills` (preload), `mcpServers`, `hooks`, `memory` (user/project/local), `background`, `effort`, `isolation` (worktree), `color`, `initialPrompt`, `experimental` (`cacheTtl`: v2.1.248+).

### 2.5 Subagent scopes (priority order)

1. Managed settings (org-wide, highest)
2. `--agents` CLI flag (session)
3. `.claude/agents/` (project)
4. `~/.claude/agents/` (user)
5. Plugin `agents/` (lowest)

Hot-reload confirmed: agent file changes detected within seconds, no restart needed — except when `agents/` directory was newly created mid-session (restart required). Confirmed on v2.1.136 by probe.

### 2.6 Fork mode

Default on in interactive sessions (v2.1.232+), off in `-p` and Agent SDK. `CLAUDE_CODE_FORK_SUBAGENT=1` enables everywhere; `=0` disables everywhere. Forks inherit full conversation context, system prompt, tools, model, and prompt cache. Cannot spawn further forks.

### 2.7 Background subagents

Background is the default when fork mode is on. Background subagents now surface permission prompts to main session (v2.1.186+). Background subagents have a reduced built-in tool set (Read, Grep, Glob, Bash, PowerShell, Edit, Write, NotebookEdit, WebFetch, WebSearch, TodoWrite, Skill, ToolSearch, EnterWorktree, ExitWorktree, Monitor, TaskStop, SendMessage, Artifact).

### 2.8 Subagent output scanning (v2.1.210+)

Inserts backslashes into text imitating CC tags. Prepends marker line for permission-setting mentions. Does not reword content.

### 2.9 Persistent subagent memory

`memory` field: `user` (~/.claude/agent-memory/), `project` (.claude/agent-memory/), `local` (.claude/agent-memory-local/). First 200 lines or 25KB of MEMORY.md injected at startup. Part of auto-memory; disabled if `autoMemoryEnabled` is off.

---

## 3. Agent Teams

Research preview since v2.1.32 (2026-02-05). Coordinates multiple CC sessions; a team lead session breaks down tasks, spawns teammates.

- Named subagents spawned from main conversation launch as teammates (when teams enabled and not a fork).
- Teammates get task tools and cron tools in addition to their subagent tool set.
- Teammates in split-pane display mode run as separate CC processes with their own model.
- In-process teammates cannot spawn background subagents (error on `background: true`).
- Can reference subagent definitions for teammate configuration.
- Workflow agents and teammates follow their own limits, not `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`.

---

## 4. Git Worktrees

`isolation: worktree` gives a subagent its own temporary git worktree, branched from the default branch (not HEAD).

- Worktree auto-cleanup if subagent makes no changes.
- Bash/PowerShell commands inside worktree-isolated subagent are checked: redirect vectors into main checkout blocked; unverifiable git commands refused (v2.1.210+).
- Commands targeting removed worktree fail with error (v2.1.203+; previously ran in main checkout).
- Hook events: `WorktreeCreate`, `WorktreeRemove`.
- When main session itself runs in a worktree, isolation checks apply to the session and all its subagents.

---

## 5. Dynamic Workflows

Research preview since 2026-05-28. Claude writes JavaScript workflow scripts to orchestrate subagents at scale.

- Deterministic control flow in code (loops, branching, intermediate results), not model-decided turn-by-turn.
- Can coordinate dozens to hundreds of subagents.
- Workflow agents follow their own limits, not the subagent concurrency cap.
- Includes adversarial checking pattern: independent agents verify findings before synthesis.
- Accessed via the `Workflow` tool (removed from subagent tool pools).

---

## 6. Hooks

30+ lifecycle events as of September 2026.

**Event cadences:**
- Once per session: `SessionStart`, `SessionEnd`
- Once per turn: `UserPromptSubmit`, `UserPromptExpansion`, `Stop`, `StopFailure`
- Per tool call: `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PostToolBatch`
- Subagent lifecycle: `SubagentStart`, `SubagentStop`, `TaskCreated`, `TaskCompleted`
- Permission: `PermissionRequest`, `PermissionDenied` (auto-mode denials)
- Compaction: `PreCompact`, `PostCompact`
- Teams: `TeammateIdle`
- Async/standalone: `WorktreeCreate`, `WorktreeRemove`, `Notification`, `ConfigChange`, `InstructionsLoaded`, `CwdChanged`, `FileChanged`
- MCP-nested: `Elicitation`, `ElicitationResult`
- Display-only: `MessageDisplay` (streams with assistant text)

**Hook handler types:** command (shell), HTTP endpoint, MCP tool call, prompt (LLM evaluation), agent (subagent-based verification).

**Key since last alignment:** prompt hooks and agent hooks added; hooks fire identically across terminal, IDE, Desktop, and cloud sessions; plugin hooks support monitors; subagent frontmatter hooks require workspace trust (v2.1.218+).

---

## 7. Plan Mode

Permission mode value `plan`. Read-only exploration — Write and Edit tools denied.

- Uses Plan subagent for codebase research (inherits model, skips CLAUDE.md).
- `opusplan` composite model: Opus while in plan mode, Sonnet outside.
- Enter with `/plan`; enter at invocation with `permissionMode: plan` in subagent frontmatter.
- ExitPlanMode tool available only to plan-mode subagents.

---

## 8. Settings & Managed Policy

### 8.1 Settings files (precedence: managed > project > local > user)

| File | Scope |
|---|---|
| Managed settings | Org-wide, admin-deployed, highest precedence |
| `.claude/settings.json` | Project, version-controlled |
| `.claude/settings.local.json` | Personal/project, gitignored |
| `~/.claude/settings.json` | User, all projects |

`env` block in any settings file sets environment variables for every session. Settings file values override shell-exported values for the same variable.

### 8.2 Plugins

Bundles of skills, hooks, subagents, MCP servers. Installed from marketplaces or local directories. Plugin subagents cannot use `hooks`, `mcpServers`, or `permissionMode` in frontmatter. Plugin hooks fire alongside session hooks. Plugin monitors run shell commands for session lifetime.

### 8.3 Auto Mode

Permission mode where a background classifier evaluates tool calls against block/allow rules. Default on Pro, Max, and Team plans (unless overridden). When main conversation is in auto mode, subagent `permissionMode` is ignored — auto applies to all.

### 8.4 Managed MCP

`allowedMcpServers` and `deniedMcpServers` policies. `--strict-mcp-config` restricts to configured servers only. Managed settings restrictions apply to all subagents regardless of definition source.

---

## 9. Version Gap Assessment: 2.1.136 vs Current

The operator's CC is 2.1.136. The following Skill-referenced features require versions newer than that:

| Feature | Minimum version | Skill reference |
|---|---|---|
| `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` | v2.1.217 | delegation cap mechanism table |
| `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` (default 3) | v2.1.219 | nesting depth |
| `CLAUDE_CODE_SUBAGENT_MODEL_FORCE` | v2.1.257 | model routing |
| `CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION` | v2.1.212 | per-session budget |
| Explore inherits main model | v2.1.198 | role-table Explore row |
| Fork mode on by default | v2.1.232 | fork-based delegation |
| Subagent output scanning | v2.1.210 | security posture |
| `maxTurns` partial marking | v2.1.246 | return contract |
| `permissionMode: bypassPermissions` exception | v2.1.267 | permission isolation |
| `cacheTtl` experimental field | v2.1.248 | prompt caching |

**Resolution:** The Skill should mark every `CLAUDE_CODE_*` variable and default it names with the minimum version that introduced it, per the existing "dated product fact to verify" convention. The D9a test pass should either upgrade CC or run on the current version and accept that version-gated features are untestable.
