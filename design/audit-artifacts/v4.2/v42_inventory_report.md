# rootnode-cc-design v4.2 — step 1 inventory + gate report

## Header

- **MM** = `b8db38cd769fc582f7799321179c7418c985c714`
- **SKILL.md LF-sha** = `0c0e5e4f18379765d5d5cc8535a66d154a07181edc85522c419bbe7bab4a3aaf`
- **metadata.version** = `4.1.0`
- **claude --version** = `2.1.136 (Claude Code)`; model ID = `claude-opus-4-7[1m]`
- **S5 total LF bytes** = **239,221** / 13 files (SKILL.md 36,751; refs 186,634; schema 17,436)

## Gate (D1–D9)

| Dim | Grade | Evidence |
|---|:-:|---|
| D1 | **WARN** | description YAML-parsed **1017/1024**, headroom 7 (0.7%) SKILL.md:3-17; body 241 lines OK; body tokens ~8588 vs ~5000 soft cap |
| D2 | PASS | verb triggers + 9 phrases + 4 negative triggers SKILL.md:4,10,13,234-237 |
| D3 | PASS | authority matrix, delegation arch, 7-layer rule, source discipline preserved |
| D4 | **WARN** | `references/cc-anti-patterns.md` **349 lines, NO TOC**; body-tokens overflow same as D1 |
| D5 | PASS | 6× "if available" soft cross-Skill refs SKILL.md:234-237, cc-anti-patterns.md:7 |
| D6 | PASS | verb-based desc; `disable-model-invocation` absent |
| D7 | note | §3.6 build-scaffolding leak: `metadata.original-source` ~1.2 KB narrative SKILL.md:23 |
| D8 | PASS | no leaks; delegation cap correctly at `settings.json`/frontmatter |
| D9a/b | not run | v4.2 step 4 |
| D9c | PASS | 14-tendency taxonomy: #3,#5,#10,#11,#12,#13 addressed; others irrelevant surface |

**D4 SKILL.md size limits enforced by repo:**

| Constraint | Source | Limit | Current | Headroom |
|---|---|---:|---:|---:|
| description YAML-parsed | SBD §3.1; rootnode-skill-builder/SKILL.md:45,113,214 | 1024 chars | 1017 | **7** |
| body lines | same | 500 | 241 | 259 |
| body tokens (soft) | skills-spec.md:197,411 | ~5000 | ~8588 | **−3588** |
| refs TOC | SBD §3.4; skills-spec.md:58 | >~300 lines | see above | — |

**Fixes:** D1-desc → extract trigger phrases to body table (`+`); D1/D4-body → extract SKILL.md:37-51 v4.0/v4.1 narrative to `cc-delegation-patterns.md`/`cc-methodology-patterns.md` (`+`); D4-refs → add TOC to `references/cc-anti-patterns.md` (neutral); D7 §3.6 → trim `metadata.original-source` narrative (`+`).

## Coverage

**Practices enumerated: 149** — CCEG §1–§9 numbered+bold (89), CCEG §10 quick ref (20), AEA §4 (15), AEA §5+subsub (8), AAP §2 [both] (3), AAP §4 CC (14).

**Count table by source × status:**

| Source | present | stale | absent | total |
|---|---:|---:|---:|---:|
| CCEG (§1–§9 + bold) | 81 | 2 | 6 | 89 |
| CCEG §10 quick ref | 18 | 1 | 1 | 20 |
| AEA §4 | 11 | 0 | 4 | 15 |
| AEA §5 | 5 | 0 | 3 | 8 |
| AAP §2 | 3 | 0 | 0 | 3 |
| AAP §4 | 14 | 0 | 0 | 14 |
| **Total** | **132** | **3** | **14** | **149** |

Sums from `SCRATCH/B_matrix.tsv`.

### Stale (3)

| ID | severity | evidence |
|---|---|---|
| CCEG-9-layer-fit | med | Skill has SKILL.md:120-122 runtime-tooling recommendation, but omits CCEG §9's "runtime Skills are thin governance over thick workflow systems" framing (GSD/Superpowers positioning). Skill's only workflow-system mention is SKILL.md:31 practitioner-consensus list. |
| CCEG-term | low | Skill uses "autonomous CC iteration" (SKILL.md:63) and "autonomous CC execution" (SKILL.md:122). CCEG-term canonicalizes "execution surface" and advises against baking "autonomous" into architectural framings. Skill's usage is runtime-mode descriptive (fits allowed use) — soft stale. |
| CCEG10-verify-instr-accum | med | CCEG §10 names "Verification-instruction accumulation (Opus 5)" as a CC anti-pattern; `cc-anti-patterns.md` catalog table (line 17-31) does not carry it as its own row. Content surfaces only implicitly via SKILL.md:41 verification-topology rule + cc-delegation-patterns.md. |

### Absent (14)

