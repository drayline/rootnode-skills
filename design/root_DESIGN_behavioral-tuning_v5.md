# root_DESIGN_behavioral-tuning_v5 — design spec for rootnode-behavioral-tuning 5.0.0

**Predecessor:** rootnode-behavioral-tuning 4.0.0 (`820e5c0`; SKILL.md 490 lines; `references/countermeasure-templates.md` 663 lines).
**Inputs:** `root_MODEL_LANDSCAPE_2026-10.md` §5 (the behavior table — every row below cites its Anthropic guide through that table); root_OPTIMIZATION_REFERENCE.md (canonical taxonomy, 14 entries); SBD §7.3 (taxonomy additions are warrant-requiring).
**Scope:** taxonomy 14 → 15; SKILL.md routing surface repaired; deployment-conditioning tables rebuilt for the `medium`-default generation; four tendencies gain documented facets; one conditional defect narrowed.

---

## 1. Defect found in the predecessor (fix first)

SKILL.md v4.0.0 still carries the 10-tendency routing surface: the description says "Covers ten tendencies"; line 28 says "Version 2.0 — 10-tendency taxonomy, Opus 4.8 calibration"; the "## The Ten Tendencies" section stops at #10; the Diagnostic routing table has no row for #11–#14. Tendencies 11–14 and the #3a/3b/3c refactor exist only in `references/countermeasure-templates.md` as a "v4.0 addendum" (sections 11–14, lines 437–620). A user whose symptom is "Claude keeps re-checking its work" or "Claude spawns subagents for one-line fixes" cannot reach the countermeasure from the routing surface. This is a D4 progressive-disclosure failure (routing surface does not route) and a D3 methodology-preservation failure against the canonical KF. v5.0 repairs it as part of the taxonomy extension, so the repair and the extension land in one edit of each affected section.

## 2. Tendency #15 — Early turn termination (NEW; warrant below)

**Definition.** The model ends its turn while work it was asked for is still owed: a summary that closes by announcing the next step with no tool call; an offer to continue "unless you'd prefer otherwise"; a list of decisions for the user when none of them blocks the remaining work; a report because the turn has been long or a milestone is done; at low effort, pausing to confirm a plan or asking a question it could answer itself; in long agent prompts, handing the task back. Distinct from #12 scope expansion (the model does too much) and from #6 over-exploration (search breadth within a task) — #15 is too little, and its countermeasure runs in the opposite direction from #12's, which is why it cannot be a #12 facet.

**Warrant (SBD §7.3).** Documented with a prompt-level countermeasure in all four current Anthropic prompting guides: Opus 5.5 ("Unattended agentic runs" — the four named early stops; "Treat a text-only end of turn as a report rather than as proof the task is done"), Sonnet 5.5 ("Carrying work through" at `low`/`medium`), Haiku 5.5 ("Early stopping" — raising `low`→`medium` "roughly halved early stopping"), Fable 5.1 ("Finishing the whole task" — two blocks). Four independent primary-source documentations clears the named-practitioner-documentation threshold; the behavior is also the mechanism behind CC_EG §5.9 turn economy and the operator's standing instruction that multi-phase CC prompts run end-to-end.

**Deployment conditioning** (D9c analytical from the guides; not measured):
- Chat interface (default effort): LOW — a chat turn is supposed to end.
- Claude Code (`medium` default on Opus 5.5 / Sonnet 5.5 / Haiku 5.5): **MEDIUM at `medium`, HIGH at `low`**; LOW at `high` and above. Long system prompts raise it (Haiku guide).
- API agentic (developer-controlled effort): same as Claude Code by effort level; HIGH for fully unattended loops with no harness continuation.
- Cowork / scheduled runs: HIGH — no operator present to send the continuation.

