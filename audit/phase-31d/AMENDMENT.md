# SKILLS_AUDIT_REPORT_AMENDMENT.md

**Amendment date:** 2026-05-05
**Amends:** `audit/phase-31c/SKILLS_AUDIT_REPORT.md` (Phase 31c, repo SHA `6b2a2e2`)
**Reason for amendment:** Operator review identified C9 verdict misclassifications in both directions, traced to a defect in the C9 §3.1 provenance-discrimination protocol. The original report is preserved as durable record of what the protocol produced; this amendment supersedes the original for Phase 31d planning.

---

## 1. Why this amendment exists

The Phase 31c audit's C9 protocol §3.1 keys provenance discrimination on two frontmatter signals: `metadata.version: "2.0"+` OR `metadata.predecessor:` field present. The protocol treats both signals as proxies for "post-Phase-30 audit-artifact discipline applied at build time."

Operator review confirmed the protocol misclassifies in both directions:

- **False positive (post-discipline classified, actually pre-discipline).** Skills with high version numbers from iterative improvements over time can carry `version: "2.0"+` without having been built under the post-Phase-30 discipline. Version numbers are per-Skill convention, not standardized discipline markers.
- **False negative (pre-discipline classified, actually post-discipline).** First-of-kind builds under the post-Phase-30 discipline can carry `version: "1.0.x"` with no predecessor field (because they have no predecessor — they're new). The protocol misses them.

The operator's project memory is the authoritative source for which Skills were built under the discipline. Per that record, the in-flight builds with new-discipline application are: cc-design, repo-hygiene, critic-gate, mode-router, handoff-trigger-check, profile-builder (the "6 CC Skills built with skill-builder v2"), plus skill-builder v2 itself. No others.

This amendment corrects the C9 verdicts based on that authoritative classification.

## 2. Verdict corrections

Seven verdict changes total. Two reclassify from `ADVISORY` to `N/A` (false positives). Five reclassify from `N/A` to `PASS` (false negatives, all with required artifacts uploaded). One additional Skill stays in `ADVISORY` pending artifact upload (skill-builder v2 — operator located the artifacts post-audit; verdict updates to `PASS` once filed in `audit/build-artifacts/rootnode-skill-builder/`).

| Skill | Original verdict | Corrected verdict | Reason |
|---|---|---|---|
| rootnode-behavioral-tuning v2.0 | ADVISORY — artifacts not uploaded | **N/A — predates discipline** | False positive: v2.0 version predates Phase 29 / Phase 30 builds |
| rootnode-context-budget v5.0 | ADVISORY — artifacts not uploaded | **N/A — predates discipline** | False positive: v5.0 version predates Phase 29 / Phase 30 builds |
| rootnode-skill-builder v2.0 | ADVISORY — artifacts not uploaded | **PASS** (after upload) | Operator located artifacts post-audit; upload to `audit/build-artifacts/rootnode-skill-builder/` resolves |
| rootnode-critic-gate v1.0.2 | N/A — predates discipline | **PASS** | False negative: post-discipline first build; placement note uploaded; required set complete (no predecessor → promotion provenance optional; no D7 catches → ap_warnings optional) |
| rootnode-handoff-trigger-check v1.1.2 | N/A — predates discipline | **PASS** | False negative: post-discipline first build; placement note uploaded |
| rootnode-mode-router v1.0.2 | N/A — predates discipline | **PASS** | False negative: post-discipline first build; placement note uploaded |
| rootnode-profile-builder v1.0.2 | N/A — predates discipline | **PASS** | False negative: post-discipline first build; placement note uploaded |
| rootnode-repo-hygiene v1.0 | N/A — predates discipline | **PASS** | False negative: post-discipline first build; full required set uploaded (placement, ap_warnings, promotion_evidence) |

## 3. Updated aggregate C9 summary

| Source | PASS | PASS-WITH-CAVEAT | FAIL | ADVISORY | N/A |
|---|---|---|---|---|---|
| Original report | 1 | 0 | 0 | 3 | 23 |
| Amendment (corrected) | 7 | 0 | 0 | 0 | 20 |

Other category aggregates (C1–C8) are unchanged.

## 4. Reduced Phase 31d scope

The original report's Phase 31d handoff §1 ("Audit-artifact retention gap on 3 post-discipline Skills") collapses to a single action: file skill-builder v2 artifacts in `Projects/ROOT/research/` (artifacts located, action is filesystem-only). behavioral-tuning and context-budget have no post-discipline artifacts to locate — they predate the discipline.

The original report's Phase 31d handoff §2 ("Provenance-signal protocol asymmetry on 5 Skills") expands in scope: the protocol bug is bidirectional, not unidirectional. The Phase 31d remediation must address both misclassification directions. Recommended fix: replace the C9 §3.1 frontmatter-only protocol with a discipline-marker convention — post-discipline Skills carry an explicit `metadata.discipline_post: phase-30` (or equivalent) frontmatter field added by skill-builder at build time. Future audits read the marker directly; no inference from version semantics.

For Skills already shipped without the marker, retroactive addition is a one-line frontmatter edit per Skill, applied at Phase 31d to the 7 confirmed post-discipline Skills (cc-design, repo-hygiene, critic-gate, mode-router, handoff-trigger-check, profile-builder, skill-builder).

## 5. New finding surfaced during amendment review

Brand-cleanliness leak in pre-discipline Skills. The audit did not scan for `metadata.original-source` references to project-specific build briefs (e.g., `rootnode_context_budget_v5_enhancement_brief.md`, `Skill Design Spec: Brief Builder & Ecosystem Intelligence`). These references leak build-time scaffolding into user-facing frontmatter. The brand-cleanliness discipline is canonicalized in `root_AGENT_ENVIRONMENT_ARCHITECTURE.md §4.10` (added Phase 31a) but is not in C7's anti-pattern subset or C8's leak-check categories.

Phase 31d remediation candidates:
- Cleanup: pass over pre-discipline Skills' `metadata.original-source` fields; replace project-specific brief references with canonical KF references (where applicable), generic anonymized text, or remove the field if no agnostic source exists.
- Methodology: add a brand-cleanliness scan dimension to the audit criteria (proposed C10, separate concern from C7 anti-patterns and C8 mechanism leaks).

## 6. Disposition

- **Original report:** preserved at `audit/phase-31c/SKILLS_AUDIT_REPORT.md`. Durable record of what the C9 protocol produced. Not modified.
- **Amendment:** filed at `audit/phase-31c/SKILLS_AUDIT_REPORT_AMENDMENT.md`. Supersedes original for Phase 31d planning.
- **Both files** uploaded to seed Project for Phase 31d intake.

## 7. Audit-protocol learning captured

The C9 §3.1 protocol defect is a methodology finding worth durable record beyond Phase 31d execution. Adding to seed Project methodology backlog:

- Frontmatter version fields are unreliable as discipline-discriminators. Use explicit discipline markers instead.
- Audit protocols that infer state from heuristic signals should include an operator-override mechanism (analogous to R5's pre-flight overrides) so authoritative human knowledge can correct heuristic misclassifications without protocol violations.
- Phase 31c's amendment workflow (preserve original, supersede via amendment) is the right pattern when audit findings need correction post-completion. Adopt as convention.

---

*This amendment is filed alongside the original Phase 31c audit report. Phase 31d consumes both — the original for protocol-output record, the amendment for authoritative findings.*
