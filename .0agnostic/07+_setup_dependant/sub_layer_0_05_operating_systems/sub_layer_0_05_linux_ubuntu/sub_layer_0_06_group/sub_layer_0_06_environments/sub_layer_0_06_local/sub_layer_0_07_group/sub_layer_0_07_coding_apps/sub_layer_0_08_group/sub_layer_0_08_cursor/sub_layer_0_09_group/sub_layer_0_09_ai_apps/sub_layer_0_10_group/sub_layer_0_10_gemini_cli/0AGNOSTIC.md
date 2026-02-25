# 0AGNOSTIC.md — sub_layer_0_10_gemini_cli

# ═══ STATIC CONTEXT (always loaded) ═══

# ── Entity Definition ──

## Identity

**Role**: AI App Configuration Manager — Gemini CLI
**Type**: Sub-Layer (Increased Specificity)
**Level**: 0.10 (Specific AI App)
**Scope**: Gemini CLI setup, configuration, and app-specific operational knowledge for Linux Ubuntu > Local Environment > Cursor IDE > AI Apps > Gemini CLI

**Specificity Chain**: OS (Linux Ubuntu) > Environment (Local) > Coding App (Cursor) > AI Apps > **Gemini CLI**

## Key Behaviors

- Manages Gemini CLI configuration and setup for this specific environment path
- App-specific children live in `sub_layer_0_11_group/`
- Shared infrastructure (MCP servers, AI models, tools, protocols, agent setup) lives in sibling feature entities at level 10 — see parent delegation contract
- Knowledge cascades from parent levels (coding apps > AI apps category) — only store Gemini CLI-specific content here
- Legacy setup docs migrated to `.0agnostic/01_knowledge/legacy_setup/`

## Inputs

- Parent context from sub_layer_0_09_ai_apps (shared AI app knowledge)
- Sibling feature entities (shared tools, models, protocols)
- Gemini CLI-specific setup docs and configuration

## Outputs

- Gemini CLI setup and configuration documentation
- App-specific children at level 11
- Operational rules and protocols specific to Gemini CLI

# ── Current Status ──

## Current Status

- **Stage**: Active (entity created 2026-02-22, restructured 2026-02-25)
- **Structure**: Canonical entity structure, shared content migrated to sibling features
- **Children**: App-specific children in sub_layer_0_11_group/
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

## Open Items

- [ ] Populate Gemini CLI-specific rules and knowledge
- [ ] Run agnostic-sync.sh to generate CLAUDE.md etc.

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
| Internal (stages) | `sub_layer_0_10_group/sub_layer_0_10_99_stages/` |
| Parent | `../0AGNOSTIC.md` |
| Shared Tools & Services | `../sub_layer_0_10_01_tools_and_services/` |
| Shared AI Models | `../sub_layer_0_10_02_ai_models/` |
| Shared Protocols | `../sub_layer_0_10_04_protocols/` |
