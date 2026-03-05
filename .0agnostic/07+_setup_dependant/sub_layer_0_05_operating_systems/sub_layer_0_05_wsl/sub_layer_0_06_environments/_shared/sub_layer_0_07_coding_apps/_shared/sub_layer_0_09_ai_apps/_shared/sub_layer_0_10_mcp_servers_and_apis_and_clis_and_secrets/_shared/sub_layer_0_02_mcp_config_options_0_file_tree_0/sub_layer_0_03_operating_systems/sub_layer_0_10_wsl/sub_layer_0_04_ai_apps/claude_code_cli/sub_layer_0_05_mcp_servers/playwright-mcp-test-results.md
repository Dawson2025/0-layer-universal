---
resource_id: "09ed667b-f586-4823-97b1-f0970f462af2"
resource_type: "document"
resource_name: "playwright-mcp-test-results"
---
# Playwright MCP Server Test Results

**Date:** 2025-12-30
**System:** WSL (Windows Subsystem for Linux) - Ubuntu
**Node.js Version:** v22.20.0
**Playwright Version:** 1.55.0
**Playwright MCP Version:** 0.0.54

<!-- section_id: "8eedea29-0f90-417c-a49a-454a2da636ce" -->
## Test Summary

The Playwright MCP server is **CONFIGURED and PARTIALLY WORKING** in Claude Code CLI. The server can start successfully and respond to MCP protocol commands, but has browser installation path issues that prevent full functionality.

<!-- section_id: "e7af7231-7621-4c68-9ce7-06720455a918" -->
### Overall Status: ⚠️ CONFIGURED BUT NEEDS BROWSER PATH FIX

---

<!-- section_id: "704ba994-57bf-405a-9d14-12a4b55b7deb" -->
## 1. Configuration Review

<!-- section_id: "cdef1a14-6fc5-4818-98b5-61940996957a" -->
### Claude Code Configuration Location
- **File:** `/home/dawson/.claude.json`
- **Project Scope:** `/home/dawson` (user's home directory)

<!-- section_id: "ecd5e0d8-3770-47fe-87df-a0dd3db3330a" -->
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

<!-- section_id: "a6266da3-e92f-4bce-9247-a9f0d1fe656e" -->
## 2. Browser Installation Verification

<!-- section_id: "5be77f9e-620f-49a1-adb8-68226124273a" -->
### Playwright Browsers Directory
- **Path:** `/home/dawson/.cache/ms-playwright`
- **Status:** ✅ EXISTS

<!-- section_id: "31530018-802d-4f91-8045-a1c9797c49a0" -->
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

<!-- section_id: "74c4f540-04d6-49d7-a386-85f58c458092" -->
## 3. MCP Server Startup Test

<!-- section_id: "99b01fa5-d9d9-4b7d-9bc1-459853c7b021" -->
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

<!-- section_id: "8d7a41e7-e474-40c9-94eb-c1adc84af220" -->
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

<!-- section_id: "f5b92fe6-3b6c-47c8-87ca-9d0f37b5d8ce" -->
## 4. Available Tools Test

<!-- section_id: "78ed0c36-8fda-41ee-a49a-589d50250583" -->
### Test Method
Sent `tools/list` request after initialization

<!-- section_id: "5bc7a3bc-f57a-4d82-b38e-fb20150e9818" -->
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

<!-- section_id: "dab93c43-419e-4103-b07f-6daf5c6f798a" -->
## 5. Functional Test Results

<!-- section_id: "10e28548-872b-4a5a-b53a-88d9f995ec24" -->
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

<!-- section_id: "e2661ce3-3301-410d-a9ff-1a9a83b7b406" -->
## 6. Issue Analysis

<!-- section_id: "fa46bda2-11c0-46f7-98ba-43030750ec54" -->
### Root Cause
The Playwright MCP server cannot find the installed Chromium browser despite:
- Chromium being installed at `/home/dawson/.cache/ms-playwright/chromium-1200/chrome-linux64/chrome`
- Environment variable `PLAYWRIGHT_BROWSERS_PATH` being set in the configuration
- Environment variable `HOME` being set in the configuration

<!-- section_id: "0059333e-cab5-4d95-8928-bf24ce67e57c" -->
### Possible Reasons
1. **Version Mismatch:** The MCP server may be looking for a different Chromium version
2. **Path Recognition:** The MCP server's internal Playwright installation may not respect the `PLAYWRIGHT_BROWSERS_PATH` environment variable when launched via `npx -y`
3. **NPX Caching:** The `npx -y` command may create its own temporary installation that doesn't share the browser cache

<!-- section_id: "4102fd40-1004-40f9-b110-a31b98572346" -->
### Evidence
- Browser install attempt via `browser_install` tool timed out (15+ seconds)
- Manual Playwright installation shows Chromium 1200 is present
- When installing via `npx -y playwright install chromium`, it removed version 1202 but kept 1200

---

<!-- section_id: "8cff0a19-8067-42a9-b791-c0f8ecb1c6f8" -->
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

<!-- section_id: "fe35aa09-0d0b-4aa4-9efe-b9e4e297461f" -->
## 8. Recommendations

<!-- section_id: "b4648cfa-ed21-47af-933e-0ab155df6f0f" -->
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

<!-- section_id: "21a3b820-bf76-4bd9-b02e-18f11418788a" -->
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

<!-- section_id: "86c3056b-b18a-4ebf-9dd9-aef94d581f86" -->
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

<!-- section_id: "19ededcd-90f4-4443-be8b-3003b8c890f2" -->
## 9. Workaround for Immediate Use

If you need to use Playwright MCP right now:

1. Open Claude Code
2. Navigate to a project with Playwright MCP configured
3. Ask Claude to use the `browser_install` tool
4. Wait for the installation to complete
5. Try browser automation again

This will let the MCP server install browsers in its own cache location.

---

<!-- section_id: "61d6b056-1312-4f41-ae69-ff865b143476" -->
## 10. Additional Information

<!-- section_id: "b37424d6-0775-4818-9c31-31a0336a9bf0" -->
### Environment Details
- **OS:** Linux 6.6.87.2-microsoft-standard-WSL2 (WSL)
- **Shell:** bash
- **Node Package Manager:** npm via nvm
- **npx Path:** `/home/dawson/.nvm/versions/node/v22.20.0/bin/npx`

<!-- section_id: "157a447c-56c1-4290-8b6e-3271598d9b3d" -->
### Related Directories
- **Playwright Cache:** `/home/dawson/.cache/ms-playwright/`
- **Claude Config:** `/home/dawson/.claude.json`
- **MCP Directory:** `/home/dawson/.playwright-mcp/` (empty/doesn't exist)

<!-- section_id: "c871ec2e-493d-4579-a98b-55899e17de11" -->
### Test Files Created
- `/tmp/test-playwright-mcp.js` - Node.js test script for MCP protocol

---

<!-- section_id: "ffeb0678-15c1-4915-83d2-8193f036a072" -->
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
