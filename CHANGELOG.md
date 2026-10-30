# Changelog

Append-only changelog for the rootnode-skills catalog. Per-Skill entries record sweep / RELAX / reframe / tier-set / validator status for each pass.

---

## Phase Opus 4.8 Alignment — Pass 1 (`phase-opus48-alignment-pass1`)

Voice-and-framing recalibration to Opus 4.8 per `prompts/root_skill_4_8_alignment_rubric.md`. Methodology preserved (D3).

- rootnode-session-handoff v2.0 — drop-in (no sweep/relax/reframe; already 4.8-calibrated) / tier-set broad-tier / validated
- rootnode-skill-builder v3.0 — swept 0 / relaxed 0 / reframed 0 (gate-dense methodology — no advisory step-sequences) / tier-marker unchanged (already abstracted "Opus-primary"; caveat-drop test-gated per §6) / validated (SKILL.md 433 lines)
- rootnode-identity-blocks v1.1 — swept 0 / relaxed 0 / reframed 0 (catalog content; decision-tree steps are selection gates) / tier-marker unchanged (already abstracted) / validated (SKILL.md 156 lines)
- rootnode-reasoning-blocks v1.1 — swept 0 / relaxed 0 / reframed 0 (catalog content; selection gates) / tier-marker unchanged (already abstracted) / validated (SKILL.md 178 lines)
- rootnode-output-blocks v1.1 — swept 0 / relaxed 0 / reframed 0 (catalog content; selection gates) / tier-marker unchanged (already abstracted) / validated (SKILL.md 130 lines)
- rootnode-block-selection v1.1.1 — swept 0 / relaxed 1 (Reasoning discipline self-critique scaffolding — lightened from imperative to reasoned voice; instruction preserved) / reframed 0 (Step 1-5 are selection gates) / tier-marker unchanged (already abstracted) / version bumped 1.1 → 1.1.1 / validated (SKILL.md 378 lines)
- rootnode-domain-software-engineering v1.1 — swept 0 / relaxed 0 (Behavioral countermeasures are meta-content for USER prompts, not Claude self-critique scaffolding) / reframed 0 (Step 1-5 are prompt-construction gates) / tier-marker unchanged (already abstracted) / validated (SKILL.md 154 lines)
- rootnode-domain-business-strategy v1.1 — swept 0 / relaxed 0 / reframed 0 (already outcome-led; "uses up to four layers" already graceful-degradation framing) / tier-marker unchanged / validated (SKILL.md 205 lines)
- rootnode-domain-content-communications v1.1 — swept 0 / relaxed 0 / reframed 0 / tier-marker unchanged / validated (SKILL.md 223 lines)
- rootnode-domain-research-analysis v1.1 — swept 0 / relaxed 0 / reframed 0 / tier-marker unchanged / validated (SKILL.md 224 lines)
- rootnode-domain-agentic-context v1.1 — swept 0 / relaxed 0 / reframed 0 (escalation ladder is graceful-degradation already; Step 1-3 are decision gates) / tier-marker unchanged / validated (SKILL.md 186 lines)
- rootnode-prompt-compilation v1.2.1 — swept 0 (Sonnet 4.6 / Haiku 4.5 are current floor refs; Opus-recommended caveat test-gated) / relaxed 0 / reframed 1 (4-stage workflow Parse→Select→Construct→Validate: added outcome-anchor before Stage 1 — within-stage gates kept imperative, parallels session-handoff §4 worked example) / tier-marker unchanged (Tier 3, Opus-primary, caveat-drop test-gated) / version bumped 1.2 → 1.2.1 / validated (SKILL.md 276 lines)
- rootnode-prompt-validation v1.1.1 — swept 0 / relaxed 1 (Reasoning discipline — voice lightened; evidence-first scoring gate preserved) / reframed 0 / tier-marker unchanged / version bumped 1.1 → 1.1.1 / validated (SKILL.md 262 lines)
- rootnode-anti-pattern-detection v1.1.1 — swept 0 / relaxed 1 (Reasoning discipline) / reframed 0 (7-pattern detection sequence is gates) / tier-marker unchanged / version bumped 1.1 → 1.1.1 / validated (SKILL.md 183 lines)
- rootnode-memory-optimization v1.2.1 — swept 0 / relaxed 1 (Reasoning discipline; user-confirmation gate preserved imperative) / reframed 1 (4-stage Project Comprehension→Audit→Prescription→Delivery: added outcome-anchor before Stage 1) / tier-marker unchanged / version bumped 1.2 → 1.2.1 / validated (SKILL.md 278 lines)
- rootnode-project-brief v1.0.1 — swept 0 / relaxed 0 (anti-fabrication is output-content discipline, not §3 self-referential RELAX target) / reframed 1 (5-step Generate Brief pipeline: added outcome-anchor) / tier-marker unchanged / version bumped 1.0 → 1.0.1 / validated (SKILL.md 191 lines)
- rootnode-handoff-trigger-check v1.1.2 — swept 0 / relaxed 0 / reframed 0 (mechanics-only workflow; Step 1-5 are evaluation gates) / no existing tier marker (preserved absence — adding one is content authoring beyond voice recalibration) / validated (SKILL.md 318 lines)
- rootnode-profile-builder v1.0.2 — swept 0 / relaxed 0 / reframed 0 (mechanics-only workflow; validate-before-write gate) / no existing tier marker (preserved absence) / validated (SKILL.md 170 lines)
- rootnode-project-audit v1.2.1 — swept 0 / relaxed 0 (evidence-first principle is hard gate, not RELAX target) / reframed 1 (Audit Workflow 5-step pipeline: added outcome-anchor) / tier-marker unchanged (Tier 3, Opus-primary; caveat-drop test-gated) / version bumped 1.2 → 1.2.1 / validated (SKILL.md 239 lines)
- rootnode-full-stack-audit v1.0.1 — swept 0 / relaxed 0 / reframed 1 (4-component pipeline outcome anchor strengthened) / tier-marker unchanged / version bumped 1.0 → 1.0.1 / validated (SKILL.md 188 lines)
- rootnode-global-audit v1.0.1 — swept 0 / relaxed 0 / reframed 1 (4-stage Global Audit Pipeline: added outcome anchor) / tier-marker unchanged / version bumped 1.0 → 1.0.1 / validated (SKILL.md 188 lines)
- rootnode-context-budget v5.0 — swept 0 / 2 ambiguous-reference halts logged (SKILL.md:95, :308 — "1M tokens GA for Opus 4.6, Sonnet 4.6"; historical-GA vs current-support-set ambiguity; left unchanged per §5) / relaxed 0 / reframed 0 (Mode 1 and Mode 2 are already outcome-led at the mode header level) / tier-marker unchanged / validated (SKILL.md 365 lines)
- rootnode-critic-gate v1.0.2 — swept 0 / relaxed 0 / reframed 0 (mechanics-only; Workflow Step 1-6 are evaluation gates) / no existing tier marker (preserved absence) / validated (SKILL.md 207 lines)
- rootnode-mode-router v1.0.2 — swept 0 / relaxed 0 / reframed 0 (mechanics-only; rule-evaluation gates) / no existing tier marker (preserved absence) / validated (SKILL.md 247 lines)
- rootnode-repo-hygiene v1.0 — swept 0 (all §4.X hits are doc-section refs, not model versions — false positives) / relaxed 0 / reframed 0 (Phase 1 / Phase 2 step sequences are enforcement-grade gates; "five principles" are the load-bearing constraints) / no existing tier marker (preserved absence) / validated (SKILL.md 230 lines)
- rootnode-cc-design v2.1 — swept 0 (§4.X are doc-section refs — false positives) / relaxed 0 / reframed 0 (Step 1-6 are workflow gates; source-discipline / 7-layer placement are hard gates; 5 modes already outcome-led) / no existing tier marker (preserved absence) / validated (SKILL.md 241 lines)
- rootnode-behavioral-tuning v2.0.1 — swept 3 (SKILL.md line 28 Skill-level calibration "Opus 4.7 calibration" → 4.8; SKILL.md line 412 Skill runtime context "Opus 4.7 Adaptive" → 4.8; references/countermeasure-templates.md line 5 document-level "Updated for Opus 4.7 calibration" → 4.8 with carry-forward annotation) / relaxed 1 (Reasoning discipline self-critique scaffolding) / reframed 0 (no advisory step-sequence; content-organized catalog of 10 tendencies) / preserved as historical: all "NEW in 4.7" / "Reduced in 4.7" / "Emerged in 4.7" tendency-emergence markers (factual generation-history), all per-template "(4.7-calibrated)" labels (empirical testing markers — bumping unverified), "Anthropic Opus 4.7 migration guide" citation (specific external doc), "pre-4.7" emphatic-language inflection markers (historical inflection point) / tier-marker unchanged / version bumped 2.0 → 2.0.1 / validated (SKILL.md 490 lines)

