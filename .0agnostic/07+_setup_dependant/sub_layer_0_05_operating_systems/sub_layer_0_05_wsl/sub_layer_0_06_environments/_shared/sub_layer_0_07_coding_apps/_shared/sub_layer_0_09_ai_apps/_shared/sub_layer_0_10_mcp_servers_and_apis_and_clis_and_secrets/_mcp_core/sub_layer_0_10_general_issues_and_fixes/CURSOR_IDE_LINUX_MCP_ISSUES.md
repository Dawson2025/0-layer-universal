---
resource_id: "33f3cafc-80c2-4edf-a7ac-826fb313e61e"
resource_type: "document"
resource_name: "CURSOR_IDE_LINUX_MCP_ISSUES"
---
# Cursor IDE Linux/Ubuntu MCP Issues

**Date**: 2025-12-02  
**Location**: Universal Layer → Coding App Setup  
**Status**: Critical Cursor IDE-specific limitations on Linux

<!-- section_id: "03d1a0b4-9328-48e8-ad0e-0d55476c2dac" -->
## Overview

This document outlines Linux/Ubuntu-specific issues with Cursor IDE's MCP (Model Context Protocol) integration. These issues affect how MCP servers are exposed to AI agents within Cursor IDE.

<!-- section_id: "168c7c7a-e860-4bb1-a4e6-3feb77b3a839" -->
## Critical Cursor IDE Issues on Linux

<!-- section_id: "b84cd322-3fc2-4113-8ae2-09a3e6131322" -->
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

<!-- section_id: "7fe3c33a-70a0-4490-9fdb-5db2888b9cf2" -->
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

<!-- section_id: "9a5f0095-d3eb-49d8-8d63-0dcbdeefe14f" -->
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

<!-- section_id: "9d2c1dbc-a60b-42b0-8891-9d86d8854ab5" -->
## Available vs. Unavailable Tools

<!-- section_id: "845aa9d9-860c-4840-b23b-1ab028871097" -->
### ✅ Available on Linux
- `mcp_cursor-browser-extension_*` (18 tools) - From Cursor's browser extension (may have browser detection issues)

<!-- section_id: "928825e5-5506-4b5b-a27f-f66dddece73f" -->
### ⚠️ May Be Available on Linux (Needs Verification)
- `mcp_browser_*` (21 tools) - From `@agent-infra/mcp-server-browser` (documentation claims should work, but needs testing)

<!-- section_id: "df98a4f1-36d9-4426-9d11-816ac83c2b6e" -->
### ❌ Not Available on Linux
- `mcp_playwright_*` (22 tools) - Server connects but tools not exposed to agents

<!-- section_id: "d54a82b0-df87-403a-9fe2-acdfcca4520b" -->
### ❌ Not Available on WSL (2025-12-05 Update)
- `mcp_playwright_*` (22 tools) - Server connects but tools not exposed to agents
- `mcp_browser_*` (21 tools) - **NEW FINDING**: Server runs but tools NOT exposed to agents (more severe than native Linux)

<!-- section_id: "2cbd49e5-a06c-495a-ac09-8c63da5b5969" -->
## Troubleshooting

<!-- section_id: "53aad2bb-c4f8-4960-ab00-427dfea35c81" -->
### Check MCP Server Status

```bash
# Check if MCP servers are running
ps aux | grep -E "playwright|mcp" | grep -v grep

# Check Cursor MCP logs
find ~/.config/Cursor/logs -name "*playwright*" -o -name "*mcp*" | head -5
```

<!-- section_id: "d00d1a3f-7bea-4488-9504-fb3d864804d2" -->
### Verify Configuration

```bash
# Check MCP configuration
cat ~/.cursor/mcp.json | jq '.'

# Verify browser paths
ls -la ~/.cache/ms-playwright/chromium-*/chrome-linux64/chrome
```

<!-- section_id: "2fcc98fc-3748-4bb0-8f4d-976b51ea0b3b" -->
### Check Tool Availability

In Cursor IDE:
1. Go to Settings → Tools & MCP
2. Check "Model Context Protocol" section
3. Verify which tools are listed as available
4. Note: Playwright tools may show as "22 tools" but not be accessible to agents

<!-- section_id: "0a85a982-1da7-4ef9-920f-3b8d069f8e75" -->
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

<!-- section_id: "dd1f2bc8-5f50-4590-b613-70abf263893b" -->
## Related Documentation

- **OS-Level Issues**: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MCP_ISSUES.md`
- **Browser MCP Setup Experience**: `../../browser-mcp/BROWSER_MCP_SETUP_EXPERIENCE.md`
- **AI Apps Setup**: `layer_0/0.02_sub_layers/sub_layer_0_09_ai_apps_tools_setup/`

<!-- section_id: "b1d9a148-dfe9-428d-a691-486472aea35f" -->
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

<!-- section_id: "d6eacf17-c07d-45f9-aaae-47392caf3bf6" -->
## WSL-Specific Findings (2025-12-05)

<!-- section_id: "e349e8f0-d0e2-4193-8e54-5f44ebe571fb" -->
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
