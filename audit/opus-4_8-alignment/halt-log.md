# Opus 4.8 Alignment — Pass 1 Halt Log

Each row is a halt event with diagnosis. Line-local halts (ambiguous model references) are recorded without stopping the pass; methodology-change / validator-failure / engine-missing halts stop work.

| # | Trigger | Skill / file:line | Diagnosis | Disposition |
|---|---|---|---|---|
| 1 | AMBIGUOUS MODEL REFERENCE (§5) | `rootnode-context-budget/SKILL.md:95` | `\| API \| 1M tokens (GA for Opus 4.6, Sonnet 4.6) \| User-controlled (no platform RAG) \|`. Reading A (historical-GA fact): "1M became GA at the 4.6 generation; Opus 4.7 / 4.8 inherit the spec per F7." Reading B (stale calibration marker): "the Skill catalogs the 1M-context support set; 4.7 and 4.8 should be listed." Both are plausible. Line touches the catalog's published claim about which model surfaces support 1M context — operator should resolve before any second pass. | Left unchanged; continued with the rest of the Skill. |
| 2 | AMBIGUOUS MODEL REFERENCE (§5) | `rootnode-context-budget/SKILL.md:308` | `Context window: 1M tokens (Opus 4.6, Sonnet 4.6) — GA at standard per-token pricing.` Same ambiguity as halt #1, in the prose form. Reading A: lists the GA-origination generation. Reading B: lists current support set and is missing 4.7/4.8. | Left unchanged; continued with the rest of the Skill. |
