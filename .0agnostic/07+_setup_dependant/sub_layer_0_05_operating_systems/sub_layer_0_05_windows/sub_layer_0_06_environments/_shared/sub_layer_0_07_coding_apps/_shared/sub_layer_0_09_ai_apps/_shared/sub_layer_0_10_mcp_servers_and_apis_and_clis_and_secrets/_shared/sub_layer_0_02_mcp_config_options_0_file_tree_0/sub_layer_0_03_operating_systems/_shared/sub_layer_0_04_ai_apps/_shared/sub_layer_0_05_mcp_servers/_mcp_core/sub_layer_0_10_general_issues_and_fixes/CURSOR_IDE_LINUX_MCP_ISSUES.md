---
resource_id: "40d16aa2-3a2d-4c36-bc20-72695bbb1b70"
resource_type: "document"
resource_name: "CURSOR_IDE_LINUX_MCP_ISSUES"
---
# Cursor IDE Linux/Ubuntu MCP Issues

**Date**: 2025-12-02  
**Location**: Universal Layer → Coding App Setup  
**Status**: Critical Cursor IDE-specific limitations on Linux

<!-- section_id: "c84975cc-1788-499b-8786-efb2b2a2cfed" -->
## Overview

This document outlines Linux/Ubuntu-specific issues with Cursor IDE's MCP (Model Context Protocol) integration. These issues affect how MCP servers are exposed to AI agents within Cursor IDE.

<!-- section_id: "c58ead81-8444-4054-9eea-fe3a1d32ca3a" -->
## Critical Cursor IDE Issues on Linux

<!-- section_id: "2691fa75-7bbc-495a-869b-9e91212bfaea" -->
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

