# AP-Warning Summary: rootnode-skill-builder v2 self-audit

**Date:** 2026-05-04 (Phase 29 build CV)
**Audit subject:** rootnode-skill-builder v2 SKILL.md + 5 new references + 2 preserved references
**Audit tool:** v2 (self-audit per design spec §5 self-consistency criteria)

---

## Catches summary

| # | Pattern | Catalog ref | Subject file | Disposition |
|---|---|---|---|---|
| 1 | Kitchen Sink (structural) | `root_AGENT_ANTI_PATTERNS.md §3.4` | SKILL.md | **Accepted** |

Total catches: 1
Accepted: 1
Revised: 0
Outstanding: 0

---

## Catch detail

### Catch 1 — §3.4 Kitchen Sink (structural) — ACCEPTED

**Detection signal:** SKILL.md defines three top-level workflows (Build New Skill / Review Existing Skill / Revise Existing Skill) that each have their own procedure scaffolding. The catalog detection rule fires when a single Skill spans 3+ unrelated procedures.

**Why accepted:** The three workflows are not unrelated — they share the same machinery (spec compliance constraints, conversion rules, 8-dimension quality gate, reference file structure). Build produces; Review evaluates the same spec; Revise modifies and re-evaluates. They are three operational modes of a single Skill operating on the same subject matter (Skill files), not three different Skills hiding inside one folder.

**Reasoning per catalog disposition rule:** `references/anti-pattern-catalog.md` "Disposition of warnings" section explicitly documents this case: *"Pattern 4 (Kitchen Sink) accepted: The Skill genuinely benefits from co-locating workflows (e.g., `rootnode-skill-builder` itself has Build / Review / Revise workflows, intentionally unified because they share the same spec/quality gate machinery)."*

The acceptance is documented in the catalog reference itself — this isn't a one-off override, it's a precedent the catalog explicitly anticipates.

**Future maintainer guidance:** If at some point Build / Review / Revise diverge to the point that the shared machinery is no longer doing meaningful work — e.g., Review needs a fundamentally different spec model than Build, or Revise becomes a complex transformation pipeline — revisit this catch. Splitting may then be warranted. As of v2.0, the unification holds.

---

## Catches NOT detected (selected — for confidence)

These patterns were scanned and produced no catches; documenting the negative result for audit clarity:

| Pattern | Subject | Result |
|---|---|---|
| §2.1 Monolithic standing context | SKILL.md | 330 lines (under 500 spec limit), under threshold |
| §2.2 Layer hierarchy violation | SKILL.md | One enforcement-flavored phrase ("always run") found in Example 4, but it appears in a quoted user input demonstrating the Gate 1 redirect — the Skill is *describing* a pattern that should be a hook, not asserting that pattern itself. Not a catch. |
| §3.5 Blurred Layers | SKILL.md | All reference-shaped content delegated to references/. SKILL.md retains procedural / instruction content only. |
| §4.3 Manual-only Skills | frontmatter | `disable-model-invocation` not set; description has 10 explicit + 3 symptom-phrased verb-based triggers. |
| §4.11 Verification absent | SKILL.md | The 8-dimension quality gate IS the verification surface. Step 5 explicitly walks each dimension with pass/fail evidence. |
| §4.14 Stale content | SKILL.md + references | All canonical KF references match current naming (cc-design rename applied throughout, not stale cchq-design). All 7 reference citations from SKILL.md match the 7 references actually shipped (5 new + 2 preserved). |

---

## 7-layer leak-check result

Run separately from AP catalog scan per validation dimension 8.

| Leak type | Result |
|---|---|
| File-pattern rules in references/ → candidate for `.claude/rules/` | None detected. References are conceptual frameworks, not file-pattern rules. |
| Always-relevant facts → candidate for CLAUDE.md | None detected. All content is procedural / on-demand applicable, not always-loaded standing context. |
| Enforcement guarantees → candidate for hooks | None detected. Pre-build gates are advisory (Gate 2 and Gate 3 explicitly so; Gate 1 is strict per design spec but is a routing decision, not an environment-level enforcement). |
| External integration logic → candidate for MCP | None detected. v2 has no API calls or service-specific code. |

7-layer leaks: 0

---

## Overall self-audit verdict

v2 passes its own 8-dimension quality gate. The single AP catch is accepted with documented reasoning that the catalog itself anticipates. Zero 7-layer leaks. Self-consistency criteria from design spec §5 satisfied.

This artifact ships alongside v2 as part of the Phase D packaging. Future maintainers can consult this artifact to understand which catches were deliberate choices vs. which would warrant revision if surfaced again.
