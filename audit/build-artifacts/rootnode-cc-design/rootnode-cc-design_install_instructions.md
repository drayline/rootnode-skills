# rootnode-cc-design v2.0 — Install Instructions

**Build CV:** Phase 30 D-build (May 5, 2026)
**Predecessor:** `rootnode-cchq-design` v1.1.1
**Successor:** None (v2.0 is the latest)
**Distribution status:** v2.3 standalone release (deferred from v2.2 paired ship; ship after skill-builder v2 + repo-hygiene v1 paired distribution completes)

---

## Why a clean install is required

The frontmatter `name:` field changes from `rootnode-cchq-design` to `rootnode-cc-design`. Both folders cannot coexist in `~/.claude/skills/` — Claude's auto-activation engine treats them as separate Skills, and overlapping descriptions (which inevitably happens between v1.1.1 and v2.0) cause unpredictable triggering.

**The rule:** remove `rootnode-cchq-design/` BEFORE installing `rootnode-cc-design/`.

This is not optional. v1.1.1 and v2.0 are incompatible duplicates by design — the rename is intentional, not a migration.

---

## Path A: Personal install (local machine, single-user)

For installing into a single user's `~/.claude/skills/` directory:

```bash
# 1. Verify v1.1.1 is currently installed (if not, skip step 2)
ls ~/.claude/skills/rootnode-cchq-design/SKILL.md

# 2. Remove the old folder (the rename makes v1 + v2 coexistence break)
rm -rf ~/.claude/skills/rootnode-cchq-design/

# 3. Extract the v2.0 deployable
cd ~/.claude/skills/
unzip /path/to/rootnode-cc-design.zip
# This creates ~/.claude/skills/rootnode-cc-design/ with the proper folder structure

# 4. Verify the install
ls ~/.claude/skills/rootnode-cc-design/SKILL.md
ls ~/.claude/skills/rootnode-cc-design/references/   # should show 9 .md files
ls ~/.claude/skills/rootnode-cc-design/schema/        # should show 2 .json files

# 5. Verify auto-activation
# Start a Claude session and use a trigger phrase like:
#   "design CC for a new Python CLI project"
# or "remediate the hygiene findings in this repo"
# Claude should announce mode confirmation, e.g. "DESIGN MODE — building a new Claude Code deployment plan."
```

---

## Path B: GitHub release (drayline/rootnode-skills repo distribution)

For publishing as part of the v2.3 standalone release (downstream of the v2.2 paired ship):

```bash
# Pre-conditions: you are at the rootnode-skills repo root, on a clean working tree, with gh CLI authenticated.

# 1. Stage the new skill folder (replacing the old one in the repo)
git rm -rf rootnode-cchq-design/
mkdir -p rootnode-cc-design/
unzip -o /path/to/rootnode-cc-design.zip -d ./
# This places rootnode-cc-design/ at repo root with proper structure

# 2. Verify no orphaned references in repo-level docs (README, CONTRIBUTING, marketplace.json)
grep -rn "rootnode-cchq-design" .
# All hits should be in legacy artifacts that are intentionally renamed; correct each:
#   - README.md skill catalog
#   - .claude-plugin/marketplace.json (if marketplace plugin manifest exists)
#   - CONTRIBUTING.md examples
#   - any release notes referencing the old name

# 3. Update README.md skill catalog (replace rootnode-cchq-design row with rootnode-cc-design)

# 4. Commit + tag + release
git add -A
git commit -m "v2.3: rootnode-cc-design v2.0 (renamed from rootnode-cchq-design v1.1.1)

REMEDIATE evolution:
- Three approval forms (blanket / fragmented / conditional)
- Step-level risk tags (high/medium/low)
- Critic-gate composition (required/optional) aligned with repo-hygiene v1

Documentation:
- cc-anti-patterns substantively rebuilt to canonical §X.Y numbering
- cc-methodology-patterns restructured with canonical-cite preamble
- All hyge contamination anonymized to 'production CC deployment 2026-05-04'

Cross-Skill contracts (verified against repo-hygiene v1 built artifact):
- HYGIENE_REPORT.md format owned by rootnode-repo-hygiene
- Cat 1–10 → repo-hygiene Phase 2 cleanup
- Cat 11–14 + 7-layer leaks → cc-design REMEDIATE
- F-{cat}.{n} finding-ID format
- critic_gate_threshold field name + semantics

Audit artifacts:
- placement_note.md (Gate 3 ecosystem placement)
- promotion_provenance.md (Gate 2 warrant inheritance from v1.1.1)
- ap_warnings.md (Gate 5 D7 — Kitchen Sink ACCEPTED with reasoning)"

git tag v2.3
gh release create v2.3 \
  rootnode-cc-design.zip \
  --title "v2.3: rootnode-cc-design v2.0" \
  --notes-from-tag

# 5. Push tag + commits
MSYS_NO_PATHCONV=1 git push origin main --tags
# (MSYS_NO_PATHCONV=1 needed on Windows for refs with colons)
```

