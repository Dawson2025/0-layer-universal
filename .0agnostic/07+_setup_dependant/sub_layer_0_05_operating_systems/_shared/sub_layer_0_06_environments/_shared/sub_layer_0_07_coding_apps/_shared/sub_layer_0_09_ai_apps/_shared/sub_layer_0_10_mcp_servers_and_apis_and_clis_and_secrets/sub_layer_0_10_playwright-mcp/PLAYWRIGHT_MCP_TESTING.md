---
resource_id: "fa80e9bc-4bad-401f-8547-c89e434583d9"
resource_type: "document"
resource_name: "PLAYWRIGHT_MCP_TESTING"
---
# Testing Playwright MCP Server - Cursor IDE

**Date**: 2025-12-02  
**Status**: In Progress  
**Issue**: Playwright MCP tools may not be directly accessible in Cursor IDE

<!-- section_id: "9fcd7c80-64e5-442d-baee-d2cb496da760" -->
## Problem

The Playwright MCP server is configured and running (22 tools enabled in Cursor settings), but the tools are not accessible with expected names:
- Expected: `mcp__playwright__browser_navigate` (double underscore)
- Available: `mcp_cursor-browser-extension_browser_navigate` (single underscore, different prefix)

**Linux/Ubuntu-Specific Issue**: This appears to be a platform-specific problem. The Playwright MCP server successfully connects and reports 22 tools, but Cursor IDE on Linux/Ubuntu does not expose these tools to the AI agent. This is likely a Cursor IDE integration issue specific to Linux systems.

<!-- section_id: "60a244fd-ddbc-4cf7-9902-033463a15e35" -->
## Current Status

<!-- section_id: "6448a76a-9d5c-4994-a8d6-0f95d867a003" -->
### MCP Servers Running
- ✅ Playwright MCP: 3+ processes active
- ✅ Browser MCP: 1 process active
- ✅ Configuration: Updated in `~/.cursor/mcp.json` (2025-12-02)

<!-- section_id: "b57e3f50-bdb8-4a46-885d-1052886c6715" -->
### Configuration Fix Applied (2025-12-02)

**Issue**: Playwright MCP may not have access to Node.js/npx if NVM is not loaded.

**Solution**: Updated configuration to use bash wrapper that loads NVM:
```json
{
  "playwright": {
    "command": "bash",
    "args": [
      "-c",
      "export NVM_DIR=\"$HOME/.nvm\" && [ -s \"$NVM_DIR/nvm.sh\" ] && \\. \"$NVM_DIR/nvm.sh\" && npx -y @playwright/mcp@latest --browser chromium"
    ],
    "env": {
      "PLAYWRIGHT_BROWSERS_PATH": "/home/dawson/.cache/ms-playwright"
    }
  }
}
```

**Status**: ✅ Configuration fix successful - server connects after restart.

**Test Results After Restart (2025-12-02)**:
- ✅ Playwright MCP server starts successfully with bash wrapper
- ✅ Server connects: "Successfully connected to stdio server"
- ✅ Server reports: "Found 22 tools, 0 prompts, and 0 resources"
- ⚠️ **Linux/Ubuntu Issue**: Tools are NOT accessible to AI agent despite successful connection
- ⚠️ **Root Cause**: Cursor IDE on Linux does not expose Playwright MCP tools to agents

<!-- section_id: "95e0bb17-e7eb-462b-a2fd-427cbfd26c0e" -->
### Tools Available
- `mcp_cursor-browser-extension_*` (18 tools) - Not working (requires Chrome extension)
- `mcp_browser_*` (21 tools) - Accessible, but browser detection issues
- Playwright tools (22 tools) - Registered but not exposed on Linux/Ubuntu

<!-- section_id: "2e9e9d6b-483e-46be-9d23-90f4a3a06476" -->
## Testing Approach

<!-- section_id: "689e4dcc-5f93-464a-9d35-7befdc8b878b" -->
### Option 1: Check Tool Naming
Playwright tools might be available with:
- `mcp_playwright_*` (single underscore)
- `mcp__playwright__*` (double underscore)
- `browser_*` (no prefix)
- Different naming convention in Cursor

<!-- section_id: "40c58b6b-e651-457b-bfca-8f29b03d74d7" -->
### Option 2: Use Native Browser Automation
According to Cursor docs, browser automation is "native" and doesn't require MCP tools. The browser automation might work through Cursor's built-in system rather than MCP.

<!-- section_id: "329b8db1-2ed6-42a0-a54d-eb1d11dbf235" -->
### Option 3: Verify MCP Server Connection
Check if Playwright MCP server is actually connected to Cursor:
- Check MCP logs
- Verify server processes
- Test direct MCP communication

<!-- section_id: "56b1fc19-61d2-4e13-a306-656378432a57" -->
## Next Steps

1. Test if Playwright tools work with different naming
2. Check Cursor's native browser automation
3. Verify MCP server connection status
4. Document findings

<!-- section_id: "d38dd157-96d0-4aac-a6be-5a3c042e3873" -->
## References

- [Playwright MCP Usage Guide](../setup/playwright-mcp-usage.md)
- [Cursor Browser Documentation](https://cursor.com/docs/agent/browser)
- [MCP Configuration Guide](./MCP_CONFIGURATION_GUIDE.md)

