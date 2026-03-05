---
resource_id: "e512df28-16da-493e-8a52-fc83686842e9"
resource_type: "document"
resource_name: "LINUX_UBUNTU_MCP_ISSUES"
---
# Linux/Ubuntu-Specific MCP Issues - OS Level

**Date**: 2025-12-02  
**Location**: Universal Layer → OS Setup  
**Status**: Critical platform-specific limitations

<!-- section_id: "5217d624-888a-43b6-ae5a-2910d2fbdf47" -->
## Overview

This document outlines Linux/Ubuntu-specific issues that affect MCP (Model Context Protocol) server functionality at the OS level. These issues impact all MCP-dependent systems including Cursor IDE, AI apps, tools, and agents.

<!-- section_id: "127bc2f7-6cc7-4542-a4cd-83dac82ce1bd" -->
## Critical IDE-Level Issues

<!-- section_id: "0fdee88f-2ddb-4e22-ae72-df1a6b9771b4" -->
### 0. Cursor IDE Tool Exposure (Cross-Platform Bug)

**Problem**: Cursor IDE (v2.0.77+) fails to expose Playwright MCP tools to agents, even when the server connects successfully.

**Status**: Confirmed bug affecting Linux, Windows, and WSL.

**Impact**: 
- `mcp_playwright_*` tools are registered but not available to the agent.
- `mcp_browser_*` tools (from `@agent-infra`) ARE available on Linux (sometimes) but not WSL.

**See Detailed Analysis**: `CURSOR_IDE_LINUX_MCP_ISSUES.md`

<!-- section_id: "f6a2dac4-9749-4409-b360-9c6752d9911d" -->
## Critical OS-Level Issues

<!-- section_id: "8d1ca180-a1ce-4a8a-b8a4-9a8c87dc3128" -->
### 1. Browser Path Detection

**Problem**: Linux does not have a standard browser installation location, causing automatic browser detection to fail.

**Impact**: 
- MCP servers cannot automatically find browser executables
- Browser automation tools fail with "Browser not installed" errors
- Affects all browser-based MCP servers (Playwright, Browser MCP, cursor-browser-extension)

**Solution**: Always use explicit browser paths in MCP configurations:
```json
{
  "browser": {
    "args": [
      "--executable-path",
      "/absolute/path/to/browser"
    ]
  }
}
```

**Common Browser Locations on Linux**:
- Playwright Chromium: `~/.cache/ms-playwright/chromium-*/chrome-linux64/chrome`
- System Chrome: `/usr/bin/google-chrome` or `/usr/bin/chromium-browser`
- System Chromium: `/usr/bin/chromium`

<!-- section_id: "55aab0b5-9994-4864-9ee0-1f8b2412a284" -->
### 2. NVM/Node.js Environment Variables

**Problem**: MCP server processes do not inherit NVM environment variables, causing Node.js/npx to be unavailable.

**Impact**:
- MCP servers fail to start
- `npx` commands not found
- Node.js-based MCP servers cannot execute

**Solution**: Use bash wrapper to load NVM in MCP server processes:
```json
{
  "playwright": {
    "command": "bash",
    "args": [
      "-c",
      "export NVM_DIR=\"$HOME/.nvm\" && [ -s \"$NVM_DIR/nvm.sh\" ] && \\. \"$NVM_DIR/nvm.sh\" && npx -y @playwright/mcp@latest --browser chromium"
    ]
  }
}
```

<!-- section_id: "ccd780d1-637b-4ecc-b16f-ea5472404d26" -->
### 3. Display/Graphics Environment

**Problem**: Headed browser automation requires proper DISPLAY environment variable and graphics support.

**Impact**:
- Browser windows may not open
- Screenshots may fail
- Visual debugging unavailable

**Solution**: Ensure DISPLAY is set:
```bash
export DISPLAY=:0
# Or for remote: export DISPLAY=:10.0
```

<!-- section_id: "6e836a2e-d3da-4431-ae2f-34c9cf2a559a" -->
### 4. File Permissions and Paths

**Problem**: Linux file permissions and path conventions differ from Windows/macOS.

**Impact**:
- MCP servers may not have execute permissions
- Path resolution issues
- Configuration file access problems

**Solution**: 
- Use absolute paths in configurations
- Verify executable permissions: `chmod +x /path/to/executable`
- Check file ownership and permissions

<!-- section_id: "33409f3a-52d3-4606-9f05-088f247ded2a" -->
## Platform-Specific Configuration Requirements

<!-- section_id: "e8b04b1c-f019-4047-97b0-c1d4658ef901" -->
### Required Environment Variables

```bash
# NVM (if using Node.js via NVM)
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"

# Display (for headed browsers)
export DISPLAY=:0

# Playwright browsers path
export PLAYWRIGHT_BROWSERS_PATH="$HOME/.cache/ms-playwright"
```

<!-- section_id: "c4c34bc9-c6e8-4a7f-93a7-5e68460c291c" -->
### Required System Dependencies

```bash
# Install Playwright system dependencies
npx playwright install-deps

# Verify browser installation
npx playwright install chromium
```

<!-- section_id: "b226f99f-c785-4e9b-8de9-b92f08b1a002" -->
## Verification Commands

```bash
# Check browser installation
ls -la ~/.cache/ms-playwright/chromium-*/chrome-linux64/chrome

# Check Node.js availability
which node && node --version
which npx && npx --version

# Check DISPLAY
echo $DISPLAY

# Verify MCP server processes
ps aux | grep -E "playwright|mcp" | grep -v grep
```

<!-- section_id: "47fa797b-d93f-4a62-b475-1149492c3c2a" -->
## Related Documentation

- **Browser MCP Setup Experience**: `../../browser-mcp/BROWSER_MCP_SETUP_EXPERIENCE.md`
- **Cursor IDE Setup**: `layer_0/0.02_sub_layers/sub_layer_0_07_coding_app_setup/`
- **AI Apps Setup**: `layer_0/0.02_sub_layers/sub_layer_0_09_ai_apps_tools_setup/`

<!-- section_id: "56bc7d98-6cd8-4089-ad19-b0c1b42b05b1" -->
## References

- GitHub Issues: #942, #1113 (Ubuntu-specific Playwright MCP problems)
- Playwright Linux Documentation: https://playwright.dev/docs/browsers#install-system-dependencies

---

**Last Updated**: 2025-12-02  
**Version**: 1.0
