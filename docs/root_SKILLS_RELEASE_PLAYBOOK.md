# rootnode-skills Release Playbook & Lessons Learned

Canonical runbook for cutting a `drayline/rootnode-skills` catalog release. Read this **before** any release conversation — chat-side planning or CC execution. It exists because the v3.1 release (2026-06-25/26) churned hard on things that were already settled but not written down, and then needed a follow-on UX fix when the umbrella shipped notes-only and the download path was poor. Every decision, convention, and anti-churn rule we landed on — including the post-ship bundle/README fix — is here so the next catalog update is fast and low-friction.

**Companion artifacts.** The executable release prompt (`root_CC_PROMPT_vN_release.md`) is the step-by-step CC prompt for a specific version; this playbook is the *why* and the *standing rules* behind it. Packaging conventions also live in the repo `CLAUDE.md` (`## Packaging conventions`).

**Artifact lifecycle — read this first.** A version-stamped release prompt (e.g., `root_CC_PROMPT_v3_1_release.md`) is **spent once its version ships**. Do not re-edit a spent release prompt to capture a new lesson — it is a record of one execution, not a living document. The durable home for release knowledge is *this playbook* (version-agnostic) plus the repo `CLAUDE.md` packaging section and the committed packager. Each new release **derives its prompt from this playbook** (copy → bump version → adjust deltas), never from the prior spent prompt. The v3.1 bundle/README fix, for instance, lives here and in `build_release_artifacts.py` — it was deliberately *not* back-patched into the spent v3.1 prompt.

---

## 1. Release architecture — the model (never re-derive this)

### 1.1 Two artifact types per catalog version

A catalog release is **27 per-Skill releases + 1 catalog umbrella** — not one bundle.

- **Per-Skill releases.** One GitHub release per Skill, tag `rootnode-<skill>/vN`, carrying that Skill's surface zip(s). This is where the individual downloadable packages live.
- **Catalog umbrella.** One release tagged `catalog-vN`, marked `--latest`, carrying **(a) the catalog-index notes and (b) exactly one bundle asset, `rootnode-catalog-vN.zip`** (all 29 artifact zips packaged together). Its body is the catalog index: a categorized list linking every per-Skill release, plus Architecture and Site sections, plus a `## Download` section pointing at the bundle. It frames the per-Skill releases as one unified system and is what GitHub surfaces as "Latest."

This superseded the **v2.x model** (a single release with all Skill zips attached loose, no per-Skill releases) at v3.0. Do not revert to the all-zips-in-one-release form.

**Umbrella asset rule (revised at v3.1).** The 29 **individual** per-Skill artifact zips are NOT attached loose to the umbrella — they live on their per-Skill releases. The umbrella carries exactly **one** asset: the `rootnode-catalog-vN.zip` bundle (every artifact in one download). This was the v3.1 UX fix. The original v3.1 umbrella shipped **notes-only (zero assets)**, which left users with no single "everything" download and effectively pushed them at GitHub's auto-generated Source-code archives — which are not a usable Skills download and cannot be removed. The bundle asset plus a `## Download` section in the notes steer users past those archives to a real download. (Earlier drafts of this playbook described the umbrella as "notes-only"; that is the pre-UX-fix model and is superseded by this section.)

### 1.2 Packaging shapes and surface mapping

Two zip shapes, one per surface, from the same un-suffixed source folder (`rootnode-<skill>/`):

- **`-cp` = flat.** Contents at the zip root (`SKILL.md`, `references/`, …). CP / Claude.ai Projects upload reads `SKILL.md` at the root.
- **`-cc` = wrapper.** A nested `rootnode-<skill>/` folder containing the contents. CC extracts the folder into `~/.claude/skills/`; a flat `-cc` would extract loose files and break the install.

Surface map (the authoritative assignment):

| Bucket | Count | Skills | Ships |
|---|---|---|---|
| cp-only | 22 | everything not listed below | `-cp` |
| cc-only | 3 | `critic-gate`, `mode-router`, `repo-hygiene` | `-cc` |
| dual | 2 | `skill-builder`, `cc-design` | `-cp` + `-cc` |

