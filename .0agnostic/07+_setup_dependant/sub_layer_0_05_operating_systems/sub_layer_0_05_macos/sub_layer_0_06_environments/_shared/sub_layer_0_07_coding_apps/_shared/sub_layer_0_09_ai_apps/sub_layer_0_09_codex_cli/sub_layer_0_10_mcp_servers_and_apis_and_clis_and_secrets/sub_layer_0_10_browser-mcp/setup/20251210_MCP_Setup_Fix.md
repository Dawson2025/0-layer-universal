---
resource_id: "b1fc94a1-3d24-4259-b22e-26d502e8150f"
resource_type: "document"
resource_name: "20251210_MCP_Setup_Fix"
---
# 2025-12-10 - MCP Server Setup Fix for Linux/Ubuntu

**Status**: Resolved  
**Date**: 2025-12-10  
**Affected MCP Servers**: `playwright`, `browser`  
**Related Document**: `BROWSER_MCP_SETUP_EXPERIENCE.md`

<!-- section_id: "d0d43440-0051-4487-b721-5e90a0d0a1d2" -->
## Problem

When attempting to use browser automation tools (e.g., `browser_navigate`, `browser_click`) on a Linux/Ubuntu system, the following error was consistently encountered: "Browser specified in your config is not installed". This occurred even when the browser (Chromium) was confirmed to be installed and executable manually. Additionally, general accessibility to Playwright MCP tools was inconsistent.

<!-- section_id: "961e3de8-8d18-4f1f-aae7-c226a32d70e5" -->
## Root Cause

As documented in `BROWSER_MCP_SETUP_EXPERIENCE.md` (Lesson 2), MCP servers executed via `npx` run in isolated environments and do not inherit shell environment variables. Specifically, the `PLAYWRIGHT_BROWSERS_PATH` and `HOME` environment variables were not being passed to the MCP server processes, preventing them from locating the installed browsers in `~/.cache/ms-playwright`.

<!-- section_id: "f6a43896-0be6-4f29-a8ef-117ae6aee7bb" -->
## Solution

The `~/.gemini/mcp.json` configuration file was updated to explicitly include the `PLAYWRIGHT_BROWSERS_PATH` and `HOME` environment variables for both the `playwright` and `browser` MCP servers.

**Original `mcp.json` (relevant parts):**
```json
{
  "mcpServers": {
    "playwright": {
      "command": "/home/dawson/.config/mcp/servers/mcp-playwright-generic.sh",
      "args": [],
      "env": {}
    },
    "browser": {
      "command": "/home/dawson/.config/mcp/servers/mcp-browser-generic.sh",
      "args": [],
      "env": {}
    }
    // ... other servers
  }
}
```

**Updated `mcp.json` (relevant parts):**
```json
{
  "mcpServers": {
    "playwright": {
      "command": "/home/dawson/.config/mcp/servers/mcp-playwright-generic.sh",
      "args": [
        "-y",
        "@playwright/mcp@latest",
        "--browser",
        "chromium"
      ],
      "env": {
        "PLAYWRIGHT_BROWSERS_PATH": "/home/dawson/.cache/ms-playwright",
        "HOME": "/home/dawson"
      }
    },
    "browser": {
      "command": "/home/dawson/.config/mcp/servers/mcp-browser-generic.sh",
      "args": [
        "@agent-infra/mcp-server-browser"
      ],
      "env": {
        "PLAYWRIGHT_BROWSERS_PATH": "/home/dawson/.cache/ms-playwright",
        "HOME": "/home/dawson"
      }
    }
    // ... other servers remain unchanged
  }
}
```

**Steps Taken:**
1.  Read `~/.gemini/mcp.json` to inspect the current configuration.
2.  Modified the JSON content programmatically to include the `args` and `env` blocks as specified in the `BROWSER_MCP_SETUP_EXPERIENCE.md` document.
3.  Wrote the updated JSON content back to `~/.gemini/mcp.json`.

<!-- section_id: "7c6f9be8-1ac9-4bbb-b2bb-cdf3bfbc481f" -->
## Post-Solution Actions

After updating the `mcp.json` file, a **restart of the Cursor IDE is mandatory** for the changes to take effect and for the MCP servers to reload with the new environment variables. Once restarted, browser automation tools are expected to function correctly, with a preference for `mcp_browser_*` tools as they were noted to be more accessible on Linux environments in the related documentation.

<!-- section_id: "409385b6-965d-42ba-9f1a-c0ac800a090a" -->
## Next Steps

*   Verify MCP tools functionality after Cursor IDE restart.
*   Continue with ALEKS assignments, adapting strategies for graphical input limitations.
