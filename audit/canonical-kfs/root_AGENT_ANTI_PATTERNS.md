# root_AGENT_ANTI_PATTERNS.md

The unified catalog of structural and operational anti-patterns in AI agent environments. Covers both Claude Projects (CP — chat surface) and Claude Code (CC — autonomous execution surface). Each pattern is surface-tagged: `[CP]`, `[CC]`, or `[both]`. Patterns at one surface that have analogs at the other are cross-referenced.

This KF consolidates root.node's seven structural CP anti-patterns and the fifteen operational CC anti-patterns surfaced through production validation, deduplicated and unified. It is the diagnostic catalog for audit work — both surface-specific audits (running `rootnode-project-audit` on a chat Project, running `rootnode-repo-hygiene` on a CC repository) and cross-surface design reviews.

The architectural principles that the patterns violate are documented in `root_AGENT_ENVIRONMENT_ARCHITECTURE.md`. Surface-specific application contexts are in `root_PROJECT_ARCHITECTURE_GUIDE.md` (CP) and `root_CC_ENVIRONMENT_GUIDE.md` (CC).

---

## 1. How to use this catalog

**Use during audit.** When auditing a deployment, walk the catalog systematically — both surface-invariant patterns and surface-specific patterns. Every detected pattern carries a finding tagged with the pattern ID, structural evidence, and the recommended fix. Findings ordered by impact, not order of detection.

**Use during design review.** When reviewing a proposed deployment design, scan for patterns the design might introduce. Pre-launch detection is cheaper than post-launch remediation.

**Use during evolution.** When a deployment surfaces friction, diagnose against the catalog before redesigning. Most friction is a known anti-pattern manifesting; the named pattern usually carries the fix.

**Severity calibration.** Not every pattern is a blocker. Some are concerns to track; some are immediate fixes. The catalog provides the structural diagnosis; severity depends on deployment context.

**Catalog maintenance.** Patterns enter the catalog after surfacing in 3+ independent deployments or being documented by named practitioners. Speculative patterns are not added — the catalog is grounded in production evidence. New patterns are added through methodology evolution sessions, with grounding documented in `root_build_context.md`.

---

## 2. Surface-invariant patterns (apply to both CP and CC)

### 2.1 Monolithic standing context `[both]`

**CP signature:** A single Custom Instructions file or knowledge file carries multiple unrelated concerns. The CI mixes identity, behavioral rules, output standards, reference material, and conversational guidance. A KF tries to be both methodology and reference and history. The component is large, scrolls past easily, and adherence to specific rules degrades as the file grows.

**CC signature:** CLAUDE.md exceeds the 200-line target, contains multi-step procedures embedded inline, contains file-pattern-specific rules, contains reference material that should live in dedicated files. (The CLAUDE.md-specific manifestation — "Bloat" — is documented at `root_CC_ENVIRONMENT_GUIDE.md §2.4`.)

**Cause:** Treating the standing-context layer as the catch-all. "If I write it here, the agent will see it." Conflating "always-relevant facts" with "everything the agent should know." Adding to the file faster than refactoring it.

**Fix:** Apply the placement rule from `root_AGENT_ENVIRONMENT_ARCHITECTURE.md` §4.1. Multi-step procedures move to Skills. Path-specific rules move to `.claude/rules/` (CC) or scope-narrow KFs (CP). Reference material moves to dedicated files Claude reads on demand. Behavioral guarantees (CC) move to hooks. Trim until only "facts that matter every session" remain in the standing-context layer.

**Validation:** after refactor, re-audit the standing-context layer against the placement rule. If any section still fits a different mechanism, the refactor is incomplete.

### 2.2 Layer hierarchy violation `[both]`

**CP signature:** A lower-precedence layer attempts to override a higher-precedence layer. Custom Instructions tries to override User Preferences (or vice versa: User Preferences expecting CI-level specificity). RAM (Project Memory) carries content that should be in CI (always-relevant rules) or KFs (searchable depth). Conversation tries to permanently change behavior without the CI being updated.

**CC signature:** Auto memory (machine-local, per-working-tree) carries team-relevant rules that should be in CLAUDE.md (team-shared, version-controlled). Project-level CLAUDE.md attempts to override managed-policy CLAUDE.md (which sits at organizational ceiling). Settings inheritance produces unexpected behavior because the higher-priority layer wasn't accounted for. (Specific CC variant: see §4.10 Auto memory misuse below.)

