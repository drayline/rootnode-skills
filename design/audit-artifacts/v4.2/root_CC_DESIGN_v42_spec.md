# rootnode-cc-design v4.2 — design specification

**Input:** v42_inventory_report.md (step 1) + root_CC_LANDSCAPE_20260911.md (step 2 sweep)
**Constraint:** description headroom is 7 chars; body tokens ~8,588 vs ~5,000 soft cap. Extraction precedes addition.
**Version:** 4.1.0 → 4.2.0 (minor: new reference content, routing changes, coverage additions, no methodology rework)

---

## 1. Budget plan

### Phase A — Extract (create headroom)

| ID | Operation | Target | Savings |
|---|---|---|---|
| A1 | Shrink description from 1017 to ≤850 chars | SKILL.md:3-17 | ~170 chars headroom |
| A2 | Extract SKILL.md:37-51 (v4.0 + v4.1 update sections) into references | SKILL.md body | ~1,200 B / ~300 tokens |
| A3 | Trim `metadata.original-source` narrative | SKILL.md:23 | ~1,200 B / ~300 tokens |
| A4 | Deduplicate SKILL.md↔reference overlap | SKILL.md body | ~4,650 B / ~1,163 tokens |

**Projected body-token result:** ~8,588 − ~1,763 = ~6,825 tokens. Still over the ~5,000 soft cap but within reasonable range. Further reduction would cut methodology content, which is the wrong tradeoff.

### Phase B — Add (use headroom)

All additions go into reference files, not SKILL.md body. Body impact limited to routing lines.

---

## 2. SKILL.md changes

### 2.1 Description (A1)

**Current:** 1017 chars, 15 lines. Contains inline trigger phrases ("Use when user says...") and inline negative triggers ("Do NOT use...").

**Design:** Extract the trigger-phrase list and negative-trigger list out of the description into the body's existing routing table or a new "Activation" section. The description retains only the functional summary and mode list. Target: ≤850 chars.

Rewritten description structure (content, not final copy — CC writes final):
```
Line 1: What it does (one sentence)
Line 2: What it produces (artifact list)
Line 3: Five modes (one sentence)
Line 4-5: Primary negative triggers (2 lines max)
```

The current trigger phrases ("design CC for X", "build CC environment", etc.) move into a `## Activation` table in the body, between the calibration block and the first H2. This is the pattern used by rootnode-prompt-compilation (description 812 chars, triggers in body).

### 2.2 Body extraction (A2)

**Lines 37-51** contain two update sections ("v4.0 update" and "v4.1 update") that are changelog narrative, not routing logic. They duplicate content already in references:

- v4.0 subagent-delegation caps → already in `cc-delegation-patterns.md` §6
- v4.0 verification topology → already in `cc-delegation-patterns.md` and `cc-methodology-patterns.md`
- v4.0 CC defaults → already in `cc-delegation-patterns.md`
- v4.0 model selection tradeoff → routing-only, not methodology
- v4.1 delegation architecture → already in `cc-delegation-patterns.md`

**Replace lines 37-51 with a 2-line routing surface:**
```markdown
## Delegation architecture
See `references/cc-delegation-patterns.md` for the role table, delegation briefs, Builder-to-Refuter loop, cap mechanisms, and the orchestrator/worker model. See `references/cc-methodology-patterns.md` for the verification topology and the agent-warranted test.
```

### 2.3 Metadata trim (A3)

**Line 23** (`original-source`) is ~1,200 bytes of provenance narrative. The provenance function is served by `metadata.predecessor` plus the repo's git history. Replace with a one-line summary: the KF sources and the version lineage, ≤150 chars.

### 2.4 Deduplication (A4)

The report identified ~4,650 bytes of SKILL.md body duplicated into references. Deduplicate by replacing inline content with pointer sentences to the reference that carries the full text. Key overlaps:

| SKILL.md location | Duplicated into | Action |
|---|---|---|
| :108 end-state rule (~800 B) | cc-prompt-design-patterns.md:378 | Keep in reference, replace SKILL.md with 1-line pointer at Step 4 |
| :108 LF-normalize (~250 B) | same | Fold into the pointer |
| :107 ultracode (~350 B) | cc-delegation-patterns.md:129,171 | Keep in reference, pointer in Step 4 |
| :47-51 role-tier + B-to-R (~1,200 B) | cc-delegation-patterns.md | Removed by A2 |
| :39 delegation cap (~800 B) | cc-delegation-patterns.md | Removed by A2 |
| :29,43 CC defaults (~400 B) | cc-delegation-patterns.md | Removed by A2 |

After A2, the remaining dedup target is ~1,400 B in Step 4 (lines 103-112). Replace the inline rules with pointer sentences to the references that carry them. Step 4 keeps the rule *names* and the "non-negotiable" marker but not the rule *bodies*.

---

## 3. Route map fix

### 3.1 Route cc-delegation-patterns.md from modes (H5)

**Current:** `cc-delegation-patterns.md` appears in the reference table (line 134) but NOT in any mode's "consults:" list (lines 97-101).

