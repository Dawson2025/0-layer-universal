# Tavily MCP Server

## Overview

Tavily MCP (Model Context Protocol) server provides AI agents with powerful web search capabilities through the Tavily API. This integration enables Claude Code CLI and other AI tools to perform real-time web searches, news lookups, and answer generation directly within your development workflow.

**Platform:** Linux Ubuntu | **Environment:** Local | **AI App:** Claude Code CLI

## Features

### Core Capabilities

| Feature | Description |
|---------|-------------|
| **Web Search** | General-purpose web search with customizable depth and filtering |
| **News Search** | Dedicated news article search with time-based filtering |
| **Answer Generation** | AI-powered answer synthesis from search results |
| **Domain Filtering** | Include or exclude specific domains from results |
| **Content Extraction** | Retrieve raw content from search result pages |

### Search Parameters

- **search_depth**: `basic` (fast) or `advanced` (comprehensive)
- **max_results**: Control number of results (1-20)
- **include_domains**: Whitelist specific domains
- **exclude_domains**: Blacklist specific domains
- **include_answer**: Get AI-synthesized answers
- **include_raw_content**: Extract full page content

## Quick Start

### 1. Get Your API Key

1. Visit [https://tavily.com](https://tavily.com)
2. Sign up for a free account
3. Navigate to your dashboard
4. Copy your API key

### 2. Configure Environment Variable

```bash
# Add to your shell profile (~/.bashrc, ~/.zshrc, etc.)
export TAVILY_API_KEY="tvly-your-api-key-here"

# Reload your shell
source ~/.bashrc
```

### 3. MCP Configuration

Add the Tavily server to your MCP configuration (`~/.config/mcp/mcp.json` or project-level `.mcp.json`):

```json
{
  "mcpServers": {
    "tavily": {
      "command": "npx",
      "args": ["-y", "@tavily/mcp"],
      "env": {
        "TAVILY_API_KEY": "${TAVILY_API_KEY}"
      }
    }
  }
}
```

### 4. Verify Installation

Restart Claude Code CLI and verify the server is available:

```bash
claude --mcp-servers
```

## Usage Examples

### Basic Web Search

```
Search the web for "Python best practices 2024"
```

### News Search

```
Find recent news about AI regulations in the EU
```

### Domain-Specific Search

```
Search for React tutorials only from official documentation sites
```

### Answer Generation

```
What is the current market cap of major tech companies? Include an AI-generated summary.
```

## API Tiers and Limits

| Tier | Monthly Searches | Rate Limit | Price |
|------|------------------|------------|-------|
| Free | 1,000 | 10/min | $0 |
| Basic | 10,000 | 100/min | $50/mo |
| Pro | 100,000 | 500/min | $200/mo |
| Enterprise | Unlimited | Custom | Contact |

## Available Tools

The Tavily MCP server exposes the following tools:

### `tavily_search`
General web search with full parameter control.

**Parameters:**
- `query` (required): Search query string
- `search_depth`: `basic` | `advanced`
- `max_results`: Number of results (default: 5)
- `include_domains`: Array of domains to include
- `exclude_domains`: Array of domains to exclude
- `include_answer`: Boolean to include AI answer
- `include_raw_content`: Boolean to include full page content

### `tavily_news_search`
Search specifically for news articles.

**Parameters:**
- `query` (required): News search query
- `days`: Number of days back to search (default: 7)
- `max_results`: Number of results (default: 5)

## Directory Structure

```
tavily-mcp/
├── README.md                    # This file
├── setup/
│   ├── README.md               # MCP automation system docs
│   ├── TROUBLESHOOTING.md      # Common issues and solutions
│   └── scripts/
│       ├── mcp_manager.py      # Core MCP server setup
│       ├── codex_mcp_sync.py   # Codex CLI sync
│       └── mcp_concurrent_browser.py
├── 0.07_universal_tools/
│   └── _shared/
├── 0.08_protocols/             # Workflow documentation
│   ├── web-research-workflow.md
│   ├── news-monitoring-workflow.md
│   └── fact-checking-workflow.md
└── 0.09_agent_setup/
```

## Integration Notes

### Claude Code CLI Specific

- Tavily searches complement the built-in `WebSearch` tool
- Use for specialized searches requiring domain filtering or news focus
- Combine with browser MCP for comprehensive web research

### Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `TAVILY_API_KEY` | Yes | Your Tavily API key |

## Canonical Documentation

For shared MCP server documentation across all platforms:
- `../../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/tavily-mcp/`

## Related Resources

- [Tavily Official Documentation](https://docs.tavily.com)
- [Tavily MCP GitHub Repository](https://github.com/tavily-ai/tavily-mcp)
- [MCP Protocol Specification](https://modelcontextprotocol.io)

## Support

For issues specific to this setup:
- See `setup/TROUBLESHOOTING.md` for common problems
- Check the MCP automation system in `setup/README.md`