**Cause:** Unfamiliarity with the precedence chain. Letting incidental writes (auto memory in CC, conversation drift in CP) accumulate content that should have been promoted to a higher-precedence layer. Treating layers as interchangeable rather than as a hierarchy.

**Fix:** Identify the correct layer for each piece of content using the surface-specific layer model (`root_PROJECT_ARCHITECTURE_GUIDE.md` for CP, `root_CC_ENVIRONMENT_GUIDE.md` §1 for CC). Promote team-relevant content from machine-local layers to team-shared layers. Audit RAM (CP) and auto memory (CC) periodically to surface promotion candidates. Document the precedence chain explicitly in onboarding artifacts so future contributors know the hierarchy.

### 2.3 Transcript-as-context `[both]`

**CP signature:** Custom Instructions or knowledge files reference past chat conversations as if they were durable context ("As we discussed in our earlier session..."). RAM carries content that's actually conversation-specific decisions rather than persistent orientation. The deployment relies on the assumption that prior conversation is still in context — but the conversation may have ended or been compacted.

**CC signature:** A handoff document or onboarding file reads like pasted chat history. Prompts contain "remember our conversation about X" framing. CLAUDE.md or change_log entries reference verbal decisions that have no file backing. (The CC variant is documented at §4.1 Transcript dump below.)

**Cause:** Chat as source of truth instead of files. Failing to convert conversation outcomes into version-controlled artifacts before the conversation closes.

**Fix:** Apply the files-as-context principle from `root_AGENT_ENVIRONMENT_ARCHITECTURE.md` §4.6. Restructure conversation outcomes into named-section spec files (PLAN.md, SPEC.md, design briefs). Capture every decision worth carrying forward in a file before the chat window closes (CP) or before `/compact` runs (CC). Plans and specs are markdown artifacts the agent reads, not paragraphs the agent infers.

---

## 3. CP-only patterns

These patterns are specific to the Claude Project surface. They have no direct CC analog because the failure mode depends on the conversational/Project structure that doesn't exist in CC.

### 3.1 Phantom Conversation `[CP]`

**Signature:** Custom Instructions or knowledge files reference past conversations, sessions, or conversational decisions that don't exist in the current Project's persistent state. "As we established last week," "per the earlier session," "you'll remember from our discussion." The agent cannot retrieve the referenced context because conversational state doesn't persist across sessions.

**Cause:** Treating conversation as if it were durable context. Failing to migrate conversation outcomes into KFs, RAM, or CI before the conversation closed.

**Fix:** Audit CI and KFs for conversational references. For each reference, locate the underlying decision and migrate it into the appropriate persistent layer (CI for behavioral rules, KFs for searchable depth, RAM for active orientation, User Preferences for cross-Project patterns). Remove the conversation references; replace with citations to the persistent artifacts that now carry the content.

**Related:** §2.3 Transcript-as-context (the broader cross-surface pattern); §4.1 Transcript dump (CC variant).

### 3.2 Echo Chamber `[CP]`

**Signature:** Custom Instructions duplicate content from knowledge files (or vice versa). The same rule appears in CI, in a KF, and possibly in RAM. When the rule needs updating, multiple files must change in lockstep — they drift instead.

**Cause:** Adding content where it feels needed without checking whether it already exists elsewhere. Defensive duplication ("better to have it in both places"). Lack of single-source-of-truth discipline.

**Fix:** Identify the single canonical home for each rule. Behavioral rules live in CI. Reference depth lives in KFs. Cross-Project patterns live in User Preferences. Active orientation lives in RAM. Reduce duplicates to a single canonical entry; replace duplicate copies with references to the canonical location. Audit periodically — duplication accumulates over time.

**Related:** §3.4 Kitchen Sink (a CI mixing concerns is often duplicating KF content as a side effect); §3.3 Orphan File (a KF whose content lives in CI is essentially orphaned).

### 3.3 Orphan File `[CP]`

**Signature:** A knowledge file exists in the Project but nothing routes to it. The CI doesn't reference it; no other KF cites it; conversation patterns don't trigger it. The file consumes Project storage but never reaches the agent's context. In RAG mode, it may be retrieved occasionally by query similarity but with no purposeful triggering.

