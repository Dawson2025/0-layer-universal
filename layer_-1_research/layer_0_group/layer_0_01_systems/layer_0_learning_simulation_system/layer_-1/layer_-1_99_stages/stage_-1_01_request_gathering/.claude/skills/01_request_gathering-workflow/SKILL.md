---
resource_id: "53b3731d-a62c-48f0-b300-173e25bb2fef"
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

<!-- section_id: "22c59747-5f34-4dc7-ba68-089f2fd0ced4" -->
## When to Use
- When entering the 01_request_gathering stage
- When performing 01_request_gathering activities
- When completing 01_request_gathering deliverables

<!-- section_id: "366fa73d-a5bb-4adf-a673-e2c6a9719d1b" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 01_request_gathering activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "7955293c-f38a-4585-bdf1-15a39f56143c" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "7484ed0f-ed2e-4c4d-91ae-673994ccd64c" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
