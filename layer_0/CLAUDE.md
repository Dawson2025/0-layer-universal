# Claude Code Context

## Identity
You are an AI agent working within the layer_0 (universal) context. This layer contains rules, prompts, and knowledge that apply across ALL projects.


## Navigation
- **Detailed resources**: `.0agnostic/` folder
- **Rules**: `.0agnostic/rules/`
- **Prompts**: `.0agnostic/prompts/`
- **Knowledge**: `.0agnostic/knowledge/`
- **Agents**: `.0agnostic/agents/`


## Key Behaviors

### Context Discovery
Before starting any task, traverse the context hierarchy:
1. Read this file (0AGNOSTIC.md)
2. Check `.0agnostic/` for detailed resources if needed
3. Follow layer-stage framework conventions

### Episodic Memory
Record your work in `.0agnostic/episodic_memory/`:
- Create session files for significant work
- Update divergence.log when changing outputs
- Enable next session to continue seamlessly

### Multi-Agent Safety
When modifying shared outputs:
- Check for locks before writing
- Use atomic writes (temp file → rename)
- Log changes to divergence.log


## Triggers

| Situation | Action |
|-----------|--------|
| Need detailed rules | Load `.0agnostic/rules/` |
| Need implementation prompts | Load `.0agnostic/prompts/` |
| Need reference knowledge | Load `.0agnostic/knowledge/` |
| Need agent definitions | Load `.0agnostic/agents/` |
| Starting new session | Read `.0agnostic/episodic_memory/index.md` |
| Modifying outputs | Check `.locks/` first |



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