**Root Cause**: 
- **Primary**: Cursor IDE bug (version 2.0.77 has known issue where MCP tools aren't exposed to agents)
- **Secondary**: Cursor IDE's MCP tool exposure mechanism may have platform-specific behavior
- **Evidence**: Internet research (2025-12-05) shows Windows users also experiencing the same issues
- **Conclusion**: This is primarily a Cursor IDE bug affecting multiple platforms, not just Linux

**Workaround**: 
- **Native Linux**: Use `mcp_browser_*` tools from `@agent-infra/mcp-server-browser` (if available) or `mcp_cursor-browser-extension_*` tools
- **WSL**: Use `mcp_cursor-browser-extension_*` tools (both Playwright and Browser MCP tools are not exposed in WSL)

<!-- section_id: "b928cc1b-9e04-4e6a-9e5f-fef63e401edb" -->
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

<!-- section_id: "d18d92db-4883-495d-b281-7a30461e78d3" -->
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

<!-- section_id: "67aaff55-b02e-46fb-96d2-19ada9412cb7" -->
## Available vs. Unavailable Tools

<!-- section_id: "519ad1cf-64de-46c5-a528-279076f36f7b" -->
### ✅ Available on Linux
- `mcp_cursor-browser-extension_*` (18 tools) - From Cursor's browser extension (may have browser detection issues)

<!-- section_id: "ee1871fd-de2e-49b7-bd9c-f0805c578a80" -->
### ⚠️ May Be Available on Linux (Needs Verification)
- `mcp_browser_*` (21 tools) - From `@agent-infra/mcp-server-browser` (documentation claims should work, but needs testing)

<!-- section_id: "ae4b6de7-f4dd-441c-ac19-dfb4cd8f44b5" -->
### ❌ Not Available on Linux
- `mcp_playwright_*` (22 tools) - Server connects but tools not exposed to agents

<!-- section_id: "fd236325-7d43-42cb-b9ef-bfc0963b7849" -->
### ❌ Not Available on WSL (2025-12-05 Update)
- `mcp_playwright_*` (22 tools) - Server connects but tools not exposed to agents
- `mcp_browser_*` (21 tools) - **NEW FINDING**: Server runs but tools NOT exposed to agents (more severe than native Linux)

<!-- section_id: "bf7359b4-961b-40e1-bf28-ebb475cd853f" -->
## Troubleshooting

<!-- section_id: "b8f75b28-80fc-4621-86f0-c726b3558a81" -->
### Check MCP Server Status

```bash
# Check if MCP servers are running
ps aux | grep -E "playwright|mcp" | grep -v grep

# Check Cursor MCP logs
find ~/.config/Cursor/logs -name "*playwright*" -o -name "*mcp*" | head -5
```

<!-- section_id: "f46c5eeb-67c6-44c9-8639-7d3c71783019" -->
### Verify Configuration

```bash
# Check MCP configuration
cat ~/.cursor/mcp.json | jq '.'

# Verify browser paths
ls -la ~/.cache/ms-playwright/chromium-*/chrome-linux64/chrome
```

<!-- section_id: "296abe96-7575-4fd9-8a73-78cbb5f9fa9e" -->
### Check Tool Availability

In Cursor IDE:
1. Go to Settings → Tools & MCP
2. Check "Model Context Protocol" section
3. Verify which tools are listed as available
4. Note: Playwright tools may show as "22 tools" but not be accessible to agents

<!-- section_id: "1aa199c4-a632-450c-b676-474f8d7b8e5d" -->
## Recommendations for Linux Users

1. **Use Cursor Browser Extension Tools** (Most Reliable):
   - `mcp_cursor-browser-extension_*` tools are accessible on both Linux and WSL
   - Configure browser path in Cursor Settings → Tools & MCP → Browser Automation
   - These tools work despite other MCP tools not being exposed

2. **For Native Linux: Try Browser MCP** (If Available):
   - Browser MCP tools (`mcp_browser_*`) may be accessible on native Linux
   - Configure with explicit browser path and environment variables
   - Use bash wrapper for NVM support if needed
   - **Note**: Needs verification - documentation claims should work but not confirmed

3. **For WSL: Use Cursor Browser Extension Only**:
   - Both Playwright and Browser MCP tools are NOT exposed in WSL
   - Only `mcp_cursor-browser-extension_*` tools are available
   - This is more severe than native Linux

2. **For WSL: cursor-browser-extension is the Only Option**:
   - In WSL, both Playwright and Browser MCP tools are not exposed
   - `mcp_cursor-browser-extension_*` tools are the only browser automation tools available
   - Configure browser path in Cursor Settings (use Windows Chrome path: `C:\Program Files\Google\Chrome\Application\chrome.exe`)

3. **Always Use Explicit Paths**:
   - Never rely on automatic browser detection
   - Always specify `--executable-path` in MCP configs
   - Use absolute paths, not relative paths

4. **Test After Configuration Changes**:
   - Restart Cursor IDE completely after MCP config changes
   - Verify tools are accessible before assuming they work
   - Check MCP logs for connection status

<!-- section_id: "09b10916-182f-4a57-ad45-8e041fbfc1c0" -->
## Related Documentation

- **OS-Level Issues**: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MCP_ISSUES.md`
- **Browser MCP Setup Experience**: `../../browser-mcp/BROWSER_MCP_SETUP_EXPERIENCE.md`
- **AI Apps Setup**: `layer_0/0.02_sub_layers/sub_layer_0_09_ai_apps_tools_setup/`

<!-- section_id: "a478f75d-b7a1-4a57-88d3-a5829eae597c" -->
## References

- Cursor IDE Documentation: https://cursor.com/docs
- GitHub Issues: #942, #1113 (Ubuntu-specific Playwright MCP problems)
- Cursor Forum: Browser Automation Linux Install Path discussions
- **Internet Research (2025-12-05)**:
  - Cursor Forum: "MCP servers are not exposed to agents" (version 2.0.77 bug)
  - Cursor Forum: "Browser Agent Tools Not Accessible Despite 'Ready' Status" (Windows users)
  - Cursor Forum: "Playwright MCP not working on Cursor" (cross-platform)
  - See [MCP Tool Exposure OS Analysis](./MCP_TOOL_EXPOSURE_OS_ANALYSIS.md) for comprehensive findings

---

<!-- section_id: "4b2a10d1-e987-424c-a0bf-938c60183a22" -->
## WSL-Specific Findings (2025-12-05)

<!-- section_id: "f6401a7d-bc28-4e80-bb76-fd81dbc3f08c" -->
### Critical WSL Discovery

**Finding**: In WSL2, BOTH Playwright AND Browser MCP tools are NOT exposed to AI agents, even though:
- Both servers connect successfully
- Both servers report tools as registered
- Server processes are running correctly
- Environment variables are configured properly

**Impact**: This is MORE severe than native Linux, where Browser MCP tools may be available.

**Available Tools in WSL**:
- ✅ `mcp_cursor-browser-extension_*` (18 tools) - Only browser automation option in WSL
- ❌ `mcp_playwright_*` (22 tools) - Not exposed
- ❌ `mcp_browser_*` (21 tools) - Not exposed

**WSL Configuration Notes**:
- Cursor IDE runs on Windows but connects to WSL
- MCP servers run in WSL environment
- Browser path in Cursor Settings should use Windows path: `C:\Program Files\Google\Chrome\Application\chrome.exe`
- Environment variables in MCP config use Linux paths: `/home/dawson/.cache/ms-playwright`

**See Also**: [MCP Tool Exposure OS Analysis](./MCP_TOOL_EXPOSURE_OS_ANALYSIS.md) for comprehensive platform comparison

---

**Last Updated**: 2025-12-05  
**Version**: 2.0
