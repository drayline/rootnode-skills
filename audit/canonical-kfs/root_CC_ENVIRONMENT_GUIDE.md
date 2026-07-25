# root_CC_ENVIRONMENT_GUIDE.md

The methodology for designing Claude Code (CC) environments — the execution surface where Claude operates against repository-aware context and version-controlled artifacts. Surface-specific application of the architectural principles in `root_AGENT_ENVIRONMENT_ARCHITECTURE.md`. Consult this KF when designing a new CC deployment, evolving an existing one, auditing a deployment for structural issues, or producing CLAUDE.md and supporting artifacts for a delivery project.

This KF assumes familiarity with the surface-invariant principles in `root_AGENT_ENVIRONMENT_ARCHITECTURE.md` (placement discipline, decomposition by mechanism, source authority, evidence grounding, lean over comprehensive, files-as-context, halt-and-escalate, behavioral countermeasures). Those principles are not repeated here; this KF applies them to CC.

---

## Terminology

CC is referred to throughout this KF as the **execution surface** — distinct from the chat-side **conversation surface** (Claude Projects). The execution-surface framing is deliberate: CC sessions span a continuum from highly interactive (operator confirms each step) to fully autonomous (agent runs unattended); the architecture should not bake in a runtime mode that may not match the deployment.

**Avoid** as architectural labels: "autonomous execution surface," "autonomous CC," "agent-only context." These framings imply unattended operation as the default; many production CC deployments are operator-supervised by design. Architecture descriptions that imply autonomy create false expectations and constrain valid deployment patterns.

**Use:** "execution surface" for CC. "Conversation surface" for chat-side Projects (CP). When the runtime mode matters (autonomous vs. supervised, scheduled vs. on-demand), specify explicitly in context — do not bake the assumption into the architectural label. Descriptive uses of "autonomous" remain valid where the context genuinely is autonomous (e.g., "autonomous iteration scope," "autonomous engine evolution," "long-running autonomous sessions"); the discipline applies to the surface label specifically, not to every appearance of the word.

**Propagation.** This terminology is canonical for CC architecture descriptions. Downstream uses — references in `root_AGENT_ENVIRONMENT_ARCHITECTURE.md` to CC, Distribution project external materials (website copy, README, marketing language), blog posts and product documentation — should adopt the same terminology when describing CC at the architectural layer. The runtime-mode-neutral framing also matches the §8 Routines section's positioning (scheduled CC deployment surface), where the same architecture supports both unattended and operator-reviewed modes.

`[generalizable; grounded in Block 4 from prior CV — operator's reasoning: CC sessions span manual to autonomous; architecture should not bake in runtime mode]`

---

## 1. The 7-layer CC architecture

A Claude Code environment is composed of seven mechanisms. Each has a load profile (when its content reaches Claude), an authority profile (whether the content is enforced or merely advised), and a workflow fit (which kinds of work the mechanism naturally supports). Misplaced content is the dominant failure mode in CC deployments — most reliability problems trace to content that lives in the wrong mechanism.

| # | Mechanism | Location | Load profile | Authority | Workflow fit |
|---|---|---|---|---|---|
| 1 | CLAUDE.md | Repository root (and nested in monorepos) | Loaded every session, full content | Advisory (model reads and complies) | Stable always-relevant facts |
| 2 | `.claude/rules/` | `.claude/rules/{name}.md` with `paths:` frontmatter | Loaded on demand when matching files are read | Advisory (scoped to file context) | File-pattern-specific conventions |
| 3 | Skills | `.claude/skills/{name}/SKILL.md` | Loaded on demand when description matches task | Advisory (procedural guidance) | Reusable multi-step procedures |
| 4 | Subagents | `.claude/agents/{name}.md` | Spawned with own context window | Advisory (specialized prompt) | Focused specialists with isolated context |
| 5 | Hooks | `.claude/settings.json` (hooks section) | Run deterministically on lifecycle events | **Enforced** by runtime | Lifecycle guarantees |
| 6 | MCP servers | `.mcp.json` | Tool schemas in context, data fetched on demand | Advisory (tool definitions) | External data and APIs |
| 7 | Settings + permissions | `.claude/settings.json` (permissions section) + managed policy | **Enforced** by runtime | Trust and permission boundaries |

Two of the seven layers (hooks and settings) provide deterministic enforcement. The other five layers carry content the model reads and is expected to comply with. The placement rule: if compliance must be guaranteed, use hooks or settings. If compliance is preferred but not invariant, use the appropriate advisory layer.

The seven layers below are explained in turn. For each: when to use it, when not to, common misplacement that produces the wrong layer choice.

### 1.1 CLAUDE.md (always-loaded standing context)

CLAUDE.md is the highest-leverage artifact in any CC deployment. It loads at session start and stays in context for the duration. Well-structured CLAUDE.md content prevents the majority of failure modes that derail agentic sessions.

**Use CLAUDE.md for:** stable facts that affect every decision the agent makes; mission and scope statements; authority constraints; halt-and-escalate triggers; pre-flight checklists; the agent's standing context for "what is this project, how do I behave here."

**Do not use CLAUDE.md for:** multi-step procedures (use Skills); per-directory or per-extension conventions (use path-scoped rules); reference material that is occasionally consulted but doesn't affect every decision (use separate files Claude reads on demand); behavioral guarantees that must hold deterministically (use hooks).

**Length discipline:** target under 200 lines per CLAUDE.md file (per Anthropic primary documentation guidance). Longer files reduce adherence — important rules get lost in noise. When CLAUDE.md exceeds 200 lines, audit each section against the placement rule. Multi-step procedures move to Skills. Path-specific rules move to `.claude/rules/`. Reference material moves to dedicated files. Behavioral guarantees move to hooks.

CLAUDE.md sections come in two tiers (§2 below): required for every deployment (no exceptions) and warranted (add only when the inclusion test passes).

### 1.2 `.claude/rules/` (path-scoped on-demand rules)

Path-scoped rules load on demand when matching files are read. Each rule file has `paths:` frontmatter declaring which file patterns trigger loading.

