---
name: 11_archives-workflow
description: Workflow skill for Historical versions and deprecated content. Activated when working on archives tasks.
version: 1.0.0
---

# Archives Workflow Skill

## When to Use
- When entering the archives stage
- When performing archives activities
- When completing archives deliverables

## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform archives activities
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
