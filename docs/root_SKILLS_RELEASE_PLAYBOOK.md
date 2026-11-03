# rootnode-skills Release Playbook & Lessons Learned

Canonical runbook for cutting a `drayline/rootnode-skills` catalog release. Read this **before** any release conversation — chat-side planning or CC execution. It exists because the v3.1 release (2026-06-25/26) churned hard on things that were already settled but not written down. Since catalog v6.0 (2026-11-02) the release unit is the **plugin**: the 27 Skills ship in six plugins from one marketplace, and the per-Skill zip model of v3.0–v5.0.1 is retired. Every decision, convention, and anti-churn rule is here so the next catalog update is fast and low-friction.

**Companion artifacts.** The executable release prompt (`root_CC_release_vN.md`, or the older `root_CC_PROMPT_vN_release.md` form) is the step-by-step CC prompt for a specific version; this playbook is the *why* and the *standing rules* behind it. Packaging conventions also live in the repo `CLAUDE.md` (`## Packaging conventions`) and, as build discipline, in `root_SKILL_BUILD_DISCIPLINE.md` §4.7 and §6.6.

**Artifact lifecycle — read this first.** A version-stamped release prompt is **spent once its version ships**. Do not re-edit a spent release prompt to capture a new lesson — it is a record of one execution, not a living document. The durable home for release knowledge is *this playbook* (version-agnostic) plus the repo `CLAUDE.md` packaging section and the committed packager. Each new release **derives its prompt from this playbook** (copy → bump version → adjust deltas), never from the prior spent prompt.

---

## 1. Release architecture — the model (never re-derive this)

### 1.1 What a catalog release produces

A catalog release has three outputs, and only the first one reaches installed users.

- **Marketplace publish.** Merging a raised `version` in `plugins/<plugin>/.claude-plugin/plugin.json` to `main` publishes that plugin version. claude.ai accounts with **Sync automatically** on pick it up on the next sync; Claude Code users pick it up with `claude plugin update`. Merge is publish — so the content PR must be release-complete before the operator merges it (§3).
- **Per-plugin releases.** One GitHub release per plugin that changed, tag `<plugin>/v<version>`, where `<plugin>` is the full plugin name (it carries the `rootnode-` prefix) and `<version>` is read from that plugin's `plugin.json` (e.g. `rootnode-projects/v6.0.0`), `--latest=false`. Each carries exactly one asset, `<plugin>-v<version>.zip`, and its notes from `release-notes/<plugin>-v<version>.md`. These are the record and the manual-download path, not the install path.
- **Catalog umbrella.** One release tagged `catalog-vN.N` (or `catalog-vN.N.N` for a patch), marked `--latest`, notes from `release-notes/catalog-vN.N[.N].md`, carrying **the six plugin zips as loose assets** — each plugin at its current version. Its body is the catalog index: what changed, install (marketplace first), a `## Download` section, a plugin index that links every plugin's current release and lists the Skills inside it, plus Architecture and Site sections. It frames the plugins as one system and is what GitHub surfaces as "Latest."

**Model history.** v2.x: one release, all Skill zips loose. v3.0: per-Skill releases plus a notes-only umbrella. v3.1: the umbrella gained one bundle asset (`rootnode-catalog-vN.zip`, a zip of the 29 surface zips) after the notes-only umbrella left users at GitHub's auto Source-code archives. v6.0: per-plugin releases plus an umbrella with six loose plugin zips; the bundle and the `-cp`/`-cc` surface zips retired (design D4/D5). Do not revert to an earlier form.

**Umbrella asset rule (revised at v6.0).** Six assets is a short list, and every asset installs as-is through claude.ai **Upload plugin**; the v3.1 bundle was a zip of zips that had to be unpacked first. So the umbrella attaches the six plugin zips directly and no bundle. GitHub's auto Source-code archives still appear and still cannot be removed; the `## Download` section steers users past them.

### 1.2 Install paths and account sync

The marketplace is named `rootnode` (`.claude-plugin/marketplace.json`). Each entry's `source` is a `./plugins/<plugin>` path, because claude.ai sync rejects bare names under `metadata.pluginRoot` (SBD §4.7). Three install paths, in the order the README presents them:

