# Placement Note: rootnode-skill-builder v2

**Surface:** CP
**Composition pattern:** Producer (builds all rootnode Skills) + Consumer (consumes process-abstraction handoff briefs from rootnode-repo-hygiene)
**Layer fit:** Governance — over the Skill-build workflow (Skill build is the workflow; v2 governs it with gates + 8-dim quality)

---

## Composes with

- **rootnode-repo-hygiene** (v1, in design as of this build): Producer→Consumer pattern. repo-hygiene Cat 14 process-abstraction detection produces handoff briefs in the format specified in `references/warrant-check-criteria.md`; v2 consumes these briefs as Gate 2 warrant evidence (auto-pass when brief is provided).

- **rootnode-cc-design** (formerly rootnode-cchq-design): Sibling. cc-design handles CC environment design; skill-builder handles Skill construction. Both apply the unified principle layer (`root_AGENT_ENVIRONMENT_ARCHITECTURE.md`) from different angles. Cross-references each other in the runtime tooling map.

- **All rootnode Skills (CP-side and CC-side)**: skill-builder is the build tool for the entire rootnode Skill ecosystem. Every other Skill in the catalog is potentially built or revised through skill-builder. v2's pre-build gates and 8-dim quality gate now apply to all future Skill builds.

---

## Fills which gap

v1 produced deployment-ready Skill files but did not gate-check whether the work belonged in a Skill at all (decomposition), whether the abstraction was warranted (3+ occurrences), or whether the Skill duplicated existing capability (ecosystem fit). v2 closes these three gaps with explicit pre-build gates.

v1's 5-dimension quality gate validated spec compliance, activation precision, methodology preservation, progressive disclosure, and standalone completeness. It did not check auto-activation discipline (description must include verb-based triggers; `disable-model-invocation: true` requires justification), did not scan against the unified anti-pattern catalog, and did not check for 7-layer leaks (content that should live in CLAUDE.md / `.claude/rules/` / hooks / MCP rather than in the Skill). v2 closes these three gaps with three new validation dimensions (6, 7, 8).

These six closures together prevent the dominant failure modes documented in `root_AGENT_ANTI_PATTERNS.md`: misplaced content (gates 1, validation dim 8), premature abstraction (gate 2), routing collisions (gate 3), undertriggering (validation dim 6), and structural anti-patterns inside produced Skills (validation dim 7).

---

## Suggested catalog entry for `root_AGENT_ENVIRONMENT_ARCHITECTURE.md §6`

The current entry for `rootnode-skill-builder` in the runtime tooling catalog should be updated to reflect v2's expanded responsibilities. Suggested text (Aaron applies this to the canonical KF in a separate edit):

```
| `rootnode-skill-builder` | CP | Builds, validates, and packages
deployment-ready Skill files from design specifications. Three pre-build
gates (decomposition / warrant / ecosystem fit) prevent misplaced or
premature Skill builds. Eight-dimension quality gate covers spec
compliance, activation precision, methodology preservation, progressive
disclosure, standalone completeness, auto-activation enforcement,
anti-pattern catalog scan, and 7-layer leak-check. Consumes
process-abstraction handoff briefs from rootnode-repo-hygiene. Produces
ecosystem placement notes, promotion provenance, and AP-warning summaries
as build artifacts. Builds all other rootnode Skills (Producer pattern). |
```

If the catalog uses a different format (table layout, bullet list, etc.), adapt accordingly — the substance is the same.

---

## Migration / extension considerations

**v1-built Skills continue to work unmodified.** v2 is additive — no breaking changes to existing Skill files. Users with v1 installed can replace with v2 without touching any other Skill.

**v2 reviewing v1-built Skills produces 8-dimension verdict with v1's three new dimensions (6, 7, 8) surfaced as advisory warnings only.** Aaron's existing rootnode Skill catalog (21 public + personal versions) will not break under v2 review; v2 will surface advisory warnings against the new dimensions that Aaron can disposition over time.

**Personal install replacement timing:** Immediate. Replace `/mnt/skills/user/rootnode-skill-builder/SKILL.md` and `references/` content with v2 outputs. The two preserved references (`conversion-guide.md`, `skills-spec.md`) inherit unchanged from v1.

**Public catalog ship timing:** Deferred to paired v2.2 release with rootnode-repo-hygiene v1 (per locked decision #11 in the design spec). The paired ship narrative is "v2.2: methodology refresh — skill-builder gates + repo-hygiene scans," which carries more story value than shipping skill-builder alone.

**Backward compatibility sweep:** When v2 ships, run "Review Existing Skill" against the catalog of 21 public Skills to surface any advisory warnings against the new dimensions (auto-activation, AP catches, layer leaks). This produces a maintenance backlog ordered by warning severity. Treat as an opportunistic improvement queue, not a forced migration.

---

## Notes for the canonical KF update (separate edit)

Beyond the §6 catalog entry above, two related KFs may benefit from light updates after v2 ships:

1. **`root_build_context.md` Phase 29 entry** — capture the v2 ship event with reference to the build CV transcript and this placement note. Run the Propagation Checklist against the v2 ship (CI/Memory/KF section update list).

2. **`root_PROJECT_LIFECYCLE_GUIDE.md`** — if the lifecycle guide describes how Skills get built or evolved within the seed Project, update to reflect that the in-Project bootstrap pattern (v1 builds v2) is now precedent, and the design-then-build workflow uses the rootnode-skill-builder Skill rather than a cross-project hop.

These are recommendations, not prescriptions. Aaron applies what's relevant.
