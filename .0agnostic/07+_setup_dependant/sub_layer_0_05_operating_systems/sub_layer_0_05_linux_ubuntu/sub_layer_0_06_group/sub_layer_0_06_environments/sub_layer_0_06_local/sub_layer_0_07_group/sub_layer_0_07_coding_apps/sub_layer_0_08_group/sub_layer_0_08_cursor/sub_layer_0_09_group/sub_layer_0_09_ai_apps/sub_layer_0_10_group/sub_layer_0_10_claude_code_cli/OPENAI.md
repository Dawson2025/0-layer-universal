<!-- resource_id: "a6e1a3da-a659-472f-b28e-36e921d43638" -->
# OpenAI Context

## Identity

**Role**: AI App Configuration Manager — Claude Code CLI
**Type**: Sub-Layer (Increased Specificity)
**Level**: 0.10 (Specific AI App)
**Scope**: Claude Code CLI setup, configuration, and app-specific operational knowledge for Linux Ubuntu > Local Environment > Cursor IDE > AI Apps > Claude Code CLI

**Specificity Chain**: OS (Linux Ubuntu) > Environment (Local) > Coding App (Cursor) > AI Apps > **Claude Code CLI**

## Key Behaviors

- Manages Claude Code CLI configuration and setup for this specific environment path
- App-specific children (e.g., Claude in Chrome) live in `sub_layer_0_11_group/`
- Shared infrastructure (MCP servers, AI models, tools, protocols, agent setup) lives in sibling feature entities at level 10 — see parent delegation contract
- Knowledge cascades from parent levels (coding apps > AI apps category) — only store Claude Code CLI-specific content here
- Legacy setup docs migrated to `.0agnostic/01_knowledge/legacy_setup/`

## Inputs

- Parent context from sub_layer_0_09_ai_apps (shared AI app knowledge)
- Sibling feature entities (shared tools, models, protocols)
- Claude Code CLI-specific setup docs and configuration

## Outputs

- Claude Code CLI setup and configuration documentation
- App-specific children (Claude in Chrome) at level 11
- Operational rules and protocols specific to Claude Code CLI


## Current Status

- **Stage**: Active (entity created 2026-02-22, restructured 2026-02-25)
- **Structure**: Canonical entity structure, shared content migrated to sibling features
- **Children**: Claude in Chrome (app-specific) in sub_layer_0_11_group/
- **Migration**: Legacy setup docs in `.0agnostic/01_knowledge/legacy_setup/`. Shared MCP servers, AI models, tools, protocols moved to sibling feature entities.

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
