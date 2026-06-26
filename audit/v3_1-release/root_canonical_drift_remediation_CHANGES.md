# Canonical-KF drift remediation — change summary

**Date detected:** 2026-06-25
**Detection method:** canonical-vs-seed `diff` (CRLF-normalized) across all five `audit/canonical-kfs/` files, prompted by stale Phase-32a drafts found lingering in `design/staging-kf/`.
**Scope:** AEA, CC_EG, SBD only. AAP and OPT_REF are excluded (see below).

This is a propagation-gap remediation, **not** a methodology change. Each canonical file is being brought up to the current seed-Project state; no new methodology is authored here. Keep it separate from the v3.1 / Opus-4.8 sync (which touches OPT_REF only).

---

## Root cause

The Phase-32-expansion centralization (~2026-05-09) and later updates revised the seed-Project copies of AEA, CC_EG, and SBD but the corresponding `audit/canonical-kfs/` sync was never completed for those three. At that centralization, AAP and OPT_REF were verified identical to canonical and correctly needed no sync — but the three KFs that *did* change were not pushed. The mirror has been drifting since, undetected because the canonical-vs-seed diff (the O10 staleness check) was not run. The stale Phase-32a drafts sitting in `design/staging-kf/` were the first visible symptom.

---

## Drift inventory (canonical → current seed)

| KF | canonical (stale) | seed (current) | Δ lines | Missing from canonical |
|---|---|---|---|---|
| AEA | 397 | 423 | 28 | §4.13 (multi-lens audit for self-referential validation); §5.5 (KF propagation chain — three landing locations + global CLAUDE.md) |
| CC_EG | 404 | 476 | 82 | §8 (Routines as scheduled CC deployment surface — observation-before-action, daily-triad + weekly-audit); §5.6 (continuation-phrase ambiguity gate); §5.7 (forward-state-aware artifact authoring); Terminology additions |
| SBD | 617 | 726 | 115 | §11 (catalog-wide consistency discipline); §12 (Validate before commit — §12.1 investigation precedes design, §12.2 multi-property elicitation precedes drafting); §3.1 D1 catalog extension; §4.7 paired-output rule |

Section markers verified present in the staged seed copies and absent in canonical via `grep`. Missing-section attribution is by marker, not by exhaustive phase provenance — seed CC_EG (476) and SBD (726) exceed the line counts the Phase-32-expansion build_context entry records (462 / 645), so some content post-dates that entry and is not separately logged in build history (the same Phase 33/34 build-history gap noted elsewhere).

---

## Excluded — correctly

- **AAP** — canonical 363 = seed 363, 0 differing lines. Current. Not synced.
- **OPT_REF** — canonical 1029 is byte-identical to the *pre-4.8* seed; its only pending change is the Opus-4.8 calibration line, which is staged separately and ships with the v3.1 release (manifest = OPT_REF). Not part of this remediation.

---

## Remediation

1. Stage the current seed copies of AEA (423), CC_EG (476), SBD (726) into `design/staging-kf/` — drift manifest, three files, nothing else.
2. Named-file sync `design/staging-kf/{AEA,CC_EG,SBD}.md` → `audit/canonical-kfs/` (no glob).
3. CRLF-normalized `diff` after each; confirm the diff equals the drift inventory above (28 / 82 / 115 lines) and nothing more.
4. Commit (`docs: sync canonical-kfs AEA/CC_EG/SBD to current seed (close Phase-32-expansion propagation gap)`).
5. Clear the three files from `design/staging-kf/` after the verified sync.

Sequence **before** the v3.1 release so the mirror is whole when the catalog ships — but as a distinct commit, not bundled into the OPT_REF/4.8 sync. After this lands, run the canonical-vs-seed diff across all five to confirm the mirror is fully current.

---

*End of canonical-KF drift remediation change summary.*
