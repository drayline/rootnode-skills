# root_DS_cc_design_update.md (rev2)

**Target Skill:** rootnode-cc-design (currently v2.0)
**Update type:** Description Refinement Loop pass + DESIGN-mode output checklist additions (5 bullets)
**Source:** Empirical evidence captured during seed Project sessions 2026-05-06 and 2026-05-08 (v3.0 build execution)
**Consumer:** v3 skill-builder build pass when invoked against rootnode-cc-design

**Revision history:**
- rev1 (2026-05-06): Two changes — description trigger gap + shell-agnostic command syntax bullet
- rev2 (2026-05-08): Added three DESIGN-mode bullets reflecting Phase 32 execution learnings — pre-flight Skill enumeration, continuation-phrase ambiguity gate, forward-state-aware authoring. All five output checklist bullets ship together.

---

## Purpose

This document specifies five targeted updates to the `rootnode-cc-design` Skill: one description refinement (Change 1) and four DESIGN-mode output checklist additions (Changes 2–5). All are empirically tested in production sessions, not theoretical refinements.

The five updates are independent and could be applied separately, but they're packaged together because they emerged from the same root cause family — cc-design's DESIGN-mode output discipline lacks several explicit standards that show up empirically as friction during CC prompt execution.

---

## Change 1 — Description trigger gap

### Current state

The `rootnode-cc-design` SKILL.md frontmatter description (currently sits at ~950–1000 chars against the 1024 ceiling) enumerates these triggers:

> "Use when user says 'design CC for X', 'build CC environment', 'design CLAUDE.md', 'we hit X friction in CC', 'should we adopt Y for CC', 'give me a CLAUDE.md skeleton', 'remediate the hygiene findings', 'fix the audit issues', 'close the loop on the report'."

Nine triggers total. Three of them are REMEDIATE-mode specific ("remediate the hygiene findings", "fix the audit issues", "close the loop on the report"). Zero of them cover CC-prompt-specific phrasings.

### Empirical evidence

In a seed Project session on 2026-05-06, the operator phrased: **"Help me build a CC prompt for the steps you described."**

The Skill did NOT auto-activate. The operator had to explicitly invoke it. Investigation surfaced the cause: "build a CC prompt" doesn't pattern-match any of the nine listed triggers — the closest is "build CC environment," but "CC prompt" ≠ "CC environment." The Skill handles CC prompts (per `cc-prompt-design-patterns.md` reference and the modes table's explicit "initial prompt" / "session prompt" outputs), but the trigger language doesn't advertise this capability surface.

This is a classification gap between the Skill's actual capability surface and its description's auto-activation evidence.

### Recommended change

**Drop:** Two of three REMEDIATE-mode triggers. Keep one (recommended: "remediate the hygiene findings"). Rationale: three triggers for one mode over-weights the description toward REMEDIATE; the kept trigger is the most semantically distinct.

**Add:** Three CC-prompt-specific triggers:
- "build a CC prompt"
- "design a CC prompt for X"
- "write a session prompt"

### Before / After

**Before (current):**

> "Use when user says 'design CC for X', 'build CC environment', 'design CLAUDE.md', 'we hit X friction in CC', 'should we adopt Y for CC', 'give me a CLAUDE.md skeleton', 'remediate the hygiene findings', 'fix the audit issues', 'close the loop on the report'."

**After (recommended):**

> "Use when user says 'design CC for X', 'build CC environment', 'design CLAUDE.md', 'build a CC prompt', 'design a CC prompt for X', 'write a session prompt', 'we hit X friction in CC', 'should we adopt Y for CC', 'give me a CLAUDE.md skeleton', 'remediate the hygiene findings'."

### Char budget analysis

- Dropped: "fix the audit issues" (~22 chars including separator), "close the loop on the report" (~31 chars including separator) = ~53 chars freed
- Added: "build a CC prompt" (~21), "design a CC prompt for X" (~28), "write a session prompt" (~26) = ~75 chars added
- Net delta: approximately +22 chars

If the current description is at ~970 chars, post-change is ~992 — still under the 1024 ceiling with ~32 chars of headroom. If the current description is closer to the upper end (~1010+), the audit pass should drop one additional redundant phrase from elsewhere in the description to maintain headroom (target: stay below ~990 chars after the change).

### Apply during audit pass

When the v3 skill-builder audit pass reaches `rootnode-cc-design`, run the Description Refinement Loop on this Skill specifically and apply the trigger consolidation as part of the loop's output. Verify post-change char count via the Skill's frontmatter YAML parser; halt if it exceeds 1024.

