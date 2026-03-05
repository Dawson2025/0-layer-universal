<!-- derived_from: "222ae9a2-e10e-41e6-a0ef-c988ab667147" -->
# Gemini Context

## Identity
Stages container for multi_os_multi_machine.
- **Parent**: `../../0AGNOSTIC.md`
- **Layer**: 0

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
