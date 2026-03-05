---
resource_id: "c62d101d-c742-4657-a6f6-1e3c5a22f7a2"
resource_type: "skill
knowledge"
resource_name: "SKILL"
---
---
name: 05_design-workflow
description: Workflow skill for Technical design and architecture. Activated when working on 05_design tasks.
version: 1.0.0
---

# 05_design Workflow Skill

<!-- section_id: "82b0a3d7-e2bd-41b1-840a-4651f2057050" -->
## When to Use
- When entering the 05_design stage
- When performing 05_design activities
- When completing 05_design deliverables

<!-- section_id: "edbaeba1-15da-4439-bd5c-f9b2e4490d6e" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 05_design activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "3187dcd1-0212-4d6c-8d6a-6f843f057033" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "0982a433-6321-43b1-956a-74c304862fef" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
