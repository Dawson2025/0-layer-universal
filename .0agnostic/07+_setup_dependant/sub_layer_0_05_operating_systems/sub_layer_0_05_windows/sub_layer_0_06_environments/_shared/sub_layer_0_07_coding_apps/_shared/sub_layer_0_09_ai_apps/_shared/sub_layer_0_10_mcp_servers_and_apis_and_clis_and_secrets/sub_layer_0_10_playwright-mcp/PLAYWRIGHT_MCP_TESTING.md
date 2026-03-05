---
resource_id: "65000c29-a910-4805-9dd1-5b99d782c2ca"
resource_type: "document"
resource_name: "PLAYWRIGHT_MCP_TESTING"
---
# Testing Playwright MCP Server - Cursor IDE

**Date**: 2025-12-02  
**Status**: In Progress  
**Issue**: Playwright MCP tools may not be directly accessible in Cursor IDE

<!-- section_id: "a2067a76-81b4-4c29-be68-d8665b914fb0" -->
## Problem

The Playwright MCP server is configured and running (22 tools enabled in Cursor settings), but the tools are not accessible with expected names:
- Expected: `mcp__playwright__browser_navigate` (double underscore)
- Available: `mcp_cursor-browser-extension_browser_navigate` (single underscore, different prefix)

**Linux/Ubuntu-Specific Issue**: This appears to be a platform-specific problem. The Playwright MCP server successfully connects and reports 22 tools, but Cursor IDE on Linux/Ubuntu does not expose these tools to the AI agent. This is likely a Cursor IDE integration issue specific to Linux systems.

<!-- section_id: "8f5f886d-95d1-4f71-8ebd-b15f2c26f89f" -->
## Current Status

<!-- section_id: "c1cb8b27-c852-4c34-9aeb-dca3a7515dde" -->
### MCP Servers Running
- ✅ Playwright MCP: 3+ processes active
- ✅ Browser MCP: 1 process active
- ✅ Configuration: Updated in `~/.cursor/mcp.json` (2025-12-02)

<!-- section_id: "4ea9175d-cdb6-4b82-96a6-f6bb8925a293" -->
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

<!-- section_id: "687532fd-dfc2-4ca9-8ae7-351b965aa7b3" -->
### Tools Available
- `mcp_cursor-browser-extension_*` (18 tools) - Not working (requires Chrome extension)
- `mcp_browser_*` (21 tools) - Accessible, but browser detection issues
- Playwright tools (22 tools) - Registered but not exposed on Linux/Ubuntu

<!-- section_id: "ccbfd657-fbd9-4e0a-9a61-b9c53369da2c" -->
## Testing Approach

<!-- section_id: "843d3bd7-3e25-49f3-868b-42d18cf5214e" -->
### Option 1: Check Tool Naming
Playwright tools might be available with:
- `mcp_playwright_*` (single underscore)
- `mcp__playwright__*` (double underscore)
- `browser_*` (no prefix)
- Different naming convention in Cursor

<!-- section_id: "9e15c4c1-0f9b-49ab-b01d-f53939af0bf1" -->
### Option 2: Use Native Browser Automation
According to Cursor docs, browser automation is "native" and doesn't require MCP tools. The browser automation might work through Cursor's built-in system rather than MCP.

<!-- section_id: "9d7a6b93-b772-4cfb-91ae-7ae71978f617" -->
### Option 3: Verify MCP Server Connection
Check if Playwright MCP server is actually connected to Cursor:
- Check MCP logs
- Verify server processes
- Test direct MCP communication

<!-- section_id: "c7d64855-1bd5-4d9d-b0ac-f1dd57363907" -->
## Next Steps

1. Test if Playwright tools work with different naming
2. Check Cursor's native browser automation
3. Verify MCP server connection status
4. Document findings

<!-- section_id: "5e4bce92-bdb8-4881-a72a-d40a649019b9" -->
## References

- [Playwright MCP Usage Guide](../setup/playwright-mcp-usage.md)
- [Cursor Browser Documentation](https://cursor.com/docs/agent/browser)
- [MCP Configuration Guide](./MCP_CONFIGURATION_GUIDE.md)