---

## Verification post-install

After installing, verify three properties:

**1. Auto-activation fires on intended phrases.** Try these in a fresh chat:

```
"Design CC for a Python CLI tool"           → DESIGN mode confirmation
"We hit X friction in CC last session"      → EVOLVE mode confirmation
"Remediate the hygiene findings"            → REMEDIATE mode (Phase 1)
"Should we adopt subagents for CC"          → RESEARCH mode confirmation
"Give me a CLAUDE.md skeleton"              → TEMPLATE mode confirmation
```

Each should produce a clear mode confirmation in the response opener.

**2. Auto-activation does NOT fire on routed-away phrases.**

```
"Audit my CC repo for hygiene issues"        → should route to rootnode-repo-hygiene
"Score this prompt"                          → should route to rootnode-prompt-validation
"Audit my Claude Project"                    → should route to rootnode-project-audit
```

If `rootnode-cc-design` activates on these, the description's negative triggers may be misordered against another installed Skill — surface to Aaron for routing diagnosis.

**3. REMEDIATE three approval forms parse correctly.** After Phase 1 produces an EXECUTION_PLAN.md, test:

```
"execute"                                  → blanket approve, all steps run
"execute steps 1, 2, 4"                    → fragmented, only those step IDs run
"execute medium-and-low risk; halt high"   → conditional, predicate-filtered
"looks good"                               → REJECTED (anti-condition; ambiguous)
```

The first three should enter Phase 2 with the appropriate filter. The fourth should NOT enter Phase 2; the Skill should surface "I need an explicit approval form: blanket / fragmented / conditional."

---

## Rollback plan

If v2.0 surfaces blocking issues post-install, revert to v1.1.1:

```bash
# 1. Remove v2.0
rm -rf ~/.claude/skills/rootnode-cc-design/

# 2. Re-install v1.1.1 from the source zip (still in /mnt/user-data/uploads/ during the build CV; archived in Drive Projects/ROOT/research/)
cd ~/.claude/skills/
unzip /path/to/rootnode-cchq-design-v1_1_1.zip
```

v1.1.1 remains a working Skill; rollback is non-destructive. Aaron should surface any v2.0 issues as v2.x evolution candidates rather than as v2.0 patches (no v2.0.1 ship pattern unless a hard-blocking defect surfaces).

---

## What to file in Drive

Upon successful install + verification:

- `rootnode-cc-design.zip` → `Projects/ROOT/research/` (durable record of the v2.0 deployable)
- `rootnode-cc-design_placement_note.md` → `Projects/ROOT/research/`
- `rootnode-cc-design_promotion_provenance.md` → `Projects/ROOT/research/`
- `rootnode-cc-design_ap_warnings.md` → `Projects/ROOT/research/`
- This install instructions file → `Projects/ROOT/research/` (named `rootnode-cc-design_install_instructions.md`)
- Updated `root_build_context.md` → replace seed Project KF (Phase 30 D-design + D-build entries added)

---

*This install instructions document is the closeout artifact for the Phase 30 D-build CV. Per Q-B6 disposition, it documents the folder-removal-before-install discipline that the frontmatter `name:` change requires.*