**Cause:** KF added during exploratory work and never integrated into the routing structure. KF whose role was superseded by other content but never deleted. KF written for a use case that didn't materialize.

**Fix:** Audit each KF against CI references. KFs with no reference are candidates for routing addition (if the content is still relevant) or deletion (if the content is obsolete or duplicated elsewhere). Update CI to reference active KFs explicitly with guidance on when to consult them. Maintain `root_CONTENTS_INDEX.md` (or equivalent navigation index) so the routing structure is auditable.

**Related:** CC analog is closer to §4.3 Manual-only Skills (with weak descriptions that never auto-activate) — the structural failure is similar (artifact exists but doesn't reach Claude's context).

### 3.4 Kitchen Sink (structural) `[CP]`

**Signature:** A single component (CI, KF, or RAM section) carries multiple unrelated concerns. The CI mixes identity, behavioral rules, output standards, mode definitions, and reference material. A KF tries to be both methodology and reference and worked examples. The agent has trouble finding the right content for the current task because everything is jumbled.

**Cause:** Concerns added to existing components without refactoring. "I'll just add this here" pattern repeated without periodic decomposition. No discipline of "one component, one purpose."

**Fix:** Decompose by concern. CI carries behavioral rules and identity; reference material moves to KFs. Each KF has one clear purpose with no content overlap. RAM carries active orientation only — methodology lives in KFs, cross-Project patterns in User Preferences. Audit each component for coherent purpose.

**Related:** §2.1 Monolithic standing context (Kitchen Sink in CI is one form of monolithic context); §3.5 Blurred Layers (mixing instructions with reference material is one form of Kitchen Sink). CC has a separately-named pattern at §4.13 Kitchen-sink session, but it's operational not structural — see §4.13 below.

### 3.5 Blurred Layers `[CP]`

**Signature:** Behavioral instructions and reference material live in the same file. CI contains long passages of explanatory content that should be in KFs; KFs contain operational rules that should be in CI. The agent reads CI as both rule source and reference source, with no clear delineation of which content controls behavior vs. which content informs reasoning.

**Cause:** No clear discipline of "rules in CI, reference in KFs." Adding explanatory context inline because it feels helpful, without recognizing that CI's role is behavioral guidance, not exposition. Reference material accumulating in CI because it was easier to write there than to create a KF.

**Fix:** Audit CI for content that's actually reference material — explanatory passages, examples, background context, methodology depth. Migrate to appropriate KFs. CI should be lean behavioral guidance; KFs carry the depth. Conversely, audit KFs for content that's actually behavioral rules; promote to CI if they apply universally, or restructure as KF guidance for specific work.

**Related:** §2.1 Monolithic standing context; §3.4 Kitchen Sink. CC's CLAUDE.md Bloat pattern (`root_CC_ENVIRONMENT_GUIDE.md §2.4`) overlaps when CLAUDE.md mixes rules with reference.

### 3.6 Build-scaffolding leak in user-facing artifact `[CP]`

**Signature:** A Skill or other user-facing artifact carries references to project-specific build-time scaffolding in its frontmatter, body, or examples — design-brief filenames the user has never seen, internal phase tags (`phase-29`, `cv-12`), proper-noun anchors to the author's own projects (specific brand names, internal session identifiers, undocumented codenames). The most common manifestation: `metadata.original-source` field listing a project-specific design brief (e.g., `rootnode_context_budget_v5_enhancement_brief.md`) that doesn't exist in any artifact the user can access.

**Cause:** Scaffolding was useful at build time and got serialized into shipped frontmatter or content without a brand-cleanliness pass. The author was building inside their own project context where the references were meaningful; the scrub-for-public step was skipped or never defined as a build obligation. The principle in `root_AGENT_ENVIRONMENT_ARCHITECTURE.md §4.10` (brand cleanliness in shipped artifacts) was either not yet codified at the time of the build or not applied during build closeout.

**Fix:** During build, every user-facing field is checked against the test "would a user installing this Skill globally understand this reference without access to my private project?" If no, generalize. Three replacement strategies in priority order: (1) cite a canonical KF the user can read (e.g., `OPTIMIZATION_REFERENCE.md` instead of a project-internal brief), (2) anonymize ("seed-project methodology synthesis," "production CC deployment 2026-05-04"), or (3) remove the field entirely if no agnostic replacement exists. The build CV's closeout explicitly runs this scrub against the produced artifact before zip delivery.

