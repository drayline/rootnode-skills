# 5-Generation Alignment — Verification Log (Phase 0)

**Session:** 5-gen alignment execution (design v1.3, prompt v1.2)
**Executed:** 2026-07-24
**Design doc:** `design/root_skill_5gen_alignment_design.md` (v1.3, dated 2026-07-21, decisions LOCKED 7/21)
**Playbook:** `docs/root_SKILLS_RELEASE_PLAYBOOK.md`
**Elapsed since D1–D3 lock:** 3 days

**HEADLINE:** Multiple V-items contradict a locked-decision rationale. Return-to-chat trigger fired. Do NOT proceed to Phase 1 without a chat-side reconciliation of D1.

---

## V1 — Fable 5 subscription / accessibility state

**Verdict:** Fable 5 is GA on API, Bedrock, Claude Platform on AWS, Google Cloud, Microsoft Foundry per the models overview page. The overview positions Fable 5 as "Anthropic's most capable widely released model" and recommends starting with **Claude Opus 5** for general workloads.

**Design §1 framing:** Fable 5 is "accessible on subscriptions without a temporary-access flag as of 7/21." The overview page as of 2026-07-24 does not mention a subscription-tier gate or temporary-access flag, but also does not enumerate claude.ai plan behavior explicitly. Practical reach limited by token economics still holds ($10/$50 pricing).

**Sources:**
- https://platform.claude.com/docs/en/about-claude/models/overview (fetched 2026-07-24)

---

## V2 — Sonnet 5 system card / behavioral deltas

**Verdict (partial — direct system-card fetch not performed this pass; whats-new page substituted for the API-visible behavior deltas):**

Confirmed from `whats-new-sonnet-5`:
- Model ID `claude-sonnet-5`. ✓ matches design §1.
- 1M context (**default AND max — no smaller variant**). ✓ matches design.
- 128k max output. ✓
- Three breaking API changes: adaptive thinking on by default; manual extended thinking (`budget_tokens`) → 400; non-default `temperature`/`top_p`/`top_k` → 400. ✓ matches design.
- **Tokenizer:** "approximately 30% more tokens than on Claude Sonnet 4.6" — design says "~1.0–1.35x". Design upper bound is close; the authoritative number is **~30% (=1.30x)**.
- Pricing: intro $2/$10 through 2026-08-31, standard $3/$15 after. ✓
- Priority Tier: not available on Sonnet 5. ✓
- Cybersecurity safeguards: "first Sonnet-tier model with real-time cybersecurity safeguards" — refusals return HTTP 200 with `stop_reason: "refusal"`. ✓ matches design's "Cyber safeguards from Opus 4.7/4.8 enabled by default."
- Reliable knowledge cutoff: Jan 2026. ✓
- ZDR: **Sonnet 5 supports ZDR for organizations with ZDR agreements** — this is different from Fable 5 (Fable 5 is "Covered Model", no ZDR per design). Recorded for OPT_NOTES / cc-design.

**Behavior deltas vs 4.6 (misuse cooperation, deception):** the whats-new page states "Claude Sonnet 5 is a capability upgrade over Claude Sonnet 4.6 at the same price" and points to https://www.anthropic.com/transparency for benchmarks. The design's specific "lower rate of undesirable behaviors than 4.6 per Anthropic" claim is NOT verbatim on the whats-new page. Marked **pending direct system-card read** for the behavioral-tuning deployment-conditioning table update.

**Effort levels:** the whats-new page does NOT enumerate "low/medium/high/max/xhigh" — it points to `/docs/en/build-with-claude/effort` for guidance. Design's effort-level list is unverified. Marked pending direct effort-page fetch.

**Sources:**
- https://platform.claude.com/docs/en/about-claude/models/whats-new-sonnet-5 (fetched 2026-07-24)

---

## V3 — Claude.ai Projects RAG threshold under 1M-window models

**Verdict:** UNRESOLVED as stated in the design fallback, BUT the finding is stronger than expected — the design's "revalidation pending" framing understates the drift.

