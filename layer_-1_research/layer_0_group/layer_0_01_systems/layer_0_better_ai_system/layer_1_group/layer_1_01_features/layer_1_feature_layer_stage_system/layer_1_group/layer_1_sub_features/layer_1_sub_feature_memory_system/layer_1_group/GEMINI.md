<!-- derived_from: "a0d3e2e2-bd7c-40c9-9fc6-d73d7c8d53fa" -->
# Gemini Context

## Identity
Internal structure container for the memory_system entity.
- **Parent**: `../0AGNOSTIC.md`

## Contents
- `layer_1_00_layer_registry/` — Registry and proposals
- `layer_1_01_ai_manager_system/` — AI manager orchestration
- `layer_1_02_manager_handoff_documents/` — Handoff communication
- `layer_1_99_stages/` — Stage workflow (00-11)

## Gemini-Specific Notes

### Context Loading
Load detailed resources from .0agnostic/ when needed:
- rules/ - Behavioral constraints
- prompts/ - Task-specific prompts
- knowledge/ - Reference information
- agents/ - Agent definitions

### Session Continuity
Maintain episodic memory in .0agnostic/episodic_memory/:
- sessions/ - Timestamped session records
- changes/ - Divergence and conflict logs
- index.md - Searchable session index

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
