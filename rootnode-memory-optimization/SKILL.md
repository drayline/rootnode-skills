---
name: rootnode-memory-optimization
description: >-
  Rebalances context across Memory, Custom Instructions, and knowledge files in
  Claude Projects. Audits Memory for redundancy, staleness, and misplacement,
  then prescribes knowledge file trimming enabled by Memory optimization. Use
  when user says "optimize my memory," "what should be in my memory," "trim my
  knowledge files," "reduce my context usage," "rebalance my project," "my
  project feels bloated," or asks whether something belongs in Memory or a
  knowledge file. Also use when a user reports context window pressure or
  truncation in long conversations. Do NOT use for full project architecture
  audits (use rootnode-project-audit if available). Do NOT use for evaluating
  a single prompt (use rootnode-prompt-validation if available).
license: Apache-2.0
metadata:
  author: rootnode
  version: "1.1"
  original-source: "NEW"
---

# Context Layer Optimization for Claude Projects

Rebalances context across Memory, Custom Instructions, and knowledge files in Claude Projects. Produces Memory edit prescriptions, knowledge file trimming recommendations, and cross-layer alignment findings.

## Critical Rule: User Confirmation Before Memory Edits

**Never execute Memory edits without presenting the full prescription and receiving explicit user confirmation.** Memory is persistent and personal — this skill recommends, the user decides.

**Confirmation protocol (every engagement):**
1. Present the complete optimization prescription: Memory edits (organized Remove → Add → Replace), knowledge file trimming recommendations, and context budget impact summary
2. State clearly: "These are my recommendations. I'll make the Memory changes only after you confirm."
3. Wait for explicit user approval before calling `memory_user_edits`
4. Execute edits in the correct sequence: removals first (highest line numbers first to avoid index shifts), then additions, then replacements
5. Present the final Memory state (via `memory_user_edits` view) as verification after execution

If the user says "just do it" or "go ahead with everything" — that IS confirmation. Execute. The gate ensures the user has seen the prescription, not to add friction.

If the user wants partial execution — execute only the approved edits. Note which recommendations remain unexecuted.

## Critical Rule: Complete File Output

When producing any updated file — Custom Instructions, knowledge files, or any other deliverable — always output the complete file as a single, separately copyable unit. Never output diffs, patches, or partial sections that require manual splicing. The user replaces the old file by copying the complete output.

## Core Thesis

Optimal Project performance requires the right fact in the right layer:

| Layer | Purpose | What Belongs Here |
|---|---|---|
| **Memory** | Always-loaded orientation | High-frequency facts every conversation needs: current phase, active constraints, key decisions, identity facts |
| **Custom Instructions** | Always-loaded behavioral architecture | Identity, behavioral rules, output standards, knowledge file routing, mode definitions |
| **Knowledge files** | Searchable reference depth | Structured content, detailed procedures, historical records, checklists, extended examples |
| **Conversation** | Per-message working context | Task-specific input, iterative refinement, session state |

Misalignment in any direction — orientation buried in a knowledge file, reference material crammed into Memory, behavioral rules in a knowledge file — degrades performance. Memory optimization is not a standalone operation; it cascades. When Memory is optimized, knowledge files can be trimmed. When knowledge files are trimmed, context budget is freed. When context budget is freed, Claude has more room for the actual conversation.

## When to Use This Skill

**Use when:**
- User wants to optimize their Memory or review what's in it
- User wants to trim knowledge files or reduce context usage
- User asks whether content belongs in Memory or a knowledge file
- User reports context window pressure, truncation, or Claude forgetting instructions in long conversations
- User describes their project as "bloated" in the context of files, memory, or context (not behavior or output)
- A project audit found Knowledge Architecture scoring ≤ 3 and the user has Memory enabled

**Do NOT use when:**
- User wants a full project architecture audit → recommend rootnode-project-audit if available
- User wants to evaluate a single prompt → recommend rootnode-prompt-validation if available
- User wants to build a new project from scratch → recommend rootnode-prompt-compilation if available
- User wants to edit a single Memory entry without broader optimization context → assist directly, no skill needed

---

## Stage 1: Project Comprehension

Understand the project holistically before touching any layer. This prevents rote optimization — the skill must know what the project is trying to accomplish before it can judge what every conversation needs.

