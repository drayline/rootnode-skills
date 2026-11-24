# root.node — Design: Fable 5.2 alignment and scale-fit rigor (catalog v6.1)

```
root · DESIGN · fable-5-2-alignment · v1.0 · 2026-11-24
Status: LOCKED 2026-11-24 as the build spec for catalog v6.1. Decisions D1–D10 taken as recommended under the operator's instructions "continue with your recommendations" and "ok, continue". §7 is the build specification.
Inputs: root_RESEARCH_fable_5_2_alignment.md (pass 1); Anthropic pages fetched 2026-11-24 (prompting guide, migration guide, model overview); drayline/rootnode-skills main at 07ae3fa0cb960d9b6c398da1cd387080fdd73fdc.
```

Labels: **PRIMARY** (Anthropic page, read through a summarizing fetch) · **COUNT** (grep at `07ae3fa`) · **INFERENCE** · **UNVERIFIED**.

## 1. Corrections to research pass 1

| Pass 1 said | Corrected |
|---|---|
| Reasoning requested in the response is the highest-risk item for `rootnode-prompts` (22 hits in 10 files) | Wrong as a risk rating. I read the hits. The catalog already carries the `reasoning_extraction` rule from v5.0: 6 of the hits are the catalog's own warnings against the practice, and 4 are advice to replace "think step by step". Two lines remain to reword: the identity trait "You explain your reasoning transparently…" in `identity-blocks/SKILL.md:134` and its copy in `block-selection/references/identity-blocks.md:191` |
| One "treat that answer as done" line exists | The pattern matched once, but a context read returned nothing. UNVERIFIED; the build greps for it and reports |
| Claude Code platform rows need the official changelog | Still open. The fetch of `code.claude.com/docs/en/changelog` returned a copy whose newest entry is 2.1.311 (2026-10-26). Every November row in pass 1 §4 stays SECONDARY except `additionalContext` for Stop hooks, which is in the hooks reference |
| Context window and max output not stated | PRIMARY (overview): 1M context, 128K max output, knowledge cutoff June 2026, cache read $0.20, release 2026-11-09. Default effort by model: Fable 5.2 `high`, Opus 5.5 `medium`, Sonnet 5.5 `high`, Haiku 5.5 `medium`. No tokenizer change is stated |

## 2. Decisions