**Related:** `root_AGENT_ENVIRONMENT_ARCHITECTURE.md §4.10` (brand cleanliness, the canonical principle this pattern violates). §3.4 Kitchen Sink can hide brand leakage when build-scaffolding is mixed with substantive content. The cc-design v2 build is a positive example — it deliberately anonymized brand-anchored content to "production CC deployment 2026-05-04," documenting the scrub explicitly in its placement note.

---

## 4. CC-only patterns

These patterns are specific to the Claude Code surface. They depend on CC mechanisms (hooks, MCP, subagents, settings) that don't exist in CP.

### 4.1 Transcript dump `[CC]`

**Signature:** Handoff documents or onboarding files read like pasted chat history. Prompts contain "remember our conversation about X." CLAUDE.md or change_log references verbal decisions with no file backing.

**Cause:** Chat as source of truth instead of files.

**Fix:** Restructure chat decisions into named-section spec files (PLAN.md, SPEC.md, design doc). Apply files-as-context discipline.

**Related:** §2.3 Transcript-as-context (the cross-surface principle).

### 4.2 MCP bloat `[CC]`

**Signature:** `.mcp.json` with 5+ servers; tool schemas exceed roughly 20K tokens; sessions degrade after a few turns due to context pressure.

**Cause:** Adding every available MCP "for completeness" instead of fitting tools to actual workflows. The mechanism is per-turn injection: every enabled MCP server's tool schemas are injected into the context window on every turn, regardless of whether any tools are invoked. A heavyweight server can cost 20K+ tokens per turn on its own. This cost compounds across subagent spawns — each fresh subagent inherits the full schema overhead. Five unused servers averaging 5K tokens each impose a 25K-token tax on every turn before the agent reads a single project file.

**Fix:** Trim to 2-3 essentials per the deployment's actual tooling needs. Use deferred tool loading (Claude Code 2026 default). Evaluate each MCP against actual usage data — if a server's tools haven't been invoked in N sessions, deprecate. Per-subagent MCP scoping (`mcpServers:` in subagent frontmatter) keeps tool definitions out of the main conversation when only a specialist needs them. Before long-running autonomous phases, audit enabled servers: browser/playwright tools needed? platform-specific tools needed? cross-project stale MCPs still enabled? Trimming MCPs and tuning model profiles are independent levers that compound — do both, and audit MCPs first because per-turn savings show up immediately.

### 4.3 Manual-only Skills `[CC]`

**Signature:** Skills present but `disable-model-invocation: true` widespread, weak `description:` fields lacking triggering verbs, no auto-activation hooks. Skills exist but Claude doesn't auto-invoke them; users must remember to invoke explicitly.

**Cause:** Treating Skills as user-triggered commands rather than as Claude-discoverable capabilities. Description fields written as static descriptors rather than as activation criteria.

**Fix:** Strengthen `description:` fields with verb-based triggering language and context phrases users actually say. Auto-invocation defaults to on. Reserve `disable-model-invocation: true` for Skills that should genuinely be human-only (deploys, irreversible operations, multi-step workflows where auto-invocation would skip a required earlier step). Add UserPromptSubmit / PreToolUse hooks for high-priority Skills if needed.

