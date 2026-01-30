---
name: 04_planning-workflow
description: Workflow skill for Create implementation plan. Activated when working on planning tasks.
version: 1.0.0
---

# Planning Workflow Skill

## When to Use
- When entering the planning stage
- When performing planning activities
- When completing planning deliverables

## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform planning activities
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
