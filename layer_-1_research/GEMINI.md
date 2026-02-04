# Gemini Context

## Identity
You are an AI agent working within the layer_-1 (research) context. This layer contains research projects, experiments, and exploratory work.


## Navigation
- **Detailed resources**: `.0agnostic/` folder
- **Universal rules**: Inherit from `../layer_0/.0agnostic/rules/`
- **Research projects**: Direct children of this layer
- **Active research**: Check 0INDEX.md for current projects


## Key Behaviors


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
