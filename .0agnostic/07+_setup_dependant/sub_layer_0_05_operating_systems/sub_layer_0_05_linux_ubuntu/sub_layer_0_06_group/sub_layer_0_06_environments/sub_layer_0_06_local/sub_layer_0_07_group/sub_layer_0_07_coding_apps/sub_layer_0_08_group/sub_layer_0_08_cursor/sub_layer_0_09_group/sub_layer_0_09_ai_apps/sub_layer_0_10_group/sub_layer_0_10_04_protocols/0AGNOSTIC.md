---
resource_id: "1511a418-f4d5-4c30-b971-412f00c4d533"
resource_type: "agnostic_document"
resource_name: "0AGNOSTIC"
---
# 0AGNOSTIC.md — sub_layer_0_10_04_protocols

# ═══ STATIC CONTEXT (always loaded) ═══

# ── Entity Definition ──

<!-- section_id: "a512f1e7-ae39-43d7-91d7-23c55b11d1b3" -->
## Identity

**Entity**: Protocols
**Sub-Layer**: 0.10
**Type**: Feature (shared across all AI apps)
**Feature Number**: 04 (fourth in sequence — operational protocols that govern how AI apps behave)
**Scope**: Shared operational protocols for all AI apps, including document operations, git workflows, and service integrations

**Specificity Chain**: OS (05) → Linux Ubuntu (05) → Environments (06) → Local (06) → Coding Apps (07) → Cursor (08) → AI Apps (09) → **Protocols (10)**

<!-- section_id: "2fa28f66-263d-4c70-a864-45b3538e5bc3" -->
## Key Behaviors

- Contains protocols like docx_operations, github_operations, and other cross-app workflows
- Protocols stored in `.0agnostic/03_protocols/` following the standard convention
- Protocols here must be AI-app-agnostic — app-specific protocols stay in their respective entity
- References Tools and Services (01) for tool-specific protocol bindings
- References AI Models (02) for model-specific protocol variations
- Protocol versioning tracked to handle breaking changes

<!-- section_id: "7df26a95-0fa2-4fbd-bd3d-e28a2edd12d3" -->
## Delegation Contract

**Children** (level 11): Individual protocol definitions (future — if protocols grow complex enough)
**Parent** (level 09): AI Apps Category
**Siblings**: 01_tools_and_services, 02_ai_models, 03_universal_tools, 05_agent_setup (features), claude_code_cli, codex_cli, cursor_agent, gemini_cli (further_specificity)

<!-- section_id: "16d7b8ef-a534-46f0-85dc-7588c8d77ab3" -->
## Inputs

- Workflow requirements from AI app entities
- Tool capabilities from Tools and Services (01)
- Best practice documentation and operational standards

<!-- section_id: "3520c0a5-f8e0-4794-a944-3ef0e472dc38" -->
## Outputs

- Standardized operational protocols for all AI apps
- Protocol documentation with step-by-step procedures
- Integration patterns between tools and workflows

# ── Current Status ──

<!-- section_id: "e4f57895-0e88-4393-9f04-c7168345a3e2" -->
## Current Status

- **Stage**: Active (created 2026-02-25 from content migration)
- **Structure**: Full canonical entity with .0agnostic/, stages directory
- **Content**: Protocols migrated from Claude Code CLI sub_layer_0_13_protocols/
- **Protocols**: docx_operations, github_operations, and additional shared workflows

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── Current State ──

<!-- section_id: "4e969f50-82e1-4f97-b4b2-3a1307438a4e" -->
## Current State Detail

Content migrated from `sub_layer_0_10_claude_code_cli/sub_layer_0_13_protocols/`. Protocols that were previously scoped to Claude Code CLI but apply to all AI apps have been elevated here.

<!-- section_id: "98c846a3-e0ee-4608-8248-383d1553f1b1" -->
## Open Items

- [ ] Audit each protocol for true app-agnosticism — move app-specific protocols back
- [ ] Migrate protocol content into `.0agnostic/03_protocols/` standard structure
- [ ] Cross-reference protocols with Tools and Services (01) tool capabilities
- [ ] Version-tag existing protocols for change tracking

# ── References ──

<!-- section_id: "1ad02256-76a1-4390-bef0-e72c98136584" -->
## Navigation

| Resource | Location |
|----------|----------|
| Knowledge | `.0agnostic/01_knowledge/` |
| Rules | `.0agnostic/02_rules/` |
| Protocols | `.0agnostic/03_protocols/` |
| Stages | `sub_layer_0_10_group/sub_layer_0_10_99_stages/` |
| Parent | `../../0AGNOSTIC.md` |
| Sibling: Tools and Services | `../sub_layer_0_10_01_tools_and_services/0AGNOSTIC.md` |
| Sibling: AI Models | `../sub_layer_0_10_02_ai_models/0AGNOSTIC.md` |
| Sibling: Universal Tools | `../sub_layer_0_10_03_universal_tools/0AGNOSTIC.md` |
