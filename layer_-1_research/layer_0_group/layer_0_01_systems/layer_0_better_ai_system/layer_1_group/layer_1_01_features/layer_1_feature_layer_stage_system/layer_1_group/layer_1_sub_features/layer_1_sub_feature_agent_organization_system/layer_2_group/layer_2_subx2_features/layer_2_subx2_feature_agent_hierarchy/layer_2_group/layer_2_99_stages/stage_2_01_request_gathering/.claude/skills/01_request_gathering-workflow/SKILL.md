---
resource_id: "eac52ca0-e447-4125-9dc7-97d2de9072bd"
resource_type: "skill_document"
resource_name: "SKILL"
---
---
name: 01_request_gathering-workflow
description: Workflow skill for Collect and clarify requirements. Activated when working on 01_request_gathering tasks.
version: 1.0.0
---

# 01_request_gathering Workflow Skill

<!-- section_id: "7f9ef8b6-9d03-45fa-b26e-0d4c67046c0e" -->
## When to Use
- When entering the 01_request_gathering stage
- When performing 01_request_gathering activities
- When completing 01_request_gathering deliverables

<!-- section_id: "bc84b05d-4cdf-46c6-a117-34f5945b6ed9" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 01_request_gathering activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "d6baccdf-b20c-407f-8eea-6c2b8a066a3e" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "f84fe215-d54a-456d-9fb9-eeb1fd1825f4" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