**Assess:**
- **Mission:** What does this project do? What outcome does it serve?
- **Phase:** Active development, burn-in, mature maintenance, or expansion? The phase determines what Memory needs to emphasize.
- **Task profile:** What types of conversations happen here? Uniform tasks need less orientation; varied tasks need Memory to anchor the common thread.
- **Active constraints:** What decisions, limitations, or boundaries affect every conversation? (File count limits, deferred features, architectural principles, deployment targets.) These are prime Memory candidates.
- **Volatility:** How often does this project's state change? High-volatility facts (current phase, active sprint goals) belong in Memory. Low-volatility facts (design principles, permanent decisions) can live in knowledge files.

**Information sources:**
- Auto-populated userMemories (visible in system context): identity, projects, current state, preferences
- Manual Memory edits (via `memory_user_edits` view): user-curated facts
- Custom Instructions (user provides or describes): behavioral architecture
- Knowledge files (user provides key files or describes): reference depth
- If the user is running this in the project being optimized, all of the above is directly accessible

**Do not interrogate.** Assess what's available, request only the highest-leverage missing piece, and state what you're assuming about the rest. If the user is in the project being optimized, start immediately with what's accessible.

## Stage 2: Context Layer Audit

Map what's in each layer. Identify redundancies, gaps, and misalignments.

### 2a: Memory Assessment

Evaluate current Memory edits against five criteria. See `references/assessment-rubric.md` for expanded anchoring examples, common failure patterns, and the layer placement decision tree.

| Criterion | What to Check |
|---|---|
| **Orientation Coverage** | Does Memory cover the facts every conversation needs? Current phase, active constraints, key decisions, identity facts. |
| **Redundancy** | Is the same information in both manual edits AND auto-populated memories? Or duplicated across Memory and knowledge files? |
| **Staleness** | Are any Memory edits outdated — completed phases, old decisions, resolved constraints? |
| **Layer Misplacement** | Are any Memory edits carrying content that belongs in a knowledge file (reference depth) or Custom Instructions (behavioral rules)? |
| **Slot Efficiency** | Of 30 available slots, how many are used? Are remaining slots allocated to the highest-leverage facts? |

Rate each criterion **Pass / Partial / Fail** with specific evidence. Do not score without citing the specific Memory edit or gap.

### 2b: Custom Instructions Assessment (Memory-Relevant Scope Only)

