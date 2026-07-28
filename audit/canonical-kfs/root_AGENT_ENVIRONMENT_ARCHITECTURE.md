# root_AGENT_ENVIRONMENT_ARCHITECTURE.md

The shared principle layer for designing AI agent environments. Establishes the architectural concepts that govern both Claude Projects (chat surface) and Claude Code (autonomous execution surface), the relationship between the two surfaces, and the surface-invariant principles that apply to both. Operationalizes the discipline that an agent's behavior is determined as much by *where* its context lives as by *what* its context says.

This KF is the canonical home for surface-invariant methodology. Surface-specific application lives in `root_PROJECT_ARCHITECTURE_GUIDE.md` (CP — chat-side Claude Projects) and `root_CC_ENVIRONMENT_GUIDE.md` (CC — Claude Code environments). The unified anti-pattern catalog lives in `root_AGENT_ANTI_PATTERNS.md`.

When designing or auditing any AI agent deployment, this is the first KF consulted — it establishes the placement framework and routing discipline. Surface KFs apply the framework to their respective contexts.

---

## 1. The unified principle

An AI agent environment is a **layered context architecture**. Every piece of content the agent acts on lives in one of several mechanisms — each with a load profile (when the content reaches the agent), an authority profile (whether the content is enforced or merely advised), and a workflow fit (which kinds of work the mechanism naturally supports). The agent's reliability is determined by whether each piece of content lives in the correct mechanism.

The placement rule that governs every architectural decision: **"what mechanism enforces this guarantee?"** before **"what should I write?"** A rule that must hold deterministically belongs in an enforcement layer; a rule that is advisory belongs in a context layer; a procedure with multiple steps belongs in a procedural layer; reference material consulted on demand belongs in a retrieval layer. Misplacement produces unreliable behavior — not because the content is wrong but because the mechanism cannot enforce what the content asks.

This principle is surface-invariant. It governs Claude Project design (the 9-layer CP architecture in `root_PROJECT_ARCHITECTURE_GUIDE.md`) and Claude Code environment design (the 7-layer CC architecture in `root_CC_ENVIRONMENT_GUIDE.md`) equivalently. The mechanisms differ; the discipline is the same.

---

## 2. The two surfaces

AI agent work happens on two distinct surfaces. They are different in shape, different in deployment, and require different mechanisms — but both are governed by the same architectural principles.

**Chat-side (CP — Claude Project surface).** The user works with Claude in a conversational interface (Claude.ai web, mobile app, desktop app). Context is structured into layers that load at conversation start and persist for the conversation duration. The agent's job is reasoning, design, analysis, content production, conversational problem-solving. The surface is bounded by the conversation — when the conversation ends, only the file artifacts the user created persist. Common deployments: methodology design hubs, knowledge-work assistants, domain-specific advisor Projects, content production Projects.

**Code-side (CC — Claude Code surface).** The user works with Claude in a repository-aware autonomous execution environment. Context loads from on-disk artifacts (CLAUDE.md, `.claude/` directory, repository state) at session start. The agent's job is autonomous code execution, multi-step engineering work, file system operations, integration with version control, build systems, and external tooling via MCP. The surface is bounded by the repository — context, history, and artifacts all live in version-controlled files. Common deployments: production codebases under autonomous Claude Code iteration, design-to-deploy delivery projects, repository hygiene and audit operations.

**The two surfaces compose.** Most non-trivial AI agent work involves both. Design happens chat-side; execution happens code-side; evolution learnings flow back chat-side. The chat→Code and Code→chat handoffs are first-class architectural concerns — see §5 below.

**The seed Project (this Project) is the canonical CP example.** It is itself a Claude Project that designs the methodology that governs both surfaces. The reference implementation is dogfooded.

---

## 3. The two layer models

Each surface has its own layer architecture. Both are real; neither subsumes the other. The unified principle (§1) governs both.

**The 9-layer CP architecture.** Defined in detail in `root_PROJECT_ARCHITECTURE_GUIDE.md` and `root_OPTIMIZATION_REFERENCE.md` (Nine-Layer Architecture Model section). Brief inventory:

| # | Layer | Authority | Load profile |
|---|---|---|---|
| 1 | User Preferences | Global, cross-Project | Always loaded |
| 2 | Styles | Global, cross-Project | Always loaded |
| 3 | Global Memory | Global, cross-Project | Always loaded |
| 4 | Skills (global) | Global, cross-Project | On-demand by description match |
| 5 | MCP Connectors | Global, cross-Project | Tool schemas in context, data on demand |
| 6 | Custom Instructions | Project-scoped | Always loaded |
| 7 | Knowledge Files | Project-scoped | Automatic RAG retrieval when knowledge approaches/exceeds the model's context window; full-context loading below that. See `root_OPTIMIZATION_REFERENCE.md` (Context Budget Principles) for the current landscape and the historical ~66,500 measurement from the 200K era. |
| 8 | Project Memory (RAM) | Project-scoped | Always loaded |
| 9 | Conversation | Conversation-scoped | Live context |

The CP layers exist for content that lives across conversations within a Project, content that lives across all Projects (global), and content that exists only within a single conversation. The placement rule: stable always-relevant facts go in CI or RAM; searchable depth goes in KFs; cross-Project patterns go in global layers; conversation-specific decisions stay in conversation.

**The 7-layer CC architecture.** Defined in detail in `root_CC_ENVIRONMENT_GUIDE.md`. Brief inventory:

| # | Layer | Authority | Load profile |
|---|---|---|---|
| 1 | CLAUDE.md | Project-scoped, version-controlled | Loaded every session, full content |
| 2 | `.claude/rules/` (path-scoped) | Project-scoped | Loaded on demand when matching files are read |
| 3 | Skills (`.claude/skills/`) | Project-scoped (or user-scoped) | Loaded on demand when description matches task |
| 4 | Subagents (`.claude/agents/`) | Project-scoped | Spawned with own context window |
| 5 | Hooks (`.claude/settings.json`) | Project-scoped | Run deterministically on lifecycle events |
| 6 | MCP servers (`.mcp.json`) | Project-scoped or user-scoped | Tool schemas in context, data fetched on demand |
| 7 | Settings + permissions | Project-scoped, can inherit from managed policy | Enforced by runtime, not by model |

The CC layers exist for content that loads at every session start (CLAUDE.md), content that loads only when relevant files are read (path-scoped rules), procedures invoked on demand (Skills), focused specialists with isolated context (subagents), deterministic lifecycle guarantees (hooks), external integrations (MCP), and trust/permission boundaries (settings). The placement rule: facts that affect every decision go in CLAUDE.md; per-directory conventions go in path-scoped rules; multi-step procedures go in Skills; context-isolation work goes in subagents; non-negotiable enforcement goes in hooks; external data goes in MCP; trust decisions go in settings.