| # | Decision | Taken | Rationale | Rejected |
|---|---|---|---|---|
| D1 | Release shape | **Catalog v6.1**, a full catalog release. Five plugins to 6.1.0, `rootnode-code` to 6.2.0, umbrella `catalog-v6.1` | Calibration lines change in all six plugins (COUNT: 27 marker lines), so the single-plugin shape does not fit. One cut also carries the 6.1.0 queue (harness fix, spec v1.1, playbook line, SBD line) | Six single-plugin cuts; a patch label for a behavior change in cc-design |
| D2 | Calibration scope | Opus 5.5 + Sonnet 5.5 stay the dual-primary pair for Tier 1 and Tier 2. **Fable 5.2 replaces Fable 5.1 and becomes a named target for Tier 3**, not a fallback. Tier membership: zero moves (T1=13, T2=7, T3=7) | Fable 5.2 is on all paid plans and is the model the operator runs. It costs 2x Opus 5.5, so it is not the default recommendation for Tier 1 and 2 work. Changing tier meaning and membership together makes a regression unattributable (v4.0 precedent) | Fable 5.2 as sole primary; leaving it "integrated-aware" |
| D3 | Effort wording | One sentence per tier, built on PRIMARY facts: Fable 5.2 starts at `high` and steps down to `medium` where the work holds; Opus 5.5 starts at `medium`; `xhigh` only on a measured gain; "reserve Fable 5.1" lines go | The current lines assume a `medium` default (COUNT: 49 hits in 10 files) | Per-Skill effort tables with no evals behind them |
| D4 | Taxonomy 15 → 17, defects 4 → 5 | **#16 caution accumulation** and **#17 silent long runs** as new entries. Facets: #13 gains self-review subagents at `xhigh`/`max`; #15 gains effort conditioning and its token cost; #12 gains ownership framing as a costed lever; #11 gains the "treat as done" caution. New conditional defect: a token budget shown in the prompt raises spending | Each has a documented behavior and a documented countermeasure in the Fable 5.2 guide. Numbering extends, so no reference breaks | Folding #16 into #12: the direction is opposite (too little action, not too much) |
| D5 | Scale-fit rigor in cc-design | A `rigor` field in the design brief: **sprint**, **standard**, **strict** (§3). A three-condition stop rule replaces the open-ended halt list (§4). Every prompt lists routine actions that need no approval | The operator's finding and Anthropic's guidance agree: stop conditions and cautions sized for a large system slow a small one, and most stops carry no decision | Keeping today's defaults and adding advice to "halt less" |
| D6 | Token budgets | cc-design stops requiring token budgets in prompt text. Budgets live in mechanisms (`--max-budget-usd`, caps in settings or environment) and the numbers stay in the design brief | PRIMARY: a budget shown in the prompt raised spending at equal performance. Conflict with cc-design Step 4 (COUNT: 26 hits in 11 files; only the cc-design and Phase Loop uses are prompt-facing) | Removing budgets from the methodology |
| D7 | Capitalized absolutes | This cut classifies and rewrites only text that cc-design and behavioral-tuning **emit into user artifacts** (CLAUDE.md templates, session-prompt blocks, countermeasure templates). The catalog-wide sweep (COUNT: 807 in 124 files) waits for the measurement cycle | PRIMARY: "never" is read as absolute; scoped rules with reasons are preferred. Emitted text multiplies into every project; internal Skill prose does not. A blind sweep would delete real constraints (the 2-of-2 false-positive result recorded in the v4.0 propagation cycle) | Bulk replace |
| D8 | Stale-caution check | One check added to `memory-optimization`: instructions and cautions whose reason no longer holds, and lines written for an older model. The other audits are candidates for the measurement cycle | PRIMARY: stale instructions keep being followed. First-party tooling covers the Claude Code layer only | Adding it to four Skills at once |
| D9 | Phase Loop | Reopened for the operator's own use. Built outside the catalog, at **sprint** rigor first: PLAN → BUILD → LAND, tests on the merged tree, revert on red, questions in a file. REFUTE and digest binding become settings that standard and strict turn on | The dropped half of the October verdict was "keep as internal practice". v0.1 as written is strict rigor on every item, which removes file transfers and keeps the ceremony | Building v0.1 unchanged |
| D10 | Validation for this cut | Mechanical gates for the calibration and taxonomy edits. One behavioral check for cc-design: three briefs (small personal project, production service, one-file control), scored on whether the output's stops and gates match the brief. One test pass, one fix pass | The Skill's stated goal is the bar (SBD §3.9 stopping rule). Full eval suites belong to the measurement cycle | A D9a on all six plugins |

Default for D5 that is the operator's to change: a brief with no `rigor` value is treated as **sprint** unless it names production data, an irreversible operation, or more than one contributor, which make it **standard**. **Strict** is chosen explicitly.

## 3. Rigor levels (cc-design)

| Setting | Sprint | Standard | Strict |
|---|---|---|---|
| Stops in a session | Only the stop rule (§4) | The stop rule, plus one merge or release gate | The stop rule, plus a gate per phase |
| Independent review | None. Tests are the check | One refute pass, one cycle, no operator gate | Builder→Refuter, two cycles, digest-bound ACCEPT |
| Digest binding | For files the operator hands over | Spec digest | Spec and diff digests, receipt freeze |
| `rootnode-code` gates | Config with `mode: watch` | `watch` until a named milestone, then `enforce` | `enforce` |
| Session report | Five lines and the file list | Computed-state report | Computed-state report with evidence per gate |
| CLAUDE.md | Mission, scope, stop rule | R1–R5 | R1–R5 and warranted W1–W3 |
| Delegation | None unless the brief asks | Capped by mechanism | Capped by mechanism, roles fully specified |

Moving up a level is an EVOLVE-mode change with a recorded trigger: first production deploy, first external user, first irreversible data operation, or a defect that a higher level would have caught.

## 4. Stop rule

A session stops for the operator only when one of three conditions holds: the next action cannot be undone; a decision could reasonably go either way and only the operator can make it; a spend cap is reached. In every other case the session decides, records the choice in its report, and continues. A blocked step is worked through or routed around and reported; it is a stop only when it meets one of the three conditions. Hooks and deny rules still enforce the irreversible set; the rule governs prose stops, not mechanisms.

Lands in: AEA §4.7 (halt-and-escalate principle), CC_EG §4 and §5.9 (scope authorization and turn economy), cc-design `cc-prompt-design-patterns.md` and the CLAUDE.md template.

