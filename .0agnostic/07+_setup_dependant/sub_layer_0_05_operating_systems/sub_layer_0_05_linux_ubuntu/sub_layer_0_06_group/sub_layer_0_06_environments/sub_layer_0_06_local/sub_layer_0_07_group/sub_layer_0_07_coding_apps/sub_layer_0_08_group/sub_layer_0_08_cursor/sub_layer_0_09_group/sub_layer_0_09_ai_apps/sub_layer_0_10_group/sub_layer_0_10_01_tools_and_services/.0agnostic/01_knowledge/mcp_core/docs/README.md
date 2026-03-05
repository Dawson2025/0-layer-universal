---
resource_id: "b6c49688-58c8-4f99-8420-f8d9f46e3e3c"
resource_type: "readme
knowledge"
resource_name: "README"
---
# _mcp_core

Core MCP (Model Context Protocol) configuration and automation shared across all MCP servers in this structure.

## Overview

`_mcp_core` serves as the centralized configuration hub for MCP server management. It contains:

- Shared automation scripts for consistent MCP server setup
- Cross-platform configuration management
- Concurrent browser session handling for multiple AI tools
- Universal protocols and agent setup templates

## Directory Structure

```
_mcp_core/
├── README.md                          # This documentation
├── 0.12_universal_tools/
│   └── _shared/                       # Shared utilities across all MCP servers
├── 0.13_protocols/                    # MCP protocol definitions and templates
├── 0.14_agent_setup/                  # Agent-specific configuration templates
└── setup/
    ├── README.md                      # Setup automation documentation
    ├── CONCURRENT_BROWSER_SETUP.md    # Guide for multi-tool browser concurrency
    ├── 20251210_MCP_Setup_Fix.md      # Historical fix documentation
    ├── TROUBLESHOOTING.md             # Common issues and solutions
    └── scripts/
        ├── mcp_manager.py             # Core MCP server setup automation
        ├── codex_mcp_sync.py          # Codex CLI MCP configuration sync
        └── mcp_concurrent_browser.py  # Concurrent browser manager
```

## Relationship to Other MCP Servers

`_mcp_core` provides the foundation that all sibling MCP server directories build upon:

```
0.10_mcp_servers_and_apis_and_secrets/
├── _mcp_core/          <-- This directory (shared core)
├── _shared/            <-- Shared assets (non-core)
├── browser-mcp/        <-- Uses _mcp_core automation
├── chrome-devtools-mcp/<-- Uses _mcp_core automation
├── claude_in_chrome/   <-- Uses _mcp_core automation
├── context7-mcp/       <-- Uses _mcp_core automation
├── playwright-mcp/     <-- Uses _mcp_core automation
└── tavily-mcp/         <-- Uses _mcp_core automation
```

### How It Works

1. **Server Definitions**: `mcp_manager.py` contains the source of truth for all supported MCP servers (playwright, browser, web-search, context7, chrome-devtools)

2. **Wrapper Generation**: The automation creates platform-specific wrapper scripts that properly set environment variables (PATH, PLAYWRIGHT_BROWSERS_PATH, HOME, DISPLAY)

3. **Configuration Deployment**: Generates `mcp.json` files for various scopes (user, project, system, local)

4. **Tool-Specific Configs**: Creates configurations for different AI tools (Claude, Gemini, Codex, Cursor)

## Quick Reference: Setup Scripts

### mcp_manager.py - Primary Setup Tool

The main automation script for setting up all MCP servers.

```bash
# User-level installation (recommended)
python3 setup/scripts/mcp_manager.py --scope user

# Project-level installation
python3 setup/scripts/mcp_manager.py --scope project

# System-level installation (may require sudo)
python3 setup/scripts/mcp_manager.py --scope system

# Local directory installation
python3 setup/scripts/mcp_manager.py --scope local
```

**What it does:**
- Detects operating system and Node.js/npx location
- Creates wrapper scripts with proper environment variables
- Generates `mcp.json` configuration file
- Handles WSLg-specific browser settings

### codex_mcp_sync.py - Codex CLI Sync

Syncs MCP server configurations to Codex CLI's `config.toml`.

```bash
# Sync development environment (default)
python3 setup/scripts/codex_mcp_sync.py --env development

# Sync testing environment
python3 setup/scripts/codex_mcp_sync.py --env testing

# Sync with specific servers disabled
python3 setup/scripts/codex_mcp_sync.py --disable chrome-devtools web-search

# Force headless mode for Playwright
python3 setup/scripts/codex_mcp_sync.py --headless
```

### mcp_concurrent_browser.py - Concurrent Browser Manager

Enables multiple AI tools to use Playwright browsers simultaneously.

```bash
# Set up concurrent configs for all tools
python3 setup/scripts/mcp_concurrent_browser.py setup

# Set up for specific tools only
python3 setup/scripts/mcp_concurrent_browser.py setup --tools codex claude

# Update Codex CLI to use tool-specific config
python3 setup/scripts/mcp_concurrent_browser.py apply-codex

# Check current status
python3 setup/scripts/mcp_concurrent_browser.py status
```

## Supported Platforms

| Platform | Status | Notes |
|----------|--------|-------|
| Linux (Ubuntu) | Supported | Primary development platform |
| WSL/WSL2 | Supported | WSLg detection for headed browsers |
| macOS | Supported | Standard Unix paths |
| Windows | Supported | Uses .cmd wrappers |

## Supported AI Tools

| Tool | Config Location | Notes |
|------|-----------------|-------|
| Claude Code CLI | `~/.config/mcp/` | Internal MCP management |
| Codex CLI | `~/.codex/config.toml` | TOML-based config |
| Gemini CLI | `~/.gemini/settings.json` | JSON-based config |
| Cursor | `~/.config/mcp/` or `.cursor/` | Per-project support |

## After Setup

**Important**: Always restart your AI Agent/IDE after running setup scripts for changes to take effect.

## Related Documentation

- `setup/README.md` - Detailed setup automation documentation
- `setup/CONCURRENT_BROWSER_SETUP.md` - Multi-tool browser concurrency guide
- `setup/TROUBLESHOOTING.md` - Common issues and solutions
