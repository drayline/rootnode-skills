# Project Audit Framework

The complete methodology for evaluating Claude Projects. This file contains the tools used during every audit: the Project Scorecard for structured scoring of Project-scoped layers, the Global Layer Scorecard for evaluating account-wide configuration, the Anti-Pattern Checklist for detecting known failure patterns, the Cross-Layer Alignment Check for diagnosing inter-layer conflicts, the Quality Criteria evaluation for holistic assessment, and the Diagnostic Question Bank for guided discovery when the user's Project materials are incomplete.

**Surface scope:** This framework applies CP-side (Claude Projects — the chat surface). For CC-side (Claude Code environment) audits, see `root_CC_ENVIRONMENT_GUIDE.md` for the methodology and `rootnode-repo-hygiene` for the operational sweep tool. The architectural principles that govern both surfaces are unified in `root_AGENT_ENVIRONMENT_ARCHITECTURE.md`.

**Calibration scope:** Audit findings are calibrated against **Opus 5 + Sonnet 5 dual-primary**, with Fable 5 integrated-aware, Opus 4.8 fallback-graceful (findings must remain sound on Opus 4.8 because classifier-flagged requests fall back there silently), Sonnet 4.6 legacy-graceful, and Haiku 4.5 graceful-with-extended-thinking. Haiku 4.5 without extended thinking and Haiku 3.5 are out of scope. Mythos 5 / Mythos Preview out of scope. The Behavioral Calibration dimension and Diagnostic Question Bank reference the 14-tendency taxonomy (14 numbered entries #1–#14, with 7 discrete facets — 1a/1b under #1, 3a/3b/3c under #3, 7a/7b under #7) plus two non-tendency prompt/environment-conditional defects documented in `root_OPTIMIZATION_REFERENCE.md` and `root_CLAUDE_OPTIMIZATION_NOTES.md`. See `root_CALIBRATION_SCOPE_DECISION.md` for the full scope authority and `root_SKILL_PORTABILITY_TIER_ASSIGNMENTS.md` for per-Skill tier assignments and Claude Code applicability classifications.

---

## The Project Scorecard

Score each dimension 1-5. The anchors describe what each score level looks like. A Project's composite score is the average across all six dimensions, but the individual dimension scores matter more than the average — a Project scoring 5/5 on five dimensions and 1/5 on one dimension has a critical weakness that the average obscures.

### Dimension 1: Identity Precision

Does the system prompt establish a clear, appropriately-scoped identity that produces distinctive expert output?

| Score | Description |
|-------|-------------|
| 1 | No identity set, or identity is generic ("You are a helpful assistant"). Claude operates as base Claude with no domain calibration. Output will be competent but undifferentiated — no consistent expertise, tone, or analytical perspective across conversations. |
| 2 | Identity names a domain but lacks specificity ("You are a marketing expert"). Claude has a general direction but no expertise depth, seniority level, or analytical disposition. Output will reference the domain but lack the depth of a genuine specialist. |
| 3 | Identity specifies a role with some expertise markers ("You are a senior product manager with experience in B2B SaaS"). Sufficient to produce domain-appropriate output, but missing the reasoning style, priority hierarchy, or behavioral calibration that would make the identity distinctive. |
| 4 | Identity specifies role, seniority, domain expertise, and analytical disposition ("You are a senior product strategist who evaluates opportunities through the lens of market timing, competitive dynamics, and engineering feasibility. You prioritize evidence over intuition and say when the data is insufficient."). Produces consistently expert output with a clear perspective. |
| 5 | All elements of 4, plus the identity is calibrated to the Project's full scope — broad enough for all operational modes, specific enough for distinctive output. Includes one behavioral sentence that addresses the most likely failure mode for this domain. The identity would pass the blind test: reading the output alone, you could reconstruct what role Claude was playing. |

### Dimension 2: Instruction Clarity

Are the behavioral rules clear, non-contradictory, and appropriately scoped?

| Score | Description |
|-------|-------------|
| 1 | No explicit behavioral rules, or rules are vague platitudes ("Be helpful and thorough"). Claude falls back on defaults for every behavioral decision. |
| 2 | Some rules present but they are generic ("Be concise", "Be accurate") and not targeted to the Project's domain or task types. Rules that could apply to any Project do not improve this specific Project. |
| 3 | Rules are relevant to the Project's domain and task types, but some conflict with each other or with instructions in knowledge files. Or rules are present but stated as conversational suggestions rather than directives. |
| 4 | Rules are clear, non-contradictory, domain-relevant, and stated as directives. Each rule addresses a specific behavioral need rather than restating generic best practices. The rule set is lean — no "just in case" instructions diluting the important ones. |
| 5 | All elements of 4, plus rules are ordered by importance with critical constraints at the top of the system prompt. Rules use the principle/default distinction: hard rules are stated as rules, preferences are stated as defaults with flexibility. The rule set has been audited for noise — every rule demonstrably improves output. |

### Dimension 3: Knowledge & Context Architecture

Are knowledge files and Memory well-structured, appropriately scoped, and effectively routed? Does the total knowledge file load fit within context budget constraints? Does the Project use both context layers — searchable knowledge files and always-loaded Memory — according to their strengths?

| Score | Description |
|-------|-------------|
| 1 | No knowledge files, or files exist but are not referenced in Custom Instructions (orphan files). No Memory configured. Claude has no persistent reference material, no orientation context, and no routing signal to consult anything. |
| 2 | Knowledge files exist and are referenced in Custom Instructions, but references are inventory-style ("This project contains company_info.md") rather than routing-style ("Consult company_info.md when the user asks about our product, market, or competitive position"). Memory is either absent or contains only auto-populated content with no manual edits. Claude may not consult the right file at the right time and starts each conversation without orientation context. |
| 3 | Files are referenced with routing guidance, but the file architecture has structural issues: content overlap between files, files serving multiple purposes (violating one-purpose principle), or files that are significantly over/under-sized. Or: the Project is in RAG mode without the architecture accounting for it — no tiering awareness, no distinction between files that must be in-context versus files that can tolerate retrieval. Memory may be configured but contains misplaced content — reference-depth material that belongs in knowledge files, or stale orientation facts that no longer reflect the project's current state. The two context layers are not working as complements. |
| 4 | Each file has a single clear purpose, no content overlap, descriptive naming, and decision-oriented routing in Custom Instructions. File sizes are appropriate — neither too large (multiple topics) nor too small (should be a section in another file). The total knowledge file load is within the target budget for the Project's intended operating tier, or if it exceeds the budget, the Project's architecture accounts for RAG mode (files are tiered, behavioral content is in Custom Instructions rather than knowledge files, retrieval-friendly practices like clear naming and explicit document targeting are in place). For Projects with 3+ knowledge files: Memory is configured with current orientation facts (project phase, key constraints, user context) that complement rather than duplicate the knowledge files. The instruction/reference separation is clean. |
| 5 | All elements of 4, plus the file architecture is evolvable — a new file can be added without restructuring existing files. Memory and knowledge files follow the complementary layer principle: Memory holds always-loaded orientation, knowledge files hold searchable depth, and neither duplicates the other. Memory is reviewed at project transitions and contains no stale facts. Files front-load their most important content. The Project's context budget is actively managed and the context architecture matches the project's workload. For projects targeting full-context mode: knowledge files stay well below the model's context window with clear headroom (under the current landscape — 1M-window primary models — most Projects have substantial headroom), and cross-file reasoning works reliably. For projects operating in retrieval mode: the architecture is designed for retrieval quality — files are single-topic and self-contained, behavioral content lives entirely in Custom Instructions, Memory, and Skills, routing descriptions accurately distinguish files, the retrieval pool is free of noise files, and large files have coherent section boundaries. In either mode: the context architecture would serve as a good pattern for others to replicate. See `root_OPTIMIZATION_REFERENCE.md` (Context Budget Principles) for the current automatic-by-window RAG behavior and the historical ~66,500 token measurement from the 200K era. |

**Context budget and scoring interaction.** A Project can have well-structured, well-routed files (score 4–5 on structural quality) but still face context budget problems if the total load is excessive relative to the model's context window. When evaluating this dimension, assess both structural quality and budget health. A Project in RAG mode without architectural awareness of its retrieval status — behavioral rules in knowledge files that may not be retrieved, no tiering distinction, no retrieval-friendly practices — should not score above 3 on this dimension regardless of how well individual files are structured. Budget awareness is a necessary condition for scores of 4 and 5. Note that under current 1M-window primary models, some Projects that were in retrieval mode under 200K-era plans may already be operating in full-context mode without content changes — verify current mode by checking for `project_knowledge_search` presence before scoring.

### Dimension 4: Mode Design

Are operational modes well-defined, genuinely distinct, and appropriate for the Project's task types?

| Score | Description |
|-------|-------------|
| 1 | No operational modes defined. All task types receive the same treatment regardless of whether they need different reasoning approaches, output structures, or behavioral rules. |
| 2 | Modes are defined but they are cosmetic — different labels for essentially the same behavior. The modes do not specify different reasoning approaches, output structures, or quality criteria. Claude would produce similar output regardless of which mode applied. |
| 3 | Modes are genuinely distinct (different behaviors for different task types), but some modes are missing key elements: no output structure specified, or reasoning approach is vague, or trigger conditions are ambiguous so Claude may not select the right mode. |
| 4 | Each mode has clear trigger conditions, a distinct reasoning approach, a specific output structure, and behavioral rules calibrated to the task type. Modes pass the differentiation test: the same input would produce noticeably different output depending on which mode was active. |
| 5 | All elements of 4, plus modes cover the Project's full scope without gaps or unnecessary overlap. Mode boundaries are clean — there are no ambiguous tasks that could fall into multiple modes without clear resolution. If modes are not needed (the Project handles one task type), the absence of modes is deliberate and the single behavioral pattern is well-specified. |

### Dimension 5: Output Standards

Are output quality criteria and format defaults specified clearly and placed effectively?

| Score | Description |
|-------|-------------|
| 1 | No output standards. Claude uses its defaults for length, format, tone, and structure. Output quality and format will be inconsistent across conversations. |
| 2 | Basic output guidance present ("Keep responses concise", "Use a professional tone") but no structural specifics — no length targets, no format defaults, no per-mode output specifications. |
| 3 | Output standards specify format and length defaults, but are not positioned for maximum attention (not near the bottom of the system prompt) or are contradicted by instructions elsewhere. Or standards are present but do not vary by mode when they should. |
| 4 | Output standards are specific (format defaults, length guidance, tone calibration), positioned at the bottom of the system prompt following the primacy-recency principle, and consistent with all other instructions. Standards vary by mode where appropriate. |
| 5 | All elements of 4, plus output standards include a pre-response verification check ("Before responding, verify..."), exclusion rules ("Do not include unrequested sections"), and edge case handling. Standards are calibrated to the Project's audience and domain, not generic quality instructions. |

### Dimension 6: Behavioral Calibration

Are Claude-specific behavioral countermeasures present for the failure modes this Project's domain and deployment context are likely to trigger? Does the Project account for the 14-tendency taxonomy including the four Opus-5-new tendencies (#11 over-verification, #12 scope expansion, #13 subagent over-delegation, #14 correction narration) and the two prompt/environment-conditional defects (conservative-instruction literalism, thinking-disabled artifacts)?

| Score | Description |
|-------|-------------|
| 1 | No behavioral countermeasures. The Project relies entirely on Claude's defaults. Any domain-relevant tendencies (agreeableness including persistent-preference dilution; hedging; the verbosity three-surface family — conversational, agentic narration, written deliverables; list overuse; fabricated precision on external facts; over-exploration; tool trigger miscalibration including under-triggering; LaTeX defaulting; editorial drift; self-referential fabrication; over-verification on Opus 5; scope expansion on Opus 5; subagent over-delegation on Opus 5; correction narration on Opus 5) will go unaddressed. Prompt/environment-conditional defects (conservative-instruction literalism, thinking-disabled output artifacts) also go undetected. |
| 2 | Generic countermeasures present but not targeted ("Be concise. Be direct. Challenge assumptions."). These are reasonable but do not address the specific failure modes this Project's domain or deployment context triggers. Or: countermeasures present but calibrated for pre-Opus-5 models (emphatic language for tendencies that Opus 5's calibration improvements have already reduced; verification-instruction accumulation from 4.7/4.8 era prompts that now causes over-verification). Or: countermeasures for the four Opus-5-new tendencies are absent even on Claude Code / API agent deployments where they surface strongly. |
| 3 | One or two targeted countermeasures present for the most likely failure mode, but other relevant tendencies are unaddressed. Or countermeasures are present but vaguely worded, reducing their effectiveness. Or: countermeasures address content tendencies (#1a, #5) without addressing process tendencies (#10 self-referential fabrication, #11 over-verification) in a Project where the deployment context exposes both. Or: the audit prompt uses conservative-review-instruction phrasing ("only report high-severity issues," "be conservative") which causes Opus 5 to follow literally and under-report. |
| 4 | Targeted countermeasures for all domain-relevant failure modes, each with specific language. No generic countermeasures for tendencies this domain or deployment does not trigger. Countermeasures are placed at high-attention positions (identity block or output standards). For chat-interface deployments: countermeasures address the chat-interface-specific tendencies (#1b, #7b, #9, #10, #14) where relevant. For Claude Code / API agent deployments: countermeasures address the four Opus-5-new tendencies (#11 removal of self-directed re-check instructions; #12 explicit scope constraint; #13 subagent-delegation caps; #14 correction narration limits). Audit and review prompts use report-everything-then-filter form rather than conservative-review literalism. |
| 5 | All elements of 4, plus countermeasures reinforce rather than contradict the identity and output blocks. The countermeasure set has been calibrated to both the Project's specific domain AND its deployment context — a targeted selection, not a generic full-list. The Project does not carry obsolete countermeasures for tendencies that Opus 5's calibration improvements have reduced (#1a output-content agreeableness, #2 hedging on factual claims, #3a conversational verbosity, #5 external-fact fabrication, #6 over-exploration on focused tasks, #7a tool over-triggering) unless the failure mode is empirically observed. The Project does not accumulate self-directed verification instructions (tendency #11 — remove double-check / re-verify / verification step / subagent-to-verify phrasing) while preserving external-artifact verification (evidence grounding against sources, files, tests, rendered pages) in imperative voice. For thinking-disabled integrations: no "do not think" instructions in the system prompt (that phrasing increases `<thinking>` tag leakage rather than suppressing it). |

---

## The Global Layer Scorecard

Six dimensions for evaluating the account-wide layers (Layers 1-5 in the Nine-Layer Architecture Model). Used during Global Audit and Full Stack Audit modes. Score each dimension 1-5 using the same anchoring methodology as the Project Scorecard. The Global Layer Scorecard evaluates configuration that affects every conversation — inside and outside Projects.

### Dimension 1: Preference Precision

Is the User Preferences text well-crafted — concise, universally applicable, and free of domain-specific content?

| Score | Description |
|-------|-------------|
| 1 | Empty, generic filler, or actively harmful instructions that degrade output in many contexts. |
| 2 | Heavily domain-specific. Multiple instructions that only apply to certain types of work. Preferences function as a second system prompt for one domain rather than a universal foundation. |
| 3 | Mix of universal and domain-specific content. Some instructions would be better placed in Project CI. Organization is adequate but not optimized. |
| 4 | Mostly universal with minor domain-specific leakage. Clear and well-organized. Instructions improve output across the majority of conversations. |
| 5 | Concise, universally applicable rules that improve every conversation. No domain-specific content — anything project-specific lives in the relevant Project CI. No redundancy with typical Project instructions. The Preferences serve as a strong behavioral foundation that Projects build on without repeating. |

### Dimension 2: Style Coherence

Do Styles work with, not against, other layers?

| Score | Description |
|-------|-------------|
| 1 | Active Style contradicts core User Preferences or breaks structured output in Projects. |
| 2 | Style conflicts with one or more Project CI output specifications. The Style override is causing unintended formatting in certain Projects. |
| 3 | Some Style settings duplicate or conflict with User Preferences. No active Project-level conflicts. |
| 4 | Minor Style/Preference overlap. No active conflicts with any Projects. Custom Styles, if present, are well-defined for their intended contexts. |
| 5 | Styles complement User Preferences without conflict. No Style conflicts with any Project CI output standards. Custom Styles are clearly scoped (if present). Users who don't use custom Styles score 5 by default if there are no conflicts with the default or selected Style. |

### Dimension 3: Memory Hygiene

Is Global Memory well-maintained, current, and properly delineated from deliberate layers?

| Score | Description |
|-------|-------------|
| 1 | Unconfigured/neglected, or stuffed with reference-depth content that wastes always-loaded context. |
| 2 | Significant staleness or depth misplacement. Memory and Preferences contain conflicting information. Memory has not been reviewed since initial auto-population. |
| 3 | Some stale entries. Some content that should be in User Preferences or Project CI instead. No active contradictions but delineation is unclear. |
| 4 | Mostly clean. Minor overlap with Preferences. No stale content. Memory provides useful context that supplements deliberate layers. |
| 5 | Memory contains stable, accurate context. No overlap with User Preferences. No reference-depth content. Regularly reviewed. Memory and Preferences serve clearly complementary roles — Memory provides learned context, Preferences provide deliberate rules. |

### Dimension 4: Skill Portfolio Fitness

Are installed Skills relevant, non-conflicting, and well-curated?

| Score | Description |
|-------|-------------|
| 1 | No awareness of Skill portfolio, or severe conflicts causing unpredictable behavior across Projects. |
| 2 | Multiple Skill/Project conflicts. Several unused Skills consuming discovery context. Skills were installed without evaluating interaction with existing Projects. |
| 3 | Some Skills installed speculatively that are never triggered. One or more overlaps with Project knowledge file content. Skill portfolio has not been reviewed since installation. |
| 4 | Mostly well-curated. Minor overlap with one Project's knowledge files. Each Skill serves a clear purpose and triggers appropriately. |
| 5 | Every installed Skill serves a clear purpose. No Skill/Project overlaps that cause behavioral conflicts. Skills complement Project architectures — Projects that benefit from installed Skills reference or account for them. Skills that are never triggered have been removed. |

### Dimension 5: Connector Alignment

Are MCP Connectors configured to match the user's Project needs?

| Score | Description |
|-------|-------------|
| 1 | No connectors configured despite Projects that would benefit, or extensive connector bloat consuming context without purpose. |
| 2 | Multiple Projects assume capabilities that aren't configured. Significant orphan connectors wasting context budget. |
| 3 | Some connector/instruction gaps — a Project references external tools without the connector. A few orphan connectors that could be removed. |
| 4 | Minor gaps — one Project references a tool without the connector. No orphan connectors. Loading mode (deferred vs. always-loaded) is appropriate. |
| 5 | Every Project that references external tools has the corresponding connectors configured. No orphan connectors consuming context without being used. Loading mode is optimized for the user's usage pattern. |

### Dimension 6: Cross-Layer Efficiency

Is context budget used efficiently across all nine layers, with no redundancy or undetected conflicts?

| Score | Description |
|-------|-------------|
| 1 | Layers actively fight each other. Heavy context waste from duplication. Multiple undetected cross-layer failures. |
| 2 | Significant redundancy or several undetected conflicts between layers. No awareness of cross-layer interactions. |
| 3 | Moderate redundancy. One or two silent overrides that the user may not be aware of. Some awareness of layer interactions but no systematic management. |
| 4 | Minor redundancies (one or two instructions duplicated across layers). No active conflicts. The user has some awareness of how layers interact. |
| 5 | No redundant layering. No silent overrides. Global layers provide a strong foundation that Projects build on without repetition. Context budget is well-managed across all layers. The user understands the precedence chain and has designed their layer configuration deliberately. |

---

## Anti-Pattern Checklist

The seven patterns below are the CP-side surface application of the unified anti-pattern catalog in `root_AGENT_ANTI_PATTERNS.md`. They are the operational checklist used during live Project audits — the unified catalog is the broader reference covering both CP and CC surfaces with surface-tagged patterns and cross-surface mappings. Consult the unified catalog when:
- The audit needs to evaluate a deployment that spans both surfaces (e.g., a CP design Project paired with a CC delivery repository).
- A surfaced pattern needs cross-surface context (e.g., this CP Monolith's CC analog is the CLAUDE.md Bloat pattern documented in `root_CC_ENVIRONMENT_GUIDE.md §2.4` — both manifest the surface-invariant Monolithic standing context principle at `root_AGENT_ANTI_PATTERNS.md §2.1`).
- Behavioral anti-patterns need to be checked alongside structural ones (the unified catalog references `root_OPTIMIZATION_REFERENCE.md` for the 14-tendency behavioral taxonomy plus the two non-tendency prompt/environment-conditional defects).

Check for each pattern during every audit. For each pattern detected, cite the specific evidence — do not assert a pattern without quoting the component that exhibits it.

### 1. The Monolith

**Detection criteria:** Custom Instructions exceed ~1500 words AND contain reference material (examples, frameworks, data tables, extended explanations) mixed with behavioral instructions. Or: a single knowledge file contains content serving multiple distinct purposes.

**Symptoms:** Inconsistent adherence to behavioral rules. Claude treats some instructions as optional. Output quality varies unpredictably.

**Evidence to cite:** Quote the specific reference material embedded in Custom Instructions, or identify the multiple purposes served by a single knowledge file.

### 2. The Orphan File

**Detection criteria:** A knowledge file exists in the Project but is not referenced by name in Custom Instructions, or is referenced with only an inventory description ("This project contains X.md") rather than routing guidance.

**Symptoms:** Claude rarely or never draws from the file's content. The file's information is absent from output even when directly relevant.

**Evidence to cite:** Name the unreferenced or weakly referenced file. Quote the Custom Instructions to show the absence or inadequacy of the routing description.

### 3. The Echo Chamber

**Detection criteria:** The same instruction, principle, or rule appears in multiple locations (Custom Instructions + knowledge file, or multiple knowledge files) with different wording. Look for: instructions that say the same thing using different language, or behavioral rules restated with subtle variations.

**Symptoms:** Inconsistent Claude behavior — following one version in some conversations and another version in others. Or: Claude synthesizes the variations into a compromise that matches none of the intended versions.

**Evidence to cite:** Quote each instance of the duplicated instruction, highlighting the wording differences.

### 4. The Phantom Conversation

**Detection criteria:** Custom Instructions are written in conversational style — addressing Claude as "you" in a chatty way, using phrases like "Hi Claude, in this project you'll be helping with..." or "When someone asks you about X, you might want to think about..."

**Symptoms:** Claude treats instructions as suggestions rather than directives. Behavioral rules are followed inconsistently because the conversational framing reduces their perceived authority.

**Evidence to cite:** Quote the conversational phrasing and contrast it with declarative alternatives.

### 5. The Kitchen Sink

**Detection criteria:** Custom Instructions contain instructions for edge cases, rare scenarios, or "just in case" situations that dilute attention to the core behavioral rules. Indicators: the system prompt addresses more than 8-10 distinct behavioral instructions, or includes conditional logic for scenarios that arise less than 10% of the time.

**Symptoms:** Core behavioral rules are followed less reliably because they compete for attention with low-priority instructions. Output quality is mediocre across all scenarios rather than excellent for common scenarios.

**Evidence to cite:** Identify the low-priority instructions and estimate their relevance frequency. Quote the core rules that are at risk of attention dilution.

### 6. The Misaligned Hierarchy

**Detection criteria:** Behavioral instructions exist in knowledge files rather than (or in addition to) Custom Instructions, without explicit delegation from the system prompt. Or: the system prompt is brief and high-level while a knowledge file contains the actual behavioral rules.

**Symptoms:** Unpredictable adherence to behavioral rules. Claude may treat knowledge-file instructions as context rather than directives. Rules in knowledge files may be followed in some conversations and ignored in others.

**Evidence to cite:** Quote the behavioral instructions found in knowledge files. Show whether the system prompt delegates authority to those files.

### 7. The Blurred Layers

**Detection criteria:** Memory contains reference-depth content that belongs in knowledge files (detailed explanations, procedural steps, decision rationale, historical context). Or: knowledge files contain always-relevant orientation facts that should be in Memory (current project phase, active constraints, key decisions the user expects Claude to know immediately). Or: the same facts appear in both Memory and knowledge files without a clear authoritative home, creating a coherence risk if one is updated and the other is not.

**Symptoms:** Wasted always-loaded context on material Claude only needs occasionally (Memory overloaded with reference content). Or: Claude starts conversations without key orientation context that would improve first-message relevance (orientation facts buried in knowledge files instead of Memory). Or: Claude cites contradictory versions of the same fact from different layers (duplication across layers with drift).

**Evidence to cite:** Quote the specific Memory edits that contain reference-depth content, or identify the orientation-level facts in knowledge files that would be better served by Memory. For duplication, quote both the Memory edit and the knowledge file passage, highlighting any discrepancies.

---

## Cross-Layer Alignment Check

A structured sweep of cross-layer failure modes from the Nine-Layer Architecture Model (see OPTIMIZATION_REFERENCE.md for the full failure mode catalog). Run during Global Audit and Full Stack Audit. Each check specifies the layers involved, the detection method, and the severity classification.

For each failure mode detected, produce a finding with: symptom (what the user experiences), cause (which layers conflict and how), fix (specific changes to resolve the conflict), and expected impact (what improves after the fix).

### Severity Classification

**Critical** — causes wrong or unpredictable output. Claude's behavior contradicts the user's explicit intent. Includes: Skill/Project Collision producing inconsistent behavior, Silent Override causing unexpected departures from preferences, Connector/Instruction Mismatch causing hallucinated tool access.

**Major** — wastes significant context or creates fragile behavior. Includes: Redundant Layering consuming double context, Cross-Project Duplication wasting tokens across every Project, Memory/Preference Confusion creating fragile behavior dependent on synthesis cycles.

**Minor** — missed optimization opportunity. Includes: Style/CI Tension in Projects where the format conflict is cosmetic, Context Waste from Global Layers that is measurable but not yet impacting conversation quality.

### Check Sequence

1. **Redundant Layering** (Layers 1 + 6): Compare User Preferences text against each Project CI for semantic overlap in behavioral instructions. Flag instructions that appear in both. Severity: Major.

2. **Silent Override** (Layers 1 + 6): Compare behavioral instructions in User Preferences against Project CI for direct contradictions. Flag cases where the Project CI implicitly overrides a Preference without acknowledgment. Severity: Critical.

3. **Skill/Project Collision** (Layers 4 + 6/7): Compare installed Skill descriptions and trigger conditions against Project knowledge file purposes and CI behavioral rules. Flag overlapping procedural content or contradictory behavioral guidance. Severity: Critical.

4. **Connector/Instruction Mismatch** (Layers 5 + 6): Scan Project CI for references to external tools, data sources, or integrations. Cross-reference against configured MCP connectors. Flag assumed capabilities without corresponding connectors. Severity: Critical.

5. **Memory/Preference Confusion** (Layers 3/8 + 1): Scan Global and Project Memory for behavioral patterns that have stabilized across multiple synthesis cycles. Flag patterns that should be codified as explicit Preferences or CI rules. Severity: Major.

6. **Style/CI Tension** (Layers 2 + 6): Compare active Style instructions against Project CI output standards. Flag format/tone conflicts where the Style override would break structured output requirements. Severity: varies (Critical if it breaks structured output; Minor if cosmetic).

7. **Cross-Project Duplication** (Layer 6 across Projects): Compare behavioral rules across the user's Project portfolio. Flag instructions that appear in 3+ Projects and pass the Universality Test (would improve output in every context). These are promotion candidates for User Preferences. Severity: Major.

8. **Context Waste from Global Layers** (Layers 1-5 combined): Estimate total context consumed by global layers. Flag when User Preferences are overdetailed, when Skills are installed but never triggered, or when MCP connector overhead is excessive relative to usage. Severity: Minor.

### Information Requirements

The Cross-Layer Alignment Check requires visibility into multiple layers. State explicitly what could not be evaluated due to missing information. Checks 1-2 require User Preferences + at least one Project CI. Check 3 requires the installed Skills list. Check 4 requires the configured connectors list. Check 5 requires Memory contents. Check 6 requires active Style information. Check 7 requires CI from 3+ Projects. Check 8 requires a rough inventory of all global layer components.

---

## Quality Criteria Evaluation

Evaluate against each criterion after completing the Scorecard and Anti-Pattern checks. These are holistic criteria that assess the Project as a system, not individual components.

### Comprehensibility

**Test:** Read only the Custom Instructions. Can you construct a complete mental model of the Project — its purpose, scope, how to use it, what files exist, and when to consult them?

**Pass indicators:** Purpose is stated in the first 2-3 sentences. Every knowledge file is named with routing guidance. Operational modes are described with trigger conditions. A new user could use this Project effectively after reading only the system prompt.

**Fail indicators:** Purpose is implicit or buried. Knowledge files are listed without usage guidance. Modes are described without trigger conditions. Understanding the Project requires reading the knowledge files, not just the system prompt.

### Coherence

**Test:** Check for content overlap between files, conflicting instructions between Custom Instructions and knowledge files, and inconsistent terminology. Also check that Memory edits do not contradict knowledge file content or Custom Instructions.

**Pass indicators:** Each concept has one authoritative location. Terminology is consistent across all components. No instruction in one place contradicts an instruction in another. Memory edits and knowledge files present consistent facts.

**Fail indicators:** The same concept is explained differently in two files. Custom Instructions say "be concise" while an output block specifies 1500 words. The system prompt uses "operational modes" while a knowledge file calls them "task profiles." A Memory edit states a fact that contradicts information in a knowledge file.

### Efficiency

**Test:** For every instruction in Custom Instructions, ask: "If I removed this, would the output get noticeably worse?" For every knowledge file, ask: "Is this file consulted often enough to justify its presence?" For Memory, ask: "Does every edit contain orientation-level facts that are relevant to most conversations?" For the context budget, ask: "Is the total knowledge file load justified by the value each file provides, or are files consuming budget without proportional return?"

**Pass indicators:** Every instruction demonstrably improves output. Every file serves a purpose that arises in a significant fraction of conversations. Memory contains only current, orientation-level facts. The system prompt is not bloated — it contains behavioral rules and routing, not reference material. The knowledge file load fits within the target budget for the Project's intended operating tier.

**Fail indicators:** Instructions that were added "just in case." Knowledge files for rare edge cases. Reference material embedded in Custom Instructions. Memory stuffed with reference-depth content or stale facts. The system prompt could be 30%+ shorter without degrading output. The Project is in RAG mode without awareness, or knowledge files well exceed the budget without justification.

### Evolvability

**Test:** Imagine adding a knowledge file for a topic adjacent to the Project's domain. Would it slot in cleanly (add the file, add a routing entry), or would it require restructuring?

**Pass indicators:** Adding a file requires adding one routing entry to Custom Instructions. No existing files need modification. Architectural decisions are documented or self-evident.

**Fail indicators:** Adding a file requires changing how existing components work. Components are tightly coupled — changing one requires changing others. There is no documentation of why the Project is structured the way it is.

### Instruction/Reference Separation

**Test:** Are all behavioral instructions in Custom Instructions and all reference material in knowledge files? Or are they mixed? Is always-loaded orientation in Memory and searchable depth in knowledge files? Or are the layers blurred?

**Pass indicators:** Custom Instructions contain only: identity, behavioral rules, knowledge file routing, operational modes, and output standards. Knowledge files contain only: reference material, frameworks, data, templates, and examples. Memory contains only: current orientation facts relevant to most conversations. Each layer serves its designated function.

**Fail indicators:** Custom Instructions contain data tables, extended examples, or framework descriptions. Knowledge files contain "always do X" behavioral instructions that should be in the system prompt. Memory contains detailed procedural content or historical rationale that belongs in knowledge files. The same fact is maintained in multiple layers without a clear authoritative home.

---

## Diagnostic Question Bank

Use these questions when the user's submission is incomplete — they have pasted Custom Instructions but not described their knowledge files, or they have described symptoms but not provided the Project materials.

### Architecture Discovery

- How many knowledge files does this Project have, and what does each one contain?
- What are the main task types users perform in this Project?
- Who uses this Project — what is their expertise level?
- What output formats does the Project produce?
- What is the Project's scope — what is explicitly outside it?

### Memory Discovery

- Has the Project's Memory been configured with manual edits, or is it using only auto-populated memories?
- What orientation facts does Claude need in every conversation — current project phase, key constraints, user role, active decisions?
- Is there a build_context.md or similar institutional memory file in the Project's knowledge files?
- Has the Memory been reviewed since the Project's last significant change?

### Context Budget Discovery

- What is the optimization objective — full-context restoration, or maximizing retrieval quality within the current mode? (If uncertain, the mode-aware assessment in the Context Budget Analysis will determine feasibility and recommend the appropriate strategy.)
- How many knowledge files does the Project have, and what types are they? (Include all uploaded file types — .md, .pdf, .docx, .xlsx, .csv, .txt, images — as well as GitHub-connected repositories. All count toward the knowledge file budget.)
- Has the user noticed `project_knowledge_search` appearing in Claude's responses, or a retrieval-augmented generation indicator in the Project UI?
- Does the Project depend on Claude reasoning across multiple files simultaneously, or does it primarily handle queries against individual documents?
- Has the Project experienced symptoms of retrieval mode without awareness — Claude forgetting instructions it used to follow, giving generic answers despite detailed context files, or inconsistent behavior across conversations?
- Which knowledge files contain frequent cross-references to other knowledge files? (High cross-file dependency files are most vulnerable to quality loss under retrieval mode.)
- How many MCP connectors, Skills, and platform features are connected to the Project? (These are threshold-exempt — they cannot trigger RAG mode — but they reduce conversation runway, shortening productive session length.)
- Has the user added files incrementally over time without evaluating cumulative budget impact?

### Global Layer Discovery

Use these questions when running a Global Audit or Full Stack Audit, or when the user reports cross-project inconsistencies.

- Can you share your User Preferences text? (Required for Global Audit. This is the foundation all other layers build on.)
- Are you using a custom Style, or one of Claude's presets? If custom, what communication rules does it specify? (Needed for Style/CI conflict detection.)
- How many Projects do you actively use? Can you share the Custom Instructions from 2-3 of them? (Enables Cross-Project Pattern Analysis and promotion/demotion detection. Three or more Projects required for meaningful evolutionary recommendations.)
- What Skills do you have installed? (List is visible in the Skills menu. Needed for Skill/Project collision detection.)
- What MCP connectors are configured, and are they set to "load as needed" or always active? (Needed for connector alignment and overhead estimation.)
- Have you reviewed your Global Memory recently? Does it contain facts that are no longer accurate or preferences you've since changed? (Needed for Memory hygiene assessment.)
- Do you notice Claude behaving differently across Projects in ways you didn't intend? (Symptom of cross-layer conflicts — Silent Override, Skill/Project Collision, or Style/CI Tension.)

### Symptom Discovery

- What specific output problem are you seeing? (Generic output, wrong format, shallow analysis, inconsistent quality, wrong tone, excessive length, etc.)
- Is the problem consistent or intermittent across conversations?
- Does the problem affect all task types or only specific ones?
- When did the problem start — was the Project working better before?
- Can you provide an example of a conversation where the output was not what you expected?

### Context Discovery

- What domain does this Project operate in?
- How often is the Project used — daily, weekly, occasionally?
- Has the Project been modified since initial setup?
- What is the Project's primary deployment context — chat interface (claude.ai), Claude Projects with extensive use, Claude Code, or API integration? (Behavioral countermeasure relevance varies by deployment context — chat-interface deployments are most exposed to tendencies #1b, #7b, #9, and #10.)
- Are there any specific Claude behavioral tendencies you have noticed? (Agreeableness bias on output content or persistent-preference dilution over long conversations; hedging; verbosity — conversational response length, agentic progress narration, or written-deliverable length; list overuse; fabricated precision on external facts; over-exploration; tool over-triggering; tool under-triggering; LaTeX defaulting; editorial drift / unsolicited boundary commentary; self-referential fabrication / claims about actions not actually performed; over-verification / prompt or Skill instructions telling the model to double-check its own output that now compound with Opus 5's automatic self-verification; scope expansion / delivering beyond what was asked; subagent over-delegation on Claude Code; correction narration for corrections that don't materially change the outcome)
- Prompt/environment-conditional defects surfaced in the Project's audit or review Skills: "only report high-severity" or "be conservative" phrasing that causes Opus 5 to under-report; thinking-disabled configurations where tool calls leak as text or internal XML tags appear in visible output.
