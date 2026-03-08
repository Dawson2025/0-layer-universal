---
resource_id: "653420f3-2e86-471e-a442-15c7f0c0df52"
resource_type: "agnostic_document"
resource_name: "0AGNOSTIC"
---
# 0AGNOSTIC.md — sub_layer_0_10_05_agent_setup

# ═══ STATIC CONTEXT (always loaded) ═══

# ── Entity Definition ──

<!-- section_id: "3cad2c8e-10e1-4034-8bbf-bc43e394aa6c" -->
## Identity

**Entity**: Agent Setup
**Sub-Layer**: 0.10
**Type**: Feature (shared across all AI apps)
**Feature Number**: 05 (last in sequence — uses knowledge from features 01-04 to configure agents)
**Scope**: Shared agent configuration patterns, templates, settings, and customization across all AI app entities

**Specificity Chain**: OS (05) → Linux Ubuntu (05) → Environments (06) → Local (06) → Coding Apps (07) → Cursor (08) → AI Apps (09) → **Agent Setup (10)**

<!-- section_id: "013ac874-0c9a-41b0-9ada-cd6ecdf13d75" -->
## Key Behaviors

- Last in feature sequence — depends on knowledge from: Tools and Services (01), AI Models (02), Universal Tools (03), Protocols (04)
- Contains agent templates, default settings, and customization patterns shared across all AI apps
- Agent configuration patterns must be app-agnostic — app-specific agent configs stay in their respective entity
- References AI Models (02) for model selection in agent configurations
- References Protocols (04) for behavioral protocol bindings
- Templates support instantiation for any AI app (Claude Code, Cursor Agent, Codex, Gemini)

<!-- section_id: "157e8fcb-463b-417c-9268-b1624da41e0b" -->
## Delegation Contract

**Children** (level 11): Individual agent template or configuration entities (future)
**Parent** (level 09): AI Apps Category
**Siblings**: 01_tools_and_services, 02_ai_models, 03_universal_tools, 04_protocols (features), claude_code_cli, codex_cli, cursor_agent, gemini_cli (further_specificity)

<!-- section_id: "7c71a590-fdac-49a4-85f1-1fd7160e6254" -->
## Inputs

- Tool capabilities from Tools and Services (01)
- Model specifications from AI Models (02)
- Available tools from Universal Tools (03)
- Operational protocols from Protocols (04)
- Agent requirements from individual AI app entities

<!-- section_id: "1d4a1afe-5a53-4b3c-82b1-747ee7498ec4" -->
## Outputs

- Reusable agent configuration templates
- Default agent settings and customization patterns
- Agent setup guides for new AI app onboarding

# ── Current Status ──

<!-- section_id: "d5647bc5-5990-4888-a41b-453a9e14fc34" -->
## Current Status

- **Stage**: Created (2026-02-25, awaiting content population)
- **Structure**: Full canonical entity with .0agnostic/, stages directory
- **Content**: Awaiting population — will draw from patterns observed across AI app entities
- **Dependencies**: Builds on features 01-04; those should stabilize first

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── Current State ──

<!-- section_id: "7c0dd3bb-252a-4916-9f75-a3f166b2e235" -->
## Current State Detail

Entity created as the capstone feature in the AI Apps feature sequence. No content migrated yet — this entity will be populated by extracting common agent configuration patterns from individual AI app entities (claude_code_cli, cursor_agent, codex_cli, gemini_cli) once those are established.

<!-- section_id: "a2f61716-d467-4afb-8759-2a30af7482cf" -->
## Open Items

- [ ] Survey existing AI app entities for common agent configuration patterns
- [ ] Extract shared templates and settings into `.0agnostic/01_knowledge/`
- [ ] Create agent setup protocol in `.0agnostic/03_protocols/`
- [ ] Document model selection criteria for agent configurations (cross-ref AI Models 02)
- [ ] Build onboarding guide for adding new AI app entities

# ── References ──

<!-- section_id: "c40f617b-0019-48b3-913d-a447b74def70" -->
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
| Sibling: Protocols | `../sub_layer_0_10_04_protocols/0AGNOSTIC.md` |
