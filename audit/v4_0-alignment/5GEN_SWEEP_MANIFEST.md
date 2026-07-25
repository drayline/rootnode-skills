# 5-Generation Alignment — Sweep Manifest (Phase 0, rewritten for v2.0)

**Rewritten:** 2026-07-25 (session 2). Prior manifest superseded per design §8-W0 — its pattern set predated D4.
**Design doc:** `design/root_skill_5gen_alignment_design.md` v2.0.
**Session:** 5-gen alignment execution on `release/v4.0`.

**Pattern set (full v2.0):**

Carried from v1.3:
- `Opus recommended`, `non-Opus`
- `4\.6`, `4\.7`, `4\.8`, `Sonnet`, `Haiku`, `Fable`, `Opus` (in `rootnode-*/**/*.md`)
- `effort`, `xhigh`, `budget_tokens`, `extended thinking`, `tokenizer`, `200[Kk]`, `66,?500`, `1M`
- `> \*\*Calibration:\*\*` (SKILL.md tier markers), `Model Compatibility` (README)

New (D4 — verification-instruction discipline):
- `double-check`, `re-verify`, `verify your (own )?work`, `verification step`, `subagent to verify`, `check your answer`

New (D4 — conservative-instruction literalism):
- `high-severity`, `be conservative`, `only report`, `only flag`

New (Opus 5 landscape):
- `Opus 5`, `opus-5`, `Fast mode`, `max effort`, `prompt cach`

**Classification key:**
- (a) still-accurate
- (b) stale-fact → §1 landscape
- (c) stale-calibration → D1/D2 language
- (d) new content required per D1 integration floor
- (e) self-re-check → **remove** per D4
- (f) external-artifact verification → **keep**, confirm imperative voice per D4
- (REVIEW) — ambiguous, not batch-applied

---

## Class-A: Skill description-field lines carrying "Opus recommended; non-Opus models…" (D2 replacement target)

**Class:** (c). All require SBD §9 description refinement loop (truncation check, trigger preservation).

| File | Line | Excerpt (truncated) |
|---|---|---|
| `rootnode-prompt-compilation/SKILL.md` | 16 | `Opus recommended; non-Opus models may produce less complete prompt construction.` |
| `rootnode-global-audit/SKILL.md` | 16 | `available). Opus recommended; non-Opus models may produce less complete` |
| `rootnode-project-audit/SKILL.md` | 16 | `rootnode-memory-optimization if available). Opus recommended; non-Opus models` |
| `rootnode-context-budget/SKILL.md` | 16 | `rootnode-behavioral-tuning if available). Opus recommended; non-Opus models` |
| `rootnode-full-stack-audit/SKILL.md` | 16 | `available). Opus recommended; non-Opus models may produce less complete` |

Total: 5 SKILL.md descriptions carry the D2-target phrase. D2 new label: "High-effort recommended — run on Opus 5 or Sonnet 5. Both default to `high`, which is the recommended starting point; step up to `xhigh` for long-horizon agentic work. Quality degrades at `low` effort and on legacy models."

---

## Class-B: Inline `> **Calibration:**` markers on SKILL.md files

**Class:** all require D1/D2 rewrite (Opus-primary → dual-primary per new scope). Also: 6 Skills MISSING inline markers entirely (Design D2 mandates all 6 gain markers this cycle).

**21 present (all "Opus-primary" language):**

