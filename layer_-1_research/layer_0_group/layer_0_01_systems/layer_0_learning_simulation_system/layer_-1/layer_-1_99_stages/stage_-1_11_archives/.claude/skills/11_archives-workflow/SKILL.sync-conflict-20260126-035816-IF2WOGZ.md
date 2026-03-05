---
resource_id: "f2aa5b51-40a9-40aa-b62a-6cc16d9ff75f"
resource_type: "document"
resource_name: "SKILL.sync-conflict-20260126-035816-IF2WOGZ"
name: 11_archives-workflow
description: Workflow skill for Historical versions and deprecated content. Activated when working on 11_archives tasks.
version: 1.0.0
---

# 11_archives Workflow Skill

<!-- section_id: "69f25013-c180-475b-8c22-a232b6d89c38" -->
## When to Use
- When entering the 11_archives stage
- When performing 11_archives activities
- When completing 11_archives deliverables

<!-- section_id: "41f90112-9537-4245-8345-a84f146bed47" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 11_archives activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "0957ba4b-4118-4d21-93f7-415fa38d7ad7" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "517574cc-c2a3-4608-a4cb-f31e8076304b" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
