---
resource_id: "d518cebc-bd3c-469f-8230-a7b1f3e97cc4"
resource_type: "skill_document"
resource_name: "SKILL"
---
---
name: 07_testing-workflow
description: Workflow skill for Quality assurance and validation. Activated when working on 07_testing tasks.
version: 1.0.0
---

# 07_testing Workflow Skill

<!-- section_id: "447377a5-168b-405a-acc2-f7e6d9e0983b" -->
## When to Use
- When entering the 07_testing stage
- When performing 07_testing activities
- When completing 07_testing deliverables

<!-- section_id: "6051a950-12f8-4113-a993-8097b8af9d13" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 07_testing activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "9a796bf3-c367-45ad-ac6a-92145b635afe" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "79946258-bfd4-4abf-9716-4a7a5fac6b9f" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
