# AutoGen Agent Context

## Identity

**Role**: AI App Configuration Manager — Codex CLI
**Type**: Sub-Layer (Increased Specificity)
**Level**: 0.10 (Specific AI App)
**Scope**: Codex CLI setup, configuration, and app-specific operational knowledge for Linux Ubuntu > Local Environment > Cursor IDE > AI Apps > Codex CLI

**Specificity Chain**: OS (Linux Ubuntu) > Environment (Local) > Coding App (Cursor) > AI Apps > **Codex CLI**

## Key Behaviors

- Manages Codex CLI configuration and setup for this specific environment path
- App-specific children live in `sub_layer_0_11_group/`
- Shared infrastructure (MCP servers, AI models, tools, protocols, agent setup) lives in sibling feature entities at level 10 — see parent delegation contract
- Knowledge cascades from parent levels (coding apps > AI apps category) — only store Codex CLI-specific content here
- Legacy setup docs migrated to `.0agnostic/01_knowledge/legacy_setup/`

## Inputs

- Parent context from sub_layer_0_09_ai_apps (shared AI app knowledge)
- Sibling feature entities (shared tools, models, protocols)
- Codex CLI-specific setup docs and configuration

## Outputs

- Codex CLI setup and configuration documentation
- App-specific children at level 11
- Operational rules and protocols specific to Codex CLI


## Current Status

- **Stage**: Active (entity created 2026-02-22, restructured 2026-02-25)
- **Structure**: Canonical entity structure, shared content migrated to sibling features
- **Children**: App-specific children in sub_layer_0_11_group/
- **Migration**: Legacy setup docs in `.0agnostic/01_knowledge/legacy_setup/`. Shared MCP servers, AI models, tools, protocols moved to sibling feature entities.

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
