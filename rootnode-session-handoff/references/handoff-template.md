# Handoff Template Reference

Complete XML schema for session handoff documents. Read this file when producing the handoff document in Stage 3 (Structure) and Stage 4 (Produce).

---

## Status Vocabulary

Use these exact values in all `status` attributes. No variations, no freeform text.

| Status | Meaning |
|--------|---------|
| `COMPLETE` | Work finished, no further action needed |
| `IN_PROGRESS` | Work started, not yet finished |
| `BLOCKED` | Cannot proceed until a dependency is resolved |
| `NOT_STARTED` | Identified but no work done yet |
| `DEFERRED` | Deliberately postponed — not blocked, chosen to delay |
| `NEEDS_VERIFICATION` | Work done but outcome needs validation |

---

## Complete XML Schema

```xml
<?xml version="1.0" encoding="UTF-8"?>
<session_handoff>

  <!-- ============================================================
       SECTION 1: SESSION HEADER
       Orients the next session to project, phase, and scope.
       ============================================================ -->
  <header>
    <project>
      <!-- Full project name — e.g., "Customer Support Operations" -->
    </project>
    <project_code>
      <!-- Project prefix — e.g., "support" — used in handoff filename -->
    </project_code>
    <date>
      <!-- YYYY-MM-DD -->
    </date>
    <phase>
      <!-- Current phase or "multi-phase" if session spanned boundaries.
           For non-phase-gated projects, use a brief context label. -->
    </phase>
    <prior_handoff>
      <!-- Filename of prior handoff if this session continued from one.
           "none" if this is the first session in the chain. -->
    </prior_handoff>
    <session_objectives>
      <!-- 1-3 sentences: what this session set out to do. -->
    </session_objectives>
    <completion_summary>
      <!-- 1 sentence: "2 of 3 objectives completed; track 3 deferred." -->
    </completion_summary>
  </header>

  <!-- ============================================================
       SECTION 2: ACTIVITY TRACKS
       One <track> per concurrent work stream. This is the structural
       core of the handoff. Single-track sessions still use this format.
       ============================================================ -->
  <activity_tracks>

    <track id="1" status="IN_PROGRESS">
      <name>
        <!-- Specific track name — not generic. "Context Budget Skill v5 Design"
             not "Skill work." -->
      </name>
      <objective>
        <!-- What this track is trying to accomplish. -->
      </objective>
      <starting_state>
        <!-- Where this track stood at session start. For new tracks: "New this session."
             For continued tracks: specific state from prior handoff or session start. -->
      </starting_state>
      <progress>
        <!-- Each step/milestone with status attribute and substantive detail.
             Not just "did step 3" — what step 3 produced or decided. -->
        <step status="COMPLETE">Defined the 4-stage pipeline (Inventory, Assess, Structure, Produce) with clear stage boundaries and per-stage outputs.</step>
        <step status="COMPLETE">Designed the XML document architecture — 8 sections, fixed status vocabulary, ID-based cross-referencing.</step>
        <step status="IN_PROGRESS">Building SKILL.md — core pipeline and examples done, troubleshooting section in progress.</step>
      </progress>
      <current_state>
        <!-- Where this track stands RIGHT NOW. Specific enough that the next
             session can resume without re-deriving context. This is not a summary
             of progress — it is the precise resumption point.

             Good: "SKILL.md body is complete at ~220 lines. Reference files not
             yet started. Design spec is the source — available in Drive."
             Bad: "Most of the work is done." -->
      </current_state>
      <next_steps>
        <!-- Sequenced, specific actions. Priority indicates order within this track. -->
        <step priority="1">Build references/handoff-template.md from the XML schema in the design spec.</step>
        <step priority="2">Build references/closeout-checklist.md from the closeout section of the design spec.</step>
        <step priority="3">Run the 5-dimension publication review.</step>
      </next_steps>
      <dependencies>
        <!-- "none" if no dependencies. Otherwise, specific blockers or prerequisites. -->
        none
      </dependencies>
    </track>

    <track id="2" status="COMPLETE">
      <name>Example of a completed track</name>
      <objective>Demonstrates compressed format for finished work.</objective>
      <starting_state>Started from prior handoff at step 3 of 5.</starting_state>
      <progress>
        <step status="COMPLETE">Steps 3-5 completed. Final deliverable produced.</step>
      </progress>
      <current_state>Complete. Deliverable saved to project storage (e.g., cloud drive folder, version-controlled repo).</current_state>
      <next_steps>
        <!-- Completed tracks may still have follow-on items. If none: -->
        <step priority="1">No further action.</step>
      </next_steps>
      <dependencies>none</dependencies>
    </track>

  </activity_tracks>

  <!-- ============================================================
       SECTION 3: KEY DECISIONS
       Every substantive decision with rationale. Never just the choice.
       ============================================================ -->
  <decisions>

    <decision id="1">
      <topic>Handoff document format</topic>
      <choice>XML over markdown for the handoff document.</choice>
      <rationale>XML provides more reliable structural parsing for Claude ingestion. The consistency of element boundaries outweighs the minor readability cost. Users review the XML directly when needed and pretty-printing is acceptable as long as the schema remains valid.</rationale>
      <implications>All handoff documents use the XML schema defined in this Skill. The starter prompt section uses CDATA wrapping to prevent parsing conflicts when prompts contain XML-like markup.</implications>
    </decision>

    <decision id="2">
      <topic>{Topic of second example decision}</topic>
      <choice>{What was chosen}</choice>
      <rationale>{Why — the reasoning that supports the choice}</rationale>
      <implications>{Downstream consequences — what this decision shapes about future work}</implications>
    </decision>

  </decisions>

  <!-- ============================================================
       SECTION 4: INGESTED CONTENT
       Summaries of uploaded files and external information.
       Capture the working understanding, not raw content.
       ============================================================ -->
  <ingested_content>

    <source id="1">
      <name>
        <!-- Filename or source identifier -->
      </name>
      <type>
        <!-- uploaded_file | web_reference | conversation_context | external_data -->
      </type>
      <key_content>
        <!-- The relevant facts, data, or constraints extracted.
             This is the session's working understanding — dense, specific,
             not a file description.

             Good: "Revenue was $4.2M in Q3 with 62% gross margin.
             Enterprise segment grew 34% YoY while SMB declined 8%.
             CAC payback period is 14 months."

             Bad: "The spreadsheet contained financial data." -->
      </key_content>
      <usage>
        <!-- How this content influenced the session's work. -->
      </usage>
      <reupload_needed>
        <!-- true or false.
             true = next session needs the original file for continued work.
             false = everything relevant is captured in key_content above.

             When in doubt, true. Losing access to source material is
             worse than a redundant upload. -->
      </reupload_needed>
    </source>

  </ingested_content>

  <!-- ============================================================
       SECTION 5: ARTIFACTS PRODUCED
       Files created, updated, or delivered during the session.
       ============================================================ -->
  <artifacts>

    <artifact id="1">
      <filename>
        <!-- Full filename with project prefix.
             e.g., support_Escalation_Decision_Tree_v2.md -->
      </filename>
      <location>
        <!-- Where the file lives. Examples:
             "Cloud drive: Projects/{prefix}/" for canonical storage outside the conversation
             "/mnt/user-data/outputs/" for session delivery point
             Local repo path for code projects
             Both if applicable -->
      </location>
      <status>COMPLETE</status>
      <description>
        <!-- What it is and what it contains. 1-2 sentences. -->
      </description>
      <cross_project>
        <!-- Only include this element if the artifact is intended for
             another project. Value is the target project name.
             e.g., "Engineering project" or "Strategy project"
             Omit entirely for within-project artifacts. -->
      </cross_project>
    </artifact>

  </artifacts>

  <!-- ============================================================
       SECTION 6: OPEN ITEMS
       Unresolved questions, deferred items, blockers, follow-ups.
       ============================================================ -->
  <open_items>

    <item priority="high">
      <description>
        <!-- What needs to be resolved. Specific and actionable. -->
      </description>
      <context>
        <!-- Why this matters, urgency level, what blocks on it.
             Include enough context that the next session understands
             the item without re-deriving background. -->
      </context>
    </item>

    <item priority="medium">
      <description>{Brief, actionable description of a deferred item}</description>
      <context>{Why this matters and why it's deferred. Include enough background that the next session understands the item without re-deriving context. Note any urgency level or dependency.}</context>
    </item>

  </open_items>

  <!-- ============================================================
       SECTION 7: CONTINUATION PLAN
       Sequenced priorities across all tracks for the next session.
       ============================================================ -->
  <continuation_plan>
    <summary>
      <!-- 1-2 sentences: overall assessment of where things stand
           and what the next session should focus on. -->
    </summary>
    <scope_estimate>
      <!-- "Completable in one session" | "Will likely require N sessions"
           | "Depends on X" -->
    </scope_estimate>
    <priority_sequence>
      <!-- Actions sequenced across all tracks. track_ref links to track IDs.
           Sequence the first action as what to start with — the next session
           reads this as the immediate resumption point. Reason for priority
           included so the next session understands the sequencing logic. -->
      <action priority="1" track_ref="1">{First action — typically the highest-priority unblocker or near-completion item}</action>
      <action priority="2" track_ref="1">{Second action — what comes once priority 1 is unblocked}</action>
      <action priority="3" track_ref="2">{Action on a different track — note the track_ref attribute}</action>
    </priority_sequence>
    <items_carried_forward>
      <!-- Items from a PRIOR handoff's open_items that were NOT resolved
           in this session. Prevents items from falling through cracks
           across handoff chains.
           Omit this element entirely if there was no prior handoff
           or all prior items were resolved. -->
      <item source="prior_handoff">Description of unresolved item — carried forward because it was not addressed this session due to [reason].</item>
    </items_carried_forward>
  </continuation_plan>

  <!-- ============================================================
       SECTION 8: STARTER PROMPT
       Ready-to-paste opener for the next session.
       Wrapped in CDATA because the prompt may contain XML-like markup.
       ============================================================ -->
  <starter_prompt>
    <prompt><![CDATA[
Uploading session handoff from [date]. The handoff file covers [brief scope].

Resume with [specific first action from continuation plan]. The continuation plan in the handoff has the full sequence.

[Any additional orientation the next session needs — e.g., "The design spec is also uploaded for reference" or "the institutional memory file needs updating before we proceed."]
    ]]></prompt>
  </starter_prompt>

</session_handoff>
```

