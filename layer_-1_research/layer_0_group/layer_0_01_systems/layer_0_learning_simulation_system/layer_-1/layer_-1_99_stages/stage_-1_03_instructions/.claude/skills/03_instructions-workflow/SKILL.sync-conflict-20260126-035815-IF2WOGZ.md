---
resource_id: "b75a6d6c-88cb-49a4-b5ad-a0b21a384650"
resource_type: "document"
resource_name: "SKILL.sync-conflict-20260126-035815-IF2WOGZ"
name: 03_instructions-workflow
description: Workflow skill for Document setup and usage instructions. Activated when working on 03_instructions tasks.
version: 1.0.0
---

# 03_instructions Workflow Skill

## When to Use
- When entering the 03_instructions stage
- When performing 03_instructions activities
- When completing 03_instructions deliverables

## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 03_instructions activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
