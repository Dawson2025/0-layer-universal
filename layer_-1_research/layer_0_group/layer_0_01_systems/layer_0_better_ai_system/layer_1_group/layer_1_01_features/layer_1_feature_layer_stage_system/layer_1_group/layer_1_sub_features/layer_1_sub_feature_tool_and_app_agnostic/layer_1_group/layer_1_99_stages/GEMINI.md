<!-- derived_from: "2c9df44f-d0c6-4eac-88aa-60ff92cd9a0c" -->
# Gemini Context

## Identity
Stages container for tool_and_app_agnostic.
- **Parent**: `../../0AGNOSTIC.md`
- **Layer**: 1

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
