---
resource_id: "22a0af9f-be61-4af5-9472-86903ba6c3d2"
resource_type: "document"
resource_name: "CLAUDE.sync-conflict-20260126-101457-IF2WOGZ"
---
# stage_-1_00_stage_registry

<!-- section_id: "28637fc0-a634-4471-9993-3c11f4ae3398" -->
## Purpose
Stage metadata and registration

<!-- section_id: "5a64de9b-bf11-4c73-9991-12e387d4b11d" -->
## Structure
- `ai_agent_system/` - AI agent configurations for this stage
- `hand_off_documents/` - Handoff templates and documents
- `outputs/` - Stage outputs and artifacts

<!-- section_id: "2791dd49-aeb6-4c5c-b33f-de98f5d25c6b" -->
## Context
- **Layer**: -1
- **Stage**: stage_registry

<!-- section_id: "97b2b203-0750-47af-9a7a-54454ab60643" -->
## Workflow
When working in this stage:
1. Check `hand_off_documents/` for incoming context
2. Use `ai_agent_system/` configurations
3. Place deliverables in `outputs/`
