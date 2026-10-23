# Claude-Specific Optimization Notes

A practical reference for writing prompts and building Projects optimized for how Claude actually works. Calibrated for the 5.5 generation: Claude Opus 5.5 and Sonnet 5.5 dual-primary, Fable 5.1 integrated-aware for long-horizon agent workloads, Haiku 5.5 subagent-aware, Opus 5 and Sonnet 5 fallback-graceful, and Sonnet 4.6 legacy-graceful. Consult this document whenever building or refining prompts. Section 3 is the dated model-landscape block (verified 2026-10-22): other files and design records reference it rather than restating its facts, and it is refreshed at each model-release cycle (AEA §4.15).

**Calibration scope:** Opus 5.5 + Sonnet 5.5 **dual-primary** (Opus 5.5 is the Claude Code default on every Anthropic-hosted plan and Anthropic's recommended starting model; Sonnet 5.5 is the cost-optimal agentic tier with the same 1M / 128K envelope); Fable 5.1 **integrated-aware** (default nowhere — reserve it for long-horizon work where Opus 5.5 at higher effort still fails your evals); Haiku 5.5 **subagent-aware** (the first Haiku with a 1M window and effort control, positioned for scout and extraction roles); Opus 5 / Sonnet 5 **fallback-graceful** (the models users are silently served on classifier-flagged requests — output must keep its shape there without user awareness); Sonnet 4.6 **legacy-graceful** until retirement. Haiku 4.5 (out of scope from 2026-10-15, its earliest retirement date) and Mythos 5.1 are out of scope. When this document discusses model behavior without qualification, it refers to Opus 5.5. Where Anthropic documents a behavior for only some models, the entry names them rather than generalizing across the tier.

**Effort-level note:** the effort default moved on the 5.5 generation. Claude Code defaults to `medium` on Opus 5.5, Sonnet 5.5, and Haiku 5.5; on the API the default is `medium` on Opus 5.5 and Haiku 5.5 and `high` on Sonnet 5.5 and Fable 5.1. Anthropic reports Opus 5.5 at `medium` matches or exceeds Opus 5 at `high` on coding and knowledge-work evaluations. The rule from the Opus 5 cycle stands: start at the model's default, adjust on your own evals, use `low`/`medium` as cost controls where quality holds, and step to `xhigh`/`max` only on a measured gain. Do not carry effort settings over from earlier models — re-run an effort sweep. Thinking cannot be disabled on Opus 5.5, Sonnet 5.5, or Fable 5.1.

---

## 1. Structural Formatting That Claude Responds To

### XML Tags Are Claude's Native Structure

Claude was trained to attend strongly to XML tags. Use them to delineate sections of your prompt clearly. This is the single most impactful Claude-specific technique.

```xml
<role>
You are a senior data engineer specializing in pipeline architecture.
</role>

<context>
We are migrating from a monolithic ETL system to event-driven microservices.
The current system processes 2M records/day with a 4-hour batch window.
</context>

<instructions>
Design a migration plan that maintains data consistency during the transition.
</instructions>

<output_format>
Return your response as:
1. Migration architecture overview (2-3 paragraphs)
2. Phase-by-phase plan (table format)
3. Risk register with mitigation strategies
</output_format>
```

**Why this works:** XML tags create unambiguous boundaries between prompt sections. Claude parses these more reliably than markdown headers, numbered sections, or natural language transitions. When a prompt has competing instructions, XML-tagged sections reduce confusion about which instruction applies where.

**Key tags to use:**
- `<role>` — identity and expertise
- `<context>` — background information
- `<instructions>` — the actual task
- `<constraints>` — boundaries and limitations
- `<output_format>` — how to structure the response
- `<examples>` — few-shot demonstrations
- `<input>` — the variable content that changes per use

### Hierarchical Nesting

For complex prompts, nest tags to create clear hierarchies:

```xml
<task>
  <primary_objective>Evaluate the acquisition target.</primary_objective>
  <sub_tasks>
    <financial_analysis>Review the last 3 years of financials.</financial_analysis>
    <market_analysis>Assess competitive positioning.</market_analysis>
    <risk_assessment>Identify deal-breakers.</risk_assessment>
  </sub_tasks>
</task>
```

---

## 2. Long Context: Claude's Key Advantage

Claude handles long system prompts and large context windows exceptionally well. All four current models — Fable 5.1, Opus 5.5, Sonnet 5.5, Haiku 5.5 — support a 1M-token context window with 128K max output; legacy Haiku 4.5 is 200K. See Section 3 for the full landscape. Unlike some models, Claude does not degrade significantly with longer prompts. Use this to your advantage.

### Be Verbose Where It Matters

- **Don't compress instructions to save tokens.** Clarity always beats brevity in system prompts.
- **Include full reference material** in Projects knowledge files rather than summarizing.
- **Repeat critical constraints** at the start and end of long prompts — Claude attends strongly to the beginning and end of context.

### The Primacy-Recency Pattern

Claude pays the most attention to:
1. The very beginning of the system prompt
2. The very end of the system prompt (closest to the user message)
3. Content immediately surrounding the user's input

**Structural implication:** Place your most critical instructions (identity, non-negotiable constraints) at the top. Place output format and quality standards near the bottom, close to where Claude begins generating.

**For long-document tasks (20K+ tokens):** Place longform data and documents near the top of the prompt, with your query, instructions, and examples below them. Anthropic's testing shows queries positioned after documents can improve response quality by up to 30% on complex, multi-document inputs. This aligns with the primacy-recency pattern: the document content occupies the high-attention opening position, while the query sits in the high-attention position closest to generation.

```xml
<!-- TOP: Identity and hard constraints -->
<role>...</role>
<critical_rules>
Never recommend solutions that require downtime exceeding 30 minutes.
Always include cost estimates.
</critical_rules>

<!-- UPPER-MIDDLE: Long documents and reference data (for document-heavy tasks) -->
<documents>...</documents>
<reference_data>...</reference_data>

<!-- LOWER-MIDDLE: Context, background, operational details -->
<context>...</context>

<!-- BOTTOM: Query, output format, and quality checks (close to generation) -->
<instructions>...</instructions>
<output_format>...</output_format>
<quality_standards>...</quality_standards>
```

### Grounding in Quotes for Long Documents

When working with long documents, ask Claude to extract and quote relevant passages before performing its task. This forces Claude to locate the specific evidence rather than generating from its general understanding of the document's themes.

```xml
<instructions>
Before answering, find and quote the specific passages from the documents
that are most relevant to the question. Then base your analysis on
those passages.
</instructions>
```

---

## 3. Model Landscape — dated block (verified 2026-10-22)

This section is the reference for model-fact statements elsewhere in this document and in the other knowledge files. Every fact traces to Anthropic primary documentation fetched 2026-10-22 (sources at the end of the section). It supersedes the 2026-07-24/25 block (Opus 5 + Sonnet 5 dual-primary). Decision records cite this block rather than restating it (AEA §4.15); refresh it at the next model release. Every `CLAUDE_CODE_*` name, default, and minimum version below is a dated product fact — `[verify against the running Claude Code version]` travels with it into any generated design (`root_CC_ENVIRONMENT_GUIDE.md` §6).

**What changed since the last block, in one paragraph.** Four releases in five weeks: Fable 5.1 (2026-09-01), Opus 5.5 (2026-09-22), Sonnet 5.5 (2026-09-28), Haiku 5.5 (2026-10-07). All four share a 1M context window, 128K max output, and a June 2026 reliable knowledge cutoff. Opus 5.5 is the Claude Code default on every Anthropic-hosted plan and the recommended starting model for most workloads ("For most workloads, start with Claude Opus 5.5" — Fable 5.1 what's-new). The effort default moved to `medium` on the three 5.5 models in both the API (Opus 5.5 only) and Claude Code (all three). Thinking cannot be disabled on Opus 5.5, Sonnet 5.5, or Fable 5.1; Haiku 5.5 still accepts `disabled` at `high` or below. Forced tool use (`tool_choice: any|tool`) is rejected on all four. Haiku 5.5 is the first 1M-context, effort-capable Haiku and is positioned as a subagent model. Prices fell: Opus 5.5 $4/$20 (from $5/$25), Sonnet 5.5 cache reads halved, Fable 5.1 cache reads quartered.

### Current models

| | Fable 5.1 | Opus 5.5 | Sonnet 5.5 | Haiku 5.5 |
|---|---|---|---|---|
| API ID | `claude-fable-5-1` | `claude-opus-5-5` | `claude-sonnet-5-5` | `claude-haiku-5-5` |
| Released | 2026-09-01 | 2026-09-22 | 2026-09-28 | 2026-10-07 |
| Positioning (Anthropic) | demanding reasoning and long-horizon agentic work | long-running agentic coding and knowledge work | best combination of speed and intelligence | high-volume, latency-sensitive: classification, extraction, routing, subagent tasks |
| Input / output $/MTok | $10 / $50 | $4 / $20 | $2 / $10 | $0.10 / $0.50 (≤100K prompt); $0.50 / $2.50 (>100K) |
| Cache read $/MTok | $0.25 (0.025× base) | $0.20 (0.05×) | $0.10 (0.05×) | $0.01 / $0.05 by band |
| Context / max output | 1M / 128K | 1M / 128K | 1M / 128K | 1M / 128K |
| Reliable cutoff | Jun 2026 | Jun 2026 | Jun 2026 | Jun 2026 |
| Thinking | adaptive, always on | adaptive, always on | adaptive; `between_tools` is the floor (`disabled` → 400) | adaptive on by default; `disabled` allowed at ≤`high` |
| API default effort | `high` | `medium` | `high` | `medium` |
| Claude Code default effort | `high` | `medium` | `medium` | `medium` |
| Effort ladder | low · medium · high · xhigh · max | same | same | same |
| Tokenizer | same as Fable 5 (Opus 4.7-era; ~30% more tokens than pre-4.7) | — | same as Sonnet 5 | Opus 4.7-era; ~30% more tokens than Haiku 4.5 |
| Min cacheable prompt | 512 | 512 | 512 (Sonnet 5 was 1,024) | 512 (Haiku 4.5 was 4,096) |
| Tentative retirement | not sooner than 2027-09-01 | not sooner than 2027-09-22 | not sooner than 2027-09-28 | not sooner than 2027-10-07 |

Sources: models overview, per-model what's-new pages, pricing, model deprecations (all platform.claude.com/docs — see Sources below).

**Mythos 5.1** (`claude-mythos-5-1`) shares the Fable 5.1 model with looser safeguards; verified-organization access only. Out of scope for Skill calibration.

### Still-active prior generation (fallback / legacy posture)

| Model | State | Role in this landscape |
|---|---|---|
| Opus 5 (`claude-opus-5`) | Active, retirement not sooner than 2027-07-24 | Permitted fallback target for Fable 5.1. Reads/writes thinking blocks compatible with Opus 5.5. |
| Sonnet 5 (`claude-sonnet-5`) | Active, not sooner than 2027-06-30 | Server-side fallback target for Sonnet 5.5 `cyber`/`frontier_llm` declines. |
| Fable 5 (`claude-fable-5`) | Active, not sooner than 2027-06-09 | Superseded; `fable` alias resolves to Fable 5.1 except in Claude apps gateway sessions. |
| Opus 4.8 (`claude-opus-4-8`) | Active, not sooner than 2027-05-28 | Permitted fallback target for Fable 5.1. Rejected as an advisor for Sonnet 5.5 executors. |
| Sonnet 4.6 (`claude-sonnet-4-6`) | Active, not sooner than 2027-02-17 | Legacy; effort ladder lacks `xhigh`; 1M only via `[1m]`. |
| Haiku 4.5 (`claude-haiku-4-5-20251001`) | Active, not sooner than **2026-10-15** | Earliest retirement in the active set. Still the `haiku` alias on Bedrock / Agent Platform / Foundry / Claude Platform on AWS. |
| Sonnet 4.5 | **Deprecated 2026-09-30, retires 2026-11-30** | Replacement: `claude-sonnet-5-5`. Still the Foundry default model in Claude Code. |

### Calibration scope (accepted as catalog decision D2, 2026-10-22)

**Dual-primary: Opus 5.5 + Sonnet 5.5.** Opus 5.5 is the CC default on every Anthropic-hosted plan and the API's recommended starting point; Sonnet 5.5 is the cost-optimal agentic tier with the same 1M/128K envelope. **Fable 5.1 integrated-aware** (not default anywhere; reserve for long-horizon work where Opus 5.5 at higher effort still fails evals). **Haiku 5.5 subagent-aware** — the first Haiku that fits the Scout/Researcher roles with effort control and a 1M window. **Opus 5 / Sonnet 5 fallback-graceful** (the models users are silently served on classifier-flagged requests). **Sonnet 4.6 and Haiku 4.5 legacy-graceful** until their retirement dates; Haiku 4.5 drops out of scope on 2026-10-15 and the catalog should not carry a Haiku 4.5 line past that date.

This replaces the v4.0 scope sentence ("Opus 5 + Sonnet 5 dual-primary, Fable 5 integrated-aware, Opus 4.8 fallback-graceful, Sonnet 4.6 legacy-graceful, Haiku 4.5 graceful-with-extended-thinking"). The three-tier structure (Model-compatible / Sonnet-graceful / High-effort recommended) is landscape-independent and survives unchanged; only the model column refreshes.

### Breaking API changes that touch Skill content

1. **Thinking cannot be disabled** on Opus 5.5, Sonnet 5.5, Fable 5.1 (`disabled` and `enabled`+`budget_tokens` → 400). Sonnet 5.5 offers `between_tools` as the floor (≤`high` only). Haiku 5.5 accepts `disabled` at ≤`high`. Claude Code: "You can't turn thinking off on Opus 5.5, Sonnet 5.5, Haiku 5.5, or the Fable models"; `MAX_THINKING_TOKENS=0` no longer applies to them.
2. **Forced tool use removed** — `tool_choice: {"type":"any"}` / `{"type":"tool"}` → 400 on all four. Replacement: `auto` + `strict: true`, or structured outputs, or state in the prompt when the tool applies. Rationale (Fable 5.1 what's-new): forced calls skip thinking and the model "would write its working-out into the tool arguments instead."
3. **Thinking blocks are model- and conversation-bound.** Opus 5.5 reads Opus 5 and (API/Google Cloud) Sonnet 5.5 / Haiku 5.5 blocks, not Fable/Mythos; Sonnet 5.5 does not read Opus 5 / Opus 5.5 blocks. Accounts created ≥ 2026-08-31 get prefix-change enforcement by default (editing `system`, `tools`, or earlier turns after a thinking block → 400). Keep conversations append-only; use mid-conversation system messages and turn-scoped system messages (`clear_at: "next_user_message"`, beta) instead of editing history.
4. **`computer_20251124` rejected** on API and Google Cloud → `computer_toolset_20260801` (Bedrock still accepts the old type).
5. **`reasoning_extraction` is a refusal category** on all four: prompts that ask the model to reproduce its internal reasoning in response text may be declined. "A short explanation of the answer or a summary of actions taken is still fine." Read reasoning from `display: "summarized"` thinking blocks instead.
6. **Refusal billing changed 2026-09-24:** a refusal before any output is billed in low-false-positive categories. Server-side fallback: Opus 5.5 `fallbacks: "default"` (beta); Sonnet 5.5 retries `cyber`/`frontier_llm` on Sonnet 5 only; **Haiku 5.5 has no server-side fallback**; Fable 5.1 fallback targets are Opus 4.8 and Opus 5.
7. **Text between tool calls now arrives in `thinking` blocks** (progress-update blocks), empty under the default `display: "omitted"`. API clients that render only `text` go silent between tool calls. Set `thinking.display` to `"updates"` (beta) or `"summarized"`.
8. Haiku 5.5 additionally rejects `temperature`/`top_p`/`top_k`, assistant prefill, `budget_tokens`, and `computer_20250124`; it retains thinking blocks from all earlier turns (Haiku 4.5 kept only the latest). Fable 5.1 rejects prefill and sampling params as Fable 5 did.
9. **Advisor tool pairings:** the advisor must be at least as capable as the executor. Sonnet 5.5 executor rejects Opus 4.8, Opus 4.7, Sonnet 5, and Haiku 5.5 advisors.
10. **New betas relevant to agent design:** per-message effort (`mid-conversation-output-config-2026-07-01`), turn-scoped system messages (`mid-conversation-system-clear-at-2026-08-21`), progress-update display (`thinking-display-updates-2026-08-18`), compact on demand (`compact-2026-09-04`), inline tool definitions (`inline-tools-2026-09-15`), thinking-binding controls (`thinking-binding-controls-2026-08-01`), task budgets, fast mode (`speed: "fast"`, Opus 5.5).

### Claude Code facts (verified against code.claude.com/docs, 2026-10-22)

- **Default model:** Opus 5.5 on Pro, Max, Team, Enterprise, and Anthropic API; also on Claude Platform on AWS, Bedrock, Google Cloud Agent Platform. Microsoft Foundry defaults to Sonnet 4.5. "Fable models are not the account-type default on any plan or provider."
- **Alias resolution (Anthropic API):** `opus` → Opus 5.5, `sonnet` → Sonnet 5.5, `haiku` → Haiku 5.5, `fable` → Fable 5.1 (Fable 5 in Claude apps gateway sessions), `best` → `fable` where available else `opus`. Third-party providers lag: Bedrock/Agent Platform `sonnet` → Sonnet 4.5, `haiku` → Haiku 4.5.
- **Minimum Claude Code versions:** Fable 5.1 v2.1.257+, Opus 5.5 v2.1.280+, Sonnet 5.5 v2.1.284+, Haiku 5.5 v2.1.293+. Current changelog tip observed: 2.1.308.
- **Default effort:** `high` on every effort-capable model except Opus 5.5 / Sonnet 5.5 / Haiku 5.5 (`medium`) and Opus 4.7 (`xhigh`). Resolution order: `CLAUDE_CODE_EFFORT_LEVEL` / `--effort` / `/effort` → `modelSettings` per-model or `effortLevel` → model default. Doc states "Opus 5.5 ignores a top-level `effortLevel` in user settings, which applies to Opus 5 and earlier models" — *verify on the running version before relying on it*; use per-model `modelSettings`.
- **Opus 5.5 at `medium` "matches or exceeds Opus 5 at `high` on coding and knowledge-work evaluations"** — "When you move from Opus 5 to Opus 5.5, start at `medium`."
- **Thinking:** cannot be turned off on the 5.5 trio or Fable; `ultrathink` requests deeper reasoning for one turn.
- **Ultracode:** a session setting, not an effort level; `/effort ultracode` and `/effort ultracode off` (v2.1.284+); `"ultracode": true` in settings; exempts the session from the concurrent-subagent limit; unavailable when workflows are off or the model lacks `xhigh`.
- **Subagents:** model resolution order (v2.1.251+): per-invocation `model` → definition `model` frontmatter (`inherit` selects main) → `CLAUDE_CODE_SUBAGENT_MODEL` → main conversation's model. `CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1` (v2.1.257+) overrides all. **`CLAUDE_CODE_WORKFLOW_SUBAGENT_MODEL`** (v2.1.296) runs every workflow agent on one model. **Agent tool `effort` parameter** (v2.1.292) sets a sub-agent's effort per invocation. Built-in Explore inherits the main model; when main runs Fable, Explore runs on the `opus` alias (Anthropic-hosted only). Concurrent-subagent limit 20 (`CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`, v2.1.217+); nesting depth 3 (`CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`, `1` turns nesting off); fork mode on by default (`CLAUDE_CODE_FORK_SUBAGENT=0` to disable); `maxTurns` returns partial output (v2.1.246+); `CLAUDE_CODE_DISABLE_EXPLORE_PLAN_AGENTS=1` (v2.1.198+).
- **1M context** is the default (no `[1m]` suffix) on Fable, Sonnet 5+, Haiku 5.5, Opus 4.7+. `CLAUDE_CODE_DISABLE_1M_CONTEXT=1` reverts to 200K. Haiku 5.5 bills a higher band above 100K prompt tokens.
- **Other 2.1.29x additions worth noting for CC design:** `CLAUDE_CODE_RETRY_WATCHDOG*` unattended retry mode; `CLAUDE_CODE_AUTO_COMPACT_WINDOW` accepts `k`/`M`; idle compaction (`CLAUDE_CODE_IDLE_COMPACT_MIN_TOKENS`, v2.1.290+); `/advisor`; `/ultrareview`; agent teams; Workflow tool / dynamic workflows (`CLAUDE_CODE_DISABLE_WORKFLOWS` still referenced by the Skill — verify the name on the running version).

Every `CLAUDE_CODE_*` name and default above is a dated product fact. Carry the "verify against the running Claude Code version" marker into any generated design (CC_EG §6 rule).

### Open items — do not assert

- ZDR and data-retention posture for the 5.5 generation: not re-verified this cycle. The 2026-07 block's Fable 5 "Covered Model, no ZDR" fact is not carried forward to Fable 5.1 without verification.

- Opus 5.5 tokenizer vs Opus 5: not stated on any fetched page. Treat as "same family as Sonnet 5.5 / Fable 5.1 (Opus 4.7-era)" only after `count_tokens` confirmation.
- Claude.ai plan defaults (which model Free/Pro/Max serve by default in chat): not fetched; the Claude Code defaults above are verified, chat defaults are not.
- Whether `CLAUDE_CODE_DISABLE_WORKFLOWS` is still the workflow kill switch name on 2.1.30x.
- Claude Code default *model* on Max vs Pro beyond "Opus 5.5" (e.g., whether Pro has usage-credit gating on Opus 5.5): not stated on the fetched page.
- Behavioral re-baselining of the 15-tendency deployment-conditioning tables on the 5.5 generation is analytical (D9c) from Anthropic's guides, not measured. Calibration Lab re-baselining remains open (carried from v4.0).

### Sources

- https://platform.claude.com/docs/en/about-claude/models/overview
- https://platform.claude.com/docs/en/about-claude/model-deprecations
- https://platform.claude.com/docs/en/models/opus-5-5/whats-new-opus-5-5
- https://platform.claude.com/docs/en/models/sonnet-5-5/whats-new-sonnet-5-5
- https://platform.claude.com/docs/en/models/haiku-5-5/whats-new-haiku-5-5
- https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1
- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5
- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5
- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-haiku-5-5
- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1
- https://code.claude.com/docs/en/model-config
- https://code.claude.com/docs/en/sub-agents
- https://code.claude.com/docs/en/changelog (entries 2.1.292–2.1.308)
- Secondary (dates and pricing cross-check only): TechCrunch 2026-09-22 (Opus 5.5), VentureBeat 2026-09-01 (Fable 5.1), powerdrill.ai (Sonnet 5.5 / Haiku 5.5 dates).

### Refusal-aware prompt design (landscape-independent)

A refusal returns HTTP 200 with `stop_reason: "refusal"` and a category, so it behaves differently from an error. Four practices hold across generations:
- **Do not ask for reproduced reasoning.** Instructions to "show your work" or "reproduce your reasoning" in the visible response can be declined as `reasoning_extraction` on all four current models. Read reasoning from `display: "summarized"` thinking blocks; a short explanation of the answer or a summary of actions taken is still fine.
- **Instrument refusals as their own signal.** Monitoring built on error rates or 5xx responses never sees an HTTP-200 refusal. Emit one event per refusal and one per fallback-served response, and alert on the gap between the two counts.
- **Budget retries per request, not per turn or per session.** A single turn can produce several refusals — an agent plus its sub-agents.
- **Give sub-agent calls their own fallback.** On the Opus 5 generation the `fallbacks` parameter did not propagate into model calls made from inside tool execution `[verified 2026-07; re-verify for the 5.5 generation]`. Per-model server-side fallback for the current generation is in the breaking-changes list above — note that Haiku 5.5 has none.

---

## 4. Reasoning and Thinking

### Adaptive Thinking (current generation)

All four current models use adaptive thinking: the model decides when and how much to think on each turn, and the `effort` parameter controls thinking depth. Thinking cannot be disabled on Opus 5.5, Sonnet 5.5, or Fable 5.1 — `disabled`, and `enabled` with `budget_tokens`, return 400; Sonnet 5.5 offers `between_tools` as its floor at `high` or below. Haiku 5.5 runs adaptive thinking by default and accepts `disabled` at `high` or below. Section 3 has the per-model table.

**The effort parameter** (full ladder on all four current models):
- **`low`** — minimal thinking, fastest responses. A legitimate primary cost/latency control where evals show quality holds; early turn termination (#15) and tool under-triggering (#7b) rise here.
- **`medium`** — moderate thinking. The Claude Code default on Opus 5.5, Sonnet 5.5, and Haiku 5.5, and the API default on Opus 5.5 and Haiku 5.5. Anthropic reports Opus 5.5 at `medium` matches or exceeds Opus 5 at `high` on coding and knowledge-work evaluations.
- **`high`** — substantial thinking. The API default on Sonnet 5.5 and Fable 5.1, and the Claude Code default on Fable 5.1. Step here when verification matters or edge cases are likely.
- **`xhigh`** — step up for demanding coding and agentic work, on a measured gain. Sonnet 5.5 at `xhigh`/`max` self-starts review rounds and reviewer subagents (#11, #13); Fable 5.1 may draft a deliverable twice (#3c).
- **`max`** — top tier for the deepest reasoning; use when a task justifies unconstrained spend and the model has room (set a large `max_tokens`).

Effort controls how much the model **thinks**, not how much it **says**. Lowering effort does not reliably shorten the visible response — prompt for response length explicitly (see tendency #3a below). A prompt-level "think less" instruction does not reliably reduce thinking either; lower effort instead.

### Extended Thinking (legacy)

Haiku 4.5 supports only extended thinking via `thinking: {"type": "enabled"}` with a `budget_tokens` cap. No current model needs it, and Haiku 5.5 rejects `budget_tokens`.

### Managing Over-Exploration

Current models are well-calibrated about when exploration adds value, but the tendency persists for complex agentic workflows at `xhigh`/`max`. On Opus 5.5 multi-app workflows the opposite — under-exploration — is documented; see tendency #6 in `root_OPTIMIZATION_REFERENCE.md`. This is search breadth (exploring multiple approaches) — distinct from scope expansion (delivering more than was asked), which is tendency #12.

**Countermeasure — when Claude is doing too much upfront exploration:**
```xml
<efficiency>
Choose an approach and commit to it. Avoid revisiting decisions unless you
encounter new information that directly contradicts your reasoning. If you're
weighing two approaches, pick one and see it through. You can always
course-correct later if the chosen approach fails.
</efficiency>
```

### Interleaved Thinking

Current models support interleaved thinking — reasoning between tool calls, not just at the start. Text the model writes between tool calls now arrives in `thinking` blocks (progress-update blocks), which are empty under the default `display: "omitted"`; a client that renders only `text` goes silent between tool calls, so set `thinking.display` to `"updates"` (beta) or `"summarized"`. This is particularly valuable for agentic workflows where Claude needs to reflect on tool results before deciding what to do next.

**To encourage reflection between steps:**
```xml
<reasoning_approach>
After receiving tool results, carefully reflect on their quality and determine
optimal next steps before proceeding. Use your thinking to plan and iterate
based on this new information, and then take the best next action.
</reasoning_approach>
```

### Reasoning Instructions by Task Type

Generic "think step by step" is better than nothing, but task-specific reasoning instructions are significantly better. With current models' reasoning capabilities, prefer general framing over prescriptive step-by-step plans — the model's reasoning frequently exceeds what a hand-written plan would produce. The blocks below are abbreviated references for quick consultation. For the full, expanded reasoning blocks (18 variants across 6 categories with usage guidance and failure mode notes), consult the `rootnode-reasoning-blocks` Skill.

**For analytical tasks:**
```xml
<reasoning>
1. State the core question explicitly before analyzing.
2. Identify the key assumptions underlying the problem.
3. Test each assumption — which are well-supported and which are fragile?
4. Where evidence is ambiguous, flag it rather than choosing a side silently.
5. Draw conclusions only from what the evidence supports.
</reasoning>
```

**For strategic/planning tasks:**
```xml
<reasoning>
1. Map the stakeholders and their competing interests.
2. Identify the binding constraints (non-negotiable vs. flexible).
3. Generate at least three distinct approaches, not variations of one idea.
4. Evaluate each approach against the constraints explicitly.
5. Recommend the approach with the best constraint satisfaction, and explain what it sacrifices.
</reasoning>
```

**For creative tasks:**
```xml
<reasoning>
1. Explore the possibility space broadly before committing to a direction.
2. Identify the 2-3 most promising directions and articulate why each is interesting.
3. Develop the strongest direction fully.
4. Revisit whether elements from other directions would strengthen the chosen one.
</reasoning>
```

**For technical/debugging tasks:**
```xml
<reasoning>
1. Reproduce the problem statement in your own words to confirm understanding.
2. Identify the most likely failure points.
3. Trace the logic from input to output, checking each step.
4. When you find the issue, verify that your fix doesn't introduce new problems.
</reasoning>
```

---

## 5. Claude's Behavioral Tendencies (And How to Manage Them)

The tendency taxonomy expanded for Opus 5 (v4.0 cycle) and for the 5.5 generation (v5.0 cycle). Verbosity refactored into a three-surface family (#3a/#3b/#3c) with distinct triggers and countermeasures. Four tendencies were added for Opus 5 (#11–#14) and one for the 5.5 generation (#15 early turn termination). Four prompt/environment-conditional defects are treated separately at the end of this section rather than as model tendencies. Total: **15 numbered entries (#1–#15)** with 7 discrete facets (1a/1b under #1; 3a/3b/3c under #3; 7a/7b under #7) + 4 non-tendency defects. `root_OPTIMIZATION_REFERENCE.md` is the canonical taxonomy; this section is the quick-reference copy carrying the most-pasted templates. The 5.5-generation facets on #3c, #4, #5, #6, #7, #11, #12, and #13 — with their verbatim Anthropic blocks — live there.

Deployment context matters. The same tendency manifests differently on the chat interface (Adaptive effort, no CI anchor), in Projects (CI partially anchors), on Claude Code (default `medium` on the 5.5 trio), and on the API (developer-controlled effort). Countermeasure calibration in each tendency entry names the deployment surfaces where it most applies.

### 1. Agreeableness Bias

Two facets.

- **1a — Output-content agreeableness.** Validating user ideas in responses, softening disagreement under follow-up, opening with premise validation. Reduced in Opus 5 but not eliminated.
- **1b — Persistent-preference dilution.** Configured preferences (User Preferences, Project CI rules) drift over long conversations. Configured rules hold for the first several turns then gradually weaken.

**Countermeasure for 1a:**
```xml
<critical_thinking>
If the premise of this request contains errors, flawed assumptions, or
better alternative framings, say so directly before proceeding.
Do not simply execute a flawed request without comment.
</critical_thinking>
```

**Countermeasure for 1b:**
```xml
<persistent_preference_adherence>
Treat User Preferences and Project Custom Instructions as equal-priority
constraints to user messages. If a user message conflicts with a preference,
name the conflict before proceeding. Do not silently drop preferences over a
long conversation. At every turn, the full Preference and CI ruleset applies.
</persistent_preference_adherence>
```

**Deployment calibration:**
- Chat interface (Adaptive): HIGH for 1b, MEDIUM for 1a
- Claude Projects: MEDIUM for 1b, LOW for 1a
- Claude Code: LOW for both
- API (effort ≥ high): LOW for both

### 2. Hedging and Over-Qualification

Hedging on factual claims is well-controlled on Opus 5. It persists on editorial and recommendation framings — language patterns: "it depends," "there are many factors," "this is just one perspective," "it's worth considering."

**Countermeasure (apply selectively to advisory contexts):**
```xml
<constraints>
Be direct and decisive in your recommendations. Where you are confident,
state your position clearly. Reserve caveats for genuinely uncertain areas,
and when you do caveat, be specific about what is uncertain and why.
Do not hedge on well-established facts or best practices.
</constraints>
```

### 3. Verbosity — three-surface family (refactored for Opus 5)

Opus 5's default responses are longer than Opus 4.8 on multiple surfaces. Refactored from a single tendency into three surfaces with different triggers and different countermeasures.

#### 3a. Conversational response length

Default user-facing responses run longer on Opus 5. Effort does not reliably shorten them (effort controls thinking, not visible output length).

**Countermeasure:**
```xml
<tone_preference>
Keep responses focused, brief, and concise. Keep disclaimers and caveats short,
and spend most of the response on the main answer. When asked to explain
something, give a high-level summary unless an in-depth explanation is
specifically requested.
</tone_preference>
```

In a long system prompt, pair the main concision instruction with a short reminder near the end:
```xml
<tone_preference>
Keep outputs reasonably concise.
</tone_preference>
```

#### 3b. Agentic progress narration

Opus 5 narrates readily during agentic work — announcing what it is about to do and giving longer per-message output in agentic sessions than prior models.

**Countermeasure — describe the cadence and shape (positive examples beat prohibitions):**
```xml
<agentic_communication>
Before your first tool call, say in one sentence what you're about to do.
While working, give a brief update only when you find something important
or change direction. When you finish, lead with the outcome: your first
sentence should answer "what happened" or "what did you find," with
supporting detail after it for readers who want it.
</agentic_communication>
```

#### 3c. Written-deliverable length

Files that Opus 5 writes to disk (reports, Markdown documents, summaries) are often longer than on prior models — separate from conversational verbosity.

**Countermeasure — explicit length calibration for authored documents:**
```xml
<document_length>
Match the length of written documents to what the task needs: cover the
substance, but do not pad with filler sections, redundant summaries, or
boilerplate.
</document_length>
```

### 4. List and Bullet Overuse

Claude still defaults to bulleted lists even when prose would be more appropriate. Persists across Opus 4.6 → 4.7 → 4.8 → 5.

**Countermeasure:**
```xml
<format_note>
Write in connected prose paragraphs. Use lists only when the content is
genuinely a set of discrete, parallel items. Do not convert narrative
explanations into bullet points.
</format_note>
```

On Fable 5.1, which formats less by default, this template can over-correct and suppress structure the content needs — use the conditional formulation in `root_OPTIMIZATION_REFERENCE.md` #4 instead.

### 5. Fabricated Precision (External-Fact)

Scope: external-fact fabrication only (statistics, sources, citations). Self-referential fabrication — claims about what the model has done, checked, or loaded — is a distinct failure mode tracked as tendency #10.

External-fact fabrication still occurs in domains with thin training-data coverage or where pressure to produce specific numbers is high. Apply in research, financial, and health contexts.

**Countermeasure:**
```xml
<data_integrity>
Use only data explicitly provided. If you do not have a specific number,
do not estimate one — state what data would be needed. Never invent a
statistic, percentage, or quantitative claim to fill a gap in the
available information.
</data_integrity>
```

### 6. Over-Exploration (search breadth)

Distinct from tendency #12 (scope expansion). This is Claude exploring multiple approaches to a task rather than committing to one. Persists for complex agentic workflows at higher effort settings.

**Countermeasure (apply when over-exploration is observed):**
```xml
<efficiency>
Only make changes that are directly requested or clearly necessary.
Keep solutions simple and focused. Don't add features, refactor code,
or make improvements beyond what was asked.
</efficiency>
```

### 7. Tool Trigger Miscalibration — two facets

**Facet 7a — Tool over-triggering** (mostly reduced in Opus 5). Historically caused by emphatic tool-use language ("MUST", "ALWAYS", "CRITICAL"). Reduced at the model level.

**Countermeasure for 7a — dial back aggressive tool-use language:**
```xml
<tools>
Use the search tool when the question requires current data that may have
changed since your training. For well-established facts and concepts,
answer directly.
</tools>
```

**Facet 7b — Tool under-triggering.** On the chat interface at Adaptive effort, Skills can fail to fire on legitimate triggers because the model weights persistent context (Skill descriptions loaded via progressive disclosure) less heavily than immediate prompts. On the 5.5 generation a second driver is more common: tool-suppressing language carried over from older prompts ("only use tools when strictly necessary") causes under-search. Remove that language before adding enforcement; the search nudge and model-specific steps are in `root_OPTIMIZATION_REFERENCE.md` #7b.

**Countermeasure for 7b — explicit tool-use enforcement:**
```xml
<tool_use_required>
When User Preferences or Project Custom Instructions specify a tool that
should be used for a category of request, treat that specification as a hard
requirement, not a suggestion. Invoke the tool before responding. Do not
substitute general reasoning for the specified tool unless the tool is
unavailable in the current environment.
</tool_use_required>
```

### 8. LaTeX Defaulting

Opus defaults to LaTeX notation for mathematical expressions. Persists in Opus 5. Appropriate for academic/technical contexts; problematic for plain-text outputs or non-technical audiences.

**Countermeasure — when you need plain text math:**
```xml
<format_note>
Format all mathematical expressions in plain text. Do not use LaTeX,
MathJax, or markup notation such as \( \), $, or \frac{}{}.
Write math expressions using standard text characters (/ for division,
* for multiplication, ^ for exponents).
</format_note>
```

### 9. Editorial Drift

Unsolicited commentary on the model's own boundaries, the act of responding, or its constraints. Symptoms: meta-statements about what the model can or cannot do that were not asked for; disclaimers about response scope inserted into otherwise direct answers; preamble explaining approach; closing commentary about what the user might want to consider next.

Most pronounced on the chat interface where Adaptive effort and the absence of tight CI scaffolding allow editorial content to leak.

**Countermeasure:**
```xml
<no_editorial_drift>
Do not add unsolicited commentary about your own boundaries, what you will
or won't do, or how you are approaching the response. Do not preamble with
explanations of your reasoning approach unless asked. Do not close with
suggestions about what the user might want next unless asked. Answer the
question; stop when the answer is complete.
</no_editorial_drift>
```

### 10. Self-Referential Fabrication

Claims to have performed an action, checked a state, or inspected runtime context without actually doing so. Distinct from external-fact fabrication (#5): #5 is about content; #10 is about process.

Symptom profile:
- "I searched and found X" when no search was performed
- "I checked the Memory and confirmed Y" when Memory was not consulted
- "I loaded the file and see Q" when the file was not loaded
- Process claims appearing in support of conclusions already stated

Asymmetric pattern: fabrication appears in initial responses; honest correction appears under direct challenge.

**Countermeasure:**
```xml
<verification_of_self_referential_claims>
Before asserting that an action has been performed or that a state has been
verified, confirm the action's observable effect. If the effect cannot be
confirmed from the available evidence, state that the action's status is
unknown rather than asserting completion.

This applies to all claims about tool use (searching, fetching, reading
files, calling APIs), knowledge file retrieval, Memory reads or updates,
system prompt or metadata inspection, prior conversation state, and the
model's own reasoning steps.

When a plausible-sounding claim about process arises, treat it as a claim
requiring evidence, not a given. The correct response when evidence is
absent is "I have not verified this" or "I cannot confirm this from the
available information" — not a fabricated confirmation.

Under no circumstances should the model invent process details to support a
conclusion already reached. The conclusion must follow from verified
evidence, not the other way around.
</verification_of_self_referential_claims>
```

For Skills and Projects that report on actions taken (audit Skills, memory-optimization Skills, context-budget Skills), this countermeasure is essentially universal — those Skills are structurally exposed to the failure mode regardless of deployment context.

### 11. Over-Verification (NEW in Opus 5)

Opus 5 verifies its own work automatically. Instructions telling it to "double-check your answer," "re-verify before responding," "include a final verification step," or "use a subagent to verify" compound with the model's own behavior and cause over-verification — token spend without a quality gain.

**Countermeasure — remove self-directed re-checking instructions.** This is a new countermeasure shape: the fix is *removal of instructions*, not addition of instructions.

Distinguish self-directed re-checking (remove) from external-artifact verification (keep). External-artifact verification asks the model to check a claim against a source outside its own output — read the file, run the diff, execute the test, inspect the rendered page, confirm the tag resolves. That is evidence grounding, not self-re-checking, and Opus 5 does not automatically do it (it needs to be told to). Keep those instructions and keep them imperative.

**Remove:**
- "double-check your answer"
- "re-verify before responding"
- "include a final verification step"
- "use a subagent to verify your work"

**Keep (evidence-grounding, external-artifact):**
- "verify the file exists"
- "check the rendered page"
- "confirm the tag resolves against the actual repo state"
- "diff the artifact against the source"

### 12. Scope Expansion (NEW in Opus 5)

Opus 5 expands the scope of a task, adding steps that weren't requested or applying its own judgment about what the task should be. This is deliverable-boundary drift — distinct from tendency #6 over-exploration (which is search breadth within a defined task).

**Countermeasure — constrain scope explicitly:**
```xml
<scope>
Deliver what was asked, at the scope intended. Make routine judgment calls
yourself, and check in only when different readings of the request would
lead to materially different work. If the request seems mistaken or a better
approach exists, say so in a sentence and continue with the task as asked
rather than quietly narrowing, widening, or transforming it. Finish the
whole task, and stop short of actions that are clearly beyond what was asked.
</scope>
```

### 13. Subagent Over-Delegation (NEW in Opus 5)

Opus 5 delegates to subagents more readily than prior models. Delegation pays off on genuinely independent, sizeable tracks of work but multiplies cost and time when applied to small tasks.

**Countermeasure — cap delegation:**
```xml
<subagent_delegation>
Delegate to a subagent only for large tasks that are genuinely independent
and parallelizable, such as a wide multi-file investigation. Do not delegate
work you can finish yourself in a handful of tool calls, and do not use
subagents to verify or double-check your own work. If one subagent can
complete the task, use one rather than several, and keep spawn counts low.
</subagent_delegation>
```

### 14. Correction Narration (NEW in Opus 5)

Opus 5 narrates corrections to its earlier statements more than prior models — including corrections that don't materially change the user's outcome.

**Countermeasure — restrict corrections to material ones:**
```xml
<correction_policy>
Only correct an earlier statement when the error would change the user's
code, conclusions, or decisions. State corrections plainly and briefly, then
continue the task. For slips that change nothing for the user, make the fix
and move on without noting it.
</correction_policy>
```

### 15. Early Turn Termination (NEW in the 5.5 generation)

The model ends its turn while work it was asked for is still owed: a summary that closes by announcing the next step with no tool call, an offer to continue, a list of decisions none of which blocks the remaining work, or a report because a milestone is done. At low effort it pauses to confirm a plan or asks a question it could answer itself. It is the opposite of #12 (too little, not too much), documented with countermeasures in all four 5.5-generation prompting guides. It rises as effort falls: MEDIUM on Claude Code at the `medium` default, HIGH at `low`, and HIGH in unattended runs.

**Countermeasure — first lever is effort.** At `low`/`medium`, raise effort before adding a block. Then the default block `[Anthropic docs — Sonnet 5.5 guide, fetched 2026-10-22]`, both paragraphs — the second is the #12 countermeasure, and a prompt that only says "keep working" invites scope expansion. A turn-boundary instruction, not self-verification (AEA §4.14):
```text
Keep working until everything the user asked for is done, and only stop to ask when you can't go on without the user or before a risky step.

When the work the user asked for is done and checked, stop and report. Don't add features, tests, files, docs or refactors that weren't asked for. If you think one would help, mention it at the end instead of doing it.
```

For fully unattended loops, the Opus 5.5 guide's long "standing instruction" variant and the harness continuation rule (treat a text-only end of turn as a report, cap continuations at two or three) are in `root_OPTIMIZATION_REFERENCE.md` #15.

### Prompt/environment-conditional defects (not model tendencies)

Four failure modes track cleanly to the prompt, the harness, or the runtime configuration rather than the model. They are handled by writing prompts differently or configuring the API or harness differently, not by adding counter-tendency instructions.

#### Conservative-instruction literalism

Opus 5 follows "only report high-severity issues" or "be conservative" literally, which causes under-reporting. This is a **prompt defect** exposed by the model, not a model tendency.

**Fix — ask for everything, filter in a separate pass.** Rewrite review prompts to two stages: (1) report every issue found; (2) filter to the severity level or subset the user wants. Do not compress "report everything" and "filter to high severity" into one instruction.

Sweep pattern for audit and review Skills: `only report`, `only flag`, `be conservative`, `high-severity` — replace with report-everything-then-filter form.

#### Thinking-disabled output artifacts (narrowed for the 5.5 generation)

Thinking cannot be disabled on Opus 5.5, Sonnet 5.5, or Fable 5.1, so on the current generation this defect is documented only on Haiku 5.5 at `low` or with thinking off, and on Sonnet 5.5 at `between_tools` when a "don't think" instruction is left in the prompt. There, reasoning leaks into visible text; on the Opus 5 generation, `thinking: {"type": "disabled"}` produced two further artifacts:

- **Tool calls as text.** The model writes a tool call into user-facing text instead of emitting a structured `tool_use` block. The call never runs; in agentic loops the leaked text stays in the conversation history and affects later turns. Most common on tool-heavy workloads such as search.
- **Internal XML tags in visible response.** `<thinking>` tags or other internal tags leak into the visible response.

Both are **API-configuration failure modes** — the fix is not to prompt around them but to keep thinking on and control cost via effort. For most tasks, thinking-on at `low` effort outperforms thinking-off at similar cost.

**Sub-finding — a system-prompt rule against thinking increases tag leakage.** Do NOT add instructions like "do not think" or "do not reason" to a system prompt while thinking is disabled — that instruction increases tag leakage rather than suppressing it. If a mitigation instruction is required (for integrations that must keep thinking disabled), use the general form rather than naming the tags:

```xml
<output_hygiene>
When you use a tool, you may say a brief sentence first. If no tool can
express what the user asked for, say so instead of guessing. Do not include
internal or system XML tags in your response.
</output_hygiene>
```

#### Mid-turn user text misread as injection (NEW in the 5.5 generation)

Sonnet 5.5 and Haiku 5.5 treat user text placed inside `tool_result` blocks, per-step harness notices, and token countdowns as possible prompt injection, and may ignore them. A harness fix, not a prompt fix: deliver the user's words as a text block after the last `tool_result`, keep harness notices in a separate mid-conversation system message, and add no countdowns in interactive sessions. Detail in `root_OPTIMIZATION_REFERENCE.md`.

#### Reasoning-extraction refusal (NEW in the 5.5 generation)

Prompts that ask the model to reproduce its internal reasoning in the response can be declined — `stop_reason: "refusal"`, category `reasoning_extraction` — on all four current models. Remove those instructions, ask for a short explanation or a summary of actions taken, and read the reasoning itself from `display: "summarized"` thinking blocks.

---

## 6. Few-Shot Examples: The Quality Multiplier

Providing 1-3 examples of desired input/output pairs is one of the most reliable ways to improve Claude's output. Examples communicate what instructions alone cannot.

### Effective Example Structure

```xml
<examples>
  <example>
    <input>Analyze the competitive position of a mid-size SaaS company entering the CRM market.</input>
    <ideal_output>
      The CRM market is dominated by Salesforce (33% share), with HubSpot and
      Microsoft Dynamics as strong secondary players. A mid-size entrant faces
      three structural challenges...

      [show the depth, tone, structure, and specificity you want]
    </ideal_output>
  </example>

  <example>
    <input>Analyze the competitive position of a regional bank launching a digital wallet.</input>
    <ideal_output>
      Digital wallets are a consolidating market where Apple Pay and Google Pay
      control consumer mindshare. A regional bank's advantages are...

      [second example reinforces the pattern]
    </ideal_output>
  </example>
</examples>
```

### What Examples Communicate Best

- **Depth and specificity level** — more powerful than saying "be detailed"
- **Tone and register** — more reliable than describing the tone
- **Structure and formatting** — shows rather than tells
- **What to include and exclude** — implicit boundaries

### Examples with Thinking

When using adaptive thinking, you can include `<thinking>` tags inside your few-shot examples to demonstrate the reasoning pattern you want. Claude will generalize that style to its own thinking blocks.

---

## 7. Claude Projects: How Claude Processes Project Structure

This section covers how Claude interprets and responds to the structural elements of a Project — the optimization principles that govern system prompt layout, knowledge file design, and context management. For the full framework on how to design and architect Claude Projects, see the Project Architecture Guide (`root_PROJECT_ARCHITECTURE_GUIDE.md`).

### Knowledge Files: What Claude Attends To

- **One concept per file.** Claude uses the file boundary as a semantic signal. Unrelated content in the same file creates ambiguity about which context applies to which task. Separate files produce cleaner retrieval.
- **Name files descriptively.** Claude uses filenames as context signals when deciding what information is relevant. `root_OPTIMIZATION_REFERENCE.md` communicates more than `notes2.md`.
- **Front-load the most important content.** Even in long files, Claude attends most strongly to the first few paragraphs. Put the highest-value content — definitions, key principles, critical rules — at the top.
- **Use the system prompt for instructions; use knowledge files for reference.** Claude processes the Custom Instructions as behavioral directives — rules to follow. Knowledge files are treated as reference material — information to draw from. When behavioral rules are buried in knowledge files, Claude may treat them as optional context rather than binding instructions.

### System Prompt Structure for Projects

The same primacy-recency principle from Section 2 applies to system prompts. Place identity and hard constraints at the top (where Claude attends first), and output standards and quality checks at the bottom (closest to generation). The middle carries context, knowledge file references, and operational details.

**Note on emphasis language across models:** Instructions that needed emphasis in pre-4.6 models (capitalization, repetition, "CRITICAL" prefixes) should be written in normal-weight language on current models to avoid over-compliance. The exception is when overriding tendency 1b or 7b in chat-interface contexts where preference dilution and tool under-triggering are observed.

```xml
<identity>
[Who Claude is in this Project — role, expertise, perspective]
</identity>

<core_instructions>
[The non-negotiable rules that apply to every interaction in this Project]
</core_instructions>

<knowledge_file_guide>
[Brief description of each knowledge file and when to reference it —
this gives Claude a decision rule for which file to consult, not just an inventory]
</knowledge_file_guide>

<default_behavior>
[How Claude should behave when no specific instruction applies —
default tone, format, length, level of detail]
</default_behavior>

<output_standards>
[Quality standards that apply to all outputs from this Project]
</output_standards>
```

### RAG and Context in Projects

Anthropic Projects use **automatic RAG activation** when the uploaded knowledge base approaches or exceeds the model's context window. There is no fixed token threshold — the trigger is tied to the current model's window capacity. When knowledge stays below the limit, Claude loads all project content into context normally; when knowledge approaches or exceeds the limit, Claude retrieves only the most relevant chunks per query.

This is a change from the earlier fixed-threshold framing (a ~66,500-token cutoff measured under a 200K-era platform against Opus 4.6). Under the current landscape — where all four current models have 1M-token windows — the RAG threshold has moved with the window and is no longer a small-fixed-number that a Project sits comfortably below.

**Preserved distinction:** a model's context window is **not** the Projects RAG threshold. They were numerically entangled under the 200K era, which made the fixed 66,500 figure look like a stable rule of thumb. Under 1M-window models, the RAG threshold *tracks* the window rather than being a fraction of it, but they remain conceptually distinct. State them separately in prompt/Project design.

See `root_OPTIMIZATION_REFERENCE.md` (context-budget section) and the `rootnode-context-budget` Skill for the current tier bands and Project-sizing math.

### Context Management in Long Sessions

Fable 5, Opus 5, and Sonnet 5 all have context awareness — the ability to track remaining context window capacity during a conversation. For Projects used in extended sessions:

**Compaction:** The Compaction API provides automatic context summarization when conversations approach the context window limit. If your Project uses an agent harness or workflow that supports compaction, inform Claude so it doesn't prematurely wrap up work:

```xml
<context_management>
Your context window will be automatically compacted as it approaches its
limit, allowing you to continue working indefinitely. Do not stop tasks
early due to context concerns. If approaching the limit, save your
current progress and state before the context refreshes.
</context_management>
```

**Memory across sessions:** The memory tool allows Claude to persist information between context windows and sessions. For Projects that span multiple conversations, this enables continuity without manual re-briefing.

### Variable Inputs with XML Tags

For reusable prompts, use clearly marked variable slots:

```xml
<instructions>
Analyze the following company for acquisition suitability.
</instructions>

<input>
  <company_name>{{COMPANY_NAME}}</company_name>
  <industry>{{INDUSTRY}}</industry>
  <annual_revenue>{{REVENUE}}</annual_revenue>
  <key_question>{{SPECIFIC_QUESTION}}</key_question>
</input>
```

This separates the reusable prompt architecture from the variable content, making prompts genuinely modular.

---

## 8. Controlling Output Quality

### Avoid Over-Engineering

Match prompt complexity to task complexity. Current models follow instructions precisely, which means over-specified prompts produce rigid, over-engineered outputs rather than being smoothed over.

**Principle:** Only make changes that are directly requested or clearly necessary. Don't add features, documentation, error handling, or abstractions for scenarios that aren't part of the current task. The right amount of complexity is the minimum needed.

### External-Artifact Verification (not self-re-checking)

Adding a **self-directed re-checking** instruction — "before presenting your final answer, verify your reasoning" — is counterproductive on Opus 5 (see tendency #11). Opus 5 already re-checks its own work automatically, and the instruction compounds the behavior into over-verification without a quality gain.

Adding an **external-artifact verification** instruction — one that asks the model to check its claims against a source outside its own output — remains valuable, because Opus 5 does not automatically do this. Keep these instructions and keep them imperative.

**Example — external-artifact verification for a research task:**
```xml
<verification>
Before presenting the final answer, verify each factual claim against the
provided sources. For every quantitative claim, cite the source passage the
number came from. If a claim cannot be grounded in the provided sources,
flag it explicitly rather than including it in the final answer.
</verification>
```

The instruction above asks the model to consult external evidence (the sources), not to re-examine its own output. That distinction is the difference between the D4 keep-list and the D4 remove-list.

### Assumption Surfacing

Claude often makes silent assumptions that shape the entire output. Force them into the open:

```xml
<instructions>
Before beginning your analysis, explicitly state the 3-5 key assumptions
you are making. Then proceed with the analysis. At the end, revisit
whether different assumptions would change your conclusions.
</instructions>
```

### Anti-Patterns to Avoid

| Anti-Pattern | Why It Fails | Better Alternative |
|---|---|---|
| "Be creative" | Too vague to act on | Provide an example of the creative style you want |
| "Think carefully" | No structure for careful thinking | Specify the reasoning steps, or set effort explicitly |
| "Be concise but thorough" | Contradictory without boundaries | "Limit to 500 words. Prioritize X over Y." |
| "Consider all perspectives" | Produces unfocused output | "Compare perspective A vs. perspective B on dimension X" |
| "Do your best" | No signal at all | Specify quality criteria |
| "ALWAYS use [tool]" | Causes over-triggering; on Haiku 5.5 a blanket search instruction searched on about half the prompts that needed none, with no accuracy gain | "Use [tool] when it would enhance your understanding" — and on the 5.5 generation, remove tool-suppressing language rather than adding blanket triggers (tendency 7b) |
| "Think carefully before answering" | Effort is the control; the line compounds thinking (tendency #11) | Remove it and set effort |
| "Show your reasoning in the response" | Can be declined as `reasoning_extraction` on all four current models | Ask for a short explanation; read summarized thinking blocks |
| "Double-check your answer before responding" | Compounds Opus 5's automatic self-verification (tendency #11); wasted tokens | Remove. If external verification is needed, phrase it as evidence grounding: "verify each claim against the provided sources." |
| "Only report high-severity issues" | Opus 5 follows literally and under-reports | "Report every issue you find, then filter to high severity in a separate pass." |

---

## 9. Multi-Turn Conversation Management

### Context Window Awareness

Fable 5, Opus 5, and Sonnet 5 can track their remaining context window during a conversation. For agent workflows and long sessions, Claude can manage its own context budget — but it may also try to wrap up work prematurely when it senses the window is filling. The compaction API (see Section 7) addresses this for applications that support it.

For applications without compaction, earlier messages get pushed further from Claude's active attention as conversations grow. For critical information:

- **Restate important context** when starting a new phase of work.
- **Summarize decisions made so far** before asking for the next step.
- **Don't assume Claude remembers** details from 10+ messages ago without reinforcement.

This is particularly important for chat-interface deployments where tendency 1b (persistent-preference dilution) compounds the natural attention decay over long conversations.

### Conversation Steering

When a conversation goes off track, direct correction works better than hints:

- **Weak:** "Could you maybe focus a bit more on the technical aspects?"
- **Strong:** "Stop. Restart this section. Focus exclusively on the technical architecture. Do not discuss business strategy."

Claude responds well to clear, direct course corrections. You don't need to be polite about steering — clarity is what matters.

### Multi-Context-Window Workflows

For tasks that span multiple context windows (common in agent and coding workflows):

- **Use the first window for setup.** Establish a framework — write tests, create setup scripts, define the todo list — then use subsequent windows to iterate.
- **Persist state externally.** Have Claude write progress, decisions, and remaining tasks to files or memory rather than relying on conversation history.
- **Structured progress tracking.** Ask Claude to maintain a structured state file (e.g., tests.json, progress.md) that can be re-read at the start of each new context window.

---

## 10. Common Pitfalls

**Over-prompting for current models:** Instructions designed to overcome limitations in earlier Claude models (emphatic language, repeated directives, aggressive tool-use triggers) cause over-compliance in current models. If your prompts were tuned for earlier models, audit them for instructions that should be softened. Replace "CRITICAL: You MUST..." with normal-weight language. Remove "If in doubt, always..." type instructions — current models have good judgment about when to act. Exception: where you are specifically countering tendency 1b or 7b on chat-interface deployments, explicit enforcement language remains appropriate.

**Verification-instruction accumulation:** Prompts that grew over multiple model generations often carry "double-check", "re-verify", "include a verification step", and "use a subagent to verify" instructions layered on top of each other. On Opus 5, these compound into over-verification (tendency #11). Audit for and remove self-directed re-checking instructions; keep only external-artifact verification (evidence grounding).

**Conservative-review literalism:** Prompts that say "only report high-severity issues" or "be conservative" cause Opus 5 to follow the instruction literally and under-report. Rewrite these to two-stage form: report everything, then filter in a separate pass.

**Subagent-verification patterns:** Harness patterns that use subagents to verify the parent agent's work are counterproductive on Opus 5. Opus 5 verifies its own work automatically; a subagent doing the same work is duplicate cost. Reserve subagent delegation for genuinely independent, parallelizable tracks of work.

**Prompt stuffing:** Adding every possible instruction "just in case" creates noise that dilutes the important instructions. Include only what's relevant to the task. Improved instruction following in current models makes this more important, not less — every instruction will be followed more precisely, including the noisy ones.

**Conflicting instructions:** If your prompt says "be concise" in one place and "be thorough and comprehensive" in another, Claude will oscillate between the two unpredictably. Audit for contradictions. Opus 5's stricter instruction adherence makes contradictions more visible in output rather than smoothing them over.

**Assuming format from description:** Saying "write a professional report" means different things to different people. Show the format explicitly or provide a structural template.

**Ignoring the user message:** In Projects, the system prompt sets behavior but the user message drives the specific task. Don't try to anticipate every possible user message in the system prompt — set principles and let them generalize.

**Over-engineering simple tasks:** A 2,000-word system prompt for "summarize this article" is counterproductive. Match prompt complexity to task complexity.

**Prefill removal:** Starting with Claude 4.6, prefilled assistant responses on the last turn are no longer supported. If your prompts relied on prefill for format control, preamble elimination, or continuation, migrate to explicit instructions.

**Carrying effort settings over from prior models:** The default moved again on the 5.5 generation — `medium` in Claude Code on Opus 5.5, Sonnet 5.5, and Haiku 5.5 — and a setting that worked on an earlier model is not necessarily right for your evals. Anthropic explicitly recommends re-running an effort sweep on your own evals rather than carrying settings over.

**Carrying Opus-5-era mitigations into 5.5-generation prompts:** thinking-disabled mitigations no longer apply (thinking cannot be disabled on Opus 5.5, Sonnet 5.5, or Fable 5.1); tool-suppressing language now causes under-search (7b); forced tool use (`tool_choice` `any` or `tool`) returns 400 on all four current models — state in the prompt when the tool applies, or use `auto` with `strict: true`.

**Adding "do not think" instructions with thinking disabled:** A system-prompt rule instructing the model not to think or not to reason (Haiku 5.5 is the only current model that can run with thinking disabled) INCREASES `<thinking>` tag leakage rather than suppressing it. If a mitigation is needed for a thinking-disabled integration, use the general "do not include internal or system XML tags" form.

---

## 11. 5.5-Generation Calibration Notes

Opus 5.5 and Sonnet 5.5 are the dual-primary calibration targets for root.node as of catalog v5.0 (2026-10-22). This section documents the calibration scope, the deployment context model, and generation-specific guidance that inform prompt and Project design decisions. Landscape facts — model IDs, prices, context windows, effort defaults, breaking changes — live in Section 3 and are not restated here.

### Calibration Scope

- **Opus 5.5 + Sonnet 5.5 dual-primary:** Skills and prompt patterns are designed against both. Where their documented behavior diverges, both are documented; T3 Skills favor Opus 5.5 behavior on divergence, T1/T2 favor Sonnet 5.5.
- **Fable 5.1 integrated-aware:** output keeps its shape on Fable 5.1, including its refusal behavior; not a routine execution target because of price, and the default on no plan or provider.
- **Haiku 5.5 subagent-aware:** the first Haiku that fits scout, researcher, and extraction roles — 1M context and effort control. Tier 2 Skills run on it at `high` effort with less depth on multi-dimensional analysis. It is a valid D9a subject model, not a grader.
- **Opus 5 / Sonnet 5 fallback-graceful:** the models users are silently served on classifier-flagged requests (Sonnet 5.5 falls back to Sonnet 5 for `cyber` and `frontier_llm`; Fable 5.1 to Opus 4.8 or Opus 5). Output must keep its shape there without the user knowing a fallback fired.
- **Sonnet 4.6 legacy-graceful:** users may still select it until retirement; quality tuning targets Sonnet 5.5.
- **Out of scope:** Haiku 4.5 (out of scope from 2026-10-15, its earliest retirement date; on third-party providers the `haiku` alias may still resolve to it — pin `claude-haiku-5-5`), Haiku 3.5 and earlier, Mythos 5.1.

**Effort-level guidance:** start at the model's default (`medium` in Claude Code on the 5.5 trio), step to `high` when verification matters, and to `xhigh` only on a measured gain. Tier 3 Skills say: Opus 5.5 at its `medium` default or `high`, or Sonnet 5.5 at `high`.

### The Deployment Context Model

| Deployment | Default Effort | Tendency Surface | Implication |
|---|---|---|---|
| Chat interface (claude.ai web/mobile) | Adaptive | HIGH for #1b, #7b, #9, #10; MEDIUM for #1a, #3a, #14 | Persistent-context instructions are weighted lower than immediate prompts. Strong countermeasures for the chat-specific tendencies. |
| Claude Projects | Adaptive (CI anchors) | MEDIUM for #1b, #9, #14; LOW for most | CI partially mitigates the chat-interface tendencies. Moderate countermeasures suffice. |
| Claude Code | `medium` on Opus 5.5 / Sonnet 5.5 / Haiku 5.5; `high` on Fable 5.1 | HIGH for #11, #12, #13; MEDIUM for #15 at `medium`, HIGH at `low`; LOW for chat-specific tendencies | The agentic tendencies surface here. Verification-instruction discipline, delegation caps, and the early-stop block (paired with the #12 paragraph) are the core set. Countermeasures excluded on the assumption of `high` effort should be applied on observation at `medium`. |
| API | Developer-controlled; defaults `medium` (Opus 5.5, Haiku 5.5) or `high` (Sonnet 5.5, Fable 5.1) | Depends on effort level and model | At `high` and above, behaves like Claude Code for agentic work; at `low`, #7b and #15 rise. |

Before applying a countermeasure, identify the deployment context. A countermeasure essential on the chat interface may be wasted tokens on Claude Code, and the reverse.

### Model-Version Awareness Guidance

Current models remain exposed to tendency #10 for model-identity claims: the model may make claims about its own version, runtime context, or system metadata without verification. For prompts and Projects where model identity matters (debugging, testing, calibration work), include explicit instructions:

```xml
<model_identity>
Do not assert your model version unless the system context explicitly
provides it. If asked what model you are running, state that you cannot
determine this from your runtime context unless the information is
explicitly available. Do not infer the model version from training data
patterns or behavioral cues.
</model_identity>
```

This is a specific application of the tendency #10 countermeasure scoped to model-identity claims.

### Tokenizer Notes

Fable 5.1 uses the same tokenizer as Fable 5 — the one introduced with Opus 4.7, roughly 30% more tokens than pre-4.7 models. Sonnet 5.5 uses the Sonnet 5 tokenizer, approximately 30% more tokens than Sonnet 4.6. Haiku 5.5 uses the Opus 4.7-era tokenizer, roughly 30% more tokens than Haiku 4.5, and bills a higher price band above 100K prompt tokens. The Opus 5.5 tokenizer is not stated on any fetched Anthropic page — treat measurements with explicit tolerance until confirmed via `count_tokens` in a future Calibration Lab session.

### API Parameter Landscape (current)

1. **Thinking cannot be disabled** on Opus 5.5, Sonnet 5.5, or Fable 5.1 (`disabled`, and `enabled` with `budget_tokens`, return 400); Sonnet 5.5's floor is `between_tools` at `high` or below; Haiku 5.5 accepts `disabled` at `high` or below.
2. **Forced tool use is removed** — `tool_choice: {"type": "any"}` or `{"type": "tool"}` returns 400 on all four current models. Use `auto` with `strict: true`, structured outputs, or a prompt statement of when the tool applies.
3. **Sampling parameters and prefill.** `temperature`, `top_p`, and `top_k` return 400 on Claude 4.7 and later models; Haiku 5.5 and Fable 5.1 also reject assistant prefill. Adaptive thinking and effort control output variation.
4. **Conversations are append-only where thinking blocks are present.** Thinking blocks are model- and conversation-bound, and accounts created on or after 2026-08-31 reject edits to `system`, `tools`, or earlier turns after a thinking block. Use mid-conversation and turn-scoped system messages instead of editing history.
5. **Progress updates arrive in `thinking` blocks** — set `thinking.display` to `"updates"` (beta) or `"summarized"`, or an API client that renders only `text` goes silent between tool calls.

For Project deployments via the chat interface these are transparent; for API integrations and Calibration Engine work they are mandatory implementation details.

### Alignment and Safety Posture

Opus 5.5 ships under the same bio and cyber safeguards as Fable. Sonnet 5.5 is the first Sonnet with frontier-model cyber safeguards. Fable 5.1's cyber safeguards trigger about 60% fewer interventions per Claude Code session than Fable 5's (Anthropic, reported via VentureBeat — a Tier 2 secondary source). Across the four guides, finding vulnerabilities in source code is allowed and high-risk dual-use work is not. The v4.0 figure that Opus 5 would intervene about 85% less often than Fable 5 is superseded. Design consequence: for defensive-security Skills, false-positive reducers matter more than model choice — ask "are there bugs" rather than "does this compile," supply documentation for lesser-known languages, and strip base64 from tool output (Fable 5.1 guide).

### When This Section Is Updated

This section is revised when:
- Anthropic ships a new Opus, Sonnet, Haiku, or Fable generation, or changes which model is the Claude Code default
- An effort default, a thinking rule, or fallback semantics change
- A new tendency is documented by Anthropic or observed in production across independent deployments
- The Calibration Engine produces empirical regression data that contradicts current calibration assumptions

Last revision: October 2026 (v5.0 alignment cycle — 5.5-generation alignment; landscape block verified 2026-10-22).
