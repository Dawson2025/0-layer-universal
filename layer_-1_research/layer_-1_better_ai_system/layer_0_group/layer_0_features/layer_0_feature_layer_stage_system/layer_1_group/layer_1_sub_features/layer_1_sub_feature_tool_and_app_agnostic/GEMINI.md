# Gemini Context

## Identity
You are an agent at **Layer 1** (Sub-Feature), **Sub-Feature**: Tool and App Agnostic.
- **Role**: Tool-agnostic context system — ensuring the framework works across all AI tools and applications
- **Scope**: Agnostic sync, merge system, tool-specific overrides, cross-tool compatibility
- **Parent**: `../../../0AGNOSTIC.md` (layer_0_feature_layer_stage_system)
- **Children**: None (leaf entity)






## Gemini-Specific Notes

### Context Loading
Load detailed resources from .0agnostic/ when needed:
- rules/ - Behavioral constraints
- prompts/ - Task-specific prompts
- knowledge/ - Reference information
- agents/ - Agent definitions

### Session Continuity
Maintain episodic memory in outputs/episodic/:
- sessions/ - Timestamped session records
- changes/ - Divergence and conflict logs
- index.md - Searchable session index

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
