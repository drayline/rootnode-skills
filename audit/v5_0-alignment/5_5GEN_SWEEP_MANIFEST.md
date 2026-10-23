# 5_5GEN_SWEEP_MANIFEST — catalog v5.0 (gate T1, plus T8 record)

**Status:** Phase 2 test pass, 2026-10-22, branch `release/v5.0`. Append-only after commit.

## T1 — landscape sweep

Command (session prompt, verbatim): `grep -rnE -e 'Opus 5\b' -e 'Sonnet 5\b' -e 'Haiku 4\.5' -e 'Fable 5\b' -e 'Opus 4\.8' rootnode-*/`

- Literal output: **190** hit lines, read in full. `\b` matches between `5` and `.`, so the literal regex also hits every `Opus 5.5` / `Sonnet 5.5` / `Fable 5.1` mention.
- Exact old-generation forms (same pattern with `(?![.\d])` after each bare version; run in Python because Git Bash `grep -P` refused the locale): **46** lines, each classified below.
- Regex artifacts: 190 − 46 = **144** lines whose every match is a 5.5-generation name (`Opus 5.5`, `Sonnet 5.5`, `Fable 5.1`). Class: current — not a landscape hit.

### Classification of the 46 exact-form lines

| Location | Matched forms | Class | Note |
|---|---|---|---|
| `rootnode-anti-pattern-detection/SKILL.md:27` | Opus 5, Sonnet 5 | fallback-or-legacy clause | §3.1 calibration template ("Fallback-graceful on Opus 5 / Sonnet 5") |
| `rootnode-behavioral-tuning/SKILL.md:27` | Opus 5, Sonnet 5 | fallback-or-legacy clause | §3.1 calibration template ("Fallback-graceful on Opus 5 / Sonnet 5") |
| `rootnode-behavioral-tuning/SKILL.md:422` | Opus 5 | historical | comparison baseline in Anthropic quote: Opus 5.5 at medium "matches or exceeds Opus 5 at high" |
| `rootnode-behavioral-tuning/references/countermeasure-templates.md:3` | Opus 5 | historical | names the v4.0 cycle (Opus 5 generation) |
| `rootnode-behavioral-tuning/references/countermeasure-templates.md:510` | Opus 5 | historical | v4.0-cycle quotation from the Opus 5 prompting guide, labeled as such |
| `rootnode-behavioral-tuning/references/countermeasure-templates.md:769` | Opus 5 | historical | "Carried from the Opus 5 generation" - conditional-defect provenance |
| `rootnode-block-selection/SKILL.md:27` | Opus 5, Sonnet 5 | fallback-or-legacy clause | §3.1 calibration template ("Fallback-graceful on Opus 5 / Sonnet 5") |
| `rootnode-cc-design/references/cc-delegation-patterns.md:42` | Opus 5, Sonnet 5 | fallback-or-legacy clause | comparison baseline quote + "Opus 5 / Sonnet 5 remain valid fallbacks" |
| `rootnode-cc-design/references/cc-environment-design-patterns.md:189` | Haiku 4.5 | fallback-or-legacy clause | D6 third-party `haiku`-alias pin note (Skill-side twin of the README pin line) |
| `rootnode-context-budget/SKILL.md:51` | Opus 5, Sonnet 5 | fallback-or-legacy clause | "Fallback-graceful on Opus 5 / Sonnet 5" |
| `rootnode-context-budget/SKILL.md:69` | Haiku 4.5 | fallback-or-legacy clause | row-mandated legacy note (catalog §4 context-budget row a) |
| `rootnode-context-budget/SKILL.md:85` | Haiku 4.5 | fallback-or-legacy clause | row-mandated legacy-only sentence (row b) |
| `rootnode-context-budget/SKILL.md:94` | Haiku 4.5 | fallback-or-legacy clause | tokenizer comparison baseline (row c) |
| `rootnode-context-budget/SKILL.md:95` | Sonnet 5 | fallback-or-legacy clause | "Sonnet 5.5 uses the Sonnet 5 tokenizer" - current fact (row c) |
| `rootnode-context-budget/SKILL.md:120` | Haiku 4.5 | fallback-or-legacy clause | row-mandated "Legacy" table sub-row (row d) |
| `rootnode-critic-gate/SKILL.md:31` | Opus 5, Sonnet 5 | fallback-or-legacy clause | §3.1 calibration template ("Fallback-graceful on Opus 5 / Sonnet 5") |
| `rootnode-critic-gate/SKILL.md:158` | Opus 4.8, Sonnet 5 | fallback-or-legacy clause | advisor pairings rejected by a Sonnet 5.5 executor (landscape §4.9 fact) |
| `rootnode-domain-agentic-context/SKILL.md:25` | Opus 5, Sonnet 5 | fallback-or-legacy clause | §3.1 calibration template ("Fallback-graceful on Opus 5 / Sonnet 5") |
| `rootnode-domain-agentic-context/SKILL.md:55` | Sonnet 5 | fallback-or-legacy clause | Sonnet 5.5 server-side fallback target is Sonnet 5 (landscape §4.6) |
| `rootnode-domain-agentic-context/SKILL.md:57` | Opus 4.8, Opus 5 | fallback-or-legacy clause | Fable 5.1 fallback targets Opus 4.8 / Opus 5 (landscape §4.6) |
| `rootnode-domain-agentic-context/references/reasoning-approaches.md:89` | Opus 5 | row-preserved | catalog §4 row: "Line 89 (reasoning-approaches.md) unchanged" - next-patch candidate: generalize "Opus 5" to the 5.5 generation |
| `rootnode-domain-business-strategy/SKILL.md:25` | Opus 5, Sonnet 5 | fallback-or-legacy clause | §3.1 calibration template ("Fallback-graceful on Opus 5 / Sonnet 5") |
| `rootnode-domain-content-communications/SKILL.md:25` | Opus 5, Sonnet 5 | fallback-or-legacy clause | §3.1 calibration template ("Fallback-graceful on Opus 5 / Sonnet 5") |
| `rootnode-domain-research-analysis/SKILL.md:27` | Opus 5, Sonnet 5 | fallback-or-legacy clause | §3.1 calibration template ("Fallback-graceful on Opus 5 / Sonnet 5") |
| `rootnode-domain-software-engineering/SKILL.md:24` | Opus 5, Sonnet 5 | fallback-or-legacy clause | §3.1 calibration template ("Fallback-graceful on Opus 5 / Sonnet 5") |
| `rootnode-domain-software-engineering/SKILL.md:38` | Fable 5 | historical | comparison basis for the ~60% figure ("than Fable 5") |
| `rootnode-domain-software-engineering/SKILL.md:54` | Opus 5 | row-preserved | catalog §4 row: keep the conservative-review-instruction fix verbatim |
| `rootnode-full-stack-audit/SKILL.md:45` | Opus 5 | fallback-or-legacy clause | "Fallback-graceful on Opus 5 / Sonnet 5" (orchestrator ruling wording) |
| `rootnode-global-audit/SKILL.md:45` | Opus 5 | fallback-or-legacy clause | "Fallback-graceful on Opus 5 / Sonnet 5" (orchestrator ruling wording) |
| `rootnode-handoff-trigger-check/SKILL.md:30` | Opus 5, Sonnet 5 | fallback-or-legacy clause | §3.1 calibration template ("Fallback-graceful on Opus 5 / Sonnet 5") |
| `rootnode-handoff-trigger-check/SKILL.md:38` | Haiku 4.5 | fallback-or-legacy clause | operator-specified legacy sentence (cycle 3) + "legacy 200K Haiku 4.5 window" |
| `rootnode-handoff-trigger-check/SKILL.md:44` | Haiku 4.5, Sonnet 5 | fallback-or-legacy clause | row-mandated tokenizer comparison (Sonnet 5 tokenizer; Haiku 4.5 baseline) |
| `rootnode-identity-blocks/SKILL.md:27` | Opus 5, Sonnet 5 | fallback-or-legacy clause | §3.1 calibration template ("Fallback-graceful on Opus 5 / Sonnet 5") |
| `rootnode-memory-optimization/SKILL.md:27` | Opus 5, Sonnet 5 | fallback-or-legacy clause | §3.1 calibration template ("Fallback-graceful on Opus 5 / Sonnet 5") |
| `rootnode-mode-router/SKILL.md:31` | Opus 5, Sonnet 5 | fallback-or-legacy clause | §3.1 calibration template ("Fallback-graceful on Opus 5 / Sonnet 5") |
| `rootnode-output-blocks/SKILL.md:27` | Opus 5, Sonnet 5 | fallback-or-legacy clause | §3.1 calibration template ("Fallback-graceful on Opus 5 / Sonnet 5") |
| `rootnode-profile-builder/SKILL.md:30` | Opus 5, Sonnet 5 | fallback-or-legacy clause | §3.1 calibration template ("Fallback-graceful on Opus 5 / Sonnet 5") |
| `rootnode-project-audit/SKILL.md:43` | Opus 5 | fallback-or-legacy clause | "Fallback-graceful on Opus 5 / Sonnet 5" (orchestrator ruling wording) |
| `rootnode-project-brief/SKILL.md:27` | Opus 5, Sonnet 5 | fallback-or-legacy clause | §3.1 calibration template ("Fallback-graceful on Opus 5 / Sonnet 5") |
| `rootnode-prompt-compilation/SKILL.md:53` | Opus 5 | fallback-or-legacy clause | "Fallback-graceful on Opus 5 / Sonnet 5" (orchestrator ruling wording) |
| `rootnode-prompt-validation/SKILL.md:26` | Opus 5, Sonnet 5 | fallback-or-legacy clause | §3.1 calibration template ("Fallback-graceful on Opus 5 / Sonnet 5") |
| `rootnode-prompt-validation/references/symptom-fix-map.md:176` | Opus 5 | row-preserved | catalog §4 row: "Line 156 (self-consistency) unchanged" - next-patch candidate |
| `rootnode-reasoning-blocks/SKILL.md:27` | Opus 5, Sonnet 5 | fallback-or-legacy clause | §3.1 calibration template ("Fallback-graceful on Opus 5 / Sonnet 5") |
| `rootnode-session-handoff/SKILL.md:29` | Opus 5, Sonnet 5 | fallback-or-legacy clause | §3.1 calibration template ("Fallback-graceful on Opus 5 / Sonnet 5") |
| `rootnode-skill-builder/SKILL.md:29` | Opus 5, Sonnet 5 | fallback-or-legacy clause | §3.1 calibration template ("Fallback-graceful on Opus 5 / Sonnet 5") |
| `rootnode-skill-builder/references/multi-environment-adaptation.md:34` | Opus 5, Sonnet 5 | fallback-or-legacy clause | "(Opus 5 / Sonnet 5 valid fallback)" - row text |