**Surface mapping.** Some concerns map cleanly across surfaces; some don't. Examples:

- *Always-loaded standing context.* CP: Custom Instructions. CC: CLAUDE.md. Both are "facts the agent reads at every session start."
- *On-demand procedures.* CP: Skills. CC: Skills. Same mechanism, same shape, same authoring discipline.
- *Searchable depth.* CP: Knowledge Files. CC: project files in the repository, indexed by file system rather than RAG.
- *Enforcement layer.* CP: no analog (chat-side has no deterministic enforcement primitive — Custom Instructions are advice, not enforcement). CC: Hooks. The asymmetry matters: CP-side guarantees are advisory; CC-side guarantees can be made deterministic. This is one of the strongest reasons to deploy work CC-side when reliability requirements are strict.
- *External integrations.* CP: MCP Connectors at the global layer. CC: MCP servers at the project layer. Mechanism is the same; scope differs.

The asymmetries are not gaps — they reflect what each surface is good at. CP is for reasoning, design, and content; CC is for execution, enforcement, and integration.

---

## 4. Surface-invariant principles

These principles apply to both CP and CC. They govern every architectural decision in either surface. Surface-specific applications live in the respective surface KFs.

### 4.1 Placement discipline

Ask "what mechanism enforces this guarantee?" before "what should I write?" If the answer requires the model to read context and decide to comply, the rule is advisory — fine for preferences, insufficient for invariants. If the answer is "a hook will block the operation," "a settings restriction will prevent the action," "a path-scoped rule will only load when relevant files are touched," the rule is enforced by the runtime, not by model judgment.

The placement rule is surface-invariant. CP-side: ask whether content belongs in User Preferences (cross-Project), Custom Instructions (Project-stable), Knowledge Files (Project-searchable), RAM (active orientation), or conversation (transient). CC-side: ask whether content belongs in CLAUDE.md (always-loaded), path-scoped rules (file-pattern-specific), Skills (on-demand procedures), subagents (isolated context), hooks (enforcement), MCP (external data), or settings (trust).

Misplacement is the dominant failure mode in both surfaces. The unified anti-pattern catalog (`root_AGENT_ANTI_PATTERNS.md`) is largely a catalog of misplacement patterns.

### 4.2 Decomposition by mechanism

Before specifying any content, decompose the work by what mechanism handles each concern. Do not write CLAUDE.md (or Custom Instructions) and then later think about whether something should be elsewhere. Decompose first; specify second. The decomposition step prevents the "write everything in one place and refactor later" pattern that produces bloated standing-context artifacts.

The decomposition test for any piece of content: does it apply to every session/conversation (always-loaded layer), only when specific work is being done (on-demand layer), only for specific file patterns or contexts (scoped layer), or as a deterministic guarantee (enforcement layer)? Place accordingly.

### 4.3 Lean over comprehensive

A standing context with five precise rules outperforms one with twenty vague ones. The model's adherence to any single rule decreases as the rule count increases — important rules get lost in the noise. Audit every piece of content for whether it earns its place.

The lean-over-comprehensive principle applies most strongly to always-loaded layers (CI, CLAUDE.md). For on-demand layers (Skills, KFs, path-scoped rules), the constraint relaxes — content only loads when relevant, so over-inclusion costs context only at retrieval time. The discipline still applies (scope tightly, name precisely, avoid kitchen-sink files), but the load-cost asymmetry is real.

### 4.4 Source authority hierarchy

When grounding a recommendation, sources rank by authority. Higher-ranked sources override lower-ranked ones when they conflict. This applies surface-invariant — for both CP-side methodology decisions and CC-side environment design decisions.

