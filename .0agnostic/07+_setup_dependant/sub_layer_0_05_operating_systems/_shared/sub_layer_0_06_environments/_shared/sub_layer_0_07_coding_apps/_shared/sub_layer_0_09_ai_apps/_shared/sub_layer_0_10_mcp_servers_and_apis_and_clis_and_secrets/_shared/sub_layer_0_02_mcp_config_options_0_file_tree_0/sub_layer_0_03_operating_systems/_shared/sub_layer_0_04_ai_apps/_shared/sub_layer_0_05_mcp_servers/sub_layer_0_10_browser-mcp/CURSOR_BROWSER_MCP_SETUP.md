---
resource_id: "ceb4a2f4-e026-432e-ba12-d94ffe3aae37"
resource_type: "document"
resource_name: "CURSOR_BROWSER_MCP_SETUP"
---
# Cursor IDE Browser MCP Setup - Linux/Ubuntu

**Location**: Universal Tools → MCP Tools  
**Last Updated**: 2025-12-05  
**Status**: ✅ Working and tested (Linux/Ubuntu), ⚠️ Partially working (WSL)

<!-- section_id: "befcdb00-9582-4661-9058-8cc5f46fedff" -->
## Overview

This document documents the setup and troubleshooting of browser MCP servers in Cursor IDE on Linux/Ubuntu systems, including WSL (Windows Subsystem for Linux) environments. It covers Playwright MCP, browser MCP, and cursor-browser-extension MCP server configurations.

**Platforms Covered**:
- ✅ Native Linux/Ubuntu
- ⚠️ WSL2 (Ubuntu 24.04) on Windows 11 (Lenovo Yoga 9 Pro)

<!-- section_id: "03125663-e127-42ed-962f-7e7f2430f6c9" -->
## Current Configuration

<!-- section_id: "eac07a51-7532-4103-ac03-f6518e668b56" -->
### MCP Servers Configured

**Location**: `~/.cursor/mcp.json`