**Counts by class:** fallback-or-legacy clause = 38; historical = 5; row-preserved = 3 -> total 46. **Defects remaining: 0** (defects found during the build were fixed by the Builders; see the appendix logs).

### Haiku 4.5 mentions vs the gate's pass wording

The session prompt's T1 pass condition says the README `haiku`-alias pin line should be the only Haiku 4.5 mention outside historical text. Inside `rootnode-*/`, Haiku 4.5 still appears on 7 lines (context-budget :69, :85, :94, :120; handoff-trigger-check :38, :44; cc-environment-design-patterns :189 — handoff :38 and :44 each carry two mentions). Each is a legacy note the catalog spec §4 row requires (context-budget rows a–d; the handoff-trigger-check "legacy-only" clause and tokenizer comparison), the operator-specified cycle-3 wording (handoff-trigger-check :38), or the Skill-side twin of the D6 pin line (cc-design :189). None names Haiku 4.5 as a calibration target. Recorded as a tension between the spec rows and the gate wording for operator review, not as a defect.

### Next-patch candidates from the sweep

- `rootnode-domain-agentic-context/references/reasoning-approaches.md:89` — "Opus 5 already does this automatically": kept because the row says the line is unchanged; generalize to the 5.5 generation next patch.
- `rootnode-prompt-validation/references/symptom-fix-map.md:176` — "Opus 5's automatic self-verification": same reason.

