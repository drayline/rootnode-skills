# Skills Spec Reference

This document is the authoritative reference for the Agent Skills specification as of March 2026. It is extracted from Anthropic's official "Complete Guide to Building Skills for Claude" and supplemented with patterns observed in production Skills (Anthropic's public skills, partner skills, and the skill-creator).

---

## What Is a Skill

A Skill is a set of instructions — packaged as a simple folder — that teaches Claude how to handle specific tasks or workflows. Skills are one of the most powerful ways to customize Claude for specific needs. Instead of re-explaining preferences, processes, and domain expertise in every conversation, Skills let you teach Claude once and benefit every time.

Skills work identically across Claude.ai, Claude Code, and API. Create a Skill once and it works across all surfaces without modification, provided the environment supports any dependencies the Skill requires.

---

## Folder Structure

```
your-skill-name/
├── SKILL.md          # Required — main skill file
├── scripts/          # Optional — executable code (Python, Bash, etc.)
├── references/       # Optional — documentation loaded as needed
└── assets/           # Optional — templates, fonts, icons used in output
```

### Critical Rules

**SKILL.md naming:** Must be exactly `SKILL.md` (case-sensitive). No variations accepted (`SKILL.MD`, `skill.md`, etc.).

**Skill folder naming:** Use kebab-case only. No spaces, no underscores, no capitals.
- Correct: `notion-project-setup`
- Wrong: `Notion Project Setup`, `notion_project_setup`, `NotionProjectSetup`

**No README.md:** Do not include `README.md` inside the skill folder. All documentation goes in SKILL.md or `references/`. A repo-level README for human visitors is separate from the skill folder itself.

**Skills named with "claude" or "anthropic" are reserved** and will be rejected.

---

## YAML Frontmatter

The YAML frontmatter is how Claude decides whether to load a Skill. This is the first level of progressive disclosure — always loaded in Claude's system prompt for all enabled skills.

### Required Fields

```yaml
---
name: your-skill-name
description: What it does. Use when user asks to [specific phrases].
---
```

**`name`** (required):
- Kebab-case only
- Max 64 characters
- No spaces or capitals
- Must match folder name
- No leading or trailing hyphens

**`description`** (required):
- Max 1024 characters
- MUST include BOTH: what the skill does AND when to use it (trigger conditions)
- No XML angle brackets (`<` or `>`) — security restriction, as frontmatter appears in Claude's system prompt
- Include specific task phrases users would actually say
- Mention file types if relevant

### Optional Fields

**`license`**: Use if making skill open source. Common values: `MIT`, `Apache-2.0`.

**`compatibility`**: 1-500 characters. Indicates environment requirements (intended product, required system packages, network access needs).

**`metadata`**: Any custom key-value pairs. Suggested: `author`, `version`, `mcp-server`.

```yaml
metadata:
  author: rootnode
  version: "1.0"
  original-source: AUDIT_FRAMEWORK.md
```

---

## Progressive Disclosure Model

Skills use a three-level loading system to minimize token usage while maintaining specialized expertise:

### Level 1 — Metadata (Always Loaded)
The YAML frontmatter (`name` + `description`) is always present in Claude's system prompt for all enabled skills. This is approximately 100 words. It provides just enough information for Claude to know when each skill should be used without loading the full body.

### Level 2 — SKILL.md Body (Loaded on Activation)
The full SKILL.md body is loaded when Claude determines the skill is relevant to the current task. Contains the complete instructions and guidance. Recommended: under 500 lines, under ~5000 tokens.

### Level 3 — Linked Files (Loaded on Demand)
Additional files in `scripts/`, `references/`, and `assets/` directories. Claude navigates to and reads these only as needed. Scripts can execute without being loaded into context. Reference files are read into context when Claude needs detailed documentation.

### Key Patterns

- Keep SKILL.md under 500 lines. If approaching this limit, add hierarchy and clear pointers to reference files.
- Reference files clearly from SKILL.md with guidance on when to read them.
- For large reference files (>300 lines), include a table of contents at the top.
- Domain organization: when a skill supports multiple variants, organize references by variant so Claude reads only the relevant one.

```
cloud-deploy/
├── SKILL.md (workflow + selection logic)
└── references/
    ├── aws.md
    ├── gcp.md
    └── azure.md
```

---

## Writing Effective Descriptions

The description field is the activation trigger. Claude decides whether to load a Skill based almost entirely on this field. Getting this right is the single most important task.

### Structure

```
[What it does] + [When to use it] + [Key capabilities]
```

### Good Examples

```yaml
# Specific and actionable
description: Analyzes Figma design files and generates developer handoff documentation. Use when user uploads .fig files, asks for "design specs", "component documentation", or "design-to-code handoff".

# Includes trigger phrases
description: Manages Linear project workflows including sprint planning, task creation, and status tracking. Use when user mentions "sprint", "Linear tasks", "project planning", or asks to "create tickets".

# Clear value proposition
description: End-to-end customer onboarding workflow for PayFlow. Handles account creation, payment setup, and subscription management. Use when user says "onboard new customer", "set up subscription", or "create PayFlow account".
```

