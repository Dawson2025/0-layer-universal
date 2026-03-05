---
resource_id: "83743c27-cd5d-48fc-9d35-b8944df49387"
resource_type: "agnostic
document"
resource_name: "0AGNOSTIC"
---
# 0AGNOSTIC.md — sub_layer_0_10_01_tools_and_services

# ═══ STATIC CONTEXT (always loaded) ═══

# ── Entity Definition ──

## Identity

**Entity**: Tools and Services
**Sub-Layer**: 0.10
**Type**: Feature (shared across all AI apps)
**Feature Number**: 01 (first in sequence — know your tools before anything else)
**Scope**: MCP servers, APIs, CLIs, secrets, and budget tracking shared across all AI app entities

**Specificity Chain**: OS (05) → Linux Ubuntu (05) → Environments (06) → Local (06) → Coding Apps (07) → Cursor (08) → AI Apps (09) → **Tools and Services (10)**

## Key Behaviors

- Contains all shared MCP servers (Perplexity, Tavily, Playwright, Canvas, etc.), APIs, CLIs, and secrets
- Budget tracking configuration lives at entity root (budget_config.json)
- Per-service pricing docs live in each MCP server child's directory
- Individual MCP servers are children at level 11 in `sub_layer_0_11_group/`
- App-specific tools (e.g., Claude in Chrome) do NOT live here — they stay in their specific AI app entity
- **MCP API cost tracking**: $20/mo budget, warn at 80%, confirm at 100%. Protocol inherited from AI Apps parent

## Delegation Contract

**Children** (level 11): Individual MCP servers, CLI tools, secrets, shared resources
**Parent** (level 09): AI Apps Category
**Siblings**: 02_ai_models, 03_universal_tools, 04_protocols, 05_agent_setup (features), claude_code_cli, codex_cli, cursor_agent, gemini_cli (further_specificity)

## Inputs

- MCP server configuration files and setup documentation
- API keys and secrets (managed externally)
- Budget and pricing information

## Outputs

- Organized MCP server documentation and configuration
- Budget tracking and cost analysis
- Shared tool knowledge for all AI apps

# ── Current Status ──

## Current Status

- **Stage**: Active (created 2026-02-25 from content migration)
- **Structure**: Full canonical entity with .0agnostic/, 12 stages, children group
- **Content**: MCP servers migrated from Claude Code CLI, budget_config.json, pricing docs. Knowledge topics: `api_keys` (setup guide + config template), `mcp_system` (7 docs — system guide, config, server setup, matrix, routing, codex sync), `mcp_setup` (setup docs + scripts: mcp_manager.py, mcp_concurrent_browser.py, codex_mcp_sync.py), `mcp_core` (core reference)
- **Children**: 10+ shared MCP server entities, CLI tools, secrets in sub_layer_0_11_group/

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── Current State ──

## Current State Detail

Content migrated from `sub_layer_0_10_claude_code_cli/sub_layer_0_10_mcp_servers_and_apis_and_clis_and_secrets/`. MCP servers that are app-specific (Claude in Chrome) remain in their respective AI app entity.

## Open Items

- [ ] Renumber MCP server children from sub_layer_0_10_* to sub_layer_0_11_*
- [ ] Create 0AGNOSTIC.md for each MCP server child entity

# ── References ──

## Navigation

| Resource | Location |
|----------|----------|
| Budget Config | `budget_config.json` |
| Knowledge: API Keys | `.0agnostic/01_knowledge/api_keys/` |
| Knowledge: MCP System | `.0agnostic/01_knowledge/mcp_system/` |
| Knowledge: MCP Setup | `.0agnostic/01_knowledge/mcp_setup/` |
| Knowledge: MCP Core | `.0agnostic/01_knowledge/mcp_core/` |
| Rules | `.0agnostic/02_rules/` |
| Protocols | `.0agnostic/03_protocols/` |
| Children (MCP servers) | `sub_layer_0_11_group/` |
| Stages | `sub_layer_0_10_group/sub_layer_0_10_99_stages/` |
| Parent | `../../0AGNOSTIC.md` |