**Working Configuration (Verified 2025-12-05 - Updated with Environment Variables)**:
Configuration that works reliably in Cursor IDE on Linux/Ubuntu with proper environment variable setup:

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
      ],
      "env": {
        "PLAYWRIGHT_BROWSERS_PATH": "/home/dawson/.cache/ms-playwright",
        "HOME": "/home/dawson"
      }
    },
    "browser": {
      "command": "npx",
      "args": [
        "@agent-infra/mcp-server-browser"
      ],
      "env": {
        "PLAYWRIGHT_BROWSERS_PATH": "/home/dawson/.cache/ms-playwright",
        "HOME": "/home/dawson"
      }
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

**Critical Configuration Notes**:
- **Environment Variables Required**: The `PLAYWRIGHT_BROWSERS_PATH` and `HOME` environment variables are essential for MCP servers to find installed browsers
- **Why This Matters**: MCP servers run via `npx` in isolated environments and don't inherit your shell's environment variables
- **Prevents Recurring Issues**: This configuration prevents the constant "browser needs installation" problem
- **Replace Paths**: Replace `/home/dawson` with your actual home directory path

**Key Configuration Details**:
- **Environment Variables**: `PLAYWRIGHT_BROWSERS_PATH` and `HOME` are required for MCP servers to find browsers
- **Simplified Playwright config**: Removed complex options (executable-path, user-data-dir, output-dir, viewport-size, etc.)
- Uses `--browser chromium` (Playwright will auto-detect the installed browser when environment variables are set)
- **Critical Fix**: Environment variables prevent the recurring "browser needs installation" problem
- Same pattern works across different projects when environment variables are included

**Previous Complex Configuration (Not Recommended)**:
The previous configuration had many options that may cause issues:
- Explicit `--executable-path` pointing to `/usr/bin/google-chrome`
- Custom `--user-data-dir` and `--output-dir`
- `--viewport-size` and `--save-session` flags
- `PLAYWRIGHT_BROWSERS_PATH` environment variable

**Lesson Learned**: Simpler is better. The Playwright MCP server can automatically find and use Chromium without explicit paths.

<!-- section_id: "3b4db2dd-3d34-4cea-bcdd-d1cbcc2127e7" -->
### Status

- ✅ **Playwright MCP**: Configured, running, and **tested successfully** (2025-12-04)
- ✅ **Browser MCP**: Configured and working
- ✅ **Cursor IDE Browser Tools**: Working (`mcp_cursor-ide-browser_*` tools available)
- ⚠️ **cursor-browser-extension**: Shows "No server info found" - requires Chrome extension (not needed)

<!-- section_id: "3cfce580-8e7d-44de-8f0c-ba5cd83ddda6" -->
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

<!-- section_id: "dd5befe9-9eb7-42c1-b46c-75a2cc1ec518" -->
## Browser Installation

<!-- section_id: "cab9b582-28db-407e-9804-925787174ea7" -->
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

<!-- section_id: "b5a83504-cddd-490c-ba07-f7b07b9e139a" -->
### Google Chrome (System)

**Location**: `/usr/bin/google-chrome`  
**Version**: 143.0.7499.40  
**Status**: ✅ Installed

<!-- section_id: "13f3cdbc-5306-4596-8c17-60b325410a76" -->
## Cursor IDE Browser Automation Settings

<!-- section_id: "c50ce5a6-462f-4eac-99e2-06f8685b6e6d" -->
### Configuration

- **Browser Automation**: "Ready (Chrome detected)"
- **Connection Type**: "Custom Executable Path"
- **Chrome Executable Path**: `/usr/bin/google-chrome`

<!-- section_id: "6c97a49f-06f9-483b-bbf0-60d995982969" -->
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

<!-- section_id: "ea10ccc4-935d-4d29-87cd-781dca16b0a9" -->
## Available Tools

<!-- section_id: "bcc185e6-29c8-4b85-bde5-c1eb33c40fa3" -->
### Playwright MCP (22 tools)
- Navigation: `browser_navigate`, `browser_navigate_back`, `browser_tabs`
- Interaction: `browser_click`, `browser_type`, `browser_hover`, `browser_drag`
- Forms: `browser_fill_form`, `browser_select_option`, `browser_file_upload`
- Information: `browser_snapshot`, `browser_take_screenshot`, `browser_console_messages`, `browser_network_requests`
- Code: `browser_evaluate`, `browser_run_code`
- Dialogs: `browser_handle_dialog`
- Management: `browser_close`, `browser_resize`, `browser_install`
- Waiting: `browser_wait_for`

<!-- section_id: "02b6fe4e-d281-4155-9bdb-b6bb2e901e5e" -->
### Browser MCP (21 tools, 1 resource)
- Similar tool set to Playwright
- Configured with explicit Chromium executable path

<!-- section_id: "c7c509e2-43a0-4c3e-a532-882a3b1356ab" -->
### cursor-browser-extension (18 tools)
- **Status**: Not working - requires Chrome extension
- Tools available but return "Browser specified in your config is not installed"

<!-- section_id: "6d4bd8b1-5500-4848-9f1d-c812bee58ea8" -->
## Troubleshooting

<!-- section_id: "945646bd-b6fe-43f6-a150-671334c5e354" -->
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

<!-- section_id: "d6167353-59a1-4e36-b148-0507fb04cf40" -->
### Issue: cursor-browser-extension "No server info found"

**Cause**: Requires Cursor Chrome extension to be installed

**Community Extension** (not official):
- Repository: https://github.com/sirvenis/cursor-mcp-extension
- Installation: Load unpacked extension from cloned repository
- Location: `/tmp/cursor-mcp-extension` (if cloned)

**Note**: According to Cursor documentation, browser automation is "native" and doesn't require an extension. The `cursor-browser-extension` MCP server may be separate from native browser automation.

<!-- section_id: "d5c57fc1-240e-45cc-a6af-39cd428e02fe" -->
## WSL (Windows Subsystem for Linux) Setup - Lenovo Yoga 9 Pro

**Last Updated**: 2025-12-05  
**Environment**: WSL2 (Ubuntu 24.04) on Windows 11, Lenovo Yoga 9 Pro  
**Status**: ⚠️ Partially Working - Configuration documented, requires Windows Chrome path  
**Critical Finding (2025-12-05)**: In WSL, both Playwright and Browser MCP tools are NOT exposed to AI agents. Only `mcp_cursor-browser-extension_*` tools are available.

<!-- section_id: "4094d5e3-7ba2-4360-8cf6-ccd9c494cec2" -->
### WSL-Specific Configuration

When running Cursor IDE within WSL, the browser automation setup requires special consideration because:

1. **Cursor IDE runs on Windows** but connects to WSL for terminal/development
2. **Chrome can be installed in both WSL and Windows**
3. **Browser extension needs Windows Chrome path**, not WSL Chrome path

<!-- section_id: "9b5fea15-0463-4d3d-a998-d830a08787eb" -->
### System Configuration

**WSL Environment**:
- OS: Ubuntu 24.04 (WSL2)
- Display: `DISPLAY=:0` (X11 forwarding configured)
- Chrome in WSL: `/usr/bin/google-chrome` → `/opt/google/chrome/google-chrome` (symlink)
- Chrome in Windows: `C:\Program Files\Google\Chrome\Application\chrome.exe`
- Chrome Version (WSL): 142.0.7444.162
- Chrome Version (Windows): Available and accessible from WSL

<!-- section_id: "04d82e97-265c-4ab1-b932-a9714d25f67e" -->
### Setup Process Attempted (2025-12-05)

#### Step 1: Initial WSL Chrome Path Configuration

**Attempted**: Configure Cursor with WSL Chrome path
- **Path tried**: `/usr/bin/google-chrome`
- **Result**: Settings showed "Ready (Chrome detected)" but MCP server returned "Browser specified in your config is not installed"
- **Logs showed**: "No server info found" errors

**Verification**:
```bash
# Chrome exists in WSL
which google-chrome
# Output: /usr/bin/google-chrome

# Follow symlink to actual location
readlink -f /usr/bin/google-chrome
# Output: /opt/google/chrome/google-chrome

# Verify executable
test -x /opt/google/chrome/google-chrome && echo "Executable"
# Output: Executable exists and is executable
```

#### Step 2: Updated to Actual Executable Path

**Attempted**: Use resolved symlink path
- **Path tried**: `/opt/google/chrome/google-chrome`
- **Result**: Settings showed "Ready (Chrome detected)" but MCP server still returned errors
- **MCP logs**: Still showing "No server info found"

#### Step 3: Windows Chrome Path Configuration

**Attempted**: Configure with Windows Chrome path (since Cursor runs on Windows)
- **Path tried**: `C:\Program Files\Google\Chrome\Application\chrome.exe`
- **Result**: ✅ Settings showed "Ready (Chrome detected)" and Chrome window opened when settings were saved
- **Status**: Configuration appears correct, but MCP server tools still return errors

**Verification**:
```bash
# Windows Chrome accessible from WSL
ls -la "/mnt/c/Program Files/Google/Chrome/Application/chrome.exe"
# Output: File exists and is readable

# Test Windows Chrome execution
"/mnt/c/Program Files/Google/Chrome/Application/chrome.exe" --version
# Output: Opens in existing browser session (works)
```

<!-- section_id: "ea504029-a516-4fa9-a5f4-3730ea7b7fb3" -->
### Current Configuration (WSL)

**Cursor Settings → Tools → Browser Automation**:
- **Connection Type**: "Custom Executable Path"
- **Chrome Executable Path**: `C:\Program Files\Google\Chrome\Application\chrome.exe`
- **Status**: "Ready (Chrome detected)"
- **Show Localhost Links in Browser**: Enabled

**MCP Configuration** (`~/.config/mcp/mcp.json`):
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
      ],
      "env": {
        "PLAYWRIGHT_BROWSERS_PATH": "0"
      }
    },
    "browser": {
      "command": "npx",
      "args": [
        "@agent-infra/mcp-server-browser"
      ],
      "env": {
        "BROWSER_PATH": "/opt/google/chrome/google-chrome"
      }
    }
  }
}
```

<!-- section_id: "068b18a6-d216-4c40-a5db-04e058ee6412" -->
### WSL-Specific Issues Encountered

#### Issue 1: MCP Server Not Reading Browser Path

**Symptoms**:
- Cursor UI shows "Ready (Chrome detected)" with correct path
- `cursor-browser-extension` MCP server logs show "No server info found"
- Browser tools return: "Browser specified in your config is not installed"

**Root Cause Analysis**:
- The `cursor-browser-extension` MCP server appears to be a built-in Cursor feature
- It should read browser path from Cursor's UI settings, but isn't picking it up
- This may be a bug in how Cursor passes configuration to the MCP server layer
- WSL environment may add complexity to path resolution

**Attempted Solutions**:
1. ✅ Updated browser path in Cursor Settings UI
2. ✅ Tried both WSL path (`/opt/google/chrome/google-chrome`) and Windows path (`C:\Program Files\Google\Chrome\Application\chrome.exe`)
3. ✅ Restarted Cursor multiple times
4. ✅ Verified Chrome executable exists and is accessible
5. ⚠️ MCP server still not connecting properly

#### Issue 2: Path Resolution in WSL

**Finding**: Chrome in WSL is a symlink chain:
```
/usr/bin/google-chrome → /etc/alternatives/google-chrome → /opt/google/chrome/google-chrome
```

**Impact**: Using `/usr/bin/google-chrome` should work (symlinks are resolved), but explicit path may be more reliable.

<!-- section_id: "f49686f6-9b37-47fe-84a5-77a83d7e5db7" -->
### WSL Troubleshooting Steps

#### Check WSL Chrome Installation
```bash
# Find Chrome in WSL
which google-chrome
readlink -f $(which google-chrome)

