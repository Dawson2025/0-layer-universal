---
resource_id: "7c4d8d5a-8f0d-43f8-8cd8-0e2e9e5c5b62"
resource_type: "skill
document"
resource_name: "SKILL"
---
---
name: 07_testing-workflow
description: Workflow skill for Quality assurance and validation. Activated when working on 07_testing tasks.
version: 1.0.0
---

# 07_testing Workflow Skill

<!-- section_id: "c7a5c4b8-a59d-4996-b99a-393d6a2736cb" -->
## When to Use
- When entering the 07_testing stage
- When performing 07_testing activities
- When completing 07_testing deliverables

<!-- section_id: "04a6243c-f748-4351-9b10-425a22a861cb" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 07_testing activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "c4b29b3f-28ec-4489-9441-548d8e47dd45" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "0971aefd-5f1c-4d8e-bb91-b4b206d411cf" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
