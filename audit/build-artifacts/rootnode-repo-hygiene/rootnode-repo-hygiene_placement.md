# Placement Audit — rootnode-repo-hygiene v1.0

**Build date:** 2026-05-05
**Built via:** rootnode-skill-builder v2.0
**Design spec:** root_design_repo_hygiene_skill.md (v2.0, root.node-framed)

## File placement verification

12 files produced, all in correct locations:

```
rootnode-repo-hygiene/
├── SKILL.md                                    (235 lines)
├── references/
│   ├── sweep-categories.md                     (475 lines)
│   ├── anti-pattern-catalog.md                 (271 lines)
│   ├── seven-layer-framework.md                (140 lines)
│   ├── execution-discipline.md                 (240 lines)
│   ├── process-abstraction-detection.md        (270 lines)
│   ├── cc-best-practices.md                    (217 lines)
│   └── worked-example.md                       (409 lines)
├── schema/
│   └── profile.schema.json                     (Draft-07 valid)
└── profiles/
    ├── default.json                            (validates)
    ├── quick-scan.json                         (validates)
    └── deep-audit.json                         (validates)
```

## Spec compliance summary (Dim 1)

| Requirement | Target | Actual | Status |
|---|---|---|---|
| `name` (kebab, ≤64) | rootnode-repo-hygiene | rootnode-repo-hygiene (21 chars) | PASS |
| `description` (parsed YAML, ≤1024) | ≤1024 chars | 1018 chars | PASS |
| Trigger phrases in description | ≥8 | 8 | PASS |
| Negative trigger refs | ≥4 | 4 (skill-builder, prompt-compilation, prompt-validation, project-audit) | PASS |
| `license` | Apache-2.0 | Apache-2.0 | PASS |
| `metadata.author` | rootnode | rootnode | PASS |
| `metadata.version` | "1.0" | "1.0" | PASS |
| `metadata.original-source` | references canonical KFs + production validation | 481 chars citing 3 KFs + 2026-05-04 production validation | PASS |
| XML angle brackets in frontmatter | 0 | 0 | PASS |
| Body line count | 280-330 (soft target) | 235 | UNDER (see deviation note) |
| Body line cap | <500 (hard) | 235 | PASS |
| Required structural sections | 15 | 15 | PASS |
| Worked examples | ≥2 | 3 | PASS |

## Reference file targets (design spec §12.2)

| File | Target range | Actual | Status |
|---|---|---|---|
| sweep-categories.md | 420-520 | 475 | PASS |
| anti-pattern-catalog.md | 240-300 | 271 | PASS |
| seven-layer-framework.md | 130-170 | 140 | PASS |
| execution-discipline.md | 280-360 | 240 | UNDER by 40 |
| process-abstraction-detection.md | 200-260 | 270 | OVER by 10 |
| cc-best-practices.md | 180-220 | 217 | PASS |
| worked-example.md | 320-400 | 409 | OVER by 9 |

## Content fidelity verification (design spec §13.3)

| Locked decision | Where preserved | Status |
|---|---|---|
| D6 — Bootstrap heritage carve-out (Cat 1 calibration) | SKILL.md Principle 4 + "Bootstrap heritage handling" section + sweep-categories.md Cat 1 + dedicated section "Bootstrap heritage calibration"; profile.schema.json `bootstrap_heritage` field | PASS |
| D7 — Three commit plan options (A/B/C) | SKILL.md "Commit plan handling" section + execution-discipline.md "Commit plan execution" section | PASS |
| D8 — Process-abstraction scope categorization (project-local vs methodology-generalizable) | SKILL.md "Process-abstraction candidates" section + process-abstraction-detection.md "Scope categorization (D8)" section | PASS |
| D9 — Dual-direction Cat 2 permissions scan (stale-removal + missing-entry) | sweep-categories.md Cat 2 section + SKILL.md Phase 1 step 2 description | PASS |
| D10 — File-state-grounded authorization (no verbal-only fallback) | SKILL.md Principle 1 + "Authorization discipline" section + execution-discipline.md EC-1 | PASS |
| D11 — Defer-to-downstream as first-class commit plan option | SKILL.md Principle 3 + "Commit plan handling" Option + execution-discipline.md "Defer-to-downstream" subsection | PASS |

## Deviation: SKILL.md body line count under target

**Target:** 280-330 lines  
**Actual:** 235 lines (under by 45)

**Assessment:** All 15 required structural sections are present and substantive. All 8+ trigger phrases, all 4 negative triggers, 3 worked examples (above the ≥2 minimum), and 8 troubleshooting entries all present. The shortfall is stylistic (dense paragraph prose vs. line-break-heavy formatting) rather than missing content.

**Decision:** Ship as-is. The 280-330 target is a soft sizing estimate from the spec, not a hard requirement. Hard requirements (frontmatter compliance, section presence, trigger count, examples count, body cap <500) all pass. Adding line breaks for cosmetic compliance would not improve the Skill's behavior or the user's experience.

## Deviations (non-blocking)

- SKILL.md 235 vs 280-330 target: noted above; ship as-is.
- execution-discipline.md 240 vs 280-360 target: file is dense and complete; cleanup_execution_log template + per-category verification table + critic-gate composition rules + commit-plan options all present. Padding for line count would degrade rather than improve.
- process-abstraction-detection.md 270 vs 200-260 target: 10 lines over. Includes 5 production-validated examples per design spec §10 example requirement. Trim would lose validation evidence.
- worked-example.md 409 vs 320-400 target: 9 lines over. Covers full Phase 1 + Phase 2 + closeout per design spec §16; the "What this example demonstrates" 6-point closer adds explanatory value.

## Approvals

Spec compliance: PASS  
Structural placement: PASS  
Content fidelity: PASS  
Ship recommendation: APPROVED
