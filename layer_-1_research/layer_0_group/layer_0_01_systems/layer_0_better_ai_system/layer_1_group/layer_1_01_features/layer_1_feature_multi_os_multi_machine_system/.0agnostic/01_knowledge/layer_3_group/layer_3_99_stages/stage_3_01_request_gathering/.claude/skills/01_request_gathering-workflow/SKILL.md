---
resource_id: "e24160ab-2704-4e9c-a341-78ca2104c0d1"
resource_type: "skill
knowledge"
resource_name: "SKILL"
---
---
name: 01_request_gathering-workflow
description: Workflow skill for Collect and clarify requirements. Activated when working on 01_request_gathering tasks.
version: 1.0.0
---

# 01_request_gathering Workflow Skill

<!-- section_id: "52743c00-9b27-485b-a26d-fd23ad02be80" -->
## When to Use
- When entering the 01_request_gathering stage
- When performing 01_request_gathering activities
- When completing 01_request_gathering deliverables

<!-- section_id: "de74f0dc-7ded-4da7-b594-48e78a98b164" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 01_request_gathering activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "86c3b1d7-11a4-4a41-b3be-ccefdfbc52f4" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "3627c8cb-8588-41c1-9f89-58521adcc855" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