## 5. Change list

| Surface | Change | Decisions |
|---|---|---|
| `root_CLAUDE_OPTIMIZATION_NOTES.md` §3 and header | Landscape block refreshed for Fable 5.2 (facts in §1 and research §2); Fable 5.1 lines retired | D2, D3 |
| `root_OPTIMIZATION_REFERENCE.md` taxonomy | #16, #17, the four facets, the fifth conditional defect, with countermeasure templates and deployment conditioning marked D9c-analytical | D4 |
| `root_AGENT_ENVIRONMENT_ARCHITECTURE.md` §4.7, §4.8 | Stop rule; taxonomy count 15 → 17 | D4, D5 |
| `root_CC_ENVIRONMENT_GUIDE.md` §3.4, §4, §5.9, §6 | 5.2 defaults; rigor levels; stop rule; budgets as mechanisms; opt-in rule for blocking hooks | D3, D5, D6 |
| `root_AUDIT_FRAMEWORK.md`, `root_AGENT_ANTI_PATTERNS.md` §6, `root_SKILL_BUILD_DISCIPLINE.md` §3.9 and §7.3 and the hooks paragraph | Taxonomy counts; SBD block 1 from `kf-update-blocks.md` | D4, 6.1.0 queue |
| `root_SKILLS_RELEASE_PLAYBOOK.md` line 29 | "Chat ignores plugin hooks and agents" corrected | 6.1.0 queue |
| All 27 SKILL.md calibration lines; README model-compatibility section | D2 and D3 wording | D2, D3 |
| `rootnode-tuning:behavioral-tuning` | SKILL.md routing surface and references for #16, #17 and the facets (Observation 29: both, not references only); emitted templates reworded per D7 | D4, D7 |
| `rootnode-code:cc-design` | Rigor field in the brief schema and interview; stop rule; positive scope; Step 4 budget bullet; emitted templates per D7; 6.1.0 spec v1.1 and harness fix | D5, D6, D7 |
| `rootnode-prompts` | The two identity-trait lines in §1; `domain-agentic-context` prompt-facing budget wording | D6, §1 |
| `rootnode-projects:memory-optimization` | Stale-caution check | D8 |
| Custom Instructions | Taxonomy count, CC-mode rules 7–9 for rigor and the stop rule | D4, D5 |

KF propagation chain for the cut: (1) seed Project first; (2) `design/staging-kf/` then `audit/canonical-kfs/` and `docs/`; (3) installed plugins on release; (4) global `~/.claude/CLAUDE.md`: the stop rule is a candidate that passes the universality test on its face (it names no model), to be confirmed against the project-scoped CLAUDE.md files before it lands there.

## 6. Ranked candidates outside this cut (INFERENCE; nothing ships before eval suites exist)

| Rank | Candidate | Basis |
|---|---|---|
| 1 | Measurement cycle as already planned: graders the baseline can fail, effort sweep per model, the collapse test | Anthropic's own migration order is "sweep effort, then fix one behavior at a time and measure" |
| 2 | Stale-caution and older-model checks in project-audit and global-audit, on the claude.ai layers `/doctor` does not read | Research §3 row 11; the October second pass |
| 3 | Verify gate message through `additionalContext` in `watch` mode | Hooks reference; lets a watch-mode gate inform without blocking |
| 4 | Session-handoff re-scope once the Phase Loop runs | October review §5 |
| 5 | Consolidation of the eleven `rootnode-prompts` Skills | Needs lift data first |

## 7. Build specification

Correction to draft 1 and to research pass 1: the halt-and-escalate principle is AEA §4.7. §4.6 is "Files as primary context surface". Section numbers below were read from the mirror at `07ae3fa`.

**KF route for this cut (a deliberate deviation, stated once).** The usual order is seed Project first, then staging, then the mirror. Here the build session edits the eight files from their repo copies, using this spec as the approved content, and the operator uploads the eight results to the Project after the merge. Reason: the Projects tool returns KFs inline and accepts a write only after a full read, so seed-first costs a full read and a full write of eight large files in chat, while the repo copies matched the seed by digest on 2026-11-03 and the build context records no KF edit since. One upload step replaces two transfers.

**Quotation rule for the build.** Anthropic's wording in this spec is paraphrase. Put quotation marks around Anthropic text only when the session fetched the page itself and copied the words. Otherwise paraphrase and tag `[Anthropic docs — <page>, fetched 2026-11-24, paraphrase]`.

