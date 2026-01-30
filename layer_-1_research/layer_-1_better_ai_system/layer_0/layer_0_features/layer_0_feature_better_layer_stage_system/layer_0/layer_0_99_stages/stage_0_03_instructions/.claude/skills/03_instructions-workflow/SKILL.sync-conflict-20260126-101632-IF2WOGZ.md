---
name: 03_instructions-workflow
description: Workflow skill for Document setup and usage instructions. Activated when working on instructions tasks.
version: 1.0.0
---

# Instructions Workflow Skill

## When to Use
- When entering the instructions stage
- When performing instructions activities
- When completing instructions deliverables

## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform instructions activities
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
