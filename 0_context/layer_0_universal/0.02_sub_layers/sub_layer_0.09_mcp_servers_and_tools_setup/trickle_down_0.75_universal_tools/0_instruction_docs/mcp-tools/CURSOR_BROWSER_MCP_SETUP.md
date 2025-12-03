# Cursor IDE Browser MCP Setup - Linux/Ubuntu

**Location**: Universal Tools → MCP Tools  
**Last Updated**: 2025-12-02  
**Status**: Configured, requires testing

## Overview

This document documents the setup and troubleshooting of browser MCP servers in Cursor IDE on Linux/Ubuntu systems. It covers Playwright MCP, browser MCP, and cursor-browser-extension MCP server configurations.

## Current Configuration

### MCP Servers Configured

**Location**: `~/.cursor/mcp.json`

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "-y",
        "@playwright/mcp@latest",
        "--browser",
        "chromium"
      ]
    },
    "browser": {
      "command": "npx",
      "args": [
        "-y",
        "@agent-infra/mcp-server-browser",
        "--executable-path",
        "/home/dawson/.cache/ms-playwright/chromium-1200/chrome-linux64/chrome"
      ]
    }
  }
}
```

### Status

- ✅ **Playwright MCP**: Configured, running (22 tools enabled)
- ✅ **Browser MCP**: Configured with explicit executable path (21 tools, 1 resource enabled)
- ⚠️ **cursor-browser-extension**: Shows "No server info found" - requires Chrome extension

## Browser Installation

### Chromium (Playwright)

**Installed via Node.js Playwright:**
```bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
npx -y playwright@latest install chromium
```

**Location**: `~/.cache/ms-playwright/chromium-1200/chrome-linux64/chrome`  
**Size**: 252MB  
**Status**: ✅ Installed and executable

### Google Chrome (System)

**Location**: `/usr/bin/google-chrome`  
**Version**: 143.0.7499.40  
**Status**: ✅ Installed

## Cursor IDE Browser Automation Settings

### Configuration

- **Browser Automation**: "Ready (Chrome detected)"
- **Connection Type**: "Custom Executable Path"
- **Chrome Executable Path**: `/usr/bin/google-chrome`

### Linux-Specific Issues

**Problem**: `cursor-browser-extension` MCP server shows "No server info found" even with:
- Chrome installed and detected
- Custom executable path configured
- All MCP servers running

**Root Cause**: The `cursor-browser-extension` MCP server requires the Cursor Chrome extension to be installed, regardless of browser path configuration.

**Solution Options**:
1. Install Cursor Chrome extension (community-developed, not official)
2. Use Playwright MCP tools directly (22 tools available)
3. Use browser MCP tools directly (21 tools available)

## Available Tools

### Playwright MCP (22 tools)
- Navigation: `browser_navigate`, `browser_navigate_back`, `browser_tabs`
- Interaction: `browser_click`, `browser_type`, `browser_hover`, `browser_drag`
- Forms: `browser_fill_form`, `browser_select_option`, `browser_file_upload`
- Information: `browser_snapshot`, `browser_take_screenshot`, `browser_console_messages`, `browser_network_requests`
- Code: `browser_evaluate`, `browser_run_code`
- Dialogs: `browser_handle_dialog`
- Management: `browser_close`, `browser_resize`, `browser_install`
- Waiting: `browser_wait_for`

### Browser MCP (21 tools, 1 resource)
- Similar tool set to Playwright
- Configured with explicit Chromium executable path

### cursor-browser-extension (18 tools)
- **Status**: Not working - requires Chrome extension
- Tools available but return "Browser specified in your config is not installed"

## Troubleshooting

### Issue: "Browser specified in your config is not installed"

**Symptoms**:
- Error appears even when Chrome/Chromium is installed
- `cursor-browser-extension` MCP shows "No server info found" in logs

**Linux-Specific Causes**:
1. Path detection fails on Linux
2. "Default (Bundled Chrome)" option may not work on Linux
3. `cursor-browser-extension` requires Chrome extension regardless of path

**Solutions**:
1. Set "Custom Executable Path" in Cursor settings: `/usr/bin/google-chrome`
2. Use Playwright MCP tools directly (they work without extension)
3. Use browser MCP tools directly (configured with explicit path)

### Issue: cursor-browser-extension "No server info found"

**Cause**: Requires Cursor Chrome extension to be installed

**Community Extension** (not official):
- Repository: https://github.com/sirvenis/cursor-mcp-extension
- Installation: Load unpacked extension from cloned repository
- Location: `/tmp/cursor-mcp-extension` (if cloned)

**Note**: According to Cursor documentation, browser automation is "native" and doesn't require an extension. The `cursor-browser-extension` MCP server may be separate from native browser automation.

## Verification

### Check MCP Servers Running
```bash
ps aux | grep -E "playwright|mcp.*browser" | grep -v grep
```

### Check Browser Installation
```bash
# Chromium (Playwright)
ls -la ~/.cache/ms-playwright/chromium-1200/chrome-linux64/chrome

# Chrome (System)
which google-chrome && google-chrome --version
```

### Check MCP Logs
```bash
LATEST_LOG=$(ls -t ~/.config/Cursor/logs/*/window*/exthost/anysphere.cursor-mcp/MCP\ cursor-browser-extension.log 2>/dev/null | head -1)
tail -20 "$LATEST_LOG"
```

## Recommended Approach

**For Linux/Ubuntu users:**

1. **Use Playwright MCP** (primary recommendation)
   - Most reliable on Linux
   - 22 tools available
   - No extension required
   - Cross-browser support

2. **Use Browser MCP** (alternative)
   - 21 tools available
   - Configured with explicit executable path
   - No extension required

3. **Avoid cursor-browser-extension** (if possible)
   - Requires Chrome extension
   - Linux-specific issues
   - Not officially supported

## References

- [Cursor Browser Documentation](https://cursor.com/docs/agent/browser)
- [Playwright MCP Setup Guide](../setup/playwright-mcp-cursor-setup.md)
- [Browser Automation Framework](../browser-automation/README.md)
- [MCP Configuration Guide](./MCP_CONFIGURATION_GUIDE.md)

## Related Documentation

- Universal Browser Opening Rule: `layer_0_universal/0.02_sub_layers/sub_layer_0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/browser_opening_rule.md`
- Playwright MCP Usage: `layer_0_universal/0.02_sub_layers/sub_layer_0.05_os_setup/trickle_down_0.5_setup/0_instruction_docs/setup/playwright-mcp-usage.md`

---

**Next Steps**: Test Playwright MCP tools directly to verify they work without the cursor-browser-extension.