### 7.1 Landscape facts (dated block, 2026-11-24)

| Fact | Value | Source |
|---|---|---|
| Model | Claude Fable 5.2, `claude-fable-5-2`, released 2026-11-09; replaces Fable 5.1 | overview; migration guide |
| Window, output, cutoff | 1M tokens; 128K max output; knowledge cutoff June 2026 | overview |
| Price per million tokens | $8 input, $40 output; cache read $0.20; Opus 5.5 is $4 / $20 | overview; migration guide |
| Default effort by model | Fable 5.2 `high`; Opus 5.5 `medium`; Sonnet 5.5 `high`; Haiku 5.5 `medium` | overview comparison table |
| Effort guidance for Fable 5.2 | Start at `high`; most of the gain arrives there; step down to `medium` where evals hold; `low` suits subagent and high-volume work; `xhigh` only on a measured gain; re-run the sweep, do not carry settings from 5.1 or Opus 5.5 | prompting guide |
| Thinking | Adaptive, always on; `disabled` and `budget_tokens` return 400; "do not deliberate" lines do not stop thinking at `medium` and above; thinking counts toward `max_tokens` | all three pages |
| Rejected or omitted parameters | Prefill and forced `tool_choice` return 400; omit `temperature`, `top_p`, `top_k` | migration guide; overview |
| History | Editing `system`, `tools` or earlier messages mid-conversation fails a prefix check (400); keep history append-only | prompting and migration guides |
| Refusals | `stop_reason: "refusal"` with `stop_details.category`; reasoning written into the response is a trigger | prompting guide |
| Not stated | Tokenizer change; Claude Code's default model and default effort for Fable 5.2 | — |

Every value is a dated product fact. In KF and Skill text each carries `[Anthropic docs — <page>, fetched 2026-11-24]`. Claude Code version-specific statements are written only if the session verifies them on its running version, and then with that version.

### 7.2 Calibration lines (27 SKILL.md files)

Edit sentences, not whole lines; each Skill's own tail text stays.

| Tier | Change |
|---|---|
| 1 | After "(Opus 5.5, Sonnet 5.5)" add ", on Fable 5.2," before "and on Haiku 5.5" |
| 2 | After the sentence that names the default effort, add: "On Fable 5.2 the default is `high`; step down to `medium` where the work holds." |
| 3 | Replace the sentence that begins "Reserve Fable 5.1" with: "Fable 5.2 is a named target: start at its `high` default and step down to `medium` where your evals hold. It costs about twice Opus 5.5 per token, so choose it for the hardest and longest runs." |

Description fields do not change. A line whose shape does not match its tier's rule is reported and edited to the same meaning.

### 7.3 Every other "Fable 5.1" mention (COUNT at `07ae3fa`: 86 in 18 plugin files; 65 in the seven KFs)

Classify each before editing; report the table. **Landscape** (states what is current: defaults, roles, "reserve", calibration scope) → rewrite for Fable 5.2 from §7.1. **Evidence** (cites a Fable 5.1 guide as the source of a documented behavior) → keep, and add the Fable 5.2 guide beside it where §7.4 gives one. **History** (changelog, "NEW in", a dated record) → keep unchanged.

### 7.4 Taxonomy (canonical home `root_OPTIMIZATION_REFERENCE.md`; same format as entry #15)

**#16 Caution Accumulation (NEW in Fable 5.2).** *What it looks like:* the agent asks for approval on routine steps, holds back ordinary actions, or stops at the first error, because cautions have piled up in memory, notes, rules and instruction files; absolute "never" rules are applied far outside the case they were written for. *Warrant:* Prompting Claude Fable 5.2, "Keep caution from piling up" and "Review prompts"; the operator's own observation across projects, 2026-11-24. *Deployment calibration (D9c analytical, not measured):* multi-agent and long-lived projects with Memory or handoff chains HIGH; Claude Code with a large CLAUDE.md and rules MEDIUM to HIGH; chat LOW; single-shot API LOW. *Opposite of #12:* #12 is action beyond the request; #16 is too little action. *Levers, in order:* (1) remove: delete cautions whose reason no longer holds, at every model generation; (2) scope: rewrite an absolute as a scoped rule with its reason; (3) positive scope: name the routine steps that need no approval; (4) narrow validation stops such as "stop at the first error"; (5) if a system stays stuck, restart it with trimmed memory and notes. *Template:*

