---
resource_id: "988a7052-e372-444a-aa39-b571b99aa1ed"
resource_type: "knowledge"
resource_name: "AI_CONTEXT_MODIFICATION_PROTOCOL"
---
# AI Context Modification Protocol

<!-- section_id: "1f9dadab-354a-4795-bbea-26d9c4dc613f" -->
## Rule

Before modifying ANY files within the AI context system (sublayers, stages, rules, prompts, knowledge system), the AI MUST:

1. **Store proposal in registry**
   - Location: `layer_X_00_layer_registry/proposals/YYYY-MM-DD_description/`
   - Create `SUMMARY.md` with full proposal details
   - For multi-layer changes: modular proposals per layer, summary at common parent

2. **Present a DIAGRAM** showing the proposed changes
   - Reference the stored proposal file
   - Show full file paths (not abbreviated)
   - Show before/after state where applicable
   - Summarize content of new files

3. **Wait for explicit user approval**
   - Do not proceed until user confirms
   - User may request modifications to the plan

4. **Proceed with modifications**
   - Follow the approved diagram exactly
   - Report completion when done

5. **Update proposal status**
   - Change status to "Executed" in SUMMARY.md
   - Mark approval checkboxes as complete

<!-- section_id: "50eba360-84a6-40a9-976d-51f074cf8c5d" -->
## Scope

This rule applies to modifications in:

| Path Pattern | Description |
|--------------|-------------|
| `layer_0/` | Universal layer internals |
| `sub_layer_*` | Any sublayer directory |
| `stage_*` | Any stage directory |
| `CLAUDE.md` | Claude context files |
| `*_rules/` | Rules directories |
| `*_prompts/` | Prompts directories |
| `*_knowledge_system/` | Knowledge system directories |
| `status.json` | Stage status files |

<!-- section_id: "1b81126d-6d88-4230-b651-5ac420fa85e6" -->
## Rationale

- **Visibility**: User can see exactly what will change before it happens
- **Control**: User maintains authority over the AI instruction system
- **Intentionality**: Prevents accidental or unintended modifications
- **Auditability**: Creates a clear record of approved changes

<!-- section_id: "61105061-3e2f-4e7e-84d4-0a00cf6aabfb" -->
## Diagram Requirements

The diagram MUST include:

1. **Full paths** - Complete path from root, not abbreviated
2. **File listing** - Show directory structure before and after
3. **Content summary** - Brief description of new file contents
4. **Action type** - Mark files as NEW, UPDATE, or DELETE

<!-- section_id: "74e6d871-e62d-4085-a8ee-0ee57146c228" -->
## Example

```
Location:
/home/user/workspace/0_layer_universal/
  └── layer_0/
      └── layer_0_03_sub_layers/
          └── sub_layer_0_04_rules/
              └── new_rule.md   ◄── NEW FILE

Content:
- Rule description
- Scope
- Rationale
```

<!-- section_id: "98391a5a-5062-4213-ba6b-2f35c1128d44" -->
## Date Added
2026-01-26

<!-- section_id: "c5cb0e0f-e34b-4e42-adc8-490e354c3b7a" -->
## Related Issues
- Yoga Pro 9 speaker audio fix documentation request
