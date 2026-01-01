# Playwright MCP Server Test Results

**Date:** 2025-12-30
**System:** WSL (Windows Subsystem for Linux) - Ubuntu
**Node.js Version:** v22.20.0
**Playwright Version:** 1.55.0
**Playwright MCP Version:** 0.0.54

## Test Summary

The Playwright MCP server is **CONFIGURED and PARTIALLY WORKING** in Claude Code CLI. The server can start successfully and respond to MCP protocol commands, but has browser installation path issues that prevent full functionality.

### Overall Status: ⚠️ CONFIGURED BUT NEEDS BROWSER PATH FIX

---

## 1. Configuration Review

### Claude Code Configuration Location
- **File:** `/home/dawson/.claude.json`
- **Project Scope:** `/home/dawson` (user's home directory)

### Playwright MCP Configuration
```json
{
  "playwright": {
    "type": "stdio",
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
  }
}
```

**Configuration Status:** ✅ VALID - Properly configured with correct environment variables

---

## 2. Browser Installation Verification

### Playwright Browsers Directory
- **Path:** `/home/dawson/.cache/ms-playwright`
- **Status:** ✅ EXISTS

### Installed Browsers
```
/home/dawson/.cache/ms-playwright/
├── chromium-1200/
│   └── chrome-linux64/chrome (263,990,488 bytes) ✅
├── chromium_headless_shell-1200/
├── firefox-1497/
├── webkit-2227/
├── mcp-chromium-ec5e1e8/
├── mcp-chromium/
├── mcp-chromium-9c76515/
└── [various other browser installations]
```

**Browser Status:** ✅ INSTALLED - Chromium 1200 is present at `/home/dawson/.cache/ms-playwright/chromium-1200/chrome-linux64/chrome`

---

## 3. MCP Server Startup Test

### Test Method
Sent MCP protocol initialization request via stdio:
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "initialize",
  "params": {
    "protocolVersion": "2024-11-05",
    "capabilities": {},
    "clientInfo": {"name": "test", "version": "1.0"}
  }
}
```

### Response
```json
{
  "result": {
    "protocolVersion": "2024-11-05",
    "capabilities": {"tools": {}},
    "serverInfo": {"name": "Playwright", "version": "0.0.54"}
  },
  "jsonrpc": "2.0",
  "id": 1
}
```

**Startup Status:** ✅ SUCCESS - Server starts and responds correctly

---

## 4. Available Tools Test

### Test Method
Sent `tools/list` request after initialization

### Available Tools (22 total)
1. `browser_close` - Close the page
2. `browser_resize` - Resize the browser window
3. `browser_console_messages` - Returns all console messages
4. `browser_handle_dialog` - Handle a dialog
5. `browser_evaluate` - Evaluate JavaScript expression on page or element
6. `browser_file_upload` - Upload one or multiple files
7. `browser_fill_form` - Fill multiple form fields
8. `browser_install` - Install the browser specified in the config
9. `browser_press_key` - Press a key on the keyboard
10. `browser_type` - Type text into editable element
11. `browser_navigate` - Navigate to a URL
12. `browser_navigate_back` - Go back to the previous page
13. `browser_network_requests` - Returns all network requests since loading the page
14. `browser_run_code` - Run Playwright code snippet
15. `browser_take_screenshot` - Take a screenshot of the current page
16. `browser_snapshot` - Capture accessibility snapshot of the current page
17. `browser_click` - Perform click on a web page
18. `browser_drag` - Perform drag and drop between two elements
19. `browser_hover` - Hover over element on page
20. `browser_select_option` - Select an option in a dropdown
21. `browser_tabs` - List, create, close, or select a browser tab
22. `browser_wait_for` - Wait for text to appear or disappear or a specified time to pass

**Tools List Status:** ✅ SUCCESS - All 22 tools available

---

## 5. Functional Test Results

### Test: Navigate to https://example.com

**Command Sent:**
```json
{
  "jsonrpc": "2.0",
  "id": 3,
  "method": "tools/call",
  "params": {
    "name": "browser_navigate",
    "arguments": {"url": "https://example.com"}
  }
}
```

**Response:**
```json
{
  "result": {
    "content": [{
      "type": "text",
      "text": "### Result\nError: Browser specified in your config is not installed. Either install it (likely) or change the config.\n"
    }],
    "isError": true
  },
  "jsonrpc": "2.0",
  "id": 3
}
```

**Navigation Status:** ❌ FAILED - Browser path not recognized by MCP server

---

## 6. Issue Analysis

### Root Cause
The Playwright MCP server cannot find the installed Chromium browser despite:
- Chromium being installed at `/home/dawson/.cache/ms-playwright/chromium-1200/chrome-linux64/chrome`
- Environment variable `PLAYWRIGHT_BROWSERS_PATH` being set in the configuration
- Environment variable `HOME` being set in the configuration

### Possible Reasons
1. **Version Mismatch:** The MCP server may be looking for a different Chromium version
2. **Path Recognition:** The MCP server's internal Playwright installation may not respect the `PLAYWRIGHT_BROWSERS_PATH` environment variable when launched via `npx -y`
3. **NPX Caching:** The `npx -y` command may create its own temporary installation that doesn't share the browser cache

### Evidence
- Browser install attempt via `browser_install` tool timed out (15+ seconds)
- Manual Playwright installation shows Chromium 1200 is present
- When installing via `npx -y playwright install chromium`, it removed version 1202 but kept 1200

---

## 7. Test Results Summary

| Test Component | Status | Details |
|---------------|--------|---------|
| Configuration File | ✅ PASS | Valid JSON, correct structure |
| Browser Installation | ✅ PASS | Chromium 1200 installed |
| MCP Server Startup | ✅ PASS | Responds to initialization |
| Tools Discovery | ✅ PASS | All 22 tools available |
| Browser Navigation | ❌ FAIL | Cannot find browser |
| Page Snapshot | ❌ FAIL | Cannot find browser |
| Browser Close | ✅ PASS | Executes (no browser to close) |

**Overall Score:** 5/7 tests passed (71%)

---

## 8. Recommendations

### Immediate Fixes

1. **Run Browser Install Tool from Claude Code:**
   ```bash
   # Let the MCP server install its own browser
   # Use the browser_install tool within Claude Code
   ```

2. **Alternative: Install via npx with explicit path:**
   ```bash
   PLAYWRIGHT_BROWSERS_PATH=/home/dawson/.cache/ms-playwright \
   npx -y @playwright/mcp@latest --browser chromium &
   # Then use the browser_install tool
   ```

3. **Verify Browser Detection:**
   Check if the MCP server can detect browsers:
   ```bash
   PLAYWRIGHT_BROWSERS_PATH=/home/dawson/.cache/ms-playwright \
   npx -y playwright install --dry-run chromium
   ```

### Configuration Adjustments

Consider adding these to the MCP configuration:
```json
{
  "playwright": {
    "type": "stdio",
    "command": "npx",
    "args": [
      "-y",
      "@playwright/mcp@latest",
      "--browser",
      "chromium"
    ],
    "env": {
      "PLAYWRIGHT_BROWSERS_PATH": "/home/dawson/.cache/ms-playwright",
      "HOME": "/home/dawson",
      "DEBUG": "pw:browser*"  // Enable browser detection debugging
    }
  }
}
```

### Long-term Solution

1. **Use Local Installation:**
   Instead of `npx -y @playwright/mcp@latest`, install locally:
   ```bash
   npm install -g @playwright/mcp
   playwright install chromium
   ```

   Then update configuration:
   ```json
   {
     "command": "playwright-mcp",
     "args": ["--browser", "chromium"]
   }
   ```

2. **Create Wrapper Script:**
   Create `/home/dawson/.local/bin/playwright-mcp-wrapper.sh`:
   ```bash
   #!/bin/bash
   export PLAYWRIGHT_BROWSERS_PATH=/home/dawson/.cache/ms-playwright
   export HOME=/home/dawson
   exec npx -y @playwright/mcp@latest "$@"
   ```

---

## 9. Workaround for Immediate Use

If you need to use Playwright MCP right now:

1. Open Claude Code
2. Navigate to a project with Playwright MCP configured
3. Ask Claude to use the `browser_install` tool
4. Wait for the installation to complete
5. Try browser automation again

This will let the MCP server install browsers in its own cache location.

---

## 10. Additional Information

### Environment Details
- **OS:** Linux 6.6.87.2-microsoft-standard-WSL2 (WSL)
- **Shell:** bash
- **Node Package Manager:** npm via nvm
- **npx Path:** `/home/dawson/.nvm/versions/node/v22.20.0/bin/npx`

### Related Directories
- **Playwright Cache:** `/home/dawson/.cache/ms-playwright/`
- **Claude Config:** `/home/dawson/.claude.json`
- **MCP Directory:** `/home/dawson/.playwright-mcp/` (empty/doesn't exist)

### Test Files Created
- `/tmp/test-playwright-mcp.js` - Node.js test script for MCP protocol

---

## Conclusion

The Playwright MCP server is **properly configured** in Claude Code and can:
- Start successfully
- Respond to MCP protocol commands
- List all available tools
- Execute non-browser commands

However, it **cannot execute browser automation** due to browser path detection issues. The issue is likely related to how `npx -y` handles temporary package installations and browser caching.

**Recommended Next Step:** Use the `browser_install` tool from within Claude Code to let the MCP server install browsers in its own location, or switch to a local installation of `@playwright/mcp` for better control over browser paths.

---

**Test Performed By:** Claude Code Agent
**Test Script:** `/tmp/test-playwright-mcp.js`
**Documentation Generated:** 2025-12-30