```text
Routine steps that need no approval: {LIST}. Do them without asking.
Ask before: {SCOPED LIST, each item with its reason}.
A rule in memory, notes or an instruction file applies only while its reason holds. If you find one whose reason no longer applies, name the file and the line in your report. Do not keep following it silently, and do not delete it yourself.
```

*Placement:* core rules; the lists come from the project's scope authorization. Cross-reference CC_EG §4 (rigor levels and the stop rule).

**#17 Silent Long Runs (NEW in Fable 5.2).** *What it looks like:* the first tool call arrives with no statement of intent, and long stretches of tool calls pass with no user-facing text. *Warrant:* Prompting Claude Fable 5.2, "Keep users informed". *Deployment calibration (D9c analytical):* chat and Cowork with a person watching MEDIUM to HIGH; interactive Claude Code MEDIUM; unattended Claude Code and API loops not applicable, because the session report carries the need. *Opposite of #3b:* #3b is too much narration. Choose by deployment, never ship both. *Template, for watched sessions only:*

```text
Before your first tool call, say in one line what you are about to do. Every few tool calls, give a one-line update. End with a short recap that a reader who saw none of the steps can follow.
```

*Cost:* Anthropic reports about 20% more output tokens for the full form. *Harness lever:* check that the client shows thinking updates between tool calls before adding prompt text.

**Facets and notes on existing entries.** #13 gains a facet, self-review delegation: at `xhigh` and `max` the model starts subagents to review its own work, and subagents can be a large share of session cost; levers are the effort level, the existing mechanism caps, and a subagent tool description that states the cost, when delegation is worth it, and how to brief. #15 gains Fable 5.2 conditioning: more common at `low` and `medium`; Anthropic reports a finishing block roughly halved sessions that ended with continuable work at `medium`, at about 30% more output tokens. #12 gains a note: ownership framing ("owner and long-term maintainer") is a deliberate lever that makes the model consolidate duplicate code and also raises output tokens by 70 to 80% and produces unrequested changes; a "no drive-by refactors" rule did not cancel it; use it only when the operator owns the design decision, never as a default. #11 gains a caution: lines that tell the model to treat an answer as done reduce its willingness to flag its own earlier mistakes on Fable 5.2; scope them or remove them.

**Fifth prompt/environment-conditional defect: prompt-visible token budget.** A token budget shown in the prompt raises spending; Anthropic reports lower cost at equal performance with it removed, at `high` and `xhigh`. Fix: keep the number in the design brief and enforce it with a mechanism (a spend flag, a cap in settings or the environment), not with prompt text.

**Counts.** Every statement of "15 tendencies" and "four conditional defects" that describes the current taxonomy becomes 17 and five, in the seven KFs and in `behavioral-tuning` (SKILL.md routing surface and references, both). Dated history lines keep their numbers.

### 7.5 Rigor, stop rule, scope and budgets (text is §3 and §4 of this spec)

| Lands in | Content |
|---|---|
| AEA §4.7 | The stop rule as the default halt set, with the sentence that hooks and deny rules still enforce the irreversible set |
| CC_EG §4 | A subsection "Rigor levels" holding the §3 table, the default rule under the §2 table, and the move-up triggers; a subsection "Positive scope": every prompt and CLAUDE.md lists the routine actions that need no approval |
| CC_EG §5.9 | The stop rule replaces any open-ended list of phase halts; a halt that meets none of the three conditions is a defect in the prompt |
| CC_EG §3.4 | Retitled for the current generation; §7.1 defaults; subagents at `low` on Fable 5.2 as a starting point |
| CC_EG §6 | Budgets are mechanisms, not prompt text (D6); the SBD hooks paragraph's opt-in rule in one sentence, pointing to SBD |
| SBD hooks paragraph | Block 1 of `audit/v6_1-release/kf-update-blocks.md`, as written there |
| Playbook line 29 | Replace "Chat ignores plugin hooks and agents." with: "A chat session that has a container runs plugin hooks; a shipped hook that can block must opt in per repository (SBD §4.7)." |

### 7.6 `rootnode-code:cc-design`

