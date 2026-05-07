# rootnode-cc-design Anti-Pattern Warnings

**Build event:** v2.0 release (predecessor `rootnode-cchq-design` v1.1.1)
**Build date:** 2026-05-05
**Build CV phase:** Phase 30 D-build
**Skill builder version:** rootnode-skill-builder v2.0
**Quality gate:** Step 5 (8-dimension), Dimension D7 (anti-pattern catalog scan)

---

## Catches summary

| Pattern | Status | Disposition | Documented in |
|---|---|---|---|
| `root_AGENT_ANTI_PATTERNS.md §3.4` Kitchen Sink (structural, CP-side) | CATCH | ACCEPTED with reasoning | This artifact §1 |

**Total catches:** 1
**Total accepted-with-reasoning:** 1
**Total revised-to-resolve:** 0
**Total halt-and-escalate:** 0

---

## §1. Kitchen Sink (structural, CP-side) — ACCEPTED with reasoning

**Pattern source:** `root_AGENT_ANTI_PATTERNS.md §3.4` (structural Kitchen Sink — distinct from `§4.13` operational Kitchen Sink for CC sessions).

**Surface tag:** `[CP]` (the structural variant applies to CP — Skills, Projects, methodology systems with too many co-located concerns).

**Catch context:** rootnode-cc-design v2.0 has five modes (DESIGN, EVOLVE, RESEARCH, TEMPLATE, REMEDIATE) co-located in a single Skill. Pattern §3.4 surfaces when "a single artifact carries multiple semi-independent concerns that could plausibly be separate Skills."

**Disposition:** ACCEPTED with reasoning. Inherited from v1.1.1 architecture; affirmed in design spec §12.3 D7 + scope-lock §2.10.

### Why the co-location is intentional

The five modes share a substantial methodology grounding that cannot be cleanly factored without duplication or fragmentation:

1. **Shared methodology references.** All five modes consult one or more of the same reference files (`cc-methodology-patterns.md`, `cc-environment-design-patterns.md`, `cc-anti-patterns.md`, `source-grading-and-tagging.md`, `chat-to-code-handoff-patterns.md`). Splitting modes into separate Skills would either duplicate the references 5× (violating progressive disclosure and inflating the ecosystem's reference token budget by ~5×) or create cross-Skill dependency chains (violating skill-builder v2's standalone-first composition discipline).

2. **Shared operational invariants.** All five modes apply the same 5-tier source authority hierarchy, the same 7-layer placement framework, the same agent-warranted test, the same change_log discipline, and the same generalizable-vs-project-specific tagging discipline. These are not mode-specific guarantees; they are Skill-level disciplines applied uniformly.

3. **Cross-mode handoffs are common.** A typical workflow invokes DESIGN to scaffold, EVOLVE to add new patterns from session friction, RESEARCH to evaluate a candidate before adopting, TEMPLATE to extract reusable artifacts, and REMEDIATE to close hygiene loops. Splitting these into separate Skills would force users to remember which Skill to invoke for each transition, when in practice the transitions are part of one continuous design discipline.

4. **Production validation evidence.** v1.1.1 shipped with this five-mode structure and was validated against a production CC deployment 2026-05-04. The co-located mode structure was not the source of any reported friction in that validation; it carries warrant inheritance into v2.0.

### Why splitting was not the right call

Considered alternatives during the v2 design CV (per scope-lock §2.10):

- **Split into 5 single-mode Skills.** Would require ~5× duplication of methodology references OR cross-Skill soft-pointer chains. Both options regress the architecture vs v1.1.1.
- **Split REMEDIATE into its own Skill (the only execution mode), keep DESIGN/EVOLVE/RESEARCH/TEMPLATE in cc-design.** Considered at length. Rejected because (a) REMEDIATE shares the methodology references with the other four modes (the per-pattern fix recipes in `cc-anti-patterns.md` are read by REMEDIATE for fix-recipes and by EVOLVE for diagnosis), and (b) the chat→Code handoff workflow benefits from one Skill spanning both surfaces.
- **Keep as v1.1.1 (5 modes co-located).** Selected. The structural Kitchen Sink catch is a known architectural cost; the alternative architectures regress on ecosystem coherence and duplication discipline.

### What this means for downstream evolution

If a sixth mode is proposed in a future v2.x, apply this test: does the new mode share the methodology grounding (5-tier source authority, 7-layer placement, agent-warranted test, change_log, tagging discipline)? If yes, add it to cc-design. If no, build a separate Skill.

If the existing five modes diverge in their methodology grounding over time (e.g., REMEDIATE adopts a different placement framework than DESIGN), the Kitchen Sink ACCEPTED-with-reasoning verdict should be re-litigated. This artifact is durable record; future builds re-evaluate whenever the underlying conditions change.