**Evidence:**
- Web search surfaced an Anthropic support article: `support.anthropic.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects` — Projects now feature "automatic RAG activation when the uploaded knowledge base exceeds what can fit within the model's context window." Article not fetched in-depth this pass, but the summary alone indicates the platform-level RAG threshold model has shifted from "fixed ~66,500 tokens (33% of 200K)" to "automatic based on the underlying model's context window."
- Latest models comparison (overview page): Opus 5, Sonnet 5, Fable 5 = 1M context; Sonnet 4.6, Opus 4.6, Opus 4.7, Opus 4.8 = 1M context (legacy table); Sonnet 4.5 = 200K (legacy); Haiku 4.5 = 200K.
- **Only Haiku 4.5 (and older Sonnet 4.5 / Opus 4.5) still use a 200K window.** Every current top-tier and mid-tier chat model is on 1M.

**Implication:** the KFs' entire ~66,500 threshold discussion is calibrated against a platform state that no longer exists across most model surfaces. Tier bands, per-file evaluation math, and the "measured under 200K-era platform" caveat are all stale.

**Recommendation:** the context-budget rewrite scope exceeds the design's "1M-window landscape note" bullet. This is a KF section rebuild, not an update. Return-to-chat item.

**Sources:**
- https://platform.claude.com/docs/en/about-claude/models/overview (fetched 2026-07-24)
- https://support.anthropic.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects (search snippet only, not fetched in full)

---

## V4 — Claude Code default model + effort defaults post-Sonnet-5; Fable in CC

**Verdict:** UNRESOLVED this pass — no CC-defaults page was fetched. Overview page notes: "On Claude Opus 4.8, the `effort` parameter defaults to `high` on all surfaces, including the Claude API, Claude Code, and claude.ai. On Claude Opus 5 and Claude Sonnet 5, it defaults to `high` on the Claude API and Claude Code." Nothing on the current CC default *model*.

**Effect on scope:** cc-design and CC_EG edits need this fact before proceeding. Fetch cc-defaults page next session.

---

## V5 — Sonnet 4.6 official deprecation timeline

**Verdict:** Unresolved. Web search returned no official deprecation date for Sonnet 4.6. Sonnet 4.6 IS in the "Legacy models" accordion on the overview page, marked "Consider migrating to current models for improved performance" — but no scheduled retirement date. Only Claude Opus 4.1 has a hard retirement date (August 5, 2026); the others in the legacy table (Opus 4.8, 4.7, 4.6, Sonnet 4.6, 4.5, Opus 4.5) are still active.

**Effect on scope:** the design's "legacy-graceful" framing for Sonnet 4.6 holds. Design's "Active until at least Feb 2027" community claim is not confirmed but is not contradicted either. Leave the language as "legacy-graceful; no announced retirement" in KF text.

**Sources:**
- https://platform.claude.com/docs/en/about-claude/models/overview (fetched 2026-07-24)

---

## V6 — Prompt-compilation output/delivery contract + W4 root-cause classification

**Verdict:** Contract fully read. W4 root cause primarily matches **H1** (contract-shape gap), with an additional finding that reframes the "defect" itself.

**Current contract (SKILL.md lines 224-231, Project Mode Delivery):**
> "Present the complete Custom Instructions in its own code block…"
> "Present each knowledge file in its own code block, preceded by the filename and a one-line purpose statement. Each file's code block must be independently copyable — the user pastes it as a new knowledge file."

The Skill is designed for **inline code-block delivery**. The user pastes each block into the target field. Nothing in SKILL.md or references (checked: `five-layer-architecture.md`, `compilation-examples.md`) instructs file creation.

**W4 classification:**
- **H1 primary** — the contract exists and is coherent, but it prescribes code-block delivery, not file delivery. Design's "fix" is a **contract change from code-block-inline to file-creation**, not a defect fix within the existing contract.
- H2: RULED OUT — no delivery contract lives in a reference file that could be mis-placed.
- H3: partially applicable — the "code block" phrasing does not disambiguate between "code fence in chat" and "file with code content"; a Sonnet 5 run could rationalize either.
- H4: cannot be diagnosed from SKILL.md alone; needs failure evidence.