- **claude.ai (recommended).** **Customize > Plugins > Add > Add marketplace** → `drayline/rootnode-skills`, turn on **Sync automatically**, then add the plugins wanted. One account install reaches chat, Cowork and Claude Code; Claude Code signed in with that account loads each plugin as `<plugin>@synced`. Chat ignores plugin hooks and agents.
- **Claude Code without an account sync** (API-key sessions). `claude plugin marketplace add drayline/rootnode-skills`, then `claude plugin install <plugin>@rootnode`. Auto-update is off by default for a third-party marketplace, so updates take `claude plugin update`. `[dated product fact — verify on the running Claude Code version]`
- **Manual.** Download `<plugin>-v<version>.zip` from a release and use claude.ai **Upload plugin**. No update channel.

**Double-load hazard.** Installing the same plugin on the account and locally loads two copies. So does keeping a pre-v6.0 standalone upload (`rootnode-<skill>`) beside the plugin copy (`<plugin>:<skill>`). Install on the account *or* locally, and turn off the pre-v6.0 standalone Skills once the plugins are in. The README Quick Start carries the same rule.

### 1.3 Packaging toolchain

Repo-root script roster is **two** from the v6.0 release PR on:

- **`build_release_artifacts.py` — THE release packager.** Writes one zip per plugin, `dist/<plugin>-v<version>.zip`, with `<version>` read from that plugin's `plugin.json` and `.claude-plugin/plugin.json` at the zip root (the shape **Upload plugin** takes). Leaves `evals/` out at the plugin root and each Skill root; stores shell scripts LF with mode 0755; asserts six zips on a full build (non-zero exit on mismatch). On a full build it clears stale `dist/*.zip` first, and it fails the build when a Skill reference's embedded copy of a shipped script drifts from the shipped file. Both behaviors land in the v6.0 release PR.
- **`generate_release_notes.py` — the release-notes generator.** Driven by a per-cycle config under `audit/v<N>_<M>-release/`. From v6.0 it writes per-plugin notes (`release-notes/<plugin>-v<version>.md`) for the plugins the config lists; the umbrella notes are authored by hand.
- `build_releases.py` (flat per-Skill zips, legacy since v3.1) is removed in the v6.0 release PR.

**Not the release packager.** Anthropic's single-Skill `package_skill.py` lives upstream at `anthropics/skills` → `skills/skill-creator/scripts/package_skill.py` (writes `<name>.skill` with a `<name>/` wrapper); skill-builder's own `scripts/package_zip.py` is adapted from it. Neither is used to cut a release (SBD §4.7).

**Validation instruments.** `claude plugin validate .` (marketplace) and `claude plugin validate ./plugins/<plugin> --strict` (each plugin) must pass before a release. `[dated product fact — verify on the running Claude Code version]` They check Claude Code's rules only; claude.ai sync applies its own, so the operator's first **Add marketplace** after a manifest change is a separate check (SBD §4.7).

Historical cycle tooling (`audit/v3_1-release/`, the per-cycle notes configs under `audit/v4_0-alignment/` and later) stays at its original path as cycle history.

**Authoritative packager inventory: `audit/repo-catalog/`** (regenerated at the end of every release — see Post-verification). Where §1.3 and the catalog disagree, the catalog wins and this section is a defect to fix.

### 1.4 Tag naming

- **Per-plugin:** `<plugin>/v<plugin.json version>`, with the full plugin name — always three-part semver, e.g. `rootnode-code/v6.0.0`.
- **Catalog umbrella:** `catalog-vN.N` for a catalog version, `catalog-vN.N.N` for a patch catalog release. The catalog version is the umbrella's label; plugin versions move independently after v6.0.0.
- **Historical per-Skill tags** `rootnode-<skill>/vN` (v3.1–v5.0.1) and the two v3.0 prefix-less tags stay as history. No new per-Skill tags after v5.0.1. The `rootnode-skill-builder/` prefix now carries the Skill's history (v3.1–v5.0) and the plugin's line (v6.0.0 on); check any pattern-generated tag against `git tag --list` before creating it (§4 rule 5).

### 1.5 Alternate release shape — the single-plugin cut

Use a **single-plugin cut** when exactly one plugin changes and the catalog does not.

