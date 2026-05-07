# Anti-Pattern Warnings — rootnode-repo-hygiene v1.0

**Build date:** 2026-05-05
**Source:** Dim 7 anti-pattern catalog scan applied to the Skill itself

## Status: NO WARNINGS

Dim 7 of the 8-dimension validation runs the anti-pattern catalog scan against the Skill being built. For rootnode-repo-hygiene v1.0, no anti-patterns surfaced.

## Patterns scanned and verified clean

The Skill teaches an anti-pattern catalog; Dim 7 verifies the Skill itself does not exhibit those patterns.

| Pattern | Where it could surface in a Skill | Verdict for this Skill |
|---|---|---|
| §2.1 Monolithic standing context | A SKILL.md that absorbs everything (procedures, references, examples) into one document | Clean — content split across SKILL.md (235 lines) + 7 references (140-475 lines each); SKILL.md carries activation + 5 principles + section pointers, not bulk content |
| §4.1 Transcript dump | A SKILL.md that reads like a chat conversation distilled poorly | Clean — content is structured prose, not dialogue; principles, procedures, and examples are declaratively framed |
| §4.3 Manual-only Skills | `disable-model-invocation: true` without `metadata.notes` justification | Clean — flag not set; description has 8 verb-based triggers + symptom triggers + 4 negative triggers for full auto-activation |
| §4.4 Enforcement-as-preference | Skill text describing guarantees as "remember to..." rather than as enforced behavior | Clean — Skill principles are encoded as enforcement-grade behaviors (halt-on-failure, file-state-grounded auth, recommendation-only routing); language is declarative ("Phase 2 reads...", "the Skill does not retry"), not aspirational |
| §4.13 Kitchen-sink session | Skill scope sprawl beyond a single coherent purpose | Clean — scope is bounded (CC-only audit and execution); CP-side patterns explicitly listed as not-scanned in anti-pattern-catalog.md; non-audit work routes to other named Skills |
| §4.14 Stale content | Skill references citing outdated paths or commands | Clean — fresh build; references cite stable canonical sources (root_AGENT_*.md, root_CC_ENVIRONMENT_GUIDE.md) per their current organization |

## Skill-design-specific patterns scanned

Beyond the general anti-pattern catalog, three Skill-design-specific patterns were verified:

| Pattern | Verdict |
|---|---|
| Monolithic SKILL.md | Clean — 235 lines, with detail split to 7 reference files |
| Description over-coupling | Clean — description disambiguates against 4 named adjacent Skills (skill-builder, prompt-compilation, prompt-validation, project-audit) without claiming those Skills' scope |
| Reference duplication | Clean — references cross-reference by file pointer ("see references/sweep-categories.md Cat 1 section") rather than duplicating content |

## Recommendation

No anti-pattern remediation required. The Skill ships as built.

This artifact is produced as part of the standard skill-builder v2 audit set; the absence of warnings is itself a recorded outcome (the audit ran and found nothing).