**Related:** §3.3 Orphan File (CP analog — artifact exists but doesn't reach Claude).

### 4.4 Enforcement-as-preference `[CC]`

**Signature:** CLAUDE.md or Skills contain rules like "always run tests" or "never modify X" without a backing hook. The rule is followed most of the time but not deterministically.

**Cause:** Believing prompt-level instructions are sufficient for invariants. Underestimating the cost of occasional non-compliance.

**Fix:** Move guarantees to hooks. PreToolUse to block; PostToolUse to enforce; Stop to verify-before-completion. Keep prompts for preferences only. See `root_CC_ENVIRONMENT_GUIDE.md` §6 for the hooks-vs-prompts decision rule.

### 4.5 Subagent overuse `[CC]`

**Signature:** 10+ custom subagents; many rarely invoked; agents that duplicate built-ins (Explore, Plan, general-purpose); agents created for sequential work that doesn't actually parallelize.

**Cause:** Treating subagents as a default multiplier instead of a context-isolation primitive. "More agents = more capability" mental model.

**Fix:** Audit each subagent against the agent-warranted test (`root_CC_ENVIRONMENT_GUIDE.md` §3.1). Deprecate or merge agents that don't meet warrant criteria. Lean on built-ins where they suffice. The agent-warranted test asks: does the work require multiple distinct cognitive perspectives running in parallel, or sequential decomposition with handoffs? If neither, a single-agent loop is correct.

**Related:** §4.6 Subagent underuse (the complementary pattern — both indicate poorly calibrated subagent strategy).

### 4.6 Subagent underuse `[CC]`

**Signature:** Main conversations consistently bloat with research; no custom subagents; built-in Explore is not used for codebase queries; sessions routinely fill past 60K tokens of context.

**Cause:** Unfamiliarity with subagents; culture of single-conversation work; not recognizing that research tasks pollute main context.

**Fix:** Identify recurring research-heavy patterns; promote to explicit subagent invocations. Use built-in Explore for codebase queries (read-only, isolates the search context from the main conversation). Consider 1-2 well-scoped custom subagents for repeated specialist work (e.g., security reviewer, test writer, docs proofreader).

### 4.7 `bypassPermissions` outside sandbox `[CC]`

**Signature:** `--dangerously-skip-permissions` in scripts, CI configurations, or default user settings outside containers/VMs. Permission system disabled in environments where mistakes have real consequences.

**Cause:** Permission fatigue; speed-over-safety in non-sandboxed environments.

**Fix:** Sandboxing for local autonomy. Auto mode with classifier for trusted infrastructure (Anthropic auto-mode reduces ~93% of permission prompts via classifier-based approval). `bypassPermissions` only in throwaway environments — containers, ephemeral VMs, scratch directories. Document the reasoning in settings comments so future contributors don't widen the scope unintentionally.

### 4.8 Missing managed policy where required `[CC]`

**Signature:** Compliance-sensitive context (regulated industry, enterprise) but no managed policy CLAUDE.md or settings; security rules only in project-level or user-level files. Project-level rules can be weakened by individual contributors; managed policy cannot.

**Cause:** Unfamiliarity with managed policy hierarchy; assumption that project-level rules are enforceable as ceiling.

**Fix:** Identify rules requiring ceiling-level enforcement. Deploy to managed policy location. Use `claudeMdExcludes` for monorepo cleanup. Settings hierarchy: managed policy → CLI flags → local project → user. Higher-priority settings override lower-priority — use this to deploy organizational guarantees that project-level configs cannot weaken.

### 4.9 Path-scoped rules opportunity missed `[CC]`

**Signature:** CLAUDE.md contains rules like "for files in `src/api/**`, do X" or per-directory conventions baked into one document. CLAUDE.md grows beyond the 200-line target due to per-path content.

**Cause:** CLAUDE.md predates `.claude/rules/` with path-scoped frontmatter; not yet migrated. Or the team is unaware of the path-scoped mechanism.

**Fix:** Extract per-path rules into `.claude/rules/{name}.md` files with `paths:` frontmatter. CLAUDE.md becomes lighter; rules load on demand only when matching files are read. The per-path rule reaches the agent in the right context, not as always-loaded standing context.

### 4.10 Auto memory misuse `[CC]`

**Signature:** Important team conventions or project decisions in `~/.claude/projects/<project>/memory/MEMORY.md` (machine-local) instead of in version-controlled CLAUDE.md.

**Cause:** Letting Claude's auto memory write team-relevant content; not realizing auto memory is machine-local. Convenience of auto memory's automatic capture vs. the discipline of explicit CLAUDE.md updates.

**Fix:** Audit auto memory periodically. Promote team-relevant entries to CLAUDE.md (where the team can see them). Leave only personal preferences and cross-project habits in auto memory.

**Related:** §2.2 Layer hierarchy violation (the broader cross-surface pattern).

### 4.11 Verification-before-completion absent `[CC]`

**Signature:** CC outputs use speculative language ("should work," "probably fine," "looks good"); no test runs before declaring task complete; no Stop hook blocking completion without test evidence.

**Cause:** Default Claude Code behavior drifts toward implementation-first when verification gates aren't enforced. Without explicit gates, the "trust-then-verify gap" emerges — the agent declares completion based on its own judgment rather than concrete evidence.

**Fix:** Install verification-before-completion as a Skill or hook. Add Stop hook blocking completion without test evidence. Ban speculative language in Skill prompts and CLAUDE.md (specify "do not declare complete without test results showing pass" rather than "verify your work"). The verification iron law: no completion without evidence.

### 4.12 Skills/Commands legacy mix `[CC]`

**Signature:** Both `.claude/commands/` and `.claude/skills/` directories present with overlapping content; team confusion about which mechanism to use; some workflows in commands, others in Skills, no clear migration plan.

**Cause:** Migration to Skills incomplete; legacy commands still in place.

**Fix:** Migrate `.claude/commands/` content to `.claude/skills/` with appropriate frontmatter (use `disable-model-invocation: true` for previously manual-only commands that should remain explicit). Delete `.claude/commands/` once migrated. Document the mechanism choice in CLAUDE.md so future contributors don't recreate the legacy pattern.

### 4.13 Kitchen-sink session (operational) `[CC]`

**Signature:** Single CC sessions spanning 100+ turns mixing unrelated tasks; the agent's context is polluted with debugging from one task while working on a different task; never use `/clear` or `/compact`.

**Cause:** Habit of keeping one terminal session open for multiple tasks. Not recognizing that context pollution from prior tasks degrades performance on current task.

**Fix:** `/clear` between unrelated tasks. Subagents for side investigations (their isolated context window prevents pollution). Named sessions (`claude --continue` with descriptive names) for distinct workstreams. `/compact` periodically when sessions accumulate large but mostly-irrelevant history.

**Note:** This is a different pattern from CP's structural Kitchen Sink (§3.4). The structural pattern is about how content is organized; this operational pattern is about how sessions are managed. Same name, different failure mode.

### 4.14 Stale CLAUDE.md `[CC]`

**Signature:** CLAUDE.md last modified months ago; references tools/files/patterns that no longer exist; rules contradicted by current codebase. Engine state snapshot section claims old version numbers, old test counts, old halt-violation counts. The agent reads CLAUDE.md cold and inherits incorrect orientation.

**Cause:** CLAUDE.md treated as set-and-forget, not as evolving context.

**Fix:** Audit CLAUDE.md against current codebase. Remove dead references. Date-stamp the file at every meaningful update. Quarterly audit as part of repo hygiene (the `rootnode-repo-hygiene` Skill detects this). For deployments with auto-updated state sections, ensure the auto-update mechanism is functioning — a snapshot section that hasn't updated in months is worse than no snapshot.

---

## 5. Cross-surface mapping table

For users navigating between surfaces or designing patterns that need to apply both, this table maps related patterns across CP and CC.

| Pattern | CP version | CC version | Relationship |
|---|---|---|---|
| Monolithic standing context | Monolith (§2.1, CI/KF manifestation) | CLAUDE.md Bloat (`root_CC_ENVIRONMENT_GUIDE.md §2.4`) | Same structural pattern, different artifact. Both violate the lean-over-comprehensive principle. |
| Layer hierarchy violation | Misaligned Hierarchy (§2.2, precedence chain across CP layers) | §4.10 Auto memory misuse (specific instance: machine-local content that should be team-shared) | CP version is general; CC version is one specific manifestation. Both violate placement discipline. |
| Transcript-as-context | §3.1 Phantom Conversation (CI references past chats) | §4.1 Transcript dump (handoff/onboarding as chat history) | Same root cause: chat as source of truth instead of files. Different surface manifestations. |
| Mixing rules with reference | §3.5 Blurred Layers (CI mixes behavioral guidance with explanatory depth) | CLAUDE.md Bloat (`root_CC_ENVIRONMENT_GUIDE.md §2.4`, when bloat includes reference material) | CP version is named distinctly; CC version is one symptom of CLAUDE.md Bloat. Both violate file-purpose discipline. |
| Component carrying multiple concerns | §3.4 Kitchen Sink (CI/KF mixes unrelated concerns) | §4.13 Kitchen-sink session (operational, not structural) | **Different patterns despite similar name.** CP version is about how content is organized in artifacts; CC version is about how sessions are managed. Don't confuse. |
| Artifact exists but doesn't reach agent | §3.3 Orphan File (KF nothing references) | §4.3 Manual-only Skills (with weak descriptions that don't auto-activate) | Different mechanisms; same structural failure. Both indicate routing/activation gaps. |

