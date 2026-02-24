# OpenAI Context

## Identity

**Entity**: AI Apps Category
**Sub-Layer**: 0.09
**Type**: Increased Specificity (narrows from Coding Apps → AI-powered coding tools)
**Scope**: All AI-powered coding assistants and their shared infrastructure

**Specificity Chain**: OS (05) → Linux Ubuntu (05) → Environments (06) → Local (06) → Coding Apps (07) → Cursor (08) → **AI Apps (09)**

## Key Behaviors

- Shared protocols, knowledge, and rules cascade to all child AI app entities (level 10)
- MCP server knowledge shared across AI apps lives in `.0agnostic/01_knowledge/mcp_servers/`
- Browser automation protocol applies to all AI apps that use browser-based tools
- Each child AI app (Claude Code CLI, Codex CLI, Cursor Agent, Gemini CLI) is a full entity at level 10

## Delegation Contract

**Children** (level 10): claude_code_cli, codex_cli, cursor_agent, gemini_cli
**Parent** (level 08): Cursor


## Current Status

**State**: Restructuring in progress
**Scope**: 4 AI app entities at level 10, shared MCP server knowledge, browser automation protocol
**Content**: Shared protocols migrated to `.0agnostic/03_protocols/`, shared MCP knowledge migrated to `.0agnostic/01_knowledge/mcp_servers/`
**Readiness**: Entity structure created, children in `sub_layer_0_10_group/`

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
