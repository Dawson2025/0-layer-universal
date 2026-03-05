---
resource_id: "0522af32-8f4c-4d84-a03d-dd1d7e0526ac"
resource_type: "document"
resource_name: "LINUX_UBUNTU_MCP_ISSUES"
---
# Linux/Ubuntu-Specific MCP Issues - OS Level

**Date**: 2025-12-02  
**Location**: Universal Layer → OS Setup  
**Status**: Critical platform-specific limitations

<!-- section_id: "58476164-3a93-41e7-87e5-3d650a7780ad" -->
## Overview

This document outlines Linux/Ubuntu-specific issues that affect MCP (Model Context Protocol) server functionality at the OS level. These issues impact all MCP-dependent systems including Cursor IDE, AI apps, tools, and agents.

<!-- section_id: "db7b44dc-e5ad-4d30-94cf-69754cdbb04d" -->
## Critical IDE-Level Issues

<!-- section_id: "f31bc205-7df4-4348-9b4c-0101099fc397" -->
### 0. Cursor IDE Tool Exposure (Cross-Platform Bug)

**Problem**: Cursor IDE (v2.0.77+) fails to expose Playwright MCP tools to agents, even when the server connects successfully.

**Status**: Confirmed bug affecting Linux, Windows, and WSL.

**Impact**: 
- `mcp_playwright_*` tools are registered but not available to the agent.
- `mcp_browser_*` tools (from `@agent-infra`) ARE available on Linux (sometimes) but not WSL.

**See Detailed Analysis**: `CURSOR_IDE_LINUX_MCP_ISSUES.md`

<!-- section_id: "df66b5fd-25d0-4107-abd0-f1cddf1d9947" -->
## Critical OS-Level Issues

<!-- section_id: "8f0c41dc-1625-4fc5-86be-55e000e59117" -->
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

<!-- section_id: "c346978a-3110-43df-be74-fd816924a6c4" -->
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

<!-- section_id: "ab9b2089-aa90-491b-bc0f-1749fcb46311" -->
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

<!-- section_id: "dc52ea6c-11ee-4e0b-abb9-90d6221a7a33" -->
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

<!-- section_id: "a7a89449-6b39-4f66-ab19-ac8f00a6cdab" -->
## Platform-Specific Configuration Requirements

<!-- section_id: "c40cd859-2a17-4b8e-8df4-fb877bfa3837" -->
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

<!-- section_id: "133a6879-2ea5-4e14-9c56-667aba37ccac" -->
### Required System Dependencies

```bash
# Install Playwright system dependencies
npx playwright install-deps

# Verify browser installation
npx playwright install chromium
```

<!-- section_id: "df55dc52-fcfc-411d-8c3f-919e7377ac9e" -->
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

<!-- section_id: "2ee437cb-b10b-4be4-a1b9-3285a4365c8b" -->
## Related Documentation

- **Browser MCP Setup Experience**: `../../browser-mcp/BROWSER_MCP_SETUP_EXPERIENCE.md`
- **Cursor IDE Setup**: `layer_0/0.02_sub_layers/sub_layer_0_07_coding_app_setup/`
- **AI Apps Setup**: `layer_0/0.02_sub_layers/sub_layer_0_09_ai_apps_tools_setup/`

<!-- section_id: "f8a54be7-60ae-4f5c-9e7f-69bf3a9bd43a" -->
## References

- GitHub Issues: #942, #1113 (Ubuntu-specific Playwright MCP problems)
- Playwright Linux Documentation: https://playwright.dev/docs/browsers#install-system-dependencies

---

**Last Updated**: 2025-12-02  
**Version**: 1.0
