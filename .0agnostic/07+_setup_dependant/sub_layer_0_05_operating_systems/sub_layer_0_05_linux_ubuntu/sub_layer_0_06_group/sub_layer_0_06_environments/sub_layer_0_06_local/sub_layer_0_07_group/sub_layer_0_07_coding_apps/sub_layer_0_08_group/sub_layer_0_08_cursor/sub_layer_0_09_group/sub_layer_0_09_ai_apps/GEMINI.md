# Gemini Context

## Identity

**Entity**: AI Apps Category
**Sub-Layer**: 0.09
**Type**: Increased Specificity (narrows from Coding Apps → AI-powered coding tools)
**Scope**: All AI-powered coding assistants and their shared infrastructure

**Specificity Chain**: OS (05) → Linux Ubuntu (05) → Environments (06) → Local (06) → Coding Apps (07) → Cursor (08) → **AI Apps (09)**

## Key Behaviors

- Shared protocols, knowledge, and rules cascade to all child AI app entities (level 10)
- MCP server knowledge shared across AI apps lives in `.0agnostic/01_knowledge/mcp_servers/`
- **MCP API cost tracking** — protocol and budget enforcement rule at this level apply to ALL paid MCP API calls across all child AI apps
- Browser automation protocol applies to all AI apps that use browser-based tools
- **Two entity types at level 10**: *Features* (numbered, shared infrastructure) and *Further Specificity* (unnumbered, app-specific config). Features provide shared tools, models, protocols, and agent setup; app-specific entities inherit from and can override shared features.

## Triggers

| Situation | Action |
|-----------|--------|
| About to call a paid MCP API tool | Read `.0agnostic/02_rules/dynamic/MCP_API_BUDGET_ENFORCEMENT/` — check budget before calling |
| After calling a paid MCP API tool | Follow `.0agnostic/03_protocols/mcp_api_cost_tracking_protocol.md` — log usage |
| User asks about API spending | Read `memory/mcp_api_usage.md` and report budget status |
| Extracting content from Perplexity | Read `.0agnostic/02_rules/static/perplexity_extraction_rules.md` |

## Delegation Contract

**Children** (level 10):
- *Features* (numbered, shared): 01_tools_and_services, 02_ai_models, 03_universal_tools, 04_protocols, 05_agent_setup
- *Further Specificity* (app-specific): claude_code_cli, codex_cli, cursor_agent, gemini_cli
**Parent** (level 08): Cursor


## Current Status

**State**: Active
**Scope**: 5 shared feature entities + 4 AI app entities at level 10
**Content**: Shared features contain MCP servers, AI models, universal tools, protocols, agent setup. App-specific entities contain per-app config and overrides.
**Readiness**: Restructured 2026-02-25: features extracted from Claude Code CLI to shared level

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
