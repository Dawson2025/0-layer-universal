---
name: 01_request_gathering-workflow
description: Workflow skill for Collect and clarify requirements. Activated when working on request_gathering tasks.
version: 1.0.0
---

# Request_gathering Workflow Skill

## When to Use
- When entering the request_gathering stage
- When performing request_gathering activities
- When completing request_gathering deliverables

## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform request_gathering activities
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