**Use path-scoped rules for:** per-directory conventions (e.g., "files in `src/api/**` follow this naming convention"); per-extension rules (e.g., "all `.tsx` files use this component pattern"); per-subsystem rules that don't apply when working elsewhere in the codebase.

**Do not use path-scoped rules for:** rules that apply to every file in the project (use CLAUDE.md instead — promoting a path-scoped rule to CLAUDE.md when it actually applies universally is a common discovery during audit); rules that specify multi-step procedures (use Skills with file-pattern triggers in the description).

The mechanism is most valuable in monorepos and large codebases where conventions vary by subsystem. In small single-package repositories, path-scoped rules add overhead with little benefit — most concerns can live in CLAUDE.md.

### 1.3 Skills (`.claude/skills/`)

Skills are reusable multi-step procedures with explicit triggering conditions. The Skill's `description:` field determines auto-invocation — Claude reads the description and decides whether the current task matches.

**Use Skills for:** workflows the agent performs repeatedly across sessions (audit procedures, build pipelines, deployment workflows); procedures with multiple steps that benefit from progressive disclosure (the Skill's SKILL.md is loaded fully; references/ files are consulted on demand); patterns that have surfaced 3+ times in real use and are documented well enough to codify.

**Do not use Skills for:** content that is purely reference (no procedure — use a regular file that Claude reads on demand); enforcement guarantees (use hooks); always-loaded facts (use CLAUDE.md); patterns that have only surfaced once or twice in speculative future use (use a paste-and-edit template until the pattern is recurring).

**Auto-activation discipline:** the Skill's `description:` field must include verb-based triggering language ("build," "review," "audit," "convert") and context phrases users actually say. Static descriptors ("a Skill for X") activate poorly. The auto-invocation default should be on — `disable-model-invocation: true` is reserved for Skills that should genuinely be human-only (destructive operations requiring explicit invocation, multi-step workflows where auto-invocation would skip a required earlier step).

**Description length cap:** 1024 characters (YAML-parsed). Tight constraint — every word earns its place.

**SKILL.md body length:** under 500 lines. Beyond that, content extracts to references/. Progressive disclosure is the load-management discipline: name and description (~30-50 tokens) load at startup, SKILL.md loads on activation, references/ files load only when the SKILL.md cites them for a specific task.

The Skill design and packaging methodology lives in the `rootnode-skill-builder` Skill (CP-side, used in this seed Project to build deployment-ready Skill files from design specs).

### 1.4 Subagents (`.claude/agents/`)

Subagents are focused specialists with their own context window. The parent conversation invokes a subagent for a specific task; the subagent runs with its own prompt, tool access, and context, then returns a result. The parent conversation's context is not polluted with the subagent's working set.

**Use subagents for:** independent review of a *different* agent's work (a code reviewer reviewing the implementation agent's diff, a test writer producing tests against a spec another agent authored, a docs proofreader reviewing content another agent drafted); research-heavy side tasks that would flood the main conversation with file contents not referenced again; work that requires a fresh perspective uninfluenced by the implementation conversation; specialized roles that recur across sessions.

**Do not use subagents to verify the model's own work.** Opus 5 verifies its own work automatically (see `root_OPTIMIZATION_REFERENCE.md` Behavioral Tendencies §11 — over-verification). A subagent spawned to "double-check" the parent's output is duplicate cost for no quality gain, and the "use a subagent to verify" pattern is one of the specific instructions Anthropic's Opus 5 prompting guide names for removal. The Critic role (see §3.2) survives this rule because it is independent re-derivation of a *different* agent's proposed change against invariants — not the same agent re-checking itself.

**Do not use subagents for:** "coverage" — using more agents because more is better is anti-pattern; sequential work where each step depends on the previous (subagents block on each other); same-file edits (two subagents editing the same file in parallel produces conflicts); single-perspective tasks where one thorough audit beats four shallow ones; small tasks where delegation overhead exceeds the benefit.

**Delegation caps on Opus 5.** Opus 5 delegates to subagents more readily than prior Opus models. On CC deployments running Opus 5, cap delegation explicitly in CLAUDE.md or Skill instructions — for example: "Delegate to a subagent only for large tasks that are genuinely independent and parallelizable. Do not delegate work you can finish in a handful of tool calls. If one subagent can complete the task, use one rather than several, and keep spawn counts low." Anthropic's Opus 5 prompting guide names this as required prompting discipline for Opus-5-based deployments.

**Built-in subagents first.** Claude Code ships three built-in subagents — Explore (read-only, codebase search), Plan (read-only, used in plan mode), general-purpose (full tools, complex multi-step work). Default to built-ins where they fit; create custom subagents only when a recurring specialist role emerges with clear warrant.

**Custom subagent reliability requirements:**
- *Specific `description:` field.* Claude uses this to decide auto-delegation. "Reviews code for security issues before commits" routes better than "security expert."
- *Restricted tool access.* Read-only for review roles, full tools for implementation roles. Tool restriction is the cheapest reliability gain available.
- *Focused system prompt.* One expertise area per subagent; not "general-purpose plus also security plus also testing."

**The agent-warranted test.** Before recommending a multi-agent topology, apply the agent-warranted test: does the work require multiple distinct cognitive perspectives running in parallel, or sequential decomposition with handoffs? If the work is a single-loop iteration (read, edit, verify, repeat), a single Claude Code session is the right architecture — adding subagents introduces coordination overhead without proportional benefit.

Signals that warrant multi-agent topology: verification requires perspectives that conflict by design (structural correctness vs. visual quality vs. content fidelity); work decomposes into independent units that parallelize *and* an implementation plan exists *and* tasks are mostly independent; a class of decisions requires independent re-derivation (Critic role); research-heavy side tasks would flood main context.

Signals that don't warrant multi-agent: "coverage"; sequential chains; same-file edits; single-perspective verification; small tasks; work requiring agents to coordinate with each other directly (use agent teams instead — different mechanism).

### 1.5 Hooks (`.claude/settings.json`)

