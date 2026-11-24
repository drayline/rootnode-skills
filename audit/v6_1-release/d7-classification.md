# D7 classification — absolutes in emitted text (catalog v6.1)

Spec: `design/root_DESIGN_fable_5_2_alignment.md` v1.0, D7, §7.6 item 6 and §7.7 (behavioral-tuning row). Scope: text that `cc-design` and `behavioral-tuning` **emit into user artifacts** — the CLAUDE.md template, session-prompt and autonomous-prompt blocks, delegation brief text, the brief interview, and countermeasure templates. Skill-internal prose is out of scope; the catalog-wide sweep waits for the measurement cycle (spec §7.9).

Rule: keep an absolute for an irreversible action, a safety boundary or a spec rule; otherwise rewrite it as a scoped rule with its reason.

Method: a scan of fenced blocks (and the interview questions, which are quoted prose the Skill asks) in `plugins/rootnode-code/skills/cc-design/**/*.md` and `plugins/rootnode-tuning/skills/behavioral-tuning/**/*.md`, at `07ae3fa` and on the branch. Section A is the spec's literal population (all-caps NEVER / ALWAYS / MUST). Section B extends the scan to any case, because the Fable 5.2 guide says the model treats an instruction containing "never" as absolute whatever its case. Line numbers are on the branch.

## A. Capitalized NEVER / ALWAYS / MUST

