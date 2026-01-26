---
name: 10_current_product-workflow
description: Workflow skill for Production-ready artifacts. Activated when working on current_product tasks.
version: 1.0.0
---

# Current_product Workflow Skill

## When to Use
- When entering the current_product stage
- When performing current_product activities
- When completing current_product deliverables

## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform current_product activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

## Best Practices
- Follow established patterns
- Document decisions and rationale
- Keep deliverables organized
