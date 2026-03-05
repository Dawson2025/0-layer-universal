---
resource_id: "d518cebc-bd3c-469f-8230-a7b1f3e97cc4"
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

## When to Use
- When entering the 07_testing stage
- When performing 07_testing activities
- When completing 07_testing deliverables

## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 07_testing activities
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