---

## Change 2 — DESIGN-mode output checklist addition (shell-agnostic command syntax)

### Current state

The `rootnode-cc-design` Skill's DESIGN-mode output (CC prompts, CLAUDE.md drafts, session prompts) doesn't require shell-agnostic command syntax. CC prompts are produced with whatever shell syntax the prompt author was thinking about — typically the operator's local environment.

### Empirical evidence

In a seed Project session on 2026-05-06, a Phase 31d merge CC prompt was produced via cc-design DESIGN mode. The prompt's command blocks defaulted to PowerShell syntax (matching the operator's stated environment per User Preferences: "Windows/PowerShell environment").

When the prompt ran in CC, the harness's actual shell was **bash (Git Bash on Windows)** — not PowerShell. The agent translated PowerShell-only commands on the fly:
- `Get-Content` → `cat`
- `Test-Path` → `[ -f <file> ]`
- `Measure-Object -Line` → `wc -l`
- Backtick line continuation → backslash line continuation

The translation worked correctly, but it relied on agent judgment, created inconsistency in execution logs, and could fail silently for less-obvious command divergences. The root cause: the prompt author (Claude) defaulted to PowerShell because the operator's local environment was PowerShell; but the CC harness's runtime shell is independent of the operator's local shell.

### Recommended addition

Add the following bullet to the DESIGN-mode output checklist. Suggested placement: SKILL.md §"Step 4 — Apply output standards" as a new bullet alongside existing bullets (file naming, Markdown for CLAUDE.md drafts, halt triggers, source-tagged claims, etc.). Alternative placement: `references/cc-prompt-design-patterns.md` if v3.1 keeps prompt-specific guidance there.

> **Shell environment in CC prompts.** When producing CC prompts that include shell command blocks, default to bash — bash is the typical CC harness shell (Git Bash on Windows, sh/bash on Linux/macOS) even when the operator's local environment defaults to PowerShell. Provide PowerShell variants for the commands that diverge: `Test-Path`/`Get-Content`/`Set-Content`, `wc -l`/`Measure-Object -Line`, line-continuation `\` vs backtick. Universal commands — all `git` and `gh` invocations, `pwd`, `ls` — work in both without variants. Pattern: bash as primary block, PowerShell labeled and adjacent for the divergent set. `[generalizable: Phase 31d merge prompt execution 2026-05-06]`

### Apply during audit pass

When the v3 skill-builder audit pass reaches `rootnode-cc-design`, add this bullet to the appropriate checklist location during the DESIGN-mode methodology pass. The bullet itself is short enough that it can be inserted as-is without rebudgeting the checklist's other content.

---

## Change 3 — DESIGN-mode bullet: pre-flight Skill enumeration

### Empirical evidence

In Phase 31d execution (2026-05-07) and Phase 32 execution (2026-05-07/08), CC prompts WITHOUT a pre-flight Skill enumeration step reached working-tree-edit operations before agents discovered which Skills were available. This created two failure modes: (a) agents made decisions assuming Skills they didn't have, requiring rework when discovery happened mid-execution; (b) agents skipped Skill activation entirely, missing methodology that should have applied.

The fix: CC prompts should enumerate available Skills as the first action, before any other file reads. This is now codified in CC_ENVIRONMENT_GUIDE §1.1 (per `root_KF_UPDATES_postv3_session.md` Update 1.1).

### Recommended addition

Add the following bullet to the DESIGN-mode output checklist. Suggested placement: SKILL.md §"Step 4 — Apply output standards" alongside Change 2's shell-agnostic syntax bullet.

> **Pre-flight Skill enumeration in CC prompts.** When producing a multi-step CC prompt (any session prompt with phases, halts, or non-trivial scope), include a pre-flight stage that enumerates available Skills before any other file reads. Pattern: "Before reading other files, enumerate available Skills in this session. Note the relevant Skills you'll compose with; explicitly note any expected Skill that's missing." Rationale: Skills determine methodology grounding; agents that don't know what's available make decisions on incomplete information. See CC_ENVIRONMENT_GUIDE §1.1 for full methodology.

### Apply during build pass

Insert as a new bullet in the appropriate checklist location during the DESIGN-mode methodology pass. Char-budget-neutral against existing bullets (each is independent guidance).

---

## Change 4 — DESIGN-mode bullet: continuation-phrase ambiguity gate

### Empirical evidence

