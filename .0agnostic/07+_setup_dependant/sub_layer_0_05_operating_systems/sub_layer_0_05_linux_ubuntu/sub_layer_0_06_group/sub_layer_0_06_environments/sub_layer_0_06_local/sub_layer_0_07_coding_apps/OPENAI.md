# OpenAI Context

## Identity

**Entity**: Coding Apps
**Sub-Layer**: 0.07
**Type**: Increased Specificity (narrows from Local Environment → Coding applications)
**Scope**: All coding applications and their AI integrations on the local environment

**Specificity Chain**: OS (05) → Linux Ubuntu (05) → Environments (06) → Local (06) → **Coding Apps (07)**

## Key Behaviors

- Rules and protocols here cascade to all child coding apps (currently: Cursor at level 08)
- Legacy shared content preserved in `.0agnostic/01_knowledge/legacy_shared/` (pre-restructuring)
- Future coding apps (VS Code, Neovim, etc.) would be added as siblings to Cursor at level 08

## Delegation Contract

**Children** (level 08): Cursor IDE (sub_layer_0_08_cursor)
**Parent** (level 06): Local Environment


## Current Status

**State**: Restructuring complete
**Scope**: 1 child coding app (Cursor), which contains AI Apps (level 09) → 4 AI app entities (level 10)
**Content**: Entity structure created, legacy `_shared/` content preserved in `.0agnostic/01_knowledge/legacy_shared/`, child moved to `sub_layer_0_08_group/`
**Readiness**: Structure ready, awaiting knowledge population and agnostic-sync

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
