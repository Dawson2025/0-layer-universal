# OpenAI Context

## Identity
You are an AI agent working within the layer_-1 (research) context. This layer contains research projects, experiments, and exploratory work.


## Navigation
- **Detailed resources**: `.0agnostic/` folder
- **Universal rules**: Inherit from `../layer_0/.0agnostic/rules/`
- **Research projects**: Direct children of this layer
- **Active research**: Check 0INDEX.md for current projects


## Key Behaviors

### Agent Context Loading
Each directory may have a `.gab.jsonld` agent definition with a matching `.integration.md` summary (same base name):
- e.g., `agent_orchestrator.gab.jsonld` → `agent_orchestrator.integration.md`
- Read the `.integration.md` for a quick summary; query the `.gab.jsonld` via jq for precise mode constraints
- `.integration.md` files are auto-generated — do not edit directly

### Context Discovery
Before starting any task:
1. Read this file (0AGNOSTIC.md)
2. Check `../layer_0/` for universal rules
3. Read project-specific context in research directories
4. Find the `.gab.jsonld` for your role and read its matching `.integration.md`
5. Read episodic memory if resuming work

### Episodic Memory
Record your work in `outputs/episodic/`:
- Create session files for significant work
- Update divergence.log when changing outputs
- Enable next session to continue seamlessly

### Research Protocol
Research projects follow stages 01-11 (see Stage Navigation below).


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
