# Testing Playwright MCP Server - Cursor IDE

**Date**: 2025-12-02  
**Status**: In Progress  
**Issue**: Playwright MCP tools may not be directly accessible in Cursor IDE

## Problem

The Playwright MCP server is configured and running (22 tools enabled in Cursor settings), but the tools are not accessible with expected names:
- Expected: `mcp__playwright__browser_navigate` (double underscore)
- Available: `mcp_cursor-browser-extension_browser_navigate` (single underscore, different prefix)

## Current Status

### MCP Servers Running
- ✅ Playwright MCP: 3+ processes active
- ✅ Browser MCP: 1 process active
- ✅ Configuration: Correct in `~/.cursor/mcp.json`

### Tools Available
- `mcp_cursor-browser-extension_*` (18 tools) - Not working (requires Chrome extension)
- Playwright tools (22 tools) - Status unknown, may have different naming

## Testing Approach

### Option 1: Check Tool Naming
Playwright tools might be available with:
- `mcp_playwright_*` (single underscore)
- `mcp__playwright__*` (double underscore)
- `browser_*` (no prefix)
- Different naming convention in Cursor

### Option 2: Use Native Browser Automation
According to Cursor docs, browser automation is "native" and doesn't require MCP tools. The browser automation might work through Cursor's built-in system rather than MCP.

### Option 3: Verify MCP Server Connection
Check if Playwright MCP server is actually connected to Cursor:
- Check MCP logs
- Verify server processes
- Test direct MCP communication

## Next Steps

1. Test if Playwright tools work with different naming
2. Check Cursor's native browser automation
3. Verify MCP server connection status
4. Document findings

## References

- [Playwright MCP Usage Guide](../setup/playwright-mcp-usage.md)
- [Cursor Browser Documentation](https://cursor.com/docs/agent/browser)
- [MCP Configuration Guide](./MCP_CONFIGURATION_GUIDE.md)

