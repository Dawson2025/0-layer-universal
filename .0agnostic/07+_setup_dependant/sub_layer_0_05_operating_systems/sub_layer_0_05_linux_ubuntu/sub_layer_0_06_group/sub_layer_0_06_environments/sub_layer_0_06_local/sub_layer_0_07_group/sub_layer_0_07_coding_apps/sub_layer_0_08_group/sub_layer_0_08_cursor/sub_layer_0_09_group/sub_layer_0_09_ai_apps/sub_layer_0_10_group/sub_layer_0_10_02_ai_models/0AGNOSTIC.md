---
resource_id: "f6a79f4a-4f60-48ed-a9ef-096c09108b54"
resource_type: "agnostic_document"
resource_name: "0AGNOSTIC"
---
# 0AGNOSTIC.md — sub_layer_0_10_02_ai_models

# ═══ STATIC CONTEXT (always loaded) ═══

# ── Entity Definition ──

<!-- section_id: "ea2da678-1ce5-4ec9-828f-2c8ee9930c8f" -->
## Identity

**Entity**: AI Models
**Sub-Layer**: 0.10
**Type**: Feature (shared across all AI apps)
**Feature Number**: 02 (second in sequence — understand model capabilities after knowing your tools)
**Scope**: AI model definitions, capabilities, pricing, and selection guidance shared across all AI app entities

**Specificity Chain**: OS (05) → Linux Ubuntu (05) → Environments (06) → Local (06) → Coding Apps (07) → Cursor (08) → AI Apps (09) → **AI Models (10)**

<!-- section_id: "ba2928bf-9819-43cd-b074-39b6916a7904" -->
## Key Behaviors

- Contains model knowledge for all providers (Claude 3.5 Haiku, Sonnet, Opus; GPT-4o; Gemini; etc.)
- Model capabilities, context windows, pricing, and selection criteria documented per model
- Knowledge topics organized in `.0agnostic/01_knowledge/` by provider and model family
- Does NOT contain app-specific model configuration — that stays in each AI app entity
- Model pricing updates tracked with effective dates for budget calculations
- Cross-references Tools and Services (01) for API cost tracking integration

<!-- section_id: "c310a967-21a4-4605-8bf4-dcca862fc253" -->
## Delegation Contract

**Children** (level 11): Individual model definitions (future — per-provider or per-model entities)
**Parent** (level 09): AI Apps Category
**Siblings**: 01_tools_and_services, 03_universal_tools, 04_protocols, 05_agent_setup (features), claude_code_cli, codex_cli, cursor_agent, gemini_cli (further_specificity)

<!-- section_id: "02fb18ac-58bc-4797-8499-01e44ffc8121" -->
## Inputs

- Model documentation from providers (Anthropic, OpenAI, Google)
- Pricing pages and capability announcements
- Benchmark results and comparison data

<!-- section_id: "1b1de34a-4a42-4583-89c5-d3d9f3ca69c2" -->
## Outputs

- Structured model capability reference for all AI apps
- Pricing documentation for budget planning
- Model selection guidance based on task requirements

# ── Current Status ──

<!-- section_id: "481f6dea-0193-4761-b640-b550de5b076c" -->
## Current Status

- **Stage**: Active (created 2026-02-25 from content migration)
- **Structure**: Full canonical entity with .0agnostic/, stages directory
- **Content**: Model knowledge migrated from Claude Code CLI sub_layer_0_11_ai_models/
- **Coverage**: Claude model family documented; other providers pending expansion

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── Current State ──

<!-- section_id: "31032288-a887-4b10-9c27-b75c03fdf1c0" -->
## Current State Detail

Content migrated from `sub_layer_0_10_claude_code_cli/sub_layer_0_11_ai_models/`. Currently focused on Claude model family. Other provider models (OpenAI, Google, etc.) to be added as knowledge topics.

<!-- section_id: "5d6b95a9-ad40-429e-9edb-b8de128506ac" -->
## Open Items

- [ ] Expand model knowledge beyond Claude family (GPT, Gemini, etc.)
- [ ] Create per-provider knowledge topic directories
- [ ] Add model comparison matrices and selection decision trees
- [ ] Link pricing data to Tools and Services (01) budget tracking

# ── References ──

<!-- section_id: "12dc4e17-53ea-4388-858c-10b273f7ba88" -->
## Navigation

| Resource | Location |
|----------|----------|
| Knowledge | `.0agnostic/01_knowledge/` |
| Rules | `.0agnostic/02_rules/` |
| Protocols | `.0agnostic/03_protocols/` |
| Children | `sub_layer_0_11_group/` |
| Stages | `sub_layer_0_10_group/sub_layer_0_10_99_stages/` |
| Parent | `../../0AGNOSTIC.md` |
| Sibling: Tools and Services | `../sub_layer_0_10_01_tools_and_services/0AGNOSTIC.md` |