# Verify executable
test -x /opt/google/chrome/google-chrome && echo "WSL Chrome OK"
```

#### Check Windows Chrome from WSL
```bash
# Verify Windows Chrome accessible
test -f "/mnt/c/Program Files/Google/Chrome/Application/chrome.exe" && echo "Windows Chrome OK"

# Test execution
"/mnt/c/Program Files/Google/Chrome/Application/chrome.exe" --version
```

#### Check MCP Server Logs
```bash
# Find latest cursor-browser-extension log
find ~/.cursor-server/data/logs -name "*cursor-browser-extension.log" -type f -exec ls -t {} + | head -1

# View recent errors
tail -30 "$(find ~/.cursor-server/data/logs -name '*cursor-browser-extension.log' -type f -exec ls -t {} + | head -1)"
```

#### Check Display Configuration
```bash
# Verify X11 forwarding
echo $DISPLAY
# Should output: :0 or similar

# Check if GUI apps can run
which xeyes || echo "X11 apps not available"
```

<!-- section_id: "45289ea3-ac6f-474c-baa6-057ac5a2135f" -->
### Recommended WSL Configuration

**For Cursor IDE Browser Automation in WSL**:

1. **Use Windows Chrome Path** (Primary recommendation):
   - Set Chrome Executable Path to: `C:\Program Files\Google\Chrome\Application\chrome.exe`
   - This works because Cursor IDE runs on Windows and needs to launch Windows Chrome
   - Status should show "Ready (Chrome detected)"

2. **WSL Limitation - Playwright/Browser MCP Not Available**:
   - ⚠️ **In WSL, Playwright MCP tools are NOT exposed to AI agents** (2025-12-05 finding)
   - ⚠️ **In WSL, Browser MCP tools are also NOT exposed** (2025-12-05 finding)
   - Even though servers connect and report tools, they are not accessible to agents
   - **Use `mcp_cursor-browser-extension_*` tools instead** - these are the only browser automation tools available in WSL

3. **If Issues Persist**:
   - Toggle browser extension MCP server off/on in Cursor Settings
   - Restart Cursor completely
   - Check MCP server logs for specific errors
   - Consider using Playwright MCP tools directly instead

<!-- section_id: "33c140f2-1f05-47cd-a7bd-5e494a6a2115" -->
### WSL-Specific Notes

- **X11 Forwarding**: Required for GUI applications in WSL. Verify with `echo $DISPLAY`
- **Path Format**: Use Windows paths (`C:\...`) for Cursor settings, Linux paths (`/opt/...`) for MCP env vars
- **Chrome Installation**: Chrome can exist in both WSL and Windows - use Windows path for Cursor
- **MCP Server Location**: MCP config is at `~/.config/mcp/mcp.json` (symlinked from `~/.cursor/mcp.json`)
- **Log Location**: Cursor server logs at `~/.cursor-server/data/logs/`

<!-- section_id: "c776b8b8-8059-4dc1-8141-8244093e6d76" -->
### Next Steps for WSL Users

1. ✅ Configure Cursor Settings with Windows Chrome path: `C:\Program Files\Google\Chrome\Application\chrome.exe`
2. ✅ Verify Chrome opens when settings are saved (indicates configuration is correct)
3. ⚠️ If MCP tools still don't work, use Playwright MCP as alternative
4. 🔄 Monitor Cursor updates for potential fixes to browser extension MCP server

<!-- section_id: "78871b20-0720-401a-848f-8223fe6b8dd2" -->
### Related WSL Documentation

- WSL Setup: `../../sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/setup/WSL_SETUP.md`
- Linux MCP Issues: `../../sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MCP_ISSUES.md`

---

<!-- section_id: "abf44868-df81-4fb6-9bca-59b08ba33d65" -->
## Verification

<!-- section_id: "7645a63f-3ef1-4be8-82e6-619057501d86" -->
### Check MCP Servers Running
```bash
ps aux | grep -E "playwright|mcp.*browser" | grep -v grep
```

<!-- section_id: "58305b54-db75-41cf-afaf-691b1da9608f" -->
### Check Browser Installation
```bash
# Chromium (Playwright)
ls -la ~/.cache/ms-playwright/chromium-1200/chrome-linux64/chrome