| ID | sev | evidence (search terms; NO HITS) |
|---|---|---|
| CCEG-8.1..8.5 Routines (5 rows) | high | `Routine\|scheduled\|cron\|daily-triad\|weekly-audit\|observation-before-action` — entire CCEG §8 surface missing |
| CCEG-1.4-thinking-400 | med | `thinking:disabled\|xhigh 400\|breaking change thinking` — Opus 5 400-error reminder not carried |
| CCEG10-conservative-literal | med | `conservative\|literalism\|report-everything` — Opus 5 conservative-review pattern not carried |
| AEA-4.3 lean-over-comprehensive | low | `lean over comprehensive\|start lean` |
| AEA-4.11 explain-the-why | low | `explain the why\|explain.*why.*calibration` |
| AEA-4.12 multi-environment | low | `multi-environment\|environment-adaptive` |
| AEA-4.13 multi-lens | low | `multi-lens\|self-referential validation` |
| AEA-5.4 cross-Skill-contracts parent | low | umbrella absent; children 5.4.1, 5.4.2 present via REMEDIATE |
| AEA-5.4.3 producer→consumer chain | low | `producer.*consumer\|consumer chain` |
| AEA-5.5 KF-propagation four-landing | low | `KF propagation\|four landing` (may be out-of-surface) |

### Present (ID lists only)

Full 132-row ID+`file:line` list in `SCRATCH/B_matrix.tsv`. Coverage summary:
- **CCEG §1–§9 + bold (81):** all §1.1–§1.7, §2.1–§2.4, §3.1–§3.5 (incl. 3.4-ultracode), §4, §5.1–§5.8 (incl. 5.7-end-state, 5.8-hypotheses), §6, §7.1–§7.3, §9; all §1.4 subagent bold rules; §1.1–§1.7 use-for/not-for pairs; §2.1 R1–R5, §2.2 W1–W3, §2.3 specificity+auto-memory; §4 3cats/auth-ground/4halt; §5 antipatterns and normalize.
- **CCEG §10 (18):** all except `conservative-literal` (absent) and `verify-instr-accum` (stale).
- **AEA §4 (11):** 4.1, 4.2, 4.4–4.10, 4.14, 4.15.
- **AEA §5 (5):** 5.1, 5.2, 5.3, 5.4.1, 5.4.2.
- **AAP §2 (3):** 2.1 explicit; 2.2 via SKILL.md:61; 2.3 via cc-anti-patterns.md:63.
- **AAP §4 (14):** 4.1–4.14 all as explicit cc-anti-patterns catalog rows 17-31.

## Route cost per mode

Route source: `SKILL.md:93-102`. SKILL.md (36,751 B) always loaded. Tokens EST = bytes ÷ 4.

| Mode | Files (mandatory) | LF bytes | Tokens EST |
|---|---|---:|---:|
| DESIGN | +methodology+env+skills-hooks+handoff | 109,868 | ~27,467 |
| DESIGN +opt cc-prompt | above +cc-prompt | 136,241 | ~34,060 |
| EVOLVE | +anti+methodology+(env OR skills-hooks) | 97,290–105,127 | ~24k–26k |
| RESEARCH | +source-grading+anti | 72,255 | ~18,063 |
| TEMPLATE | +methodology+1 CC ref | 59k–85k | ~15k–21k |
| REMEDIATE | +remediate-execution+anti+env+exec-plan schema | 112,507 | ~28,126 |

- **Largest reference:** `cc-prompt-design-patterns.md` = 26,373 B.
- **References with no Step 3 mode route:** `cc-delegation-patterns.md` (16,797 B — v4.1 headline; conditional-only via SKILL.md:134), `troubleshooting.md` (13,500 B), `schema/cc-design-brief.schema.json` (7,402 B).
- **Overlap (approx bytes duplicated into SKILL.md):** end-state rule ~800 (SKILL.md:108 ↔ cc-prompt-design-patterns.md:378); LF-normalize ~250 (same pair); ultracode ~350 (SKILL.md:107 ↔ cc-delegation-patterns.md:129,171); role-tier+B-to-R ~1200 (SKILL.md:47-51 ↔ cc-delegation-patterns.md); Explore v2.1.198 ~200; delegation cap ~800 (SKILL.md:39 ↔ cc-delegation-patterns.md §6); CC defaults ~400 (SKILL.md:29,43); pre-state troubleshooting ~350. **~4,650 B (~1,163 tokens) of SKILL.md is duplicated** — accounts for most of D1 body-tokens overflow.

## Open inputs (Part D)

