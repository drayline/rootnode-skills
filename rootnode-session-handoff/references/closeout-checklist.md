# Closeout Checklist Reference

Template and guidance for the closeout actions produced after the handoff document. Read this file during Stage 4 (Produce) after outputting the XML handoff file.

The closeout checklist is delivered in conversation (not in the XML file). It is the final output of the Skill.

---

## Closeout Checklist Template

Present this checklist after delivering the handoff document:

```
## Closeout Actions

- [ ] **Handoff document delivered:** {filename} — saved to /mnt/user-data/outputs/
- [ ] **Memory updates:** {specific recommendations or "none needed"}
- [ ] **File delivery:** {all session artifacts accounted for, or list missing items}
- [ ] **build_context.md:** {specific updates needed, or "current — no update needed"}
- [ ] **Propagation items:** {items requiring cross-file updates, or "none"}
- [ ] **Starter prompt:** Ready in the handoff document, Section 8
```

---

## Memory Update Recommendations

The handoff Skill recommends Memory updates but does not execute them. Present recommendations as specific, actionable items.

### What Qualifies as a Memory Update

Memory holds always-loaded orientation facts — things the next session (and all future sessions) should know without searching. A fact qualifies for Memory if it passes both tests:

1. **Persistence test:** Will this fact still be relevant in 5+ sessions? If it's session-specific or will change soon, it stays in the handoff only.
2. **Orientation test:** Does Claude need this fact to orient correctly at the start of every conversation? If Claude only needs it during specific tasks, it belongs in a knowledge file or the handoff, not Memory.

### Common Memory Update Patterns

**Phase advancement:** "Phase N is COMPLETE. Phase N+1 is active." This is the most common update — phases are orientation-critical.

**Project state changes:** New knowledge files added/removed, new Skills installed, architectural decisions that change how the project operates.

**Workflow convention changes:** New patterns established that change how recurring work is handled (e.g., a deliverable that used to require multiple projects now happens in one).

**Key facts discovered:** Empirical findings, threshold values, or constraints discovered through work that will affect future sessions.

### What Does NOT Go in Memory

- Session progress details (too transient — belongs in the handoff)
- Decisions about specific deliverables (belongs in the deliverable or build_context.md)
- File contents or summaries (belongs in knowledge files)
- Step-by-step plans (belongs in the handoff continuation plan)
- Anything that duplicates content already in a knowledge file

### Recommendation Format

```
**Memory updates recommended:**
1. ADD: "Phase {N} active — {brief description of current work}"
2. UPDATE: Existing entry that's been superseded by a new decision or finding
3. REMOVE: Outdated entry that no longer reflects the project's state
```

If no updates are needed, state: "No Memory updates needed — current entries are accurate."

---

## build_context.md Assessment

For projects with a build_context.md file, assess whether it needs updating. This file is institutional memory — it tracks phases, decisions, and project evolution.

### When build_context.md Needs Updating

- A build phase was completed or advanced
- A significant architectural decision was made that affects the project going forward
- New knowledge files, Skills, or components were added or removed
- A design spec was produced that will drive future work
- The project's operational state changed (e.g., entered RAG mode, completed a major milestone)

### When It Does NOT Need Updating

- Routine work within an existing phase (unless a milestone within the phase was reached)
- Conversations that were purely planning/discussion with no deliverables
- Work that is fully captured in the deliverable itself and doesn't affect project-level state

### Recommendation Format

```
**build_context.md update needed:** Yes
- Add Build History entry for the work just completed
- Update "next priorities" to reflect completion
- Add to Skills inventory if a new Skill was built
```

Or: "**build_context.md:** Current — no update needed this session."

---

## Propagation Assessment

If the session changed system-wide facts, flag propagation items per any propagation checklist your project documents (commonly tracked in `build_context.md` or an equivalent institutional memory file).

### System-Wide Facts That Trigger Propagation

- File counts (knowledge files added/removed)
- Block/approach counts (new reasoning or output approaches)
- Tendency taxonomy changes (new behavioral tendencies identified)
- Compiler or Optimizer mode changes
- Architectural state changes (e.g., new layer model, new threshold values)
- Skill inventory changes (new Skills created, existing Skills revised)

### Propagation Targets

When propagation is needed, identify which files/stores need updating:

1. **build_context.md** — always a target when system facts change
2. **CONTENTS_INDEX.md** — if knowledge file inventory changed
3. **Memory** — if orientation facts changed
4. **CI (Custom Instructions)** — if knowledge file routing, Skill references, or operational modes changed
5. **Dependent knowledge files** — any file that references the changed fact

### Recommendation Format

```
**Propagation items:**
1. New Skill (rootnode-session-handoff) → build_context.md Skills inventory, Memory, CONTENTS_INDEX.md if the Skill is backed by a knowledge file
2. Workflow convention change → Memory entry capturing the new convention so future sessions follow the updated pattern
```

Or: "**Propagation:** None — no system-wide facts changed this session."

---

## Chain-of-Handoff Handling

When the current session started from a prior handoff document, the closeout must account for the chain.

### Rules

1. **The new handoff replaces the prior one.** The next session uploads only the new handoff — not both. The new document must be self-contained.

2. **Carry forward unresolved items.** Check the prior handoff's `open_items` and `items_carried_forward`. Any item not resolved in this session must appear in the new handoff's `items_carried_forward` element with a note on why it wasn't addressed.

3. **Reference, don't reproduce.** If the prior handoff's decisions or ingested content are still relevant, the new handoff captures them as part of its own decisions or ingested content sections. Don't create a "prior session" section — integrate the still-relevant content into the standard structure.

4. **Break long chains.** If a handoff chain exceeds 3 sessions, audit for items that have been carried forward without action across multiple handoffs. These are likely either stale (remove them) or blocked (escalate their priority). Flag any item carried forward for 2+ handoffs.

### Chain Awareness in the Closeout

```
**Handoff chain:** This is session 3 in a chain (started from {prefix}_session_handoff_2026-04-11.xml → {prefix}_session_handoff_2026-04-12.xml → this session).
- 1 item carried forward from session 1 (still unresolved — elevated to high priority)
- 2 items from session 2 resolved this session
- 1 new item added this session
```

Or for a new chain: "**Handoff chain:** New chain — no prior handoff."

---

## Cross-Project Handoff Items

When session work produces artifacts or decisions intended for another project, the closeout flags them separately from within-project items.

### What Qualifies

- Design specs intended for build in another project
- Decisions that affect another project's architecture or content
- Files that need to be loaded into another project's knowledge base
- Information that should be propagated to another project's Memory or CI

### Recommendation Format

```
**Cross-project items:**
1. Design spec produced this session → target build project for implementation
2. Strategic positioning update → strategy project (note any reference files that should be loaded into context for that work)
3. Phase status update → cross-project registry, if your portfolio maintains one
```

Or: "**Cross-project items:** None — all work contained within this project."