## T8 — reasoning-blocks sweep

- Before (literal four-phrase grep): 0 hits. A block-by-block read found 4 paraphrased instructions to put reasoning in the response (comparative-reasoning.md ×2, strategic-reasoning.md ×1, technical-reasoning.md ×1). All 4 were rewritten to "state a short rationale" and are listed by path:line in the Builder-B log below.
- After: 0 hits. The literal grep was re-run in Python because Git Bash grep aborted on this pattern set. Refuter-B and Refuter-B2 paraphrase sweeps of SKILL.md plus all six references found 0 remaining.

## Appendix — Builder sweep logs (verbatim scratchpad copies at build time)

### sweep_A.md

# sweep_A — Builder-A landscape sweep (8 Skills), 2026-10-22

Files swept: SKILL.md + references/*.md of anti-pattern-detection, context-budget, critic-gate, domain-agentic-context, domain-content-communications, domain-research-analysis, domain-software-engineering, full-stack-audit.

Literal grep (`Opus 5\b|Sonnet 5\b|Haiku 4\.5|Fable 5\b|Opus 4\.8`) post-edit: 51 hit lines. `\b` also matches the current-generation forms (Opus 5.5, Sonnet 5.5, Fable 5.1), which are correct current-landscape statements by construction: 32 of the 51 lines are only such forms and need no classification. The remaining 19 lines (exact-form hits: Opus 5, Sonnet 5, Fable 5, Haiku 4.5, Opus 4.8) are classified below.

## A. Remaining exact-form hits (19 lines): 16 fallback/legacy, 3 historical, 0 defects

rootnode-anti-pattern-detection/SKILL.md:27 — fallback/legacy — T2 template line; "fallback-graceful on Opus 5 / Sonnet 5" per D2
rootnode-context-budget/SKILL.md:51 — fallback/legacy — "Fallback-graceful on Opus 5 / Sonnet 5"; the trailing Haiku 4.5 out-of-scope sentence was later deleted per orchestrator correction (defect-fixed; no Haiku 4.5 hit remains on this line)
rootnode-context-budget/SKILL.md:69 — fallback/legacy — row (a) legacy note for Haiku 4.5 (200K), explicitly authorized by the row
rootnode-context-budget/SKILL.md:85 — fallback/legacy — row (b) legacy-only Haiku 4.5 200K sentence
rootnode-context-budget/SKILL.md:94 — fallback/legacy — Haiku 4.5 used as the tokenizer comparison baseline for Haiku 5.5 (row (c))
rootnode-context-budget/SKILL.md:95 — fallback/legacy — "Sonnet 5.5 uses the Sonnet 5 tokenizer" (row (c))
rootnode-context-budget/SKILL.md:120 — fallback/legacy — row (d) "Legacy" sub-row for Haiku 4.5
rootnode-critic-gate/SKILL.md:31 — fallback/legacy — T2 template line
rootnode-critic-gate/SKILL.md:158 — fallback/legacy — advisor pairing list (landscape §4.9): Sonnet 5.5 executor rejects Opus 4.8 / Opus 4.7 / Sonnet 5 / Haiku 5.5 advisors
rootnode-domain-agentic-context/SKILL.md:25 — fallback/legacy — T1 template line
rootnode-domain-agentic-context/SKILL.md:55 — fallback/legacy — Sonnet 5 as Sonnet 5.5's cyber/frontier_llm fallback target (landscape §4.6)
rootnode-domain-agentic-context/SKILL.md:57 — fallback/legacy — Fable 5.1 fallback targets Opus 4.8 / Opus 5 (landscape §4.6)
rootnode-domain-agentic-context/references/reasoning-approaches.md:89 — historical — "Opus 5 already does this automatically"; row says line 89 unchanged; left verbatim (flag: arguably should read "the 5.5 generation")
rootnode-domain-content-communications/SKILL.md:25 — fallback/legacy — T1 template line
rootnode-domain-research-analysis/SKILL.md:27 — fallback/legacy — T1 template line
rootnode-domain-software-engineering/SKILL.md:24 — fallback/legacy — T1 template line
rootnode-domain-software-engineering/SKILL.md:38 — historical — "Fable 5" is the comparison baseline of the Fable 5.1 ~60% figure (Tier 2 source, marked)
rootnode-domain-software-engineering/SKILL.md:54 — historical — conservative-review-instruction fix kept verbatim per row ("Opus 5 follows literally"; landscape §5 lists it as a carried-over, not re-documented, conditional defect)
rootnode-full-stack-audit/SKILL.md:45 — fallback/legacy — "Fallback-graceful on Opus 5 / Sonnet 5" (identical to the Builder-B wording); the trailing Haiku 4.5 out-of-scope sentence was later deleted per orchestrator correction (defect-fixed; no Haiku 4.5 hit remains on this line)

## B. Stale current-landscape claims rewritten (defect-fixed), post-edit line numbers

rootnode-context-budget/SKILL.md:16-17 — defect-fixed — description effort sentence to the exact full-stack-audit wording (row did not target the description; see concern)
rootnode-context-budget/SKILL.md:27 — defect-fixed — T3 template
rootnode-context-budget/SKILL.md:49 — defect-fixed — "Opus 5 or Sonnet 5 (both default to `high`)" to T3 wording
rootnode-context-budget/SKILL.md:51 — defect-fixed — "(Opus 5, Sonnet 5) at `high`" and "Haiku 4.5 with extended thinking" and "Fallback-graceful on Opus 4.8" rewritten
rootnode-context-budget/SKILL.md:68 — defect-fixed — context window list to Fable 5.1 / Opus 5.5 / Sonnet 5.5 / Haiku 5.5 (row (a))
rootnode-context-budget/SKILL.md:85 — defect-fixed — 200K-Haiku paragraph made legacy-only (row (b))
rootnode-context-budget/SKILL.md:94-96 — defect-fixed — tokenizer notes (row (c)); tolerance line kept for Opus 5.5
rootnode-context-budget/SKILL.md:112 — defect-fixed — "verified during the v4.0 alignment cycle" intro of the window table updated to 2026-10-22
rootnode-context-budget/SKILL.md:116-120 — defect-fixed — table: four current rows plus Legacy Haiku 4.5 sub-row (row (d))
rootnode-context-budget/SKILL.md:365 — defect-fixed — API-deployment context-window sentence: model list updated, 200K Haiku 4.5 clause dropped (row (e) says "unchanged"; see concern)
rootnode-anti-pattern-detection/SKILL.md:27, rootnode-critic-gate/SKILL.md:31, rootnode-domain-agentic-context/SKILL.md:25, rootnode-domain-content-communications/SKILL.md:25, rootnode-domain-research-analysis/SKILL.md:27, rootnode-domain-software-engineering/SKILL.md:24, rootnode-full-stack-audit/SKILL.md:27 — defect-fixed — calibration lines replaced whole by tier template
rootnode-domain-agentic-context/SKILL.md:31-33 — defect-fixed — "v4.0 update — refusal & fallback semantics (Opus 5, Fable 5)" retitled and re-scoped to the 5.5 generation
rootnode-domain-software-engineering/SKILL.md:36-52 — defect-fixed — "v4.0 update — Opus 5 cyber classifier posture" replaced; 85% figure deleted
rootnode-full-stack-audit/SKILL.md:16-17, 43, 45 — defect-fixed — description, Model-requirements paragraphs to T3 wording

"fourteen" / "14" tendency count: no occurrence in any of the 8 Skills (SKILL.md or references). No symptom-routing table lists tendencies by number in anti-pattern-detection. Nothing to change.

### sweep_B.md

# sweep_B.md

## T8 before
(end of hit list)

## T8 after
Command rerun after edits: 0 hits (literal phrases). Before: 0 hits.

### T8 paraphrase and block-by-block review (SKILL.md plus six references, every `<reasoning>` block read)
Rewritten to "state a short rationale" phrasing (instruction to present reasoning with the answer; mapped to the reasoning_extraction category risk). Count: 4.
- rootnode-reasoning-blocks/references/comparative-reasoning.md:19 — "Make a clear recommendation with explicit reasoning" -> "Make a clear recommendation and state a short rationale for it"
- rootnode-reasoning-blocks/references/comparative-reasoning.md:50 — "Recommend a selection with reasoning" -> "Recommend a selection and state a short rationale"
- rootnode-reasoning-blocks/references/strategic-reasoning.md:50 — "Recommend a specific allocation with reasoning" -> "Recommend a specific allocation and state a short rationale"
- rootnode-reasoning-blocks/references/technical-reasoning.md:19 — "Present your recommended architecture with clear reasoning for each major decision" -> "Present your recommended architecture and state a short rationale for each major decision"
Reviewed and left unchanged (task-specific analytical steps, allowed under Anthropic's guidance; no instruction to reproduce internal reasoning):
- analytical-reasoning.md:14 "State the core question you are answering before beginning analysis" (framing step in the deliverable, not a transcript of reasoning)
- analytical-reasoning.md step 4/6, comparative-reasoning.md:17, creative-reasoning.md:15, technical-reasoning.md:16 ("State the tradeoffs explicitly", "articulate ...") are analytical content steps
- SKILL.md:164 and :174 matched only the loose "step" scan ("not more reasoning steps", "steps beyond 7"); not instructions to show reasoning
Same-phrase duplicates outside the reasoning-blocks scope but inside this builder's writable set (prompt-compilation), rewritten for consistency:
- rootnode-prompt-compilation/references/five-layer-architecture.md:269 and compilation-examples.md:115 — "Make a clear recommendation with explicit reasoning" -> "... and state a short rationale"

## Landscape sweep (post-edit)
Command: grep -nE -e 'Opus 5\b' -e 'Sonnet 5\b' -e 'Haiku 4\.5' -e 'Fable 5\b' -e 'Opus 4\.8' over the 8 SKILL.md and 39 reference .md files (47 files). Note: `Opus 5\b` also matches "Opus 5.5", so lines carrying only current-generation names are listed as defect-fixed (text written to D2 this cycle).
Defects found by the sweep beyond the row-listed lines and fixed: body "Run on Opus 5 or Sonnet 5 (both default to `high` ...)" at global-audit:43, project-audit:41, prompt-compilation:51 (rewritten to the T3 wording); prompt-compilation:272 (row-listed, now "the 5.5 generation"); project-audit Dimension 6 "eight known behavioral tendencies" and "all eight tendencies" -> fifteen.
Taxonomy count sweep: no "fourteen" / "14-tendency" / "10-tendency" remains describing the behavioral taxonomy in the 47 files. Remaining "14" hits are repo-hygiene's 14 hygiene CATEGORIES (not the behavioral taxonomy; unchanged). skill-builder "10-tendency" -> "15-tendency" at SKILL.md:121, behavioral-validation.md:36 and :90, plus skills-spec.md:388 (same propagation miss, not in the row).
Per-hit classification (path:line — class — note):
rootnode-global-audit/SKILL.md:16 — defect-fixed — line carries only current-generation names (Opus 5.5 / Sonnet 5.5 matched by the literal regex); text written to D2 this cycle
rootnode-global-audit/SKILL.md:27 — defect-fixed — line carries only current-generation names (Opus 5.5 / Sonnet 5.5 matched by the literal regex); text written to D2 this cycle
rootnode-global-audit/SKILL.md:43 — defect-fixed — line carries only current-generation names (Opus 5.5 / Sonnet 5.5 matched by the literal regex); text written to D2 this cycle
rootnode-global-audit/SKILL.md:45 — fallback/legacy — 'Fallback-graceful on Opus 5 / Sonnet 5' (D2); 'Haiku 4.5 without extended thinking is out of scope' is the unchanged remainder per row (exclusion, not a supported-target claim); see open concern
rootnode-handoff-trigger-check/SKILL.md:30 — fallback/legacy — T1 template: 'Fallback-graceful on Opus 5 / Sonnet 5'
rootnode-handoff-trigger-check/SKILL.md:38 — fallback/legacy — Haiku 4.5 named only as the legacy 200K case (row: clause becomes legacy-only; D6 permitted)
rootnode-handoff-trigger-check/SKILL.md:42 — defect-fixed — line carries only current-generation names (Opus 5.5 / Sonnet 5.5 matched by the literal regex); text written to D2 this cycle
rootnode-handoff-trigger-check/SKILL.md:44 — fallback/legacy — Sonnet 5 tokenizer identity and Haiku 4.5 tokenizer comparison (row-mandated; D6 permitted)
rootnode-project-audit/SKILL.md:16 — defect-fixed — line carries only current-generation names (Opus 5.5 / Sonnet 5.5 matched by the literal regex); text written to D2 this cycle
rootnode-project-audit/SKILL.md:17 — defect-fixed — line carries only current-generation names (Opus 5.5 / Sonnet 5.5 matched by the literal regex); text written to D2 this cycle
rootnode-project-audit/SKILL.md:27 — defect-fixed — line carries only current-generation names (Opus 5.5 / Sonnet 5.5 matched by the literal regex); text written to D2 this cycle
rootnode-project-audit/SKILL.md:41 — defect-fixed — line carries only current-generation names (Opus 5.5 / Sonnet 5.5 matched by the literal regex); text written to D2 this cycle
rootnode-project-audit/SKILL.md:43 — fallback/legacy — same as global-audit:45
rootnode-prompt-compilation/SKILL.md:16 — defect-fixed — line carries only current-generation names (Opus 5.5 / Sonnet 5.5 matched by the literal regex); text written to D2 this cycle
rootnode-prompt-compilation/SKILL.md:27 — defect-fixed — line carries only current-generation names (Opus 5.5 / Sonnet 5.5 matched by the literal regex); text written to D2 this cycle
rootnode-prompt-compilation/SKILL.md:51 — defect-fixed — line carries only current-generation names (Opus 5.5 / Sonnet 5.5 matched by the literal regex); text written to D2 this cycle
rootnode-prompt-compilation/SKILL.md:53 — fallback/legacy — same as global-audit:45
rootnode-prompt-compilation/SKILL.md:134 — defect-fixed — line carries only current-generation names (Opus 5.5 / Sonnet 5.5 matched by the literal regex); text written to D2 this cycle
rootnode-prompt-compilation/SKILL.md:249 — defect-fixed — line carries only current-generation names (Opus 5.5 / Sonnet 5.5 matched by the literal regex); text written to D2 this cycle
rootnode-prompt-compilation/references/five-layer-architecture.md:281 — defect-fixed — line carries only current-generation names (Opus 5.5 / Sonnet 5.5 matched by the literal regex); text written to D2 this cycle
rootnode-prompt-compilation/references/five-layer-architecture.md:283 — defect-fixed — line carries only current-generation names (Opus 5.5 / Sonnet 5.5 matched by the literal regex); text written to D2 this cycle
rootnode-prompt-compilation/references/five-layer-architecture.md:293 — defect-fixed — line carries only current-generation names (Opus 5.5 / Sonnet 5.5 matched by the literal regex); text written to D2 this cycle
rootnode-prompt-validation/SKILL.md:26 — fallback/legacy — T2 template fallback clause
rootnode-prompt-validation/references/symptom-fix-map.md:147 — defect-fixed — line carries only current-generation names (Opus 5.5 / Sonnet 5.5 matched by the literal regex); text written to D2 this cycle
rootnode-prompt-validation/references/symptom-fix-map.md:151 — defect-fixed — line carries only current-generation names (Opus 5.5 / Sonnet 5.5 matched by the literal regex); text written to D2 this cycle
rootnode-prompt-validation/references/symptom-fix-map.md:157 — defect-fixed — line carries only current-generation names (Opus 5.5 / Sonnet 5.5 matched by the literal regex); text written to D2 this cycle
rootnode-prompt-validation/references/symptom-fix-map.md:176 — historical — 'Opus 5's automatic self-verification (tendency #11)'; row says line unchanged (self-consistency row); see open concern
rootnode-reasoning-blocks/SKILL.md:27 — fallback/legacy — T1 template: 'Fallback-graceful on Opus 5 / Sonnet 5'
rootnode-repo-hygiene/SKILL.md:29 — defect-fixed — line carries only current-generation names (Opus 5.5 / Sonnet 5.5 matched by the literal regex); text written to D2 this cycle
rootnode-skill-builder/SKILL.md:29 — fallback/legacy — T2 template fallback clause plus D9a grader fallback sentence (row-mandated)
rootnode-skill-builder/references/multi-environment-adaptation.md:34 — fallback/legacy — 'Opus 5 / Sonnet 5 valid fallback' grader clause (row-mandated)

Counts by class (lines): historical 1 / fallback-legacy 10 / defect-fixed 20 (31 literal-hit lines)

## Correction after orchestrator brief (D6 deletion)
Per the brief, the sentence "Haiku 4.5 without extended thinking is out of scope." was deleted (the README owns the out-of-scope list). The three hits below are reclassified: the Haiku 4.5 token no longer appears on these lines; the lines keep only "Fallback-graceful on Opus 5 / Sonnet 5" (fallback/legacy). The earlier notes for these lines that mention the "unchanged remainder" are superseded.
- rootnode-global-audit/SKILL.md:45 — defect-fixed — Haiku 4.5 out-of-scope sentence deleted
- rootnode-project-audit/SKILL.md:43 — defect-fixed — Haiku 4.5 out-of-scope sentence deleted
- rootnode-prompt-compilation/SKILL.md:53 — defect-fixed — Haiku 4.5 out-of-scope sentence deleted
Residual literal-hit lines are unchanged in count (31 lines); the Haiku 4.5 hits remaining are only the row-mandated legacy notes in handoff-trigger-check (SKILL.md:38, :44).

### sweep_C.md

# Landscape sweep — Builder-C (rootnode-cc-design 5.0.0)

Command (post-edit, working tree): `grep -rnE -e 'Opus 5\b' -e 'Sonnet 5\b' -e 'Haiku 4\.5' -e 'Fable 5\b' -e 'Opus 4\.8' rootnode-cc-design/`
Result: 13 hit lines.

Instrument note: `\b` matches between `5` and `.`, so `Opus 5\b` / `Sonnet 5\b` also hit every `Opus 5.5` / `Sonnet 5.5` mention. A strict re-run excluding a following `.digit` (Python `(Opus 5|Sonnet 5|Fable 5)(?![.\d])|Haiku 4\.5|Opus 4\.8`) returns only 2 lines with true prior-generation names: cc-delegation-patterns.md:42 and cc-environment-design-patterns.md:189. Lines whose only matches are 5.5-generation names get the extra class `current (regex artifact)`; they are compliant with D2 and need no action.

Pre-edit sweep on HEAD (`git grep` same regex): 3 hits — SKILL.md:24, cc-delegation-patterns.md:42, cc-delegation-patterns.md:48. All three were defects against D2 and were fixed (see below).

## Classification

- rootnode-cc-design/SKILL.md:25 — defect-fixed — calibration line replaced whole with the T3 template (was "Opus 5 or Sonnet 5 (both default to `high`)… Opus 4.8 fallback-graceful", line 24 pre-edit; moved to 25 because the description gained a line). Remaining matches are Opus 5.5 / Sonnet 5.5 only.
- rootnode-cc-design/references/cc-delegation-patterns.md:33 — current (regex artifact) — role-table Orchestrator row: Opus 5.5 / Fable 5.1.
- rootnode-cc-design/references/cc-delegation-patterns.md:35 — current (regex artifact) — Researcher row: Haiku 5.5 / Sonnet 5.5.
- rootnode-cc-design/references/cc-delegation-patterns.md:36 — current (regex artifact) — Builder row: Sonnet 5.5 / Opus 5.5.
- rootnode-cc-design/references/cc-delegation-patterns.md:37 — current (regex artifact) — Refuter row: Opus 5.5 or above.
- rootnode-cc-design/references/cc-delegation-patterns.md:38 — current (regex artifact) — Debugger row: Opus 5.5.
- rootnode-cc-design/references/cc-delegation-patterns.md:42 — fallback/legacy — residual true hits: "Opus 5" inside the Anthropic quotation ("matches or exceeds Opus 5 at `high`…", landscape §6) as the comparison baseline, and "Opus 5 / Sonnet 5 remain valid fallbacks; Sonnet 4.6 is legacy" (landscape §2/§3, D2). Pre-edit this line was a defect (Opus 5 at `high` as recommended default; Fable 5; Sonnet 5 primary) — rewritten per spec §3.
- rootnode-cc-design/references/cc-delegation-patterns.md:48 — defect-fixed — pre-edit "`thinking: disabled` … returns HTTP 400 on Opus 5" replaced per spec §3 (thinking non-disableable on Opus 5.5 / Sonnet 5.5 / Fable 5.1; Haiku 5.5 accepts `disabled` at ≤`high`). Remaining matches are 5.5 names only.
- rootnode-cc-design/references/cc-environment-design-patterns.md:189 — fallback/legacy — D6-permitted third-party `haiku` alias note ("may still resolve to Haiku 4.5; pin `claude-haiku-5-5` via `ANTHROPIC_DEFAULT_HAIKU_MODEL`"), landscape §2/§6.
- rootnode-cc-design/references/cc-prompt-design-patterns.md:249 — current (regex artifact) — early-stop countermeasure: Opus 5.5 / Sonnet 5.5 / Haiku 5.5 / Fable 5.1 guides.
- rootnode-cc-design/references/cc-prompt-design-patterns.md:256 — current (regex artifact) — "Sonnet 5.5 / Haiku 5.5 short form" label for the verbatim B2 block.
- rootnode-cc-design/references/cc-prompt-design-patterns.md:264 — current (regex artifact) — pointer to the Opus 5.5 unattended-runs block.
- rootnode-cc-design/references/cc-prompt-design-patterns.md:391 — current (regex artifact) — verbatim B1 block intro (Sonnet 5.5 / Haiku 5.5).

## Counts (summed from the list above)

- historical: 0
- fallback/legacy: 2 (delegation:42, environment:189)
- defect-fixed: 2 (SKILL.md:25, delegation:48)
- current (regex artifact): 9
- total: 13

No Haiku 4.5 calibration/degradation line remains (D6); the only Haiku 4.5 mention is the third-party alias note. `CLAUDE_CODE_DISABLE_WORKFLOWS` appears once (cc-delegation-patterns.md §5 cap table) and carries `[unverified on 2.1.30x — verify against the running version]` (landscape §7).

### sweep_D.md

# sweep_D — rootnode-behavioral-tuning landscape sweep (Builder-D, 2026-10-22)

Command (post-edit): `grep -nE -e 'Opus 5\b' -e 'Sonnet 5\b' -e 'Haiku 4\.5' -e 'Fable 5\b' -e 'Opus 4\.8' rootnode-behavioral-tuning/`
Broad result: 85 matching lines. `\b` also matches "Opus 5.5" / "Sonnet 5.5" / "Fable 5.1", so 80 of those lines carry only current-generation forms and are not classified.
Exact old-generation forms, found with `(Opus|Sonnet|Fable) 5(?![.\d])|Haiku 4\.5|Opus 4\.8`: 7 hits on 5 lines. Haiku 4.5, Opus 4.8, and Fable 5 have zero hits.

## Post-edit exact hits (classified)

- rootnode-behavioral-tuning/SKILL.md:27 [Opus 5] — fallback/legacy — T2 calibration template line (catalog spec §3.1), "fallback-graceful on Opus 5 / Sonnet 5" (landscape §2)
- rootnode-behavioral-tuning/SKILL.md:27 [Sonnet 5] — fallback/legacy — same line as above
- rootnode-behavioral-tuning/SKILL.md:422 [Opus 5] — historical — quoted Anthropic baseline comparison: Opus 5.5 at `medium` "matches or exceeds Opus 5 at `high`…" (landscape §6)
- rootnode-behavioral-tuning/references/countermeasure-templates.md:3 [Opus 5] — historical — "the v4.0 cycle (Opus 5 generation) refactored verbosity…"
- rootnode-behavioral-tuning/references/countermeasure-templates.md:499 [Opus 5] ×2 — historical — Section 11 rationale, verbatim v4.0-cycle quote attributed to "Anthropic's Opus 5 prompting guide (v4.0 cycle)"
- rootnode-behavioral-tuning/references/countermeasure-templates.md:747 [Opus 5] — historical — conservative-review literalism "Carried from the Opus 5 generation (not re-documented for 5.5)" (landscape §5 row: carried, not re-documented)

Counts by class: historical 5, fallback/legacy 2, defect-fixed 0 remaining.

## Pre-edit hits fixed (defect-fixed; no longer present in the working tree)

Pre-edit lines from HEAD `820e5c0`:
- SKILL.md: 26, 28, 103, 130, 156, 183, 209, 234, 256, 284, 311, 404, 412, 464 (14 lines)
- countermeasure-templates.md: 5, 7, 15, 23, 24, 25, 26, 302, 424, 425, 441, 443, 460, 473, 488, 490, 505, 524, 534, 536, 565, 567, 595, 597, 623, 645, 649, 659 (28 lines)

What was fixed:
- SKILL.md:26 calibration line: replaced whole with the T2 template. It removed Opus 5 / Sonnet 5 as primary, Haiku 4.5, and Opus 4.8.
- SKILL.md:28 "Version 2.0 — 10-tendency taxonomy, Opus 4.8 calibration": changed to "Version 5.0 — 15-tendency taxonomy, 5.5-generation calibration".
- SKILL.md:103–311 and 464: every "Claude Code (`high` default on Opus 5 / Sonnet 5)" line now reads "Claude Code (`medium` default on Opus 5.5 / Sonnet 5.5 / Haiku 5.5)". Example 3 (old line 464) moved to the reference.
- SKILL.md:404 "Anthropic's Opus 5 guidance recommends starting at the default `high`": replaced with the three API defaults (Opus 5.5 `medium`, Sonnet 5.5 `high`, Fable 5.1 `high`) and the quoted Opus 5.5-at-`medium` sentence.
- SKILL.md:412 self-application "(Opus 5 / Sonnet 5)": now "(Opus 5.5 / Sonnet 5.5)".
- Reference header lines 5 and 7: rewritten for the 5.5 cycle. Opus 5 now appears only as history, on line 3.
- Reference TOC lines 15 and 23–26, and section titles and bodies at 441–623 ("(Opus 5)", "Opus 5 verifies / expands / delegates / narrates…"): made model-neutral. Each section notes "added in the v4.0 cycle" as history.
- Reference lines 302 and 424–425 ("`high` (the Opus 5 / Sonnet 5 default)", "Opus 5 and Sonnet 5 default to `high` on the Claude API"): rewritten to the `medium` default with the apply-on-observation note and the three API defaults.
- Reference lines 645, 649, and 659 (thinking-disabled on Opus 5, the 400 at `xhigh`/`max`): narrowed to Haiku 5.5 only, plus Sonnet 5.5 `between_tools`, per spec §3 and §4 and landscape §4.1.

## Operator ruling — appended after PR open (2026-10-22)

The 7 Haiku 4.5 lines inside `rootnode-*/` (see "Haiku 4.5 mentions vs the gate's pass wording" above) are **confirmed as legacy clauses required by their catalog-spec §4 rows, not defects**. The session prompt's T1 pass wording ("the README `haiku`-alias pin line is the only Haiku 4.5 mention outside historical text") was stricter than revised D6, which drops Haiku 4.5 from the calibration templates and the README scope but does not forbid row-mandated legacy notes. T1 stands as PASS. Future landscape-gate wording should exempt row-mandated legacy clauses explicitly.

## Round 4 re-check — appended (2026-10-22)

After the operator-granted cc-design round 4 (spec items D8, A6, E3 + guard notes), T1 was re-run: **190** literal / **46** exact-form lines, unchanged. The cc-design exact-form lines are still `references/cc-delegation-patterns.md:42` and `references/cc-environment-design-patterns.md:189`, classified above. No new hits; defects remaining 0.
