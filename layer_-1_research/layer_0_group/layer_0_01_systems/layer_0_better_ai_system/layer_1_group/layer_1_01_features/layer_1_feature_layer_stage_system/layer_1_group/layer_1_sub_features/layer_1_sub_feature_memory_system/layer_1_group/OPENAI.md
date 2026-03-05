<!-- derived_from: "a0d3e2e2-bd7c-40c9-9fc6-d73d7c8d53fa" -->
# OpenAI Context

## Identity
Internal structure container for the memory_system entity.
- **Parent**: `../0AGNOSTIC.md`

## Contents
- `layer_1_00_layer_registry/` — Registry and proposals
- `layer_1_01_ai_manager_system/` — AI manager orchestration
- `layer_1_02_manager_handoff_documents/` — Handoff communication
- `layer_1_99_stages/` — Stage workflow (00-11)

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