---

## §2. Other Skill-relevant patterns scanned (no catches)

The Step 5 D7 scan walked the following Skill-relevant patterns; none caught:

- **Bloated Skill body** (>500 lines): SKILL.md is 248 lines. Below ceiling.
- **Description bloat** (>1024 chars): description is 990 chars after YAML parsing. Margin 34.
- **Reference files >5000 tokens** (skill-builder v2 soft guideline): see token measurement report. Several references are borderline under estimated Opus 4.7 tokenization (chars/4 lower bound + 1.45× upper bound for technical markdown). Aaron deferred split decision per design spec §13 known gap. Not a hard catch — deferred to Aaron's review per his stated preference.
- **Circular reference dependencies**: the 9 references are independently readable; no chain dependencies. Inherited v1.1.1 architecture preserved.
- **Methodology-as-data**: reference files carry methodology text (Signature/Cause/Symptoms/Fix/Source per anti-pattern; Canonical source/Skill-specific application per methodology pattern), not Skill-level instructions. The instruction layer lives in SKILL.md; the reference layer lives in `references/*.md`. Correct architecture.
- **Duplicate auto-activation triggers across installed Skills**: Skill name and trigger phrases are unique within the rootnode ecosystem. Verified during description-collision check.
- **Hidden cross-Skill dependencies**: only soft pointers used (`if available` language). Skill works standalone.

---

## §3. Token-budget known gap (deferred to Aaron, design spec §13)

The token measurement report flagged several references where the estimated Opus 4.7 token count may exceed the 5000-token reference-size guideline. The estimates use chars/4 lower bound + 1.45× upper bound for technical markdown content (the Anthropic-published Opus 4.7 tokenizer multiplier ranges 1.0–1.35×; independent measurement on technical content shows 1.45–1.47×).

**Files flagged for review** (lower-bound estimates exceeding 5000 tokens):
- `cc-anti-patterns.md` — ~5,782 lower-bound (substantive rebuild grew from v1.1.1's 259 lines to 350 lines due to per-pattern Canonical/Surface tag/Sweep category mapping headers)
- `cc-environment-design-patterns.md` — ~5,425 lower-bound (preserved verbatim from v1.1.1)
- `cc-methodology-patterns.md` — ~5,429 lower-bound (preserved verbatim with canonical-cite preamble + per-section Canonical source headers added)
- `SKILL.md` — ~7,011 lower-bound (above the body-length ceiling line count of 500, but body length is the authoritative D2 dimension which checks lines, not tokens; SKILL.md is 248 lines, well below 500)

**Files clearly below threshold** (lower-bound estimates < 5000 tokens):
- `cc-prompt-design-patterns.md` — ~4,671
- `chat-to-code-handoff-patterns.md` — ~3,380
- `cc-skills-and-hooks-composition.md` — ~3,637
- `remediate-mode-execution.md` — ~4,904 (within budget)
- `source-grading-and-tagging.md` — ~2,844
- `troubleshooting.md` — ~3,364

**Disposition (per design spec §13 known gap):** Aaron decides whether to split. Recommended path:
1. At install time, verify against the actual Opus 4.7 tokenizer.
2. If a reference materially exceeds 5000 tokens, consider splitting along natural section boundaries (e.g., split `cc-anti-patterns.md` into `cc-anti-patterns-bloat.md` + `cc-anti-patterns-permissions.md` + `cc-anti-patterns-skills-hooks.md`, keyed by the structural fix domain).
3. If splits are made, update SKILL.md's Reference Files table accordingly.

This is a soft-guideline catch, not a hard violation. The 5000-token guideline exists to keep on-demand reference loads from polluting the active context; references that are 5500–6500 tokens still load productively in most workflows.

---

## §4. Promotion-provenance integration

This artifact is the third of three Step-6 audit artifacts (placement note, promotion provenance, AP warnings). Together they document the v2.0 build's architectural decisions for future audit reference. File to `Projects/ROOT/research/`.

**Cross-reference:**
- `rootnode-cc-design_placement_note.md` — Gate 3 ecosystem placement decisions
- `rootnode-cc-design_promotion_provenance.md` — Gate 2 warrant inheritance from v1.1.1
- This artifact — Gate 5 (D7) anti-pattern catch dispositions

---

*This anti-pattern warnings artifact is produced as a Step 6 audit artifact during the v2.0 build CV. It documents the D7 scan results: 1 catch (Kitchen Sink, structural — ACCEPTED with reasoning), 0 revisions, 0 halts. File to `Projects/ROOT/research/`.*
