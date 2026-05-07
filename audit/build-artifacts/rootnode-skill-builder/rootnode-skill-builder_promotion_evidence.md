# Promotion Provenance: rootnode-skill-builder v2

**Warrant standard:** Met (this is a versioned successor to a shipped Skill, not a net-new build — warrant inherits from v1's track record).

**Date promoted:** 2026-05-04 (Phase 29 build CV)

**Promotion source:** This is a version upgrade (v1.0 → v2.0), not a paste-and-edit template promotion. Warrant evidence is the operational track record of v1 plus the methodology absorption from Phase 27/28 that surfaced the five gaps v2 closes.

---

## Evidence summary

**v1 operational track record (warrant inheritance):**
- v1 shipped in earlier project phase as part of the rootnode-skills v2.1 catalog (21 Skills published 2026-05-01 at `github.com/drayline/rootnode-skills/releases/tag/v2.1`).
- v1 has been used as the build tool for all rootnode Skills in the catalog (Producer pattern in placement note).
- v1's 5-dimension quality gate has produced shipped, working Skills — the Skills in the v2.1 catalog all passed v1's gate. v1 works.

**Methodology absorption surfacing the five gaps (per design spec §1):**
- **Gap 1 — Decomposition check**: Surfaced from Phase 27/28 absorption of `root_AGENT_ENVIRONMENT_ARCHITECTURE.md §4.1` (placement discipline) and `root_CC_ENVIRONMENT_GUIDE.md §1` (7-layer model). Misplaced content is documented in the canonical as the dominant CC failure mode.
- **Gap 2 — Auto-activation discipline**: Surfaced from `root_CC_ENVIRONMENT_GUIDE.md §1.3` and Manual-only Skills anti-pattern (`root_AGENT_ANTI_PATTERNS.md §4.3`).
- **Gap 3 — Warrant check**: Surfaced from `root_CC_ENVIRONMENT_GUIDE.md §4` (agent-warranted test) — applied one layer up to Skill abstraction decisions.
- **Gap 4 — AP catalog scan**: Surfaced from `root_AGENT_ANTI_PATTERNS.md` (the unified catalog itself, which v1 didn't have access to).
- **Gap 5 — 7-layer leak-check**: Surfaced from `root_CC_ENVIRONMENT_GUIDE.md §1` (7-layer model) — applied to Skill-internal content placement.

The five gaps are not speculative — each maps to documented failure modes in the canonical KFs that landed during the Phase 27/28 methodology refresh. v2 addresses these gaps in the build tool that produces all future Skills.

---

## Decision rationale (why version upgrade vs. new Skill)

Considered alternative: ship v2 capabilities as a separate Skill (e.g., `rootnode-skill-builder-pro` or `rootnode-skill-gates`).

Rejected because:
1. **Routing collision risk.** Two Skills with overlapping descriptions (build / review / revise) competing for activation creates exactly the duplication failure Gate 3 prevents in others. Hypocritical to ship v2 as a separate Skill while teaching others not to.
2. **Backward compatibility was achievable.** v1's existing workflows (Build / Review / Revise) preserved unchanged in shape; v2 adds pre-build gates as a layer in front, expands the quality gate from 5→8, adds output artifacts. v1-built Skills continue to work; v2 reviews them advisorially.
3. **Single Skill stays under spec constraints.** v2 SKILL.md is 330 lines (well under 500). Splitting wouldn't have meaningfully reduced complexity per Skill — it would have spread complexity across two Skills.

Versioning convention: v1.0 → v2.0 (major version bump, additive but materially expanded responsibilities). frontmatter `metadata.version: "2.0"` and `metadata.predecessor: "rootnode-skill-builder v1.0"` capture provenance.

---

## Audit trail

This artifact serves as the audit trail for future maintenance. When a future maintainer asks "why does v2 exist? what evidence supported the upgrade?" the answer is documented here:
- v1 worked but had five identifiable gaps surfaced by methodology refresh.
- v2 closes those gaps additively.
- Backward compatibility preserved.
- No alternative architecture (separate Skill) was cleaner.

If at some future point a v3 is considered, the v3 promotion provenance should reference this artifact and document the new evidence justifying that further evolution.
