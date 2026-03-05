---
resource_id: "d637fd74-9e32-418f-8230-5b7a0438ceae"
resource_type: "document"
resource_name: "LINUX_UBUNTU_MCP_ISSUES"
---
# Linux/Ubuntu-Specific MCP Issues - OS Level

**Date**: 2025-12-02  
**Location**: Universal Layer → OS Setup  
**Status**: Critical platform-specific limitations

<!-- section_id: "98fd54ab-d6fc-4834-b61f-a45ca802f36b" -->
## Overview

This document outlines Linux/Ubuntu-specific issues that affect MCP (Model Context Protocol) server functionality at the OS level. These issues impact all MCP-dependent systems including Cursor IDE, AI apps, tools, and agents.

<!-- section_id: "90c5893f-8c5e-4288-8380-9d0fb70ce6c0" -->
## Critical IDE-Level Issues

<!-- section_id: "886828d4-111b-49a2-a45f-6309e1188b3b" -->
### 0. Cursor IDE Tool Exposure (Cross-Platform Bug)

**Problem**: Cursor IDE (v2.0.77+) fails to expose Playwright MCP tools to agents, even when the server connects successfully.

**Status**: Confirmed bug affecting Linux, Windows, and WSL.

**Impact**: 
- `mcp_playwright_*` tools are registered but not available to the agent.
- `mcp_browser_*` tools (from `@agent-infra`) ARE available on Linux (sometimes) but not WSL.

**See Detailed Analysis**: `CURSOR_IDE_LINUX_MCP_ISSUES.md`

<!-- section_id: "cadc3f13-d1f0-424e-9fd8-b85825c7626f" -->
## Critical OS-Level Issues

<!-- section_id: "fdd2fdce-fe7e-47f3-b377-9087bf12d0a9" -->
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

<!-- section_id: "c84a64e7-fa9b-4c8e-9445-3ac186ee8e1a" -->
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

<!-- section_id: "e8b030e0-4108-4910-9109-689f785ab563" -->
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

<!-- section_id: "273f3f57-085e-460b-a34f-0218e4d23d17" -->
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

<!-- section_id: "0020b651-7fa2-4b3b-bbc6-bd4a6efea887" -->
## Platform-Specific Configuration Requirements

<!-- section_id: "219e7132-2de5-448a-94d6-a3360bec1a66" -->
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

<!-- section_id: "bd832b14-a0cf-431a-b360-42622e2bd950" -->
### Required System Dependencies

```bash
# Install Playwright system dependencies
npx playwright install-deps

# Verify browser installation
npx playwright install chromium
```

<!-- section_id: "30c75d48-f1ee-441d-bc2c-8941592ca7f3" -->
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

<!-- section_id: "b29148f1-e695-462f-aa15-dc8199aef725" -->
## Related Documentation

- **Browser MCP Setup Experience**: `../../browser-mcp/BROWSER_MCP_SETUP_EXPERIENCE.md`
- **Cursor IDE Setup**: `layer_0/0.02_sub_layers/sub_layer_0_07_coding_app_setup/`
- **AI Apps Setup**: `layer_0/0.02_sub_layers/sub_layer_0_09_ai_apps_tools_setup/`

<!-- section_id: "0c032152-a4ba-494c-9d25-d714feb03298" -->
## References

- GitHub Issues: #942, #1113 (Ubuntu-specific Playwright MCP problems)
- Playwright Linux Documentation: https://playwright.dev/docs/browsers#install-system-dependencies

---

**Last Updated**: 2025-12-02  
**Version**: 1.0
