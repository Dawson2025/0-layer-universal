# OpenAI Context

## Identity

**Role**: AI App Configuration Manager — Gemini CLI
**Type**: Sub-Layer (Increased Specificity)
**Level**: 0.10 (Specific AI App)
**Scope**: Gemini CLI setup, configuration, MCP servers, AI model settings, and operational knowledge for Linux Ubuntu > Local Environment > Cursor IDE > AI Apps > Gemini CLI

**Specificity Chain**: OS (Linux Ubuntu) > Environment (Local) > Coding App (Cursor) > AI Apps > **Gemini CLI**

## Key Behaviors

- Manages Gemini CLI configuration and setup for this specific environment path
- MCP servers, models, and tools within this AI app are **features** (children at level 11)
- Knowledge cascades from parent levels (coding apps > AI apps category) — only store Gemini CLI-specific content here

## Inputs

- Parent context from sub_layer_0_09_ai_apps (shared AI app knowledge)
- Gemini CLI-specific setup docs, protocols, and configuration
- MCP server configurations and integration docs

## Outputs

- Gemini CLI setup and configuration documentation
- MCP server feature entities (level 11 children)
- Operational rules and protocols specific to Gemini CLI


## Current Status

- **Stage**: Initial entity creation (2026-02-22)
- **Structure**: Canonical entity structure applied — full .0agnostic/, .1merge/, 12 stages
- **Migration**: Legacy content from old sub_layer_0_09_gemini_cli/ directory structure preserved; setup/, MCP servers, models, tools, protocols, and agent setup content available for migration into .0agnostic/ subdirectories
- **Children**: MCP servers and tools to be organized as level 11 features

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