→ **29 artifacts = 24 `-cp` (flat) + 5 `-cc` (wrapper)** from 27 source folders. The `-cp`/`-cc` suffix is applied by the packager, never present on the source folder. The umbrella bundle (`rootnode-catalog-vN.zip`) contains all 29 of these artifact zips.

### 1.3 Packaging toolchain

Repo-root script roster is **three** (as of v4.0):

- **`build_release_artifacts.py` — THE release packager.** Single entry point. Reads the surface map, emits flat for `-cp` / wrapper for `-cc`, applies the suffix, and self-asserts 24+5=29 (non-zero exit on mismatch). On a **full build** it also runs `write_bundle()` to archive all 29 artifact zips into `dist/rootnode-catalog-vN.zip` — the umbrella bundle. This is what a release runs. Both shape emitters live inside the orchestrator; wrapper-shape logic is ported from Anthropic's upstream `package_skill.py` (see `build_release_artifacts.py:7` and `:61`), which is **not** a tracked file in this repo.
- `build_releases.py` — flat shape only, no suffix, no surface routing, no bundle. Superseded by the orchestrator; retained as a legacy reference only.
- **`generate_release_notes.py` — the version-agnostic release-notes generator** (added v4.0 per D7 expansion). Takes `VERSION`, `TIER_LABEL`, `CATALOG_RELEASE`, `VARIANT_A/B/C`, and `EXPECTED_COUNTS` from a per-cycle Python config file. Preserves the three variant templates (`-cp` flat / `-cc` wrapper / dual) and the 22+3+2=29-artifact count assertion from the v3.1 artifact it succeeded. Per-cycle configs live under `audit/v<N>-*/` (e.g., `audit/v4_0-alignment/release-notes-v4.0-config.py`).

Historical v3.1 cycle tooling — `audit/v3_1-release/generate_release_notes.py` (the version-hardcoded artifact this repo-root generator succeeded) and `audit/v3_1-release/create_releases.py` — remains as cycle-artifact history at its original path. Do not use it for post-v3.1 releases; use `generate_release_notes.py` at repo root instead.

**Authoritative packager inventory: `audit/repo-catalog/`** (regenerated at the end of every release — see Phase B post-verification step). Where §1.3 and the catalog disagree, the catalog wins and this section is a defect to fix.

### 1.4 Tag naming

- **Per-Skill:** `rootnode-<skill>/vN`. Uniform prefix as of v3.1. (v3.0 had two prefix-less dual-surface tags — `skill-builder/v3.0`, `cc-design/v3.0`. Do not carry that asymmetry forward.)
- **Catalog umbrella:** `catalog-vN` (not `vN` — distinct from per-Skill tags).
- **Bundle asset name:** `rootnode-catalog-vN.zip` — distinct from the umbrella *tag* `catalog-vN`. The asset is what users download; the tag is what the release is keyed on.

---

## 2. Release process — two-phase, branch-protection-aware