**Countermeasure templates** (both verbatim from Anthropic; the Skill supplies placement, not wording):
- *Default block* (Sonnet 5.5 / Haiku 5.5 guides): "Keep working until everything the user asked for is done, and only stop to ask when you can't go on without the user or before a risky step. When the work the user asked for is done and checked, stop and report. Don't add features, tests, files, docs or refactors that weren't asked for. If you think one would help, mention it at the end instead of doing it." — note the second paragraph is the #12 countermeasure; the two ship together because a prompt that only says "keep working" invites scope expansion.
- *Fully-unattended variant* (Opus 5.5 guide, the long "standing instruction from the user… about how your turns end" block): place at the end of the system prompt from the first request; never in human-in-the-loop applications; keep the risky-action confirmation step.
- *Harness complement*: a continuation message naming the open items, capped at two or three per task; if something the model started is still running (background command, subagent), the task is not done — wait and return its output as the next user message.
- *First lever is effort*: at `low`/`medium` try raising effort before adding the block; the block lengthens and costs more at low effort (Sonnet guide).

**Symptom rows for the routing table:** "Claude stops and asks me to confirm mid-task" → 15; "Claude writes a summary and a next step but doesn't do the step" → 15; "the agent hands the task back half-done" → 15; "Claude offers to continue instead of continuing" → 15.

**Self-referential note.** An instruction that tells the model to keep working is not a self-verification instruction (AEA §4.14) — it governs turn boundaries, not re-checking. The D7 scan must not flag it.

## 3. Facets added to existing tendencies (from landscape §5)

| Tendency | New facet / change | Source | Countermeasure change |
|---|---|---|---|
| #3c written-deliverable length | **Whole-file rewrites for small edits** (token cost, not quality); **draft-in-thinking-then-again-in-reply** at `xhigh`/`max` | Fable 5.1 guide | Add "surgically edit a file rather than rewrite the entire thing" and the max_tokens-aware "don't draft twice" line; prefer `high` |
| #3c / #4 list overuse | **Over-correction warning**: Fable 5.1 formats less (less bold, fewer headers/lists) and writes denser prose by default; v4.0-era anti-formatting countermeasures can now suppress structure the content needs | Fable 5.1 guide | Replace blanket anti-list rules with the conditional formulation ("use lists… when the content is multifaceted enough that they help; plain prose in conversational exchanges"); "remove all mannered prose" for density |
| #5 fabricated precision | **Unmarked quotations** — reproduces source passages without quotation marks in summaries | Fable 5.1 guide | One complete worked example (request → correct response → rationale) in the system prompt; marked quotation required in the Output layer |
| #6 over-exploration | **Inverse note**: Opus 5.5 "tends to get to work quickly" in multi-app workflows — under-explores | Opus 5.5 guide | Deployment-conditioned: on Opus 5.5 multi-app tasks the countermeasure is the opposite ("Before taking any action, explore broadly with tool calls…"); keep #6 for `xhigh`/`max` |
| #7 tool trigger miscalibration | **Fix direction flipped for 7b**: tool-suppressing language from older prompts ("only use tools when strictly necessary") now causes under-search; at `low` the model answers from memory | Sonnet 5.5, Haiku 5.5, Fable 5.1 guides | Remove discouraging language; add the search nudge; give the current date (Haiku); on Fable 5.1 at `low` raise effort for affected turns or add the name-verification nudge; **do not add blanket "always search" instructions** (Haiku guide: searched on half the no-search prompts, no accuracy gain). 7a (over-triggering) keeps its template but its CC likelihood drops to LOW |
| #11 over-verification | **Thinking-instruction extension**: "think carefully before answering," "re-verify earlier answers" lines are removal targets; effort is the control. **Effort-conditioned facet**: at `xhigh`/`max` Sonnet 5.5 starts its own review rounds | Opus 5.5, Sonnet 5.5 guides | Removal sweep pattern list gains "think carefully / think step by step before answering"; add the optional "treat earlier answers as settled" line for chat only (not for agentic work, where later steps can reveal earlier mistakes) |
| #12 scope expansion | **Unrequested additions**: tests, docs, small supporting files that fit repo conventions, at every effort level and more at higher; **builds on open-ended "show me what you can do"** | Sonnet 5.5, Fable 5.1, Haiku 5.5 guides | The "Don't add features, tests, files, docs…" paragraph (shared with #15); "When the user asks for ideas, options or a plan, give them that and stop"; the Fable 5.1 "pre-existing bug → report as follow-up" block for coding |
| #13 subagent over-delegation | **Effort-conditioned**: at `xhigh`/`max` Sonnet 5.5 launches reviewer subagents on its own — the one-paragraph countermeasure "stopped reviewer subagent launches and cut session cost by about a third, with no change in quality" | Sonnet 5.5 guide | Add the paragraph as the first-line countermeasure before any cap mechanism; keep the mechanism template (CLAUDE_CODE_* names re-verified per the cc-design spec §3) |
| Conditional defect: thinking-disabled output artifacts | **Narrowed**: thinking cannot be disabled on Opus 5.5 / Sonnet 5.5 / Fable 5.1; the artifact (reasoning leaks into visible text, internal tags) is now documented only on Haiku 5.5 at `low` or with thinking off, and on Sonnet 5.5 `between_tools` when a "don't think" instruction is left in place | Haiku 5.5, Sonnet 5.5 guides | Fix: adaptive thinking at `medium`; remove any "do not think" line (it increases tag leakage — the v4.0 sub-finding stands) |
| Conditional defect: conservative-review literalism | unchanged | carried | unchanged |
| NEW conditional defect: **mid-turn user text misread as injection** | Sonnet 5.5 / Haiku 5.5 treat user text inside `tool_result` blocks, per-step harness notices, and token countdowns as injection and may ignore them | Sonnet 5.5, Haiku 5.5 guides | Harness fix, not a prompt fix: user words as a text block after the last `tool_result`; harness notices in a separate mid-conversation system message; no countdowns in interactive sessions. Routes to rootnode-domain-agentic-context for the harness design; this Skill carries the symptom row ("Claude ignores messages I send while it's working") |
| NEW conditional defect: **reasoning-extraction refusal** | Prompts asking the model to reproduce its reasoning in the response are declined (`stop_reason: refusal`, category `reasoning_extraction`) | all four guides | Remove reproduce-your-reasoning instructions; ask for a short explanation or action summary; read `display: "summarized"` thinking blocks. Symptom row: "Claude refuses when I ask it to show its reasoning" |