# Chrome (System)
which google-chrome && google-chrome --version
```

<!-- section_id: "67bd3291-0536-4933-b512-ac0561d2f81c" -->
### Check MCP Logs
```bash
LATEST_LOG=$(ls -t ~/.config/Cursor/logs/*/window*/exthost/anysphere.cursor-mcp/MCP\ cursor-browser-extension.log 2>/dev/null | head -1)
tail -20 "$LATEST_LOG"
```

<!-- section_id: "1f5ccfe4-c088-4f15-86ac-3667b10c2ef1" -->
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

<!-- section_id: "b16e83ff-be2c-404a-8f9b-43a60524e5f2" -->
## References

- [Cursor Browser Documentation](https://cursor.com/docs/agent/browser)
- [Playwright MCP Setup Guide](../setup/playwright-mcp-cursor-setup.md)
- [Browser Automation Framework](../browser-automation/README.md)
- [MCP Configuration Guide](./MCP_CONFIGURATION_GUIDE.md)

<!-- section_id: "8fc275e4-4885-4cd7-b844-ab17b7bcd7a4" -->
## Related Documentation

- Universal Browser Opening Rule: `layer_0/0.02_sub_layers/sub_layer_0_04_universal_rules/trickle_down_0_universal/0_instruction_docs/browser_opening_rule.md`
- Playwright MCP Usage: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/setup/playwright-mcp-usage.md`

<!-- section_id: "ae2c51ac-ac1b-49dd-8a56-f8e6114a2756" -->
## Setup Instructions

<!-- section_id: "fc1afc82-44e2-4064-9c3a-62aa81f87a9e" -->
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

<!-- section_id: "36fbc4b5-1965-4df4-886e-9c32d61a6d86" -->
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

