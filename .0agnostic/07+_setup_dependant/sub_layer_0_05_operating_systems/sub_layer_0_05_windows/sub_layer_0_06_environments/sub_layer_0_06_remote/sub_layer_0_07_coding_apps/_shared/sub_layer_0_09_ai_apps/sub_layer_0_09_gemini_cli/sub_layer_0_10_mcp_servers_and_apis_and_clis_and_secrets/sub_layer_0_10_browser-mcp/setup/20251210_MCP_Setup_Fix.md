---
resource_id: "1cb4d7ea-1c5c-4070-aac1-6bb8d626d26c"
resource_type: "document"
resource_name: "20251210_MCP_Setup_Fix"
---
# 2025-12-10 - MCP Server Setup Fix for Linux/Ubuntu

**Status**: Resolved  
**Date**: 2025-12-10  
**Affected MCP Servers**: `playwright`, `browser`  
**Related Document**: `BROWSER_MCP_SETUP_EXPERIENCE.md`

<!-- section_id: "b0d466ce-beda-4aee-ab6d-3dd474a62c98" -->
## Problem

When attempting to use browser automation tools (e.g., `browser_navigate`, `browser_click`) on a Linux/Ubuntu system, the following error was consistently encountered: "Browser specified in your config is not installed". This occurred even when the browser (Chromium) was confirmed to be installed and executable manually. Additionally, general accessibility to Playwright MCP tools was inconsistent.

<!-- section_id: "b0829aeb-1829-4573-b908-ce738b41889b" -->
## Root Cause

As documented in `BROWSER_MCP_SETUP_EXPERIENCE.md` (Lesson 2), MCP servers executed via `npx` run in isolated environments and do not inherit shell environment variables. Specifically, the `PLAYWRIGHT_BROWSERS_PATH` and `HOME` environment variables were not being passed to the MCP server processes, preventing them from locating the installed browsers in `~/.cache/ms-playwright`.

<!-- section_id: "a336e2a5-841a-4c07-84f9-5f1dbbc23320" -->
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

<!-- section_id: "04cea139-3005-4240-a37c-4c564e021614" -->
## Post-Solution Actions

After updating the `mcp.json` file, a **restart of the Cursor IDE is mandatory** for the changes to take effect and for the MCP servers to reload with the new environment variables. Once restarted, browser automation tools are expected to function correctly, with a preference for `mcp_browser_*` tools as they were noted to be more accessible on Linux environments in the related documentation.

<!-- section_id: "8f19b7af-eb80-4d33-b75b-b33fc9814044" -->
## Next Steps

*   Verify MCP tools functionality after Cursor IDE restart.
*   Continue with ALEKS assignments, adapting strategies for graphical input limitations.
