# kf-update-blocks — catalog v5.0 (5.5-generation alignment)

**Status:** SURFACED, not applied. Per repo CLAUDE.md halt #5 and *Knowledge-file change surfacing*, nothing here is written to `audit/canonical-kfs/`. Route: apply to the seed-Project KFs → stage to `design/staging-kf/` → sync to `audit/canonical-kfs/` in a separate mirror PR (v4.1 precedent).

**Sources:** catalog spec `design/root_DESIGN_catalog_v5_model_alignment.md` §3.5 (LF sha256 `1ccfb1a8fc3216b57c9856b7850aa77435e994e0c20010827cbb21429168706d`); cc-design spec `design/root_DESIGN_cc-design_v5.md` §12 (`0e6414802d93dc06c8e58fbde68381f799c3336b800f3dde14dd12d1d5c0431e`); behavioral-tuning spec `design/root_DESIGN_behavioral-tuning_v5.md` §9 (`fdb60955b8ebad5012ebbe31479b62896b409bb3ae836b3097fece32ef835cfb`); landscape block `design/root_MODEL_LANDSCAPE_2026-10.md` (`45515513126645bddfcd420c11870adcee91c2257124e88f124d99a680f28e70`).

**Format:** one block per row — target KF · action · block · rationale · source. Where two specs touch the same KF section, the blocks are listed together under that KF and both sources are cited.

---

## 1. root_CLAUDE_OPTIMIZATION_NOTES.md (mirror)

| # | Action | Block | Rationale | Source |
|---|---|---|---|---|
| 1.1 | REVISE | Replace the dated model-landscape block (2026-07-24/25, Opus 5 + Sonnet 5 dual-primary) with `root_MODEL_LANDSCAPE_2026-10.md` §1–§4 and §6, carried as a dated block with its "verify against the running Claude Code version" marker | The prior block's dual-primary, effort-default, and fallback claims are false on the 5.5 generation (landscape "What changed") | catalog §3.5; behavioral-tuning §9 |

## 2. root_OPTIMIZATION_REFERENCE.md (mirror)

