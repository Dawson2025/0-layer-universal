---
resource_id: "88e3a56f-b65d-4185-854d-15e5983f0ca8"
resource_type: "rule"
resource_name: "LOCATION_RULE_APPLICATION_PROTOCOL"
---
# Location Rule Application Protocol

**Layer**: layer_0 (Universal)
**Type**: Scenario-Based Rule
**Applies When**: User requests a rule be applied "for every API request at location X"

---

<!-- section_id: "29df59d1-da8c-4333-ab25-21c186acc8ab" -->
## Purpose

When user says "I want X to happen for every API request at location Y", this protocol defines how to make that rule permanent at that location.

---

<!-- section_id: "f3ee2b91-0fb2-4c38-a625-2a9eda8cffdc" -->
## The Rule

**When user requests a location-specific rule:**

1. **Identify the location** (layer, stage, feature, etc.)
2. **Update CLAUDE.md** at that location with the rule
3. **Update .claude/** at that location if needed (skills, hooks, etc.)
4. **Confirm changes** with user per AI Context Modification Protocol

---

<!-- section_id: "d62aeb14-da33-4bce-bd8b-8d45494dc72a" -->
## What to Update

<!-- section_id: "f484c0e0-7ffc-4c9c-94c3-a1fa532d3ff5" -->
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

<!-- section_id: "902626a7-2ee7-437f-9299-676a79eab8c4" -->
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

<!-- section_id: "88976460-0e04-4958-905f-9ad4c537eb4a" -->
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

<!-- section_id: "25e5542e-9e14-47e8-896c-1068cd2ec1d5" -->
## Decision Matrix

| Rule Type | Update CLAUDE.md? | Create Skill? | Create Hook? |
|-----------|-------------------|---------------|--------------|
| Always-on (LLM decides) | ✅ Yes | ❌ No | ❌ No |
| On-demand (user/LLM invokes) | ⚠️ Reference | ✅ Yes | ❌ No |
| Automated (must happen) | ❌ No | ❌ No | ✅ Yes |
| Hybrid | ✅ Yes | ⚠️ Maybe | ⚠️ Maybe |

---

<!-- section_id: "08649452-0da3-46ea-9ae0-7081dd804e80" -->
## Examples

<!-- section_id: "3f5e771c-129d-4160-80a2-7024fbe08093" -->
### Example 1: Output-First Protocol

User: "I want outputs written to files before responding, at this research stage"

**Action**: Update CLAUDE.md with mandatory section:
```markdown
## [MANDATORY] Output-First Protocol
...
```

<!-- section_id: "50e81726-1587-4cf5-a17a-85b88e0b6fc6" -->
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

<!-- section_id: "4331420c-28cc-4a63-a1cd-189acfd24dd1" -->
### Example 3: Security Review Before Commit

User: "I want security review before any commit at this project"

**Action**: Create skill + update CLAUDE.md:
```markdown
## Before Committing
Always run `/security-review` skill before any git commit.
```

---

<!-- section_id: "2fb28c9e-dc4e-44fe-a085-2067d9f3cdbf" -->
## Scope Inheritance

Rules can be applied at different scopes:

| Scope | Location | Inherited By |
|-------|----------|--------------|
| Universal | `layer_0/.../sub_layer_0_02_rules/` | Everything |
| Project | `layer_1/[project]/CLAUDE.md` | All features/components |
| Feature | `layer_2/[feature]/CLAUDE.md` | All components |
| Stage | `stage_XX/CLAUDE.md` | Only that stage |

---

<!-- section_id: "4e8284b3-608f-4984-88b9-6d11d0be022f" -->
## Related Rules

- `OUTPUT_FIRST_PROTOCOL.md` - Example of a location-specific rule
- `AI_CONTEXT_MODIFICATION_PROTOCOL.md` - How to modify AI context files