This is NOT a full CI audit. Focus narrowly on:
- Does the CI contain orientation content that should be in Memory? (Common in pre-Memory projects: the CI carries "current state" paragraphs that are now Memory's job.)
- Does the CI acknowledge the Memory layer in its information architecture?
- Are there entries styled as behavioral rules that are actually orientation facts? ("This project is in Phase 3" is orientation, not behavior.)

### 2c: Knowledge File Assessment

**Primary target:** Institutional memory files (build_context.md or equivalent) that carry project history, state tracking, and orientation content. These are the files most affected by Memory's existence because they often carry always-loaded content that Memory handles better.

For each institutional memory file, assess:
- **Redundancy with Memory:** Which sections duplicate what Memory already provides? These are trimming candidates.
- **Redundancy with Custom Instructions:** Which sections duplicate the CI's identity description, knowledge file guide, or behavioral rules? These are trimming candidates.
- **Unique depth:** Which sections contain structured, interconnected content that only a knowledge file can hold? (Decision rationale chains, checklists with cross-references, phase histories with dependency tracking.) These are KEEP zones.
- **Context cost:** Approximately how many tokens does this file consume? What percentage could be recovered through trimming?

For other knowledge files, assess at a lighter level:
- Are any files carrying content better suited to Memory?
- Are any files bloated with content now unnecessary given Memory handling orientation?

See `references/optimization-patterns.md` for trimming patterns and cross-layer alignment patterns with before/after examples.

## Stage 3: Optimization Prescription

Produce specific, actionable recommendations grounded in Stage 1's project understanding and Stage 2's audit findings. Every recommendation cites specific content — a specific Memory edit, a specific CI paragraph, a specific knowledge file section.

### 3a: Memory Edit Prescriptions

For each recommendation, provide:
- **Action:** Add / Remove / Replace (with specific text for Add and Replace)
- **Rationale:** Why this fact deserves always-loaded status (tied to project mission and task profile)
- **Layer justification:** Why Memory is the right layer (not CI, not a knowledge file)

Organize into three categories:
1. **Remove** (redundant, stale, or misplaced entries) — execute first to free slots
2. **Add** (missing orientation facts identified in Stage 2a)
3. **Replace** (entries correct in intent but poorly written, too vague, or could be sharper)

Include a net slot count: "After these changes: X of 30 slots used, Y slots remaining."

**Memory constraint awareness:** 30 edits × 500 characters = 15,000 characters maximum. Optimize for the highest-leverage entries within this budget. Note remaining slot capacity and whether the project has room for growth.

**Never recommend atomizing structured knowledge file content into flat Memory entries.** Content like checklists, phase histories with decision rationale, and cross-referencing architectural decisions belongs in knowledge files. Memory gets the index; knowledge files keep the archive.

### 3b: Knowledge File Trimming Prescriptions

For each institutional memory file:
- **Sections to compress:** Specific sections that can be reduced now that Memory or CI handles the orientation. Provide the compressed replacement text.
- **Sections to remove:** Content fully redundant with Memory or CI. Cite the specific Memory edit or CI section that covers it.
- **Sections to keep untouched:** Content with unique value as structured depth. Briefly state why.
- **Estimated impact:** Approximate character or token reduction.

If the trimming is substantial enough to warrant producing an updated file, offer to produce it. If the user accepts, output the complete updated file — never a diff or partial section.

See `references/optimization-patterns.md` for the five trimming patterns.

### 3c: Cross-Layer Alignment Recommendations

For any content found in the wrong layer:
- State what the content is
- State which layer it's currently in and which layer it should be in, and why
- Provide the migration action (move, copy-and-trim, rewrite)

If alignment recommendations include Custom Instructions changes and the user requests the updated CI, output the complete Custom Instructions as a single, separately copyable unit.

## Stage 4: Delivery and Confirmation

### Quick Optimization (Memory-only, no knowledge file changes needed)

1. Memory edit prescriptions with rationale
2. Present the full prescription: "These are my recommendations. I'll make the Memory changes only after you confirm."
3. Wait for user confirmation
4. Execute edits (removals first — highest line numbers first — then additions, then replacements)
5. Present the final Memory state via `memory_user_edits` view

### Full Optimization (Memory + knowledge file trimming)

1. Memory edit prescriptions (Remove → Add → Replace)
2. Knowledge file trimming prescriptions with before/after for each section
3. Context budget impact summary showing the cascade: "These N Memory edits enable these M knowledge file trims, recovering approximately X characters of context budget."
4. Updated knowledge file(s) as downloadable deliverable(s) if trimming is substantial
5. If CI changes are prescribed and the user requests them, produce the complete updated Custom Instructions as a downloadable deliverable
6. Present the full prescription: "These are my recommendations. I'll make the Memory changes only after you confirm."
7. Wait for user confirmation before executing any Memory edits

### Optimization with Audit Referral (significant structural issues found)

1. Deliver Memory and knowledge file recommendations as above
2. Flag the structural issues that are beyond this skill's scope
3. Recommend rootnode-project-audit for comprehensive evaluation (if available)

---

## Troubleshooting

**Skill produces mechanical recommendations without strategic grounding:**
Stage 1 was skipped or rushed. Go back and assess the project's mission, phase, and task profile before auditing layers. Two projects with identical Memory content should get different recommendations if their missions differ.

**Recommendations are vague ("improve your Memory"):**
Every recommendation must cite specific content. "Your Memory doesn't cover active constraints" is incomplete. "Your Memory doesn't include the 28-file ceiling constraint that affects every architectural discussion in this project" is grounded.

**Knowledge file trimming removes too much:**
The skill should never recommend removing structured, interconnected content (decision rationale chains, checklists with cross-references). If the recommendation is to remove a section, verify it's genuinely redundant with Memory or CI — not just thematically similar.

**User reports no improvement after optimization:**
If Memory and knowledge file optimization doesn't resolve context pressure, the issue may be structural — conflicting instructions, missing identity, or anti-patterns. Recommend rootnode-project-audit for comprehensive evaluation if available. If the issue is specific Claude behavioral tendencies (verbosity, hedging, list overuse), recommend rootnode-behavioral-tuning if available.

**User is not in the project being optimized:**
The skill works best when run inside the target project (direct access to Memory, CI, and knowledge files). If the user is working from a different context, request the Custom Instructions and key knowledge files. Use `memory_user_edits` view to access the user's Memory edits (these are user-level, not project-level, so they're accessible from any conversation).
