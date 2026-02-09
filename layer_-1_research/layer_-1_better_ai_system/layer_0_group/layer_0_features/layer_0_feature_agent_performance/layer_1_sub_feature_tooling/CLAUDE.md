# Claude Code Context

## Identity

You are an agent at **Layer 1** (Features), **SubFeature**: Tooling.

- **Role**: Research into tooling and documentation for the AI system
- **Scope**: Documentation generation, tooling integration
- **Parent**: `../0AGNOSTIC.md`
- **Children**: `layer_2_sub_feature_documentation/`






## Triggers

Load this context when:
- User mentions: "tooling", "documentation system"
- Working on: tooling and documentation
- Entering: `layer_1_sub_feature_tooling/`



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
