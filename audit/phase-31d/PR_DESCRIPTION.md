# Phase 31d remediation: D9 quality gate + brand-cleanliness sweep + methodology updates

**Note:** This PR consolidates Phase 31d work to main without cutting a v2.2 release. v3.0 will be the next tagged release and will include this work.

## Summary

This PR consolidates the post-v2.1 Skill development baseline (6 new CC governance Skills + skill-builder v1→v2 rebuild) alongside the Phase 31c audit remediation and Phase 31d catalog-wide brand-cleanliness, discipline-marker, and quality-gate updates. Total: **11 commits** on `main..HEAD` covering pre-prep setup, the seven Phase 31d work-queue items, a pre-merge cleanup, and a post-execution audit-artifact commit. CP-targeted Skill zips are built locally in `dist/`; release packaging is deferred to v3.0.

## What ships

### Post-v2.1 Skill development (commit `1f85d19`)

7 Skills baselined into the branch as the post-v2.1 development starting point:

- **rootnode-cc-design** (new, v2.0) — Designs Claude Code prompts and CC environments; modes: DESIGN, EVOLVE, RESEARCH, TEMPLATE, REMEDIATE.
- **rootnode-critic-gate** (new, v1.0.2) — Independent re-derivation gate for proposed changes during autonomous CC execution; 4-check protocol.
- **rootnode-handoff-trigger-check** (new, v1.1.2) — Gates CP→CC readiness against 7 conditions (spec stability, verification surface, invariants documented, etc.).
- **rootnode-mode-router** (new, v1.0.2) — Selects active profile from triggering context (calendar/time/manual override); deterministic precedence.
- **rootnode-profile-builder** (new, v1.0.2) — Builds runtime-Skill profile JSONs against installed schemas via guided interview.
- **rootnode-repo-hygiene** (new, v1.0) — Two-phase audit of CC repos: 14-category sweep + 7-layer leak check + executable [APPROVED] markers.
- **rootnode-skill-builder** (v1 → v2.0 rebuild) — Adds three pre-build gates (decomposition, warrant, ecosystem fit) and expands the publication review to 8 dimensions in v2 (then 9 in v2.1 per Phase 31d B2.1 below).

### Phase 31d remediation (commits `e83d0f1` through `b3f2d8a`)