- **What it produces.** The raised `plugin.json` version merged to `main` (the publish), one per-plugin release `<plugin>/v<version>` with its zip and notes, and a CHANGELOG entry.
- **What it does NOT produce.** No new umbrella, no new catalog-index notes, no regenerated repo catalog. The prior umbrella keeps `--latest`; its asset for that plugin is one version behind until the next catalog release, and the per-plugin release is the manual download for the new version.
- **Conditions.** All must hold: (1) only one plugin changed; (2) no file another plugin relies on changed; (3) no README or umbrella link depends on the change.
- **Promote to a catalog release** as soon as any condition fails, so the umbrella and the plugins move in lockstep.
- **Anti-churn.** A per-plugin release never marks itself `--latest`; the README's `/releases/latest` link depends on the umbrella keeping it.

### 1.6 Patch catalog release

A patch that changes more than one plugin, or a file another plugin relies on, ships as a **patch catalog release**. Shape settled at v5.0.1 (2026-10-29), restated for plugins at v6.0:

- **Version bumps** only in the plugins that changed (patch component). Changed Skills take their plugin's new version in `metadata.version`; unchanged Skills keep theirs (SBD §6.6).
- **Per-plugin releases** only for the changed plugins: tag `<plugin>/vN.N.N`, `--latest=false`. Unchanged plugins are not re-tagged.
- **Umbrella** `catalog-vN.N.N`, marked `--latest`, carrying all six plugin zips built from merged `main` — changed plugins at their new version, unchanged plugins at their current one — so the umbrella stays the one full-catalog download.
- **Umbrella notes** link every plugin's current release: the new tag for a changed plugin, the existing tag for an unchanged one.
- **Content PR carries the release docs:** the per-plugin notes for the changed plugins, the umbrella notes `release-notes/catalog-vN.N.N.md`, and the CHANGELOG entry ride the content PR (§2 Phase A step 4), exactly as for a full release. Write them before the Refuter review, so the reviewed diff includes them.
- **Repo catalog** regenerates after verification, as for a full release.

A patch that changes exactly one plugin with no cross-plugin effect stays a single-plugin cut (§1.5).

---

## 2. Release process — two-phase, branch-protection-aware

