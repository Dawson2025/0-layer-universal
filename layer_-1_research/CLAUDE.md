# Claude Code Context

## Identity
You are an AI agent working within the layer_-1 (research) context. This layer contains research projects, experiments, and exploratory work.


## Navigation
- **Detailed resources**: `.0agnostic/` folder
- **Universal rules**: Inherit from `../layer_0/.0agnostic/rules/`
- **Research projects**: Direct children of this layer
- **Active research**: Check 0INDEX.md for current projects


## Key Behaviors


## Triggers

| Situation | Action |
|-----------|--------|
| Need universal rules | Load `../layer_0/.0agnostic/rules/` |
| Starting research | Navigate to project's stage_-1_02_research |
| Designing solutions | Navigate to project's stage_-1_04_design |
| Starting new session | Read `outputs/episodic/index.md` |



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