---

## Catalog v5.0 — 5.5-generation alignment (`release/v5.0`)

This PR will move all 27 Skills to 5.0.0 and recalibrate the catalog for the 5.5 generation (Fable 5.1, Opus 5.5, Sonnet 5.5, Haiku 5.5) per `design/root_DESIGN_catalog_v5_model_alignment.md`, `design/root_DESIGN_cc-design_v5.md`, `design/root_DESIGN_behavioral-tuning_v5.md`, and the dated landscape block `design/root_MODEL_LANDSCAPE_2026-10.md`. Tier structure unchanged (T1 13 / T2 7 / T3 7). Methodology preserved except where a spec row changes it.

- Calibration-only (L, 9) — this PR will replace the calibration line whole with the tier template and bump to 5.0.0: rootnode-block-selection (T2), rootnode-domain-business-strategy, rootnode-identity-blocks, rootnode-memory-optimization (T2), rootnode-mode-router, rootnode-output-blocks, rootnode-profile-builder, rootnode-project-brief, rootnode-session-handoff
- Calibration plus body edits (L+, 16) — this PR will apply each Skill's §4 row: rootnode-anti-pattern-detection, rootnode-context-budget (1M universal; tokenizer and cache-pricing notes), rootnode-critic-gate (`status: blocked`; advisor pairing), rootnode-domain-agentic-context (per-model fallback; harness rules), rootnode-domain-content-communications (Fable 5.1 formatting note), rootnode-domain-research-analysis (marked quotations; search nudge), rootnode-domain-software-engineering (5.5 cyber posture; external-verification block), rootnode-full-stack-audit, rootnode-global-audit, rootnode-project-audit (effort wording; 15-tendency Dimension 6), rootnode-handoff-trigger-check (condition 7 for the 5.5 generation), rootnode-prompt-compilation (reasoning-extraction check), rootnode-prompt-validation (two symptom-fix entries), rootnode-reasoning-blocks (reasoning-extraction sweep), rootnode-repo-hygiene (hook exit-code and shape check), rootnode-skill-builder (D9a graders; 15-tendency fix)
- Structural (S, 2) — this PR will ship rootnode-cc-design 5.0.0 (predecessor v4.2: hook reference fix, session-report standard with new `references/cc-session-reports.md` and `report_dir`, delegation hardening, early-stop countermeasure) and rootnode-behavioral-tuning 5.0.0 (tendency #15 early turn termination; routing surface repaired for 11–15; deployment-conditioning tables rebuilt; Anthropic countermeasure blocks carried verbatim)
- Catalog surfaces — this PR will update README Model Compatibility and the line-31 calibration note, add `release-notes/*-v5.0.md` and `release-notes/catalog-v5.0.md`, and add `audit/v5_0-alignment/` (sweep manifest, release-notes config, KF update blocks, session report). KF changes are surfaced in `audit/v5_0-alignment/kf-update-blocks.md`, not applied to `audit/canonical-kfs/`.

## Catalog v5.0.1 — patch after the v5.0 D9a (`release/v5.0.1`)

This PR will move 12 Skills to 5.0.1 per `design/root_DESIGN_catalog_v5.0.1_patch.md` (§3, §8 rev 2, §9 rev 3); the other 15 stay at 5.0.0. Calibration and tiers are unchanged (T1 13 / T2 7 / T3 7). Release shape: patch catalog release (playbook §1.6) — per-Skill releases for the 12, `--latest=false`, and a `catalog-v5.0.1` umbrella marked Latest with the full 29-zip bundle.

- rootnode-cc-design 5.0.1 — chain-scoped Stop-hook bounds (no-progress and chain-total caps, paired with Claude Code's continuation cap); migration-guard example hardened (`find -delete`, globs, `../migrations`, PowerShell) with a statement of what it cannot see; resume line in autonomous templates; shell lessons; cross-reference and count fixes (D9a A1/A2; F13–F15, F21, F22, F27–F29, F31; R1, R2, R4, R5; S1–S3)
- rootnode-critic-gate 5.0.1 — additive `status` / `blocked_reason` output fields; readiness-gate references renamed (F19, R3)
- rootnode-mode-router 5.0.1 — readiness-gate references renamed (R3)
- rootnode-handoff-trigger-check 5.0.1 — condition 7 heading; retired `handoff-gate` name removed from its own files (F17, R3)
- rootnode-context-budget 5.0.1 — one effort rule; price-band note limited to the landscape fact (F18, F20)
- rootnode-full-stack-audit, rootnode-global-audit, rootnode-project-audit, rootnode-prompt-compilation 5.0.1 — one effort rule (F18)
- rootnode-prompt-validation, rootnode-domain-agentic-context 5.0.1 — current-tier wording (F16)
- rootnode-domain-research-analysis 5.0.1 — examples pointer (F24)
- Catalog surfaces — canonical-KF mirrors CC_EG, AAP, SBD and AEA synced from staging; README badges, bundle name and sync caveat; release playbook §1.2 and §1.6; packager `CATALOG_VERSION`; `release-notes/*-v5.0.1.md` and `release-notes/catalog-v5.0.1.md`; `audit/v5_0_1-patch/` (build reports, review files, release-notes config)
