---
resource_id: "4681aaf2-fca9-40eb-ab4d-20862313a815"
resource_type: "document"
resource_name: "SKILL.sync-conflict-20260126-035813-IF2WOGZ"
name: 01_request_gathering-workflow
description: Workflow skill for Collect and clarify requirements. Activated when working on 01_request_gathering tasks.
version: 1.0.0
---

# 01_request_gathering Workflow Skill

<!-- section_id: "505c29cb-afe3-46c7-bc2a-9319aeac149e" -->
## When to Use
- When entering the 01_request_gathering stage
- When performing 01_request_gathering activities
- When completing 01_request_gathering deliverables

<!-- section_id: "dd55d4dd-f9d0-46be-a387-5dd077a52910" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 01_request_gathering activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "6f1a9089-c5fe-4bc2-a47f-ab3944de0a8a" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "464fd875-1b39-48f5-a16a-e1ddb59fecb8" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
