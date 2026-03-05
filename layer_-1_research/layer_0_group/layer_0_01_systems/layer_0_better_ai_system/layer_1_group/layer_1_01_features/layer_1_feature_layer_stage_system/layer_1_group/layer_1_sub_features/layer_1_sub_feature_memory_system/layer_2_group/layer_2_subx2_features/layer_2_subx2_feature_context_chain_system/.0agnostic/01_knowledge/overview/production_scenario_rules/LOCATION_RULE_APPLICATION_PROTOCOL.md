---
resource_id: "0adff19a-5b91-4d73-9f2b-4ae2c48698ed"
resource_type: "knowledge"
resource_name: "LOCATION_RULE_APPLICATION_PROTOCOL"
---
# Location Rule Application Protocol

**Layer**: layer_0 (Universal)
**Type**: Scenario-Based Rule
**Applies When**: User requests a rule be applied "for every API request at location X"

---

## Purpose

When user says "I want X to happen for every API request at location Y", this protocol defines how to make that rule permanent at that location.

---

## The Rule

**When user requests a location-specific rule:**

1. **Identify the location** (layer, stage, feature, etc.)
2. **Update CLAUDE.md** at that location with the rule
3. **Update .claude/** at that location if needed (skills, hooks, etc.)
4. **Confirm changes** with user per AI Context Modification Protocol

---

## What to Update

### For Always-On Rules (every request)

Add to location's `CLAUDE.md`:

```markdown
## [MANDATORY] Rule Name

**For every API request at this location:**

1. [Action 1]
2. [Action 2]
3. [Action 3]

**Why**: [Reason for rule]
```

### For On-Demand Rules (triggered by condition)

Create skill in location's `.claude/skills/`:

```
.claude/skills/rule-name/
└── SKILL.md
```

Then reference in CLAUDE.md:
```markdown
## Available Skills
- `/rule-name` - [Description]
```

### For Automated Rules (deterministic, every time)

Create hook in location's `.claude/hooks/` or `.claude/settings.json`:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [{ "type": "command", "command": "script.sh" }]
      }
    ]
  }
}
```

---

## Decision Matrix

| Rule Type | Update CLAUDE.md? | Create Skill? | Create Hook? |
|-----------|-------------------|---------------|--------------|
| Always-on (LLM decides) | ✅ Yes | ❌ No | ❌ No |
| On-demand (user/LLM invokes) | ⚠️ Reference | ✅ Yes | ❌ No |
| Automated (must happen) | ❌ No | ❌ No | ✅ Yes |
| Hybrid | ✅ Yes | ⚠️ Maybe | ⚠️ Maybe |

---

## Examples

### Example 1: Output-First Protocol

User: "I want outputs written to files before responding, at this research stage"

**Action**: Update CLAUDE.md with mandatory section:
```markdown
## [MANDATORY] Output-First Protocol
...
```

### Example 2: Auto-Format on Edit

User: "I want code formatted after every edit at this project"

**Action**: Create hook in `.claude/settings.json`:
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [{ "type": "command", "command": "npm run format" }]
      }
    ]
  }
}
```

### Example 3: Security Review Before Commit

User: "I want security review before any commit at this project"

**Action**: Create skill + update CLAUDE.md:
```markdown
## Before Committing
Always run `/security-review` skill before any git commit.
```

---

## Scope Inheritance

Rules can be applied at different scopes:

| Scope | Location | Inherited By |
|-------|----------|--------------|
| Universal | `layer_0/.../sub_layer_0_04_rules/` | Everything |
| Project | `layer_1/[project]/CLAUDE.md` | All features/components |
| Feature | `layer_1/[feature]/CLAUDE.md` | All components |
| Stage | `stage_XX/CLAUDE.md` | Only that stage |

---

## Related Rules

- `OUTPUT_FIRST_PROTOCOL.md` - Example of a location-specific rule
- `AI_CONTEXT_MODIFICATION_PROTOCOL.md` - How to modify AI context files
