# Context File Pattern: Identity, Triggers, Pointers

**Layer**: layer_0 (Universal)
**Type**: Scenario-Based Rule
**Applies When**: Creating CLAUDE.md, 0AGNOSTIC.md, or any AI context file

---

## Purpose

Define the minimal, context-efficient pattern for AI context files (CLAUDE.md, 0AGNOSTIC.md, etc.). The goal is to give the AI enough to avoid "amnesia" while minimizing token usage per request.

---

## The Pattern: Identity, Triggers, Pointers

Every context file should contain three types of content:

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

## Token Budget Guidelines

| Section | Target | Max |
|---------|--------|-----|
| Identity | 50-100 | 150 |
| Triggers | 100-200 | 300 |
| Pointers | 50-100 | 150 |
| **Total** | **200-400** | **600** |

If your context file exceeds 600 tokens, refactor content into skills.

---

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

## Related Rules

- `OUTPUT_FIRST_PROTOCOL.md` - Session continuity
- `LOCATION_RULE_APPLICATION_PROTOCOL.md` - Applying rules to locations