**Methodology-level concern (SBD §8.2 trigger — this is exactly what the reverse-handoff calls out):** the design frames W4 as a defect fix, but on inspection it is a **behavioral contract shift** (code-block → file). This changes the Skill's product surface. Per prompt reverse-handoff triggers: "W4 cause is methodology-level (SBD §8.2 — chat reviews methodology corrections)."

**Recommendation:** W4 fix belongs on the chat-side methodology review, not in this CC pass. Do not apply the H1-shaped fix without operator confirmation that a contract shift is intended.

---

## V7 — W2 grep sweep result

**Verdict:** Sweep manifest written to `5GEN_SWEEP_MANIFEST.md`. Change surface materially matches design expectations; two new findings:

1. **6 Skills lack `> **Calibration:**` markers**, not 3. Design names critic-gate, mode-router, repo-hygiene. Sweep also found **cc-design, handoff-trigger-check, profile-builder** lack markers. Adding markers to only 3 leaves 3 more without.
2. **Only 5 of the "7 T3" Skills have inline T3 calibration markers.** README asserts "Tier 3 — Opus-recommended (7 Skills)." The 5 with inline T3 markers are: global-audit, project-audit, context-budget, prompt-compilation, full-stack-audit. The other 2 T3 Skills (implied by README) are missing inline markers — likely cc-design and skill-builder or memory-optimization based on README table, needs confirmation.

**Sweep hit-counts (highest surfaces):**
- `4.7`: 133 hits across 29 files
- `4.6`: 134 hits across 32 files
- `4.8`: 104 hits across 49 files
- `Sonnet`: 83 hits across 22 files
- `Haiku`: 30 hits across 15 files
- `Fable`: 21 hits (all in the design doc — Skill catalog carries ZERO Fable references currently)
- `Opus` (rootnode-*/**/*.md only): 45 hits across 22 files
- `effort`: 149 hits across 38 files
- `xhigh|budget_tokens|extended thinking|tokenizer|1M-context/window`: 65 hits across 13 files
- `~66,500` (RAG threshold): 15 hits across 6 files
- `200K` references (context-window era): 15+ hits — pervasive in context-budget, OPT_REF, handoff-trigger-check

**W1 out-of-mirror KFs:** design §5-W1 names `root_CLAUDE_OPTIMIZATION_NOTES.md` and `root_AUDIT_FRAMEWORK.md` as W1 edits, but neither is present in `audit/canonical-kfs/`. These are seed-project-only KFs — edits must be surfaced as KF-update blocks per CLAUDE.md discipline, not applied directly.

---

## V8 — build_release_artifacts.py read-before-run

**Verdict:** Packager code is intact and matches the design's expectations, **with one blocker requiring scope expansion**.

Confirmed from the code (lines 44-181):
- Surface map matches design bucket assignment:
  - `CC_ONLY = {"critic-gate", "mode-router", "repo-hygiene"}` ✓
  - `DUAL = {"skill-builder", "cc-design"}` ✓
  - Everything else `rootnode-*` = cp-only (22 folders) ✓
- Suffix application: applied by the packager (lines 89-101), source folders remain un-suffixed. ✓
- Self-assert: `EXPECTED_TOTAL = 29`, `EXPECTED_CP = 24`, `EXPECTED_CC = 5` (lines 53-55), enforced with non-zero exit code 2 (lines 162-172). ✓
- `write_bundle()` intact (lines 104-113); called on full-build only (line 173). ✓
- 27 source folders confirmed present on disk (ls rootnode-*/), matches the 22+3+2 bucket split.

**BLOCKER — CATALOG_VERSION is stale:**
Line 59: `CATALOG_VERSION = "v3.1"` — this generates `dist/rootnode-catalog-v3.1.zip`, not `-v3.2.zip`. The bundle filename must be `rootnode-catalog-v3.2.zip` for the umbrella upload.

Per session prompt scope: "Out-of-scope | Edits to `build_release_artifacts.py`, `build_releases.py` (V8 findings that suggest a script change are recommendation-surface — HALT and report)."

