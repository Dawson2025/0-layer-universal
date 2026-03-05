---
resource_id: "b30a9da2-b1a5-473a-a72d-a562bd3d9402"
resource_type: "document"
resource_name: "CLAUDE.sync-conflict-20260126-035816-IF2WOGZ"
---
# stage_-1_05_design

<!-- section_id: "a12ee412-96dc-4f08-b8c9-24557b858fc4" -->
## Purpose
Technical design, architecture decisions

<!-- section_id: "4a73f863-816f-428d-9d43-91b3423bdc85" -->
## Structure
- `ai_agent_system/` - AI agent configurations for this stage
- `hand_off_documents/` - Handoff templates and documents
- `outputs/` - Stage outputs and artifacts

<!-- section_id: "2aefcd9f-ae96-4b1b-9613-f82437578746" -->
## Context
- **Layer**: -1
- **Stage**: design

<!-- section_id: "97ce7814-e4ce-49a3-87fb-3af233f31b52" -->
## Workflow
When working in this stage:
1. Check `hand_off_documents/` for incoming context
2. Use `ai_agent_system/` configurations
3. Place deliverables in `outputs/`
