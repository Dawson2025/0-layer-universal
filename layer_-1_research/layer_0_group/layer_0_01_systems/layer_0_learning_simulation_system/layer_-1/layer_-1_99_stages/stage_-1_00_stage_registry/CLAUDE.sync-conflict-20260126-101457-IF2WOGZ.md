---
resource_id: "22a0af9f-be61-4af5-9472-86903ba6c3d2"
resource_type: "document"
resource_name: "CLAUDE.sync-conflict-20260126-101457-IF2WOGZ"
---
# stage_-1_00_stage_registry

## Purpose
Stage metadata and registration

## Structure
- `ai_agent_system/` - AI agent configurations for this stage
- `hand_off_documents/` - Handoff templates and documents
- `outputs/` - Stage outputs and artifacts

## Context
- **Layer**: -1
- **Stage**: stage_registry

## Workflow
When working in this stage:
1. Check `hand_off_documents/` for incoming context
2. Use `ai_agent_system/` configurations
3. Place deliverables in `outputs/`
