# Claude Code Context

## Identity
You are an AI agent working within the layer_1 (projects) context. This layer contains project-specific content, features, and components.


## Navigation
- **Detailed resources**: `.0agnostic/` folder
- **Universal rules**: Inherit from `../layer_0/.0agnostic/rules/`
- **Project features**: `layer_1_features/`
- **Project components**: `layer_1_components/`


## Key Behaviors


## Triggers

| Situation | Action |
|-----------|--------|
| Need universal rules | Load `../layer_0/.0agnostic/rules/` |
| Need project-specific rules | Load `.0agnostic/rules/` |
| Starting new session | Read `outputs/episodic/index.md` |
| Modifying outputs | Check `.locks/` first |
| Working on feature | Navigate to `layer_1_features/` |



## Claude-Specific Rules

### CLAUDE.md Integration
This file is auto-generated from 0AGNOSTIC.md. Edit 0AGNOSTIC.md to make changes.

### Tool Usage
- Use Read tool to load .0agnostic/ resources on-demand
- Use Bash for git operations and commands
- Use Write/Edit for file modifications
- Use Task tool for complex multi-step work

### Session Continuity
- Read outputs/episodic/index.md when resuming work
- Create session files after significant work
- Update divergence.log when modifying outputs

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
