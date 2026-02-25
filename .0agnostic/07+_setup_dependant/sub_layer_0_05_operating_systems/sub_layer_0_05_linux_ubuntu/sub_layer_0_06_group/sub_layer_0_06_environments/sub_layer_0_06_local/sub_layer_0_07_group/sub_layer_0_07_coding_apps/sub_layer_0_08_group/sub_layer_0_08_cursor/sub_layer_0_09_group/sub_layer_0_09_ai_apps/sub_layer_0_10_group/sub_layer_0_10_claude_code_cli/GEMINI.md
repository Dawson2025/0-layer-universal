# Gemini Context

## Identity

**Role**: AI App Configuration Manager — Claude Code CLI
**Type**: Sub-Layer (Increased Specificity)
**Level**: 0.10 (Specific AI App)
**Scope**: Claude Code CLI setup, configuration, MCP servers, AI model settings, and operational knowledge for Linux Ubuntu > Local Environment > Cursor IDE > AI Apps > Claude Code CLI

**Specificity Chain**: OS (Linux Ubuntu) > Environment (Local) > Coding App (Cursor) > AI Apps > **Claude Code CLI**

## Key Behaviors

- Manages Claude Code CLI configuration and setup for this specific environment path
- MCP servers, models, and tools within this AI app are **features** (children at level 11)
- Knowledge cascades from parent levels (coding apps > AI apps category) — only store Claude Code CLI-specific content here
- **MCP API cost tracking**: Budget config at `sub_layer_0_10_mcp_servers.../budget_config.json`, per-service pricing at each MCP server directory. Budget enforcement rule inherited from parent (AI Apps level)
- **CRITICAL**: `perplexity_research` (deep research) costs $3-5+ per call. Always prefer `perplexity_ask` (~$0.01) or `perplexity_search` (~$0.05)

## Inputs

- Parent context from sub_layer_0_09_ai_apps (shared AI app knowledge)
- Claude Code CLI-specific setup docs, protocols, and configuration
- MCP server configurations and integration docs

## Outputs

- Claude Code CLI setup and configuration documentation
- MCP server feature entities (level 11 children)
- Operational rules and protocols specific to Claude Code CLI


## Current Status

- **Stage**: Active (entity created 2026-02-22, cost tracking added 2026-02-25)
- **Structure**: Canonical entity structure applied — full .0agnostic/, .1merge/, 12 stages
- **Migration**: Legacy content from old sub_layer_0_09_claude_code_cli/ directory structure preserved; setup/, MCP servers, models, tools, protocols, and agent setup content available for migration into .0agnostic/ subdirectories
- **Children**: MCP servers parent dir contains budget_config.json and per-service pricing
- **Cost tracking**: Active — $20/mo budget, $19.46 remaining (as of 2026-02-25). Deep research = 97% of historical costs

## Gemini-Specific Notes

### Context Loading
Load detailed resources from .0agnostic/ when needed:
- rules/ - Behavioral constraints
- prompts/ - Task-specific prompts
- knowledge/ - Reference information
- agents/ - Agent definitions

### Session Continuity
Maintain episodic memory in .0agnostic/episodic_memory/:
- sessions/ - Timestamped session records
- changes/ - Divergence and conflict logs
- index.md - Searchable session index

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
