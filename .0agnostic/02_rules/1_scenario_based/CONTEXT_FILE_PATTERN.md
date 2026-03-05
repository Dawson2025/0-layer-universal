---
resource_id: "f8551fa4-037f-45e4-bf45-90b53ecc07a7"
resource_type: "rule"
resource_name: "CONTEXT_FILE_PATTERN"
---
# Context File Pattern: Identity, Triggers, Pointers

**Layer**: layer_0 (Universal)
**Type**: Scenario-Based Rule
**Applies When**: Creating CLAUDE.md, 0AGNOSTIC.md, or any AI context file

---

<!-- section_id: "8f41d8b5-80b8-4304-9eee-f7da1daaf0ff" -->
## Purpose

Define the minimal, context-efficient pattern for AI context files (CLAUDE.md, 0AGNOSTIC.md, etc.). The goal is to give the AI enough to avoid "amnesia" while minimizing token usage per request.

---

<!-- section_id: "b9ac1e42-8c8e-43ee-8678-24b705997ac9" -->
## The Pattern: Identity, Triggers, Pointers

Every context file should contain three types of content:

<!-- section_id: "1cf1eee9-b8aa-4d62-b89f-e606a5549326" -->
### 1. Identity (~50-100 tokens)
**What the AI needs to know about itself at this location.**

```markdown
## Identity

You are an agent at **Layer X** (Purpose), **Stage Y** (Purpose).

- **Role**: [What this agent does]
- **Scope**: [What it can/cannot do]
- **Parent**: `../0AGNOSTIC.md`
- **Children**: `[child]/0AGNOSTIC.md`
```

<!-- section_id: "1d9a6342-2b76-4986-b598-afa693f329d5" -->
### 2. Triggers (~100-200 tokens)
**When/where/what conditions invoke specific behaviors.**

```markdown
## Triggers

### Escalate UP When
- Task outside scope
- Need higher authority
- Cross-layer coordination

### Delegate DOWN When
- Task belongs to child
- Specialized handling needed

### Use Skill When
| Condition | Skill |
|-----------|-------|
| Starting research | `/research-workflow` |
| Creating handoff | `/handoff-protocol` |
| Need domain knowledge | `/domain-knowledge` |
```

<!-- section_id: "f151ed15-c424-48ad-a205-7aeeb794681d" -->
### 3. Pointers (~50-100 tokens)
**Where to find detailed instructions (loaded on-demand).**

```markdown
## Skills Available

| Skill | Purpose |
|-------|---------|
| `/workflow` | Detailed workflow steps |
| `/standards` | Coding standards |
| `/handoff` | Communication protocol |

## Key Locations

| Content | Path |
|---------|------|
| Outputs | `outputs/` |
| Handoffs | `hand_off_documents/` |
| Skills | `.0agnostic/skills/` |
```

---

<!-- section_id: "51bcaaaf-fc31-4d27-adfa-a8dc959f6fca" -->
## What NOT to Put in Context Files

These belong in **skills** (loaded on-demand), not in the always-loaded context file:

| Content | Why Not | Where Instead |
|---------|---------|---------------|
| Step-by-step procedures | Too many tokens | `skills/[name]/SKILL.md` |
| Templates | Rarely needed every request | `skills/[name]/references/` |
| Full coding standards | Only needed when coding | `skills/standards/SKILL.md` |
| Detailed examples | Context-heavy | `skills/[name]/references/` |
| Historical context | Rarely relevant | `.0agnostic/episodic_memory/` |

---

<!-- section_id: "eca2e1e7-d5cb-4bc4-8d62-3472caee1259" -->
## Token Budget Guidelines

| Section | Target | Max |
|---------|--------|-----|
| Identity | 50-100 | 150 |
| Triggers | 100-200 | 300 |
| Pointers | 50-100 | 150 |
| **Total** | **200-400** | **600** |

If your context file exceeds 600 tokens, refactor content into skills.

---

<!-- section_id: "ffad7596-11f6-4cec-bffd-e1d0993cfaf3" -->
## Example: Minimal Context File

```markdown
# 0AGNOSTIC.md - Layer 1, Feature X

## Identity
You are at Layer 1 (Projects), Feature X (Authentication).
- **Role**: Implement auth features
- **Scope**: Auth code only, no infrastructure
- **Parent**: `../0AGNOSTIC.md`

## Triggers
- **Escalate**: Infrastructure needs, security decisions
- **Delegate**: None (leaf)
- **Skills**: `/auth-patterns` for implementation, `/testing` for tests

## Pointers
| Need | Location |
|------|----------|
| Workflow | `/feature-workflow` skill |
| Standards | `/coding-standards` skill |
| Outputs | `outputs/` |
```

**~150 tokens** - Enough for identity, knows when to use skills, no wasted context.

---

<!-- section_id: "eeec91bf-dd92-4391-bcd0-55af83244a83" -->
## Skill Structure (Official Pattern)

From the official skill-creator, skills support:

```
.0agnostic/skills/[skill-name]/
├── SKILL.md           # Required - instructions (loaded when skill invoked)
├── scripts/           # Optional - executable code
├── references/        # Optional - docs loaded into context as needed
└── assets/            # Optional - templates, icons, fonts
```

- **SKILL.md**: Frontmatter + instructions, loaded when skill is invoked
- **references/**: Detailed docs, only loaded when Claude reads them
- **scripts/**: Automation, only run when needed
- **assets/**: Output templates, never auto-loaded

---

<!-- section_id: "3d4fe496-7a7c-41e8-9684-30ff0bc433b7" -->
## Related Rules

- `OUTPUT_FIRST_PROTOCOL.md` - Session continuity
- `LOCATION_RULE_APPLICATION_PROTOCOL.md` - Applying rules to locations
