---
resource_id: "a08ec61d-6b85-421a-8573-ff7c54b07eba"
resource_type: "document"
resource_name: "LINUX_UBUNTU_MCP_ISSUES"
---
# Linux/Ubuntu-Specific MCP Issues - OS Level

**Date**: 2025-12-02  
**Location**: Universal Layer → OS Setup  
**Status**: Critical platform-specific limitations

<!-- section_id: "5dd321d0-8f3c-4c9b-95c6-ab47d6887630" -->
## Overview

This document outlines Linux/Ubuntu-specific issues that affect MCP (Model Context Protocol) server functionality at the OS level. These issues impact all MCP-dependent systems including Cursor IDE, AI apps, tools, and agents.

<!-- section_id: "1a65854e-f947-4dd4-b005-56f541766c98" -->
## Critical IDE-Level Issues

<!-- section_id: "e7484a8a-d8a6-4c30-ba59-0f75e5813b0b" -->
### 0. Cursor IDE Tool Exposure (Cross-Platform Bug)

**Problem**: Cursor IDE (v2.0.77+) fails to expose Playwright MCP tools to agents, even when the server connects successfully.

**Status**: Confirmed bug affecting Linux, Windows, and WSL.

**Impact**: 
- `mcp_playwright_*` tools are registered but not available to the agent.
- `mcp_browser_*` tools (from `@agent-infra`) ARE available on Linux (sometimes) but not WSL.

**See Detailed Analysis**: `CURSOR_IDE_LINUX_MCP_ISSUES.md`

<!-- section_id: "6d63e88b-34ec-4b9b-8c1a-aa722401776b" -->
## Critical OS-Level Issues

<!-- section_id: "c76565cc-3686-453e-a792-7088617370bb" -->
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

<!-- section_id: "6ee51058-f68e-445c-bdce-27e75fd2a8f8" -->
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

<!-- section_id: "5f4808d5-2c2e-426a-9f50-ff507e7de6e5" -->
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

<!-- section_id: "2ee2fcac-2b11-4751-b9cd-98ef27ba8872" -->
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

<!-- section_id: "6fd3a5ce-f551-4e60-916f-21d3f189b6c7" -->
## Platform-Specific Configuration Requirements

<!-- section_id: "8592e1ba-c6ad-4995-8e03-4437f30af2af" -->
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

<!-- section_id: "cddc8b66-e06e-474f-be00-4e0a633a714b" -->
### Required System Dependencies

```bash
# Install Playwright system dependencies
npx playwright install-deps

# Verify browser installation
npx playwright install chromium
```

<!-- section_id: "055fdb2c-260a-4cbd-9105-fe955fa9f4f3" -->
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

<!-- section_id: "384b0553-33e5-4d3c-a82d-499b304990bc" -->
## Related Documentation

- **Browser MCP Setup Experience**: `../../browser-mcp/BROWSER_MCP_SETUP_EXPERIENCE.md`
- **Cursor IDE Setup**: `layer_0/0.02_sub_layers/sub_layer_0_07_coding_app_setup/`
- **AI Apps Setup**: `layer_0/0.02_sub_layers/sub_layer_0_09_ai_apps_tools_setup/`

<!-- section_id: "62301f6f-cab4-4a42-b8d7-34f1bca2d3ac" -->
## References

- GitHub Issues: #942, #1113 (Ubuntu-specific Playwright MCP problems)
- Playwright Linux Documentation: https://playwright.dev/docs/browsers#install-system-dependencies

---

**Last Updated**: 2025-12-02  
**Version**: 1.0