---

## XML Design Notes

### CDATA for the Starter Prompt

The starter prompt often contains XML tags (especially for projects using XML in Custom Instructions). CDATA prevents the parser from interpreting prompt content as document structure. Always wrap the starter prompt in CDATA, even if the current prompt doesn't contain XML.

### Attribute-Level Status

Track and step statuses are XML attributes, not child elements. This keeps the structure compact and allows quick scanning:
- `<track id="1" status="IN_PROGRESS">` — status visible without reading into the element
- `<step status="COMPLETE">` — per-step status at a glance

### ID-Based Cross-Referencing

Tracks, decisions, sources, and artifacts carry `id` attributes. The continuation plan's `track_ref` attribute links actions to their parent track. This enables the next session's Claude to navigate the document structurally — jumping from a continuation action to its track context.

IDs are simple integers (1, 2, 3...) scoped within their section. Track IDs don't need to be globally unique with decision IDs.

### Fixed Element Names

Every element name is part of the schema. No freeform element naming. This ensures consistent parsing across sessions and Claude instances. If content doesn't fit an existing element, it goes in the most relevant existing element's text — never as a custom-named element.

### The `cross_project` Element

Only present on artifacts intended for another project. Omitted entirely (not set to "none") for within-project artifacts. This makes cross-project items easy to scan — search for `<cross_project>` to find all of them.

