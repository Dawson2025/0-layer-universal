# Cursor IDE Linux/Ubuntu MCP Issues

**Date**: 2025-12-02  
**Location**: Universal Layer → Coding App Setup  
**Status**: Critical Cursor IDE-specific limitations on Linux

## Overview

This document outlines Linux/Ubuntu-specific issues with Cursor IDE's MCP (Model Context Protocol) integration. These issues affect how MCP servers are exposed to AI agents within Cursor IDE.

## Critical Cursor IDE Issues on Linux

### 1. MCP Tool Exposure Limitation

**Problem**: Cursor IDE on Linux does not expose Playwright MCP tools to AI agents, even when the MCP server successfully connects and reports tools.

**Symptoms**:
- MCP server connects successfully (logs show "Found 22 tools")
- Tools are registered with the MCP server
- Tools are NOT accessible to AI agents (attempts to use `mcp_playwright_*` tools fail with "Tool not found")

**Evidence**:
- Playwright MCP server logs: "Successfully connected to stdio server"
- Playwright MCP server logs: "Found 22 tools, 0 prompts, and 0 resources"
- AI agent tool list: No `mcp_playwright_*` tools available
- Available tools: Only `mcp_browser_*` and `mcp_cursor-browser-extension_*` are accessible

**Root Cause**: Cursor IDE's MCP tool exposure mechanism has platform-specific behavior. On Linux, Playwright MCP tools are not exposed to agents despite successful server connection.

**Workaround**: Use `mcp_browser_*` tools from `@agent-infra/mcp-server-browser` instead of Playwright MCP tools.

### 2. Browser Path Configuration

**Problem**: Cursor IDE's browser automation settings may not work correctly on Linux.

**Impact**:
- "Default (Bundled Chrome)" option may not work
- Browser detection fails
- Custom executable path required

**Solution**: 
1. Go to Cursor Settings → Tools & MCP → Browser Automation
2. Set Connection Type to "Custom Executable Path"
3. Enter explicit browser path: `/usr/bin/google-chrome` or Playwright Chromium path

### 3. MCP Configuration File Location

**Location**: `~/.cursor/mcp.json`

**Linux-Specific Requirements**:
- Use bash wrapper for NVM-dependent MCP servers
- Use absolute paths for browser executables
- Set environment variables explicitly

**Example Configuration**:
```json
{
  "mcpServers": {
    "playwright": {
      "command": "bash",
      "args": [
        "-c",
        "export NVM_DIR=\"$HOME/.nvm\" && [ -s \"$NVM_DIR/nvm.sh\" ] && \\. \"$NVM_DIR/nvm.sh\" && npx -y @playwright/mcp@latest --browser chromium"
      ],
      "env": {
        "PLAYWRIGHT_BROWSERS_PATH": "/home/dawson/.cache/ms-playwright"
      }
    },
    "browser": {
      "command": "bash",
      "args": [
        "-c",
        "export NVM_DIR=\"$HOME/.nvm\" && [ -s \"$NVM_DIR/nvm.sh\" ] && \\. \"$NVM_DIR/nvm.sh\" && npx -y @agent-infra/mcp-server-browser --executable-path /home/dawson/.cache/ms-playwright/chromium-1200/chrome-linux64/chrome"
      ]
    }
  }
}
```

## Available vs. Unavailable Tools

### ✅ Available on Linux
- `mcp_browser_*` (21 tools) - From `@agent-infra/mcp-server-browser`
- `mcp_cursor-browser-extension_*` (18 tools) - From Cursor's browser extension (may have browser detection issues)

### ❌ Not Available on Linux
- `mcp_playwright_*` (22 tools) - Server connects but tools not exposed to agents

## Troubleshooting

### Check MCP Server Status

```bash
# Check if MCP servers are running
ps aux | grep -E "playwright|mcp" | grep -v grep

# Check Cursor MCP logs
find ~/.config/Cursor/logs -name "*playwright*" -o -name "*mcp*" | head -5
```

### Verify Configuration

```bash
# Check MCP configuration
cat ~/.cursor/mcp.json | jq '.'

# Verify browser paths
ls -la ~/.cache/ms-playwright/chromium-*/chrome-linux64/chrome
```

### Check Tool Availability

In Cursor IDE:
1. Go to Settings → Tools & MCP
2. Check "Model Context Protocol" section
3. Verify which tools are listed as available
4. Note: Playwright tools may show as "22 tools" but not be accessible to agents

## Recommendations for Linux Users

1. **Use Browser MCP Instead of Playwright MCP**:
   - Browser MCP tools (`mcp_browser_*`) are accessible on Linux
   - Configure with explicit browser path
   - Use bash wrapper for NVM support

2. **Avoid cursor-browser-extension**:
   - Requires Chrome extension
   - Has Linux-specific browser detection issues
   - Not reliably supported on Linux

3. **Always Use Explicit Paths**:
   - Never rely on automatic browser detection
   - Always specify `--executable-path` in MCP configs
   - Use absolute paths, not relative paths

4. **Test After Configuration Changes**:
   - Restart Cursor IDE completely after MCP config changes
   - Verify tools are accessible before assuming they work
   - Check MCP logs for connection status

## Related Documentation

- **OS-Level Issues**: `layer_0_universal/0.02_sub_layers/sub_layer_0.05_os_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MCP_ISSUES.md`
- **MCP Setup Experience**: `layer_0_universal/0.02_sub_layers/sub_layer_0.09_mcp_servers_and_tools_setup/trickle_down_0.75_universal_tools/0_instruction_docs/mcp-tools/BROWSER_MCP_SETUP_EXPERIENCE.md`
- **AI Apps Setup**: `layer_0_universal/0.02_sub_layers/sub_layer_0.08_ai_apps_tools_setup/`

## References

- Cursor IDE Documentation: https://cursor.com/docs
- GitHub Issues: #942, #1113 (Ubuntu-specific Playwright MCP problems)
- Cursor Forum: Browser Automation Linux Install Path discussions

---

**Last Updated**: 2025-12-02  
**Version**: 1.0