CP-only patterns with no CC analog: Phantom Conversation (per the table), Echo Chamber (CI/KF duplication is CP-specific because CC's CLAUDE.md and references aren't structured the same way), §3.6 Build-scaffolding leak (specific to user-facing artifact frontmatter conventions, primarily Skills and Projects).

CC-only patterns with no CP analog: §4.2 MCP bloat, §4.4 Enforcement-as-preference, §4.5 / §4.6 Subagent overuse / underuse, §4.7 `bypassPermissions` outside sandbox, §4.8 Missing managed policy, §4.9 Path-scoped rules opportunity missed, §4.11 Verification-before-completion absent, §4.12 Skills/Commands legacy mix, §4.14 Stale CLAUDE.md. These all depend on CC mechanisms (hooks, subagents, settings hierarchy, MCP, path-scoped rules) that don't exist on the CP surface.

---

## 6. Behavioral anti-patterns reference

The patterns above are *structural* — they describe how content is organized. There is a parallel catalog of *behavioral* anti-patterns describing how the agent itself behaves under specific deployment conditions. Behavioral patterns include:

- Agreeableness (output-content + persistent-preference)
- Hedging
- Verbosity
- List overuse
- Fabricated precision
- Over-exploration
- Tool miscalibration (over- and under-triggering)
- LaTeX defaulting
- Editorial drift
- Self-referential fabrication

