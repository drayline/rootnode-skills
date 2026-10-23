## Summary

This PR will release catalog v5.0. It recalibrates all 27 Skills for the 5.5 generation (Fable 5.1, Opus 5.5, Sonnet 5.5, Haiku 5.5) and moves every Skill to 5.0.0. The new calibration scope is **Opus 5.5 + Sonnet 5.5 dual-primary**, Fable 5.1 integrated-aware, Haiku 5.5 subagent-aware, Opus 5 / Sonnet 5 fallback-graceful, and Sonnet 4.6 legacy-graceful. Tier structure is unchanged at T1 13 / T2 7 / T3 7.

Governing specs: `design/root_DESIGN_catalog_v5_model_alignment.md`, `design/root_DESIGN_cc-design_v5.md`, `design/root_DESIGN_behavioral-tuning_v5.md`, and the dated landscape block `design/root_MODEL_LANDSCAPE_2026-10.md`. All four were verified by LF digest at pre-flight. **They are untracked in this repo and are not part of this PR** (see Open items).

## Skills, by group

**Calibration only (L, 9).** This PR will replace the calibration line whole with the tier template and bump each Skill to 5.0.0:
rootnode-block-selection (T2) · rootnode-domain-business-strategy · rootnode-identity-blocks · rootnode-memory-optimization (T2) · rootnode-mode-router · rootnode-output-blocks · rootnode-profile-builder · rootnode-project-brief · rootnode-session-handoff

**Calibration plus body edits (L+, 16).** This PR will apply each Skill's catalog-spec §4 row:
rootnode-anti-pattern-detection · rootnode-context-budget · rootnode-critic-gate · rootnode-domain-agentic-context · rootnode-domain-content-communications · rootnode-domain-research-analysis · rootnode-domain-software-engineering · rootnode-full-stack-audit · rootnode-global-audit · rootnode-handoff-trigger-check · rootnode-project-audit · rootnode-prompt-compilation · rootnode-prompt-validation · rootnode-reasoning-blocks · rootnode-repo-hygiene · rootnode-skill-builder

**Structural (S, 2).** This PR will ship:
- **rootnode-cc-design 5.0.0** (predecessor v4.2): hook reference fix, session-report output standard (new `references/cc-session-reports.md`, `report_dir` in the brief schema), delegation hardening, prompt and environment additions.
- **rootnode-behavioral-tuning 5.0.0**: tendency #15 early turn termination, routing surface repaired for 11–15, deployment-conditioning tables rebuilt, Anthropic countermeasure blocks carried verbatim.

9 + 16 + 2 = 27.

## Defects this PR will fix

1. **cc-design hooks taught enforcement-as-preference.** The hook reference showed `exit 1` as blocking and a `"matchers": [...]` schema. Enforcement needs `exit 2` (or exit 0 with JSON `{"decision":"block"}`), and config is a `matcher` string plus a `hooks` array. Every hook built from the old examples silently did not block. repo-hygiene gains the matching audit check.
2. **behavioral-tuning could not route to tendencies 11–14.** v4.0 added them only as a reference-file addendum. The SKILL.md description still said "ten tendencies", and the routing table stopped at #10. This PR repairs the routing surface and adds #15 in the same edits.
3. **The skill-builder taxonomy count was stale.** SKILL.md:121, `references/behavioral-validation.md` :36 / :90, and `references/skills-spec.md` :388 said "10-tendency" (a v4.0 propagation miss). They now say 15.

## Catalog surfaces

- README: the Model Compatibility section and the line-31 calibration note are rewritten. The section now carries an effort-defaults table by model and surface, per-model fallback semantics, and the D6 pin line ("On third-party providers the `haiku` alias may still resolve to Haiku 4.5; pin `claude-haiku-5-5` via `ANTHROPIC_DEFAULT_HAIKU_MODEL`").
- `release-notes/*-v5.0.md` (27, from `audit/v5_0-alignment/release-notes-v5.0-config.py`) and the umbrella `release-notes/catalog-v5.0.md`.
- `CHANGELOG.md`: v5.0 entry appended.
- `.gitignore`: adds `.claude/settings.local.json`.
- `audit/v5_0-alignment/`: the T1 sweep manifest, KF update blocks, release-notes config, session report, and this PR body.

## KF update blocks (surfaced, not applied)

`audit/v5_0-alignment/kf-update-blocks.md` holds **30 blocks across 9 target KFs**: CLAUDE_OPTIMIZATION_NOTES, OPTIMIZATION_REFERENCE (including #15), AUDIT_FRAMEWORK, AGENT_ANTI_PATTERNS, CC_ENVIRONMENT_GUIDE, SKILL_BUILD_DISCIPLINE, AEA §4.14, build_context (O28, O29), and the CI `<knowledge_files>`. Nothing in `audit/canonical-kfs/` changes. The mirror sync follows as a separate PR after the seed KFs absorb the blocks.

## Verification

- **Builder→Refuter loop:** every group was accepted by a fresh, independent Refuter against the spec digest and the diff digest. Two groups (L+B and cc-design) reached the 2-REWORK cap. Each then got one operator-granted, scoped cycle 3, which was accepted.
- **Phase 2 gates T1–T10:** all pass on the first test pass. Calibration parity is 13 / 7 / 7; all 27 Skills are at `"5.0.0"`; every description is ≤ 1024 (cc-design 694 ≤ 700); every body is < 500 lines; the hook-correctness grep is clean; T7 finds 5 routing headings; the reasoning-extraction sweep finds 0. The skill-builder D1–D8 review passes on cc-design and behavioral-tuning. The package dry run gives 24 + 5 = 29. Evidence is in the session report and `5_5GEN_SWEEP_MANIFEST.md`.
- **D9:** D9c is analytical for all Skills. **D9a for cc-design 5.0 is deferred** to the separate validation prompt (`root_CC_PROMPT_v5_0_cc-design_d9a.md`), because a session that built a Skill cannot run its own behavioral validation.

## Open items before Phase B

- **Packager `CATALOG_VERSION` is still `"v4.0"`** (`build_release_artifacts.py:59`). Phase B needs `rootnode-catalog-v5.0.zip`. This one-line bump needs operator authorization; the session prompt scopes packager edits to surface-map changes only.
- **The v5 design specs are untracked in `design/`.** This PR cites them but does not include them.
- **Low-severity next-patch findings:** F11–F22 and F24 in the session report.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
