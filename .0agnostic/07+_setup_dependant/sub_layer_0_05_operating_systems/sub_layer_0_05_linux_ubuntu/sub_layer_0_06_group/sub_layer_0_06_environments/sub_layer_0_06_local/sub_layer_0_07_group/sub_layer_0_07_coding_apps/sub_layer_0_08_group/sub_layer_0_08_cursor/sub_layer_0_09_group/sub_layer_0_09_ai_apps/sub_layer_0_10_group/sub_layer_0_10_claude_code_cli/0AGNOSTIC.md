# 0AGNOSTIC.md — sub_layer_0_10_claude_code_cli

# ═══ STATIC CONTEXT (always loaded) ═══

# ── Entity Definition ──

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

# ── Current Status ──

## Current Status

- **Stage**: Active (entity created 2026-02-22, cost tracking added 2026-02-25)
- **Structure**: Canonical entity structure applied — full .0agnostic/, .1merge/, 12 stages
- **Migration**: Legacy content from old sub_layer_0_09_claude_code_cli/ directory structure preserved; setup/, MCP servers, models, tools, protocols, and agent setup content available for migration into .0agnostic/ subdirectories
- **Children**: MCP servers parent dir contains budget_config.json and per-service pricing
- **Cost tracking**: Active — $20/mo budget, $19.46 remaining (as of 2026-02-25). Deep research = 97% of historical costs

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── Current State ──

## Current State Detail

Entity structure created. Legacy content exists alongside new canonical structure:
- `setup/` — Original setup docs (to migrate to `.0agnostic/01_knowledge/setup/`)
- `sub_layer_0_10_mcp_servers_and_apis_and_clis_and_secrets/` — MCP server content (to become level 11 features)
- `sub_layer_0_11_ai_models/` — AI model content (to become level 11 feature)
- `sub_layer_0_12_universal_tools/` — Tools (to become level 11 feature or migrate to .0agnostic/)
- `sub_layer_0_13_protocols/` — Protocols (to migrate to `.0agnostic/03_protocols/`)
- `sub_layer_0_14_agent_setup/` — Agent setup (to migrate to `.0agnostic/01_knowledge/agent_setup/`)

## Open Items

- [ ] Migrate legacy content into .0agnostic/ subdirectories
- [ ] Convert MCP servers to level 11 feature entities
- [ ] Run agnostic-sync.sh to generate CLAUDE.md etc.
- [ ] Write stage 0AGNOSTIC.md files

# ── References ──

## Navigation

| Resource | Location |
|----------|----------|
| Knowledge | `.0agnostic/01_knowledge/` |
| Rules | `.0agnostic/02_rules/` |
| Protocols | `.0agnostic/03_protocols/` |
| Budget Config | `sub_layer_0_10_mcp_servers.../budget_config.json` |
| Perplexity Pricing | `sub_layer_0_10_mcp_servers.../sub_layer_0_10_perplexity-mcp/pricing.md` |
| Tavily Pricing | `sub_layer_0_10_mcp_servers.../sub_layer_0_10_tavily-mcp/pricing.md` |
| Handoff Documents | `.0agnostic/05_handoff_documents/` |
| Skills | `.0agnostic/06_context_avenue_web/01_file_based/05_skills/` |
| Internal (stages) | `sub_layer_0_10_group/sub_layer_0_10_99_stages/` |
| Children (features) | `sub_layer_0_11_group/` |
| Parent | `../0AGNOSTIC.md` |
