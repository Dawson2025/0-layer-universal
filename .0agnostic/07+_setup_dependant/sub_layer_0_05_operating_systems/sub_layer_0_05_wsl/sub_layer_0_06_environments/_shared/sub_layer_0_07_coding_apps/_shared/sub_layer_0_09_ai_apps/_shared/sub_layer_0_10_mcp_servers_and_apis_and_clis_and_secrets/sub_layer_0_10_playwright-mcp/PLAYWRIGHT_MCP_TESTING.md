---
resource_id: "5c010b99-985a-4ff0-be34-2b0be16efc09"
resource_type: "document"
resource_name: "PLAYWRIGHT_MCP_TESTING"
---
# Testing Playwright MCP Server - Cursor IDE

**Date**: 2025-12-02  
**Status**: In Progress  
**Issue**: Playwright MCP tools may not be directly accessible in Cursor IDE

<!-- section_id: "1c3a9376-fb4f-4298-95ec-5fcdf9eff58a" -->
## Problem

The Playwright MCP server is configured and running (22 tools enabled in Cursor settings), but the tools are not accessible with expected names:
- Expected: `mcp__playwright__browser_navigate` (double underscore)
- Available: `mcp_cursor-browser-extension_browser_navigate` (single underscore, different prefix)

**Linux/Ubuntu-Specific Issue**: This appears to be a platform-specific problem. The Playwright MCP server successfully connects and reports 22 tools, but Cursor IDE on Linux/Ubuntu does not expose these tools to the AI agent. This is likely a Cursor IDE integration issue specific to Linux systems.

<!-- section_id: "71df843e-2e7a-42c1-b25d-f00c66f74b32" -->
## Current Status

<!-- section_id: "96576daa-c9a3-4bb1-9bc1-35c38c2c223e" -->
### MCP Servers Running
- ✅ Playwright MCP: 3+ processes active
- ✅ Browser MCP: 1 process active
- ✅ Configuration: Updated in `~/.cursor/mcp.json` (2025-12-02)

<!-- section_id: "45d6cf42-ff54-4efb-bddc-fa6a43631abb" -->
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

<!-- section_id: "3725d881-553f-4eb1-915d-c8d79e1ee5ae" -->
### Tools Available
- `mcp_cursor-browser-extension_*` (18 tools) - Not working (requires Chrome extension)
- `mcp_browser_*` (21 tools) - Accessible, but browser detection issues
- Playwright tools (22 tools) - Registered but not exposed on Linux/Ubuntu

<!-- section_id: "08d6400f-fc2d-4cca-9d74-5cae29f042f7" -->
## Testing Approach

<!-- section_id: "3129d88d-23f9-43b2-9117-1a2b846b5636" -->
### Option 1: Check Tool Naming
Playwright tools might be available with:
- `mcp_playwright_*` (single underscore)
- `mcp__playwright__*` (double underscore)
- `browser_*` (no prefix)
- Different naming convention in Cursor

<!-- section_id: "53178f0a-0b7a-485c-9f19-0fc7172aec05" -->
### Option 2: Use Native Browser Automation
According to Cursor docs, browser automation is "native" and doesn't require MCP tools. The browser automation might work through Cursor's built-in system rather than MCP.

<!-- section_id: "b35b16b2-4930-4fe5-94af-3bae8b809d23" -->
### Option 3: Verify MCP Server Connection
Check if Playwright MCP server is actually connected to Cursor:
- Check MCP logs
- Verify server processes
- Test direct MCP communication

<!-- section_id: "8530049b-bf7a-42fc-acfa-4285be64741e" -->
## Next Steps

1. Test if Playwright tools work with different naming
2. Check Cursor's native browser automation
3. Verify MCP server connection status
4. Document findings

<!-- section_id: "fd1ccb71-21b2-4d78-a299-93c660283b1b" -->
## References

- [Playwright MCP Usage Guide](../setup/playwright-mcp-usage.md)
- [Cursor Browser Documentation](https://cursor.com/docs/agent/browser)
- [MCP Configuration Guide](./MCP_CONFIGURATION_GUIDE.md)

