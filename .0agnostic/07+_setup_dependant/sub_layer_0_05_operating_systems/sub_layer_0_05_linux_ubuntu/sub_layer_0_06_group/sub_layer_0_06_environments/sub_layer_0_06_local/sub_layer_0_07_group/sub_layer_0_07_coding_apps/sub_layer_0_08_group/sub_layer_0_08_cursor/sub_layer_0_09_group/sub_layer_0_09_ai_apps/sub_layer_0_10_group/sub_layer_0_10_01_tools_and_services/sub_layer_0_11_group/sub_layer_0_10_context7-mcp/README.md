---
resource_id: "8fc9989f-4238-45f4-a3b6-1fe0bfe68401"
resource_type: "readme
document"
resource_name: "README"
---
# Context7 MCP Server

Context7 MCP provides AI agents with up-to-date, version-specific documentation and code examples pulled directly from source repositories. It integrates with the Model Context Protocol (MCP) to deliver context-aware library documentation.

## Overview

Context7 is a documentation retrieval service that solves the problem of outdated or generic AI responses about libraries and frameworks. Instead of relying on potentially stale training data, Context7 fetches current documentation directly from official sources, ensuring accurate and version-specific information.

### Key Capabilities

- **Real-time Documentation Access**: Fetches current documentation from source repositories
- **Version-Specific Context**: Provides documentation for specific library versions
- **Code Examples**: Returns practical, working code examples from official sources
- **Library Resolution**: Automatically resolves library names to their documentation sources

## Features

### Context Search (`resolve-library-id`)
Search for libraries and resolve them to their Context7-compatible identifiers. This is the first step in retrieving documentation for any library.

### Context Retrieval (`get-library-docs`)
Retrieve comprehensive documentation for a specific library, including:
- API reference documentation
- Usage examples
- Configuration guides
- Best practices

### Context Management
- Caching of frequently accessed documentation
- Version tracking for documentation freshness
- Automatic fallback to cached content during API issues

## Quick Start

### 1. Obtain API Key

Get your Context7 API key from [context7.io](https://context7.io) or use the provided default key for testing.

### 2. Configure Environment

Set the following environment variables:

```bash
# Required: Your Context7 API key
export CONTEXT7_API_KEY="your-api-key-here"

# Optional: Custom API URL (defaults to official Context7 API)
export CONTEXT7_API_URL="https://api.context7.io"
```

### 3. MCP Server Configuration

Add to your MCP configuration (`mcp.json` or equivalent):

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp"],
      "env": {
        "CONTEXT7_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

### 4. Using Wrapper Scripts (Recommended)

For more reliable execution, use the automation scripts in `setup/scripts/`:

```bash
# Run the MCP manager to generate wrapper scripts
python3 setup/scripts/mcp_manager.py --scope user
```

This creates wrapper scripts that properly set environment variables including `PATH` and `HOME`.

## API Key Requirements

### CONTEXT7_API_KEY (Required)

Your Context7 API authentication key. Without this, all requests will fail with authentication errors.

**Obtaining a Key:**
1. Visit [context7.io](https://context7.io)
2. Create an account or sign in
3. Navigate to API Keys section
4. Generate a new API key

**Setting the Key:**
```bash
# Via environment variable
export CONTEXT7_API_KEY="your-key-here"

# Via MCP configuration
"env": {
  "CONTEXT7_API_KEY": "your-key-here"
}
```

### CONTEXT7_API_URL (Optional)

Custom API endpoint URL. Only needed if using a self-hosted Context7 instance or alternative endpoint.

**Default:** `https://api.context7.io`

```bash
export CONTEXT7_API_URL="https://custom-endpoint.example.com"
```

## Available Tools

### resolve-library-id

Resolves a library name to its Context7 identifier.

**Parameters:**
- `libraryName` (string, required): Name of the library to search for

**Example:**
```
Input: "react"
Output: Library ID and metadata for React documentation
```

### get-library-docs

Retrieves documentation for a specific library.

**Parameters:**
- `context7CompatibleLibraryID` (string, required): The Context7 library ID
- `topic` (string, optional): Specific topic to focus on
- `tokens` (number, optional): Maximum tokens to return (default: 10000)

**Example:**
```
Input: { "context7CompatibleLibraryID": "/facebook/react", "topic": "hooks" }
Output: Documentation about React hooks with code examples
```

## Integration with AI Tools

### Claude Code CLI

Context7 MCP is automatically available through the MCP server configuration. Use it by asking about specific libraries:

```
"Use context7 to get the latest React hooks documentation"
```

### Cursor IDE

Add to your Cursor MCP settings and the tools will be available in the agent context.

### Codex CLI

Configure via `~/.codex/config.toml`:

```toml
[mcp_servers.context7]
command = "npx"
args = ["-y", "@upstash/context7-mcp"]

[mcp_servers.context7.env]
CONTEXT7_API_KEY = "your-key-here"
```

## Directory Structure

```
context7-mcp/
├── README.md                    # This documentation
├── setup/
│   ├── README.md               # MCP automation system docs
│   ├── TROUBLESHOOTING.md      # Common issues and solutions
│   ├── scripts/
│   │   ├── mcp_manager.py      # MCP server automation
│   │   ├── codex_mcp_sync.py   # Codex configuration sync
│   │   └── mcp_concurrent_browser.py
│   ├── CONCURRENT_BROWSER_SETUP.md
│   └── 20251210_MCP_Setup_Fix.md
├── 0.12_universal_tools/
│   └── _shared/                # Shared tool configurations
├── 0.13_protocols/             # Workflow documentation
│   ├── context_retrieval_workflow.md
│   ├── context_search_workflow.md
│   └── context_management_workflow.md
└── 0.14_agent_setup/           # Agent-specific configurations
```

## Related Documentation

- **MCP Automation**: See `setup/README.md` for the complete MCP server automation system
- **Troubleshooting**: See `setup/TROUBLESHOOTING.md` for common issues
- **Protocols**: See `0.13_protocols/` for detailed workflow documentation

## Platform-Specific Notes

### Linux/Ubuntu

The MCP server runs via `npx` which requires Node.js. Ensure NVM or system Node.js is properly configured:

```bash
# Check Node.js availability
which node
which npx

# If using NVM, ensure it's sourced in your shell
source ~/.nvm/nvm.sh
```

### Claude Code CLI Specifics

Claude Code CLI manages MCP servers internally. The configuration is applied through the system's MCP configuration file, typically at `~/.config/mcp/mcp.json`.

---

**Last Updated**: 2026-01-13
**MCP Package**: `@upstash/context7-mcp`
**Status**: Active
