# OpenAI Context



## Identity

**Entity**: Protocols
**Sub-Layer**: 0.10
**Type**: Feature (shared across all AI apps)
**Feature Number**: 04 (fourth in sequence — operational protocols that govern how AI apps behave)
**Scope**: Shared operational protocols for all AI apps, including document operations, git workflows, and service integrations

**Specificity Chain**: OS (05) → Linux Ubuntu (05) → Environments (06) → Local (06) → Coding Apps (07) → Cursor (08) → AI Apps (09) → **Protocols (10)**

## Key Behaviors

- Contains protocols like docx_operations, github_operations, and other cross-app workflows
- Protocols stored in `.0agnostic/03_protocols/` following the standard convention
- Protocols here must be AI-app-agnostic — app-specific protocols stay in their respective entity
- References Tools and Services (01) for tool-specific protocol bindings
- References AI Models (02) for model-specific protocol variations
- Protocol versioning tracked to handle breaking changes

## Delegation Contract

**Children** (level 11): Individual protocol definitions (future — if protocols grow complex enough)
**Parent** (level 09): AI Apps Category
**Siblings**: 01_tools_and_services, 02_ai_models, 03_universal_tools, 05_agent_setup (features), claude_code_cli, codex_cli, cursor_agent, gemini_cli (further_specificity)

## Inputs

- Workflow requirements from AI app entities
- Tool capabilities from Tools and Services (01)
- Best practice documentation and operational standards

## Outputs

- Standardized operational protocols for all AI apps
- Protocol documentation with step-by-step procedures
- Integration patterns between tools and workflows


## Current Status

- **Stage**: Active (created 2026-02-25 from content migration)
- **Structure**: Full canonical entity with .0agnostic/, stages directory
- **Content**: Protocols migrated from Claude Code CLI sub_layer_0_13_protocols/
- **Protocols**: docx_operations, github_operations, and additional shared workflows


## OpenAI-Specific Notes

### Function Calling
When using OpenAI function calling:
- Read .0agnostic/ resources for detailed instructions
- Check episodic memory for context
- Follow multi-agent sync rules for shared files

### Context Window Management
- 0AGNOSTIC.md is lean (<400 tokens)
- Load .0agnostic/ resources on-demand
- Avoid loading everything upfront

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
