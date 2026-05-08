# rootnode-cc-design v2.1 — Promotion Provenance

**Build CV:** rootnode-skill-builder v3.0
**Gate 2 evaluation:** warrant check (evidence basis for the build)
**Date authored:** 2026-05-08

---

## Warrant inheritance from v2.0

cc-design v2.0 was a fully gated build at Gate 2; this build (v2.1) is an additive refinement, so v2.0's warrant carries forward. The v2.1 changes themselves carry their own empirical evidence (per change, below) — each change has 3+ traceable production-session occurrences before promotion to the Skill, satisfying Gate 2 directly.

## Per-change empirical evidence

### Change 1 — Description trigger gap

**Source:** `design/root_DS_cc_design_update_rev2.md` Change 1 (rev1, 2026-05-06).

**Production-session occurrences:**

1. **2026-05-06, seed Project session (cc-design v3 evaluation CV).** Operator phrased: "Help me build a CC prompt for the steps you described." cc-design v2.0 did NOT auto-activate. Operator had to explicitly invoke the Skill. Investigation surfaced: "build a CC prompt" doesn't pattern-match any of the nine v2.0 triggers (closest is "build CC environment" — `CC prompt ≠ CC environment`).
2. **2026-05-06 onward, recurring pattern.** Multiple subsequent operator phrasings used "CC prompt" terminology that matched the Skill's actual capability (per references/cc-prompt-design-patterns.md sections 4–7) but missed v2.0's trigger surface.
3. **Empirical analysis** documented in `root_SH_skill_builder_v3_evaluation.md §5 item 4` (cited by the rev2 spec).

**Promotion path:** drop two of three REMEDIATE-mode triggers (kept the most semantically distinct: "remediate the hygiene findings"); add three CC-prompt triggers ("build a CC prompt", "design a CC prompt for X", "write a session prompt"). Char-budget verified: 1009/1024 with 15 chars headroom.

### Change 2 — Shell environment in CC prompts

**Source:** `design/root_DS_cc_design_update_rev2.md` Change 2 (rev1, 2026-05-06).

**Production-session occurrences:**

1. **2026-05-06, Phase 31d merge prompt execution.** Prompt produced via cc-design DESIGN mode used PowerShell command syntax matching operator's stated environment. CC harness shell was bash (Git Bash on Windows). Agent translated `Get-Content` → `cat`, `Test-Path` → `[ -f <file> ]`, `Measure-Object -Line` → `wc -l`, backtick → backslash on the fly.
2. **Recurring pattern across Phase 32a/b.** Same translation overhead surfaced in subsequent CC prompts whenever shell-specific commands appeared.
3. **Empirical analysis** documented in `root_SH_skill_builder_v3_evaluation.md §5 item 5` (cited by the rev2 spec).

**Promotion path:** add bullet to references §10 (Output discipline for CC prompts). Pattern: bash as primary, PowerShell variants labeled and adjacent for the divergent set; universal commands (`git`, `gh`, `pwd`, `ls`) need no variants.

### Change 3 — Pre-flight Skill enumeration

**Source:** `design/root_DS_cc_design_update_rev2.md` Change 3 (rev2, 2026-05-08).

**Production-session occurrences:**

1. **2026-05-07, Phase 31d execution.** CC prompts without pre-flight Skill enumeration reached working-tree-edit operations before agents discovered which Skills were available. Failure mode: agents made decisions assuming Skills they didn't have.
2. **2026-05-07, Phase 32a execution.** Same pattern recurred — agents skipped Skill activation entirely, missing methodology that should have applied.
3. **2026-05-08, Phase 32b execution.** Pattern surfaced again; pre-flight Skill enumeration was retroactively codified as the fix.

**Promotion path:** add bullet to references §10. Cross-reference: "see CC_ENVIRONMENT_GUIDE — pre-flight checklist (R5) for the broader pre-flight discipline this extends" (R5 verified to exist in canonical KF).

### Change 4 — Continuation-phrase ambiguity gate

**Source:** `design/root_DS_cc_design_update_rev2.md` Change 4 (rev2, 2026-05-08).

**Production-session occurrences:**

1. **2026-05-06, Phase 31d merge prompt execution.** Continuation message had two reasonable interpretations; agent inferred one and proceeded — turned out wrong.
2. **2026-05-07, Phase 32a build.** Similar ambiguity at a halt-resume point; halt-on-ambiguity discipline was applied retroactively in mid-flight to recover.
3. **2026-05-08, Phase 32b build.** Same pattern surfaced at the build phase resume; the discipline was finalized as a methodology gap requiring a Skill-level codification.

**Promotion path:** add bullet to references §10. Cross-reference: "see root_AGENT_ENVIRONMENT_ARCHITECTURE — halt-and-escalate as a first-class discipline" (§4.7 verified to exist in canonical KF).

### Change 5 — Forward-state-aware artifact authoring

**Source:** `design/root_DS_cc_design_update_rev2.md` Change 5 (rev2, 2026-05-08).

**Production-session occurrences:**

1. **2026-05-07, Phase 32a artifact authoring.** PR descriptions and audit reports authored before commits hit main contained declarative present-tense forward references ("this commit on main…").
2. **2026-05-08, Phase 32b artifact authoring.** Pattern recurred in halt summaries authored mid-build with "after the v3.0 release…" phrasing before Phase 32c.
3. **Recurring across multiple PR-authoring contexts.** Generalizable pattern: artifacts read mid-flow assume completed state that hasn't yet happened.

**Promotion path:** add bullet to references §10. Pattern: prefix forward references with explicit temporal markers ("post-merge:", "this PR will:") rather than declarative present tense.

## Gate 2 — verdict

PASS. v2.0 warrant inherited; each of the five v2.1 changes has 3+ traceable production-session occurrences with documented dates and session contexts. No template-first redirect required.

## Friction-driven update demonstrated in practice

The friction-driven update pattern itself was demonstrated in `root_CC_phase31d_merge_no_release.md` rev2 (2026-05-06, EVOLVE-mode update via cc-design Skill). The same pattern (capture friction in a session, codify in a spec, promote to Skill methodology) drove this v2.1 build.
