---
resource_id: "8c1a3675-a526-4bde-bc67-e30e9b688ae8"
resource_type: "readme
document"
resource_name: "README"
---
# MCP Server Automation System

<!-- section_id: "8ea3a4d4-db12-4de6-b2db-d1bbf0d52224" -->
## Overview

This directory contains the automation system for setting up Model Context Protocol (MCP) servers across various operating systems, AI applications, and installation scopes. The core of this system is the `mcp_manager.py` script, which serves as the single source of truth for MCP server configurations.

<!-- section_id: "87ef8eff-b49b-4c23-8d35-cf92e9bd5bbd" -->
## 🚀 Purpose

The primary goals of this automation system are:

1.  **Standardized Setup**: Ensure consistent MCP server configurations across different environments (Linux/WSL, Windows, macOS) and AI tools (Gemini, Claude, Codex, Cursor).
2.  **Simplified Management**: Automate the creation of wrapper scripts and the generation of `mcp.json` configuration files, eliminating manual editing and reducing errors.
3.  **Platform & Tool Awareness**: Dynamically adapt configurations based on the detected operating system and generate specific wrappers for different AI tools.
4.  **Scope Flexibility**: Support installation at user, project, system, and local levels.
5.  **Idempotency**: The setup process can be run multiple times, always resulting in the desired state without unintended side effects.

<!-- section_id: "4ec1c1b9-8697-45da-a558-c5c5abb15946" -->
## 📁 Directory Structure

```
0.06_automation/
├── scripts/
│   ├── mcp_manager.py              # Core MCP server setup automation
│   ├── codex_mcp_sync.py           # Codex CLI MCP configuration sync
│   └── mcp_concurrent_browser.py   # Concurrent browser setup for multiple AI tools
├── CONCURRENT_BROWSER_SETUP.md     # Guide for running browsers in multiple AI tools simultaneously
└── README.md                        # This documentation
```

<!-- section_id: "1be8eeb9-f0ee-4989-977f-71a424d74b5d" -->
## 🛠️ How it Works (`mcp_manager.py`)

The `mcp_manager.py` script performs the following key steps:

1.  **Environment Detection**:
    *   Identifies the operating system (`platform.system().lower()`).
    *   Locates the `npx` executable (essential for running MCP servers) by checking the system's `PATH` and common Node.js Version Manager (NVM) installations.
    *   Determines relevant paths like `HOME_DIR`, `BROWSER_CACHE_DIR`, and `NODE_BIN_DIR` based on the detected OS.
    *   Detects the `DISPLAY` environment variable for graphical contexts (relevant for headed browser modes).

2.  **Server Definitions (Source of Truth)**:
    *   A `SERVERS` dictionary within the script defines all supported MCP servers (e.g., `playwright`, `browser`, `web-search`, `context7`).
    *   Each server definition includes its description, command (`npx`), arguments, default environment variables, and a flag indicating if it `requires_wrapper`.

3.  **Wrapper Script Generation**:
    *   For each server requiring a wrapper, `mcp_manager.py` generates a custom bash (`.sh`) or Windows batch (`.cmd`) script.
    *   These wrappers are placed in a scope-specific `servers` directory (e.g., `~/.config/mcp/servers/`).
    *   The wrappers explicitly set:
        *   `PATH`: Ensuring `npx` and `node` are found.
        *   Environment variables: Such as `PLAYWRIGHT_BROWSERS_PATH`, `HOME`, and `DISPLAY`, which are critical for browser-based MCPs.
    *   Wrappers are generated for a set of `TARGET_TOOLS` (generic, claude, gemini, codex, cursor), allowing for tool-specific logging or future customizations.

4.  **`mcp.json` Configuration Generation**:
    *   The script constructs the `mcp.json` configuration file based on the `SERVERS` definitions.
    *   For servers using wrappers, the `command` entry in `mcp.json` points directly to the generated `generic` wrapper script.
    *   This `mcp.json` is deployed to the target scope's configuration directory (e.g., `~/.config/mcp/mcp.json` for user scope).

5.  **Scope-Based Deployment**:
    *   The script accepts a `--scope` argument (`user`, `project`, `system`, `local`) to determine where the configuration files and wrappers should be installed.
    *   It handles permissions, attempting system-level installation first and falling back to user-level if permission errors occur.

<!-- section_id: "afbe5de4-1df6-4817-9bc9-eb4635820694" -->
## 🚀 How to Use

To set up MCP servers using this automation system, simply run the `mcp_manager.py` script with the desired scope:

```bash
# Example: Install MCP servers at the user level
python3 /path/to/automation/scripts/mcp_manager.py --scope user

# Example: Attempt system-level installation (may require sudo)
# The script will attempt system-level first, and fallback to user if permissions are denied.
python3 /path/to/automation/scripts/mcp_manager.py --scope system 

# Example: Install to a local project's .mcp directory
# (Requires running from the project root)
python3 /path/to/automation/scripts/mcp_manager.py --scope project

# Example: Install to the current working directory's .mcp directory
python3 /path/to/automation/scripts/mcp_manager.py --scope local
```

**After running the script, you MUST restart your AI Agent/IDE for the changes to take effect.**

<!-- section_id: "dcbcdf9f-9131-4b6c-9fa6-bc049fbb58af" -->
## ✨ Benefits

*   **Consistency**: Ensures all MCP servers are configured uniformly across different environments.
*   **Robustness**: Handles platform-specific nuances (like `PATH` and environment variables) to prevent common "browser not found" errors.
*   **Flexibility**: Supports various installation scopes to fit different use cases.
*   **Maintainability**: Centralized server definitions make it easy to add or modify MCP servers.
*   **Tool-Agnostic**: Generates wrappers that work seamlessly with various AI clients (Gemini, Claude, etc.).

<!-- section_id: "4d78c23e-87f5-4688-9ece-65e0344b1dbc" -->
## 📝 Gemini CLI Integration Notes

Getting the MCP servers to function correctly within the Gemini CLI in a WSL environment.

1.  **Configuration File Location**: The Gemini CLI primarily sources its MCP server definitions from `~/.gemini/settings.json`.
2.  **Merging `mcpServers` Block**: The `mcpServers` block generated by `mcp_manager.py` needs to be merged directly into the `~/.gemini/settings.json` file.
3.  **Browser Tool Selection**: `playwright` and `browser` servers are the intended tools for browser automation. The initial focus on `cursor-browser-extension` was a misunderstanding based on Cursor IDE-specific documentation, which does not apply to Gemini CLI. Both `playwright` and `browser` servers are now configured.
4.  **Headed vs. Headless**: Playwright MCP is **headed by default**; use `--headless` to force headless. Do not use `--headless=false` (unsupported; causes server startup failure).
    - On **WSLg**, headed Chromium may crash unless launched with Wayland/Ozone flags. Prefer using a Playwright MCP `--config` file that sets `launchOptions.args` to `["--ozone-platform=wayland", "--enable-features=UseOzonePlatform"]` and `headless: false`.

**To ensure Gemini CLI recognizes these changes, a restart of the Gemini CLI is mandatory after updating `~/.gemini/settings.json`.**

<!-- section_id: "c0ad6d0c-0efa-4a08-acd6-0975b5f5352a" -->
## 🔧 Concurrent Browser Setup (`mcp_concurrent_browser.py`)

When multiple AI tools (Codex CLI, Claude Code CLI, Gemini CLI) need to use Playwright MCP browsers simultaneously, they encounter "Browser is already in use" errors due to MCP server process locking. The `mcp_concurrent_browser.py` script solves this by creating **OS-specific and tool-specific** isolated browser configurations.

<!-- section_id: "c1bc06fc-7a82-4e09-8a8e-6d5006c7d8df" -->
### Quick Start

```bash
# Set up OS-specific concurrent browser configs (auto-detects OS)
python3 scripts/mcp_concurrent_browser.py setup

# Update Codex CLI to use OS+tool-specific config
python3 scripts/mcp_concurrent_browser.py apply-codex

# Verify setup (show current OS only)
python3 scripts/mcp_concurrent_browser.py status --os wsl
```

<!-- section_id: "ca72b730-a4e6-49a8-9f35-8ab5205f7c81" -->
### What It Does

1. **Auto-detects operating system** (WSL, Linux, macOS, Windows)
2. **Creates OS+tool-specific Playwright configs** using pattern `{os}_{tool}` (e.g., `wsl_codex`, `linux_gemini`)
3. **Assigns unique browser profile directories** per OS+tool combination to prevent conflicts
4. **Enables `isolated: true`** in all configs for concurrent browser instances
5. **Adds OS-specific launch args** (e.g., Wayland/Ozone for WSLg)
6. **Updates Codex CLI config** to reference OS+tool-specific Playwright config

<!-- section_id: "377f45ba-b266-4026-828b-98a610a817d0" -->
### Documentation

For complete setup instructions, troubleshooting, and architecture details, see:
- **[CONCURRENT_BROWSER_SETUP.md](./CONCURRENT_BROWSER_SETUP.md)** - Full guide for concurrent browser setup

<!-- section_id: "503ab5c0-ebed-41f7-ab2d-6c28bd93fc0c" -->
### Use Cases

- Run Playwright MCP browsers in Codex CLI and Claude Code CLI at the same time
- Test browser automation across multiple AI tools without conflicts
- Maintain separate browser sessions for different projects/contexts
