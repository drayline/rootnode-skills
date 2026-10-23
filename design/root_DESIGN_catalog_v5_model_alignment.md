# root_DESIGN_catalog_v5_model_alignment — design spec

**Cycle:** rootnode-skills catalog v5.0 (5.5-generation alignment)
**Inputs:** `root_MODEL_LANDSCAPE_2026-10.md` (the dated landscape block — every model fact below cites it; none is restated as a durable fact); repo `drayline/rootnode-skills` at `820e5c0` (2026-09-13 catalog-regen merge; catalog `audit/repo-catalog/root_repo_catalog_20260913.md`); `rootnode-skill-builder` v4.0.0 (pre-build gates and the 9-dimension gate applied in §6).
**Companion specs:** `root_DESIGN_cc-design_v5.md` (the only Skill with structural change), `root_DESIGN_behavioral-tuning_v5.md` (the only Skill with taxonomy change). This spec owns the other 25 Skills and all catalog-level surfaces.
**Status:** DRAFT for operator decision on D1–D6. CC build prompt follows acceptance.

---

## 1. Why this is a major version, not a patch

The v4.0 precedent: a model-generation change touched every Skill's calibration line, the README compatibility section, the tendency taxonomy, and the context-budget window table, and shipped as one catalog cut under the anti-churn rule (playbook). The 5.5 generation repeats every one of those triggers and adds three new ones: the effort default moved (`high` → `medium` on the Claude Code default model), thinking became non-disableable on the primary tier, and a documented behavior (early turn termination) has no home in the 14-tendency taxonomy. Shipping 27 patch bumps would violate the anti-churn rule; shipping only cc-design would leave 26 Skills asserting "Opus 5 or Sonnet 5 (both default to `high`)" — a landscape claim that is now false on the default model.

## 2. Decisions for the operator

| # | Decision | Recommendation | Rationale | Alternative rejected |
|---|---|---|---|---|
| D1 | Catalog version | **v5.0; every Skill → 5.0.0**; cc-design 4.2.0 → 5.0.0 with `predecessor: "rootnode-cc-design v4.2"` | v4.0 precedent for a generation alignment; one cut per the anti-churn rule; the catalog umbrella `catalog-v5.0` becomes Latest | v4.1 catalog + cc-design 4.3 — leaves "4.x" implying landscape continuity that does not exist |
| D2 | Calibration scope sentence | **Opus 5.5 + Sonnet 5.5 dual-primary; Fable 5.1 integrated-aware; Haiku 5.5 subagent-aware; Opus 5 / Sonnet 5 fallback-graceful; Sonnet 4.6 and Haiku 4.5 legacy-graceful until retirement** | Mirrors the CC default (Opus 5.5 on all Anthropic-hosted plans) and Anthropic's "start with Opus 5.5" guidance; Haiku 5.5 is the first Haiku that fits a subagent role with effort control (landscape §1, §6) | Fable 5.1 as primary — not the default anywhere, $10/$50, and Anthropic routes most workloads to Opus 5.5 first |
| D3 | Tier structure | **Unchanged** (T1 Model-compatible / T2 Sonnet-graceful / T3 High-effort recommended); only the model column refreshes | Landscape-independent per AEA §4.15 — proven by v4.0 → v5.0 surviving intact | Rename T2 to "Haiku-graceful" — premature; Haiku 5.5 multi-dimensional depth is unmeasured |
| D4 | Effort guidance in T3 lines | **"Opus 5.5 at its `medium` default or `high`; Sonnet 5.5 at `high`; `xhigh` only on measured gain"** | Anthropic: Opus 5.5 at `medium` "matches or exceeds Opus 5 at `high`"; `xhigh`/`max` are reserved for measured gains in all four guides; Sonnet 5.5 at `xhigh`/`max` self-launches reviewer subagents (cost +~⅓) | Keep "`high` default" wording — false on the CC default model from v2.1.280 |
| D5 | Tendency taxonomy | **Add #15 Early turn termination** (spec in `root_DESIGN_behavioral-tuning_v5.md` §2) | Documented with prompt countermeasures in four Anthropic prompting guides (Opus 5.5, Sonnet 5.5, Haiku 5.5, Fable 5.1) — meets the SBD §7.3 warrant (named-primary-source documentation) and is not expressible as a facet of #12 or #6 (those are "too much"; this is "too little") | Fold into #12 scope expansion — inverts the countermeasure direction and would make the #12 template contradict itself |
| D6 | Haiku 4.5 handling | **ACCEPTED (revised 2026-10-22): drop "Haiku 4.5" from all three calibration templates; add one README line — "On third-party providers the `haiku` alias may still resolve to Haiku 4.5; pin `claude-haiku-5-5` via `ANTHROPIC_DEFAULT_HAIKU_MODEL`."** | The landscape is built around Haiku 5.5; a degradation clause for a 200K/extended-thinking model is dead weight, while the pin line tells third-party-provider users what to do | Keep the legacy clause — a statement about what degrades rather than what to do |