## 4. Deployment-conditioning table rebuild

Every "Claude Code (`high` default on Opus 5 / Sonnet 5)" line (SKILL.md lines 67, 103, 130, 156, 183, 209, 234, 256, 284, 311, 340 and the §"Deployment conditioning" prose at 397–409) is rewritten as "Claude Code (`medium` default on Opus 5.5 / Sonnet 5.5 / Haiku 5.5)". Likelihood values are re-stated per tendency with this rule: where the v4.0 value was justified by `high`-effort behavior ("`high` and above already mitigate 5, 6, 7a, 9" — countermeasure-templates line 424), the v5.0 value carries a one-line note that at the `medium` default the mitigation is weaker and the countermeasure should be applied on observation rather than excluded by default. No likelihood is raised or lowered without a cited guide sentence; absent one, the v4.0 value stays with the note. The API row keeps "(effort ≥ high)" since the API defaults differ (Sonnet 5.5 `high`, Opus 5.5 `medium`, Fable 5.1 `high`) — state the three defaults once in the §"Deployment conditioning" prose and point to the landscape block.

Countermeasure-templates lines 302, 424–425 ("`high` default") rewrite the same way; line 659 (thinking-disabled 400 at `xhigh`/`max`) becomes the Haiku-only statement; line 645–649 (thinking-disabled artifacts) narrows per §3.

## 5. SKILL.md structural changes

