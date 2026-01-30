---
name: 07_testing-workflow
description: Workflow skill for Quality assurance and validation. Activated when working on testing tasks.
version: 1.0.0
---

# Testing Workflow Skill

## When to Use
- When entering the testing stage
- When performing testing activities
- When completing testing deliverables

## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform testing activities
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
