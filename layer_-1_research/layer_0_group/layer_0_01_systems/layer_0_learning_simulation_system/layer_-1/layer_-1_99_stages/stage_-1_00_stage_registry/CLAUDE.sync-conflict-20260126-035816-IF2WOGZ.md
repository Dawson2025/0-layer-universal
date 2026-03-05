---
resource_id: "fa25b427-8ab1-4ee2-b0fb-4094050b746a"
resource_type: "document"
resource_name: "CLAUDE.sync-conflict-20260126-035816-IF2WOGZ"
---
# stage_-1_00_stage_registry

<!-- section_id: "eab31d69-2b21-454d-8a47-5eee9128af77" -->
## Purpose
Stage metadata and registration

<!-- section_id: "5930c6c2-1592-4588-b236-4a2b55f8c138" -->
## Structure
- `ai_agent_system/` - AI agent configurations for this stage
- `hand_off_documents/` - Handoff templates and documents
- `outputs/` - Stage outputs and artifacts

<!-- section_id: "10df969e-2465-43ae-a65d-e5f931a9b4bb" -->
## Context
- **Layer**: -1
- **Stage**: stage_registry

<!-- section_id: "cfa6cedf-8a18-4b6a-84ae-67ac785910a2" -->
## Workflow
When working in this stage:
1. Check `hand_off_documents/` for incoming context
2. Use `ai_agent_system/` configurations
3. Place deliverables in `outputs/`