### Bad Examples

```yaml
# Too vague — will never activate
description: Helps with projects.

# Missing triggers — Claude doesn't know when to use it
description: Creates sophisticated multi-page documentation systems.

# Too technical, no user triggers
description: Implements the Project entity model with hierarchical relationships.
```

### Undertriggering Bias

Claude currently has a tendency to undertrigger Skills — to not use them when they would be useful. To combat this, make descriptions slightly "pushy." Include trigger phrases that cover both explicit and implicit user requests. For example, instead of just listing the primary function, add phrases like "Use this skill whenever the user mentions [X], [Y], or [Z], even if they don't explicitly ask for [specific term]."

### Negative Triggers

When a Skill risks overtriggering, add explicit negative triggers:

```yaml
description: Advanced data analysis for CSV files. Use for statistical modeling, regression, clustering. Do NOT use for simple data exploration (use data-viz skill instead).
```

---

## Writing the SKILL.md Body

### Recommended Structure

```markdown
---
name: your-skill
description: [What + When + Capabilities]
---

# Your Skill Name

## Instructions

### Step 1: [First Major Step]
Clear explanation of what happens.
[Add more steps as needed]

## Examples

### Example 1: [Common Scenario]
User says: "[trigger phrase]"
Actions:
1. [Step]
2. [Step]
Result: [What success looks like]
[Add more examples as needed]

## Troubleshooting

**Error: [Common error or failure mode]**
Cause: [Why it happens]
Solution: [How to fix]
```

### Writing Principles

**Be specific and actionable.** Prefer concrete instructions over vague guidance.
- Good: `Run python scripts/validate.py --input {filename} to check data format.`
- Bad: `Validate the data before proceeding.`

**Use imperative form.** Direct instructions, not suggestions.

**Include error handling.** Document common failure modes and their solutions.

**Reference bundled resources clearly.** When referring to files in `references/`, state what the file contains and when to consult it.

**Critical instructions at the top.** Put the most important rules and behaviors early in the document. Use `## Important` or `## Critical` headers for must-follow rules.

---

## Distribution

### Current Model (March 2026)

**Individual users:**
1. Download the skill folder
2. Zip the folder (if needed)
3. Upload to Claude.ai via Settings > Capabilities > Skills
4. Or place in Claude Code skills directory

**Organization-level skills:**
- Admins can deploy skills workspace-wide
- Automatic updates
- Centralized management

**API access:**
- `/v1/skills` endpoint for listing and managing skills
- Add skills to Messages API requests via the `container.skills` parameter
- Works with the Claude Agent SDK for building custom agents
- Requires the Code Execution Tool beta

**GitHub distribution (recommended):**
- Public repo for open-source skills
- Clear repo-level README with installation instructions (separate from skill folders)
- Example usage and screenshots
- Link to related documentation

### Open Standard

Agent Skills is published as an open standard — portable across tools and platforms. Skills designed for specific platform capabilities can note this in the `compatibility` field.

---

## Testing Criteria

### Triggering Tests
- Triggers on obvious tasks (direct requests matching the skill's domain)
- Triggers on paraphrased requests (same intent, different wording)
- Does NOT trigger on unrelated topics

### Functional Tests
- Valid outputs generated
- Error handling works
- Edge cases covered

### Performance Comparison
- Without skill: how many messages, tool calls, tokens, errors?
- With skill: improvement on all dimensions?

### Quantitative Targets (Aspirational)
- 90%+ trigger accuracy on relevant queries
- 0 failed API calls per workflow
- Consistent results across sessions

### Debugging Activation

Ask Claude: "When would you use the [skill name] skill?" Claude will quote the description back. Adjust based on what's missing.

---

## Common Problems

**Skill doesn't trigger:** Description too vague. Add specific trigger phrases and user intent language. Check that the description includes both what AND when.

**Skill triggers too often:** Description too broad. Add negative triggers, be more specific about scope.

**Instructions not followed:** Instructions may be too verbose (keep concise, use lists), buried (critical instructions at top), or ambiguous (replace vague language with specific checks).

**Large context issues:** SKILL.md too large. Move detailed docs to `references/`. Keep SKILL.md under 500 lines / ~5000 tokens.

---

## Skill Categories

Anthropic identifies three common use case categories:

**Category 1 — Document & Asset Creation:** Creating consistent, high-quality output (documents, presentations, apps, designs, code). No external tools required — uses Claude's built-in capabilities. Key techniques: embedded style guides, template structures, quality checklists.

**Category 2 — Workflow Automation:** Multi-step processes benefiting from consistent methodology. Key techniques: step-by-step workflows with validation gates, templates, iterative refinement loops.

**Category 3 — MCP Enhancement:** Workflow guidance enhancing tool access from an MCP server. Key techniques: coordinated multi-tool sequences, embedded domain expertise, context provision, error handling.