| # | File:line | Text | Class | Disposition |
|---|---|---|---|---|
| A1 | `behavioral-tuning/SKILL.md:220` | "When the [Project/system] specifies that a tool MUST be used for a given task type, invoking that tool is mandatory" | Spec rule — a required tool named by the deployment (the catalog's documented #7b exception) | Keep; already scoped to a task type |
| A2 | `behavioral-tuning/references/countermeasure-templates.md:336` | Same sentence as A1 (reference copy) | Spec rule | Keep |
| A3 | `behavioral-tuning/references/countermeasure-templates.md:346` | "For [task type], [tool name] MUST run before producing a response." | Spec rule — scoped to a named tool and task type | Keep |
| A4 | `cc-design/references/cc-methodology-patterns.md` interview question 4 (line 266 at `07ae3fa`) | "What MUST the agent never modify autonomously?" | Neither — a question whose answer becomes the authority list; it asked for absolutes without reasons | Rewritten: "What should the agent not change without asking you, and why? … And which routine steps can it take without asking?" Each constraint is recorded with its reason, and the routine steps become the positive-scope list |

Section A totals (computed from the rows): 4 rows — keep 3, rewrite 1.

## B. Any-case never / always / must in emitted blocks

| # | File:line | Text (excerpt) | Class | Disposition |
|---|---|---|---|---|
| B1 | `behavioral-tuning/SKILL.md:294` | "The conclusion must follow from verified evidence" | Not a prohibition — a standard for the output | Keep |
| B2 | `behavioral-tuning/references/countermeasure-templates.md:429` | Same as B1 | Not a prohibition | Keep |
| B3 | `behavioral-tuning/references/countermeasure-templates.md:503` | "… never via sudo or the system package manager, unless told not to." | Safety boundary, already scoped ("unless told not to") | Keep |
| B4 | `behavioral-tuning/references/countermeasure-templates.md:648` | "… so the next thing never starts." | Descriptive (Anthropic's Opus 5.5 unattended block, verbatim) | Keep |
| B5 | `cc-design/references/cc-environment-design-patterns.md:136` | "Use `Result<T, E>` for fallible operations; never throw." | Example content — a sample project's own coding rule | Keep (illustration of a user's rule, not a cc-design default) |
| B6 | `cc-design/references/cc-environment-design-patterns.md:137` | "Endpoints must include OpenAPI documentation in JSDoc." | Example content | Keep |
| B7 | `cc-design/references/cc-methodology-patterns.md:241` | "`limits: …   # optional; never in prompt text`" | Spec rule (D6), added by this cut | Keep |
| B8 | `cc-design/references/cc-methodology-patterns.md` brief template, Authority constraints (line 249 at `07ae3fa`) | "<what the agent must NOT modify; tier 1 / tier 2 / tier 3 if applicable>" | Neither — a placeholder that invited unscoped absolutes | Rewritten: "<what the agent may not change autonomously, each item with its reason; …>", plus a new "Routine actions that need no approval" section |
| B9 | `cc-design/references/cc-prompt-design-patterns.md:105` | "Verification: <specific commands the agent must run before declaring done>" | Not a prohibition — a placeholder for the check | Keep |
| B10 | `cc-design/references/cc-prompt-design-patterns.md:274` | "… so the next thing never starts." | Descriptive (Anthropic verbatim, as B4) | Keep |
| B11 | `cc-design/references/cc-prompt-design-patterns.md:407` | "… never via sudo or the system package manager, unless told not to." | Safety boundary, scoped (as B3) | Keep |
| B12 | `cc-design/references/cc-session-reports.md:89` | "## Pre-flight — record for the report (report-only; never a halt condition)" | Spec rule — agrees with the stop rule (an observation is not a stop) | Keep |
| B13 | `cc-design/references/cc-skills-and-hooks-composition.md:32` | "Must be seen, but a person or a later gate decides" → advisory check (deterministic, never blocks) | Descriptive — a decision tree for the designer | Keep |
| B14 | `cc-design/references/cc-skills-and-hooks-composition.md:66` | "# kebab-case, max 64 chars, must match folder name" | Spec rule (Agent Skills frontmatter) | Keep |
| B15 | `cc-design/references/cc-skills-and-hooks-composition.md:265` | "# Sourced, never run. … a missing library never blocks." (×2) | Shipped-script copy (`gate-lib.sh`, `shipped:` marker; must match the file byte for byte) | Keep — not editable here |
| B16 | `cc-design/references/cc-skills-and-hooks-composition.md:266` | "# git status must not rewrite the repository's index" | Shipped-script copy | Keep — not editable here |
| B17 | `cc-design/references/cc-skills-and-hooks-composition.md:284` | "# … or a temp fallback; never the repo" | Shipped-script copy | Keep — not editable here |
| B18 | `cc-design/references/cc-skills-and-hooks-composition.md:442` | "# Watch mode … never blocks" | Shipped-script copy (`verify-tests.sh`) | Keep — not editable here |
| B19 | `cc-design/references/cc-skills-and-hooks-composition.md:465` | "# the session count never resets" | Shipped-script copy | Keep — not editable here |
| B20 | `cc-design/references/cc-skills-and-hooks-composition.md:497` | "Never write the evidence file by hand." (CLAUDE.md rule template) | Spec rule and integrity boundary — the gate trusts evidence only because the record script ran the tests (verify-gate design §7.3) | Keep |
| B21 | `cc-design/references/remediate-mode-execution.md:197` | "Use Result<T, E> for fallible operations; never throw." | Example content (as B5) | Keep |

Section B counts occurrences per row; B13 and B15 each hold two. Totals (computed from the rows): 21 rows, 23 occurrences — keep 20 rows, rewrite 1 row (B8).

## Not absolutes but in the same spirit (changed by this cut, for the record)

The session-prompt, autonomous-prompt and delegation templates in `cc-prompt-design-patterns.md` carried an open-ended halt list ("Test failure → HALT", "Ambiguous input from a work item → HALT, do not guess", "Tool unavailable → HALT", "Halt and return early if: … verification fails"). They contain no NEVER / ALWAYS / MUST, but they are emitted caution that §4 of the spec replaces: they now follow the stop rule, work ordinary failures through, and carry a positive-scope list. `cc-methodology-patterns.md` §8's R4 categories dropped "test count drops or test failure" and "regression detected" as halt classes for the same reason.
