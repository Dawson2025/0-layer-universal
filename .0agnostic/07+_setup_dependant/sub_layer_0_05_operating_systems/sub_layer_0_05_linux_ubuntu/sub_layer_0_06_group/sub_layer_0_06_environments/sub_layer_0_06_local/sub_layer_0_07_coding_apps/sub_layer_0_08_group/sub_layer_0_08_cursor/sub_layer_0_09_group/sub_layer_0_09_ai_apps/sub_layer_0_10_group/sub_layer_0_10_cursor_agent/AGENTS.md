# AutoGen Agent Context

## Identity

**Role**: AI App Configuration Manager — Cursor Agent
**Type**: Sub-Layer (Increased Specificity)
**Level**: 0.10 (Specific AI App)
**Scope**: Cursor Agent setup, configuration, MCP servers, AI model settings, and operational knowledge for Linux Ubuntu > Local Environment > Cursor IDE > AI Apps > Cursor Agent

**Specificity Chain**: OS (Linux Ubuntu) > Environment (Local) > Coding App (Cursor) > AI Apps > **Cursor Agent**

## Key Behaviors

- Manages Cursor Agent configuration and setup for this specific environment path
- MCP servers, models, and tools within this AI app are **features** (children at level 11)
- Knowledge cascades from parent levels (coding apps > AI apps category) — only store Cursor Agent-specific content here

## Inputs

- Parent context from sub_layer_0_09_ai_apps (shared AI app knowledge)
- Cursor Agent-specific setup docs, protocols, and configuration
- MCP server configurations and integration docs

## Outputs

- Cursor Agent setup and configuration documentation
- MCP server feature entities (level 11 children)
- Operational rules and protocols specific to Cursor Agent


## Current Status

- **Stage**: Initial entity creation (2026-02-22)
- **Structure**: Canonical entity structure applied — full .0agnostic/, .1merge/, 12 stages
- **Migration**: Legacy content from old sub_layer_0_09_cursor_agent/ directory structure preserved; setup/, MCP servers, models, tools, protocols, and agent setup content available for migration into .0agnostic/ subdirectories
- **Children**: MCP servers and tools to be organized as level 11 features

## AutoGen-Specific Configuration

### Agent Registration
Register this context in your AutoGen agent configuration:

```python
agent_config = {
    "context_file": "AGENTS.md",
    "resources_dir": ".0agnostic/",
    "episodic_dir": ".0agnostic/episodic_memory/"
}
```

### Multi-Agent Coordination
- Check .locks/ before modifying shared files
- Use atomic writes (temp file → rename)
- Log changes to divergence.log
- Read session files to understand previous work

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