**Fix:** Add to DESIGN mode consults (conditional: "if the deployment plan involves subagents, model tiering, parallel work, or delegation caps"). Add to EVOLVE mode consults (conditional: "when friction involves delegation, context bloat, or subagent behavior").

### 3.2 Verify all mode→reference mappings are consistent

The reference table (lines 130-141) and the Step 3 mode lists (lines 97-101) must name the same files. After adding cc-delegation-patterns.md, verify no other reference is in the table but absent from modes.

---

## 4. Coverage additions (reference files)

### 4.1 Routines coverage (H4) — HIGH

**Gap:** CCEG §8 entirely absent (5 rows: §8.1-§8.5).

**Design:** Add a new section to `references/cc-methodology-patterns.md` titled "## Routines as a CC deployment surface" (preferred over a standalone reference because Routines are a deployment pattern, not a new file-class). Content from the landscape sweep §1:

- Three trigger types (scheduled, API, GitHub) and their combination model
- Cloud vs local distinction (Routines vs Desktop scheduled tasks vs /loop)
- Design considerations: no permission prompts, full session with Skills and connectors, daily limits per plan tier, self-hosted environment support
- When to recommend: unattended repeatable work tied to a clear outcome; distinguish from session-scoped polling (/loop) and from Desktop scheduled tasks
- Version-stability note: Routines are in research preview, API surface may change

Body routing: add one line to the "Important" or "Step 6" section noting that for scheduled/automated CC deployments, consult the Routines section in cc-methodology-patterns.md.

### 4.2 Anti-pattern additions (M2, M3) — MED

Add two rows to `cc-anti-patterns.md`:

| Canonical reference | Name | Source |
|---|---|---|
| `root_CC_ENVIRONMENT_GUIDE.md §10` | Verification-instruction accumulation | CCEG §10; the pattern where self-verification instructions accumulate across evolution cycles |
| `root_CC_ENVIRONMENT_GUIDE.md §10` | Conservative-review literalism | CCEG §10; "only report high-severity" causes under-reporting by current models |

Each gets a structural signature, cause, and fix section following the existing catalog format. The catalog grows from 15 to 17 entries. Update the catalog table and the opening paragraph count.

### 4.3 TOC for cc-anti-patterns.md (H3)

Add a table of contents after the opening paragraphs (after line 9, before "## Catalog"). Standard markdown TOC linking to each `## §X.Y` section. Required by SBD §3.4 for references >~300 lines.

### 4.4 Thinking:disabled reminder (M1)

Add to `cc-delegation-patterns.md` or `cc-environment-design-patterns.md` (wherever effort/model defaults live): a note that `thinking: disabled` at `xhigh` or `max` returns 400 on Opus 5. This is a breaking-change reminder, not a new pattern. One sentence with version tag.

### 4.5 Written-deliverable length rule (M5)

Add to the Step 4 output standards: a rule that bounds the Skill's own generated output length per OPT_REF #3c (the written-deliverable-length surface of the verbosity tendency). One sentence: "When the deliverable is a design document, CLAUDE.md draft, or session prompt, target ≤N lines / ≤M KB unless the user requests exhaustive coverage." Concrete numbers TBD by CC at build time based on the report's D5 measurements (B1 output was 45 KB, B3 was 29 KB).

### 4.6 Layer-fit framing update (M8)

Update the runtime-tooling recommendation (SKILL.md:120-122 area, Step 6) to include CCEG §9's "runtime Skills are thin governance over thick workflow systems" framing. One sentence addition.

### 4.7 Builder tier-switch mechanism (M4)

In `cc-delegation-patterns.md`, the Builder row currently says "Sonnet tier; Opus tier when the spec is hard" — prose only, no mechanism. From the landscape sweep: the mechanism is `CLAUDE_CODE_SUBAGENT_MODEL` (or `_FORCE=1` for blanket override), or per-invocation `model` parameter, or frontmatter `model` field. Replace the prose with the config path. Mark the variable names with minimum-version tags.

### 4.8 Orchestrator hygiene threshold (M9)

The report says no single number exists. Ratify the qualitative discipline explicitly: "No fixed threshold. Practice is: return locations rather than contents, scratch-file handoff for oversized results, and numeric return cap in every delegation brief." Add as a note in the delegation-brief section of `cc-delegation-patterns.md`.

### 4.9 Orchestration taxonomy (from sweep)

Add a brief taxonomy section to `cc-delegation-patterns.md` distinguishing the three CC orchestration primitives:

| Primitive | Scope | Isolation | Limits |
|---|---|---|---|
| Subagents | Single session, in-process | Own context window; optional worktree | Concurrency, depth, per-session caps |
| Agent teams | Multiple sessions, team lead coordinates | Separate CC processes (split-pane or worktree) | Own limits, not subagent caps |
| Dynamic workflows | JavaScript-orchestrated, deterministic control flow | Script holds the loop; subagents do the work | Own limits; Workflow tool removed from subagent pools |

This grounds the Skill's delegation patterns in the full platform surface. 2-3 paragraphs. Mark as dated landscape content per AEA §4.15.

