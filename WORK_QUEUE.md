# Phase 31d Work Queue

Execute in order. One commit per item (exceptions noted). After each item, run the Verify step before committing. Halt on any R4 trigger from CLAUDE.md.

**KF reference convention.** Methodology citations point to `audit/canonical-kfs/<filename>` for in-repo access. The agent reads these via `@audit/canonical-kfs/<filename>` and cites them as `root_<NAME>.md §X.Y` in commit messages and reasoning.

**Scope convention.** All `grep` verifications enumerate Skill directories via the `rootnode-*/SKILL.md` glob (top-level, current Skills only). This excludes `_v2_1_staging/`, `design_queue/`, `audit/build-artifacts/`, and other non-Skill directories that may contain SKILL.md files.

---

## Stream B1 — Phase 31c Audit Remediation

### B1.1 — Folder rename (default: SKIP)

**Default action: SKIP.**

Per Phase 31d SH §4 Q-31d-3, the operator default is "Discard the audit clone (audit outputs preserved as artifacts; clone is tooling)." If the operator has not explicitly overridden this default before the CC session, do not perform the rename.

**Operator override path:** before invoking the CC session, the operator replaces this item's "Default action: SKIP" with `Rename audit/build-artifacts/rootnode-handoff-trigger/ → audit/build-artifacts/rootnode-handoff-trigger-check/` and the agent performs the rename via `git mv`.

**Verify (default-skip):** log "B1.1 SKIPPED per Q-31d-3 default" to the execution summary. No commit produced for this item.

**Verify (override):** `ls -d audit/build-artifacts/rootnode-handoff-trigger-check/` returns the directory; `ls audit/build-artifacts/rootnode-handoff-trigger/` returns "No such file." Commit message: `phase-31d B1.1: rename handoff-trigger audit folder to match Skill name`.

### B1.2 — block-selection C5 fix

File: `rootnode-block-selection/SKILL.md`

Find the two cross-Skill references near L13–L14 that mention "the relevant catalog skill" without an "if available" qualifier (per `audit/phase-31c/SKILLS_AUDIT_REPORT.md` C5 finding). Add "if available" to match the consistent pattern used by the file's other cross-Skill references.

**Verify:**

- `grep -n "rootnode-\|catalog skill\|catalog Skill" rootnode-block-selection/SKILL.md` shows every cross-Skill reference uses "if available" or "if installed" consistently.
- `git diff --stat HEAD` shows only `rootnode-block-selection/SKILL.md` modified.

Commit: `phase-31d B1.2: tighten "if available" qualifier on block-selection cross-Skill refs`.

### B1.3 — Brand-cleanliness pass (all 27 Skills)

Scan all 27 Skills' `metadata.original-source` frontmatter fields. For each field that references a project-specific design brief by filename or proper noun (examples from `audit/phase-31d/AMENDMENT.md` §5: `rootnode_context_budget_v5_enhancement_brief.md`, `Skill Design Spec: Brief Builder & Ecosystem Intelligence`):

Apply the §3.6 Fix in priority order (read `@audit/canonical-kfs/root_AGENT_ANTI_PATTERNS.md` §3.6 and `@audit/canonical-kfs/root_AGENT_ENVIRONMENT_ARCHITECTURE.md` §4.10):

1. **Replace** with a canonical KF reference if the methodology came from one (e.g., `root_SKILL_BUILD_DISCIPLINE.md`, `root_AUDIT_FRAMEWORK.md`, `root_MASTER_FRAMEWORK.md`, `root_OPTIMIZATION_REFERENCE.md`).
2. **Anonymize** to generic dated text: `"Seed-project methodology synthesis, YYYY-MM"` using the Skill's build month if known, or `"Production CC deployment 2026-05-04"` for CC-derived patterns.
3. **Remove** the field entirely if no agnostic replacement is appropriate.

Fields that already cite canonical KFs or use generic dated text: no change.

**Halt trigger #7 applies** if a replacement is ambiguous — surface the Skill name, current field value, and candidate options to operator. Do not choose silently. This is a Tier 3 decision; if critic-gate is wired, invoke it on the proposed wording before commit.

Document the per-Skill decision in the commit message body (one bullet per Skill changed).

**Verify:**