| File | Tier | Current label |
|---|---|---|
| rootnode-block-selection/SKILL.md | Tier 2 | Opus-primary |
| rootnode-anti-pattern-detection/SKILL.md | Tier 2 | Opus-primary |
| rootnode-behavioral-tuning/SKILL.md | Tier 2 | Opus-primary |
| rootnode-skill-builder/SKILL.md | Tier 2 | Opus-primary |
| rootnode-reasoning-blocks/SKILL.md | Tier 1 | Opus-primary |
| rootnode-prompt-validation/SKILL.md | Tier 2 | Opus-primary |
| rootnode-domain-software-engineering/SKILL.md | Tier 1 | Opus-primary |
| rootnode-global-audit/SKILL.md | Tier 3 | Opus-primary |
| rootnode-identity-blocks/SKILL.md | Tier 1 | Opus-primary |
| rootnode-session-handoff/SKILL.md | Tier 1 | broad-tier — "Built and calibrated for Opus 4.8; runs on Sonnet 4.6 and Haiku 4.5" |
| rootnode-domain-agentic-context/SKILL.md | Tier 1 | Opus-primary |
| rootnode-project-audit/SKILL.md | Tier 3 | Opus-primary |
| rootnode-context-budget/SKILL.md | Tier 3 | Opus-primary |
| rootnode-prompt-compilation/SKILL.md | Tier 3 | Opus-primary |
| rootnode-output-blocks/SKILL.md | Tier 1 | Opus-primary |
| rootnode-memory-optimization/SKILL.md | Tier 2 | Opus-primary |
| rootnode-full-stack-audit/SKILL.md | Tier 3 | Opus-primary |
| rootnode-domain-research-analysis/SKILL.md | Tier 1 | Opus-primary |
| rootnode-project-brief/SKILL.md | Tier 1 | Opus-primary |
| rootnode-domain-content-communications/SKILL.md | Tier 1 | Opus-primary |
| rootnode-domain-business-strategy/SKILL.md | Tier 1 | Opus-primary |

**6 missing markers (D2 mandates all 6):**

| File | Design status |
|---|---|
| rootnode-critic-gate/SKILL.md | D2: add marker (original 3) |
| rootnode-mode-router/SKILL.md | D2: add marker (original 3) |
| rootnode-repo-hygiene/SKILL.md | D2: add marker (original 3) |
| rootnode-cc-design/SKILL.md | D2: add marker (marker-gap Skill per §3 D2) |
| rootnode-handoff-trigger-check/SKILL.md | D2: add marker (marker-gap Skill per §3 D2) |
| rootnode-profile-builder/SKILL.md | D2: add marker (marker-gap Skill per §3 D2) |

---

## Class-C: `~66,500` RAG threshold references (V3 RESOLVED — D6 rebuild)

**Class:** (b)/(c) — D6 REBUILD confirmed. Anthropic Projects use automatic-RAG-by-window; the fixed threshold is a superseded mental model, not a stale-but-directional number.

| File | Hits |
|---|---|
| `audit/canonical-kfs/root_OPTIMIZATION_REFERENCE.md` | Multiple sections — full context-budget rebuild surface |
| `audit/canonical-kfs/root_SKILL_BUILD_DISCIPLINE.md` | 1 cross-reference |
| `rootnode-context-budget/SKILL.md` | 5+ (Step 4 budget calc, tier bands, budget-pool table) |
| `rootnode-context-budget/references/compression-execution.md` | 1 (~25% of ~66,500 heuristic) |
| `README.md` | 1 (context-budget row) |

Rebuild scope: replace fixed-threshold framing with automatic-by-window framing; preserve the distinction "context window ≠ RAG threshold" that the 200K era numerically entangled.

---

## Class-D: `4.6`, `4.7`, `4.8` model refs (calibration currency)

**Class:** requires triage — many are historical citations (legitimate context) vs current calibration statements (need update).

| Pattern | Total files | Top files |
|---|---|---|
| `4.7` | ~29 md files | OPT_REF (~45), 4_8_alignment_rubric (11 — historical, do not edit), design-5gen (many — current), status.md (13 — historical), release-notes (many — historical) |
| `4.6` | ~32 md files | design-5gen (many), 4_8_alignment_rubric (historical), OPT_REF, README |
| `4.8` | ~49 md files | rootnode-behavioral-tuning/SKILL.md (~23 — heaviest Skill user), CHANGELOG (historical), OPT_REF |

**Historical carve-outs (do not edit — Class-H):** `prompts/root_skill_4_8_alignment_rubric.md`, `audit/opus-4_8-alignment/*`, `release-notes/*-v3.1.md`, `design/audit-artifacts/v2.1/*, v3.0/*`, `audit/repo-catalog/*`.

Design v2.0 §4 D1 posture: Opus 4.8 is fallback-graceful (users are *silently served* it on classifier-flagged requests), so text should shift from "Opus 4.8 primary" to "Opus 5 + Sonnet 5 dual-primary; Opus 4.8 fallback-graceful" language — but Opus 4.8 references remain valid where the topic is fallback behavior.

---

## Class-E: Sonnet 5 + Opus 5 + Fable 5 additions (D1 integration floor — new content)

**Class:** (d) new content required. Every model-fact-bearing artifact must gain Opus 5-aware + Sonnet 5-aware + Fable-aware guidance.

