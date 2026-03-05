---
resource_id: "edbe8891-6644-4084-8a93-ed3da23f46b0"
resource_type: "document"
resource_name: "SKILL.sync-conflict-20260126-101457-IF2WOGZ"
name: 01_request_gathering-workflow
description: Workflow skill for Collect and clarify requirements. Activated when working on 01_request_gathering tasks.
version: 1.0.0
---

# 01_request_gathering Workflow Skill

<!-- section_id: "c28cbe45-b7bb-48fa-b5a3-b8a7728a4bbe" -->
## When to Use
- When entering the 01_request_gathering stage
- When performing 01_request_gathering activities
- When completing 01_request_gathering deliverables

<!-- section_id: "9ed88705-9868-43d7-956c-b0d5ae0a6d4d" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 01_request_gathering activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "18726542-e811-401b-824a-49df2c03bb3b" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "30186146-0beb-48f4-8c53-4cf551181952" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