`main` is branch-protected (CLAUDE.md halt #1): **no direct commits.** All repo commits land via a `release/vN.N` branch → PR → operator merge (Phase A). Tags and GitHub releases are created off merged `main` afterward (Phase B), so every tag points at the complete state. Because merge is also the marketplace publish, the Phase A merge gate is the publish gate.

### Pre-flight
1. `git checkout main && git pull`; confirm the content work has merged (spot-check `plugin.json` versions and Skill `metadata.version` fields).
2. `gh auth status` authenticated.
3. `claude plugin validate .` and `claude plugin validate ./plugins/<each> --strict` pass.
4. Confirm the staging manifest: `design/staging-kf/` contains exactly the KFs to sync, nothing else (stale drafts pollute the mirror).
5. Confirm the umbrella notes use embedded `[name](url)` links (not bare URLs, not double-wrapped) — see §3 and §4 rule 7.

### Phase A — content PR (all commits; operator merges)
1. Branch `release/vN.N`.
2. **Canonical-KF sync** — named files only, never a glob. Copy each staged KF → `audit/canonical-kfs/` by name; CRLF-normalized `diff` each against its expected delta; **clear staging** after a verified sync.
3. **Version bumps** — raise `version` in each changed plugin's `plugin.json`; set changed Skills' `metadata.version` per SBD §6.6.
4. **Release docs** — per-plugin notes (`release-notes/<plugin>-v<version>.md`) for each changed plugin, the umbrella notes (`release-notes/catalog-vN.N.md`), and the CHANGELOG entry. Written before the Refuter review, so the reviewed diff includes them.
5. **README** — marketplace install path first (§1.2), the plugin table, and download links at **`/releases/latest`** (resolves to the umbrella while it is `--latest`).
6. Push, open PR, **HALT for operator review + merge.** The merge publishes.

### Phase B — tags + releases off merged `main`
7. Re-sync to merged `main`; verify the tip is the PR merge commit and report its SHA verbatim. Package from that commit, never from the release branch.
8. **Package:** `py -3 build_release_artifacts.py` (the operator's machine resolves `python` to an unrelated interpreter) → six zips, self-asserted. Record each zip's sha256.
9. **Per-plugin releases:** for each changed plugin, `gh release create <plugin>/v<version> dist/<plugin>-v<version>.zip --target <merge SHA> --title "<plugin> v<version>" --notes-file release-notes/<plugin>-v<version>.md --latest=false`. Name each asset path explicitly, never `dist/*.zip`. Sequential; halt on any failure.
10. **Catalog umbrella:** `gh release create catalog-vN.N --target <merge SHA> --title "root.node catalog vN.N" --notes-file release-notes/catalog-vN.N.md --latest` followed by the six explicit zip paths. Apply notes **via `--notes-file` (raw bytes)**, never by pasting a rendered copy (§3 / §4 rule 7). The umbrella stays the only `--latest` release.

### Verification (all must hold)
- Content PR merged; canonical-kfs synced to expected deltas; staging cleared; notes, CHANGELOG and README on `main`.
- **Marketplace on `main`:** `gh api repos/drayline/rootnode-skills/contents/.claude-plugin/marketplace.json` decodes and lists the six plugins; each plugin's `plugin.json` on `main` reads the expected version.
- Six zips built, each with `.claude-plugin/plugin.json` at the zip root and a name that matches its `plugin.json` version.
- One per-plugin release per changed plugin, one asset each, asset sha256 equal to the build's.
- `catalog-vN.N` umbrella created, `--latest`, six assets whose sha256 equal the build's.
- **Umbrella notes verified BOTH ways:**
  - **Stored body** — `gh release view catalog-vN.N --json body`: `]](` == 0 (no double-wrapped links); `releases/tag/rootnode-` == the number of plugin links the notes carry (six); `## Download` present.
  - **Rendered body** — `gh api -H "Accept: application/vnd.github.html+json" repos/drayline/rootnode-skills/releases/tags/catalog-vN.N --jq .body_html`: the plugin links render as `<a href=…>` anchors and no literal `[name](` text survives. An `href` in the stored body is NOT proof of a clean render (§4 rule 7).
- README install/download links resolve, and the umbrella is the only `--latest` release.
- Show `gh release list` as evidence. Banned completion phrases: "should work," "probably fine," "looks good."
- **Live install (operator).** Adding the marketplace on claude.ai and on Claude Code is an operator check after Phase B; a CC session cannot perform it and does not report it as done.

### Post-verification — repo catalog regeneration

11. **Regenerate `audit/repo-catalog/`.** After every Verification bullet above passes, produce a fresh `audit/repo-catalog/root_repo_catalog_<YYYYMMDD>.md` matching the section structure of the prior snapshot. Every section derives from a live command (`git ls-files`, `git tag --list`, `gh release list`, `ls`, `git log --oneline -20`), never from memory or the prior catalog. Regenerating **after** verification captures the new tags, the umbrella release, and the current `--latest` — running the catalog pre-package would bake in staleness in the Tags and GitHub Releases sections. Commit on `main` via a follow-up hygiene PR (branch protection forbids direct commits); commit message convention `chore(catalog): regenerate for vN.N`. The instruction to regenerate enumerates the expected deltas rather than naming files by assumption. The catalog is what future sessions read as the ground truth for repo contents; failure to regenerate is what produced the v4.0 pre-flight defect (a month-stale catalog was unreachable and an incorrect playbook became authoritative in its place — see the reconciliation cycle 2026-07-25).

---

## 3. Decisions & conventions (with rationale)

- **The plugin is the release unit (v6.0, design D4/D5).** A plugin installs once per account across chat, Cowork and Claude Code and has an update channel; a Skill zip had neither, and no telemetry. Per-plugin releases replace per-Skill releases; the surface zips and the bundle retired with them.
- **Merge is publish.** The marketplace reads `main`, so a raised `plugin.json` version reaches synced users on merge, before any tag exists. Tags and releases record a publish; they do not cause one. A content PR therefore carries everything the release needs — versions, notes, CHANGELOG, README — before the merge gate.
- **Six loose zips on the umbrella; no bundle.** Each asset installs directly through **Upload plugin**, and six is a short list. The v3.1 bundle solved a 29-asset problem that no longer exists.
- **README → marketplace first, `/releases/latest` second.** The marketplace is the path with updates; the release link is the manual fallback and auto-tracks each catalog ship. **Dependency:** `/releases/latest` resolves to the umbrella **only while the umbrella stays `--latest`** — so no per-plugin release may be marked `--latest`.
- **Explicit asset paths, never a glob.** `dist/` is build output that keeps old zips between runs; a release step using `dist/*.zip` would ship retired artifacts. Name every asset path, and let the packager clear stale zips on a full build.
- **Umbrella notes are applied as raw bytes via `--notes-file`, never pasted from a rendered copy.** The v3.1 double-wrapped-link bug (`[[name](url)](url)`, which renders as literal text) came from pasting a rendered-page copy back into the notes — *not* from the link format. Embedded `[name](url)` renders fine. Apply notes from the source markdown file; if a fix is needed post-create, `gh release edit catalog-vN.N --notes-file <file>`.
- **Two-phase branch model.** Branch protection forbids direct `main` commits, so content goes through a PR; tags/releases are created off merged `main` so they reference the final state.
- **Named-file canonical sync, never a glob.** A blind `cp staging/*.md canonical/` propagates any stale leftover into the mirror. Copy by name, diff each, clear staging after.
- **Catalog umbrella body is the full index, not a summary.** The umbrella's value is the plugin index — each plugin linked to its current release with the Skills inside it listed — plus install, `## Download`, Architecture and Site. A thin summary defeats the purpose.

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
| Packaging convention (plugin layout, one zip per plugin, six-zip assertion, explicit asset paths) | Repo `CLAUDE.md` → `## Packaging conventions`, this playbook §1.1 / §1.3, and SBD §4.7 |
| Plugin and Skill versioning, the v6.0 rename | SBD §6.6; this playbook §1.4–§1.6 |
| Install paths and the double-load rule | Repo `README.md` Quick Start and this playbook §1.2 |
| Executable release steps | `root_CC_release_vN.md` → copy, bump version, adjust deltas next cycle (the prior version's prompt is spent — see Artifact lifecycle) |
| Drift + corrected pattern + the verify-rendered observation | `root_build_context.md` (Self-Optimization Observations + release-pattern note) |
| Packaging-format methodology fixes | SBD §4.7 refinement — flows through KF → staging → canonical sync |

---

## 6. Known debt / next-cycle inputs

Closed at v6.0 (2026-11-02):

- **Distribution model — CLOSED.** The plugin marketplace replaced per-Skill zips (design `design/root_DESIGN_plugin_packaging.md`, D1–D6). The roadmap item "`rootnode-for-code` plugin bundle" is superseded by the `rootnode-code` plugin.
- **`package_skill.py` location — CLOSED.** Verified upstream at `anthropics/skills` `skills/skill-creator/scripts/package_skill.py` (commit `ca45fc496a3436251f191354091d557da31c15b5`); SBD §4.7 records it. It is not the release packager.
- **Landscape-volatility discipline — CLOSED.** AEA §4.15, validated through use in the v5.0 cycle.

Remaining / carried forward:

- **Lift evals.** Only `rootnode-projects` ships an eval suite (5 cases). Its first run scored WITH 1.00 / W/OUT 1.00 on every case, so Δ = 0 says nothing yet: the graders cannot fail the baseline (SBD §3.9a). Rewrite the graders against properties the baseline misses, then extend suites to the other plugins. The should-trigger fire rate was 6 of 9, with global-audit at 1 of 3 — a description problem for the SBD §9 loop.
- **Marketplace install not yet observed.** The v6.0 build tested **Upload plugin** for `rootnode-projects` only; marketplace add on claude.ai and on Claude Code is first checked after the v6.0 release.
- **Hook coverage.** `rootnode-code` hooks were run live on Windows only; macOS behavior, the working directory after `cd`, and real no-`jq` sessions are unverified.
- **Directory submission.** Later; submit `rootnode-projects` first, after its evals show lift.
- **Website sync.** rootnode.design still asserts v3.0; its install instructions move to the marketplace path.
- **Tokenizer re-baselining** — a Calibration Lab item; treat measurements with explicit tolerance until re-baselined.
- **Structural anti-pattern candidates.** Seven candidates remain unpromoted in `root_AGENT_ANTI_PATTERNS.md` §6 (3+ independent deployments threshold unmet).