In the Phase 31d merge prompt execution (2026-05-06), the prompt specified continuation phrases for halt-resume points but did not explicitly direct halt-on-ambiguity behavior. When the operator's continuation message had two reasonable interpretations, the agent inferred one and proceeded — turning out to be the wrong one. The fix surfaced as a methodology gap: continuation-phrase contracts must include explicit halt-on-ambiguity discipline.

This is now codified in CC_ENVIRONMENT_GUIDE §1.2 (per `root_KF_UPDATES_postv3_session.md` Update 1.2).

### Recommended addition

Add the following bullet to the DESIGN-mode output checklist:

> **Continuation-phrase ambiguity gate in multi-halt CC prompts.** When producing a CC prompt with operator halts and continuation phrases, include explicit halt-on-ambiguity discipline at each resume point. Pattern: "If the operator's continuation message is ambiguous between two or more reasonable interpretations, halt and ask one targeted clarifying question. Do not infer." Rationale: continuation phrases that look unambiguous in design can be ambiguous in execution; ambiguity-on-resume is a known failure mode where agents proceed on wrong inference. See CC_ENVIRONMENT_GUIDE §1.2 for full methodology.

### Apply during build pass

Insert as a new bullet in the same checklist location as Changes 2 and 3.

---

## Change 5 — DESIGN-mode bullet: forward-state-aware artifact authoring

### Empirical evidence

In Phase 32a (2026-05-07) and Phase 32b (2026-05-08), authored artifacts (PR descriptions, commit messages, audit reports, halt summaries) included forward references — e.g., "this commit on main..." authored before the commit hit main, "after the v3.0 release..." authored before Phase 32c. Some forward references were accurate (post-commit state); others created confusion when the artifact was read mid-flow at a state the reference assumed already happened.

The fix: artifact authoring should be deliberately forward-state-aware. References to commits, branches, or releases should explicitly indicate whether the state described is current at authoring or expected post-commit/post-merge/post-release.

This is now codified in CC_ENVIRONMENT_GUIDE §1.3 (per `root_KF_UPDATES_postv3_session.md` Update 1.3).

### Recommended addition

Add the following bullet to the DESIGN-mode output checklist:

> **Forward-state-aware artifact authoring in CC prompts.** When producing a CC prompt that authors PR descriptions, commit messages, audit summaries, or halt reports, instruct the agent to be explicit about whether forward references describe current state at authoring or expected state post-commit/post-merge. Pattern: "When referencing future state in an authored artifact, prefix with 'post-merge:' or 'this PR will:' rather than declarative present tense ('is on main')." Rationale: artifacts read mid-flow should not assume completed state that hasn't happened yet; explicit temporal markers prevent confusion. See CC_ENVIRONMENT_GUIDE §1.3 for full methodology.

### Apply during build pass

Insert as a new bullet in the same checklist location as Changes 2, 3, and 4.

---

## Composition note

These five changes are all independent. Change 1 operates on the SKILL.md frontmatter description (Description Refinement Loop pass). Changes 2–5 each add a single bullet to the DESIGN-mode output checklist (SKILL.md body or referenced file).

All five can be applied in the same build pass against `rootnode-cc-design`, producing rootnode-cc-design v2.1 (or v3.0 — version bump TBD by build pass). Each can also be applied separately — Change 1 as a quick description-only patch, or any of Changes 2–5 individually as checklist additions.

Recommendation: ship all five together in a single rev (cc-design v2.1) since they emerged from the same root-cause family and represent a coherent DESIGN-mode discipline upgrade.

---

## Source attribution

- Change 1: `root_SH_skill_builder_v3_evaluation.md` §5 item 4
- Change 2: `root_SH_skill_builder_v3_evaluation.md` §5 item 5
- Change 3: `root_KF_UPDATES_postv3_session.md` Update 1.1 (CC_ENVIRONMENT_GUIDE pre-flight Skill enumeration)
- Change 4: `root_KF_UPDATES_postv3_session.md` Update 1.2 (CC_ENVIRONMENT_GUIDE continuation-phrase ambiguity gate)
- Change 5: `root_KF_UPDATES_postv3_session.md` Update 1.3 (CC_ENVIRONMENT_GUIDE forward-state-aware authoring)
- Findings sources: seed Project session 2026-05-06 (cc-design v3 evaluation CV), Phase 31d merge prompt execution 2026-05-07, Phase 32 v3.0 build execution 2026-05-07/08
- Friction-driven update demonstrated in practice: `root_CC_phase31d_merge_no_release.md` rev2 (2026-05-06, EVOLVE mode update via cc-design Skill)