The CATALOG_VERSION bump is required for the release to succeed. This is exactly the recommendation-surface case the prompt anticipated. **Return-to-chat: operator scope expansion needed to authorize the one-line CATALOG_VERSION edit (or provide an override path).** Alternative: pre-compute the bundle path with a wrapper that overrides `CATALOG_VERSION`, but that is a workaround, not a fix, and the file docstring / message strings still reference v3.1.

---

## Pre-flight untracked state (surfaced from Pre-flight)

- `design/root_skill_5gen_alignment_design.md` — expected untracked (Phase A step 2 commits it to `release/v3.2`).
- `audit/repo-catalog/` — **unexpected untracked**. Contains two v3.1-era markdown files (root_repo_catalog_20260627.md, root_repo_catalog_20260627_post-merge.md), dated 2026-06-27. Not in v3.2 scope. Operator decides whether to commit these on `release/v3.2`, on a separate branch, or leave untracked.

## Missing helper scripts

`generate_release_notes.py` and `create_releases.py` — noted as helpers in playbook §1.3 but not present in repo. Not required (the primary orchestrator is `build_release_artifacts.py`), but per-Skill release notes generation may need to be done by hand or with a helper the session prompt does not specify. Recommend adopting a `for skill in $(ls -d rootnode-*/); do ...` pattern in Phase B step 10 using `--notes-file` per playbook §2.

---

## HALT 0 SUMMARY — RETURN-TO-CHAT RECOMMENDED

**Reverse-handoff triggers fired (per session prompt "Return-to-chat triggers"):**

1. **Locked-decision rationale contradicted by evidence (D1).** Between the design's 7/21 lock date and today (7/24), Anthropic shipped **Claude Opus 5** (`claude-opus-5`), with Opus 4.8 reclassified to the "Legacy models" accordion on the models overview. Opus 5 is now Anthropic's recommended top general-purpose model (front-page recommendation: "start with Claude Opus 5 for complex agentic coding and enterprise work"). Opus 5 also carries its own safety classifiers alongside Fable 5 (per refusals-and-fallback page). D1's core rationale — "Opus 4.8 stays primary. Operator-confirmed. It remains the Fable fallback target, the practical top-capability workhorse for most paid users…" — is factually stale as of today. Executing v3.2 under D1's current wording ships a catalog calibration for a legacy-tier model as "primary."

2. **W4 cause is methodology-level (SBD §8.2).** The prompt-compilation W4 is a contract shift (code-block → file delivery), not a defect fix within the existing contract. Methodology corrections belong on the chat side, not autonomous CC execution.

3. **V8 finding requiring packager change.** `CATALOG_VERSION` line edit in `build_release_artifacts.py` is required for Phase B to produce `rootnode-catalog-v3.2.zip`. Prompt explicitly out-of-scopes packager edits and routes them to chat.