- **D1 Builder Opus-tier switch:** **changed** — `cc-delegation-patterns.md:36` "Sonnet tier; Opus tier when the spec is hard" is prose only, no mechanism. Adjacent Scout row does cite one (`project Explore override`).
- **D2 Refuter non-fork invocation:** **resolved** — `cc-delegation-patterns.md:87,90,141` "spawn the Refuter fresh rather than as a fork." Prose-explicit; no bound config key.
- **D3 Orchestrator hygiene threshold:** **changed** — no single number. Numerics present: `cc-delegation-patterns.md:80` Anthropic 15,000-token subagent-description warning; §5 line 113 `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` default **20**; §3 line 64 return-length cap "is a number, not an adjective" (no default). Practice is qualitative discipline (§3 five rules).
- **D4 audit_references.py + cc-anti-patterns.md L7:** **confirmed** — 9 total MISSING repo-wide; **1 for rootnode-cc-design = `references/anti-pattern-catalog.md`** (cc-anti-patterns.md:7 cross-Skill cite to `rootnode-repo-hygiene`). Still false MISSING. **Resolution rule (scripts/audit_references.py:44-79):** regex `references/([A-Za-z0-9_\-./]+)`; leaf basename must exist in same Skill's own `references/` dir; no cross-Skill awareness.
- **D5 output length:** `C:\D9A\out-r3\arm1f3-B1.md` = **45,524 B**; `arm1f3-B3.md` = **29,098 B**; total **74,622 B**. Skill length rules bind only artifacts *inside* designed CC deployment (CLAUDE.md <200 lines at SKILL.md:164, cc-anti-patterns.md:49,51, cc-environment-design-patterns.md:83; designed SKILL.md body <500 at cc-skills-and-hooks-composition.md:105; delegation-brief "numeric length cap" at SKILL.md:109, cc-delegation-patterns.md:64). **No rule bounds Skill's own generation length.** OPT_REF #3c written-deliverable-length not carried.
- **D6 scratch/temp conventions:** `.gitignore` = `dist/`, `_v2_1_staging/`, `/scripts/`, `/design/skill-creator/`, `/design/staging-kf/`, `__pycache__/`, `*.pyc`. Catalog references only `design/staging-kf/`. On disk: `design/staging-kf/` (gitignored top-level) vs. `design/audit-artifacts/v4.2/scratch/` (cycle-nested, NOT gitignored). Two conventions; report only.

## Recommendations (from Parts A–D)

**high**
- Shrink SKILL.md description 1017→~800 chars; move trigger phrases into body route table. `+` — A/D1
- Extract SKILL.md:37-51 (v4.0/v4.1 update paragraphs) into `cc-delegation-patterns.md` and `cc-methodology-patterns.md`; leave 2-line routing surfaces. `+` — A/D1, A/D4, C
- Add TOC to `references/cc-anti-patterns.md` (349 lines, no TOC). `+` — A/D4
- Add CCEG §8 Routines coverage as new/folded reference. `+` — B/CCEG-8.1..5
- Route `cc-delegation-patterns.md` from DESIGN mode Step 3 explicitly. `neutral` — C

**med**
- Add CCEG §1.4 thinking:disabled xhigh→400 breaking-change reminder. `−` (small) — B/CCEG-1.4-thinking-400
- Add CCEG §10 "conservative-review literalism" as dedicated cc-anti-patterns entry. `neutral` — B/CCEG10-conservative-literal
- Add CCEG §10 "verification-instruction accumulation" as dedicated entry. `neutral` — B/CCEG10-verify-instr-accum
- Give Builder role-table row a mechanism (config/complexity signal/rule) replacing prose "when the spec is hard". `−` (small) — D/D1
- Add explicit written-deliverable length rule (OPT_REF #3c) to Skill. `neutral` — D/D5
- Trim `metadata.original-source` provenance narrative. `+` — A/D7
- Deduplicate SKILL.md↔reference content overlap (~4,650 B). `+` — A/D4, C
- Update CCEG-9 layer-fit framing (thin governance over thick workflow systems). `neutral` — B/CCEG-9-layer-fit
- Decide D3 hygiene threshold as number or ratify qualitative discipline explicitly. `neutral` — D/D3

**low**
- Add AEA §4.11 explain-the-why, §4.12 multi-env, §4.13 multi-lens, §4.3 lean-over-comprehensive to methodology. `−` — B/AEA-4.3, 4.11, 4.12, 4.13
- Add AEA §5.4 cross-Skill-contracts parent framing. `−` — B/AEA-5.4
- Add AEA §5.4.3 producer→consumer chain doc discipline. `neutral` — B/AEA-5.4.3
- Enumerate AEA §5.5 four-landing-location KF propagation or note out-of-surface. `neutral` — B/AEA-5.5
- Add AAP-2.2 and AAP-2.3 as dedicated cc-anti-patterns catalog rows (currently 15-pattern, AAP has 17). `neutral` — B/AAP-2.2, 2.3
- Carry SBD §3.9 D9a-arm-hygiene + validation-stopping-rule text into Skill D9 handling. `−` — A/D9c
- Soften "autonomous CC" surface framing at SKILL.md:63,122 per CCEG-term. `neutral` — B/CCEG-term

`+` = budget-positive (extracts from SKILL.md); `−` = budget-negative.

## Hot-reload (Part F)

**HOT-RELOAD CONFIRMED.**

Wrote `~/.claude/skills/zz-probe-hotreload/SKILL.md` mid-session (body: `When invoked, reply with exactly: HR-PROBE-7Q2X`). Invoked via `Skill{skill:"zz-probe-hotreload"}`; harness returned `Launching skill: zz-probe-hotreload` + base-dir line + SKILL.md body verbatim; assistant emitted sentinel `HR-PROBE-7Q2X`. Post-invocation system-reminder listing included `zz-probe-hotreload`; post-delete listing no longer contained it. **Applies only to `claude --version 2.1.136`.**