These are documented in detail in `root_OPTIMIZATION_REFERENCE.md` (Behavioral Tendencies section) with countermeasure templates. They are surface-aware — some surface more in CP (hedging, list overuse, agreeableness on creative work), others more in CC (over-exploration, tool over-triggering, fabricated precision in code claims, verification-before-completion absence).

When auditing a deployment, check both catalogs: this KF for structural patterns; `root_OPTIMIZATION_REFERENCE.md` for behavioral patterns. Most deployment friction traces to one or both.

---

## 7. Catalog consumption pattern (for audit/sweep Skills)

Skills that audit or sweep deployments against this catalog (`rootnode-repo-hygiene` for CC-side hygiene sweeps, `rootnode-cc-design` REMEDIATE for closing the loop on CC-side findings, `rootnode-project-audit` for CP-side audits, future audit Skills) consume the catalog through a structured mapping. The pattern documented here is the canonical structure that audit Skills follow when surfacing findings.

### 7.1 The sweep-category mapping table

Audit Skills carry an internal mapping from their sweep categories (the operational units they scan against) to the canonical anti-patterns in this KF. The mapping table is the contract between the audit Skill and this catalog — it tells reviewers which sweep categories correspond to which canonical patterns and at what surface.

**Structure (canonical form).**

| Cat ID | Sweep category | Canonical AP reference | Surface | Routing |
|---|---|---|---|---|
| `Cat N` | Audit-Skill-internal name | `root_AGENT_ANTI_PATTERNS.md §X.Y` | `[CP]` / `[CC]` / `[both]` | Where the finding routes (Phase 2 cleanup, REMEDIATE, etc.) |

Each row anchors a sweep category to a canonical pattern by section reference (`§X.Y`), tags the surface, and specifies the routing destination (which Skill consumes the finding for resolution).

**Why this structure matters.** Without explicit mapping, audit Skills drift from the canonical catalog over time — a sweep category gets renamed, a new sweep category is added without a canonical anchor, two sweep categories collapse into one without updating the canonical reference. The mapping table makes drift visible. When the canonical catalog evolves (new pattern added, existing pattern renumbered), the audit Skills' mapping tables are the propagation hooks.

**When an audit Skill authors this table.** Any Skill that scans a deployment and surfaces structured findings against the catalog. Examples: rootnode-repo-hygiene scans for 14 categories of CC-environment hygiene issues; rootnode-cc-design REMEDIATE consumes the report and routes findings by category. Both Skills carry mapping tables that anchor their categories to this KF's canonical patterns.

