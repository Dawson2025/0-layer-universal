---
resource_id: "665aefb1-1307-43bb-a3b6-997231da23a4"
resource_type: "readme_document"
resource_name: "README"
---
# Tavily MCP Server

<!-- section_id: "b13673a0-7500-46c6-930c-d52fac7e50ad" -->
## Overview

Tavily MCP (Model Context Protocol) server provides AI agents with powerful web search capabilities through the Tavily API. This integration enables Claude Code CLI and other AI tools to perform real-time web searches, news lookups, and answer generation directly within your development workflow.

**Platform:** Linux Ubuntu | **Environment:** Local | **AI App:** Claude Code CLI

<!-- section_id: "a8b8e35c-47fa-4a1f-890b-5542c468bf2c" -->
## Features

<!-- section_id: "c81b728a-fd1f-4f33-aa8d-1b0623a50721" -->
### Core Capabilities

| Feature | Description |
|---------|-------------|
| **Web Search** | General-purpose web search with customizable depth and filtering |
| **News Search** | Dedicated news article search with time-based filtering |
| **Answer Generation** | AI-powered answer synthesis from search results |
| **Domain Filtering** | Include or exclude specific domains from results |
| **Content Extraction** | Retrieve raw content from search result pages |

<!-- section_id: "7366ecfd-0f65-4d57-9c52-04fb9b7d0a0e" -->
### Search Parameters

- **search_depth**: `basic` (fast) or `advanced` (comprehensive)
- **max_results**: Control number of results (1-20)
- **include_domains**: Whitelist specific domains
- **exclude_domains**: Blacklist specific domains
- **include_answer**: Get AI-synthesized answers
- **include_raw_content**: Extract full page content

<!-- section_id: "002336f7-293c-4b20-9e8c-0bcc67a0ad02" -->
## Quick Start

<!-- section_id: "344f7e85-704d-4a91-b92e-300ccd4b23fb" -->
### 1. Get Your API Key

1. Visit [https://tavily.com](https://tavily.com)
2. Sign up for a free account
3. Navigate to your dashboard
4. Copy your API key

<!-- section_id: "318e6d92-1dcf-4d54-b9bc-4e931e235f9b" -->
### 2. Configure Environment Variable

```bash
# Add to your shell profile (~/.bashrc, ~/.zshrc, etc.)
export TAVILY_API_KEY="tvly-your-api-key-here"

# Reload your shell
source ~/.bashrc
```

<!-- section_id: "fc9bd705-33cd-4973-a973-e48c9160fb01" -->
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

<!-- section_id: "376d6801-318f-4adf-afb7-78d53ea65da2" -->
### 4. Verify Installation

Restart Claude Code CLI and verify the server is available:

```bash
claude --mcp-servers
```

<!-- section_id: "4a3f86a5-01bd-476c-b631-4557f57b1f65" -->
## Usage Examples

<!-- section_id: "33ba5e47-47cf-4086-84e0-4b4b36e8b730" -->
### Basic Web Search

```
Search the web for "Python best practices 2024"
```

<!-- section_id: "81c0cb71-5aae-4a36-9669-b1fdee49cc2f" -->
### News Search

```
Find recent news about AI regulations in the EU
```

<!-- section_id: "5cfbf5a8-1a65-4d3d-85fa-3fe5305e3e5d" -->
### Domain-Specific Search

```
Search for React tutorials only from official documentation sites
```

<!-- section_id: "6f554d3e-9c0a-44fa-b960-eb194af24644" -->
### Answer Generation

```
What is the current market cap of major tech companies? Include an AI-generated summary.
```

<!-- section_id: "811da310-534b-4800-9988-2f548389cc7e" -->
## API Tiers and Limits

| Tier | Monthly Searches | Rate Limit | Price |
|------|------------------|------------|-------|
| Free | 1,000 | 10/min | $0 |
| Basic | 10,000 | 100/min | $50/mo |
| Pro | 100,000 | 500/min | $200/mo |
| Enterprise | Unlimited | Custom | Contact |

<!-- section_id: "4be65240-3885-406c-a347-3b152664ff78" -->
## Available Tools

The Tavily MCP server exposes the following tools:

<!-- section_id: "c67a8775-82c1-49fe-ac0e-fabf373b6db1" -->
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

<!-- section_id: "03350099-3063-4870-8f45-e8b2cdbf3b0a" -->
### `tavily_news_search`
Search specifically for news articles.

**Parameters:**
- `query` (required): News search query
- `days`: Number of days back to search (default: 7)
- `max_results`: Number of results (default: 5)

<!-- section_id: "547cc764-4e43-432c-b8eb-4de373640e90" -->
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
├── 0.12_universal_tools/
│   └── _shared/
├── 0.13_protocols/             # Workflow documentation
│   ├── web-research-workflow.md
│   ├── news-monitoring-workflow.md
│   └── fact-checking-workflow.md
└── 0.14_agent_setup/
```

<!-- section_id: "1f6bdc4c-db2a-4494-a0e6-5fa7bfaffb88" -->
## Integration Notes

<!-- section_id: "9e6f57da-3fdf-4246-880f-94607a4260ad" -->
### Claude Code CLI Specific

- Tavily searches complement the built-in `WebSearch` tool
- Use for specialized searches requiring domain filtering or news focus
- Combine with browser MCP for comprehensive web research

<!-- section_id: "058ef826-bc52-43a1-b7c6-842fcf54e08e" -->
### Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `TAVILY_API_KEY` | Yes | Your Tavily API key |

<!-- section_id: "f66867d8-1d29-438b-b3df-e9a08dc9e7f7" -->
## Canonical Documentation

For shared MCP server documentation across all platforms:
- `../../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/tavily-mcp/`

<!-- section_id: "2c40a0b9-adc0-43d6-bffb-1f9e390fc7eb" -->
## Related Resources

- [Tavily Official Documentation](https://docs.tavily.com)
- [Tavily MCP GitHub Repository](https://github.com/tavily-ai/tavily-mcp)
- [MCP Protocol Specification](https://modelcontextprotocol.io)

<!-- section_id: "9dd9b204-52af-44ba-9fec-b953ae38f725" -->
## Support

For issues specific to this setup:
- See `setup/TROUBLESHOOTING.md` for common problems
- Check the MCP automation system in `setup/README.md`
