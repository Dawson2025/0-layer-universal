---
resource_id: "eac52ca0-e447-4125-9dc7-97d2de9072bd"
resource_type: "skill
document"
resource_name: "SKILL"
---
---
name: 01_request_gathering-workflow
description: Workflow skill for Collect and clarify requirements. Activated when working on 01_request_gathering tasks.
version: 1.0.0
---

# 01_request_gathering Workflow Skill

## When to Use
- When entering the 01_request_gathering stage
- When performing 01_request_gathering activities
- When completing 01_request_gathering deliverables

## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 01_request_gathering activities
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
