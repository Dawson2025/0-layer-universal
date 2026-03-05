---
resource_id: "e042f0bd-a086-4997-bdc7-99dc4046f189"
resource_type: "document"
resource_name: "PLAYWRIGHT_MCP_TESTING"
---
# Testing Playwright MCP Server - Cursor IDE

**Date**: 2025-12-02  
**Status**: In Progress  
**Issue**: Playwright MCP tools may not be directly accessible in Cursor IDE

<!-- section_id: "4e4b1af2-2f32-44c0-bf4f-006efc84a532" -->
## Problem

The Playwright MCP server is configured and running (22 tools enabled in Cursor settings), but the tools are not accessible with expected names:
- Expected: `mcp__playwright__browser_navigate` (double underscore)
- Available: `mcp_cursor-browser-extension_browser_navigate` (single underscore, different prefix)

**Linux/Ubuntu-Specific Issue**: This appears to be a platform-specific problem. The Playwright MCP server successfully connects and reports 22 tools, but Cursor IDE on Linux/Ubuntu does not expose these tools to the AI agent. This is likely a Cursor IDE integration issue specific to Linux systems.

<!-- section_id: "eb15e1be-1d4b-4e5c-ab53-ccd2aa1961c7" -->
## Current Status

<!-- section_id: "41dc4b08-e97b-4cc0-b189-bcc6c00f626c" -->
### MCP Servers Running
- ✅ Playwright MCP: 3+ processes active
- ✅ Browser MCP: 1 process active
- ✅ Configuration: Updated in `~/.cursor/mcp.json` (2025-12-02)

<!-- section_id: "a1ea1ce5-4277-421f-a127-650fdb2db332" -->
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

<!-- section_id: "56483d5b-eba9-443d-86a7-5e9757808f1a" -->
### Tools Available
- `mcp_cursor-browser-extension_*` (18 tools) - Not working (requires Chrome extension)
- `mcp_browser_*` (21 tools) - Accessible, but browser detection issues
- Playwright tools (22 tools) - Registered but not exposed on Linux/Ubuntu

<!-- section_id: "23fa600e-1811-483a-8daa-fa5abc2f8c4d" -->
## Testing Approach

<!-- section_id: "1cdb36fb-347f-4bf5-85ea-b1757e6d92ec" -->
### Option 1: Check Tool Naming
Playwright tools might be available with:
- `mcp_playwright_*` (single underscore)
- `mcp__playwright__*` (double underscore)
- `browser_*` (no prefix)
- Different naming convention in Cursor

<!-- section_id: "16ed0107-1169-4772-b4d2-9938e042cb96" -->
### Option 2: Use Native Browser Automation
According to Cursor docs, browser automation is "native" and doesn't require MCP tools. The browser automation might work through Cursor's built-in system rather than MCP.

<!-- section_id: "b5bf2b42-81c0-4c94-abd8-ed17bcbe63d8" -->
### Option 3: Verify MCP Server Connection
Check if Playwright MCP server is actually connected to Cursor:
- Check MCP logs
- Verify server processes
- Test direct MCP communication

<!-- section_id: "089693da-83c9-47f1-b3a7-ddd3da49d986" -->
## Next Steps

1. Test if Playwright tools work with different naming
2. Check Cursor's native browser automation
3. Verify MCP server connection status
4. Document findings

<!-- section_id: "423f35e4-d60d-4fc2-bcc8-2671297fd4e0" -->
## References

- [Playwright MCP Usage Guide](../setup/playwright-mcp-usage.md)
- [Cursor Browser Documentation](https://cursor.com/docs/agent/browser)
- [MCP Configuration Guide](./MCP_CONFIGURATION_GUIDE.md)

