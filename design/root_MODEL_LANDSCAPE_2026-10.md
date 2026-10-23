# root_MODEL_LANDSCAPE_2026-10 — dated landscape block

**Status:** Verified 2026-10-22 against Anthropic primary documentation. Dated block per AEA §4.15 — decision records reference this block; they do not embed it. Refresh at the next model release.

**Supersedes:** the 2026-07-24/25 landscape block (Opus 5 + Sonnet 5 dual-primary, v4.0 alignment cycle).

**What changed since the last block, in one paragraph.** Four releases in five weeks: Fable 5.1 (2026-09-01), Opus 5.5 (2026-09-22), Sonnet 5.5 (2026-09-28), Haiku 5.5 (2026-10-07). All four share a 1M context window, 128K max output, and a June 2026 reliable knowledge cutoff. Opus 5.5 is the Claude Code default on every Anthropic-hosted plan and the recommended starting model for most workloads ("For most workloads, start with Claude Opus 5.5" — Fable 5.1 what's-new). The effort default moved to `medium` on the three 5.5 models in both the API (Opus 5.5 only) and Claude Code (all three). Thinking cannot be disabled on Opus 5.5, Sonnet 5.5, or Fable 5.1; Haiku 5.5 still accepts `disabled` at `high` or below. Forced tool use (`tool_choice: any|tool`) is rejected on all four. Haiku 5.5 is the first 1M-context, effort-capable Haiku and is positioned as a subagent model. Prices fell: Opus 5.5 $4/$20 (from $5/$25), Sonnet 5.5 cache reads halved, Fable 5.1 cache reads quartered.

---

## 1. Current models

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

Sources: models overview, per-model what's-new pages, pricing, model deprecations (all platform.claude.com/docs — see §8).

**Mythos 5.1** (`claude-mythos-5-1`) shares the Fable 5.1 model with looser safeguards; verified-organization access only. Out of scope for Skill calibration.

## 2. Still-active prior generation (fallback / legacy posture)

| Model | State | Role in this landscape |
|---|---|---|
| Opus 5 (`claude-opus-5`) | Active, retirement not sooner than 2027-07-24 | Permitted fallback target for Fable 5.1. Reads/writes thinking blocks compatible with Opus 5.5. |
| Sonnet 5 (`claude-sonnet-5`) | Active, not sooner than 2027-06-30 | Server-side fallback target for Sonnet 5.5 `cyber`/`frontier_llm` declines. |
| Fable 5 (`claude-fable-5`) | Active, not sooner than 2027-06-09 | Superseded; `fable` alias resolves to Fable 5.1 except in Claude apps gateway sessions. |
| Opus 4.8 (`claude-opus-4-8`) | Active, not sooner than 2027-05-28 | Permitted fallback target for Fable 5.1. Rejected as an advisor for Sonnet 5.5 executors. |
| Sonnet 4.6 (`claude-sonnet-4-6`) | Active, not sooner than 2027-02-17 | Legacy; effort ladder lacks `xhigh`; 1M only via `[1m]`. |
| Haiku 4.5 (`claude-haiku-4-5-20251001`) | Active, not sooner than **2026-10-15** | Earliest retirement in the active set. Still the `haiku` alias on Bedrock / Agent Platform / Foundry / Claude Platform on AWS. |
| Sonnet 4.5 | **Deprecated 2026-09-30, retires 2026-11-30** | Replacement: `claude-sonnet-5-5`. Still the Foundry default model in Claude Code. |

## 3. Calibration scope for the catalog (proposal)

**Dual-primary: Opus 5.5 + Sonnet 5.5.** Opus 5.5 is the CC default on every Anthropic-hosted plan and the API's recommended starting point; Sonnet 5.5 is the cost-optimal agentic tier with the same 1M/128K envelope. **Fable 5.1 integrated-aware** (not default anywhere; reserve for long-horizon work where Opus 5.5 at higher effort still fails evals). **Haiku 5.5 subagent-aware** — the first Haiku that fits the Scout/Researcher roles with effort control and a 1M window. **Opus 5 / Sonnet 5 fallback-graceful** (the models users are silently served on classifier-flagged requests). **Sonnet 4.6 and Haiku 4.5 legacy-graceful** until their retirement dates; Haiku 4.5 drops out of scope on 2026-10-15 and the catalog should not carry a Haiku 4.5 line past that date.

This replaces the v4.0 scope sentence ("Opus 5 + Sonnet 5 dual-primary, Fable 5 integrated-aware, Opus 4.8 fallback-graceful, Sonnet 4.6 legacy-graceful, Haiku 4.5 graceful-with-extended-thinking"). The three-tier structure (Model-compatible / Sonnet-graceful / High-effort recommended) is landscape-independent and survives unchanged; only the model column refreshes.

## 4. Breaking API changes that touch Skill content

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

## 5. Behavioral deltas documented by Anthropic (what the tendency taxonomy must absorb)

Each row is a documented, prompt-addressable behavior from the per-model prompting guides. "Taxonomy" names the existing root.node tendency it maps to, or NEW where none exists.

| Behavior | Models documented | Anthropic's countermeasure (gist) | Taxonomy |
|---|---|---|---|
| **Early turn termination** — ends the turn with a summary-plus-next-step and no tool call, offers to continue, lists non-blocking decisions, or stops at a milestone; at `low`/`medium` pauses to confirm a plan or asks a question it could answer | Opus 5.5 (unattended runs), Sonnet 5.5 (`low`/`medium`), Haiku 5.5 (`low`, long prompts), Fable 5.1 ("Finishing the whole task") | Name the specific early stops to avoid and the stops you do want; "Keep working until everything the user asked for is done, and only stop to ask when you can't go on without the user or before a risky step"; harness continuation message, capped at 2–3; treat text-only end of turn as a report, not proof | **NEW #15** (candidate) — distinct from #12 scope expansion (too much) and #6 over-exploration (search breadth); this is too little |
| **Unrequested additions** — adds tests, docs, refactors, supporting files that fit repo conventions; more at higher effort; starts building on open-ended "show me what you can do" requests | Sonnet 5.5 (every level), Fable 5.1, Haiku 5.5 | "Don't add features, tests, files, docs or refactors that weren't asked for. If you think one would help, mention it at the end"; "When the user asks for ideas, options or a plan, give them that and stop" | #12 scope expansion — extend symptom list and template |
| **Self-started review rounds and reviewer-subagent launches** at `xhigh`/`max` | Sonnet 5.5 | "Don't start extra rounds of review or hardening on your own, and don't launch reviewer sub-agents unless the user asked" — cut session cost ~⅓ at `max`, no quality change | #11 over-verification + #13 over-delegation — add the effort-conditioned facet and the one-paragraph countermeasure |
| **Verification skip at `low` (and `medium` on Haiku)** — reports a change done without running a real check | Sonnet 5.5 (`low`), Haiku 5.5 (`low`/`medium`) | The "run a real check that exercises the change before reporting it done" block; "A syntax-only check, or a check command that failed to start, does not count" | External-artifact verification (AEA §4.14 keep-and-imperative class) — the opposite shape from #11; effort-conditioned |
| **Thinking-instruction accumulation** — "think carefully before answering," "re-verify earlier answers" | Opus 5.5 (chat system prompts) | Remove; effort is the control. Optional "treat earlier answers as settled" line for chat, not for agentic work | #11 over-verification — REMOVAL shape extends to thinking instructions |
| **Under-exploration in multi-app workflows** — "tends to get to work quickly" | Opus 5.5 | "Before taking any action, explore broadly with tool calls…" | Inverse of #6 — add as a deployment-conditioned note on #6, not a new tendency |
| **Tool-use suppression carried over from older prompts** — "only use tools when strictly necessary" now under-searches | Sonnet 5.5, Haiku 5.5, Fable 5.1 (`low`) | Remove discouraging language; add the search nudge; give the current date (Haiku) | #7 tool-trigger miscalibration — the fix direction flipped from "stop over-calling" to "remove suppression" |
| **Parallel tool calling more variable** — one call per turn where Fable 5 batched | Fable 5.1 | Batching nudge as a turn-scoped system message after each tool-result turn | #7 facet (CC harness already batches; API-surface only) |
| **Denser prose, less formatting, unmarked quotations** | Fable 5.1 | Remove anti-formatting rules or replace with the "use lists when the content is multifaceted" formulation; add a quotation example; "remove all mannered prose" | #3c written-deliverable length and #4 list overuse — **the v4.0 anti-list countermeasures can now over-correct on Fable 5.1**; #5 fabricated precision gains an "unmarked quotation" facet |
| **Whole-file rewrites for small edits** | Fable 5.1 | "surgically edit a file rather than rewrite the entire thing" | NEW facet under #3c (token cost, not quality) — CC-relevant |
| **Drafts deliverable in thinking, then again in reply** at `xhigh`/`max` | Fable 5.1 | Prefer `high`; the max_tokens-aware "don't draft twice" line | #3c facet, effort-conditioned |
| **Mid-turn user text misread as prompt injection** | Sonnet 5.5, Haiku 5.5 | Never put user text in `tool_result`; separate harness notices from user words; no token countdowns | Harness-design rule, not a tendency — lands in agentic-context / cc-design |
| **Reasoning leaks into visible text** at `low` or thinking-off | Haiku 5.5 | Switch to adaptive thinking at `medium` | Prompt/environment-conditional defect (existing "thinking-disabled output artifacts" entry) — update: now a Haiku-only case since the others cannot disable thinking |
| **Conservative-review literalism** | (carried from Opus 5; not re-documented) | — | Existing conditional defect; keep |
| **Communication improved:** less jargon, important information first (Opus 5.5); "writes more clearly" (Sonnet 5.5) | Opus 5.5, Sonnet 5.5 | None needed | #1 agreeableness / #2 hedging — deployment-conditioning tables can lower CC-surface likelihood a notch; verify before lowering |

**Fewer false positives on cyber:** Fable 5.1's cyber safeguards trigger ~60% fewer interventions per Claude Code session than Fable 5's (Anthropic, via VentureBeat). Opus 5.5 ships under the same safeguards as Fable (bio + cyber classifiers). Sonnet 5.5 is the first Sonnet with frontier-model cyber safeguards. The v4.0 domain-software-engineering "Opus 5 cyber classifier posture" section (85%-less-often, Fable-5-relative) is superseded.

## 6. Claude Code facts (verified against code.claude.com/docs, 2026-10-22)

- **Default model:** Opus 5.5 on Pro, Max, Team, Enterprise, and Anthropic API; also on Claude Platform on AWS, Bedrock, Google Cloud Agent Platform. Microsoft Foundry defaults to Sonnet 4.5. "Fable models are not the account-type default on any plan or provider."
- **Alias resolution (Anthropic API):** `opus` → Opus 5.5, `sonnet` → Sonnet 5.5, `haiku` → Haiku 5.5, `fable` → Fable 5.1 (Fable 5 in Claude apps gateway sessions), `best` → `fable` where available else `opus`. Third-party providers lag: Bedrock/Agent Platform `sonnet` → Sonnet 4.5, `haiku` → Haiku 4.5.
- **Minimum Claude Code versions:** Fable 5.1 v2.1.257+, Opus 5.5 v2.1.280+, Sonnet 5.5 v2.1.284+, Haiku 5.5 v2.1.293+. Current changelog tip observed: 2.1.308. **The operator's last recorded Claude Code version was 2.1.136 (2026-09-13 cycle) — upgrade to ≥ 2.1.293 before any test pass.**
- **Default effort:** `high` on every effort-capable model except Opus 5.5 / Sonnet 5.5 / Haiku 5.5 (`medium`) and Opus 4.7 (`xhigh`). Resolution order: `CLAUDE_CODE_EFFORT_LEVEL` / `--effort` / `/effort` → `modelSettings` per-model or `effortLevel` → model default. Doc states "Opus 5.5 ignores a top-level `effortLevel` in user settings, which applies to Opus 5 and earlier models" — *verify on the running version before relying on it*; use per-model `modelSettings`.
- **Opus 5.5 at `medium` "matches or exceeds Opus 5 at `high` on coding and knowledge-work evaluations"** — "When you move from Opus 5 to Opus 5.5, start at `medium`."
- **Thinking:** cannot be turned off on the 5.5 trio or Fable; `ultrathink` requests deeper reasoning for one turn.
- **Ultracode:** a session setting, not an effort level; `/effort ultracode` and `/effort ultracode off` (v2.1.284+); `"ultracode": true` in settings; exempts the session from the concurrent-subagent limit; unavailable when workflows are off or the model lacks `xhigh`.
- **Subagents:** model resolution order (v2.1.251+): per-invocation `model` → definition `model` frontmatter (`inherit` selects main) → `CLAUDE_CODE_SUBAGENT_MODEL` → main conversation's model. `CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1` (v2.1.257+) overrides all. **`CLAUDE_CODE_WORKFLOW_SUBAGENT_MODEL`** (v2.1.296) runs every workflow agent on one model. **Agent tool `effort` parameter** (v2.1.292) sets a sub-agent's effort per invocation. Built-in Explore inherits the main model; when main runs Fable, Explore runs on the `opus` alias (Anthropic-hosted only). Concurrent-subagent limit 20 (`CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`, v2.1.217+); nesting depth 3 (`CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`, `1` turns nesting off); fork mode on by default (`CLAUDE_CODE_FORK_SUBAGENT=0` to disable); `maxTurns` returns partial output (v2.1.246+); `CLAUDE_CODE_DISABLE_EXPLORE_PLAN_AGENTS=1` (v2.1.198+).
- **1M context** is the default (no `[1m]` suffix) on Fable, Sonnet 5+, Haiku 5.5, Opus 4.7+. `CLAUDE_CODE_DISABLE_1M_CONTEXT=1` reverts to 200K. Haiku 5.5 bills a higher band above 100K prompt tokens.
- **Other 2.1.29x additions worth noting for CC design:** `CLAUDE_CODE_RETRY_WATCHDOG*` unattended retry mode; `CLAUDE_CODE_AUTO_COMPACT_WINDOW` accepts `k`/`M`; idle compaction (`CLAUDE_CODE_IDLE_COMPACT_MIN_TOKENS`, v2.1.290+); `/advisor`; `/ultrareview`; agent teams; Workflow tool / dynamic workflows (`CLAUDE_CODE_DISABLE_WORKFLOWS` still referenced by the Skill — verify the name on the running version).

Every `CLAUDE_CODE_*` name and default above is a dated product fact. Carry the "verify against the running Claude Code version" marker into any generated design (CC_EG §6 rule).

## 7. Open items — do not assert

- Opus 5.5 tokenizer vs Opus 5: not stated on any fetched page. Treat as "same family as Sonnet 5.5 / Fable 5.1 (Opus 4.7-era)" only after `count_tokens` confirmation.
- Claude.ai plan defaults (which model Free/Pro/Max serve by default in chat): not fetched; the Claude Code defaults above are verified, chat defaults are not.
- Whether `CLAUDE_CODE_DISABLE_WORKFLOWS` is still the workflow kill switch name on 2.1.30x.
- Claude Code default *model* on Max vs Pro beyond "Opus 5.5" (e.g., whether Pro has usage-credit gating on Opus 5.5): not stated on the fetched page.
- Behavioral re-baselining of the 14-tendency deployment-conditioning tables on the 5.5 generation is analytical (D9c) from Anthropic's guides, not measured. Calibration Lab re-baselining remains open (carried from v4.0).

## 8. Sources

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