---

## Starter Prompt Construction

The starter prompt is the most important single paragraph in the handoff. It determines whether the next session starts productively or wastes turns re-establishing context.

**Requirements:**
1. Reference the handoff document by filename (it will be uploaded)
2. State the single first action from the continuation plan
3. Reference the full continuation plan for sequencing
4. Add any orientation the next session needs beyond the handoff (files to re-upload, Memory state, prerequisite actions)

**Style:** Match the user's communication preferences for starter prompts — typically terse and directive. No preamble, no context re-establishment beyond the handoff reference. Assume Claude will read the handoff file.

**Length:** 2-5 sentences. Longer is wasted context — the handoff file carries the detail.

**Examples:**

Single-track continuation:
```
Uploading session handoff from 2026-04-13. Resume the escalation decision tree work — reference templates are next. The design doc is also uploaded.
```

Multi-track continuation:
```
Uploading session handoff from 2026-04-13. Three tracks — start with the institutional memory file update (Track 2, highest priority per continuation plan). Track 1 (template library) is complete. Track 3 (cross-project propagation) needs the strategy project's positioning doc loaded.
```

Proactive handoff continuation:
```
Uploading session handoff from 2026-04-13. Context pressure forced early closeout. Resume with Track 1 step 4 — the 80%-complete deliverable. Continuation plan has the full sequence.
```