| Tier | Source class | Authoritative on |
|---|---|---|
| 1 | Anthropic primary documentation (docs.claude.com, code.claude.com, official Anthropic engineering posts) | Claude behavior, API parameters, MCP spec, Skills architecture, Claude Code mechanics |
| 2 | Anthropic engineering blog and design intent posts | Design rationale, emerging patterns |
| 3 | Tested production experience (root.node's own dogfooded patterns; user-validated deployments) | What was tried and what shipped, scoped to the deployment domain |
| 4 | Named practitioners with public artifacts (long-form posts, GitHub repos with documented patterns) | Current state of practice; not authoritative on Claude internals |
| 5 | Community sources (Discord, Reddit, Twitter) | Useful for surfacing emerging issues; never authoritative without independent verification |

A claim grounded only in Tier 5 is speculative and must be marked as such. A claim grounded in Tier 4 is community evidence. Only Tiers 1-3 are authoritative. When the only available source is Tier 5, the recommendation carries a `[speculative]` tag.

This hierarchy applies to research, methodology updates, recommendations to users, and audit findings. Every substantive technical claim in root.node-produced content carries an inline source tag identifying its tier.

### 4.5 Generalizable-vs-specific tagging discipline

Patterns from production deployments are tagged by their generalizability:

- `[generalizable]` — pattern works across deployments of the same surface generally. Examples: 7-layer placement discipline (CC), agent-warranted test for subagent decisions (CC), behavioral countermeasure design (CP), context budget RAG threshold (CP).
- `[specific]` — pattern was specific to one deployment's domain or shape. The structural feature that makes it work doesn't transfer.
- `[generalizable structure, specific content]` — the structural pattern transfers, the specific content does not. Example: the authority matrix (3 tiers) transfers as a structural pattern; the specific tier definitions are deployment-specific.
- `[proposal, not validated]` — described in design but not yet validated against production use. Use with caution; revisit when validated.

Default to "may be specific until proven otherwise." Generalization claims need a basis: name the structural feature that makes the pattern transfer beyond the original deployment.

### 4.6 Files as primary context surface

Decisions worth carrying forward live in files, not in chat history or conversation transcripts. The community phrase "files as universal context" applies in both surfaces: CP-side (KFs, RAM, CI as version-controlled or platform-stored files); CC-side (CLAUDE.md, change_log.md, design briefs, PLANNING.md, SHIP_MANIFEST.md as version-controlled files in the repository).

The discipline:
- Every decision worth carrying forward gets captured in a file before the conversation/session closes.
- Plans and specifications are markdown artifacts the agent reads, not paragraphs the agent infers from past conversation.
- Compaction safety: in CC, project-root CLAUDE.md re-injects after `/compact`; nested files reload on demand. Conversation-only instructions are lost. In CP, KFs persist; RAM persists; conversation-only context is lost when the conversation ends.

The named anti-pattern that violates this discipline: **transcript dump** — pasting chat history into a new session as a prompt. Always restructure into a spec file first.

### 4.7 Halt-and-escalate as a first-class discipline

Every autonomous-execution deployment specifies the conditions under which the agent must stop and surface to a human. Without explicit halt triggers, the failure mode is silent corruption — agents iterate themselves into a worse state without surfacing the change.

CC-side: halt triggers are documented in CLAUDE.md (or referenced from CLAUDE.md to a halt-triggers spec file) and, for guarantees that absolutely cannot be missed, backed by a hook. CLAUDE.md text alone is preference, not enforcement.

CP-side: halt triggers are less common because conversational work has natural human-in-the-loop checkpoints. They become relevant when CP work involves long-running multi-turn sequences with autonomous-style decision-making.

When to halt is design-specific. Examples that apply broadly: authority-matrix tier boundary approach, schema or contract change between layers, test count drop, regression detected, ambiguity that cannot be resolved from existing context. Specific halt conditions are documented in the deployment's CLAUDE.md or CI.

### 4.8 Behavioral countermeasures

Claude has known behavioral tendencies that surface differently in different deployment contexts. The 14-tendency taxonomy (documented in `root_OPTIMIZATION_REFERENCE.md`) covers: agreeableness (1a output-content / 1b persistent-preference dilution), hedging, verbosity three-surface family (3a conversational / 3b agentic narration / 3c written deliverables), list overuse, fabricated precision (external-fact), over-exploration (search breadth), tool miscalibration (7a over-triggering / 7b under-triggering), LaTeX defaulting, editorial drift, self-referential fabrication, over-verification (Opus 5 new), scope expansion (Opus 5 new), subagent over-delegation (Opus 5 new), correction narration (Opus 5 new). Two prompt/environment-conditional defects (conservative-instruction literalism and thinking-disabled output artifacts) are treated separately from the tendency list — they are prompt or API-configuration failure modes, not model tendencies.

Countermeasures are surface-aware. Some tendencies surface more in CP (hedging, list overuse, agreeableness on creative work) where conversational scaffolding is the dominant interaction. Others surface more in CC (over-exploration, subagent over-delegation, scope expansion, verification-instruction accumulation) where autonomous execution amplifies the cost of behavioral drift. The four Opus-5 new tendencies (over-verification, scope expansion, subagent over-delegation, correction narration) surface most strongly on CC and API agent workloads.

The principle: identify the tendencies most likely to surface in the deployment's context, and apply targeted countermeasures in the always-loaded layer (CI for CP, CLAUDE.md for CC). Do not apply all countermeasures to every deployment — that produces bloat. Apply the ones the deployment actually needs. Note that over-verification (Opus 5 tendency #11) is unique: its countermeasure is *removal* of instructions rather than addition. See §4.14.

### 4.9 Evidence grounding

Every claim affecting an architectural decision cites specific evidence. "Best practice" is not a justification — explain the actual mechanism. Evidence sources include: behavior observed in production deployments (cite the deployment), Anthropic primary documentation (cite the page), tested patterns from the methodology (cite the KF), named practitioner artifacts (cite the artifact). Unsupported claims are treated as speculation, not fact.

This applies to root.node's own methodology evolution. Every update to a KF carries grounding for the change. Every audit finding cites specific evidence from the audited environment. Every new pattern added to the anti-pattern catalog identifies the production occurrences that justified its inclusion.

### 4.10 Brand-cleanliness and anonymization in shipped artifacts

Methodology that surfaces from a specific production deployment carries the deployment's brand anchors — proprietary names, internal codenames, project-specific identifiers — that should not appear in shipped artifacts. The anonymization discipline removes the brand anchor without removing the evidence.

The principle: methodology grounding stays verbatim; brand identifiers are swapped for dated/generic forms. A claim grounded in production validation at a specific deployment retains its full evidentiary weight when the deployment's name is replaced with "production CC deployment 2026-05-04" (or equivalent). The reader cannot identify the source organization but can trace the date for verification against build provenance.

**What gets anonymized.** Proprietary deployment names (cchq, hyge, internal codename brands), specific repository identifiers, organization-specific role names, internal team names, project codenames that aren't part of the methodology being claimed. Frontmatter metadata fields (`predecessor`, original-source narrative for inheritance traceability) are exempt — they document the build event, not the runtime artifact.

**What is preserved verbatim.** The methodology itself: the patterns, the source-grade tags, the architectural claims, the "what was tried and what shipped" evidence, the structural feature that makes a pattern transferable. The substance of "this pattern surfaced 27 times across N sessions and resolved without halt violations" remains intact; only the deployment's brand identifier is replaced.

**Why this matters.** Without the discipline, shipped artifacts inherit the brand identifiers of their source deployments. Public-facing methodology (rootnode Skills, KFs cited by Skills, README catalogs) ships with proprietary names that confuse users and break the methodology's portability claim. Internal historical attribution is acceptable in build-provenance artifacts (placement notes, promotion provenance) where the build event itself is being documented; it is not acceptable in the runtime surface (the deployable Skill, the KF that the Skill cites).

**Reference application: Skill descriptions.** The 1024-character description field is the most-visible runtime surface — it auto-activation indexes against user queries. Brand identifiers in description fields are the highest-severity contamination because they pollute the auto-activation index. Description fields use generic phrasing or "rootnode" prefix (per the rootnode-skills repo's brand convention).

**Reference application: filename prefixes.** Files that ship as part of root.node use the `root_` prefix. Files that ship as part of any project follow that project's `{code}_` prefix per User Preferences. Files internal to a research artifact (build CV outputs, design specs) retain their project-of-origin prefix and stay in that project's Drive folder. Cross-project handoff artifacts use `shared_` prefix.

This discipline is operationalized in skill builds via the rootnode-skill-builder Skill's anonymization step (during build pipeline Step 4 — internal language adaptation). The full rule for what gets anonymized vs. preserved per Skill is documented in skill-builder's `references/conversion-guide.md`. The principle stated here is the canonical surface-invariant rule.

### 4.11 "Explain the why" calibration

When authoring agent-facing instructions — system prompts, Skills, CLAUDE.md, Custom Instructions, knowledge files — the prose voice carries weight. Imperative-without-rationale ("MUST not skip step 3", "ALWAYS verify before completion", "NEVER use --no-verify") is appropriate where the instruction is a hard constraint that the model cannot reason its way around: spec compliance, safety boundaries, regulatory requirements, irreversible operations. Reasoned voice ("verify before reporting completion because untested claims compound across sessions") is appropriate where the model can apply judgment: procedural guidance, decision rubrics, design recommendations, situational tradeoffs. The calibration discipline: use imperative voice where reasoning would dilute the constraint; use reasoned voice where reasoning carries equal or greater force.

The principle is grounded in theory-of-mind framing for instruction-tuned models. Modern Claude models reason about why a constraint exists, not just what the constraint says. An imperative without rationale has the model infer the rationale from context, which is unreliable; a reasoned formulation makes the rationale explicit, which the model can apply consistently to edge cases the original authoring did not anticipate. The capitalization of "MUST" and "ALWAYS" carries less weight than the presence of a reasoned grounding the model can verify against the situation it is in.

**When imperative is correct.** Spec compliance ("the description field MUST be ≤ 1024 characters" — the spec is the authority, not the reasoning); safety boundaries ("NEVER push to main without explicit authorization" — the boundary is the authority); irreversible operations ("do NOT force-push to shared branches"); the cases where the cost of the model reasoning its way around the rule exceeds the cost of occasional false-positive halts.

**When reasoned voice is correct.** Procedural guidance ("verify the change applied before declaring done because mid-task verification catches errors at the boundary where they are still cheap to fix"); decision rubrics ("prefer routing-surface SKILL.md sections because procedural depth in SKILL.md duplicates references and turns the 500-line ceiling into a compression problem rather than a design problem"); design recommendations where multiple reasonable choices exist; tradeoff explanations.

**When mixed voice is correct.** Many instructions blend both modes naturally — a hard constraint stated imperatively, followed by reasoned context that explains why the constraint exists and how to apply it to edge cases. The blend is typical for rules that are non-negotiable in the central case but require judgment at the boundary.

**Anti-pattern: caps-everywhere.** A standing context where every instruction is in imperative caps ("MUST", "ALWAYS", "NEVER") signals to the model that everything is non-negotiable — which dilutes the actual non-negotiables. The model loses the signal that distinguishes a hard constraint from a strong recommendation. The tendency surfaces in CLAUDE.md and Skills authored under the assumption that more emphasis produces more compliance; in practice, calibrated voice produces more reliable compliance because the model can distinguish what is load-bearing from what is advisory.

**Application surface.** This principle applies to all agent-facing standing context: CC-side CLAUDE.md and Skills, CP-side Custom Instructions and Skill descriptions, the language used inside reference files, and the prose passages in any deployable artifact the agent reads. It is invoked from `root_SKILL_BUILD_DISCIPLINE.md §7.2` (tone calibration as a permitted change-without-warrant under methodology preservation) and from skill-builder's `references/conversion-guide.md` and `references/auto-activation-discipline.md` during builds. Build CVs apply the calibration to new content authored under the spec; preserved verbatim content is not retroactively rewritten unless the methodology evolution explicitly directs it.

### 4.12 Multi-environment adaptation discipline

Skills and other agent-facing artifacts may run in multiple environments — chat-side (CP), code-side (CC), Cowork sessions, custom orchestrators. The execution capabilities of each environment differ: subagent availability, runnable script execution, file-system access, network access, persistent state. A Skill that assumes one execution context behaves unpredictably in another — its tooling layer fails silently, its empirical workflows skip without surfacing the skip, its verdicts mis-attribute infrastructural failure to methodological failure. The multi-environment adaptation discipline is the surface-invariant principle that names the variability and specifies how artifacts handle it.

The principle: an agent-facing artifact authored to run across multiple environments must flag steps that depend on environment-specific capabilities, carry an explicit compatibility matrix per step, and define fallback behavior for environments that lack a capability. Without these, the artifact has hidden environmental couplings the user discovers only at the failure point — and the failure mode is opaque, because the user cannot tell whether the cause is methodology, configuration, or environment.

**Compatibility matrix pattern.** An artifact that crosses environments documents per-step compatibility in a matrix — what runs in CP, what runs in CC, what runs in Cowork, with explicit fallback notation per environment. The matrix is the artifact future audits and future evolution cycles read to understand the artifact's environmental assumptions; without it, environmental couplings are implicit and brittle. The matrix lives in the artifact's reference layer (e.g., a Skill's `references/multi-environment-adaptation.md`), not buried in prose.

**Tier A/B/C operational model.** For empirical workflows (behavioral validation, description refinement loops, version comparison, benchmark aggregation), the operational model is a three-tier degradation pattern:

- **Tier A.** Full empirical pipeline — subagent execution available, runnable environment available, automated tooling layer invocable.
- **Tier B.** Empirical execution without subagents — runnable environment available, automated subagent grading not available.
- **Tier C.** Analytical floor — neither subagents nor a runnable environment.

The build CV (or runtime evaluation) determines tier applicability based on the actual environment, not the design intent. Verdicts cite the tier they were produced under. Lower tiers are valid as fallbacks; the discipline is "use the strongest tier the environment supports, no more." The principle layer (this section) names the model; the operational details — per-script tier compatibility, per-tier fallback procedures, scenario-specific tier determination — live in `rootnode-skill-builder/references/multi-environment-adaptation.md` and `references/tooling-layer-overview.md`.

**Why this is surface-invariant.** Environmental variability is not unique to any single Skill or surface. Every artifact that may run in more than one execution context faces the same constraint. The principle and the tier model therefore live in the surface-invariant KF; per-Skill applications of the model live in the Skill's references. The Skill that operationalized the discipline first is `rootnode-skill-builder` (v3.0); future Skills with empirical workflows or environment-dependent steps apply the same model.

**Application surface.** The discipline applies to: build CVs that produce verdicts (use the tier model to record the evidentiary basis); Skills with empirical workflows (declare per-workflow tier compatibility); Skills with tooling layers that execute scripts (declare per-script tier compatibility); reference files that walk procedures (note environmental dependencies). It is invoked from `root_SKILL_BUILD_DISCIPLINE.md §10` (environment-adaptive degradation discipline) and from D9 sub-levels (D9a/D9b/D9c) in the 9-dimension quality gate.

**Anti-pattern: silent environment assumptions.** An artifact authored without the discipline assumes its execution context — typically the context the build CV happened to run in — and fails opaquely in others. The user encounters the failure as "the Skill triggered but didn't produce output," with no path to diagnose whether the cause is methodology, configuration, or environment. The compatibility matrix and tier verdicts make environmental dependencies explicit at the artifact level so failure modes become diagnosable rather than mysterious.

### 4.13 Multi-lens audit for self-referential validation

When a framework is used to audit instances of itself, the audit cannot detect blind spots in the framework's own dimensions — definitionally. Skill-builder auditing a Skill against skill-builder's own quality gate cannot surface gaps in the gate. A prompt-validation Scorecard auditing prompts the Scorecard methodology produced cannot catch missing dimensions. Any single-framework audit of its own work product is logically constrained to find only failures the framework already knows how to find.

The fix is multi-lens audit: combine independent frameworks whose blind spots do not overlap. When skill-builder's D1–D9 quality gate, prompt-validation's six-dimension Scorecard, and anti-pattern detection's structural scan all run against the same artifact, gaps in any single lens become visible because the other lenses score on different dimensions. The lenses do not need to be perfectly orthogonal — they need to be independently grounded. A single audit framework extended with new dimensions does not satisfy the principle; the new dimensions inherit the same intellectual lineage as the original ones.

When multi-lens is required: any time a framework audits an artifact that the framework itself produced, or any artifact whose quality definition the framework also defines. Examples — Skills audited against skill-builder's gates; Projects audited against project-architecture principles produced by the same methodology; prompts audited against the Scorecard that defined them. When multi-lens is optional: audits where the audited artifact and the audit framework have independent provenance (e.g., auditing a third-party product against rootnode methodology, or auditing legacy work against newly-developed methodology).

The composition discipline: each lens declares which dimensions it owns. Overlapping coverage is acceptable; conflicting coverage requires explicit reconciliation in the audit output. The audit identifies which lens surfaced each finding so that, when blind spots later become visible, traceability points to which lens needs updating rather than requiring re-derivation across all of them.

The principle generalizes beyond Skills audit. It applies to Project audit (Project Architecture Guide + Audit Framework + Anti-Pattern catalog as three lenses), to prompt audit (prompt-validation + anti-pattern detection + behavioral-tuning), and to environment audit (CC Environment Guide + Anti-Pattern catalog + repo-hygiene). Anywhere root.node uses its own methodology to evaluate its own output, multi-lens applies. `[generalizable; grounded in Tier 3 design analysis 2026-05-07 — Skills catalog audit infrastructure design]`

### 4.14 Verification-instruction discipline

Verification instructions in prompts, Skills, and standing context divide cleanly into two classes with opposite prescriptions on any model that verifies its own work automatically. Anthropic's Opus 5 prompting guide is the specific published guidance grounding this discipline; Sonnet 5 behavior in this area is not documented equivalently (V2 partial from the v4.0 alignment cycle), so the model-specific claims below cite Opus 5 while the discipline itself is surface-invariant and applies wherever the same behavior surfaces. Applying the wrong prescription costs quality: instructing self-directed re-checking causes over-verification (tendency #11) that compounds token cost without a quality gain; removing external-artifact verification lets the model skip evidence grounding it does not automatically perform. The discipline names the two classes and prescribes the correct treatment for each.

**Self-directed re-checking (REMOVE from instructions).** An instruction that asks the model to re-examine its own reasoning or output with no new information. Opus 5 already re-checks its own work automatically; the instruction compounds the behavior. Examples: "double-check your answer," "re-verify before responding," "include a final verification step for any non-trivial task," "use a subagent to verify your work," "before presenting your final answer, verify your reasoning."

**External-artifact verification (KEEP, and keep imperative).** An instruction that asks the model to check a claim against a source outside its own output. Opus 5 does NOT automatically do this — it has to be told to, and the imperative voice is load-bearing. Examples: "verify the file exists at the path claimed," "check the rendered page — a stored-body assert is not proof of clean render," "diff the artifact against the source," "confirm the tag resolves against actual repo state," "run the tests and verify they pass," "grep for the symbol to confirm it exists before recommending it."

**Application to root.node infrastructure.** Quality gates that check an artifact against an independent reviewer or a separate evidence source are external-artifact verification and survive — the D9 quality gate (an independent grader on a separate artifact), the critic-gate Skill (an independent re-derivation of a *different* agent's proposed change), the O10 staleness diff (canonical KFs against staged seed KFs). Instructions telling the model to double-check its own output do not survive. When a quality gate reads to the model as "re-check yourself," it needs rewording; when it reads as "check against evidence X," it stays.

**Sweep discipline.** When auditing a prompt or a Skill for verification-instruction accumulation, classify each hit before acting. Some phrasings are unambiguous ("double-check your answer" — remove; "verify the file exists" — keep). Some are context-dependent ("verify" in an agent-role context may refer to reviewing another agent's work — keep). Do not batch-apply. The Phase 0 sweep patterns for this discipline are `double-check`, `re-verify`, `verify your (own )?work`, `verification step`, `subagent to verify`, `check your answer`.

**Related — conservative-instruction literalism (a prompt defect, not a tendency).** Opus 5 follows "only report high-severity issues" or "be conservative" literally, causing under-reporting. This is a prompt defect exposed by the model. Rewrite affected prompts to two-stage form: (1) report every issue found; (2) filter to the severity level the user wants. Do not compress the two steps into one instruction. Sweep patterns: `only report`, `only flag`, `be conservative`, `high-severity` (as an instruction, not as an output label).

The discipline is surface-invariant. It governs verification content in CP-side Custom Instructions and Skill files equally to CC-side CLAUDE.md and Skill files.

`[generalizable; grounded in Tier 1 Anthropic guidance — the Opus 5 prompting guide at platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5 verbatim: "instructions like these cause over-verification on Claude Opus 5, and removing them reduces wasted tokens with no loss in quality." See also §5 of `root_CLAUDE_OPTIMIZATION_NOTES.md` (tendency #11).]`

### 4.15 Landscape-volatility discipline

Model landscape facts change on release cadences that are shorter than root.node's methodology evolution cadence. Between two design cycles, Anthropic can (and does) release new models, reclassify existing models to legacy, invert effort-guidance rules, change API defaults, and add breaking changes. When those facts are embedded in decision records rather than referenced from a dated landscape block, a landscape refresh invalidates the decision record wholesale, which forces re-decision when the underlying decision may not have actually changed.

**The discipline.** Isolate model landscape facts (model IDs, prices, context windows, effort defaults, thinking behavior, fallback semantics, deprecation dates) as a **dated, independently-versioned landscape block** that decision records *reference* rather than embed. When the landscape refreshes, the landscape block updates; decisions that depended only on the substance (e.g., "we prefer the dual-primary architecture because it distributes calibration risk") survive without re-decision. Decisions that depended on specific facts (e.g., "we chose Opus 4.8 as primary because it is the current front-page recommendation") are the ones a landscape refresh legitimately unlocks — but even those unlock cleanly rather than requiring the whole decision record to be re-derived.

**Application in this cycle.** The v4.0 alignment cycle's design doc `root_skill_5gen_alignment_design.md` §1 is the landscape block — a dated table of the five current models with their facts, verified from official sources on 2026-07-24/25. The decision records (D1–D8) reference §1 rather than embedding its content, so a Sonnet 6 / Opus 5.x release refreshes §1 without invalidating D3 (release-as-major), D4 (verification-instruction discipline), or D5 (prompt-compilation contract shift) — those decisions have rationales independent of specific model identities. D1 (calibration scope) and D2 (effort tables) are the two decisions that would legitimately re-open, and both would re-open through the landscape-block update rather than through a full design-doc re-derivation.

**Design-doc pattern for future cycles.** New design docs that touch model calibration follow this pattern:
- **§1 (or equivalent) — Model landscape.** Dated, source-cited, treated as the reference block. Refresh at each cycle-start.
- **Decision records.** Reference §1 by section rather than embedding model IDs, prices, or effort defaults inline.
- **Explicit revision triggers.** Each decision names the landscape conditions under which it re-opens (e.g., "revision trigger: a Sonnet 6 / Opus 5.x release, or a Fable pricing change making it routine, re-opens D1").

**Not a substitute for verification.** The discipline structures where landscape facts live and how they update. It does not remove the need to re-verify facts against Anthropic sources at each cycle-start — the landscape block is only correct if the verification is done. Pair with §4.9 (evidence grounding).

`[generalizable; grounded in Tier 3 methodology observation — v4.0 alignment cycle experience where a v1.3 design doc locked D1–D3 against a landscape that shifted three days later when Opus 5 shipped, forcing a return-to-chat and full re-decision. The discipline codified here is the structural fix.]`

---

## 5. Cross-surface composition

Most non-trivial AI agent work crosses both surfaces. The chat→Code and Code→chat handoffs are architectural concerns, not afterthoughts.

### 5.1 The chat→Code handoff

Chat-side design produces artifacts (CLAUDE.md draft, scope authorization framework, agent topology, halt triggers, initial prompt, file inventory). When the design is ready to execute, the work moves to Claude Code at the delivery repository.

The handoff is gated by readiness. The `rootnode-handoff-trigger-check` Skill formalizes the readiness decision against seven conditions: spec stability, verification surface, invariants documented, pump-primer instance done, work decomposes into independent units, rollback cost is tolerable, token/usage budget headroom. The gate runs CP-side (in the design conversation) because that is where the readiness decision lives.

Three invocation modes serve different contexts. *Mode 1 (deliberate)* is mechanical — caller provides structured `work_context`, gate evaluates, returns JSON verdict. *Mode 2 (proactive sensing)* fires when Claude detects handoff signals in a design conversation and offers the gate. *Mode 3 (conversational walkthrough)* walks the seven conditions as discussion topics for users new to the gate or for cases where the conversation hasn't yet produced clean evidence.

After PASS verdict, the chat-side conversation produces the handoff bundle (starter CC prompt, file inventory, briefing context). The user opens Claude Code at the delivery repository and pastes the bundle. Chat→Code transition complete.

### 5.2 The Code→chat reverse handoff

Autonomous execution produces friction that warrants returning to chat-side work. Triggers to return:

- A pattern emerges across two or more sessions that wasn't anticipated in the design (warrants methodology evolution).
- A new tool, MCP server, or pattern enters consideration (warrants research before adoption).
- Friction with the existing CLAUDE.md surfaces (warrants design refinement).
- A reusable artifact extraction would benefit other deployments (warrants template production).
- A halt-and-escalate trigger fired and the resolution requires reasoning beyond the deployed scope (warrants design-time diagnosis).

The reverse handoff is currently not formalized by a dedicated Skill. The user opens chat-side Claude in the design Project and frames the issue. The design Project's CI captures the relevant evolution mode (e.g., EVOLVE mode in `rootnode-cchq-design`). When the diagnosis or design refinement is complete, the resolution either flows back to CC (incremental update) or the design itself is revised (methodology evolution). A dedicated reverse-handoff Skill is on the Stage 7 backlog.

### 5.3 The round-trip discipline

Design with the round-trip in mind. A deployment is one node in a workflow; the value comes from clean handoffs in both directions. Specifically:

- Every CC deployment plan produced chat-side names the chat→Code handoff point explicitly.
- Every CC deployment specifies the conditions under which work returns to chat-side (the §5.2 triggers, scoped to the deployment).
- Both directions are designed before execution begins. Discovering the round-trip mid-execution produces friction.

### 5.4 Cross-Skill contracts

Skills that compose with each other carry cross-Skill contracts — the field names, schema patterns, semantic invariants, and routing rules that one Skill expects from another. Without explicit contracts, composition drifts: a Producer Skill changes a field name in a v2 release, the downstream Consumer Skill keeps reading the old name, and the composition silently breaks.

The contracts surfaced through the rootnode runtime tooling builds (rootnode-repo-hygiene v1, rootnode-cc-design v2 REMEDIATE) are documented here as the canonical cross-Skill composition disciplines.

#### 5.4.1 The three approval forms (blanket / fragmented / conditional)

Runtime Skills that execute a multi-step plan against user-owned artifacts require explicit user authorization before transitioning from plan-generation to execution. The authorization model has three forms:

- **Blanket approval.** User accepts all steps in the plan. All steps execute in sequence. Use when the user has reviewed each step and accepts the full set with no exceptions.
- **Fragmented approval.** User accepts a specific subset of steps by step ID. Only those steps execute; remaining steps are skipped. Use when the user accepts some changes but not others.
- **Conditional approval.** User accepts steps that satisfy a predicate (e.g., risk tag, finding category, step type). Only steps satisfying the predicate execute. Use when the user wants risk-stratified execution without naming individual step IDs.

**Granularity rule.** The granularity of fragmented and conditional approval is determined by the natural granularity of the artifact being acted upon. For Skills consuming structured findings (rootnode-repo-hygiene's HYGIENE_REPORT.md), the granularity is finding-ID (`F-{cat}.{n}`). For Skills consuming structured execution plans (rootnode-cc-design REMEDIATE's EXECUTION_PLAN.md), the granularity is step-ID. Future Skills implementing this pattern apply the same test: what is the natural unit of decision in the artifact? That unit is the granularity. Granularity is not a stylistic choice — it is the structural property of the artifact.

**Anti-condition.** Ambiguous approval ("looks good," "go ahead") does NOT enter execution. The Skill surfaces an explicit prompt: "I need an explicit approval form: blanket / fragmented / conditional." The model must commit the user to one of the three forms before transitioning from plan-generation to execution.

#### 5.4.2 The `critic_gate_threshold` cross-Skill contract

Runtime Skills that compose with `rootnode-critic-gate` (an independent re-derivation gate that reviews proposed changes during autonomous execution) carry a profile field `critic_gate_threshold` with two valid values:

- **`required`.** Every proposed change must pass the critic gate before execution. If `rootnode-critic-gate` is not installed when this profile is active, the Skill HALTS with an explicit prompt: "critic-gate is required by the active profile but not installed; install or change profile."
- **`optional`.** The critic gate is consulted on a per-change (or per-batch) basis at user choice. If `rootnode-critic-gate` is not installed, execution proceeds without critic review.

**Negative-case rule.** When `critic_gate_threshold: optional` is set AND `rootnode-critic-gate` IS installed: the Skill prompts the user per change (or per batch) whether to invoke the critic. Both Skills currently using this contract (rootnode-repo-hygiene Phase 2, rootnode-cc-design REMEDIATE Phase 2) handle this consistently — per-step user choice. Future Skills implementing this contract follow the same per-step-prompt semantic. The consistency is part of the contract; deviating from it would break user expectations across composed Skills.

**Why two values, not three.** A "never invoke" option is unnecessary — uninstalling the critic gate, or using a different profile with `critic_gate_threshold: optional` and declining at the prompt, achieves the same effect. The two-value design keeps the contract minimal.

#### 5.4.3 Producer→Consumer chain documentation

When a Skill produces an artifact that another Skill consumes (the Producer→Consumer chain), the contract is documented in the Producer's placement note (audit artifact per `root_SKILL_BUILD_DISCIPLINE.md §4.1`) AND in the Consumer's placement note. Both directions: the Producer documents what it ships and to whom; the Consumer documents what it consumes and from whom.

**Field-level contract elements.** The chain documentation includes: the artifact name (e.g., HYGIENE_REPORT.md, EXECUTION_PLAN.md); the schema pattern (finding-ID format `^F-\d+\.\d+$`, step-ID granularity, severity tag taxonomy); the semantic invariants (which findings route to which Consumer; which categories halt vs. continue); the version-coupling rule (does the Consumer assume a specific Producer version, or any version implementing the schema?).

**Producer rebuild rule.** When a Producer Skill is rebuilt (v1 → v2), the Consumer must be re-validated against the new Producer artifact before the v2 ship is announced. The cross-Skill contract is verified against the Producer's actual built artifact, not against the Producer's design spec. This was the R6 mitigation in the Phase 30 D-build CV: cc-design v2's contracts with repo-hygiene v1 were verified against the built `rootnode-repo-hygiene.zip`, not against the design spec `root_design_repo_hygiene_skill.md`. Design specs can drift from built artifacts during build CVs (within-scope-lock material findings per `root_SKILL_BUILD_DISCIPLINE.md §8.1`); the built artifact is the authoritative contract source.

**Bidirectional handoff (deferred composition).** Some Producer→Consumer chains are bidirectional in principle but unidirectional in current implementation. Example: rootnode-repo-hygiene's Cat 14 process-abstraction findings can flow to rootnode-skill-builder Gate 2 as warrant evidence; rootnode-cc-design REMEDIATE could in principle do the same when it surfaces methodology-generalizable patterns. The forward chain (repo-hygiene → skill-builder Gate 2) is implemented; the parallel chain (cc-design REMEDIATE → skill-builder Gate 2) is documented as a roadmap item. Bidirectional contracts are valuable but cost-bound — implement when warranted.

### 5.5 KF propagation chain — four landing locations for canonical updates

When KF methodology is updated, the propagation chain has four landing locations. The first three must all be synced for any update to be effective across the ecosystem; the fourth is conditional on the update's scope:

1. **Seed Project knowledge files** (chat-side CV use). Updated by operator upload after Phase 32a-style staging review.
2. **Repo-local `audit/canonical-kfs/`** (CC session use). Updated as a precondition step on the relevant feature/release branch — the CC agent reads `@audit/canonical-kfs/` for methodology grounding during work.
3. **Installed Skill copies** (runtime use — `~/.claude/skills/{skill-name}/` or platform-specific install paths). Updated when Skills are reinstalled from new release zips.
4. **Global `~/.claude/CLAUDE.md`** (universal-discipline use — every CC session on the machine, regardless of repository). **Conditional, and the condition is load-bearing.** This location takes disciplines that are surface-invariant and project-independent — verification discipline, evidence-labeling, summary-reconciliation. It does not take methodology scoped to a project, a repository, or a model generation. Model landscape facts in particular belong in a dated landscape block per §4.15, not here: a global file is the worst place for a fact with a short half-life, because nothing prompts a re-read. Apply the universality test before landing anything here — if the discipline would not hold in an unrelated repository under a different model, it is not a location-(4) update.

Failure to sync any one of the first three creates silent staleness: a CC agent may read older methodology from `audit/canonical-kfs/` even after the seed Project has newer content; a chat-side CV may read newer content from the seed Project even after a runtime Skill ships with older content embedded. Location (4) fails differently — it does not go stale relative to the others so much as it goes *unwritten*, because no build step touches it and no session surfaces its absence. Each sync point has a different responsibility model: (1) is operator manual after staging review; (2) is CC build prompt automatic per branch; (3) is release packaging automatic per Skill rebuild; (4) is operator manual with no automation and no failure signal, which is why it needs an explicit evaluation step rather than a habit.

Pattern: every methodology update CV documents which of the four landing locations it covers, including an explicit not-applicable verdict for (4) when the update is project-scoped; the build prompt for any Skill that consumes the methodology covers location (2) as a precondition step (cf. v3.0 build prompt §32b.1.5 for the canonical-kfs/ sync example); release packaging covers location (3) by rebuilding affected Skill zips. Cross-cutting methodology updates (e.g., updates that affect multiple Skills) require multiple location-(3) syncs.

`[generalizable; grounded in Phase 31d post-execution evaluation 2026-05-07 — surfaced when the v3.0 design spec's Phase 32a left a gap between staging-kf/ updates and audit/canonical-kfs/, requiring a §32b.1.5 precondition step to close. Location (4) added 2026-07-28 from Phase 32 Observation O11, which had been live operator practice and tracked in root_build_context.md since 2026-06-27 without ever landing in this section's text — a three-location heading over a four-location practice. The gap surfaced during the v4.0 CI rewrite when this section was read rather than recalled.]`

---

## 6. Runtime tooling catalog

The rootnode runtime layer is a set of operational Skills that implement the methodology patterns from this KF and the surface KFs. Skills are profile-driven and orchestrator-agnostic — they work with any execution surface (Claude.ai, Claude Code, n8n, custom orchestrators, hand-invocation). They are not load-bearing for the methodology; the patterns stand without the Skills, and the Skills are evaluated against the patterns rather than the other way around.

The runtime layer splits across surfaces by deployment target.

### 6.1 CP-side Skills (run in chat-side Projects)

| Skill | Purpose | Implements pattern from |
|---|---|---|
| `rootnode-handoff-trigger-check` | Pre-execution readiness gate (7-condition evaluation) | §5.1 chat→Code handoff |
| `rootnode-profile-builder` | Conversational profile authoring for any consuming Skill | Configuration entry point for the runtime layer |
| `rootnode-skill-builder` | Builds deployment-ready Skill files (SKILL.md + references/) from design specs | Skill design and packaging discipline |

Two additional CP-side Skills handle design and review:

| Skill | Purpose |
|---|---|
| `rootnode-cc-design` (formerly `rootnode-cchq-design`) | Designs Claude Code prompts and CC environments. Five modes — DESIGN, EVOLVE, RESEARCH, TEMPLATE, REMEDIATE. Operates dual-surface (greenfield design CP-side; brownfield audit and remediation CC-side). |
| `rootnode-prompt-validation` | Scores chat prompts and system prompts using the Prompt Scorecard. CP-only by design — chat prompts are a CP-side artifact. |
| `rootnode-project-audit` | Audits Claude Projects against the Project Scorecard. CP-only by design — Projects are a CP-side artifact. |

(Other CP-side Skills exist in root.node's broader inventory — block libraries, domain packs, methodology-application Skills. They are documented in `root_CONTENTS_INDEX.md`.)

### 6.2 CC-side Skills (run in Claude Code at delivery repositories)

| Skill | Purpose | Implements pattern from |
|---|---|---|
| `rootnode-critic-gate` | Independent re-derivation of proposed changes during autonomous execution (4-check protocol) | Per-change governance discipline |
| `rootnode-mode-router` | Selects active profile from runtime context (calendar, time window, geofence, custom signals) | Profile-driven gate behavior |
| `rootnode-repo-hygiene` | 14-category sweep + 7-layer leak check; produces audit report; executes approved findings | Repository hygiene discipline |

`rootnode-cc-design` (above) also runs CC-side for brownfield audit and REMEDIATE mode (consuming hygiene findings, producing and executing remediation plans).

### 6.3 Layer-fit boundary

The runtime Skills do not compete with full software-development workflow systems. Workflow systems (e.g., GSD, Superpowers, custom orchestrators) define *how* to do software development — exploration, planning, execution, verification, completion. The rootnode runtime Skills govern *when* autonomous execution is allowed and *with what strictness* per change.

The composition pattern: handoff-gate fires before invoking a workflow system; critic-gate reviews changes emerging from a workflow system's execute-phase wave; mode-router selects the active profile that governs both gates. The runtime Skills are thin governance over thick workflow systems, not replacements for them.

When evaluating an external Claude Code tool against rootnode runtime Skills, the right question is layer-fit (governance vs. workflow), not feature overlap.

---

## 7. The seed Project as reference implementation

The seed Project (this Project) is the reference implementation of the methodology this KF establishes. Every structural decision made in the seed — how knowledge files are organized, how Custom Instructions reference them, how components integrate, which Skills are installed CP-side — is a tested pattern for building future Projects in any domain.

The seed dogfoods the methodology. Specifically:

- The seed's CI follows the 5-layer architecture (Identity, Objective, Context, Reasoning, Output + Quality Control) from `root_MASTER_FRAMEWORK.md`.
- The seed's KFs follow the placement discipline from §4.1 — methodology in KFs, orientation facts in RAM, behavioral rules in CI, cross-Project patterns in User Preferences.
- The seed's Memory layer follows the hygiene rules from `root_OPTIMIZATION_REFERENCE.md` (Memory section).
- The seed's KF inventory follows the principle that each file has a single, clear purpose with no content overlap.

When advising a user on how to design their own Claude Project, the seed is the worked example. When the methodology evolves, the seed evolves with it.

---

## 8. Where to go next

For surface-specific methodology:

- **CP-side (Claude Project) design and architecture:** `root_PROJECT_ARCHITECTURE_GUIDE.md`. Covers Custom Instructions design, knowledge file architecture, Project scoping, integration patterns, quality criteria, self-documentation. The 9-layer architecture in detail.

- **CC-side (Claude Code) environment design:** `root_CC_ENVIRONMENT_GUIDE.md`. Covers CLAUDE.md design (R1-R5/W1-W3), agent topology, scope authorization, halt-and-escalate, hooks, MCP minimalism, files-as-context, the chat→Code handoff. The 7-layer architecture in detail.

For the unified anti-pattern catalog:

- **Common failure modes across both surfaces:** `root_AGENT_ANTI_PATTERNS.md`. The unified catalog of structural and behavioral anti-patterns, surface-tagged. Used during audit, design review, and evolution decisions.

For Skill build discipline:

- **Building rootnode Skills (gates, quality gate, audit artifacts, methodology preservation, version lifecycle, design-spec consumption, description refinement loop, environment-adaptive degradation):** `root_SKILL_BUILD_DISCIPLINE.md`. The canonical home for rootnode Skill build methodology — pre-build gates, the 9-dimension quality gate (with D9a/D9b/D9c sub-levels), build-event audit artifacts, token-budget heuristics, version-and-lifecycle rules, methodology preservation across releases, design-spec consumption discipline, description refinement loop discipline, and environment-adaptive degradation discipline. The rootnode-skill-builder Skill operationalizes the disciplines documented there.

For audit and optimization:

- **Project audit methodology:** `root_AUDIT_FRAMEWORK.md`. Project Scorecard (six dimensions), Anti-Pattern Checklist, Cross-Layer Alignment Check, Diagnostic Question Bank.

- **Structural optimization principles and fix patterns:** `root_OPTIMIZATION_REFERENCE.md`. Nine-Layer Architecture Model in detail, behavioral tendency taxonomy, Memory layer design, context budget principles, RAG quality optimization, common structural fixes.

For prompt-level work:

- **Master framework (block libraries, 5-layer prompt architecture):** `root_MASTER_FRAMEWORK.md`.
- **Compiler (forward workflow — building prompts and Project scaffolds):** `root_PROMPT_COMPILER.md`.
- **Optimizer (reverse workflow — auditing and improving existing Projects):** `root_PROJECT_OPTIMIZER.md`.

For prompt testing and refinement:

- **Diagnostic and refinement methodology:** `root_PROMPT_TESTING_GUIDE.md`. Symptom-to-root-cause map, Prompt Scorecard, Output Evaluation Rubric.

For navigation:

- **Lightweight index of all KFs in this Project:** `root_CONTENTS_INDEX.md`. Consult first when uncertain which KF contains the needed information.

---

*End of root_AGENT_ENVIRONMENT_ARCHITECTURE.md.*
