# OpenAI Context

## Identity
Internal structure container for the memory_system entity.
- **Parent**: `../0AGNOSTIC.md`

## Contents
- `layer_2_00_layer_registry/` — Registry and proposals
- `layer_2_01_ai_manager_system/` — AI manager orchestration
- `layer_2_02_manager_handoff_documents/` — Handoff communication
- `layer_2_99_stages/` — Stage workflow (00-11)

## OpenAI-Specific Notes

### Function Calling
When using OpenAI function calling:
- Read .0agnostic/ resources for detailed instructions
- Check episodic memory for context
- Follow multi-agent sync rules for shared files

### Context Window Management
- 0AGNOSTIC.md is lean (<400 tokens)
- Load .0agnostic/ resources on-demand
- Avoid loading everything upfront

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
