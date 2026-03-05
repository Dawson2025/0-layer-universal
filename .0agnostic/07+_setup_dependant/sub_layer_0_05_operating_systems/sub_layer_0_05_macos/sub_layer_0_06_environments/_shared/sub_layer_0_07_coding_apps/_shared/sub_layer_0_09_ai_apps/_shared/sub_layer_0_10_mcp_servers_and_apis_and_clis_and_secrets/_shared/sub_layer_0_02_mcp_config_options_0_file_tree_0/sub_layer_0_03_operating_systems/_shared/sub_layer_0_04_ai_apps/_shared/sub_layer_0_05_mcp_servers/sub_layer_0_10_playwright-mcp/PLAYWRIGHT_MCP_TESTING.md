---
resource_id: "9f83160f-4143-4674-a65a-8f89647d2651"
resource_type: "document"
resource_name: "PLAYWRIGHT_MCP_TESTING"
---
# Testing Playwright MCP Server - Cursor IDE

**Date**: 2025-12-02  
**Status**: In Progress  
**Issue**: Playwright MCP tools may not be directly accessible in Cursor IDE

<!-- section_id: "d823badb-065f-421a-8e1e-b4ceb08a1773" -->
## Problem

The Playwright MCP server is configured and running (22 tools enabled in Cursor settings), but the tools are not accessible with expected names:
- Expected: `mcp__playwright__browser_navigate` (double underscore)
- Available: `mcp_cursor-browser-extension_browser_navigate` (single underscore, different prefix)

**Linux/Ubuntu-Specific Issue**: This appears to be a platform-specific problem. The Playwright MCP server successfully connects and reports 22 tools, but Cursor IDE on Linux/Ubuntu does not expose these tools to the AI agent. This is likely a Cursor IDE integration issue specific to Linux systems.

<!-- section_id: "e1edf3f7-e5d8-4ef0-a806-9340e6986cb3" -->
## Current Status

<!-- section_id: "36fb95c4-dc82-41ae-9d43-79704df28826" -->
### MCP Servers Running
- ✅ Playwright MCP: 3+ processes active
- ✅ Browser MCP: 1 process active
- ✅ Configuration: Updated in `~/.cursor/mcp.json` (2025-12-02)

<!-- section_id: "3768f919-6966-469e-85b4-910bba1ed052" -->
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

<!-- section_id: "e03046f3-16c6-4bf2-90cf-5a511c583bf8" -->
### Tools Available
- `mcp_cursor-browser-extension_*` (18 tools) - Not working (requires Chrome extension)
- `mcp_browser_*` (21 tools) - Accessible, but browser detection issues
- Playwright tools (22 tools) - Registered but not exposed on Linux/Ubuntu

<!-- section_id: "dc6de806-df16-4e86-8f57-443fb8a0c9b5" -->
## Testing Approach

<!-- section_id: "56a77d1f-fd74-42c7-ad35-db02f7993b69" -->
### Option 1: Check Tool Naming
Playwright tools might be available with:
- `mcp_playwright_*` (single underscore)
- `mcp__playwright__*` (double underscore)
- `browser_*` (no prefix)
- Different naming convention in Cursor

<!-- section_id: "e3745a12-33d5-40ec-8603-15fddbb0c2e9" -->
### Option 2: Use Native Browser Automation
According to Cursor docs, browser automation is "native" and doesn't require MCP tools. The browser automation might work through Cursor's built-in system rather than MCP.

<!-- section_id: "a1fe92d6-b016-48a8-a9a2-ee0a9dfbe625" -->
### Option 3: Verify MCP Server Connection
Check if Playwright MCP server is actually connected to Cursor:
- Check MCP logs
- Verify server processes
- Test direct MCP communication

<!-- section_id: "ad70669f-c0c6-40c5-ae1d-bb9ed3b90fe2" -->
## Next Steps

1. Test if Playwright tools work with different naming
2. Check Cursor's native browser automation
3. Verify MCP server connection status
4. Document findings

<!-- section_id: "8500d6ef-e8d7-4360-821c-9d6fc6cbef54" -->
## References

- [Playwright MCP Usage Guide](../setup/playwright-mcp-usage.md)
- [Cursor Browser Documentation](https://cursor.com/docs/agent/browser)
- [MCP Configuration Guide](./MCP_CONFIGURATION_GUIDE.md)

