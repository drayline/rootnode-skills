# rootnode-cc-design Promotion Provenance

**Build event:** v2.0 release (predecessor `rootnode-cchq-design` v1.1.1)
**Build date:** 2026-05-05
**Build CV phase:** Phase 30 D-build
**Skill builder version:** rootnode-skill-builder v2.0
**Author:** rootnode

---

## Warrant inheritance summary

v2.0 inherits warrant evidence from `rootnode-cchq-design` v1.1.1. The v1 → v2 transition is **rename + composition-alignment + REMEDIATE evolution**, not new methodology. No new warrant evidence is required because no new methodology is being introduced — the framework methodology preserved verbatim is what carries the warrant.

**Warrant test pass condition:** "3+ occurrences with documented design lineage." Inherited from v1.1.1's documented production validation; no new claim is made.

## v1.1.1 warrant evidence (inherited intact)

The predecessor v1.1.1 was warranted on:

1. **Production validation at the source CC deployment.** 27/27 ship items completed without a halt violation. 18-WI evolution arc traced through change_log discipline. (Anonymized in v2.0 to "production CC deployment 2026-05-04" per scope-lock §2.5; the evidence is preserved verbatim, the brand anchor is removed.)
2. **Anthropic primary documentation.** docs.claude.com, code.claude.com, official engineering posts (subagents post April 2026, sandboxing post October 2025).
3. **Named-practitioner consensus.** Patterns triangulated across rosmur, obra/superpowers, alexop.dev, Shrivu Shankar, Jose Parreño Garcia, Marc Nuri, others (full list in `references/source-grading-and-tagging.md` §1 Tier 4).
4. **Phase 27 methodology absorption** into root.node seed Project KFs: `root_AGENT_ENVIRONMENT_ARCHITECTURE.md`, `root_CC_ENVIRONMENT_GUIDE.md`, `root_AGENT_ANTI_PATTERNS.md`. The Skill cites these as canonical; the canonical KFs absorb the methodology, the Skill applies it.

## What is preserved verbatim from v1.1.1 (no new warrant required)

- The five modes: DESIGN, EVOLVE, RESEARCH, TEMPLATE, REMEDIATE
- REMEDIATE two-phase architecture: Phase 1 plan generation → user acceptance → Phase 2 execution with halt-on-failure (no auto-rollback)
- The five action types (`edit` / `create` / `delete` / `modify` / `run`) and 10-check validation grammar
- Authority matrix as mandatory input pattern (3-tier shape canonical; tier definitions stay project-specific)
- 4-agent S/B/C/X verification topology methodology
- 7-layer placement framework structure
- Source discipline (5-tier authority hierarchy) and inline source-tag conventions
- Generalizable-vs-project-specific tagging discipline
- Agent-warranted test, change_log discipline, halt-and-escalate trigger design, files-as-context discipline, additive evolution

## What evolves in v2.0 (composition-alignment, not new methodology)

These are **alignments to upstream Producer contracts (`rootnode-repo-hygiene` v1) and seed-KF canonicals**, not new claims:

| Change | Source of authority | Evidence type |
|---|---|---|
| Skill rename `cchq-design` → `cc-design` | Phase 28 Stage 4 propagation (`root_AGENT_ENVIRONMENT_ARCHITECTURE.md §6.1`) | Documentation alignment |
| Three approval forms (blanket / fragmented / conditional) | `rootnode-repo-hygiene` §"Authorization discipline" (verified against built artifact 2026-05-05) | Cross-Skill contract alignment |
| `critic_gate_threshold: required \| optional` | `rootnode-repo-hygiene` §"Profile selection" + §"Composition" (verified against built artifact 2026-05-05) | Cross-Skill contract alignment |
| Step-level `risk:` field (enum `high \| medium \| low`) | Mechanical consequence of conditional approval form | Schema necessity |
| Finding-ID pattern `^F-\d+\.\d+$` | repo-hygiene's `F-{cat}.{n}` format (verified) | Cross-Skill contract alignment |
| `addresses` → `addresses_finding` field rename | Terminology consistency with repo-hygiene's "finding ID" language | Within-scope-lock material finding |
| AP-N → canonical `§X.Y` numbering | `root_AGENT_ANTI_PATTERNS.md` (Phase 27 unified catalog) | Documentation alignment |
| `cchq-methodology-patterns.md` → `cc-methodology-patterns.md` (rename + restructure) | Mechanical consequence of Skill rename + repo-hygiene §6 preamble pattern | Documentation alignment |
| `cc-anti-patterns.md` substantive rebuild | Q5 reversal: canonical numbering throughout (mandated by repo-hygiene §6.2) | Documentation alignment + cross-Skill contract |
| Hyge full anonymization to "production CC deployment 2026-05-04" | repo-hygiene's `worked-example.md` discipline | Brand-surface cleanliness |

## Warrant gap analysis (none surface)

No methodological change introduces a claim that lacks warrant. The v2 evolution items are either:
- **Mechanical consequences** of locked decisions (rename, schema field renames, AP-N migrations);
- **Composition-alignments** to a verified Producer (repo-hygiene v1 built artifact); or
- **Brand-surface cleanups** that preserve evidence intact (hyge anonymization).

No item introduces a new claim about CC behavior, MCP capability, or agent design pattern that would require fresh warrant evidence.

## Cross-Skill contract verification (R6 mitigation)

Build CV re-verified the cross-Skill contracts against `rootnode-repo-hygiene` v1 built artifact at build time (extracted from `rootnode-repo-hygiene.zip` to `/home/claude/repo_hygiene_v1/`). Verification reads:

- Authorization section confirms three-form blanket / fragmented / conditional model with finding-ID granularity (`F-X.1`, `F-X.3`).
- Profile selection section confirms `critic_gate_threshold: required | optional` two-value field.
- Composition section confirms Cat 1–10 → repo-hygiene Phase 2; Cat 11–14 + leaks → cc-design REMEDIATE routing.
- No drift detected between built artifact and design spec §1.2 contracts.

## Predecessor metadata field

v2.0 frontmatter carries `metadata.predecessor: "rootnode-cchq-design v1.1.1"` for traceability. This makes the inheritance lineage machine-readable and supports future audit of which Skills are evolution lineages vs. fresh builds.

## Roadmap item (deferred from v2.0)

The bidirectional handoff with repo-hygiene — REMEDIATE surfacing methodology-generalizable patterns to `rootnode-skill-builder` v2 Gate 2 (parallel to repo-hygiene's Cat 14 process-abstraction handoff per repo-hygiene SKILL.md §"Composition" line referencing skill-builder v2's Gate 2 exception clause) — is not modeled in v2.0. Defer to v2.x post-v2.0 ship.

---

*This promotion provenance is produced as a Step 0 audit artifact during the v2.0 build CV. It documents the v1.1.1 → v2.0 inheritance lineage and the alignment-vs-new-methodology distinction. File to `Projects/ROOT/research/`.*
