# Claude Code Context

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
- Each child AI app (Claude Code CLI, Codex CLI, Cursor Agent, Gemini CLI) is a full entity at level 10

## Triggers

| Situation | Action |
|-----------|--------|
| About to call a paid MCP API tool | Read `.0agnostic/02_rules/dynamic/MCP_API_BUDGET_ENFORCEMENT/` — check budget before calling |
| After calling a paid MCP API tool | Follow `.0agnostic/03_protocols/mcp_api_cost_tracking_protocol.md` — log usage |
| User asks about API spending | Read `memory/mcp_api_usage.md` and report budget status |
| Extracting content from Perplexity | Read `.0agnostic/02_rules/static/perplexity_extraction_rules.md` |

## Delegation Contract

**Children** (level 10): claude_code_cli, codex_cli, cursor_agent, gemini_cli
**Parent** (level 08): Cursor


## Current Status

**State**: Active
**Scope**: 4 AI app entities at level 10, shared MCP server knowledge, browser automation protocol, MCP API cost tracking
**Content**: Shared protocols in `.0agnostic/03_protocols/` (browser automation, MCP cost tracking), shared knowledge in `.0agnostic/01_knowledge/` (MCP servers, cost tracking), budget enforcement rule in `.0agnostic/02_rules/dynamic/`
**Readiness**: Entity structure created, children in `sub_layer_0_10_group/`, cost tracking system active

## Claude-Specific Rules

### CLAUDE.md Integration
This file is auto-generated from 0AGNOSTIC.md. Edit 0AGNOSTIC.md to make changes.

### Tool Usage
- Use Read tool to load .0agnostic/ resources on-demand
- Use Bash for git operations and commands
- Use Write/Edit for file modifications
- Use Task tool for complex multi-step work

### Session Continuity
- Read .0agnostic/episodic_memory/index.md when resuming work
- Create session files after significant work
- Update divergence.log when modifying outputs

# Claude-Specific Additions for AI Apps (Level 09)

## Perplexity Extraction Skill

The `/perplexity-extract` skill is registered as a Claude Code skill at:
`.claude/skills/perplexity-extract/SKILL.md`

This skill requires the Claude in Chrome MCP server to be active. Key tools used:
- `mcp__claude-in-chrome__tabs_context_mcp` — get browser context
- `mcp__claude-in-chrome__tabs_create_mcp` — create fresh tab
- `mcp__claude-in-chrome__navigate` — navigate to Perplexity URL
- `mcp__claude-in-chrome__javascript_tool` — execute React fiber extraction
- `mcp__claude-in-chrome__get_page_text` — capture answer text
- `mcp__claude-in-chrome__computer` — scroll through answers

## MCP Server Dependencies

AI apps at this level share MCP server knowledge in `.0agnostic/01_knowledge/mcp_servers/`.
Claude Code specifically uses these MCP servers:
- Claude in Chrome (browser automation)
- Perplexity MCP (API queries — distinct from page extraction)
- Playwright (alternative browser automation)

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