### 4.10 Version-annotation convention (from sweep §9)

Every `CLAUDE_CODE_*` variable the Skill names carries a minimum-version annotation: `(v2.1.NNN+)`. This is a cross-cutting pass across cc-delegation-patterns.md and any other reference that names settings. The sweep §9 table provides the version data.

---

## 5. Low-priority items — deferred to v4.3

| ID | Item | Reason for deferral |
|---|---|---|
| L1-L4 | AEA §4.3, 4.11, 4.12, 4.13 | Low severity; budget-negative; these are general principles, not CC-specific patterns |
| L5-L7 | AEA §5.4 parent, §5.4.3, §5.5 | Out-of-surface (KF propagation is a seed-Project concern, not a CC-design concern) |
| L8-L9 | AAP-2.2, 2.3 as dedicated catalog rows | Currently covered implicitly; explicit promotion after the catalog stabilizes at 17 |
| L10 | SBD §3.9 D9a arm-hygiene text | Already practiced; the Skill teaches CC design, not Skill testing |
| L11 | Soften "autonomous CC" framing | Soft stale; CCEG-term allows runtime-mode descriptive use |
| D5 (report) | Cycle artifact tracking convention | Repo-structure question, not Skill content |
| D6 (report) | audit/ vs design/ path rule | Same |
| D7 (report) | Scratch-file path convention | Same |

---

## 6. KF Deltas

### KF Delta 6 — root_build_context.md, Observation 27

**Action:** REVISE. Drop instance (1) (Test A mid-session-install confound) and its "Skills load at launch" premise. Keep instances (2) and (3) and the rule. Add: "A hot-reload probe on Claude Code 2.1.136 confirmed that a Skill installed mid-session can be invoked in that session; the earlier launch-only premise was itself an unverified mechanism claim, which is the observation's own failure mode."

**Propagation:** seed KF only (no mirror for build_context).

### KF Delta 7 — root_SKILL_BUILD_DISCIPLINE.md §3.9, D9a arm hygiene

**Action:** REVISE. Keep "install each arm's Skill into its project before launching the generation session" as practice. Replace the "Skills load at launch" reason with: "hot-reload is confirmed on Claude Code 2.1.136, but installing before launch removes the question from the run."

**Propagation:** seed KF + mirror at `audit/canonical-kfs/root_SKILL_BUILD_DISCIPLINE.md`.

### KF Delta 8 — root_CUSTOM_INSTRUCTIONS.md, build_context description

**Action:** REVISE. The Observation 27 clause currently ends "(Skills load at launch)". Drop that parenthetical.

**Propagation:** CI paste only.

### KF Delta 9 — root_SKILLS_RELEASE_PLAYBOOK.md

**Action:** ADD. Record the single-Skill cut as a supported release shape (D28): per-Skill release only, no umbrella, Latest unchanged, and the conditions under which it applies (one Skill's minor release, no cross-Skill dependencies, no README link breakage).

**Propagation:** seed KF only (no mirror for playbook).

### KF Delta 10 — root_CC_ENVIRONMENT_GUIDE.md, new §5.9 or appended to §5

**Action:** ADD. The turn-economy rule: a multi-phase CC prompt runs end to end and halts only at genuine operator gates. A halt whose only purpose is letting chat read a report and hand back the next paste is a design defect. Applies to session prompts, not to CLAUDE.md standing context.

**Propagation:** seed KF + mirror at `audit/canonical-kfs/root_CC_ENVIRONMENT_GUIDE.md`.

---

## 7. Build and test plan

### 7.1 CC prompt structure

One prompt, running end to end per the turn-economy contract (D32). Phases:

1. **Setup.** Branch `feat/cc-design-v4.2-build` from main tip. Report MM SHA.
2. **Phase A — Extract.** A1-A4 in order. Commit after each.
3. **Phase B — Add.** B items (§4.1-4.10 above) grouped by target file. Commit after each file.
4. **Phase C — Route map.** Fix mode→reference mappings. Commit.
5. **Phase D — Quality gate.** Run D1-D8 self-check. Report description char count, body line count, body token estimate, and any new D4 warnings.
6. **Halt for operator review.** Report the diff summary and the quality-gate results. Operator approves or requests changes.
7. **Phase E — KF Deltas 6-10.** Apply all five. For Delta 7 and 10, stage the mirror copies. Commit.
8. **Version bump.** `metadata.version` → `4.2.0`.

### 7.2 Test pass

D9a test is step 4 in the continuation plan. Separate prompt. One test pass, one fix pass, then ship (D24).

**Open item 1 resolution:** The test arm installs the v4.2 Skill before launch (arm hygiene). If Aaron's CC is still 2.1.136, the test accepts that version-gated features (v2.1.198+ behaviors) are untestable on this version and marks them so. The Skill's version annotations carry this forward — a user on an older CC version sees which features require upgrade.

### 7.3 Acceptance bar

Same as v4.1: quality, contains all of our best practices for CC design, and token-usage conscious. The delta from v4.1 is coverage (14 absent → 0 or near-0) and budget (body tokens from ~8,588 toward ~6,825).
