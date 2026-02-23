# Claude Code Context

## Identity

**Entity**: Cursor IDE
**Sub-Layer**: 0.08
**Type**: Increased Specificity (narrows from Coding Apps → Cursor IDE specifically)
**Scope**: Cursor IDE configuration, extensions, AI features, and child AI app integrations

**Specificity Chain**: OS (05) → Linux Ubuntu (05) → Environments (06) → Local (06) → Coding Apps (07) → **Cursor (08)**

## Key Behaviors

- Cursor-specific setup, configuration, and extensions live at this level
- AI app integrations (Claude Code CLI, Codex, Gemini, etc.) are children at level 09→10
- Rules and protocols here cascade to all AI apps running within Cursor
- Setup knowledge migrated from legacy `setup/` directory

## Delegation Contract

**Children** (level 09): AI Apps category (sub_layer_0_09_ai_apps)
**Parent** (level 07): Coding Apps


## Current Status

**State**: Restructuring complete
**Scope**: Cursor IDE entity with 1 child category (AI Apps) containing 4 AI app entities
**Content**: Entity structure created, legacy content preserved, children moved to `sub_layer_0_09_group/`
**Readiness**: Structure ready, awaiting knowledge population

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