`main` is branch-protected (CLAUDE.md halt #1): **no direct commits.** All repo commits land via a `release/vN` branch → PR → operator merge (Phase A). Tags and GitHub releases are created off merged `main` afterward (Phase B), so every tag points at the complete state.

### Pre-flight
1. `git checkout main && git pull`; confirm the alignment/content work has merged (spot-check Skill `version` fields).
2. `gh auth status` authenticated.
3. Confirm `build_release_artifacts.py` is present, its surface map still matches the catalog, and its `write_bundle()` step is intact (bundle is part of a full build).
4. Confirm the staging manifest: `design/staging-kf/` contains exactly the KFs to sync, nothing else (stale drafts pollute the mirror).
5. Confirm the vN README and the `catalog-vN.md` umbrella notes are available, and that the umbrella notes use embedded `[name](url)` links (not bare URLs, not double-wrapped) — see §3 and §4 rule 7.

### Phase A — content PR (all commits; operator merges)
1. Branch `release/vN`. Commit `build_release_artifacts.py` if not yet tracked.
2. **Canonical-KF sync** — named files only, never a glob. Copy each staged KF → `audit/canonical-kfs/` by name; CRLF-normalized `diff` each against its expected delta; **clear staging** after a verified sync.
3. **Release notes** — per-Skill (`release-notes/<skill>-vN.md`) **and** the catalog umbrella (`release-notes/catalog-vN.md`).
4. **README bump** — and point install/download links at **`/releases/latest`** (resolves to the umbrella while it's `--latest`), calling out the bundle. See the README dependency in §3.
5. Push, open PR, **HALT for operator review + merge.**

### Phase B — tags + releases off merged `main`
6. Re-sync to merged `main`; verify the PR landed.
7. **Package:** `python build_release_artifacts.py` → 29 zips (self-asserted) **+ `dist/rootnode-catalog-vN.zip` bundle** on the full build.
8. **Per-Skill releases:** `gh release create <skill>/vN … <zip(s)>` ×27, sequential, halt on any failure.
9. **Catalog umbrella (notes + bundle, `--latest`):**
   - `gh release create catalog-vN --notes-file release-notes/catalog-vN.md --latest` — full categorized index body. Apply notes **via `--notes-file` (raw bytes)**, never by pasting a rendered copy (that is what double-wrapped the links at v3.1 — see §3 / §4 rule 7).
   - `gh release upload catalog-vN dist/rootnode-catalog-vN.zip --clobber` — attach the bundle.
   - The umbrella is **kept as the `--latest` release**. No per-Skill release may be marked `--latest` afterward — the README depends on `/releases/latest` resolving to the umbrella.

### Verification (all must hold)
- Content PR merged; canonical-kfs synced to expected deltas; staging cleared; notes + README on `main`.
- 29 zips, correct cp/cc split and shapes (spot-check a dual, a cc-only, a cp-only); bundle `rootnode-catalog-vN.zip` built.
- 27 per-Skill releases at `<skill>/vN`; dual-surface carry both zips.
- `catalog-vN` umbrella created, `--latest`, body links all 27 and resolves, and carries the **`rootnode-catalog-vN.zip` bundle** as a real download. (GitHub's auto Source-code archives will also appear; they are not a usable Skills download and cannot be removed — the bundle is the answer to that.)
- **Umbrella notes verified BOTH ways:**
  - **Stored body** — `gh release view catalog-vN --json body`: assert `]](` == 0 (no double-wrapped links), `releases/tag/rootnode-` == 27 (all per-Skill links present), `## Download` present.
  - **Rendered page** — open the release page in a browser and confirm the links are clickable, not literal text. An `href` present in the stored body is NOT proof of a clean render (§4 rule 7).
- README install/download links point at `/releases/latest`, resolve to the umbrella, and the umbrella is the only `--latest` release.
- Show `gh release list` as evidence. Banned completion phrases: "should work," "probably fine," "looks good."

### Post-verification — repo catalog regeneration

10. **Regenerate `audit/repo-catalog/`.** After every Verification bullet above passes, produce a fresh `audit/repo-catalog/root_repo_catalog_<YYYYMMDD>.md` matching the section structure of the prior snapshot. Every section derives from a live command (`git ls-files`, `git tag --list`, `gh release list`, `ls`, `git log --oneline -20`), never from memory or the prior catalog. Regenerating **after** verification captures the new per-Skill tags, the umbrella release, and the current `--latest` — running the catalog pre-package would bake in staleness in the Tags and GitHub Releases sections. Commit on `main` via a follow-up hygiene PR (branch protection forbids direct commits); commit message convention `chore(catalog): regenerate for vN`. The catalog is what future sessions read as the ground truth for repo contents; failure to regenerate is what produced the v4.0 pre-flight defect (a month-stale catalog was unreachable and an incorrect playbook became authoritative in its place — see the reconciliation cycle 2026-07-25).

---

## 3. Decisions & conventions (with rationale)

- **Per-Skill releases + notes-plus-bundle umbrella.** Per-Skill releases let users pin and pull individual Skills; the umbrella gives the catalog a single discoverable `--latest` anchor, a changelog, and a one-file "everything" download (the bundle) without forcing users to collect 27 releases. The umbrella carries the bundle, not the 29 loose zips. Chosen at v3.0 (per-Skill + umbrella) and refined at v3.1 (bundle on the umbrella).
- **Bundle on the umbrella; individual zips on per-Skill releases.** Keeps the umbrella a clean index + one "everything" download instead of a long multi-asset scroll (the 29 zips plus the bundle, on top of GitHub's two unremovable auto archives), while per-Skill releases remain the place to pull a single Skill. *Alternative considered:* attach all 29 to the umbrella for zero-navigation single-Skill downloads — left open; revisit only if single-Skill discoverability directly from the umbrella becomes a real need.
- **README → `/releases/latest`, not a pinned `catalog-vN` tag.** Install links auto-track each catalog ship without a per-release README edit. **Dependency:** `/releases/latest` resolves to the umbrella **only while the umbrella stays `--latest`** — so no per-Skill release may be marked `--latest` after the umbrella. Enforced in Phase B step 9 and Verification.
- **Umbrella notes are applied as raw bytes via `--notes-file`, never pasted from a rendered copy.** The v3.1 double-wrapped-link bug (`[[name](url)](url)`, which renders as literal text) came from pasting a rendered-page copy back into the notes — *not* from the link format. Embedded `[name](url)` renders fine (the v3.0 body proved it). The format was never the problem; the application path was. Apply notes from the source markdown file; if a fix is needed post-create, `gh release edit catalog-vN --notes-file <file>`.
- **Two-phase branch model.** Branch protection forbids direct `main` commits, so content (KFs, notes, README) goes through a PR; tags/releases are created off merged `main` so they reference the final state. Conflating these (committing on `main`) bounces against protection.
- **Packaging by surface.** CP upload needs flat; CC install needs the wrapped folder. Wrong shape = install failure, not cosmetics. The suffix encodes the shape.
- **Named-file canonical sync, never a glob.** A blind `cp staging/*.md canonical/` propagates any stale leftover into the mirror. Copy by name, diff each, clear staging after.
- **Catalog umbrella body is the full index, not a summary.** The umbrella's value is the categorized link map to all per-Skill releases (9 functional categories) + Architecture + Site + the `## Download` section. A thin summary defeats the purpose.

---

## 4. Anti-churn rules (the load-bearing part)

The v3.1 session burned roughly a dozen turns on avoidable churn. Every instance traces to **one root cause: acting on partial or remembered state instead of the verified artifact.** These rules are the fix.

1. **Verify release-state facts against the repo, never from memory.** Use the GitHub API / `releases.atom` / `gh release view` to confirm what exists and what it contains. *Drift caused without this:* the false "per-Skill-only, no umbrella" model, and confusion between the v2.x and v3.0 patterns.
2. **Read artifacts in full before building on them. Truncated tool output is a standing trap.** A self-truncated 400-char read of `catalog-v3.0` produced a thin umbrella missing the entire 27-link index — twice. If a tool call truncates, re-fetch the full content before modeling anything on it.
3. **When the operator hands you a screenshot, URL, or file, read *that* artifact — it is the ground truth, not your model of it.** *Caused without this:* the `dist/` vs source-folder inversion (mistaking the build output for the source), repeated across two turns.
4. **Never narrate drift as a deliberate decision.** If a "locked decision" can't be traced to evidence, it's drift — flag it and correct, don't manufacture a rationale. *Caused without this:* a fabricated justification for dropping the umbrella.
5. **Pattern-generated values must be verified to resolve before shipping.** Links, tags, and filenames built from a naming pattern (e.g., `rootnode-<skill>/vN`) must be checked against actual repo state — especially where historical asymmetry exists (the v3.0 prefix-less dual tags).
6. **Run the O10 staleness diff at session start.** `diff` (CRLF-normalized) seed KFs against `audit/canonical-kfs/` before any methodology-touching work. *Caught late without this:* the AEA / CC_EG / SBD canonical drift (~28 / 82 / 115 lines).
7. **Verify the RENDERED/stored artifact, not a proxy signal — and read tool output in full.** A signal that *looks* like success isn't success. An `href` present in a stored body is not proof the page renders the link as clickable: the v3.1 double-wrapped-link bug was dismissed on exactly this wrong-signal check, and then recurred *inside* its own fix. When the deliverable is a rendered page, check the rendered page; when it's a stored body, read the full stored body, not a truncated head; when it's a file on disk, read the file, not your model of what you wrote. This is the playbook-local form of the build_context Self-Optimization Observation "verify the rendered/stored artifact, not a proxy signal; read tool output in full," and it is the deepest root of the v3.1 churn.

---

## 5. Propagation map — where this is formalized

| Knowledge | Home |
|---|---|
| Release model, process, anti-churn rules (this doc) | Repo `docs/root_SKILLS_RELEASE_PLAYBOOK.md` (CC reads it) **and** seed project reference |
| Packaging + umbrella-asset convention (`-cp` flat / `-cc` wrapper, surface map, 29-math, bundle-on-umbrella) | Repo `CLAUDE.md` → `## Packaging conventions` **and** this playbook §1.1 / §1.3 |
| Executable release steps | `root_CC_PROMPT_vN_release.md` → copy, bump version, adjust deltas next cycle (the prior version's prompt is spent — see Artifact lifecycle) |
| Drift + corrected pattern + the verify-rendered observation | `root_build_context.md` (Self-Optimization Observations + release-pattern note) |
| Packaging-format methodology fixes | SBD §4.7 refinement (see §6) — flows through KF → staging → canonical sync |

---

## 6. Known debt / next-cycle inputs

Closed in v4.0 alignment cycle (July 2026):

- **SBD §4.7 refinement — CLOSED.** The K1/K2 residual (SBD §4.7 lines 335 / 337 / :343 asserting `package_skill.py` is a tracked repo file) was corrected during v4.0 W1 SBD recalibration via the seed-Project edit → staging → canonical-KF sync path. Corrections apply the exact replacement text from `audit/repo-catalog/REPO_CLAIM_RECONCILIATION.md` K1/K2: the wrapper shape is produced by `build_release_artifacts.py` directly (upstream origin: Anthropic's `package_skill.py` — not a tracked file). The `skill-builder`-internal `scripts/package_zip.py` remains a *separate* build-pipeline packager and stays disambiguated.
- **OPT_REF body recalibration — CLOSED.** Full body recalibration completed as part of v4.0 W1. The header and body are calibrated to Opus 5 + Sonnet 5 dual-primary; the ~45 4.7-era body refs are updated to the 5-generation landscape; the tendency taxonomy expanded per design §9 (14 tendencies + 2 non-tendency defects); the Context Budget Principles section rebuilt per D6 (automatic-RAG-by-window, with the ~66,500 figure preserved as a historical Phase 22 measurement).
- **README compatibility-matrix + per-Skill tier-marker regeneration — CLOSED at v4.0 Phase 2.** Regenerated against the v4.0 tier assignments (not the v3.1 ones) as part of the W2 mechanical sweep.
- **Tag-naming standardization — CLOSED.** Uniform `rootnode-<skill>/vN` verified at v3.1; the v3.0 asymmetry is historical and closed. No further action.

Remaining / carried forward:

- **`rootnode-for-code` plugin bundle** — roadmap, owned by the Distribution project, out of scope for the catalog release.
- **Tokenizer re-baselining** — Opus 5 and Sonnet 5 tokenizer specifics were not fully re-baselined against `count_tokens` in the v4.0 cycle. Carry as a Calibration Lab item for the next cycle; treat measurements with explicit tolerance until re-baselined.
- **Landscape-volatility discipline (D8 methodology)** — codified in AEA §4.15 for v4.0. Design docs authored under this discipline isolate model landscape facts in a dated block that decisions reference; validate the pattern's ergonomics through the next design cycle's use.
- **Structural anti-pattern candidates surfaced but not added (v4.0 AAP recommendation).** Two Opus-5-era behavioral patterns evaluated as candidates for promotion to structural entries in `root_AGENT_ANTI_PATTERNS.md`: *Verification-instruction accumulation* and *Subagent-verification harness pattern*. Both are documented as behavioral tendencies in `root_OPTIMIZATION_REFERENCE.md`; the recommendation is to promote at least the first if the sweep discipline recurs across CC deployments audited over the next cycle.
