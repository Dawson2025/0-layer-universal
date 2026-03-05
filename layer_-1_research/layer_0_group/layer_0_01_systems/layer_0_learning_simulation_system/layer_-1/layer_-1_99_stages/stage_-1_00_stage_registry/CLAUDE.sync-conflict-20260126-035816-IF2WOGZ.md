---
resource_id: "fa25b427-8ab1-4ee2-b0fb-4094050b746a"
resource_type: "document"
resource_name: "CLAUDE.sync-conflict-20260126-035816-IF2WOGZ"
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