Hooks run deterministically on lifecycle events. They are the enforcement layer — what hooks block, the model cannot bypass; what hooks require, the model cannot skip.

**Use hooks for:** lifecycle guarantees that must hold regardless of model judgment ("never write to migrations/ outside scheduled migration tasks"); verification gates that block completion without evidence ("Stop hook: do not declare task complete without test evidence"); policy enforcement that must not depend on prompt compliance.

**Do not use hooks for:** preferences (use CLAUDE.md or path-scoped rules); guidance the agent should reason about (use Skills); reference material (use files Claude reads on demand).

**The enforcement-as-preference anti-pattern.** A common failure mode in CC deployments: writing rules in CLAUDE.md like "always run tests before committing" or "never modify the migrations folder" without backing them with hooks. CLAUDE.md is advice, not enforcement. The model may comply 95% of the time; the 5% it doesn't is when the failure surfaces. If a guarantee must hold, the rule must be a hook, not a CLAUDE.md sentence.

Hook events include PreToolUse (block before action), PostToolUse (verify after action), Stop (gate completion), and others per Anthropic primary documentation. Choose the event by the timing of the guarantee.

### 1.6 MCP servers (`.mcp.json`)

MCP servers expose external data sources and APIs to Claude Code. Tool schemas load into context; data is fetched on demand when tools are invoked.

**Use MCP for:** integrations with external services that are part of the agent's actual workflow (GitHub for repo operations, observability servers for logs, browser/devtools for UI work); data sources whose content is too large to paste into context but whose summaries inform decisions.

**Do not use MCP for:** information available in the repository itself (read the file directly); integrations the agent doesn't actually need for the workflow ("for completeness" is anti-pattern); servers with bloated tool definitions when a lighter integration suffices.

**MCP minimalism.** Each MCP server consumes context for its tool schemas — and this cost is per-turn, not per-invocation. Every enabled server's schema is injected into the context window on every turn regardless of whether any tools are called. This makes MCP overhead the single largest context cost lever in most CC deployments, compounding across subagent spawns. Heavy MCP usage is a named anti-pattern (see `root_AGENT_ANTI_PATTERNS.md` §4.2) — when MCP tool schemas exceed roughly 20K tokens (community heuristic, not an Anthropic-published threshold), Claude Code has too little room left to plan and implement effectively. Anthropic's deferred tool loading (Claude Code 2026) reduces but does not eliminate this concern. For long-running autonomous sessions, audit enabled MCPs before starting — the per-turn savings compound across every subagent the orchestrator spawns.

The discipline:
- Start a new project with 2-3 essential MCP servers (typically GitHub + a logging/observability server + browser/devtools as needed for UI work).
- Add additional MCPs only when ROI is concrete — the work demonstrably needs the server's tools, and no lighter-weight integration suffices.
- Selection criteria: prefer servers with concise tool descriptions, summarized output (not raw JSON dumps), and indexed/queryable interfaces over those that return large payloads.
- Audit periodically: count tool schemas in active context; if approaching 20K tokens, trim.
- Per-subagent MCP scoping (`mcpServers:` in subagent frontmatter) keeps tool definitions out of the main conversation when only a specialist needs them.

### 1.7 Settings + permissions (`.claude/settings.json` + managed policy)

Settings configure what the runtime allows. Permissions are enforced by the runtime before the model sees the action — they are the trust boundary, not advisory text.

**Use settings/permissions for:** trust decisions (which directories the agent may write; which network endpoints it may reach; which tools require explicit approval); compliance requirements that must hold across all sessions (managed policy for organizational rules); permission modes appropriate to the deployment context (sandboxed for local autonomy, auto mode for trusted infrastructure, default for normal supervision).

**Do not use settings/permissions for:** advice (use CLAUDE.md); procedures (use Skills); preferences without consequence (use lighter mechanisms).

**Settings hierarchy.** Managed policy → CLI flags → local project settings → user settings. Higher-priority settings override lower-priority. Use this to deploy organizational guarantees (managed policy) that project-level settings cannot weaken.

**Permission modes.** Plan, default, acceptEdits, auto, dontAsk, bypassPermissions, plus inherited variants. Match the mode to the deployment's risk profile. `bypassPermissions` outside sandboxed environments is a named anti-pattern — speed-over-safety in environments where mistakes have real consequences.

---

## 2. CLAUDE.md design

CLAUDE.md is the load-bearing artifact for any CC deployment. The structural pattern below is generalizable; the specific content is project-specific.

### 2.1 Required sections (every CLAUDE.md)

These five sections must be present, regardless of deployment size or maturity. Their absence is itself the failure mode.

**R1 — Mission statement.** One paragraph. What the project produces, who it's for, what "shipped" means. Sets the success criteria every agent decision is measured against.

**R2 — Authority matrix.** A tiered table defining what content classes Claude has authority to modify, mirror, or originate. Three tiers is the typical shape (source-only / mirror-exact / free design), but the specific tier definitions are project-specific. Examples: production database schemas (mirror-only); customer-facing copy under brand approval (source-only or escalate); generated code matching an approved API contract (mirror-exact); UI chrome and presentational code (free design). Identify the tiers for the specific project; the three-tier shape generalizes, the specific definitions don't.

**R3 — Bug-fixing authorization scope.** Explicit in-scope and out-of-scope lists for autonomous iteration. Without scope, agents either over-edit (causing regressions) or freeze on every decision (losing autonomous leverage). The framework that worked across deployments has three categories: in-scope (proceed without surfacing), in-scope-with-notification (proceed but note the change in change_log), out-of-scope (halt and escalate). Specific category contents are deployment-specific.

**R4 — Halt-and-escalate triggers.** Conditions under which the agent must stop and surface to a human. Examples that apply broadly: authority-matrix tier boundary approach, schema or contract change between layers, test count drop, regression detected, ambiguity that cannot be resolved from CLAUDE.md alone. Specific triggers are deployment-specific. **Non-negotiable.** Without halt triggers, the failure mode is silent corruption — agents iterate themselves into a worse state without surfacing the change. For guarantees that absolutely cannot be missed, back the trigger with a hook — CLAUDE.md text alone is preference, not enforcement.