**Additionally surfaced:**
- V3 finding exceeds the design's "1M-window landscape note" — context-budget scope is a KF section rebuild, not an update. Anthropic Projects now use automatic RAG based on window size; the fixed ~66,500 threshold is superseded.
- V7 finding: 6 Skills lack calibration markers, not 3. Design D2 scope covers only the 3 CC-only.
- W1 lists 2 KFs (OPT_NOTES, AUDIT_FRAMEWORK) not in the canonical-kfs mirror — edits to these must be surfaced as KF-update blocks per CLAUDE.md, not applied directly.
- V4 (CC defaults) unresolved — needs a targeted fetch before cc-design/CC_EG edits.
- V2 (Sonnet 5 system-card behavioral deltas) unresolved — needs direct system-card read for behavioral-tuning table update.
- Sonnet 5 tokenizer official figure is ~30% more than Sonnet 4.6 (design's ~1.35x upper bound is close, but the exact number is available).

**Recommended chat-side reconciliation before continuing:**
- Re-open D1 given Opus 5 GA. Options span (a) redefine "primary" as Opus 5 + Sonnet 5 dual-primary with Opus 4.8/Fable 5 integrated-aware; (b) hold D1 as written with an explicit "Opus 4.8 is intentionally the primary despite Opus 5 GA, because [reason]" — operator business call; (c) escalate to v4.0.
- Decide W4 contract-shift: yes/no. If yes, methodology added to SBD §8-adjacent doc first, then CC pass applies.
- Authorize packager `CATALOG_VERSION` edit (or provide alternate path).
- Decide V3 scope: keep the "revalidation pending" fallback framing, or invest in a context-budget section rebuild that reflects Anthropic's automatic-RAG model.
- Decide V7 marker gap: add markers to all 6 missing Skills, or scope to the 3 the design names + a follow-on session.

Verified state on halt: no repo edits made in Phase 0 (verification-only phase). Working tree carries the two pre-existing untracked items plus this log and the sweep manifest.

---

# Session 2 (v2.0 execution) — appended 2026-07-25

**Design doc:** `design/root_skill_5gen_alignment_design.md` **v2.0** (Opus 5 GA revision), committed on `release/v4.0` at commit `687954f`.
**Branch:** `release/v4.0` (pushed, tracking `origin/release/v4.0`).
**PR #15 (repo reconciliation) in main history:** confirmed — `a80c61e` merge commit.

**Prior session's return-to-chat produced design v2.0.** That reconciliation is what promoted the release target from v3.2 to v4.0, redefined "primary" as Opus 5 + Sonnet 5 dual-primary with Opus 4.8 fallback-graceful, authorized D5 contract shift, authorized D6 context-budget rebuild, expanded D7 to include the version-agnostic notes generator, and added D4 (verification-instruction discipline) and D8 (mirror completion + landscape-volatility discipline). This session executes v2.0.

## O10 staleness diff — 5 mirrored KFs, CRLF-normalized

Precondition confirmed by operator: `audit/canonical-kfs/` clean against HEAD before diff (verified via `git status audit/canonical-kfs/` and `git diff HEAD -- audit/canonical-kfs/` returning empty).

| File | Content-diff lines (CRLF-normalized) | Raw-diff lines (line-ending sensitive) | Verdict |
|---|---|---|---|
| root_AGENT_ANTI_PATTERNS.md | 0 | 728 | CRLF-only drift; no content divergence |
| root_AGENT_ENVIRONMENT_ARCHITECTURE.md | 0 | 848 | CRLF-only drift; no content divergence |
| root_CC_ENVIRONMENT_GUIDE.md | 0 | 954 | CRLF-only drift; no content divergence |
| root_OPTIMIZATION_REFERENCE.md | 0 | 2060 | CRLF-only drift; no content divergence |
| root_SKILL_BUILD_DISCIPLINE.md | 0 | 0 | Byte-identical (matches staging including line endings) |

**Verdict:** all 5 mirrored KFs are content-identical to their staged seed copies. **No canonical drift to reconcile.** Staging is the current-generation seed content ready for Phase 3 sync (Phase 3 sync converts line endings as needed; mirror integrity is intact regardless). Two D8 additions (`root_AUDIT_FRAMEWORK.md`, `root_CLAUDE_OPTIMIZATION_NOTES.md`) remain in staging awaiting Phase 1 edits → Phase 3 sync.

## V2 — Sonnet 5 system card / behavioral deltas

**Status:** **STILL PARTIAL.** Direct system card not fetched this pass either. Behavioral deltas vs 4.6 (misuse cooperation, deception) remain not-verbatim on the whats-new page; Anthropic points to `anthropic.com/transparency` for benchmarks. Design v2.0 §3 D2 already anticipates this: "Where the card is silent, the column reads 'no delta documented' — never inherit a 4.6 value silently." Behavioral-tuning Sonnet 5 column will reflect this rule at Phase 1 execution.

## V3 — Projects RAG threshold — RESOLVED

Support article fetched this session (correct host `support.claude.com`):

- Verbatim: "RAG automatically activates when your project approaches or exceeds the context window limits."
- Verbatim: "Instead of loading all project content into memory at once, Claude intelligently searches and retrieves only the most relevant information needed to answer your questions."
- **No fixed token threshold specified.** No mention of 66,500 tokens or any specific figure.
- No per-model behavior variations noted.
- Article mentions "10x" capacity expansion (no per-model concrete numbers).

**D6 gate verdict:** context-budget IS a rebuild. The ~66,500 threshold is not stale-but-directionally-right — it is a wrong mental model. Context-budget Step 4 math, tier bands, and budget-pool table all derive from it and must be recalibrated.

**Preserved distinction:** a model's context window ≠ the Projects RAG threshold — they were numerically entangled under the 200K era; now the Projects RAG threshold *is* the context window (or close to it). Explicit statement required in the rebuild.

**Sources:** https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects (fetched 2026-07-25)

## V4 — Claude Code default model + effort defaults post-Opus-5 — PARTIAL

**Effort default (RESOLVED):** From Opus 5 whats-new + models overview + prompting guide: on Claude Opus 5 and Claude Sonnet 5, `effort` **defaults to `high` on the Claude API and Claude Code.** Full ladder: `low`, `medium`, `high`, `xhigh`, `max`. "Start at the default, `high`, and adjust in either direction based on your evals."

**CC default *model* (UNRESOLVED this pass):** No CC-defaults page fetched. Recommendation for Phase 2 W3 cc-design edits: use "consult Claude Code docs at update time" caveat rather than hardcode — the model default likely moves with Claude Code product releases and hardcoding invites drift. If a targeted CC-docs fetch is easy in Phase 2, do it; otherwise leave the caveat.

## V5 — Model deprecation timelines — RESOLVED

Verbatim from Anthropic Model deprecations page (fetched 2026-07-25):

| Model | Current state | Retirement (not sooner than) |
|---|---|---|
| claude-fable-5 | Active | June 9, 2027 |
| claude-opus-5 | Active | July 24, 2027 |
| claude-opus-4-8 | Active | **May 28, 2027** |
| claude-opus-4-7 | Active | April 16, 2027 |
| claude-opus-4-6 | Active | February 5, 2027 |
| claude-opus-4-5-20251101 | Active | November 24, 2026 |
| claude-opus-4-1-20250805 | **Deprecated 2026-06-05** | **August 5, 2026** (retirement) |
| claude-sonnet-5 | Active | June 30, 2027 |
| claude-sonnet-4-6 | Active | **February 17, 2027** |
| claude-sonnet-4-5-20250929 | Active | September 29, 2026 |
| claude-haiku-4-5-20251001 | Active | October 15, 2026 |

**Design language holds:** Opus 4.8 fallback-graceful posture is safe for ~10 months (May 2027 earliest retirement); Sonnet 4.6 legacy-graceful holds through Feb 2027 (matches the community claim, now Anthropic-confirmed).

**Sources:** https://platform.claude.com/docs/en/about-claude/model-deprecations (fetched 2026-07-25)

## V9 — Fallback beta header conflict — RESOLVED

Verbatim from the refusals-and-fallback page: "The beta header must carry exactly the date `2026-07-01`, which supports both `\"default\"` and the explicit-list form below, or `2026-06-01`, which accepts only the explicit-list form."

Verbatim from Opus 5 whats-new: "The `fallbacks` parameter supports a new `\"default\"` mode… Use the `server-side-fallback-2026-07-01` beta header, which supports both the `\"default\"` mode and explicit model lists (the earlier `server-side-fallback-2026-06-01` header accepts only explicit lists)."

**No conflict.** These are two distinct beta header versions for two feature levels: `2026-06-01` = explicit list only; `2026-07-01` = both `"default"` mode and explicit list. Both are current, both are valid. KF language: `server-side-fallback-2026-07-01` for the full feature, `2026-06-01` for the legacy explicit-list-only path.

**Sources:**
- https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback (fetched 2026-07-25)
- https://platform.claude.com/docs/en/about-claude/models/whats-new-opus-5 (fetched 2026-07-25)

## V10 — Opus 5 alignment/safety claims — RESOLVED

Verbatim from anthropic.com/news/claude-opus-5 (fetched 2026-07-25):

- Alignment: "our most aligned model to date" per automated behavioral audit; misalignment score **2.3** (lowest of recent models).
- Constitution adherence: better than Opus 4.8, Sonnet 5, or Fable 5.
- Deceptive behavior: "the lowest rates" among tested models.
- Misuse: "the least susceptible to being tricked into misuse."
- Cyber classifiers: "proportionally less restrictive than those on Fable 5"; expected to intervene "around 85% less often than they do for Fable 5."
- Cyber restrictions: blocks binary-based vulnerability scanning, penetration testing, and exploit generation. Source-code vulnerability finding permitted.
- Fallbacks: Opus 5 refusal → Opus 4.8 by default on Claude.ai, Claude Code, Claude Cowork.
- Availability: Claude API (`claude-opus-5`), Claude.ai, Claude Code, Claude Cowork. Bedrock/GCP/Foundry not named on the announcement page, but named on the models overview and whats-new pages.
- Release date: **2026-07-24**.
- Product surfaces: "New default model on Claude Max"; "Strongest model on Claude Pro."

**Sources:**
- https://anthropic.com/news/claude-opus-5 (fetched 2026-07-25)
- https://platform.claude.com/docs/en/about-claude/models/whats-new-opus-5 (fetched 2026-07-25)

## Opus 5 prompting guide — D4 rationale verbatim confirmation

Reading `platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5` this session confirms all of D4's language traces to the official guide:

- Verification: "If your prompt contains explicit verification instructions ('include a final verification step for any non-trivial task,' 'use a subagent to verify'), remove them: instructions like these cause over-verification on Claude Opus 5, and removing them reduces wasted tokens with no loss in quality."
- Conservative-review literalism: "If your review prompt says 'only report high-severity issues' or 'be conservative,' the model may follow that instruction literally and report less; ask it to report everything and filter in a separate pass instead."
- Subagent delegation: "do not use subagents to verify or double-check your own work"; "cap delegation."
- Scope constraint: "Deliver what was asked, at the scope intended. Make routine judgment calls yourself…"
- Correction narration: "Only correct an earlier statement when the error would change the user's code, conclusions, or decisions."
- Response length: "The [effort parameter] controls how much the model thinks rather than how much it says: lowering effort can reduce thinking volume without reliably shortening the visible response. To control response length, prompt for it explicitly."
- Written deliverables: "files that Claude Opus 5 writes to disk (reports, Markdown documents, summaries) are often longer than on prior models."
- Thinking-disabled artifacts: "the model can emit `<thinking>` tags or other internal XML tags into its visible response. If your system prompt contains a rule instructing the model not to think or not to reason, remove it; that kind of instruction increases tag leakage."

D4 (locked) matches Anthropic's guidance verbatim. No re-decision.

## Refusal-fallback API shape — reference for W1/W3 KF language

From the refusals-and-fallback page (fetched 2026-07-25):

- **Refusal categories:** `cyber`, `bio`, `frontier_llm`, `reasoning_extraction`, `general_harms`. Design v2.0 names the first four; `general_harms` is a fifth category to include in domain-agentic-context.
- **`fallback` content block shape:** `{"type": "fallback", "from": {"model": ...}, "to": {"model": ...}}` marks each model boundary.
- **`usage.iterations` shape:** each attempt is an entry; `type: "message"` for declined, `type: "fallback_message"` for the one that served the response.
- **"Instrument refusals as their own signal" pattern:** verbatim — "A refusal is an HTTP 200, so monitoring built on error rates or 5xx responses never sees it. Emit one event per refusal and one per fallback-served response (the `fallback_message` entry in `usage.iterations` marks the latter), then alert on the gap between the two counts."
- **Sticky routing:** after a fallback fires, subsequent requests for the same conversation route directly to the fallback model, retained ~1 hour, org-scoped, content-hash keyed.
- **Server-side fallback availability:** Claude API only; not on Amazon Bedrock, Google Cloud, or Microsoft Foundry. On those platforms use client-side SDK middleware.

## Packager V8 verification (re-read this session)

`build_release_artifacts.py` read in full:

- Line 44-46: `REPO_ROOT = Path(__file__).resolve().parent`, `DIST_DIR`, `SKILL_PREFIX = "rootnode-"`.
- **Line 49:** `CC_ONLY = {"critic-gate", "mode-router", "repo-hygiene"}` — matches design + surface map.
- **Line 50:** `DUAL = {"skill-builder", "cc-design"}` — matches.
- **Lines 53-55:** `EXPECTED_TOTAL = 29`, `EXPECTED_CP = 24`, `EXPECTED_CC = 5` — self-assert intact.
- **Line 59:** `CATALOG_VERSION = "v3.1"` — **must bump to `"v4.0"` per D7 in Phase 3.2 step 3.**
- **Lines 89-101 (`write_zip`):** anchor logic correct (`skill_path` for CP flat / `skill_path.parent` for CC wrapper); suffix applied by the packager (line 90: `f"{skill_path.name}-{surface}.zip"`).
- **Lines 104-113 (`write_bundle`):** intact; bundle name uses `CATALOG_VERSION`.
- **Lines 162-172:** assertion enforced with `sys.exit(2)` non-zero exit on mismatch.
- **Line 173:** `write_bundle(built)` called only when `not specific` — full-build only.

Confirmed 27 source folders on disk via `find_skills()` iteration over `rootnode-*`; the 22 cp-only / 3 cc-only / 2 dual bucket split matches.

**No changes suggested beyond the `CATALOG_VERSION` bump.** Any *other* packager change remains recommendation-surface per D7.

## D4 pattern sweep results — new for v2.0

Case-insensitive greps across all Markdown in the repo (Skill folders, canonical KFs, README, docs, release-notes, design, audit):

- **Verification-instruction patterns** (`double-check`, `re-verify`, `verify your (own )?work`, `verification step`, `subagent to verify`, `check your answer`): **30 occurrences across 17 files.** Per-file classification (self-re-check → remove vs external-artifact → keep) happens in Phase 2 W0.
- **Conservative-instruction literalism patterns** (`high-severity`, `be conservative`, `only report`, `only flag`): **9 occurrences across 8 files.**
- **Opus 5 / opus-5 in-catalog:** **0 occurrences.** The Skill catalog carries zero Opus 5 references — D1 integration-floor adds Opus 5 content across model-fact-bearing artifacts in Phase 1.
- **Fable in-catalog:** **0 occurrences** (unchanged from prior session's V7 finding — the catalog still carries zero Fable content; D1 integration floor requires adding).
- **Fast mode / max effort / prompt cach in-catalog:** 0 occurrences — new content required per Opus 5 landscape additions.

Full extended sweep manifest at `audit/v4_0-alignment/5GEN_SWEEP_MANIFEST.md` (rewritten this session; prior manifest superseded per design §8-W0).

## Web access confirmation

Web access confirmed operational this session. All Anthropic source pages fetched inline; no fetches blocked. WebFetch handled a 301 redirect from `support.anthropic.com` → `support.claude.com` correctly (V3 re-fetched at redirect target).

## Locked-decision contradictions

**None found.** Every V-item resolved this session confirms rather than contradicts design v2.0 D1–D8:

- D1 dual-primary + fallback-graceful + integrated-aware taxonomy consistent with the models overview + deprecation page (Opus 4.8 active until 2027).
- D2 effort inversion (`high` start, `xhigh` step-up, `low`/`medium` as primary cost controls) confirmed by Opus 5 whats-new + prompting guide.
- D3 v4.0 justification stands — D4 methodology + D5 contract shift are major-line changes.
- D4 verification/conservative discipline matches Opus 5 prompting guide verbatim.
- D5 contract shift is a public product-surface change; justification unchanged.
- D6 context-budget rebuild confirmed by V3 — 66,500 mental model is superseded.
- D7 packager bump + D7 expansion (version-agnostic notes generator) needed for v4.0 mechanics.
- D8 mirror completion (add OPT_NOTES + AUDIT_FRAMEWORK to canonical-kfs) — staging is ready.

## Untracked state disposition (Phase 3.2 step 7 preview)

- `audit/v4_0-alignment/5GEN_VERIFICATION_LOG.md` (this file, prior + current session) — **recommend commit** on `release/v4.0` before Phase 1 so the log is durable.
- `audit/v4_0-alignment/5GEN_SWEEP_MANIFEST.md` (rewritten this session) — **recommend commit** on `release/v4.0` before Phase 1.

Operator decides at HALT 0.
