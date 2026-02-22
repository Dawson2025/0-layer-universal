# 0AGNOSTIC.md — sub_layer_0_10_codex_cli

# ═══ STATIC CONTEXT (always loaded) ═══

# ── Entity Definition ──

## Identity

**Role**: AI App Configuration Manager — Codex CLI
**Type**: Sub-Layer (Increased Specificity)
**Level**: 0.10 (Specific AI App)
**Scope**: Codex CLI setup, configuration, MCP servers, AI model settings, and operational knowledge for Linux Ubuntu > Local Environment > Cursor IDE > AI Apps > Codex CLI

**Specificity Chain**: OS (Linux Ubuntu) > Environment (Local) > Coding App (Cursor) > AI Apps > **Codex CLI**

## Key Behaviors

- Manages Codex CLI configuration and setup for this specific environment path
- MCP servers, models, and tools within this AI app are **features** (children at level 11)
- Knowledge cascades from parent levels (coding apps > AI apps category) — only store Codex CLI-specific content here

## Inputs

- Parent context from sub_layer_0_09_ai_apps (shared AI app knowledge)
- Codex CLI-specific setup docs, protocols, and configuration
- MCP server configurations and integration docs

## Outputs

- Codex CLI setup and configuration documentation
- MCP server feature entities (level 11 children)
- Operational rules and protocols specific to Codex CLI

# ── Current Status ──

## Current Status

- **Stage**: Initial entity creation (2026-02-22)
- **Structure**: Canonical entity structure applied — full .0agnostic/, .1merge/, 12 stages
- **Migration**: Legacy content from old sub_layer_0_09_codex_cli/ directory structure preserved; setup/, MCP servers, models, tools, protocols, and agent setup content available for migration into .0agnostic/ subdirectories
- **Children**: MCP servers and tools to be organized as level 11 features

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
| Handoff Documents | `.0agnostic/05_handoff_documents/` |
| Skills | `.0agnostic/06_context_avenue_web/01_file_based/05_skills/` |
| Internal (stages) | `sub_layer_0_10_group/sub_layer_0_10_99_stages/` |
| Children (features) | `sub_layer_0_11_group/` |
| Parent | `../0AGNOSTIC.md` |
