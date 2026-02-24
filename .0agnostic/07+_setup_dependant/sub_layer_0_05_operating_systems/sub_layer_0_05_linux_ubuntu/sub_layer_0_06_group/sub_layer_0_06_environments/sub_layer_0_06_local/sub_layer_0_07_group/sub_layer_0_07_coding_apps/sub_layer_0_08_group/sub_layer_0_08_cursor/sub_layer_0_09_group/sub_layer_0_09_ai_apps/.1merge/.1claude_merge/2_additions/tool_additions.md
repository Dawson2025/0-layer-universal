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
