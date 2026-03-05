---
resource_id: "b7ec172b-f6c0-4eef-b3e7-71b5610f8c99"
resource_type: "document"
resource_name: "SKILL.sync-conflict-20260126-035815-IF2WOGZ"
name: 10_current_product-workflow
description: Workflow skill for Production-ready artifacts. Activated when working on 10_current_product tasks.
version: 1.0.0
---

# 10_current_product Workflow Skill

## When to Use
- When entering the 10_current_product stage
- When performing 10_current_product activities
- When completing 10_current_product deliverables

## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 10_current_product activities
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
