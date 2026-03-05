<!-- resource_id: "807e87be-b40c-441e-8ddb-01f5956f0e13" -->
# OpenAI Context



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


## Current Status

- **Stage**: Active (created 2026-02-25 from content migration)
- **Structure**: Full canonical entity with .0agnostic/, stages directory, children group
- **Content**: Tools migrated from Claude Code CLI sub_layer_0_12_universal_tools/
- **Children**: docx_ai_tool and other shared tools in sub_layer_0_11_group/


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
