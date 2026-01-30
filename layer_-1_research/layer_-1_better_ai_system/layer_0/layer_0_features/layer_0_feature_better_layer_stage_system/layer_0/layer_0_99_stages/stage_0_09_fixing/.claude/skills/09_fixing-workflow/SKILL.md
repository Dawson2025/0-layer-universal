---
name: 09_fixing-workflow
description: Workflow skill for Address issues from criticism. Activated when working on fixing tasks.
version: 1.0.0
---

# Fixing Workflow Skill

## When to Use
- When entering the fixing stage
- When performing fixing activities
- When completing fixing deliverables

## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform fixing activities
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
