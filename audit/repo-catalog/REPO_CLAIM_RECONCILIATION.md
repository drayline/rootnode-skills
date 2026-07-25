# REPO_CLAIM_RECONCILIATION.md — repo-fact claim inventory
_Generated 2026-07-24, branch `chore/repo-reconciliation` | Basis: `audit/repo-catalog/root_repo_catalog_20260724.md`_

Grep patterns applied across tracked `*.md`: `\.py\b`, `repo[- ]root`, `package_`, `build_`, `generate_release`, `create_releases`, `audit/`, `design/`, `docs/`, `release-notes/`, `canonical-kfs`, `scripts?/`.

Every claim below is checked against today's catalog. Grouped by verdict.

---

## FALSE — repo-fact claims contradicted by the catalog

Six in-scope FALSE claims across `docs/root_SKILLS_RELEASE_PLAYBOOK.md` and repo `CLAUDE.md`. All trace to a single misconception: that `package_skill.py` is a tracked repo file. It is not — `git ls-files` returns zero matches. The correct framing is documented at [build_release_artifacts.py:7](build_release_artifacts.py#L7), which itself explains the file as *upstream* origin ("supersedes the manual two-script dance (build_releases.py for flat + package_skill.py for wrapper)") and at [rootnode-skill-builder/references/tooling-layer-overview.md:62](rootnode-skill-builder/references/tooling-layer-overview.md#L62) ("Adapted from upstream `package_skill.py`"). `package_skill.py` appears to have been the upstream Anthropic skill-creator packager that the orchestrator replaced. It has no tracked presence in this repo.

Similarly, `generate_release_notes.py` and `create_releases.py` are framed in the playbook as repo-root helpers alongside the packager. Both actually live at `audit/v3_1-release/`, and both are **v3.1-cycle artifacts** (verified: docstring says "Assemble v3.1 release notes", writes to `release-notes/<skill>-v3.1.md`, `CP_ONLY`/`CC_ONLY`/`DUAL` lists are static v3.1 enumerations). They are not reusable release tooling.

| # | File:Line | Claim | Verdict | Correct value |
|---|---|---|---|---|
| F1 | [docs/root_SKILLS_RELEASE_PLAYBOOK.md:45](docs/root_SKILLS_RELEASE_PLAYBOOK.md#L45) | "\`package_skill.py\` — produces the **wrapper** shape only, `.skill` extension, no suffix (legacy half)." | **FALSE** | `package_skill.py` is not a tracked repo file. It is the historical *upstream* Anthropic skill-creator packager from which `build_release_artifacts.py` ported wrapper logic. The wrapper shape is now produced directly inside the orchestrator (see [build_release_artifacts.py:61](build_release_artifacts.py#L61) "Exclusions ported from package_skill.py"). There is no legacy half to keep. |
| F2 | [docs/root_SKILLS_RELEASE_PLAYBOOK.md:46](docs/root_SKILLS_RELEASE_PLAYBOOK.md#L46) | "\`generate_release_notes.py\`, \`create_releases.py\` — notes-assembly and release-blast helpers." (Framed alongside repo-root packagers in the same §1.3 list.) | **FALSE about location and status** | Both files exist but at `audit/v3_1-release/` (see catalog "Tracked file tree"), and both are v3.1-cycle-hardcoded artifacts. Not reusable release tooling. A v4.0 release cannot use them as-is. |
| F3 | [docs/root_SKILLS_RELEASE_PLAYBOOK.md:48](docs/root_SKILLS_RELEASE_PLAYBOOK.md#L48) | "Neither \`build_releases.py\` nor \`package_skill.py\` alone produces a correct release set … Keep all of these tracked in the repo; an untracked packager means the next release has no packager." | **FALSE about `package_skill.py`** (does not exist as a tracked file). `build_releases.py` claim is TRUE. The "Keep all tracked" guidance is unenforceable for a file that does not exist. |
| F4 | [docs/root_SKILLS_RELEASE_PLAYBOOK.md:139](docs/root_SKILLS_RELEASE_PLAYBOOK.md#L139) | "SBD §4.7 refinement (three fixes — **being applied this cycle**) … the wrapper script is \`package_skill.py\` (not \`package_zip.py\`) and emits `.skill` while the orchestrator emits `.zip`." | **FALSE** | Same as F1. The "being applied this cycle" language is stale — this line describes v3.1 propagation debt that was resolved, at least in the orchestrator source, differently than the doc records. |
| F5 | [CLAUDE.md:110](CLAUDE.md#L110) | "The underlying shapes come from \`build_releases.py\` (flat) and \`package_skill.py\` (wrapper); neither suffixes nor routes by surface, which is why the orchestrator exists." | **FALSE about `package_skill.py`** | The wrapper logic is *inside* the orchestrator, not a sibling script. `build_releases.py` clause is TRUE. |
| F6 | [CLAUDE.md:112](CLAUDE.md#L112) | "the repo-level wrapper tool is \`package_skill.py\` (emits `.skill`), and the orchestrator emits `.zip`." | **FALSE** | Same as F5. The line's follow-up disambiguation of `scripts/package_zip.py` remains TRUE and useful — keep it, but attach it to a correct antecedent. |

**Correction pattern for all six:** replace repo-root packager claims with "the wrapper shape is produced by `build_release_artifacts.py` directly (upstream origin: Anthropic's `package_skill.py`, whose exclusion rules were ported into the orchestrator)." Replace §1.3 restatement of repo contents with a pointer: *"For the authoritative packager inventory, see `audit/repo-catalog/`."*

---

## OUT-OF-SCOPE FALSE — belongs to the v4.0 canonical-KF session

The same `package_skill.py` misconception is embedded in a canonical KF. Per this session's out-of-scope list and the return-to-chat trigger for canonical-KF contradictions, these are recorded here for the v4.0 session to correct as part of the SBD recalibration.

| # | File:Line | Claim | Verdict | Route |
|---|---|---|---|---|
| K1 | [audit/canonical-kfs/root_SKILL_BUILD_DISCIPLINE.md:335](audit/canonical-kfs/root_SKILL_BUILD_DISCIPLINE.md#L335) | "\`package_skill.py\` — wrapper shape only, `.skill` extension, single-skill, no suffix." | **FALSE** | v4.0 W1 step 6 (SBD audit) — carry as a §4.7 refinement item. Do not edit in this session (canonical KF is Tier 1 mirror-exact; edit path is seed Project → staging → sync). |
| K2 | [audit/canonical-kfs/root_SKILL_BUILD_DISCIPLINE.md:337](audit/canonical-kfs/root_SKILL_BUILD_DISCIPLINE.md#L337) | "Keep all three tracked in the repo — an untracked packager means the next release has no packager." | **FALSE about "all three"** — no third packager to track. | Same as K1. |

The design working spec [design/root_DS_skill_builder_v3_rev3.4.md:355](design/root_DS_skill_builder_v3_rev3.4.md#L355) also references upstream `package_skill.py`, but does so *correctly* as historical attribution ("adapted from upstream `package_skill.py`"). TRUE; no correction.

---

## TRUE — asserted and confirmed

Only the material claims about the packager toolchain are enumerated; header/label matches are omitted for brevity.

| # | File:Line | Claim | Basis |
|---|---|---|---|
| T1 | [docs/root_SKILLS_RELEASE_PLAYBOOK.md:43](docs/root_SKILLS_RELEASE_PLAYBOOK.md#L43) | "`build_release_artifacts.py` — THE release packager." | Tracked at repo root; see [build_release_artifacts.py:1-15](build_release_artifacts.py#L1-L15) header. |
| T2 | [docs/root_SKILLS_RELEASE_PLAYBOOK.md:44](docs/root_SKILLS_RELEASE_PLAYBOOK.md#L44) | "`build_releases.py` — produces the **flat** shape only, no suffix, no surface routing, no bundle (legacy half)." | Tracked at repo root; matches the orchestrator's characterization at [build_release_artifacts.py:7](build_release_artifacts.py#L7). |
| T3 | [docs/root_SKILLS_RELEASE_PLAYBOOK.md:65](docs/root_SKILLS_RELEASE_PLAYBOOK.md#L65) | Pre-flight §3: "Confirm `build_release_artifacts.py` is present". | Present. |
| T4 | [docs/root_SKILLS_RELEASE_PLAYBOOK.md:70](docs/root_SKILLS_RELEASE_PLAYBOOK.md#L70) | "Commit `build_release_artifacts.py` if not yet tracked." | Already tracked; forward-conditional phrasing is fine but stale in effect. |
| T5 | [docs/root_SKILLS_RELEASE_PLAYBOOK.md:78](docs/root_SKILLS_RELEASE_PLAYBOOK.md#L78) | "Package: `python build_release_artifacts.py` → 29 zips (self-asserted) + `dist/rootnode-catalog-vN.zip` bundle on the full build." | Consistent with orchestrator behavior (asserts count, produces bundle). |
| T6 | [CLAUDE.md:103-106](CLAUDE.md#L103-L106) | Surface map: 22 cp-only + 3 cc-only + 2 dual = 29 artifacts from 27 source folders. | Matches Skills subdirectory count in catalog (27 rootnode-* source folders). |
| T7 | [rootnode-skill-builder/references/tooling-layer-overview.md:62](rootnode-skill-builder/references/tooling-layer-overview.md#L62) | "\`package_zip.py\` … Adapted from upstream `package_skill.py`." | TRUE historical attribution (upstream, not tracked here). |
| T8 | [CLAUDE.md:112](CLAUDE.md#L112) (second clause) | "the `skill-builder` Skill's internal `scripts/package_zip.py` is a *separate* build-pipeline packager — not the repo-level wrapper tool, and not to be conflated with it." | The disambiguation clause is TRUE and worth keeping; only the "repo-level wrapper tool is `package_skill.py`" antecedent is FALSE (see F6). |

---

## AMBIGUOUS — worth noting, not a defect

| # | File:Line | Claim | Note |
|---|---|---|---|
| A1 | [docs/root_SKILLS_RELEASE_PLAYBOOK.md:46](docs/root_SKILLS_RELEASE_PLAYBOOK.md#L46) | Playbook implies `generate_release_notes.py` / `create_releases.py` are usable release-time helpers. | They exist (at `audit/v3_1-release/`) and are hardcoded to v3.1. A v4.0 release either replays these logic patterns manually with `--notes-file` (per Playbook §2) or promotes them to reusable v-agnostic scripts. This is a tooling decision, not a repo-fact defect — flag as debt. |
| A2 | [docs/root_SKILLS_RELEASE_PLAYBOOK.md:44-48](docs/root_SKILLS_RELEASE_PLAYBOOK.md#L44-L48) | §1.3 restates repo-root packager inventory in prose. | Two-copy failure mode. Even after correcting the false claims, the prose restatement remains a drift risk. Recommend replacing the restatement with a pointer to `audit/repo-catalog/` — see Phase 3 correction pattern. |

---

## Totals

- **FALSE (in-scope):** 6 — all in `docs/root_SKILLS_RELEASE_PLAYBOOK.md` (§1.3 and §6) and repo `CLAUDE.md` (Packaging conventions section).
- **FALSE (out-of-scope, route to v4.0):** 2 — `audit/canonical-kfs/root_SKILL_BUILD_DISCIPLINE.md`.
- **TRUE:** 8 (material — many more label-level matches confirmed and omitted).
- **AMBIGUOUS:** 2 — hardcoded v3.1 helpers and the two-copy restatement pattern.

Total in-scope corrections needed: **6** — four in the playbook (F1–F4), two in CLAUDE.md (F5–F6). All originate from a single stale reference.

## Cross-cutting observation

The dominant failure pattern is **restating repo structure in prose that then decays**. Every FALSE claim above appears in a doc that could have pointed to the catalog instead. Phase 3 should not just correct the six lines — it should replace the packager-inventory prose in §1.3 with a pointer to `audit/repo-catalog/`, so this class of drift cannot recur in the same location.