| # | Action | Block | Rationale | Source |
|---|---|---|---|---|
| 2.1 | ADD | Tendency **#15 Early turn termination**: definition, deployment conditioning, countermeasure (the Anthropic "Keep working until…" block, verbatim, labeled turn-boundary, not self-verification), warrant (documented in the Opus 5.5, Sonnet 5.5, Haiku 5.5 and Fable 5.1 prompting guides; SBD §7.3 named-primary-source warrant) — text per behavioral-tuning spec §2 | Documented "too little" behavior with no home in #12 (too much) or #6 (search breadth) | catalog §3.5, D5; behavioral-tuning §2, §9 |
| 2.2 | REVISE | #7 tool-trigger miscalibration — fix direction flipped: from "stop over-calling" to "remove suppression language; add the search nudge; give the current date (Haiku)"; Fable 5.1 parallel-call variability as an API-surface facet | Landscape §5 rows "Tool-use suppression carried over" and "Parallel tool calling more variable" | catalog §3.5; behavioral-tuning §3, §9 |
| 2.3 | REVISE | #11 over-verification — REMOVAL shape extends to thinking instructions ("think carefully before answering", "re-verify earlier answers"); effort-conditioned reviewer-round facet at `xhigh`/`max` (Sonnet 5.5) | Landscape §5 rows "Thinking-instruction accumulation", "Self-started review rounds" | catalog §3.5; behavioral-tuning §3, §9 |
| 2.4 | REVISE | #12 scope expansion — unrequested-additions facet (tests, docs, refactors, supporting files; more at higher effort; open-ended "show me" requests start building) with the Anthropic second-paragraph block | Landscape §5 row "Unrequested additions" | catalog §3.5; behavioral-tuning §3, §9 |
| 2.5 | REVISE | #13 subagent over-delegation — effort-conditioned reviewer-subagent-launch facet with the one-paragraph Anthropic countermeasure (session cost ~⅓ lower at `max`, no quality change) | Landscape §5 row "Self-started review rounds and reviewer-subagent launches" | catalog §3.5; behavioral-tuning §3, §9 |
| 2.6 | REVISE | Facets on #3c (whole-file rewrites for small edits — token cost; draft-in-thinking-then-again at `xhigh`/`max`), #4 (v4.0 anti-list countermeasures can over-correct on Fable 5.1 — conditional "use lists when the content is multifaceted enough that they help" formulation), #5 (unmarked-quotation facet), #6 (inverse under-exploration note for Opus 5.5 multi-app workflows) | Landscape §5 rows "Denser prose…", "Whole-file rewrites", "Drafts deliverable in thinking", "Under-exploration" | behavioral-tuning §3, §9 |
| 2.7 | REVISE | Conditional-defect subsection: "thinking-disabled output artifacts" narrowed to Haiku 5.5 (the only current model that can disable thinking); conservative-review literalism kept | Landscape §4.1 and §5 row "Reasoning leaks into visible text" | catalog §3.5; behavioral-tuning §9 |
| 2.8 | REVISE | Deployment-conditioning tables rebuilt for the `medium`-default generation (analytical D9c from Anthropic's guides — marked unmeasured; Calibration Lab re-baselining carried) | Landscape §6 effort defaults; §7 open item | behavioral-tuning §4, §9 |
| 2.9 | REVISE | #6 over-exploration definition narrowed to search/exploration breadth; the "adds features beyond what was asked" symptom moves to #12 (template text unchanged) — prevents a #6/#12 routing collision now that #12 carries the unrequested-additions facet | Build-time routing decision in behavioral-tuning 5.0.0 (spec §2/§7 collision analysis); must reach the canonical taxonomy or the Skill and KF disagree | behavioral-tuning build (Builder-D return) |
| 2.10 | REVISE | #7b tool under-triggering — Claude Code conditioning value: LOW at `medium`, **MEDIUM at `low` or when tool-suppressing language is present** | Landscape §5 "Tool-use suppression carried over" row; conditional value added at build | behavioral-tuning build (Builder-D return) |
| 2.11 | ADD | Verbatim Anthropic blocks now carried in the Skill (operator directive, D5 standalone completeness): Opus 5.5 fully-unattended early-stop block (#15), "treat earlier answers as settled" (#11, chat only), explore-broadly (#6 inverse); Fable 5.1 "don't draft twice" (#3c), pre-existing-bug/extras block (#12), name-verification nudge (#7b) — each tagged `[Anthropic docs — <guide>, fetched 2026-10-22]`. OPT_REF should carry the same verbatim text, not pointers | Pointers are hidden dependencies on URLs that will move | operator directive 2026-10-22 |

## 3. root_AUDIT_FRAMEWORK.md (mirror)

| # | Action | Block | Rationale | Source |
|---|---|---|---|---|
| 3.1 | REVISE | Dimension 6 scores against the **15**-tendency taxonomy | Taxonomy count changed (2.1) | catalog §3.5; behavioral-tuning §9 |
| 3.2 | REVISE | "penalizes countermeasure sets calibrated for pre-Opus-5 models" → "pre-5.5 models" | Generation boundary moved | catalog §3.5 |

## 4. root_AGENT_ANTI_PATTERNS.md (mirror)

| # | Action | Block | Rationale | Source |
|---|---|---|---|---|
| 4.1 | REVISE | §6 pointer list: fourteen → fifteen | Taxonomy count | catalog §3.5; behavioral-tuning §9 |
| 4.2 | ADD | Three structural-catalog candidates, marked **not yet promoted**: (a) unbounded Stop hook; (b) exit-code enforcement-as-preference (a `command` hook that "enforces" with exit 1 is non-blocking — only exit 2 blocks); (c) two owners per rule | Surfaced by cc-design spec §7 (Delta F) and §2 (Delta A) | catalog §3.5; cc-design §12 |

## 5. root_CC_ENVIRONMENT_GUIDE.md (mirror)

| # | Action | Block | Rationale | Source |
|---|---|---|---|---|
| 5.1 | REVISE | §3.4 Claude Code defaults: Opus 5.5 default model (cited to the landscape block, not restated as a durable fact); effort default `medium` on the 5.5 trio; thinking non-disableable; the `thinking: disabled` → 400 rule now model-specific | Landscape §6 | catalog §3.5 |
| 5.2 | REVISE | §1.4 / §6 cap table: `CLAUDE_CODE_WORKFLOW_SUBAGENT_MODEL` (v2.1.296), Agent-tool `effort` parameter (v2.1.292), version markers on every `CLAUDE_CODE_*` name | Landscape §6 subagents bullet | catalog §3.5 |
| 5.3 | REVISE | §3.5 role table: model column — Haiku 5.5 as the Scout tier; cycle cap on Builder→Refuter loops; `status: blocked` ≠ empty findings | Landscape §1 Haiku 5.5 positioning; cc-design Delta D | catalog §3.5; cc-design §12 |
| 5.4 | REVISE | §3.3 brief fields 9–10 (content-bound brief: governing-spec digest; return contract) | cc-design Delta D | cc-design §12 |
| 5.5 | REVISE | §5.7 receipt freeze as an end-state corollary | cc-design Delta D | cc-design §12 |
| 5.6 | REVISE | §5.9 early-stop countermeasure cross-reference (to OPT_REF #15) | cc-design Delta E; behavioral-tuning #15 | cc-design §12 |
| 5.7 | REVISE | §6 hooks-vs-prompts worked example gains the exit-code contract (exit 2 blocks; exit 1 / other non-zero = non-blocking error; config shape `"matcher": "<string>"` + `"hooks": [{type, command, timeout}]`) and the bounded-Stop rule; the three-tier enforcement model (prompt / advisory check / blocking hook) | cc-design Delta A, Delta F; Anthropic hooks doc fetched 2026-10-22 | cc-design §12 |

## 6. root_SKILL_BUILD_DISCIPLINE.md (mirror)

| # | Action | Block | Rationale | Source |
|---|---|---|---|---|
| 6.1 | REVISE | §3.9 D9a grader models: Opus 5.5 or Sonnet 5.5 (Opus 5 / Sonnet 5 valid fallback); Haiku 5.5 a valid subject model, not a grader | Landscape §3 | catalog §3.5 |
| 6.2 | REVISE | D9c cites the 15-tendency taxonomy | Taxonomy count | catalog §3.5 |

## 7. AEA (architecture / execution-approach KF — section §4.14)

| # | Action | Block | Rationale | Source |
|---|---|---|---|---|
| 7.1 | REVISE | §4.14 keep-and-imperative class: the Anthropic "run a real check that exercises the change before reporting it done" block (Sonnet 5.5 / Haiku 5.5 guides, verbatim) as the canonical external-verification template; the "Keep working until…" block as the canonical non-self-verification continuation | Both blocks are external-artifact / turn-boundary instructions; tagging them prevents D7 false positives | cc-design §12; catalog §6 (D7 watch item) |

## 8. root_build_context.md (seed only)

| # | Action | Block | Rationale | Source |
|---|---|---|---|---|
| 8.1 | ADD | Phase entry for the v5.0 cycle (5.5-generation alignment; 27 Skills → 5.0.0; cc-design and behavioral-tuning structural; KF blocks surfaced here) | Cycle record | catalog §3.5 |
| 8.2 | ADD | Observation candidate **O28**: a Skill's own hook examples were enforcement-as-preference for two major versions because the exit-code claim was never verified against the artifact — a stale-proxy instance (checked against memory of the docs, not the docs) | Delta A root cause | catalog §3.5; cc-design §12 |
| 8.3 | ADD | Observation candidate **O29**: a reference-file "addendum" not mirrored onto the SKILL.md routing surface is unreachable in practice; v4.0 added four tendencies behavioral-tuning could not route to for one full cycle (O26 applied to progressive disclosure) | behavioral-tuning §1 defect | behavioral-tuning §9 |

## 9. CI `<knowledge_files>` (seed-Project Custom Instructions)

| # | Action | Block | Rationale | Source |
|---|---|---|---|---|
| 9.1 | REVISE | First trigger: counts fourteen → fifteen; "pre-Opus-5" → "pre-5.5"; CLAUDE_OPTIMIZATION_NOTES description's landscape date → 2026-10-22 | Propagation of 1.1, 2.1, 3.2 | catalog §3.5 |

## 10. Not applicable

| Target | Action | Rationale | Source |
|---|---|---|---|
| global `~/.claude/CLAUDE.md` | NOT APPLICABLE | Model-landscape facts fail the AEA §5.5 universality test by definition (§4.15) | catalog §3.5 |

---

Block count: §1 = 1, §2 = 11, §3 = 2, §4 = 2, §5 = 7, §6 = 2, §7 = 1, §8 = 3, §9 = 1 → 1 + 11 + 2 + 2 + 7 + 2 + 1 + 3 + 1 = **30 surfaced blocks** across 9 targets (+1 NOT APPLICABLE row).
