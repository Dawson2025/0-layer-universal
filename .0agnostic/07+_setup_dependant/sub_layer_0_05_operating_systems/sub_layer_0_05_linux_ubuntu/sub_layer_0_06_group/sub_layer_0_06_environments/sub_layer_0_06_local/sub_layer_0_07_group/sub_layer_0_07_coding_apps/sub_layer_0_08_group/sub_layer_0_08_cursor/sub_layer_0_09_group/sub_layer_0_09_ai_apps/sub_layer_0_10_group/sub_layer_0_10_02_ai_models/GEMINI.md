<!-- resource_id: "2b60aec3-e8b9-4221-95c4-72d8fcd4aba5" -->
# Gemini Context



## Identity

**Entity**: AI Models
**Sub-Layer**: 0.10
**Type**: Feature (shared across all AI apps)
**Feature Number**: 02 (second in sequence — understand model capabilities after knowing your tools)
**Scope**: AI model definitions, capabilities, pricing, and selection guidance shared across all AI app entities

**Specificity Chain**: OS (05) → Linux Ubuntu (05) → Environments (06) → Local (06) → Coding Apps (07) → Cursor (08) → AI Apps (09) → **AI Models (10)**

## Key Behaviors

- Contains model knowledge for all providers (Claude 3.5 Haiku, Sonnet, Opus; GPT-4o; Gemini; etc.)
- Model capabilities, context windows, pricing, and selection criteria documented per model
- Knowledge topics organized in `.0agnostic/01_knowledge/` by provider and model family
- Does NOT contain app-specific model configuration — that stays in each AI app entity
- Model pricing updates tracked with effective dates for budget calculations
- Cross-references Tools and Services (01) for API cost tracking integration

## Delegation Contract

**Children** (level 11): Individual model definitions (future — per-provider or per-model entities)
**Parent** (level 09): AI Apps Category
**Siblings**: 01_tools_and_services, 03_universal_tools, 04_protocols, 05_agent_setup (features), claude_code_cli, codex_cli, cursor_agent, gemini_cli (further_specificity)

## Inputs

- Model documentation from providers (Anthropic, OpenAI, Google)
- Pricing pages and capability announcements
- Benchmark results and comparison data

## Outputs

- Structured model capability reference for all AI apps
- Pricing documentation for budget planning
- Model selection guidance based on task requirements


## Current Status

- **Stage**: Active (created 2026-02-25 from content migration)
- **Structure**: Full canonical entity with .0agnostic/, stages directory
- **Content**: Model knowledge migrated from Claude Code CLI sub_layer_0_11_ai_models/
- **Coverage**: Claude model family documented; other providers pending expansion


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
