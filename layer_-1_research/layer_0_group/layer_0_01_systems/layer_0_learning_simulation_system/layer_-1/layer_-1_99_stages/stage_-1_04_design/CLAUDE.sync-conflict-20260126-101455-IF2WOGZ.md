---
resource_id: "1a18edc2-d289-49c6-87db-d45d4dac364d"
resource_type: "document"
resource_name: "CLAUDE.sync-conflict-20260126-101455-IF2WOGZ"
---
# stage_-1_05_design

<!-- section_id: "79c32663-2ccf-4e26-a2ff-12af7d23ceaf" -->
## Purpose
Technical design, architecture decisions

<!-- section_id: "ae3950c1-55c1-43b8-b692-c286f44ad87c" -->
## Structure
- `ai_agent_system/` - AI agent configurations for this stage
- `hand_off_documents/` - Handoff templates and documents
- `outputs/` - Stage outputs and artifacts

<!-- section_id: "a8826076-4e46-4907-81d9-705b44db4b24" -->
## Context
- **Layer**: -1
- **Stage**: design

<!-- section_id: "458fad75-5126-4023-94ba-b7870c574226" -->
## Workflow
When working in this stage:
1. Check `hand_off_documents/` for incoming context
2. Use `ai_agent_system/` configurations
3. Place deliverables in `outputs/`
