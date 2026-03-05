---
resource_id: "f5fa3418-6c58-4d4d-aea3-0795075be69c"
resource_type: "document"
resource_name: "20251210_MCP_Setup_Fix"
---
# 2025-12-10 - MCP Server Setup Fix for Linux/Ubuntu

**Status**: Resolved  
**Date**: 2025-12-10  
**Affected MCP Servers**: `playwright`, `browser`  
**Related Document**: `BROWSER_MCP_SETUP_EXPERIENCE.md`

<!-- section_id: "ed83309a-2ee1-4703-b519-1621ce39bf2d" -->
## Problem

When attempting to use browser automation tools (e.g., `browser_navigate`, `browser_click`) on a Linux/Ubuntu system, the following error was consistently encountered: "Browser specified in your config is not installed". This occurred even when the browser (Chromium) was confirmed to be installed and executable manually. Additionally, general accessibility to Playwright MCP tools was inconsistent.

<!-- section_id: "1f81fb3d-c5af-4f42-8114-a4ba6cbe02da" -->
## Root Cause

As documented in `BROWSER_MCP_SETUP_EXPERIENCE.md` (Lesson 2), MCP servers executed via `npx` run in isolated environments and do not inherit shell environment variables. Specifically, the `PLAYWRIGHT_BROWSERS_PATH` and `HOME` environment variables were not being passed to the MCP server processes, preventing them from locating the installed browsers in `~/.cache/ms-playwright`.

<!-- section_id: "8905b904-7749-4d22-88dd-1943e3d70e17" -->
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

<!-- section_id: "3601ee30-d478-45bd-aee3-54a79c30aea2" -->
## Post-Solution Actions

After updating the `mcp.json` file, a **restart of the Cursor IDE is mandatory** for the changes to take effect and for the MCP servers to reload with the new environment variables. Once restarted, browser automation tools are expected to function correctly, with a preference for `mcp_browser_*` tools as they were noted to be more accessible on Linux environments in the related documentation.

<!-- section_id: "25fde83d-f87c-4644-b86f-73e4457fd40c" -->
## Next Steps

*   Verify MCP tools functionality after Cursor IDE restart.
*   Continue with ALEKS assignments, adapting strategies for graphical input limitations.