1. Design brief: a `rigor` field (`sprint` | `standard` | `strict`) in `cc-design-brief.schema.json`, optional, and one interview question that sets it. The default rule under the §2 table applies when it is absent.
2. Every DESIGN and TEMPLATE output opens with one line: `Rigor: <level> — <reason in one clause>`.
3. The level selects what the output contains, per the §3 table. At sprint the output has no reviewer role, no phase gates and no digest gates beyond operator-supplied files.
4. Halt triggers stay mandatory, and they are the stop rule plus project-specific irreversible actions. Each prompt also carries the positive scope list.
5. Step 4 "Token budgets" bullet is replaced: spend and context limits are enforced by mechanisms and recorded in the brief; prompt text carries no token budget.
6. D7: in the CLAUDE.md template, the session-prompt blocks and the delegation brief text that the Skill emits, each capitalized NEVER / ALWAYS / MUST is classified. Keep it for an irreversible action, a safety boundary or a spec rule; otherwise rewrite it as a scoped rule with its reason. Report the table. Skill-internal prose is not in scope.
7. `design/root_DESIGN_verify_gate_fix.md` gains "## 8. Amendments (v1.1)": F1 (the guard exits 0 on empty or malformed hook input), F3 (the fingerprint includes untracked, non-ignored file contents), and routine choices 6 and 8 of the 6.1.0 session report. The harness hides one tool by building a folder of links to every other tool, not by dropping the tool's folder from `PATH`; the no-`jq` and no-`git` rows must pass on Linux for the right reason.

### 7.7 Other Skills

| Skill | Change |
|---|---|
| `rootnode-tuning:behavioral-tuning` | #16, #17, the facets and the fifth defect on the SKILL.md routing surface and in the references; "Fifteen" becomes "Seventeen"; SKILL.md stays at or under 500 lines and the description at or under 1,024 characters, with two symptom triggers added if they fit ("asks permission for everything", "goes silent for long stretches") and the result reported; emitted countermeasure templates classified per D7 |
| `rootnode-prompts:identity-blocks`, `block-selection` (its copy) | The trait "You explain your reasoning transparently so others can disagree with your logic…" becomes "You state the grounds for each conclusion, so that others can disagree with the grounds and not only with the conclusion." |
| `rootnode-prompts:domain-agentic-context` | Where it tells a prompt author to put a token budget in an agent's prompt, apply D6; context-window planning tables for the designer stay |
| `rootnode-projects:memory-optimization` | One check in its audit stage: cautions and instructions whose reason no longer holds, and lines written for an older model; the fix is removal or a scoped rewrite, proposed to the user, never applied silently |
| All 27 | `metadata.version` takes the plugin's new version (SBD §6.6); `metadata.predecessor` unchanged |
| Root README | Model-compatibility section per §7.1 and §7.2; a Quick Start line telling Claude Code users to run `/reload-plugins` or restart when synced plugins do not appear |

### 7.8 Validation (D10)

Mechanical: after the edits, no landscape-class "Fable 5.1" mention remains (§7.3 table); the count statements agree (§7.4); OPT_REF holds exactly one heading each for #16 and #17; `behavioral-tuning` limits hold; `claude plugin validate` passes for the marketplace and each plugin; the packager builds six zips and its embedded-copy check passes.

Behavioral, cc-design only. Three briefs, each run once through `claude -p` with the built plugin loaded, output saved to a file:

| Brief | Text | Assertions on the output file |
|---|---|---|
| B1 | "I'm building a personal command-line tool in Python that renames photo files by EXIF date. One contributor, no production data, pytest exists. Design the Claude Code environment and the first session prompt." | First line matches `Rigor: sprint`; no "Refuter"; no "token budget"; contains a list of actions that need no approval |
| B2 | "Design the Claude Code environment for a payments reconciliation service: three engineers, a Postgres production database with migrations, weekly production deploys." | First line matches `Rigor: standard` or `Rigor: strict`; names a merge or release gate; protects `migrations` by a mechanism |
| B3 | "Write a session prompt to fix one typo in README.md." | First line matches `Rigor: sprint`; no subagent or reviewer role; 40 lines or fewer |

Positive control: B1 against the 6.1.0 plugin from `origin/main` must fail at least one assertion. If it passes all, the assertions cannot see the change; fix them before reading any result. One test pass and one fix pass; a remaining miss is recorded and goes to the next patch.

### 7.9 Not in this cut

The catalog-wide sweep of capitalized absolutes; eval suites; stale-caution checks in project-audit and global-audit; the Phase Loop build; the `additionalContext` gate message; the website sync; the Custom Instructions (seed-side, after the merge).
