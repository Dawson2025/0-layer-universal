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

<!-- section_id: "f0010ca0-5d8d-4bb6-b999-14e4436b94a6" -->
## Purpose

When user says "I want X to happen for every API request at location Y", this protocol defines how to make that rule permanent at that location.

---

<!-- section_id: "b52048da-fba7-4d14-ae19-a69b65ec4b80" -->
## The Rule

**When user requests a location-specific rule:**

1. **Identify the location** (layer, stage, feature, etc.)
2. **Update CLAUDE.md** at that location with the rule
3. **Update .claude/** at that location if needed (skills, hooks, etc.)
4. **Confirm changes** with user per AI Context Modification Protocol

---

<!-- section_id: "356d046a-9779-4aab-b066-e85e17475cc0" -->
## What to Update

<!-- section_id: "384833ec-aeb6-4466-8656-c3935e4cc70e" -->
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

<!-- section_id: "059ee992-5138-44fd-bc20-d3dc6b237b72" -->
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

<!-- section_id: "b040c3f0-9ec0-4590-abde-9cb882d92030" -->
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

<!-- section_id: "c732a97b-449f-481c-a281-da2799e2d207" -->
## Decision Matrix

| Rule Type | Update CLAUDE.md? | Create Skill? | Create Hook? |
|-----------|-------------------|---------------|--------------|
| Always-on (LLM decides) | ✅ Yes | ❌ No | ❌ No |
| On-demand (user/LLM invokes) | ⚠️ Reference | ✅ Yes | ❌ No |
| Automated (must happen) | ❌ No | ❌ No | ✅ Yes |
| Hybrid | ✅ Yes | ⚠️ Maybe | ⚠️ Maybe |

---

<!-- section_id: "2f9bcbb6-c98e-44ab-8752-65f760350e42" -->
## Examples

<!-- section_id: "7259c78d-09d4-4f46-a267-cf4a87d8debf" -->
### Example 1: Output-First Protocol

User: "I want outputs written to files before responding, at this research stage"

**Action**: Update CLAUDE.md with mandatory section:
```markdown
## [MANDATORY] Output-First Protocol
...
```

<!-- section_id: "d9b72ddf-6548-4b1b-b1d9-9361c1030608" -->
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

<!-- section_id: "fca78779-1bcd-4be0-ac97-fa324472413b" -->
### Example 3: Security Review Before Commit

User: "I want security review before any commit at this project"

**Action**: Create skill + update CLAUDE.md:
```markdown
## Before Committing
Always run `/security-review` skill before any git commit.
```

---

<!-- section_id: "53d61933-24e8-4e25-9db9-16d987e1b9cd" -->
## Scope Inheritance

Rules can be applied at different scopes:

| Scope | Location | Inherited By |
|-------|----------|--------------|
| Universal | `layer_0/.../sub_layer_0_04_rules/` | Everything |
| Project | `layer_1/[project]/CLAUDE.md` | All features/components |
| Feature | `layer_1/[feature]/CLAUDE.md` | All components |
| Stage | `stage_XX/CLAUDE.md` | Only that stage |

---

<!-- section_id: "e9c537e7-9cd0-476f-9f5d-62c825413352" -->
## Related Rules

- `OUTPUT_FIRST_PROTOCOL.md` - Example of a location-specific rule
- `AI_CONTEXT_MODIFICATION_PROTOCOL.md` - How to modify AI context files
