---
resource_id: "6e7bec7d-e227-4c3c-b93f-5805de8c242a"
resource_type: "agnostic
document"
resource_name: "0AGNOSTIC"
---
# 0AGNOSTIC.md — sub_layer_0_10_claude_code_cli

# ═══ STATIC CONTEXT (always loaded) ═══

# ── Entity Definition ──

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

# ── Current Status ──

## Current Status

- **Stage**: Active (entity created 2026-02-22, restructured 2026-02-25)
- **Structure**: Canonical entity structure, shared content migrated to sibling features
- **Children**: Claude in Chrome (app-specific) in sub_layer_0_11_group/
- **Migration**: Legacy setup docs in `.0agnostic/01_knowledge/legacy_setup/`. Shared MCP servers, AI models, tools, protocols moved to sibling feature entities.

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── Current State ──

## Current State Detail

Entity restructured. Shared infrastructure migrated to sibling feature entities at level 10:
- MCP servers/APIs/CLIs/secrets → `../sub_layer_0_10_01_tools_and_services/`
- AI models → `../sub_layer_0_10_02_ai_models/`
- Universal tools → `../sub_layer_0_10_03_universal_tools/`
- Protocols → `../sub_layer_0_10_04_protocols/`
- Agent setup → `../sub_layer_0_10_05_agent_setup/`
- Legacy setup docs → `.0agnostic/01_knowledge/legacy_setup/`
- Claude in Chrome (app-specific child) → `sub_layer_0_11_group/sub_layer_0_11_claude_in_chrome/`

## Open Items

- [ ] Populate Claude Code CLI-specific rules and knowledge
- [ ] Create 0AGNOSTIC.md for Claude in Chrome child entity

# ── References ──

## Navigation

| Resource | Location |
|----------|----------|
| Knowledge | `.0agnostic/01_knowledge/` |
| Legacy Setup | `.0agnostic/01_knowledge/legacy_setup/` |
| Rules | `.0agnostic/02_rules/` |
| Protocols | `.0agnostic/03_protocols/` |
| Handoff Documents | `.0agnostic/05_handoff_documents/` |
| Children | `sub_layer_0_11_group/` |
| Claude in Chrome | `sub_layer_0_11_group/sub_layer_0_11_claude_in_chrome/` |
| Internal (stages) | `sub_layer_0_10_group/sub_layer_0_10_99_stages/` |
| Parent | `../0AGNOSTIC.md` |
| Shared Tools & Services | `../sub_layer_0_10_01_tools_and_services/` |
| Shared AI Models | `../sub_layer_0_10_02_ai_models/` |
| Shared Protocols | `../sub_layer_0_10_04_protocols/` |
