---
name: 00_stage_registry-workflow
description: Workflow skill for Stage metadata and registration. Activated when working on stage_registry tasks.
version: 1.0.0
---

# Stage_registry Workflow Skill

## When to Use
- When entering the stage_registry stage
- When performing stage_registry activities
- When completing stage_registry deliverables

## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform stage_registry activities
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