**R5 — Pre-flight checklist.** What every agent must do before making changes. At minimum: enumerate available Skills, read CLAUDE.md authority matrix, read change_log tail, run the test backstop, verify the orchestrator/build runs clean. Even on day 1 of a new deployment with no change_log yet, the pre-flight names the steps the agent will perform once those artifacts exist.

**Skill-availability enumeration.** Before reading other files or beginning work, the CC agent enumerates available Skills from the system reminder and confirms expected runtime tooling is loaded. If the agent expects to compose with `rootnode-critic-gate`, `rootnode-mode-router`, or another runtime Skill, verify it appears in the available-skills list. If a Skill is unexpectedly missing or unexpectedly present, halt and surface to operator before proceeding. This applies to all CC prompts regardless of whether composition is planned — preventive enumeration catches silent assumption errors at session start rather than mid-execution. `[generalizable; grounded in Phase 31d execution 2026-05-06 — prior CC agent inferred a runtime Skill was unavailable from repo source presence rather than checking its loaded tool list; R2 fallback absorbed the failure but masked the cause]`

### 2.2 Warranted sections (add when the inclusion test passes)

These three sections add real value when their warrant condition is met. When the warrant is not met, omit the section entirely — do not include it as a placeholder. A skeleton "Engine state snapshot" with no real state is worse than no section, because it teaches the agent that the section is decorative.

**W1 — Engine state snapshot.** Auto-updated section listing current state: version, registered components, test count, last full-build time, halt-violation count. *Inclusion test:* the deployment has measurable state that changes session-to-session and the agent's behavior should differ based on that state. If the deployment is a single script or the state is static, omit. *Placement when included:* immediately after the authority matrix.

**W2 — Common bug patterns to recognize.** A pattern catalog written from accumulated debugging history. Each pattern: name, root signal (the diagnostic phenomenon), default first-cut diagnosis (where to look first). *Inclusion test:* the deployment has accumulated at least 3 distinct, recurring bug patterns from real debugging history (typically reflected in 3+ change_log entries that share a structural shape). On day 1 of a new deployment, this section does not yet exist — do not pre-fill speculative patterns. They become noise that crowds out real ones once the change_log starts producing them. Add the section when the third recurring pattern surfaces. *Placement when included:* near the top, after the authority matrix and (if present) the engine state snapshot.

**W3 — Agent dispatch matrix.** Which agent type (built-in Explore, Plan, general-purpose; custom subagents; verification specialists) handles which class of work. *Inclusion test:* 3+ distinct agent types are in regular use. Below that threshold, the dispatch decision is trivial and the matrix is decorative. *Placement when included:* after the scope authorization sections, before the pre-flight checklist.

### 2.3 Length and structure discipline

Target under 200 lines. When CLAUDE.md exceeds the ceiling, audit each section against the §1 placement rules. Multi-step procedures move to Skills. Path-specific rules move to `.claude/rules/` with `paths:` frontmatter. Reference material moves to dedicated files. Behavioral guarantees move to hooks.

**Specificity over generality.** "Use 2-space indentation" beats "Format code properly." "Run `npm test` before committing" beats "Test your changes." Vague rules consume context tokens without changing behavior.

**CLAUDE.md and auto memory.** They complement each other but are not interchangeable. CLAUDE.md is human-authored, version-controlled, team-shared. Auto memory (Claude Code v2.1.59+) is machine-written, machine-local, per-working-tree. Use auto memory for incidental learnings Claude discovers session-to-session; use CLAUDE.md for deliberate team-shared context. Auto memory entries that prove team-relevant should be promoted to CLAUDE.md; otherwise teammates can't see them.

### 2.4 CLAUDE.md anti-patterns

The full unified anti-pattern catalog lives in `root_AGENT_ANTI_PATTERNS.md`. The CLAUDE.md-specific patterns (most-cited in real audits):

- **Bloat** — > 200 lines, multi-step procedures embedded inline, file-pattern-specific rules crammed in. Migrate per §1.
- **Conversational framing** — "Hi Claude, in this project you'll be helping with..." reduces perceived authority. Write declaratively.
- **Reference material mixed with rules** — full API schemas, complete data dictionaries belong in separate files Claude reads on demand.
- **Aspirational language** — "Strive for excellence" and "follow best practices" don't constrain behavior. Specify the behavior with measurable criteria.
- **Stale state sections** — an "Engine state snapshot" not updated in months is worse than no snapshot. Either auto-update or delete.
- **Pre-filled warranted sections** — including W1/W2/W3 with placeholder content because the structure feels incomplete without them. The structure is correct without them when the inclusion test fails.
- **Enforcement-as-preference** — instructions like "always run tests" or "never modify migrations" without backing hooks. If failure is unacceptable, move the rule to a hook.

---

## 3. Agent topology

### 3.1 The verification topology pattern

For deployments where verification requires perspectives that conflict by design — structural correctness, runtime behavior, content fidelity — a common topology uses three specialists plus a cross-verifier. Each specialist catches a different bug class; the cross-verifier reconciles conflicts and investigates discrepancies.

The specialists adapt to the domain by substituting per-agent specialty:

| Role | Generalized purpose |
|---|---|
| Specialist 1 | Code structure / API contract / schema validity |
| Specialist 2 | Runtime behavior / integration tests / E2E flows |
| Specialist 3 | Data integrity / business logic correctness / spec compliance |
| Cross-verifier | Reconciles the three specialists; investigates discrepancies |

The cross-verifier role is structurally invariant across deployments. The other three are domain-substituted.

This pattern is `[generalizable]`. It applies whenever verification requires conflicting perspectives. For deployments where one thorough audit suffices (single perspective, low stakes), a single agent is the right architecture — the four-agent pattern is over-engineering.

### 3.2 When to expand to Orchestrator + Critic + Scribe