**When an audit Skill does NOT author this table.** Skills that don't scan deployments don't need the mapping (e.g., rootnode-prompt-validation scores a single prompt; it doesn't sweep a deployment against the catalog). Skills that consume audit findings without re-categorizing them don't need a mapping (they read the Producer Skill's findings directly).

### 7.2 Cross-Skill alignment

Multiple audit Skills mapping to the same canonical pattern must agree on the surface tag and routing. If `rootnode-repo-hygiene` tags pattern §4.4 (Enforcement-as-preference) as `[CC]` with routing to Phase 2 cleanup, no other audit Skill should map a category to §4.4 with a different surface tag or different routing. Disagreement signals either (a) a missed surface-invariant pattern that should be re-categorized as `[both]` in the canonical catalog, or (b) genuine taxonomy drift between Skills that needs reconciliation. Both cases warrant a methodology evolution session — surface to `root_build_context.md`.

### 7.3 Where the per-Skill mapping lives

Per-Skill mapping tables live in the Skill's `references/sweep-categories.md` (or equivalent — Skill authors choose the filename). The table is a reference file, not part of SKILL.md, because it's lookup data rather than build instructions. SKILL.md cites the reference: "For the full sweep-category-to-canonical-pattern mapping, see references/sweep-categories.md."

### 7.4 The catalog itself never carries the reverse mapping

This KF does not maintain a "patterns → which audit Skills detect them" reverse index. The catalog is the source of truth; audit Skills are downstream consumers. Maintaining a reverse index in the catalog would create dual-source-of-truth drift. When checking which audit Skills scan for a given pattern, walk the audit Skills' mapping tables — they are the authoritative answer.

---

## 8. Source attribution

The patterns in this catalog come from production validation across multiple deployments. Source authority by tier (per `root_AGENT_ENVIRONMENT_ARCHITECTURE.md` §4.4):

- **Tier 1 (Anthropic primary documentation):** the existence of mechanisms (hooks, path-scoped rules, settings hierarchy, MCP) and their authority profiles. Source for what the layers are and how they enforce.
- **Tier 2 (Anthropic engineering posts):** design rationale for the placement discipline; emerging patterns around auto memory, deferred tool loading, sandboxing, auto mode. Source for why the layers exist and how they're intended to compose.
- **Tier 3 (Tested production experience):** the structural patterns themselves, validated across deployments. Source for which patterns surface most often in real audits, which fixes work, which fixes fail.
- **Tier 4 (Named practitioners):** cross-validation from public artifacts — Simon Willison's Skills writeup, Anthropic engineering team patterns, multiple practitioner repositories with documented anti-pattern observations. Source for community calibration.
- **Tier 5 (Community sources):** signal-only. Patterns that surfaced via Discord, Reddit, or Twitter without independent validation are not in this catalog. They become candidates for future addition if they accumulate Tier 3 or Tier 4 grounding.

Catalog evolution: new patterns are added when they surface in 3+ independent deployments OR when a named practitioner publishes a documented case. Removed patterns are ones that prove non-recurring in subsequent audit cycles. Maintenance happens through methodology evolution sessions; new patterns are documented in `root_build_context.md` with their grounding.

---

## 9. Where to go next

For the architectural principles the patterns violate: `root_AGENT_ENVIRONMENT_ARCHITECTURE.md`.

For surface-specific application:
- CP-side: `root_PROJECT_ARCHITECTURE_GUIDE.md` (also contains a CP-focused anti-pattern appendix that overlaps with this catalog).
- CC-side: `root_CC_ENVIRONMENT_GUIDE.md` (§9 references this catalog for the CC-side patterns).

For behavioral patterns and countermeasure templates: `root_OPTIMIZATION_REFERENCE.md`.

For audit methodology that uses this catalog: `root_AUDIT_FRAMEWORK.md` (Anti-Pattern Checklist section). The Audit Framework's checklist will be updated to reference this unified catalog rather than maintaining a separate seven-pattern list — see `root_build_context.md` for the migration status.

For Skill build discipline (where audit Skills' sweep-category mappings are authored, and where the Skill-relevant subset of this catalog is scanned during build quality gate D7): `root_SKILL_BUILD_DISCIPLINE.md`.

For navigation: `root_CONTENTS_INDEX.md`.

---

*End of root_AGENT_ANTI_PATTERNS.md.*