**Model-fact-bearing artifact list (design §2 D1):**
- OPT_NOTES (surface as KF-update block AND now mirrored per D8 — new in v4.0 cycle)
- OPT_REF (in-repo canonical KF — full body recalibration per D6 + design §8-W1 step 2)
- behavioral-tuning
- cc-design
- domain-agentic-context
- domain-software-engineering
- prompt-compilation
- context-budget (rebuild per D6)
- README

Sub-scope items also touching model facts (from V7 sweep): handoff-trigger-check (token headroom math), skill-builder (grader guidance), session-handoff (model refs).

**Current in-catalog state:**
- Opus 5 refs: **0** (design + verification log excluded from catalog surface)
- Fable refs: **0** (unchanged since prior session)
- Fast mode / max effort / prompt cach: **0**

---

## Class-F: `effort` + effort-level references

**Class:** (c) stale-calibration — Opus 5 + Sonnet 5 effort defaults, level list, inverted starting-point rule.

149 hits across 38 files. Primary carriers: `rootnode-behavioral-tuning/SKILL.md` (~21), `rootnode-repo-hygiene/references/sweep-categories.md` (~21), `rootnode-skill-builder/SKILL.md` (~8), `rootnode-prompt-validation/SKILL.md` (~7), `rootnode-project-audit/SKILL.md` (~7), `rootnode-repo-hygiene/SKILL.md` (~6), `rootnode-conversion-guide.md` (~6), `rootnode-behavioral-tuning/references/countermeasure-templates.md` (~6).

All need:
- Opus 5 + Sonnet 5 default = `high` on Claude API and Claude Code
- Full ladder: `low` → `medium` → `high` → `xhigh` → `max`
- Inverted rule: `high` is the START (not `xhigh`); `xhigh`/`max` = step-up for demanding agentic work; `low`/`medium` = legitimate primary cost controls
- Opus 5 breaking change: `thinking: {"type": "disabled"}` at `xhigh`/`max` returns 400
- Re-run effort sweep rather than carry over settings from prior model

---

## Class-G: `1M` / `200K` context-window references

**Class:** (b) stale-fact — every current model except Haiku 4.5 is on 1M.

- `1M` design-only (many hits in design; near-zero in Skill catalog) — needs new content on the Skill side.
- `200K`/`200k` — 15+ hits across context-budget, OPT_REF, handoff-trigger-check/references, examples. All need re-context per current landscape (Haiku 4.5 = 200K; everything else current = 1M).

---

## Class-D4-verify: Verification-instruction patterns (D4 — remove/keep classification pending)

**Class:** (e) or (f) or (REVIEW) — determined per hit in Phase 2 W0. Do not batch-apply.

**30 occurrences across 17 files** (case-insensitive):

| File | Hits |
|---|---|
| `docs/root_SKILLS_RELEASE_PLAYBOOK.md` | 1 |
| `audit/canonical-kfs/root_AGENT_ANTI_PATTERNS.md` | 1 |
| `design/root_skill_5gen_alignment_design.md` | 3 (design doc — not a catalog target) |
| `rootnode-prompt-compilation/SKILL.md` | 1 |
| `rootnode-repo-hygiene/SKILL.md` | 2 |
| `rootnode-skill-builder/references/conversion-guide.md` | 1 |
| `rootnode-skill-builder/SKILL.md` | 1 |
| `rootnode-skill-builder/references/anti-pattern-catalog.md` | 2 |
| `rootnode-repo-hygiene/references/execution-discipline.md` | 8 |
| `rootnode-repo-hygiene/references/anti-pattern-catalog.md` | 1 |
| `rootnode-handoff-trigger-check/references/troubleshooting.md` | 2 |
| `rootnode-handoff-trigger-check/SKILL.md` | 1 |
| `rootnode-cc-design/references/cc-methodology-patterns.md` | 1 |
| `rootnode-prompt-validation/references/symptom-fix-map.md` | 2 |
| `rootnode-domain-agentic-context/references/reasoning-approaches.md` | 1 |
| `rootnode-prompt-compilation/references/five-layer-architecture.md` | 1 |
| `design/root_DS_skill_builder_v3_rev3.4.md` | 1 (design doc — not a catalog target) |