- Scope check: `ls -d rootnode-*/SKILL.md | wc -l` returns 27 (confirms scoping is correct before grep).
- Cleanliness check: `grep -E "original-source" rootnode-*/SKILL.md -A1 | grep -vE "(root_|Seed-project methodology|Production CC deployment|^--$|^[^:]+:$)"` returns no project-specific brief filenames or proper-noun references.
- Frontmatter-only diff: `git diff HEAD -- "rootnode-*/SKILL.md"` shows changes above the closing `---` of frontmatter only (no body content modified).

Commit: `phase-31d B1.3: brand-cleanliness pass on metadata.original-source fields`.

### B1.4 — Discipline-marker addition (7 post-discipline Skills)

Add `discipline_post: phase-30` to the `metadata:` block in these 7 Skills' SKILL.md frontmatter:

1. `rootnode-cc-design/SKILL.md`
2. `rootnode-repo-hygiene/SKILL.md`
3. `rootnode-critic-gate/SKILL.md`
4. `rootnode-mode-router/SKILL.md`
5. `rootnode-handoff-trigger-check/SKILL.md`
6. `rootnode-profile-builder/SKILL.md`
7. `rootnode-skill-builder/SKILL.md`

Place `discipline_post: phase-30` as the last field under `metadata:`, before the closing `---`. Reference: `@audit/canonical-kfs/root_SKILL_BUILD_DISCIPLINE.md` §4.6.

**Verify:**

- `grep -l "discipline_post" rootnode-*/SKILL.md | wc -l` returns exactly 7.
- `grep -l "discipline_post" rootnode-*/SKILL.md | sort` returns the 7 expected paths above (lexically sorted).
- For each of the 7 Skills, parse the frontmatter and confirm `metadata.discipline_post == "phase-30"`. Per-Skill check (run for each path):
  ```
  python3 -c "import yaml; doc=open('<path>').read().split('---')[1]; d=yaml.safe_load(doc); assert d['metadata']['discipline_post']=='phase-30', d['metadata']"
  ```
  No AssertionError on any of the 7 paths.

Commit: `phase-31d B1.4: add discipline_post:phase-30 to 7 post-discipline Skills`.

### B1.5 — skill-builder emit-logic update

Files: `rootnode-skill-builder/SKILL.md` body and/or `rootnode-skill-builder/references/*`

Update skill-builder so it emits `discipline_post: phase-30` in the `metadata` block of every Skill it builds going forward.

1. Locate the build template / frontmatter spec in skill-builder's body or reference files. Likely candidates: `references/build-template.md`, the SKILL.md body's "frontmatter spec" section, or a similar template artifact. List skill-builder's references first: `ls rootnode-skill-builder/references/`.
2. Add `discipline_post: phase-30` to the emitted frontmatter `metadata` block in the template/spec. If the spec is documented across multiple files, update all of them for consistency.
3. Reference: `@audit/canonical-kfs/root_SKILL_BUILD_DISCIPLINE.md` §4.6.

This step does not run a fresh build via skill-builder. Emit-logic update is verified by template inspection; full self-test is deferred to skill-builder's next live build.

**Verify:**

