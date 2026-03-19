# Memory Assessment Rubric

Detailed assessment criteria for evaluating Memory edits in a Claude Project. Used during Stage 2a of the optimization pipeline. Each criterion is rated Pass / Partial / Fail with specific evidence.

---

## Layer Placement Decision Tree

Use this to determine which layer any piece of content belongs in:

```
Is this fact needed in EVERY conversation?
├── YES → Does it instruct behavior, or state a fact?
│   ├── Instructs behavior → Custom Instructions
│   │   Examples: output formatting rules, persona definitions,
│   │   tool usage policies, mode definitions
│   └── States a fact → Memory
│       Examples: current project phase, active constraints,
│       key decisions, deployment targets, file count limits
└── NO → Is it needed in SPECIFIC conversations on demand?
    ├── YES → Knowledge file (searchable depth)
    │   Examples: decision rationale archives, procedure checklists,
    │   API reference tables, historical phase records
    └── NO → Does it need to be in the project at all?
        ├── YES (infrequent but critical) → Knowledge file
        └── NO → Remove it
```

**Key distinction: Memory vs. Custom Instructions.** Memory states facts ("This project is in Phase 3"). Custom Instructions define behavior ("When the user asks for a status update, format it as..."). If the content tells Claude what to do, it's a behavioral instruction and belongs in CI. If it tells Claude what IS, it's an orientation fact and belongs in Memory.

**Key distinction: Memory vs. Knowledge files.** Memory is always-loaded — every conversation pays the token cost. Knowledge files are searched on demand — only loaded when relevant. Content that >50% of conversations need belongs in Memory. Content that <50% of conversations need belongs in a knowledge file, where it adds depth without consuming always-loaded budget.

---

## Five-Criterion Assessment

### Criterion 1: Orientation Coverage

**What to check:** Does Memory cover the facts that every conversation in this project needs to know?

**Pass:** Memory contains the project's current phase, active constraints, key recent decisions, and any identity facts critical to consistent behavior. A new conversation would start with enough context to avoid repeating foundational questions.

**Partial:** Memory covers some orientation but has gaps. Common gaps:
- Active constraints missing (file count limits, deferred features, architectural boundaries)
- Phase information absent or outdated
- Key decisions buried in knowledge files only — Claude discovers them through search, not upfront orientation
- Identity facts that affect every conversation missing from Memory

**Fail:** Memory is either empty, contains only auto-populated content with no manual edits, or the manual edits address peripheral concerns while core orientation is absent.

**Evidence required:** List the orientation facts that are present in Memory and the facts that are absent but needed (based on Stage 1's project comprehension).

### Criterion 2: Redundancy

**What to check:** Is the same information stored in multiple layers without purpose?

**Pass:** Each fact appears in exactly one layer, or appears in multiple layers with clear purpose (e.g., a one-line orientation pointer in Memory with detailed rationale in a knowledge file — the pointer and the detail serve different roles).

**Partial:** Some facts appear in both manual Memory edits and auto-populated memories, or in both Memory and a knowledge file, without the duplication serving a distinct purpose. The redundancy wastes slots or tokens but doesn't cause conflicting information.

**Fail:** Significant duplication across layers, especially:
- Manual Memory edits that restate what auto-populated memories already capture (user's name, role, location, stated preferences)
- Multi-paragraph content in both an institutional memory file and Memory edits
- The same constraint or decision stated in CI, Memory, AND a knowledge file with varying levels of detail and no clear authoritative source

**Evidence required:** Cite each redundant pair — the specific Memory edit and the specific other-layer content it duplicates.

### Criterion 3: Staleness

**What to check:** Are any Memory edits outdated?

**Pass:** All Memory edits reflect the project's current state. Phase markers are current. Constraints that have been lifted are removed. Decisions that were reversed are updated.

**Partial:** One or two edits reference past states but don't cause active harm (e.g., a phase marker one phase behind, a constraint that was relaxed but not removed).

**Fail:** Multiple edits reference completed phases, old decisions, or resolved constraints. The stale entries actively mislead Claude about the project's current state.

**Evidence required:** Cite each stale Memory edit and what it should say (or whether it should be removed).

### Criterion 4: Layer Misplacement

**What to check:** Are any Memory edits carrying content that belongs in a different layer?

**Common misplacements:**
- **Behavioral instructions in Memory:** "Always format output as markdown tables" belongs in Custom Instructions, not Memory. Memory states facts; CI instructs behavior.
- **Reference depth in Memory:** Multi-sentence explanations, detailed procedures, or decision rationale crammed into a 500-character Memory edit. This content belongs in a knowledge file where it has room to be complete and structured.
- **Orientation facts in CI instead of Memory:** "This project is in Phase 3 — burn-in period" in Custom Instructions when it should be a Memory edit that can be updated without editing CI.

**Pass:** All Memory edits contain orientation facts appropriate for always-loaded context. No behavioral instructions. No reference-depth content compressed beyond usefulness.

**Partial:** One or two edits are borderline (e.g., a constraint stated in slightly prescriptive language that's technically orientation but reads like a behavioral instruction).

**Fail:** Multiple edits carry behavioral instructions or reference-depth content. Memory is being used as a dumping ground rather than a curated orientation layer.

**Evidence required:** Cite each misplaced edit, state which layer it belongs in, and why.

### Criterion 5: Slot Efficiency

**What to check:** Of 30 available slots, how well is the budget allocated?

**Pass:** Slot usage reflects the project's priorities. High-frequency orientation facts consume slots. Low-frequency or low-leverage facts do not. Remaining capacity is appropriate for the project's growth trajectory.

**Partial:** Slots are used but allocation is uneven — one project area over-represented while another has no Memory coverage. Or low-leverage facts consume slots that higher-leverage facts need.

**Fail:** Either: slots are nearly exhausted with low-quality entries, leaving no room for growth; or very few slots are used despite clear orientation gaps identified in Criterion 1.

**Evidence required:** State current slot usage (X of 30). Identify any low-leverage entries that could be removed to free slots for higher-priority content.

---

## Memory Edit Quality Criteria

When evaluating existing edits or writing new ones, each Memory edit should be:

- **Concise:** Uses the 500-character limit efficiently. No filler words, no redundant context. Every character earns its place.
- **Self-contained:** Understandable without reading other Memory edits. A developer reading this single edit can grasp the fact without cross-referencing.
- **High-frequency:** Relevant to more than 50% of conversations in this project. If a fact only matters occasionally, it belongs in a knowledge file.
- **Current:** Reflects the project's actual state, not a past state. Phase markers, constraints, and decisions should be updated as the project evolves.
- **Non-behavioral:** States facts, not instructions. "This project uses Apache-2.0 licensing" (fact) belongs in Memory. "Always include license headers in generated files" (instruction) belongs in Custom Instructions.