## 3. Catalog-level surfaces

### 3.1 Calibration line templates (one per tier; replaces the v4.0 line verbatim in every SKILL.md)

Tier 1 (13 Skills):
> **Calibration:** Tier 1 (Model-compatible) — runs cleanly on the current dual-primary tier (Opus 5.5, Sonnet 5.5) and on Haiku 5.5. Structured retrieval, rule evaluation, or template lookup — output shape does not depend on the model. Fallback-graceful on Opus 5 / Sonnet 5; legacy-graceful on Sonnet 4.6. See repository README for model compatibility.

Tier 2 (7 Skills):
> **Calibration:** Tier 2 (Sonnet-graceful) — designed against Opus 5.5 + Sonnet 5.5 dual-primary. Runs on Haiku 5.5 at `high` effort with less depth on multi-dimensional analysis; fallback-graceful on Opus 5 / Sonnet 5; legacy-graceful on Sonnet 4.6. Start at the model's default effort (`medium` on Opus 5.5 and Sonnet 5.5 in Claude Code; `high` for Sonnet 5.5 on the Claude API) and re-run an effort sweep on your own evals rather than carrying a setting over. See repository README for model compatibility.

Tier 3 (7 Skills):
> **Calibration:** Tier 3 (High-effort recommended) — run on Opus 5.5 (start at its `medium` default; step to `high` when verification matters or edge cases are likely) or Sonnet 5.5 at `high`. Step up to `xhigh` only where your evals show a measured gain. Quality degrades at `low` effort and on legacy models (Sonnet 4.6). Reserve Fable 5.1 for long-horizon runs where Opus 5.5 at higher effort still fails your evals. See repository README for model compatibility.

Rules for the build: the line is replaced whole (never patched word-by-word); every other `Opus 5` / `Sonnet 5` / `Haiku 4.5` / `Fable 5` mention in a SKILL.md body is handled by the per-Skill row in §4, not by a global find-and-replace — several v4.0 sentences are historical statements ("the v4.0 alignment cycle shipped…") that stay as written.

### 3.2 README.md

