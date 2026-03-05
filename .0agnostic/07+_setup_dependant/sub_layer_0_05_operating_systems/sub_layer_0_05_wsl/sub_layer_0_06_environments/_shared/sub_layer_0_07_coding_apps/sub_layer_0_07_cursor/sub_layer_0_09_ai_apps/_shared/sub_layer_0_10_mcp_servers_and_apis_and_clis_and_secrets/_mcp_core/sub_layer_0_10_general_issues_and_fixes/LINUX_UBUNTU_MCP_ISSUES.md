---
resource_id: "6201fa88-7bdd-41ae-a35b-e7d2adc2e1c5"
resource_type: "document"
resource_name: "LINUX_UBUNTU_MCP_ISSUES"
---
# Linux/Ubuntu-Specific MCP Issues - OS Level

**Date**: 2025-12-02  
**Location**: Universal Layer → OS Setup  
**Status**: Critical platform-specific limitations

<!-- section_id: "37d566cc-8b2c-40b1-96a9-afb94170a982" -->
## Overview

This document outlines Linux/Ubuntu-specific issues that affect MCP (Model Context Protocol) server functionality at the OS level. These issues impact all MCP-dependent systems including Cursor IDE, AI apps, tools, and agents.

<!-- section_id: "52c67d01-f250-42fd-985b-45851c9cf0f4" -->
## Critical IDE-Level Issues

<!-- section_id: "17838247-df69-496f-bf8e-0aa73cebf451" -->
### 0. Cursor IDE Tool Exposure (Cross-Platform Bug)

**Problem**: Cursor IDE (v2.0.77+) fails to expose Playwright MCP tools to agents, even when the server connects successfully.

**Status**: Confirmed bug affecting Linux, Windows, and WSL.

**Impact**: 
- `mcp_playwright_*` tools are registered but not available to the agent.
- `mcp_browser_*` tools (from `@agent-infra`) ARE available on Linux (sometimes) but not WSL.

**See Detailed Analysis**: `CURSOR_IDE_LINUX_MCP_ISSUES.md`

<!-- section_id: "2d333107-169d-498c-9489-453d14c5b5f7" -->
## Critical OS-Level Issues

<!-- section_id: "90ad5148-1dbf-467b-84e5-6f83b3f40a57" -->
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

<!-- section_id: "15e0d8d4-2e39-4b00-b12f-928c036d81ef" -->
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

<!-- section_id: "c4259825-d56a-4a3f-9861-7f7de4f385ec" -->
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

<!-- section_id: "c95826a8-d9f0-4bfc-a325-47817a81c643" -->
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

<!-- section_id: "c523fcbc-e827-4fd4-94c5-3a342f0dfb57" -->
## Platform-Specific Configuration Requirements

<!-- section_id: "94c65010-adc2-4af7-a0d6-e03feca488dd" -->
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

<!-- section_id: "54eae743-1711-46c1-a97f-7283ca3ec1f2" -->
### Required System Dependencies

```bash
# Install Playwright system dependencies
npx playwright install-deps

# Verify browser installation
npx playwright install chromium
```

<!-- section_id: "275fbf2f-f5a6-4eda-9e20-322d486ed952" -->
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

<!-- section_id: "3749f85a-7140-4101-9fa5-05fef6219f42" -->
## Related Documentation

- **Browser MCP Setup Experience**: `../../browser-mcp/BROWSER_MCP_SETUP_EXPERIENCE.md`
- **Cursor IDE Setup**: `layer_0/0.02_sub_layers/sub_layer_0_07_coding_app_setup/`
- **AI Apps Setup**: `layer_0/0.02_sub_layers/sub_layer_0_09_ai_apps_tools_setup/`

<!-- section_id: "450e14f5-84d9-4844-9369-3f32f1f73a30" -->
## References

- GitHub Issues: #942, #1113 (Ubuntu-specific Playwright MCP problems)
- Playwright Linux Documentation: https://playwright.dev/docs/browsers#install-system-dependencies

---

**Last Updated**: 2025-12-02  
**Version**: 1.0
