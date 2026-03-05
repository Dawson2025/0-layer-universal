---
resource_id: "0e4e6ad0-0275-4325-b3a2-7733b3642690"
resource_type: "skill
knowledge"
resource_name: "SKILL"
---
---
name: 03_instructions-workflow
description: Workflow skill for Document setup and usage instructions. Activated when working on 03_instructions tasks.
version: 1.0.0
---

# 03_instructions Workflow Skill

<!-- section_id: "4dbeee83-c67b-45b3-af75-a1302a54d5de" -->
## When to Use
- When entering the 03_instructions stage
- When performing 03_instructions activities
- When completing 03_instructions deliverables

<!-- section_id: "469a7424-912b-49a8-b551-d2776217936a" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 03_instructions activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "969285ad-cc2a-412f-a141-d8dac89c6053" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "9b20ddf5-cc89-418f-b6c5-3f0d19a934d5" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