Replace the blockquote at line 31 and the whole "Model Compatibility" section (lines 107–123) with the D2 scope sentence (Haiku 4.5 named only in the out-of-scope list), the three tier paragraphs (model column refreshed), the D6 pin line ("On third-party providers the `haiku` alias may still resolve to Haiku 4.5; pin `claude-haiku-5-5` via `ANTHROPIC_DEFAULT_HAIKU_MODEL`"), a new "Effort" paragraph (defaults differ by model and surface; cite the landscape block's table; "Do not carry effort settings over" sentence kept), and a rewritten "Fallback semantics" paragraph: refusals still return HTTP 200 + `stop_reason: "refusal"`; server-side fallback is per-model (Opus 5.5 `fallbacks: "default"`; Sonnet 5.5 → Sonnet 5 for `cyber`/`frontier_llm` only; **Haiku 5.5 none**; Fable 5.1 → Opus 4.8 / Opus 5); refusal billing changed 2026-09-24. Tier counts (13/7/7) are recomputed from the §4 table at build time, not copied. Tier-1/2/3 cells in the catalog tables are unchanged.

### 3.3 Repo CLAUDE.md

No model facts live here. Only the packaging count sentence is checked at build time (27 source folders, 24 + 5 = 29 artifacts — unchanged by this cycle unless cc-design adds a `schema/` file, which does not change zip counts).

### 3.4 Release notes

`generate_release_notes.py` config under `audit/v5.0-*/` per the playbook; `TIER_LABEL` strings updated to the §3.1 wording. The single-Skill-cut shape (playbook §1.5) does not apply — this is a catalog cut.

### 3.5 Knowledge-file propagation (surfaced as `audit/<session>/kf-update-blocks.md`, never edited in `canonical-kfs/` directly — repo CLAUDE.md halt #5)

| Target KF | Action | Block |
|---|---|---|
| root_CLAUDE_OPTIMIZATION_NOTES.md (mirror) | REVISE | Replace the dated model-landscape block with `root_MODEL_LANDSCAPE_2026-10.md` §1–§4, §6 |
| root_OPTIMIZATION_REFERENCE.md (mirror) | ADD | Tendency #15 (from the behavioral-tuning spec §2); REVISE #7 (fix direction flipped), #11 (thinking-instruction extension), #12 (unrequested-additions facet), #13 (effort-conditioned reviewer-launch facet); REVISE the conditional-defect subsection (thinking-disabled artifacts now Haiku-only) |
| root_AUDIT_FRAMEWORK.md (mirror) | REVISE | Dimension 6 scores against the 15-tendency taxonomy; "penalizes countermeasure sets calibrated for pre-Opus-5 models" → "pre-5.5 models" |
| root_AGENT_ANTI_PATTERNS.md (mirror) | REVISE | §6 pointer list: fourteen → fifteen; add the three structural-catalog candidates from the cc-design spec §7 (unbounded Stop hook, exit-code enforcement-as-preference, two owners per rule) as not-yet-promoted |
| root_CC_ENVIRONMENT_GUIDE.md (mirror) | REVISE | §3.4 (Claude Code defaults: Opus 5.5 default model restated as *not* restated; effort defaults `medium` on the 5.5 trio; thinking non-disableable; `thinking: disabled` 400 rule now model-specific), §1.4 / §6 cap table (`CLAUDE_CODE_WORKFLOW_SUBAGENT_MODEL`, Agent-tool `effort`, version markers), §3.5 role table model column (Haiku 5.5 as Scout tier) |
| root_SKILL_BUILD_DISCIPLINE.md (mirror) | REVISE | §3.9 D9a grader models: Opus 5.5 or Sonnet 5.5 (Opus 5 / Sonnet 5 valid fallback); D9c cites the 15-tendency taxonomy |
| root_build_context.md (seed only) | ADD | Phase entry for the v5.0 cycle; Observation candidate O28 (a Skill's own hook examples were enforcement-as-preference for two major versions because the exit-code claim was never verified against the artifact — a stale-proxy instance: the claim was checked against memory of the docs, not the docs) |
| CI `<knowledge_files>` | REVISE | First trigger: counts (fourteen → fifteen), "pre-Opus-5" → "pre-5.5", CLAUDE_OPTIMIZATION_NOTES description's landscape date |
| global `~/.claude/CLAUDE.md` | NOT APPLICABLE | Model landscape facts fail the AEA §5.5 universality test by definition (§4.15) |

## 4. Per-Skill delta table (all 27)

Legend — **L** = calibration line only (§3.1 template by tier) + `metadata.version` → `5.0.0`; **L+** = line plus the listed body edits; **S** = separate spec. Line numbers are from `820e5c0` and are anchors for the build prompt, which binds halts to post-edit digests, never to these numbers.

| Skill | Tier | Scope | Body edits beyond the calibration line |
|---|---|---|---|
| rootnode-anti-pattern-detection | T2 | L+ | Anywhere the Skill cites the behavioral taxonomy count or "Opus 5" conditioning: 14 → 15; add #15 to any symptom-routing table that lists tendencies by number (verify by grep at build; SKILL.md line 27 is the only model mention found) |
| rootnode-behavioral-tuning | T2 | **S** | `root_DESIGN_behavioral-tuning_v5.md` |
| rootnode-block-selection | T1 | L | — |
| rootnode-cc-design | T3 | **S** | `root_DESIGN_cc-design_v5.md` |
| rootnode-context-budget | T3 | L+ | (a) line 68: context window "1M for Fable 5.1 / Opus 5.5 / Sonnet 5.5 / Haiku 5.5"; delete the "200K for Haiku 4.5" clause from the primary sentence and move it to a legacy note. (b) lines 84–85: the 200K-Haiku paragraph becomes legacy-only; the 1M framing is now universal on current models. (c) lines 93–95 tokenizer notes: Fable 5.1 and Haiku 5.5 share the Opus 4.7-era tokenizer (~30% more than pre-4.7 / Haiku 4.5); Sonnet 5.5 = Sonnet 5 tokenizer; **Opus 5.5 tokenizer unstated — keep the "treat with tolerance until `count_tokens`" line**. (d) table at lines 115–116: four current rows (all 1M / 128K) + Haiku 5.5's >100K price band as a budget note; Haiku 4.5 row moves under a "legacy" sub-row. (e) line 355: "Context window: 1M" unchanged. (f) NEW budget note: cache-read pricing fell (Fable 5.1 0.025×, Opus/Sonnet 5.5 0.05×) — "compacting early to save cost may no longer be the right cost-intelligence tradeoff" [Anthropic, Fable 5.1 prompting guide]; later compaction points are a legitimate experiment. (g) line 123 historical ~66,500 paragraph unchanged |
| rootnode-critic-gate | T2 | L+ | Add one paragraph under its output contract: a reviewer that could not inspect returns `status: blocked`, never an empty findings list (AI-DLC-derived; see cc-design spec §5.3 for the shared wording). Advisor-tool note: when the critic runs via the API advisor tool, the advisor must be at least as capable as the executor (landscape §4.9) |
| rootnode-domain-agentic-context | T1 | L+ | Section "v4.0 update — refusal & fallback semantics (Opus 5, Fable 5)" → retitle "Refusal & fallback semantics (5.5 generation)". Keep the five categories. REVISE fallback: per-model table from landscape §4.6 (Haiku 5.5 has **no** server-side fallback; Fable 5.1 targets Opus 4.8 / Opus 5; Sonnet 5.5 → Sonnet 5 for `cyber`/`frontier_llm` only); refusal billing change 2026-09-24. ADD harness rules: (1) never place user text inside a `tool_result` block — Sonnet 5.5 / Haiku 5.5 read it as injection; mid-turn input goes in a text block after the last `tool_result`, harness notices in a separate mid-conversation system message; no token countdowns in interactive sessions; (2) forced `tool_choice` removed — "state in the prompt when the tool applies" + `strict: true`; (3) progress-update text arrives in `thinking` blocks — set `thinking.display` or the client goes silent; (4) time budgets for multi-agent harnesses (`elapsed Ns / Ms`, advisory). Line 89 (reasoning-approaches.md) unchanged |
| rootnode-domain-business-strategy | T1 | L | — |
| rootnode-domain-content-communications | T1 | L+ | ADD one note under its formatting guidance: Fable 5.1 formats less and writes denser prose by default; v4.0-era anti-list / anti-bold countermeasures can now suppress structure the content needs — prefer the conditional formulation ("use lists when the content is multifaceted enough that they help") [Anthropic, Fable 5.1 prompting guide] |
| rootnode-domain-research-analysis | T1 | L+ | ADD: on Fable 5.1, summaries may reproduce source passages without quotation marks — require marked quotations in the Output layer and supply one worked example when the deliverable quotes sources [Anthropic]. ADD: search-triggering nudge for `low` effort (Haiku 5.5 / Fable 5.1): give the current date; remove tool-discouraging language |
| rootnode-domain-software-engineering | T1 | L+ | Replace section "v4.0 update — Opus 5 cyber classifier posture" (lines 36–54) with "Cyber classifier posture (5.5 generation)": Opus 5.5 ships under the same bio + cyber safeguards as Fable; Fable 5.1 triggers ~60% fewer interventions per CC session than Fable 5 (Anthropic via VentureBeat — Tier 2 source, marked); Sonnet 5.5 is the first Sonnet with frontier cyber safeguards; "finding vulnerabilities in source code is allowed; high-risk dual-use is not" (all four guides); false-positive reducers: ask "are there bugs" not "does this compile", supply docs for lesser-known languages, strip base64 from tool output [Fable 5.1 guide]. Delete the 85% figure. Fallback destination paragraph → per-model table reference. Keep the conservative-review-instruction fix (line 54) verbatim — still documented. ADD: the "run a real check that exercises the change" verification block (Sonnet 5.5 / Haiku 5.5 guides, verbatim) as the Output-layer external-verification template for code tasks; ADD: "surgically edit a file rather than rewrite" (Fable 5.1) as a token-cost rule |
| rootnode-full-stack-audit | T3 | L+ | Lines 16, 45: effort phrasing → §3.1 T3 wording; "fourteen" → "fifteen" where Dimension 6 is described |
| rootnode-global-audit | T3 | L+ | Lines 16, 45: same as full-stack-audit |
| rootnode-handoff-trigger-check | T1 | L+ | Section "v4.0 update — condition 7" (lines 36–42): all four current models are 1M (Haiku 5.5 included — the "Haiku 4.5 remains at 200K" clause becomes legacy-only); effort paragraph → "Opus 5.5 / Sonnet 5.5 / Haiku 5.5 default to `medium` in Claude Code; Sonnet 5.5 and Fable 5.1 default to `high` on the API" with the "effort controls thinking depth, not response length" sentence kept; tokenizer note → "Sonnet 5.5 = Sonnet 5 tokenizer; Haiku 5.5 ≈ 30% more tokens than Haiku 4.5; apply the multiplier only when the estimate was calibrated to the older model". ADD Haiku 5.5 >100K-prompt price band as a condition-7 cost note |
| rootnode-identity-blocks | T1 | L | — |
| rootnode-memory-optimization | T2 | L | — |
| rootnode-mode-router | T1 | L | — |
| rootnode-output-blocks | T1 | L | — |
| rootnode-profile-builder | T1 | L | — |
| rootnode-project-audit | T3 | L+ | Lines 16, 43: same as full-stack-audit; Dimension 6 count |
| rootnode-project-brief | T1 | L | — |
| rootnode-prompt-compilation | T3 | L+ | Lines 16, 53: T3 wording. Line 272: "On Opus 5" → "On the 5.5 generation". ADD to Stage 4 Validate (routing surface; detail in `references/five-layer-architecture.md` Reasoning layer, line ~196): **reasoning-extraction check** — a Reasoning-layer instruction that asks the model to reproduce its internal reasoning in the response text can be declined with `stop_reason: "refusal"`, category `reasoning_extraction`, on every current model; task-specific analytical steps and "a short explanation of the answer or a summary of actions taken" are fine; "think carefully before answering" lines are removed (effort is the control) [Anthropic, Opus 5.5 / Sonnet 5.5 guides]. ADD to Project Mode: thinking cannot be disabled on the primary tier, so scaffolds no longer carry thinking-disabled mitigations |
| rootnode-prompt-validation | T2 | L+ | `references/symptom-fix-map.md`: ADD row "Prompt returns `stop_reason: refusal` / category `reasoning_extraction`" → Reasoning layer → remove reproduce-your-reasoning instructions; read `display: "summarized"` blocks. ADD row "Prompt tells the model to think less / answer directly and it still thinks" → not a prompt defect; lower effort (Sonnet 5.5 / Haiku 5.5 guides: prompt-level think-less instructions do not reliably reduce thinking). Line 156 (self-consistency) unchanged |
| rootnode-reasoning-blocks | T1 | L+ | D9c sweep of every block for "write out / show your reasoning in the response" phrasing; rewrite any hit to "state the conclusion and a short rationale" (reasoning-extraction category). Build records the hit count (expected: 0–2; the grep in this design found none in SKILL.md, references not yet swept) |
| rootnode-repo-hygiene | T3 | L+ | Cat 2 (hooks) check gains one item: a `command` hook that enforces with `exit 1` is non-blocking — flag as enforcement-as-preference; `settings.json` hook entries must match the documented shape (`matcher` string + `hooks: [{type, command, timeout}]`) [Anthropic hooks doc, 2026-10-22]. This is the audit-side twin of the cc-design fix |
| rootnode-session-handoff | T1 | L | — (its completeness gate is unchanged; the session-report standard in the cc-design spec §5 points at session-handoff rather than duplicating it) |
| rootnode-skill-builder | T2 | L+ | SKILL.md line 29 → T2 template with "D9a graders run on Opus 5.5 or Sonnet 5.5 (Opus 5 / Sonnet 5 valid fallback)". **Line 121 and `references/behavioral-validation.md` lines 36, 90: "10-tendency taxonomy" → "15-tendency taxonomy"** (a v4.0 propagation miss — the taxonomy was 14 when v4.0 shipped). `references/multi-environment-adaptation.md`: Haiku 5.5 is a valid Tier-A grader-environment *subject* model but not a grader |

Counts, computed from the table: S = 2, L = 9, L+ = 16; 2 + 9 + 16 = 27.

## 5. Test plan (one test pass, one fix pass, then ship — the standing stopping rule)

| Test | Instrument | Pass condition |
|---|---|---|
| T1 Landscape consistency | `grep -rnE 'Opus 5\b|Sonnet 5\b|Haiku 4\.5|Fable 5\b' rootnode-*/` after build, output read in full | Every remaining hit is either inside a historical sentence (names a prior cycle) or a legacy-graceful clause; the build report lists each hit with its classification — a count alone does not pass |
| T2 Calibration line parity | per-tier `grep -c` of the exact §3.1 string | 13 / 7 / 7, recomputed from the §4 tier column |
| T3 D9c on the five L+ Skills with new behavioral content (domain-software-engineering, domain-agentic-context, prompt-compilation, prompt-validation, handoff-trigger-check) | analytical, per SBD §3.9 D9c, 15-tendency taxonomy | Each new block names the tendency or refusal category it counters and the Anthropic guide it derives from |
| T4 Reasoning-block sweep | grep + read of `rootnode-reasoning-blocks/references/*.md` | Hit list produced; rewrites applied; 0 remaining "reproduce reasoning in response" instructions |
| T5 Description length | YAML-parsed length of every description | ≤ 1024 on all 27 (descriptions are untouched except cc-design and behavioral-tuning; the check is cheap and catches accidental edits) |
| T6 Package | `build_release_artifacts.py` self-assertion | 24 + 5 = 29 |

D9a (empirical with/without) is run only for cc-design (its spec §8) — the only Skill whose behavior, not its facts, changes. Running D9a on calibration-line edits would be measuring a sentence that does not change what the Skill does.

## 6. Pre-build gates and quality-gate notes (skill-builder applied at design time)

Gate 1 decomposition: every delta is Skill content (calibration, reference depth, routing-surface checks) — no hook, rule, or CLAUDE.md content is being created, except the repo-hygiene Cat 2 item, which is an audit check (Skill), not an enforcement (hook). Gate 2 warrant: the landscape change is the warrant; #15 carries its own (behavioral-tuning spec §2). Gate 3 ecosystem: no new Skill; no routing collision introduced (descriptions unchanged except the two spec'd Skills).

Quality-gate watch items for the build: D1 — `metadata.version` on all 27; D4 — the prompt-compilation and domain-software-engineering additions are routing surfaces in SKILL.md with the verbatim Anthropic blocks placed in references; D7 — the two new verbatim Anthropic blocks ("run a real check…", "Keep working until…") are *external-artifact verification* and *early-stop* countermeasures, not self-verification — they pass AEA §4.14 and must be tagged so the D7 scan does not flag them; D9 — sub-level recorded per Skill (D9c for 25, D9a for cc-design).

## 7. Open items carried into the CC prompt

- Operator's Claude Code version must be ≥ 2.1.293 before any test pass (Haiku 5.5 requirement; landscape §6). The prompt's pre-flight reports `claude --version` and halts below 2.1.293.
- `CLAUDE_CODE_DISABLE_WORKFLOWS` name on 2.1.30x — verify in the running version's docs; cc-delegation-patterns.md line 125 carries it.
- Opus 5.5 tokenizer — unstated; context-budget keeps the tolerance line.
- Empirical re-baselining of the deployment-conditioning tables remains a Calibration Lab item (carried from v4.0); this cycle's tables are D9c-analytical from Anthropic's guides and say so.
