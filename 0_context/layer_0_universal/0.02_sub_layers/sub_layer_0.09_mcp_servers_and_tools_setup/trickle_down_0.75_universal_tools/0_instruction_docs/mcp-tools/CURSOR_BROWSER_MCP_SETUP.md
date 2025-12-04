# Cursor IDE Browser MCP Setup - Linux/Ubuntu

**Location**: Universal Tools → MCP Tools  
**Last Updated**: 2025-12-04  
**Status**: ✅ Working and tested

## Overview

This document documents the setup and troubleshooting of browser MCP servers in Cursor IDE on Linux/Ubuntu systems. It covers Playwright MCP, browser MCP, and cursor-browser-extension MCP server configurations.

## Current Configuration

### MCP Servers Configured

**Location**: `~/.cursor/mcp.json`

**Working Configuration (Verified 2025-12-04)**:
Simplified configuration that works reliably in Cursor IDE on Linux/Ubuntu:

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
        "@agent-infra/mcp-server-browser"
      ]
    },
    "web-search": {
      "command": "npx",
      "args": ["tavily-mcp"],
      "env": {
        "TAVILY_API_KEY": "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"
      }
    },
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp"],
      "env": {
        "CONTEXT7_API_KEY": "136116c4-6c35-4ffd-b8fa-cc8f11cb22a4"
      }
    }
  }
}
```

**Key Configuration Details**:
- **Simplified Playwright config**: Removed complex options (executable-path, user-data-dir, output-dir, viewport-size, etc.)
- Uses `--browser chromium` (Playwright will auto-detect the installed browser)
- No explicit paths needed - Playwright MCP handles browser detection automatically
- Same simple pattern works across different projects
- Configuration matches working setup from other projects (e.g., `code/I-eat-repo/.mcp.json`)

**Previous Complex Configuration (Not Recommended)**:
The previous configuration had many options that may cause issues:
- Explicit `--executable-path` pointing to `/usr/bin/google-chrome`
- Custom `--user-data-dir` and `--output-dir`
- `--viewport-size` and `--save-session` flags
- `PLAYWRIGHT_BROWSERS_PATH` environment variable

**Lesson Learned**: Simpler is better. The Playwright MCP server can automatically find and use Chromium without explicit paths.

### Status

- ✅ **Playwright MCP**: Configured, running, and **tested successfully** (2025-12-04)
- ✅ **Browser MCP**: Configured and working
- ✅ **Cursor IDE Browser Tools**: Working (`mcp_cursor-ide-browser_*` tools available)
- ⚠️ **cursor-browser-extension**: Shows "No server info found" - requires Chrome extension (not needed)

### Successful Setup Process (2025-12-04)

**Problem**: Playwright MCP was configured but needed verification and simplification.

**Solution**:
1. Located Cursor MCP config at `~/.cursor/mcp.json`
2. Compared with working configuration from other projects (`code/I-eat-repo/.mcp.json`)
3. Simplified Playwright configuration to match working pattern
4. Removed unnecessary options (executable-path, user-data-dir, output-dir, viewport-size, etc.)
5. Changed from `--browser chrome` to `--browser chromium` for auto-detection

**Testing Results**:
- ✅ Navigation: Successfully navigated to multiple websites (example.com, wikipedia.org, google.com, duckduckgo.com)
- ✅ Clicking: Successfully clicked links and buttons
- ✅ Typing: Successfully typed into search boxes and submitted forms
- ✅ Scrolling: Successfully scrolled pages
- ✅ Screenshots: Successfully captured screenshots
- ✅ Browser control: Full control over browser window (resize, navigate, interact)

**Available Tool Sets**:
1. **Cursor IDE Browser Tools** (`mcp_cursor-ide-browser_*`): 
   - Better integrated with Cursor IDE's built-in browser view
   - Tools: `browser_navigate`, `browser_snapshot`, `browser_click`, `browser_type`, `browser_hover`, `browser_resize`, `browser_take_screenshot`, etc.
   
2. **Playwright MCP Tools** (`mcp_browser_*`):
   - Direct Playwright MCP server tools
   - Tools: `browser_navigate`, `browser_click`, `browser_type`, `browser_scroll`, `browser_screenshot`, etc.

**Both tool sets work and provide full browser automation capabilities.**

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

## Setup Instructions

### Quick Setup for Cursor IDE

1. **Edit Cursor MCP Configuration**:
   ```bash
   # Edit the Cursor MCP config file
   nano ~/.cursor/mcp.json
   ```

2. **Add Simplified Playwright Configuration**:
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
       }
     }
   }
   ```

3. **Restart Cursor IDE**:
   - Close and reopen Cursor IDE to load the new MCP configuration
   - The Playwright MCP server will start automatically

4. **Verify Installation**:
   - Check that Chromium is installed: `npx playwright install chromium`
   - Verify MCP server is running in Cursor IDE settings

### Verification Test

After setup, test browser control:
- Navigate to a website
- Click links
- Type in search boxes
- Take screenshots
- Scroll pages

All of these should work with both:
- Cursor IDE browser tools (`mcp_cursor-ide-browser_*`)
- Playwright MCP tools (`mcp_browser_*`)

---

**Status**: ✅ Playwright MCP is working and tested in Cursor IDE (2025-12-04). Both Cursor IDE browser tools and Playwright MCP tools are functional.