| Item | Commit | One-line |
|---|---|---|
| B1.1 | (no commit) | **SKIPPED** per Q-31d-3 default — operator did not override the audit-clone-discard default. Folder rename `audit/build-artifacts/rootnode-handoff-trigger/ → rootnode-handoff-trigger-check/` not applicable (the source folder doesn't exist on this branch). |
| B1.2 | `e83d0f1` | block-selection — added "if available" qualifier on two cross-Skill description refs to match the file's consistent pattern. |
| B1.3 | `61edfdc` | brand-cleanliness pass on `metadata.original-source` for 4 Skills (context-budget, project-brief, session-handoff, behavioral-tuning). |
| B1.4 | `a8f7a0e` | added `metadata.discipline_post: phase-30` to 7 post-Phase-30 Skills (cc-design, critic-gate, handoff-trigger-check, mode-router, profile-builder, repo-hygiene, skill-builder) per `root_SKILL_BUILD_DISCIPLINE.md` §4.6. |
| B1.5 | `a0f500f` | updated skill-builder template / spec reference to emit `discipline_post: phase-30` on every new build (D1 spec-compliance going forward per §4.6). |
| B2.1 | `1136d7d` | added D9 (behavioral validation, RECOMMENDED) to the skill-builder quality gate; D9 verbatim canonical text in `references/skills-spec.md`; count refs updated 8→9 throughout body; D1–D9 self-pass walked and operator-approved. |
| B2.2 | (no commit) | **no-change branch** — `rootnode-repo-hygiene/references/sweep-categories.md` Cat 12 already cites canonical `§4.2` by section number; the upstream MCP-bloat expansion is consumed automatically. Logged in `B2_CONFIRMATIONS.md`. |
| B2.3 | `9b640c1` | appended Language Calibration section to `behavioral-tuning/references/countermeasure-templates.md` — Meincke et al. (2025, N=28,000) persuasion-compliance research grounding for countermeasure language design. |
| B2.4 | `b3f2d8a` | logged no-change confirmations for 4 Skills (critic-gate, mode-router, cc-design, handoff-trigger-check) per `SKILLS_IMPACT_EVAL.md`; bundled the B2.2 no-change log per WORK_QUEUE.md verify language. |

### Pre-merge cleanup (commit `ef61217`)

`CLAUDE.md` and `WORK_QUEUE.md` removed. They were branch-local CC session tooling for the Phase 31d execution; durable record of the work is preserved at `audit/phase-31c/`, `audit/phase-31d/`, and `audit/canonical-kfs/`.

### Build artifacts (`dist/`)

24 CP-relevant Skill zips built locally via `build_releases.py`, total 560 KB. CC-only Skills (`rootnode-critic-gate`, `rootnode-mode-router`, `rootnode-repo-hygiene`) intentionally excluded from the CP build per release-engineering scope. `rootnode-cc-design` is included per its dual-surface positioning (DESIGN/EVOLVE/RESEARCH/TEMPLATE modes are CP-native; REMEDIATE is CC-specific but the Skill is invokable from CP). These zips are not attached to any GitHub release in this PR — distribution is deferred to v3.0.

| Zip | Size |
|---|---|
| rootnode-anti-pattern-detection.zip | 5.6 KB |
| rootnode-behavioral-tuning.zip | 16.4 KB |
| rootnode-block-selection.zip | 32.0 KB |
| rootnode-cc-design.zip | 75.0 KB |
| rootnode-context-budget.zip | 25.9 KB |
| rootnode-domain-agentic-context.zip | 17.5 KB |
| rootnode-domain-business-strategy.zip | 16.2 KB |
| rootnode-domain-content-communications.zip | 16.4 KB |
| rootnode-domain-research-analysis.zip | 21.6 KB |
| rootnode-domain-software-engineering.zip | 15.7 KB |
| rootnode-full-stack-audit.zip | 18.8 KB |
| rootnode-global-audit.zip | 17.7 KB |
| rootnode-handoff-trigger-check.zip | 27.3 KB |
| rootnode-identity-blocks.zip | 11.3 KB |
| rootnode-memory-optimization.zip | 16.1 KB |
| rootnode-output-blocks.zip | 14.3 KB |
| rootnode-profile-builder.zip | 20.9 KB |
| rootnode-project-audit.zip | 13.0 KB |
| rootnode-project-brief.zip | 9.0 KB |
| rootnode-prompt-compilation.zip | 21.3 KB |
| rootnode-prompt-validation.zip | 14.9 KB |
| rootnode-reasoning-blocks.zip | 23.9 KB |
| rootnode-session-handoff.zip | 14.2 KB |
| rootnode-skill-builder.zip | 45.9 KB |

## Tier 3 decisions

Two Tier 3 escalations during Phase 31d, both resolved via operator approval (R2 fallback path; see Methodology observation #2 below).

### B1.3 — Brand-cleanliness wording (4 Skills, operator-approved)

| Skill | Operator-approved replacement |
|---|---|
| `rootnode-context-budget` | `original-source: root_OPTIMIZATION_REFERENCE.md` (§3.6 priority 1, canonical KF) |
| `rootnode-project-brief` | `original-source: "Seed-project methodology synthesis"` (§3.6 priority 2, anonymize without date) |
| `rootnode-session-handoff` | `original-source: "Seed-project methodology synthesis"` (§3.6 priority 2, anonymize without date) |
| `rootnode-behavioral-tuning` | `original-source: "OPTIMIZATION_REFERENCE.md, CLAUDE_OPTIMIZATION_NOTES.md"` (§3.6 priority 3, removed project-internal third item; canonical KFs preserved) |

### B2.1(d) — skill-builder D1–D9 self-pass (operator-approved after one REQUEST_CHANGES cycle)

First surfacing returned REQUEST_CHANGES (operator asked for explicit verification grep output and explicit description-state confirmation). Second surfacing — after running `grep -rni "8.dimension|eight.dimension" rootnode-skill-builder/` (returned zero matches) and revising D2 reasoning to note that the description was updated (count language only; trigger phrases unchanged; chars 978 unchanged from pre-B2.1) — returned APPROVE. One revise cycle, well within the 3-cycle cap.

D1–D9 verdict: all PASS (D9 PASS-credible per the v2.1 RECOMMENDED disposition). Walkthrough preserved in `audit/phase-31d/B2_CONFIRMATIONS.md`.

## Methodology observations

Six patterns surfaced during execution that warrant capture in the seed Project methodology backlog:

1. **Single-byte ASCII substitution preserves char count.** B2.1(b) `8` → `9` was zero-delta on the description char count. Worth a note in `root_SKILL_BUILD_DISCIPLINE.md` §5 token-budget discipline that count-reference updates within fixed-size character windows can be applied without budget concerns.

2. **R2 critic-gate fallback validated under load — but masked a real gap.** Phase 31d's two Tier 3 escalations (B1.3 wording, B2.1(d) self-pass) resolved correctly via direct operator approval. The fallback works. However, post-execution investigation (`audit/phase-31d/CRITIC_GATE_ROOT_CAUSE.md`) found the agent should have invoked `rootnode-critic-gate` directly — the Skill was installed at `~/.claude/skills/rootnode-critic-gate/`, had no `disable-model-invocation` flag, and was enumerated in the agent's available-skills list at conversation start. Root cause: agent reasoning error (inferred unavailability from the wrong signal). Prevention: add explicit Skill-availability enumeration to CC pre-flight discipline (e.g., `root_CC_ENVIRONMENT_GUIDE.md` R5) — agents must verify expected runtime tooling appears in their loaded available-tools list at session start, not infer availability mid-session.

3. **No-change branch as first-class outcome.** B2.2 collapsed to "log + skip commit" cleanly — the canonical KF expansion was in-place upstream and the sweep already cited the catalog by section number, so no behavioral change to the Skill was warranted. Worth codifying in remediation work-queue templates: every audit-driven work item should carry an explicit no-change branch with confirmation-log-only disposition, separate from the change branch's commit path.

4. **CLAUDE.md R5 needs Skill-availability check.** See observation #2 and `audit/phase-31d/CRITIC_GATE_ROOT_CAUSE.md` for evidence. Pre-flight should verify expected runtime tooling is loadable via the agent's actual available-tools enumeration, not just present in the repo source tree. The presence-vs-availability distinction is the load-bearing one.

5. **CP/CC build separation is a first-class release concern — and the classification logic itself needs evidence discipline.** The Phase 31d build outputs deliberately exclude CC-only governance Skills (critic-gate, mode-router, repo-hygiene) from the CP-targeted release. The initial classification proposal mistakenly excluded `rootnode-cc-design` based on its category-tag alone; operator review found explicit dual-surface positioning in its SKILL.md ("This Skill operates in both chat-based design conversations (CP) and Claude Code (CC)") and corrected the include/exclude split to 24/3. **Lesson:** when proposing a CP/CC split for release packaging, check positioning evidence (SKILL.md body, frontmatter `metadata`, changelog deployment-target notes) on BOTH the inclusion and exclusion sets — not only the inclusions. The classification logic should be evidence-grounded on both sides of the split. Worth documenting in the release-engineering process.

6. **Build-script Unicode robustness on Windows.** First invocation of `python build_releases.py` crashed on `UnicodeEncodeError` — the script's L68 print statement uses `→` (U+2192) which the Windows cp1252 stdout codec can't encode. Workaround was `PYTHONIOENCODING=utf-8 python build_releases.py …` without modifying the script. Worth either ASCII-only print statements, an explicit `sys.stdout.reconfigure(encoding='utf-8')` at script entry, or a documented prerequisite environment variable in the script's docstring. Filed for follow-up release-engineering hygiene.

## Verification

- All Phase 31d work-queue Verify steps PASS. Per-item validation outcomes preserved in the Phase 31d execution summary (commit messages plus `audit/phase-31d/B2_CONFIRMATIONS.md`).
- `skill-builder` D1–D9 self-pass walked and approved (B2.1(d), preserved in `B2_CONFIRMATIONS.md`).
- CP-build outputs verified per Step 3 of the post-execution task: 24/24 zips contain SKILL.md; total 560 KB; `dist/` correctly gitignored (working tree clean post-build).
- `audit/phase-31d/CRITIC_GATE_ROOT_CAUSE.md` documents the methodology observation #2/#4 evidence.

## Files

### Modified per stream

**Stream B1 (Phase 31c audit + amendment remediation):**
- `rootnode-block-selection/SKILL.md` (B1.2 — description tightening)
- `rootnode-context-budget/SKILL.md`, `rootnode-project-brief/SKILL.md`, `rootnode-session-handoff/SKILL.md`, `rootnode-behavioral-tuning/SKILL.md` (B1.3 — original-source field)
- `rootnode-cc-design/SKILL.md`, `rootnode-critic-gate/SKILL.md`, `rootnode-handoff-trigger-check/SKILL.md`, `rootnode-mode-router/SKILL.md`, `rootnode-profile-builder/SKILL.md`, `rootnode-repo-hygiene/SKILL.md`, `rootnode-skill-builder/SKILL.md` (B1.4 — discipline_post marker)
- `rootnode-skill-builder/SKILL.md` L195, `rootnode-skill-builder/references/skills-spec.md` (B1.5 — emit-logic + spec-reference field)

**Stream B2 (CC ecosystem impact eval):**
- `rootnode-skill-builder/SKILL.md`, `rootnode-skill-builder/references/skills-spec.md` (B2.1 — count refs 8→9, D9 brief in body, full canonical D9 verbatim in references)
- `rootnode-behavioral-tuning/references/countermeasure-templates.md` (B2.3 — Language Calibration section appended)
- `audit/phase-31d/B2_CONFIRMATIONS.md` (B2.1(d) self-pass + B2.2 no-change log + B2.4 4-Skill confirmations)

**Pre-merge cleanup:**
- DELETED: `CLAUDE.md`, `WORK_QUEUE.md`

**Build outputs (gitignored, not in commit):**
- `dist/*.zip` (24 files, 560 KB total)

### New files (durable record)

- `audit/phase-31c/SKILLS_AUDIT_REPORT.md`
- `audit/phase-31d/AMENDMENT.md`
- `audit/phase-31d/SKILLS_IMPACT_EVAL.md`
- `audit/phase-31d/B2_CONFIRMATIONS.md`
- `audit/phase-31d/CRITIC_GATE_ROOT_CAUSE.md` (untracked at branch tip — operator's choice on whether to commit before merge or as part of a subsequent audit-artifact commit)
- `audit/canonical-kfs/*.md` (canonical KF copies pre-staged for in-repo agent access)
- `audit/build-artifacts/*` (build placement notes, AP warnings, promotion provenance per the post-Phase-30 audit-artifact discipline)

## Notes for review

- 9 Phase 31d work commits + 1 pre-merge cleanup commit + 1 post-execution audit-artifact commit + 2 pre-prep setup commits = **11 commits on `main..HEAD`**.
- All scope-authorization rules honored during Phase 31d execution — no commits to `main`, no `git push` until this consolidation PR.
- Branch tip prior to merge: post-audit-artifact commit (see PR commit list).
- Build artifacts in `dist/` are local-only; no GitHub release is created in this PR. v3.0 will be the next tagged release and will attach distribution artifacts.
- The two Tier 3 escalations would have benefited from direct critic-gate invocation; see methodology observations #2 and #4. Operator-approval fallback worked correctly but the gap is worth closing in the next pre-flight discipline iteration.