- `grep -rn "discipline_post" rootnode-skill-builder/` returns the new entry in the build template (in addition to the entry from B1.4 in skill-builder's own frontmatter; expect ≥ 2 hits in this directory).
- The template/spec block(s) showing emitted metadata structure include `discipline_post:` as a documented field.
- `wc -l rootnode-skill-builder/SKILL.md` returns ≤ 500.

Commit: `phase-31d B1.5: update skill-builder to emit discipline_post:phase-30 on new builds`.

---

## Stream B2 — CC Ecosystem Skills Impact Eval

### B2.1 — skill-builder D9 quality gate update

Files: `rootnode-skill-builder/references/*` and SKILL.md body

**(a) Add D9 (behavioral validation, RECOMMENDED) to the quality gate reference.**

1. Read skill-builder's reference files. Locate the file that lists the quality gate dimensions (likely `references/quality-gate.md` or equivalent).
2. Add D9 content using canonical text from `@audit/canonical-kfs/root_SKILL_BUILD_DISCIPLINE.md` §3.9 (D9 — Behavioral validation). Do NOT paraphrase pass conditions, skip condition, or RECOMMENDED-vs-REQUIRED classification — copy the canonical text and adapt only for surface-level integration (heading style, list formatting).
3. Cite `root_SKILL_BUILD_DISCIPLINE.md §3.9 D9` as the canonical source within the reference file.

**(b) Update SKILL.md body and references for dimension count.**

Replace any "8 dimensions" / "8-dimension" / "eight dimensions" reference with "9 dimensions" / "9-dimension" / "nine dimensions." Inspect with `grep -rni "8.dimension\|eight.dimension" rootnode-skill-builder/` — should return no results after the edit.

**(c) Description field check.**

Description is currently 976/1024 chars (per `audit/phase-31d/SKILLS_IMPACT_EVAL.md`). Per the impact eval brief, do NOT modify the description if a D9 mention would push past 1024. D9 is discoverable via reference material once the Skill loads.

If a description edit is unavoidable for coherence, count chars first:
```
python3 -c "import yaml; doc=open('rootnode-skill-builder/SKILL.md').read().split('---')[1]; d=yaml.safe_load(doc); print(len(d['description']))"
```
Halt (trigger #2) if total > 1024.

**(d) Self-pass verification.**

After (a)–(c), walk D1–D9 explicitly against the updated skill-builder. For each dimension, document: pass / fail / skip with one-sentence reasoning. If any dimension fails, halt (trigger #8).

This is a Tier 3 judgment item — invoke `rootnode-critic-gate` on the self-pass verdict. APPROVE → commit. REQUEST_CHANGES → revise reasoning or revert affected edit (cap 3 cycles). REJECT → halt.

Log the self-pass walkthrough (D1–D9 + reasoning) to `audit/phase-31d/B2_CONFIRMATIONS.md`.

**Verify:**

- `grep -rn "D9\|nine.dimension\|9.dimension" rootnode-skill-builder/references/` returns the new D9 entry.
- `grep -rni "8.dimension\|eight.dimension" rootnode-skill-builder/` returns no results.
- Description char count ≤ 1024 (or unchanged from 976).
- `wc -l rootnode-skill-builder/SKILL.md` returns ≤ 500.
- `audit/phase-31d/B2_CONFIRMATIONS.md` contains the D1–D9 self-pass walkthrough.

Commit: `phase-31d B2.1: add D9 behavioral validation to skill-builder quality gate`.

### B2.2 — repo-hygiene MCP detection check

File: `rootnode-repo-hygiene/references/sweep-categories.md`

1. Locate the MCP-related sweep category (or categories).
2. Compare the detection focus against `@audit/canonical-kfs/root_AGENT_ANTI_PATTERNS.md` §4.2 expanded entry (per-turn injection mechanism, pre-phase audit guidance).
3. **Decision logic:**
   - If the sweep references the catalog by section number (`§4.2`), no additional change is needed — the expansion is in-place upstream. Log to `audit/phase-31d/B2_CONFIRMATIONS.md` and skip to verification.
   - If the detection focus would benefit from a 1-sentence sharpening note about per-turn injection cost (e.g., "MCP tool schemas inject per-turn, not per-invocation; N servers × M tools compounds context cost on every turn"), append it to the relevant detection focus. Keep tight.

**(c) Test-repo verification.**

Run the sweep category against a test repo with 5+ MCP servers. If a test repo is not available, halt (trigger #9) and surface to operator for an alternate verification path (synthetic fixture, dry-run inspection, or deferral with documented rationale).

**Verify:**

- MCP sweep category text in `references/sweep-categories.md` is consistent with the expanded canonical entry. `git diff rootnode-repo-hygiene/references/sweep-categories.md` shows either no change (logged to confirmations) or a ≤ 1 sentence addition.
- Test-repo run produces at least one actionable finding, OR halt-trigger #9 fired and was resolved by operator instruction. Not both.

Commit (only if file changed): `phase-31d B2.2: sharpen MCP detection focus with per-turn injection note`. If no-change, no commit; logged to B2_CONFIRMATIONS.md instead.

### B2.3 — behavioral-tuning persuasion-compliance language calibration note

File: `rootnode-behavioral-tuning/references/countermeasure-templates.md`

Read `@audit/canonical-kfs/root_OPTIMIZATION_REFERENCE.md` first (the "Note on countermeasure language design" paragraph inside §"Behavioral Tendencies and Countermeasures") to ground the cross-reference in the actual upstream source.

Append a new section at the end of the file. Draft (adjust wording for natural integration with the file's existing tone, but preserve the three required elements):

```markdown
## Language Calibration

Countermeasure language design affects compliance. Research (Meincke et al. 2025, N=28,000) found persuasion techniques — authority, commitment, and scarcity framing — more than doubled LLM behavioral compliance rates (33% → 72%, p < .001). For discipline-enforcing countermeasures (tendencies #1 agreeableness, #5 fabricated precision, #7b tool under-triggering, #10 self-referential fabrication), use imperative framing: direct commands with authority and commitment anchors (e.g., "Run the verification command. Read the output. THEN claim the result."). For overcorrection-risk tendencies (#3 verbosity, #6 over-exploration), use calibrated framing that sets boundaries without triggering compensatory extremes. See `root_OPTIMIZATION_REFERENCE.md` §"Behavioral Tendencies and Countermeasures" — "Note on countermeasure language design" for full reasoning and citation.
```

Required elements:

1. Research grounding with citation (Meincke et al. 2025, N=28,000, the 33% → 72% finding).
2. Calibration principle with explicit tendency numbers (discipline-enforcing: #1, #5, #7b, #10; overcorrection-risk: #3, #6).
3. Cross-reference to the actual location of the persuasion-compliance content in `root_OPTIMIZATION_REFERENCE.md` — it is an inline note, not a named subsection, so cite it as the parenthetical paragraph inside §"Behavioral Tendencies and Countermeasures".

SKILL.md body: no change. Description: no change.

**Verify:**

- Appended section is 3–5 sentences (manual count).
- `git diff rootnode-behavioral-tuning/references/countermeasure-templates.md` shows only additions (`+` lines), no deletions of existing content.
- File parses as valid Markdown.

Commit: `phase-31d B2.3: add persuasion-compliance language calibration note to behavioral-tuning`.

### B2.4 — No-change confirmations

For each Skill listed below, read the SKILL.md and relevant reference files. Confirm no changes are needed per `audit/phase-31d/SKILLS_IMPACT_EVAL.md`. Log each confirmation to `audit/phase-31d/B2_CONFIRMATIONS.md` with: Skill name, frontmatter version field (read from the actual file), one-sentence reason no change is needed.

Skills to confirm:

1. `rootnode-critic-gate` — 4-check protocol unaffected by D9 / persuasion / MCP changes.
2. `rootnode-mode-router` — profile selection logic unaffected.
3. `rootnode-cc-design` — no mandatory changes from ecosystem analysis (RESEARCH-mode optional note is informational only).
4. `rootnode-handoff-trigger-check` — 7 conditions unaffected.

Read the actual frontmatter `metadata.version` field for each — do not assume versions from the impact eval brief.

If any Skill turns out to need a change after inspection, halt. Do not silently expand scope.

**Verify:**

- `audit/phase-31d/B2_CONFIRMATIONS.md` exists with explicit confirmation lines for the 4 Skills above plus B2.2 (if no-change branch was taken) plus the B2.1(d) self-pass walkthrough.
- `git diff main...HEAD --stat -- rootnode-critic-gate/ rootnode-mode-router/ rootnode-cc-design/ rootnode-handoff-trigger-check/` returns no changes.

Commit: `phase-31d B2.4: log no-change confirmations for 4 Skills`.

---

## Completion

After all items:

1. `git status --porcelain` returns empty (working tree clean on `phase-31d-remediation`).
2. `git log --oneline main..phase-31d-remediation` — verify commit sequence matches work queue order. Expected count: 6–8 commits depending on B1.1 default (skipped, –1) and B2.2 branch (no-change, –1).
3. Produce execution summary:
   - Items completed (with commit hash per item)
   - Items SKIPPED (with reason — e.g., B1.1 per Q-31d-3 default)
   - Files modified (per stream)
   - Halts encountered (if any), with resolution per halt
   - Critic-gate invocations (count, items, outcomes)
   - Validation outcomes per item (pass/fail per Verify step)
4. Recommend operator next step: review feature branch (`git diff main...HEAD`); optional post-cycle hygiene sweep via `rootnode-repo-hygiene` against the feature branch; open PR or merge per repo conventions.
5. **Do NOT push or merge.** Operator action.
