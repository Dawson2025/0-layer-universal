---
resource_id: "80a14aa3-86e3-460e-8254-c9f6bb84e6e4"
resource_type: "knowledge"
resource_name: "CONTEXT_FILE_PATTERN"
---
# Context File Pattern: Identity, Triggers, Pointers

**Layer**: layer_0 (Universal)
**Type**: Scenario-Based Rule
**Applies When**: Creating CLAUDE.md, 0AGNOSTIC.md, or any AI context file

---

<!-- section_id: "916aae9b-fb26-4793-8ef5-13e539b01b6a" -->
## Purpose

Define the minimal, context-efficient pattern for AI context files (CLAUDE.md, 0AGNOSTIC.md, etc.). The goal is to give the AI enough to avoid "amnesia" while minimizing token usage per request.

---

<!-- section_id: "97af1b3b-b1e8-4d5a-b175-e9cdd50f4812" -->
## The Pattern: Identity, Triggers, Pointers

Every context file should contain three types of content:

<!-- section_id: "9106422d-5be9-4f97-89a8-5aa59f9a0ad2" -->
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

<!-- section_id: "5a94cfb2-0436-4bd7-b18f-bd634e9fa9bb" -->
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

<!-- section_id: "dd9368e8-6ef1-4259-a6f4-f3e52eeef950" -->
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

<!-- section_id: "02efb5b9-fe79-4bdf-a2ed-ccff5945c5d1" -->
## What NOT to Put in Context Files

These belong in **skills** (loaded on-demand), not in the always-loaded context file:

| Content | Why Not | Where Instead |
|---------|---------|---------------|
| Step-by-step procedures | Too many tokens | `skills/[name]/SKILL.md` |
| Templates | Rarely needed every request | `skills/[name]/references/` |
| Full coding standards | Only needed when coding | `skills/standards/SKILL.md` |
| Detailed examples | Context-heavy | `skills/[name]/references/` |
| Historical context | Rarely relevant | `outputs/episodic/` |

---

<!-- section_id: "b2ecb278-46ed-437f-8ad9-5d302f68ca3f" -->
## Token Budget Guidelines

| Section | Target | Max |
|---------|--------|-----|
| Identity | 50-100 | 150 |
| Triggers | 100-200 | 300 |
| Pointers | 50-100 | 150 |
| **Total** | **200-400** | **600** |

If your context file exceeds 600 tokens, refactor content into skills.

---

<!-- section_id: "29581372-8e3e-4c37-be5a-c4a0dc4fc86d" -->
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

<!-- section_id: "30a226a2-37c7-43f4-8b58-93958b2ad444" -->
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

<!-- section_id: "f68c752c-99be-4ea5-9647-5700ac4ad092" -->
## Related Rules

- `OUTPUT_FIRST_PROTOCOL.md` - Session continuity
- `LOCATION_RULE_APPLICATION_PROTOCOL.md` - Applying rules to locations
