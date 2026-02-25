# 0AGNOSTIC.md — sub_layer_0_10_03_universal_tools

# ═══ STATIC CONTEXT (always loaded) ═══

# ── Entity Definition ──

## Identity

**Entity**: Universal Tools
**Sub-Layer**: 0.10
**Type**: Feature (shared across all AI apps)
**Feature Number**: 03 (third in sequence — shared dev tools that work across any AI app)
**Scope**: Shared development tools usable by any AI app, independent of specific AI platform

**Specificity Chain**: OS (05) → Linux Ubuntu (05) → Environments (06) → Local (06) → Coding Apps (07) → Cursor (08) → AI Apps (09) → **Universal Tools (10)**

## Key Behaviors

- Contains tools like docx_ai_tool and other cross-platform development utilities
- Children are individual tool entities in `sub_layer_0_11_group/`
- Tools here must be AI-app-agnostic — if a tool only works with one AI app, it belongs in that app's entity
- Each child tool entity contains its own documentation, configuration, and usage patterns
- Tool dependencies and compatibility tracked in knowledge base

## Delegation Contract

**Children** (level 11): Individual tool entities (docx_ai_tool, etc.)
**Parent** (level 09): AI Apps Category
**Siblings**: 01_tools_and_services, 02_ai_models, 04_protocols, 05_agent_setup (features), claude_code_cli, codex_cli, cursor_agent, gemini_cli (further_specificity)

## Inputs

- Tool source code and documentation
- Configuration templates
- Dependency requirements

## Outputs

- Organized tool documentation accessible to all AI apps
- Configuration patterns and usage guides
- Tool compatibility matrices

# ── Current Status ──

## Current Status

- **Stage**: Active (created 2026-02-25 from content migration)
- **Structure**: Full canonical entity with .0agnostic/, stages directory, children group
- **Content**: Tools migrated from Claude Code CLI sub_layer_0_12_universal_tools/
- **Children**: docx_ai_tool and other shared tools in sub_layer_0_11_group/

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── Current State ──

## Current State Detail

Content migrated from `sub_layer_0_10_claude_code_cli/sub_layer_0_12_universal_tools/`. Tools that were previously scoped to Claude Code CLI but are actually app-agnostic have been moved here.

## Open Items

- [ ] Renumber tool children from sub_layer_0_12_* to sub_layer_0_11_*
- [ ] Audit each tool for true app-agnosticism — move app-specific tools back
- [ ] Create 0AGNOSTIC.md for each tool child entity
- [ ] Document tool dependencies and compatibility

# ── References ──

## Navigation

| Resource | Location |
|----------|----------|
| Knowledge | `.0agnostic/01_knowledge/` |
| Rules | `.0agnostic/02_rules/` |
| Protocols | `.0agnostic/03_protocols/` |
| Children (tools) | `sub_layer_0_11_group/` |
| Stages | `sub_layer_0_10_group/sub_layer_0_10_99_stages/` |
| Parent | `../../0AGNOSTIC.md` |
| Sibling: Tools and Services | `../sub_layer_0_10_01_tools_and_services/0AGNOSTIC.md` |
| Sibling: AI Models | `../sub_layer_0_10_02_ai_models/0AGNOSTIC.md` |