**Classification heuristic (per D4):**
- (e) REMOVE: "double-check your answer", "re-verify before responding", "include a final verification step", "use a subagent to verify your own work" — model-facing self-re-check instructions.
- (f) KEEP: "verify the file exists", "check the rendered page", "confirm the tag resolves", "diff the artifact against source", "verify against the source" — external-artifact evidence-grounding instructions. Confirm imperative voice.
- (REVIEW): phrasing that could be either; ambiguous scope; general audit/reviewer role guidance where the "verify" refers to human/other-agent review rather than self-review. Item-by-item disposition at HALT 2.

Highest concentration: `rootnode-repo-hygiene/references/execution-discipline.md` (8 hits) — needs careful line-by-line classification given the Skill's audit posture.

---

## Class-D4-conservative: Conservative-instruction literalism patterns (D4 — replace with report-everything-then-filter)

**Class:** (c) with a documented Opus 5 fix.

**9 occurrences across 8 files** (case-insensitive):

| File | Hits |
|---|---|
| `design/root_skill_5gen_alignment_design.md` | 2 (design doc — not a catalog target) |
| `rootnode-session-handoff/SKILL.md` | 1 |
| `rootnode-repo-hygiene/references/anti-pattern-catalog.md` | 1 |
| `rootnode-repo-hygiene/references/cc-best-practices.md` | 1 |
| `rootnode-cc-design/references/remediate-mode-execution.md` | 1 |
| `rootnode-context-budget/references/evaluation-rubric.md` | 1 |
| `rootnode-domain-agentic-context/references/reasoning-approaches.md` | 1 |
| `rootnode-domain-agentic-context/references/output-formats.md` | 1 |

**Fix per Opus 5 prompting guide:** "If your review prompt says 'only report high-severity issues' or 'be conservative,' the model may follow that instruction literally and report less; ask it to report everything and filter in a separate pass instead." Rewrite each hit to report-everything-then-filter form (or flag REVIEW if the context is not a review instruction).

---

## Class-H: Files touching pattern set but NOT in change surface (still-accurate carve-outs)

- `prompts/root_skill_4_8_alignment_rubric.md` — prior-cycle rubric, historical reference; DO NOT edit.
- `audit/opus-4_8-alignment/*` — completed prior cycle's artifacts, historical; DO NOT edit.
- `release-notes/*-v3.1.md` and earlier — historical release notes; DO NOT edit (already-shipped release notes are append-only).
- `design/audit-artifacts/v2.1/*, v3.0/*` — historical audit artifacts; DO NOT edit.
- `audit/repo-catalog/*` — repo catalog snapshots; DO NOT edit inside the release cycle (regenerated in playbook Phase B post-verification per playbook §2 step 10).
- `audit/canonical-kfs/root_AGENT_ANTI_PATTERNS.md` — canonical KF; design §5-W1 marks AAP as "grep-driven touch". Any touch classified before edit.
- `design/root_skill_5gen_alignment_design.md`, `design/root_DS_*.md` — design docs; not catalog surface.
- `audit/v4_0-alignment/5GEN_*.md` — session artifacts; not catalog surface.

---

## Sweep manifest classification summary

| Class | Files | Action |
|---|---|---|
| A | 5 SKILL.md descriptions | SBD §9 description refinement; D2 replacement label |
| B | 21 present + 6 missing = 27 total | Rewrite tier-marker line; add missing markers |
| C | 6 files | REBUILD per D6 (V3 confirmed) |
| D | 29+32+49 = up to ~50 unique md files across 4.6/4.7/4.8 | Triage historical vs calibration; update calibration statements to fallback-graceful/legacy-graceful language |
| E | 9+ model-fact-bearing artifacts | ADD Opus 5 + Sonnet 5 + Fable content per D1 floor (new content, not sweep) |
| F | 38 files | Opus 5 + Sonnet 5 effort default + level list + inverted starting-point rule + `thinking: disabled` 400 warning |
| G | 5+ files with 200K refs | Rebase to 1M-standard landscape (Haiku 4.5 = 200K exception) |
| D4-verify | 17 files (30 hits) | Per-hit remove/keep/REVIEW classification in Phase 2 W0 |
| D4-conservative | 8 files (9 hits) | Rewrite to report-everything-then-filter form |
| H | Everything historical | DO NOT EDIT |

Manifest is complete for Phase 0 purposes. Full per-line classification deferred to Phase 2 W0/W2 execution after HALT 0 unblocks.
