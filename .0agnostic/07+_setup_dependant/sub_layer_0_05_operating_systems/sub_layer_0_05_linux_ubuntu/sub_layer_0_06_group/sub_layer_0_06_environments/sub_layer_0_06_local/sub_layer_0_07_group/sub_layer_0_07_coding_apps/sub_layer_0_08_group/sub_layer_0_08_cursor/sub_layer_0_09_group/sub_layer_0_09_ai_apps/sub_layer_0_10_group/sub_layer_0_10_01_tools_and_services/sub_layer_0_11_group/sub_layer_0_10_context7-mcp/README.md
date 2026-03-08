---
resource_id: "8fc9989f-4238-45f4-a3b6-1fe0bfe68401"
resource_type: "readme_document"
resource_name: "README"
---
# Context7 MCP Server

Context7 MCP provides AI agents with up-to-date, version-specific documentation and code examples pulled directly from source repositories. It integrates with the Model Context Protocol (MCP) to deliver context-aware library documentation.

<!-- section_id: "1b0192d0-222b-4b2f-a481-d177195bc64c" -->
## Overview

Context7 is a documentation retrieval service that solves the problem of outdated or generic AI responses about libraries and frameworks. Instead of relying on potentially stale training data, Context7 fetches current documentation directly from official sources, ensuring accurate and version-specific information.

<!-- section_id: "10ea1b5a-0e36-4f6f-b507-a92a2403360e" -->
### Key Capabilities

- **Real-time Documentation Access**: Fetches current documentation from source repositories
- **Version-Specific Context**: Provides documentation for specific library versions
- **Code Examples**: Returns practical, working code examples from official sources
- **Library Resolution**: Automatically resolves library names to their documentation sources

<!-- section_id: "b9ae331b-7603-4847-9b61-55eb15abd07b" -->
## Features

<!-- section_id: "f5b7f4ff-45d9-4d85-8066-1eda0b2e75e1" -->
### Context Search (`resolve-library-id`)
Search for libraries and resolve them to their Context7-compatible identifiers. This is the first step in retrieving documentation for any library.

<!-- section_id: "d67a6ebb-70e4-4bba-b445-76649b5dcd33" -->
### Context Retrieval (`get-library-docs`)
Retrieve comprehensive documentation for a specific library, including:
- API reference documentation
- Usage examples
- Configuration guides
- Best practices

<!-- section_id: "8cf15ae3-8877-4b66-a931-4669dd6e4f04" -->
### Context Management
- Caching of frequently accessed documentation
- Version tracking for documentation freshness
- Automatic fallback to cached content during API issues

<!-- section_id: "b7a1f173-2da1-4ad8-8024-f4481a3c46fa" -->
## Quick Start

<!-- section_id: "aa116a2f-30c0-4887-9e69-1ad0d39d9367" -->
### 1. Obtain API Key

Get your Context7 API key from [context7.io](https://context7.io) or use the provided default key for testing.

<!-- section_id: "6f3d9e4f-613b-4239-82d6-ef94e00498b0" -->
### 2. Configure Environment

Set the following environment variables:

```bash
# Required: Your Context7 API key
export CONTEXT7_API_KEY="your-api-key-here"

# Optional: Custom API URL (defaults to official Context7 API)
export CONTEXT7_API_URL="https://api.context7.io"
```

<!-- section_id: "62c66250-b025-4bb1-9180-1b08229c3ccb" -->
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

<!-- section_id: "64b8c739-ac21-4608-931b-6e7feae37928" -->
### 4. Using Wrapper Scripts (Recommended)

For more reliable execution, use the automation scripts in `setup/scripts/`:

```bash
# Run the MCP manager to generate wrapper scripts
python3 setup/scripts/mcp_manager.py --scope user
```

This creates wrapper scripts that properly set environment variables including `PATH` and `HOME`.

<!-- section_id: "92db8869-8424-48da-8d0c-16df7ec469ac" -->
## API Key Requirements

<!-- section_id: "964ab641-3a54-4157-9404-9d6d0c0c5c80" -->
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

<!-- section_id: "393075cf-d14b-4965-aff4-ef000aa21fd2" -->
### CONTEXT7_API_URL (Optional)

Custom API endpoint URL. Only needed if using a self-hosted Context7 instance or alternative endpoint.

**Default:** `https://api.context7.io`

```bash
export CONTEXT7_API_URL="https://custom-endpoint.example.com"
```

<!-- section_id: "836994f7-8745-4763-9672-0177dcebd790" -->
## Available Tools

<!-- section_id: "c293782f-5cdc-4fc7-8d80-bf01d05c55db" -->
### resolve-library-id

Resolves a library name to its Context7 identifier.

**Parameters:**
- `libraryName` (string, required): Name of the library to search for

**Example:**
```
Input: "react"
Output: Library ID and metadata for React documentation
```

<!-- section_id: "51677a22-6ebb-4c88-a946-2f1fb38bf010" -->
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

<!-- section_id: "10b57fff-a17d-4b59-93d1-7f8bbad0e19c" -->
## Integration with AI Tools

<!-- section_id: "e5479d33-ad0a-4c45-88b9-700ec45cf8ce" -->
### Claude Code CLI

Context7 MCP is automatically available through the MCP server configuration. Use it by asking about specific libraries:

```
"Use context7 to get the latest React hooks documentation"
```

<!-- section_id: "147eef28-b906-4c3e-ae86-1676c9fdd006" -->
### Cursor IDE

Add to your Cursor MCP settings and the tools will be available in the agent context.

<!-- section_id: "d7169837-54ca-43e1-bebc-5f0be71d1bec" -->
### Codex CLI

Configure via `~/.codex/config.toml`:

```toml
[mcp_servers.context7]
command = "npx"
args = ["-y", "@upstash/context7-mcp"]

[mcp_servers.context7.env]
CONTEXT7_API_KEY = "your-key-here"
```

<!-- section_id: "bbc38e14-db70-4b88-b8bd-83850826ca55" -->
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

<!-- section_id: "783b0847-d315-4cf9-9db6-839c231c6207" -->
## Related Documentation

- **MCP Automation**: See `setup/README.md` for the complete MCP server automation system
- **Troubleshooting**: See `setup/TROUBLESHOOTING.md` for common issues
- **Protocols**: See `0.13_protocols/` for detailed workflow documentation

<!-- section_id: "9973220b-5533-49bc-a602-579cb15e397f" -->
## Platform-Specific Notes

<!-- section_id: "629c6ce6-cb0f-4776-b414-c71eba10b153" -->
### Linux/Ubuntu

The MCP server runs via `npx` which requires Node.js. Ensure NVM or system Node.js is properly configured:

```bash
# Check Node.js availability
which node
which npx

# If using NVM, ensure it's sourced in your shell
source ~/.nvm/nvm.sh
```

<!-- section_id: "349dc950-3b98-4e3d-8c2a-ab80580223e8" -->
### Claude Code CLI Specifics

Claude Code CLI manages MCP servers internally. The configuration is applied through the system's MCP configuration file, typically at `~/.config/mcp/mcp.json`.

---

**Last Updated**: 2026-01-13
**MCP Package**: `@upstash/context7-mcp`
**Status**: Active