A more elaborate topology introduces an Orchestrator (decomposes goals into work units), a Critic (independent re-derivation per change), and a Scribe (institutional memory updates). This is `[proposal, not validated]` — the structural pattern is sound, but the expansion has not been validated as universally beneficial. Recommend the expansion only when:

- Multiple production runs per session exist and goal decomposition becomes overhead the user wants automated.
- A Critic gate is needed because changes have high blast radius (e.g., they touch invariants the authority matrix protects).
- Institutional memory updates are recurring overhead the user wants automated.

If none of these apply, the expansion is over-engineering — recommend deferring until the gap is observed.

The Critic role is available as a standalone Skill (`rootnode-critic-gate`) without requiring the full Orchestrator+Scribe expansion. When per-change governance is warranted but the full expansion would be over-engineering, the Critic Skill alongside a verification topology is a middle ground.

**The Critic role and the Opus 5 self-verification-instruction discipline.** The Critic role reviews a *different* agent's proposed change against the authority matrix and invariants — it is independent re-derivation, not the change agent re-checking its own output. This is external-artifact verification (`root_AGENT_ENVIRONMENT_ARCHITECTURE.md §4.14`) and it survives on Opus 5 unchanged. What does not survive on Opus 5: any prompt or Skill instruction that tells the change agent to "use a subagent to verify your own work." Opus 5 already verifies its own work automatically; a subagent doing the same thing is duplicate cost. The Critic Skill's invocation guidance should read as "invoke critic-gate to review this change" (external-artifact verification of a different agent's work), not as "spawn a subagent to double-check your output" (self-directed re-checking).

### 3.3 Agent prompt grounding

Every agent prompt has concrete, verifiable tasks. Never "brainstorm creatively" or "consider all angles." Each agent has a checklist of verifiable assertions, not open-ended exploration. Subagent prompts should also specify the return format (summary, finding list with priority, diff with rationale) so the parent conversation can integrate results without re-injecting raw file content.

### 3.4 Claude Code defaults on Opus 5 and Sonnet 5

**Effort default:** on Claude Code, `effort` defaults to `high` for both Opus 5 and Sonnet 5. This is the Anthropic-recommended starting point (per the models overview and the Opus 5 whats-new page). Do not carry over `xhigh` defaults from Opus 4.7/4.8 prompts without re-running an effort sweep on the deployment's own evals — the inverted rule (`high` is the start; `xhigh` steps up for demanding work; `low`/`medium` are legitimate primary cost controls) applies on CC as it applies everywhere else.

**Model default:** the Claude Code default model moves with Claude Code product releases and is not restated here (consult Anthropic's Claude Code documentation at update time rather than hardcoding a value that will drift). Design deployments to work under the model the user is running, not under a specific model version assumed at design time.

**Breaking-change reminder:** on Opus 5, `thinking: {"type": "disabled"}` at `xhigh` or `max` returns 400. For CC deployments that need thinking disabled, drop effort to `high` or below.

---

## 4. Scope authorization

The framework: explicit in-scope and out-of-scope lists for autonomous iteration, with halt-and-escalate triggers when the agent approaches the boundary. Without this, the failure modes are over-editing (agent makes changes outside the intended scope, causing regressions) and freezing (agent halts on every decision, losing autonomous leverage).

**Three categories:**

| Category | Behavior | Examples (deployment-specific) |
|---|---|---|
| In-scope | Proceed without surfacing | Bug fixes within authorized subsystems; test additions; refactors that don't change public contracts |
| In-scope-with-notification | Proceed but log in change_log | Changes that touch shared utilities; refactors of code in the authorized subsystem that other subsystems depend on |
| Out-of-scope | Halt and escalate | Changes to authority-matrix-protected content; schema or contract changes between layers; modifications to deployment infrastructure |

**Authorization grounding.** The authorization gate must be file-state-grounded. The agent looks at what is actually in the repository to evaluate authorization, not at what the conversation said earlier. This protects against drift when conversation context is lost or compacted. When the agent is uncertain whether a change is in-scope, the grounded check is "what does the authority matrix in the current CLAUDE.md say."

**Halt triggers.** Four classes apply broadly:
- *Authority-matrix tier boundary approach.* The agent's planned change would touch a higher tier than its current authorization permits.
- *Schema or contract change between layers.* A change in one layer requires coordinated change in another (database schema + API + frontend type).
- *Test count drop or regression.* The change reduces test coverage or breaks a previously-passing test.
- *Ambiguity unresolvable from CLAUDE.md.* The agent cannot determine the right action from current standing context.

Specific halt conditions are deployment-specific and live in CLAUDE.md §R4.

---

## 5. Discipline practices

### 5.1 change_log discipline

Every fix, every change, every work item gets an entry in `change_log.md`. Format per entry:

- Work item identifier (WI number, change ID, ticket reference)
- Subsystem affected
- Diagnosis (1-2 sentences: symptom + root cause)
- Fix (what code/config changed, with narrow detection criteria where applicable)
- Verification (concrete metrics: before X, after Y)
- Regression sweep result (how many existing builds re-verified clean)

**Anti-pattern:** vague entries like "improved table parsing" without metrics. The change_log loses its diagnostic value when entries don't include before/after.

The change_log is the durable institutional memory — every new agent reads it cold and inherits the full debugging arc.

### 5.2 Test backstop

A test suite that runs in under 5 seconds and covers the high-risk patterns from the change_log. Examples of "high-risk patterns": invariant assertions (the agent must never violate X), regression cases (specific past bugs that should never recur), boundary conditions (empty inputs, max-size inputs, edge cases that surfaced in production).

**Pre-flight rule:** every agent runs the test backstop before any change, and re-runs it after. If the test count drops or any test fails after a change, the change is rejected and the agent re-derives.

The test backstop is the most cost-effective reliability investment in an autonomous CC deployment. The most common failure mode in extended sessions is the agent fixing one thing and breaking another silently — the test backstop catches this within seconds.

### 5.3 Additive evolution with narrow detection

Engine improvements are additive — they add a new code path gated by narrow detection criteria, rather than modifying an existing path. The discipline produces monotonic improvement: every old artifact rebuilds byte-identical because the fixes only fire on the specific shape they target.

When proposing a fix, design the detection criterion before designing the fix. The criterion should be specific enough that the fix only fires on the failure shape and never on the existing-passing cases. If the detection is broad, the fix has to be perfect; if the detection is narrow, the fix only has to handle the target case.

This discipline is one of the four checks performed by the `rootnode-critic-gate` Skill — when a deployment uses critic-gate to govern autonomous engine evolution, detection narrowness is automatically applied per-change.

### 5.4 Parallel orchestration

When work decomposes into independent units (one unit per service, one per component, one per record), use parallel orchestration. Single CC sessions can run with `--parallel N` to dispatch N units concurrently when they don't depend on each other.

**Anti-patterns:**
- Spawning N agents to do work that scales sequentially (each step depends on previous).
- Using parallel agents to "cover the space" rather than to parallelize independent work.
- No coordination layer — N agents that don't reconcile their outputs produce N inconsistent results.

The agent-warranted test (§3.1) governs whether parallelization is even appropriate before mechanism selection.

### 5.5 Files as primary context surface

This is a surface-invariant principle (see `root_AGENT_ENVIRONMENT_ARCHITECTURE.md` §4.6). Applied CC-side:

- CLAUDE.md, PLANNING.md, SPEC.md, INITIAL.md, change_log.md, SHIP_MANIFEST.md, design briefs, RFCs are version-controlled files the agent reads. Not paragraphs the agent infers from conversation.
- Compaction safety: project-root CLAUDE.md re-injects after `/compact`; nested files reload on demand. Conversation-only instructions are lost.
- The named anti-pattern: **transcript dump** — pasting chat history into Claude Code as a prompt. Always restructure into a spec file first.

### 5.6 Continuation-phrase ambiguity gate

When operator response at a halt point (T3 escalation, end-of-phase checkpoint, end-of-step verification) could be parsed in multiple ways — for example, "Create a merge commit" could mean "I created the merge commit, proceed" or "you create the merge commit via gh pr merge" — the agent asks one targeted clarifying question rather than inferring continuation. Pattern: identify the ambiguity explicitly, enumerate the possible interpretations, ask which applies, halt until disambiguated. The cost of one extra round-trip is negligible compared to the cost of inferring wrong (premature scope-expanding action, or stalling when action was authorized).

The discipline applies whether or not a session prompt specifies an exact continuation phrase. When a session prompt does specify exact phrases, ambiguity is any operator response that doesn't match the literal phrase or a clear semantic equivalent. When no exact phrase is specified, ambiguity is any response that admits two or more reasonable interpretations.

`[generalizable; grounded in Phase 31d merge session 2026-05-07 — agent's halt-on-ambiguity correctly forced explicit operator authorization for `gh pr merge` scope expansion that was not in the original prompt's in-scope list]`

### 5.7 Forward-state-aware artifact authoring

When a CC agent authors an artifact (PR description, release notes, audit document, halt summary) that will itself be committed in a subsequent step, the artifact's references to repo state must anticipate the post-commit state, not the pre-authoring state. Common cases: (1) PR description authored before final audit-artifact commit lands needs to state the post-commit count, not the pre-commit count; (2) release notes authored before tag push needs to reference the tag URL pattern, not assume the tag already exists; (3) audit summaries authored mid-session need to reference SHAs that will exist by completion, not those existing at authoring time.

The discipline: when authoring forward references, prefix with explicit temporal markers — "post-merge:" or "this PR will:" rather than declarative present tense ("is on main"). This prevents drift between authoring time and reading time. Artifacts read mid-flow should not assume completed state that hasn't happened yet; explicit temporal markers make the difference between current-state and expected-state visible.

`[generalizable; grounded in Phase 31d merge session 2026-05-07 — author agent correctly anticipated the audit-artifact commit would change main..HEAD count from 10 → 11 and updated PR description proactively]`

---

## 6. Hooks-vs-prompts boundary

A common architectural decision: should this rule live in CLAUDE.md (or a Skill, or path-scoped rules), or in a hook? The boundary is enforcement.

**Prompt-level mechanisms (CLAUDE.md, Skills, rules) are advisory.** The model reads them and is expected to comply. Compliance is high but not 100%. For preferences and guidance, this is fine.

**Hooks are deterministic.** A PreToolUse hook blocks the action before the model sees the result. A PostToolUse hook runs verification regardless of model decision. A Stop hook gates completion based on deterministic criteria.

Decision rule: if a guarantee absolutely must hold, use a hook. If a preference is acceptable to violate occasionally, use a prompt-level mechanism. The cost of a hook is engineering complexity (you write the hook script, you maintain it). The cost of a prompt-level mechanism is occasional non-compliance.

**Common candidates for hook conversion:**
- "Always run tests before declaring complete" → Stop hook blocking completion without test evidence.
- "Never modify the migrations folder" → PreToolUse hook blocking writes to `migrations/**`.
- "Always update change_log.md after changes" → PostToolUse hook verifying or appending.
- "Verify type-check passes before commit" → PreToolUse hook on Bash(git commit) running type-check.

---

## 7. The chat→Code handoff (round-trip pattern)

Most non-trivial CC deployments involve both surfaces. Design happens chat-side (in a design Project); execution happens code-side (in the delivery repository). The round-trip is a first-class architectural concern.

### 7.1 The forward direction (chat→Code)

Design conversation produces artifacts: CLAUDE.md draft, scope authorization framework, agent topology recommendation, halt triggers, initial CC prompt, file inventory. When the design is ready, the work moves to Claude Code at the delivery repository.

The handoff is gated by readiness. The `rootnode-handoff-trigger-check` Skill formalizes the readiness decision against seven conditions: spec stability, verification surface exists, invariants written down, pump-primer instance done, work decomposes into independent units, rollback cost is tolerable, token/usage budget headroom.

The gate runs CP-side (in the design Project). Three modes: deliberate (caller provides structured `work_context`), proactive sensing (Claude detects handoff signals and offers the gate), conversational walkthrough (Claude walks the seven conditions as discussion topics). Output is structured JSON with verdict and per-condition evidence.

After PASS verdict, the chat-side conversation produces the handoff bundle. The user opens Claude Code at the delivery repository and pastes the bundle to start CC execution.

### 7.2 The reverse direction (Code→chat)

Triggers to return chat-side:

- A pattern emerges across two or more sessions that wasn't anticipated in the design (warrants methodology evolution).
- A new tool, MCP server, or pattern enters consideration (warrants research before adoption).
- Friction with the existing CLAUDE.md surfaces (warrants design refinement — `rootnode-cc-design` EVOLVE mode).
- A reusable artifact extraction would benefit other deployments (warrants template production — `rootnode-cc-design` TEMPLATE mode).
- A halt-and-escalate trigger fired and the resolution requires reasoning beyond the deployed scope (warrants design-time diagnosis).

The reverse handoff is currently informal — the user opens chat-side Claude in the design Project and frames the issue. A dedicated reverse-handoff Skill is on the methodology backlog.

### 7.3 Round-trip discipline

Design with the round-trip in mind. A deployment is one node in a workflow; the value comes from clean handoffs in both directions.

- Every CC deployment plan produced chat-side names the chat→Code handoff point explicitly.
- Every CC deployment specifies the conditions under which work returns chat-side (the §7.2 triggers, scoped to the deployment).
- Both directions are designed before execution begins.

---

## 8. Routines: scheduled CC deployment surface

Claude Code Routines (released April 14, 2026) are scheduled, cloud-hosted CC sessions that run without an open interactive session. Each Routine is a saved CC configuration — prompt + repos + connectors — executed on a trigger (schedule, API call, or GitHub event). Routines are a deployment surface, not a separate runtime: every principle in §1–7 applies, but the absence of human-in-the-loop changes which patterns are safe and which become silent failure shapes. `[Anthropic primary docs]`

### 8.1 How Routines differ from interactive CC sessions

A Routine session has no inheritance from the user's interactive workspace: fresh state, fresh context window, only the configured connectors and the cloned repository's Skills available. Skills committed to the repo's `.claude/skills/` directory and account-level Skills configured on the Anthropic account are accessible; whether user-level Skills installed locally on a developer's machine propagate to cloud Routines is not documented and requires testing per deployment.

The absence of human-in-the-loop is the more consequential difference. There is no checkpoint between "agent decides to mutate" and "mutation lands." Every safety affordance that interactive sessions get from human pauses — catching scope drift in real time, halting on ambiguous instructions, asking clarifying questions — must be designed into the Routine itself before the schedule fires.

Routines on the cloud surface have a one-hour minimum cadence; sub-hourly cycles use `/loop` in an open session or local Desktop Tasks. Each Routine run draws against the account's usage limits the same way an interactive session does — daily cadence × multiple Routines compounds, and a single Routine running daily for a year is over a thousand sessions of usage cost.

### 8.2 Scope authorization and halt discipline for scheduled agents

Default scope for a Routine is read-only. Mutation authority is opt-in, not default, and must be specified explicitly in the Routine prompt. The reason is mechanical: a Routine that "accidentally" opens a PR or commits a change because its prompt was ambiguous about scope is the exact silent-failure shape that an unattended session produces. The scope-authorization principle from §4 applies but with stricter defaults — interactive sessions can rely on the human catching scope drift in real time; Routines cannot.

Halt-and-escalate triggers in Routines are exhaustive lists of forbidden tool calls and operations, not abstract conditions. "Halt if scope expands" is preference; "Halt if you call Edit, Write, NotebookEdit, git commit, git push, gh pr create, gh issue create" is enforcement-language at the prompt level. For guarantees that absolutely cannot be missed, the structural backstop is hooks committed to the repo's `.claude/settings.json` — not the Routine prompt. Connectors with read-only scopes (e.g., a GitHub connector with read-only repo access) are the third defense layer; configure connector scopes to match the Routine's intended authority.

### 8.3 Observation-before-action deployment phase

New Routines deploy in observation-only mode for a meaningful window before any action authority is granted. The window's purpose is calibration: the user reads outputs, validates that the Routine surfaces the right signal, and develops the action discipline that mutation authority later requires. Skipping the calibration window and deploying mutation-capable Routines on day one is the dominant failure mode for first-time Routine users.

Action authority, when granted, is narrow and explicit — "open draft PR with [specific change pattern]" yes, "merge to main" never; "comment on issue" yes, "close issue" never. Each action verb is enumerated. Expansion of authority happens only after the narrower scope has demonstrated reliable behavior over a meaningful window.

### 8.4 Routine prompt design

A Routine prompt is functionally a compressed CLAUDE.md tuned for a single repeated task. The R1–R5 sections from §2.1 still apply (mission, authority matrix, scope authorization, halt triggers, pre-flight checklist) but compressed because the prompt also carries the task specification. For single-purpose Routines (the common case), the prompt structure collapses to: identity/mission, scope authorization (read-only by default), halt triggers (exhaustive), task steps, output format spec, length cap.

Length discipline matters more in Routines than in interactive sessions because the same prompt runs hundreds or thousands of times — a vague instruction that costs 100 extra tokens per run becomes meaningful at scale. Specify outputs as fixed structural formats (sections, ordered lists, length caps) so the consumer of the report — the user, or a downstream Routine that ingests it — reads predictable shape. Sonnet-tier models handle pattern-matching and integrity-check Routines; Opus is reserved for analytical Routines where multi-lens audit (`root_AGENT_ENVIRONMENT_ARCHITECTURE.md` §4.13) or deep reasoning carries the cost premium.

### 8.5 Composition: daily-triad and weekly-audit patterns

The proposed deployment pattern for scheduled agents on a single repo is a daily triad plus a weekly audit. The triad covers three orthogonal angles on the same data: what changed (commit interpretation), what's queued (release-readiness or merge-readiness diff), what's drifting (structural integrity scan). Three angles is the design target — fewer loses cross-validation between routines; more produces report fatigue and unfocused signal. `[proposal, not validated; pattern designed during rootnode-skills audit infrastructure work 2026-05-07]`

The weekly comprehensive audit produces a structured findings report that REMEDIATE-mode CC consumes (`rootnode-cc-design` REMEDIATE) to execute remediation as a separate interactive session. The daily triad then verifies the executed changes on the next run. This closes the loop: weekly audit → remediation execution → daily verification → cycle. The pattern mirrors §3 verification topology at a different cadence — the weekly audit plays Critic, the remediation session plays Implementor, the daily triad plays Verifier.

The pattern composes with the rest of the methodology — `rootnode-repo-hygiene` covers CC-environment audits; `rootnode-cc-design` REMEDIATE consumes findings; the daily triad plus weekly audit becomes the institutionalized version of "did the agent run cause regressions." When designing CC environments that include scheduled agents, treat the triad+audit as the default starting topology and remove components only when scope warrants. Validate the pattern through use; revisit guidance after the first 2–4 weeks of production runs.

---

## 9. Runtime tooling for CC

The CC-side runtime Skills implement methodology patterns from this KF. They are profile-driven and orchestrator-agnostic — they work with Claude Code, n8n, custom orchestrators, or hand-invocation.

| Skill | Implements pattern from | Deployment |
|---|---|---|
| `rootnode-critic-gate` | §5.3 (additive evolution) + §4 (scope authorization) + §1.4 (Critic role) | At the delivery repository |
| `rootnode-mode-router` | Profile selection by runtime context (calendar, time, geofence, custom signals) | At the delivery repository |
| `rootnode-repo-hygiene` | §1 placement audit + §2 CLAUDE.md design + anti-pattern detection | At the delivery repository |
| `rootnode-cc-design` (REMEDIATE mode) | Closes the loop on hygiene findings (§3 audit → §1 placement fix) | At the delivery repository |

(The `rootnode-cc-design` Skill also runs CP-side for greenfield design — DESIGN, EVOLVE, RESEARCH, TEMPLATE modes. Only REMEDIATE mode is CC-native.)

**Layer-fit boundary.** The runtime Skills do not compete with full software-development workflow systems (e.g., GSD, Superpowers). Workflow systems define *how* to do software development; runtime Skills govern *when* autonomous execution is allowed and *with what strictness* per change. The composition: handoff-gate fires before invoking a workflow system; critic-gate reviews changes emerging from a workflow system's execute-phase wave; mode-router selects the active profile that governs both gates. Runtime Skills are thin governance over thick workflow systems.

---

## 10. Common CC anti-patterns reference

The full unified catalog with surface tags, signatures, causes, and fixes lives in `root_AGENT_ANTI_PATTERNS.md`. Most-cited CC-side patterns:

- **Bloated CLAUDE.md** — over 200 lines, multi-step procedures inline, path-specific rules crammed in.
- **Transcript dump** — chat history pasted as prompt.
- **MCP bloat** — too many MCP servers, tool schemas exceed budget.
- **Manual-only Skills** — `disable-model-invocation: true` widespread without justification.
- **Enforcement-as-preference** — guarantees in CLAUDE.md without backing hooks.
- **Subagent overuse / underuse** — too many or too few custom subagents.
- **`bypassPermissions` outside sandbox** — speed-over-safety in non-sandboxed environments.
- **Missing managed policy where required** — compliance-sensitive context with no ceiling-level enforcement.
- **Path-scoped rules opportunity missed** — per-path conventions still in CLAUDE.md, not migrated to `.claude/rules/`.
- **Auto memory misuse** — team-relevant content in machine-local auto memory instead of CLAUDE.md.
- **Verification-before-completion absent** — speculative language ("should work," "looks good") without test evidence. This is external-artifact verification and remains required on Opus 5 — the model does not automatically read the test output.
- **Verification-instruction accumulation (Opus 5)** — CLAUDE.md or Skills instructing the model to "double-check," "re-verify," "include a verification step," or "use a subagent to verify" the model's own output. Opus 5 does this automatically; the instructions compound into over-verification. Remove self-directed re-check instructions; keep external-artifact verification (see `root_AGENT_ENVIRONMENT_ARCHITECTURE.md §4.14`).
- **Subagent over-delegation (Opus 5)** — no explicit cap on subagent spawning; Opus 5 delegates readily on its own and compounds when the CLAUDE.md or Skill invites more. Add a delegation cap in the CLAUDE.md.
- **Conservative-review literalism** — audit or review prompts that say "only report high-severity issues" or "be conservative." Opus 5 follows literally and under-reports. Rewrite to report-everything-then-filter form.
- **Skills/Commands legacy mix** — overlapping `.claude/commands/` and `.claude/skills/` directories.
- **Kitchen-sink session** — 100+ turn sessions mixing unrelated tasks; no `/clear` discipline.
- **Stale CLAUDE.md** — months out of date, references dead patterns.

When auditing a deployment, scan for these patterns explicitly. The `rootnode-repo-hygiene` Skill automates this pass.

---

## 11. Where to go next

For the unified architectural principle layer that governs both CP and CC: `root_AGENT_ENVIRONMENT_ARCHITECTURE.md`.

For CP-side (Claude Project) architecture: `root_PROJECT_ARCHITECTURE_GUIDE.md`.

For the unified anti-pattern catalog with full signatures and fixes: `root_AGENT_ANTI_PATTERNS.md`.

For audit and optimization methodology: `root_AUDIT_FRAMEWORK.md` and `root_OPTIMIZATION_REFERENCE.md`.

For prompt-level work (block libraries, prompt compilation, prompt validation): `root_MASTER_FRAMEWORK.md`, `root_PROMPT_COMPILER.md`, `root_PROMPT_TESTING_GUIDE.md`.

For the Project's lightweight navigation index: `root_CONTENTS_INDEX.md`.

---

*End of root_CC_ENVIRONMENT_GUIDE.md.*
