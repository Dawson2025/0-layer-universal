---
resource_id: "988a7052-e372-444a-aa39-b571b99aa1ed"
resource_type: "knowledge"
resource_name: "AI_CONTEXT_MODIFICATION_PROTOCOL"
---
# AI Context Modification Protocol

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

## Rationale

- **Visibility**: User can see exactly what will change before it happens
- **Control**: User maintains authority over the AI instruction system
- **Intentionality**: Prevents accidental or unintended modifications
- **Auditability**: Creates a clear record of approved changes

## Diagram Requirements

The diagram MUST include:

1. **Full paths** - Complete path from root, not abbreviated
2. **File listing** - Show directory structure before and after
3. **Content summary** - Brief description of new file contents
4. **Action type** - Mark files as NEW, UPDATE, or DELETE

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

## Date Added
2026-01-26

## Related Issues
- Yoga Pro 9 speaker audio fix documentation request
