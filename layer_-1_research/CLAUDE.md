# Claude Code Context

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
Record your work in `.0agnostic/episodic_memory/`:
- Create session files for significant work
- Update divergence.log when changing outputs
- Enable next session to continue seamlessly
- **Quick review**: Check `memory/episodic.md` (auto-memory topic file) for recent session history across all layers
- **After updating**: Run `tools/episodic-sync.sh` to sync episodic memory to auto-memory

### Research Protocol
Research projects follow stages 01-11 (see Stage Navigation below).


## Triggers

| Situation | Action |
|-----------|--------|
| Need universal rules | Load `../layer_0/.0agnostic/rules/` |
| Starting research | Navigate to project's stage_-1_02_research |
| Designing solutions | Navigate to project's stage_-1_04_design |
| Starting new session | Read `.0agnostic/episodic_memory/index.md` |



## Claude-Specific Rules

### CLAUDE.md Integration
This file is auto-generated from 0AGNOSTIC.md. Edit 0AGNOSTIC.md to make changes.

### Tool Usage
- Use Read tool to load .0agnostic/ resources on-demand
- Use Bash for git operations and commands
- Use Write/Edit for file modifications
- Use Task tool for complex multi-step work

### Session Continuity
- Read .0agnostic/episodic_memory/index.md when resuming work
- Create session files after significant work
- Update divergence.log when modifying outputs

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