| Section | Change |
|---|---|
| frontmatter `description` | "Covers ten tendencies: …" → "Covers fifteen tendencies: … plus over-verification, scope expansion, subagent over-delegation, correction narration, early turn termination." Add trigger phrases: "Claude stops halfway," "keeps double-checking," "spawns subagents for everything," "adds tests I didn't ask for." Re-measure YAML-parsed length (v4.0: not recorded — build records it); if > 1024, drop the parenthetical facet list first |
| line 24 calibration | T2 template (catalog spec §3.1) |
| line 28 version line | "Version 5.0 — 15-tendency taxonomy, 5.5-generation calibration" |
| "## The Ten Tendencies" | → "## The Fifteen Tendencies"; #3 gains the 3a/3b/3c sub-structure as a routing paragraph (depth stays in the reference's Section 3 refactor); #11–#14 added as routing-surface entries (definition, deployment conditioning, one-line countermeasure, pointer to reference Section N) at the same density as #1–#10; #15 per §2 |
| Diagnostic routing table | Add rows: 11 ("Claude keeps re-checking / re-verifying its work", "the prompt says double-check and output got slower"), 12 ("Claude adds things I didn't ask for", "built a whole feature when I asked for options"), 13 ("Claude spawns subagents for tiny tasks", "every subagent runs on the expensive model"), 14 ("Claude narrates every correction"), 15 (§2 rows), and the two new conditional-defect rows |
| "## Deployment conditioning" | Rewrite per §4; add the three API defaults sentence |
| Troubleshooting line 476 ("Pre-4.7 prompts with emphatic language") | Keep; add "Pre-5.5 prompts with thinking-disabled mitigations or tool-suppression language: remove them (tendencies 7b, 11)" |
| Quality Gate | Add: "Did the countermeasure set exclude a tendency on the assumption of `high` effort when the deployment runs at `medium`?" |

Body length: v4.0 is 490 lines — already at the 500-line ceiling. Adding five routing entries and ~10 table rows requires extraction. Each tendency entry in SKILL.md carries five sub-blocks (Facets / Symptom profile / Deployment calibration / Countermeasure / Placement); the "Symptom profile" lists duplicate the Diagnostic routing table rows and are the extraction target — keep one symptom sentence per tendency in the entry and let the routing table be the symptom surface. The three Examples (lines 433–467) move to `countermeasure-templates.md` as worked examples. Target ≤ 480 lines after extraction; the build reports before/after.

Description length: v4.0 YAML-parses to **928 chars** (96 headroom). The new trigger phrases and the "fifteen tendencies" list will not fit alongside the full tendency enumeration; rewrite the enumeration as a count plus the five highest-traffic names and spend the characters on triggers (the description is the activation surface, the enumeration is not). Build records the parsed length; hard ceiling 1024.

## 6. Reference changes (`countermeasure-templates.md`)

Line 3 "14-tendency" → "15-tendency"; TOC gains Section 15; header lines 5–7 rewritten for the 5.5 cycle; Section 15 (early turn termination) added with the three templates from §2; Sections 3, 4, 5, 6, 7, 11, 12, 13 gain the §3 facets; the conditional-defects block gains the two new entries and narrows the thinking-disabled entry; "v4.0 addendum" framing (line 437) is removed — sections 11–14 become first-class sections in numeric order (the addendum structure is the mechanism by which they fell off the routing surface). Variants extracted from SKILL.md land in their matching sections. Target ≤ 800 lines, TOC present.

## 7. Routing collisions and composition

Negative triggers unchanged. New vocabulary ("stops halfway", "hands the task back") does not collide with rootnode-handoff-trigger-check (which gates *whether* to hand off to CC, not agent turn-ending) or rootnode-cc-design (which places the countermeasure in a CC prompt; this Skill diagnoses and supplies it). Composition: cc-design §6 autonomous prompts points here for the #15 template ("if available"); domain-agentic-context owns the harness-side injection fix and points here for the symptom row.

## 8. Tests

D9c for every new or changed entry (pressure scenario, cited guide sentence, expected baseline failure, expected compliance). One D9b run if Tier B is available at build: a CC session on Opus 5.5 at `medium` given a three-part task without the #15 block, then with it, counting early stops — the only new tendency with a cheap runnable instrument. D9a is not run (cost; the catalog's D9a budget goes to cc-design). Stopping rule: one test pass, one fix pass.

## 9. KF blocks surfaced

OPT_REF: #15 entry (definition, conditioning, countermeasure, warrant); facets for #3c, #4, #5, #6, #7, #11, #12, #13; conditional-defect subsection changes. AUDIT_FRAMEWORK Dimension 6: fifteen. AAP §6: fifteen. CLAUDE_OPTIMIZATION_NOTES: landscape block replacement. build_context: Observation candidate O29 — a reference-file "addendum" that is not mirrored onto the SKILL.md routing surface is unreachable in practice; the v4.0 build added four tendencies the Skill could not route to for one full release cycle (a check needs a carrier — O26 applied to progressive disclosure).
