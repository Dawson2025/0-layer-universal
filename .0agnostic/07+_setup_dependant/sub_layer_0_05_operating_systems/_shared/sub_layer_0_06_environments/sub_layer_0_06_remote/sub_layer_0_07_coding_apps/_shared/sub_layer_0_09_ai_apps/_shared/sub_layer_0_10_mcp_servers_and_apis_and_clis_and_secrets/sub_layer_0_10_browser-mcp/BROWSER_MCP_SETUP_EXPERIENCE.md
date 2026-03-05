---
resource_id: "8a1c25d7-915a-48b5-854e-a8c4fbe70452"
resource_type: "document"
resource_name: "BROWSER_MCP_SETUP_EXPERIENCE"
---
# Browser MCP Setup Experience and Lessons Learned

**Date**: 2025-12-02  
**Location**: Universal Layer → MCP Servers and Tools Setup  
**Status**: Documenting ongoing experience and lessons learned

<!-- section_id: "de40782d-de92-4cd7-adcf-c186dc12adef" -->
## Executive Summary

This document captures our experience setting up and troubleshooting browser MCP servers in Cursor IDE on Linux/Ubuntu. It covers Playwright MCP, browser MCP (`@agent-infra/mcp-server-browser`), and Cursor's native browser automation (`cursor-browser-extension`).

<!-- section_id: "2e2a2fad-30e1-4878-bce6-e80ed6f91430" -->
## Current Status (2025-12-02)

<!-- section_id: "93def8b0-b8e9-430e-be15-e0885fb20324" -->
### MCP Servers Configured

**Location**: `~/.gemini/settings.json`

```json
{
  "ide": {
    "enabled": true
  },
  "auth": {
    "method": "apiKey",
    "apiKey": "YOUR_GEMINI_API_KEY_HERE"
  },
  "security": {
    "auth": {
      "selectedType": "gemini-api-key"
    }
  },
  "hasSeenIdeIntegrationNudge": true,
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "@playwright/mcp@latest",
        "--browser",
        "chromium",
        "--headless"
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

<!-- section_id: "5c6bc324-85e1-4e55-966c-ae397c0b19bb" -->
### Tool Availability

**Available Tools** (as of 2025-12-02):
- `mcp_browser_*` - 21 tools from `@agent-infra/mcp-server-browser`
- `mcp_cursor-browser-extension_*` - 18 tools from Cursor's browser extension MCP
- Playwright tools - 22 tools configured but naming convention unclear

**Tool Naming Convention**:
- Tools use single underscore: `mcp_browser_*` (not `mcp__browser__*`)
- Prefix matches the MCP server name in config
- Cursor's browser extension uses `mcp_cursor-browser-extension_*`

<!-- section_id: "afd05684-caf0-4220-a654-ff8f562f8923" -->
## Key Lessons Learned

<!-- section_id: "0b69e0ce-b4ee-423d-9ab3-4acef8e2275c" -->
### Lesson 1: Linux/Ubuntu Has Platform-Specific MCP Issues

**Critical Finding**: Linux/Ubuntu systems experience unique challenges with MCP servers in Cursor IDE that don't occur on Windows or macOS.

**Known Linux/Ubuntu Issues**:
1. **MCP Tool Exposure**: Tools may be registered with MCP servers but not exposed to AI agents
2. **Browser Path Detection**: Automatic browser detection fails, requires explicit paths
3. **Server Startup**: More prone to connection and initialization failures
4. **Environment Variables**: NVM and Node.js paths require explicit configuration
5. **Tool Naming**: May use different naming conventions than Windows/macOS

**Evidence**:
- Playwright MCP: Server connects, reports 22 tools, but tools not accessible
- Browser MCP: Tools accessible but browser detection fails
- Community reports: GitHub issues #942, #1113 document Ubuntu-specific problems

**Recommendation**: Always test MCP configurations on Linux separately from Windows/macOS documentation.

<!-- section_id: "d4a93c27-1b06-4a97-b697-fb0fccdc7940" -->
### Lesson 2: MCP Servers Need Environment Variables (Critical Fix - 2025-12-05)

**Problem**: Browser MCP servers on Linux (and all platforms) fail with "Browser specified in your config is not installed" even when browsers are installed. This problem keeps recurring because browsers appear to need constant reinstallation.

**Root Cause**: 
- MCP servers run via `npx` in isolated execution environments
- They don't inherit your shell's environment variables (like those in `.bashrc`)
- `PLAYWRIGHT_BROWSERS_PATH` isn't set, so servers can't find browsers in `~/.cache/ms-playwright/`
- Each Cursor restart spawns new MCP processes that need the environment configured
- This is NOT a Linux-specific issue - it affects all platforms

**Solution**:
- **Always set environment variables in MCP server configuration**:
  ```json
  {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp@latest", "--browser", "chromium"],
      "env": {
        "PLAYWRIGHT_BROWSERS_PATH": "/home/dawson/.cache/ms-playwright",
        "HOME": "/home/dawson"
      }
    },
    "browser": {
      "command": "npx",
      "args": ["@agent-infra/mcp-server-browser"],
      "env": {
        "PLAYWRIGHT_BROWSERS_PATH": "/home/dawson/.cache/ms-playwright",
        "HOME": "/home/dawson"
      }
    }
  }
  ```
- Replace `/home/dawson` with your actual home directory
- The browsers ARE installed - the MCP server just can't find them without the environment variable
- This fix prevents the constant "browser needs installation" problem

**Why This Keeps Happening**:
- `npx` creates isolated execution environments
- Environment variables from your shell aren't automatically passed to MCP servers
- The MCP server needs explicit configuration to find user-installed browsers
- Each time Cursor restarts, it spawns new MCP server processes that need the environment set

**Previous Approach (Less Reliable)**:
- Using `--executable-path` with explicit browser paths can work, but environment variables are more reliable
- The environment variable approach works for all Playwright-installed browsers automatically

<!-- section_id: "c4d9d857-a0d8-4ed7-8890-86aa2cf6a148" -->
### Lesson 3: Playwright MCP vs Browser MCP vs Cursor Browser Extension

**Three Different Browser Automation Options**:

1. **Playwright MCP** (`@playwright/mcp`)
   - **Pros**: Cross-browser support, comprehensive toolset (22 tools), well-maintained
   - **Cons**: Requires browser installation via `npx playwright install`
   - **Status**: Configured, tools available but may have naming issues
   - **Best For**: Cross-browser testing, comprehensive automation

2. **Browser MCP** (`@agent-infra/mcp-server-browser`)
   - **Pros**: Simpler setup, explicit path configuration, 21 tools
   - **Cons**: Less comprehensive than Playwright
   - **Status**: Configured with explicit path, tools available
   - **Best For**: Simple browser automation, when you need explicit control

3. **Cursor Browser Extension** (`cursor-browser-extension`)
   - **Pros**: Native Cursor integration, 18 tools
   - **Cons**: Requires Chrome extension, Linux-specific issues, "No server info found" errors
   - **Status**: Not working reliably on Linux
   - **Best For**: Cursor-specific workflows (when it works)

**Recommendation**: Use Playwright MCP or Browser MCP on Linux. Avoid `cursor-browser-extension` until Linux support improves.

<!-- section_id: "9f3b5a21-007c-49c3-87dd-faff13068760" -->
### Lesson 4: Tool Naming Conventions Are Inconsistent

**Observation**: Different MCP servers use different naming conventions:
- `mcp_browser_*` (single underscore, server name)
- `mcp_cursor-browser-extension_*` (single underscore, hyphenated server name)
- Playwright tools may use different naming (needs verification)

**Implication**: 
- Always check available tools after configuring an MCP server
- Don't assume naming conventions
- Use `list_mcp_resources` or check Cursor's MCP settings to see available tools

<!-- section_id: "62934fff-0406-4564-baec-5f87e0b2bec2" -->
### Lesson 4: "Browser Not Installed" Error Is Misleading

**Problem**: Error message "Browser specified in your config is not installed" appears even when:
- Browser is installed and executable
- Path is correct
- Browser runs manually

**Actual Causes**:
1. Path detection fails (Linux-specific)
2. Executable permissions issue
3. Browser version mismatch
4. MCP server can't find browser in PATH
5. Configuration syntax error

**Debugging Steps**:
1. Verify browser exists: `ls -la /path/to/browser`
2. Test browser manually: `/path/to/browser --version`
3. Check executable permissions: `chmod +x /path/to/browser`
4. Verify MCP config syntax: `cat ~/.cursor/mcp.json | jq`
5. Check MCP logs: `tail -f ~/.config/Cursor/logs/*/window*/exthost/anysphere.cursor-mcp/*.log`

<!-- section_id: "f86e7a03-f37b-42f0-b346-1dc54c36f793" -->
### Lesson 5: Cursor Browser Extension Requires Chrome Extension

**Discovery**: The `cursor-browser-extension` MCP server requires a Chrome extension to function, regardless of browser path configuration.

**Evidence**:
- Error: "No server info found" in logs
- Error: "Browser specified in your config is not installed"
- Works on systems with Cursor Chrome extension installed

**Workaround**:
- Use Playwright MCP or Browser MCP instead
- Install community-developed Cursor MCP extension (not officially supported)
- Wait for official Linux support

<!-- section_id: "e77f5067-bbae-4006-8844-8a499f44737d" -->
### Lesson 6: Multiple MCP Servers Can Coexist

**Finding**: Multiple browser MCP servers can be configured simultaneously:
- Playwright MCP
- Browser MCP
- Cursor browser extension

**Behavior**:
- Each provides its own set of tools
- Tools are namespaced by server name
- No conflicts observed
- Can use tools from any configured server

**Best Practice**: Configure the server(s) you need. Don't configure unused servers.

<!-- section_id: "637a9e6f-e725-4163-903f-d06c4228f714" -->
## Configuration Best Practices

<!-- section_id: "2cf0f924-30ce-4399-b4f1-fbd73acf401a" -->
### For Linux/Ubuntu

1. **Always Use Explicit Paths**:
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

2. **Install Playwright Browsers**:
   ```bash
   npx playwright install chromium
   ```

3. **Verify Browser Installation**:
   ```bash
   ls -la ~/.cache/ms-playwright/chromium-*/chrome-linux64/chrome
   ```

4. **Use Playwright or Browser MCP** (avoid cursor-browser-extension on Linux)

5. **Check Tool Availability**:
   - Restart Cursor after MCP config changes
   - Check Cursor Settings → Features → Model Context Protocol
   - Verify tools appear in available tools list

<!-- section_id: "a52a0023-a3ce-438f-9df3-36fb2dcd539e" -->
### For macOS/Windows

1. **May Work with Default Paths**:
   - Browser detection is more reliable
   - Can use "Default (Bundled Chrome)" option
   - Less need for explicit paths

2. **Still Recommended**:
   - Explicit paths for reliability
   - Playwright browser installation for consistency

<!-- section_id: "619b11b8-efff-44dc-b26f-5e2485011253" -->
## Troubleshooting Guide

<!-- section_id: "a8806cb9-43c7-4f35-b357-9ec82cf4141c" -->
### Issue: "Browser specified in your config is not installed" (FIXED - 2025-12-05)

**Root Cause**: MCP servers can't find browsers because `PLAYWRIGHT_BROWSERS_PATH` environment variable isn't set.

**Checklist**:
- [ ] Browser executable exists: `ls -la ~/.cache/ms-playwright/chromium-*/chrome-linux64/chrome`
- [ ] Browser is executable (`chmod +x /path/to/browser` if needed)
- [ ] Browser runs manually (`~/.cache/ms-playwright/chromium-*/chrome-linux64/chrome --version`)
- [ ] **MCP config has `PLAYWRIGHT_BROWSERS_PATH` environment variable set** (CRITICAL)
- [ ] **MCP config has `HOME` environment variable set** (CRITICAL)
- [ ] MCP config JSON is valid
- [ ] Cursor has been restarted after config change
- [ ] MCP server process is running (`ps aux | grep mcp`)

**Solutions** (In Order of Priority):
1. **Add environment variables to MCP config** (PRIMARY FIX):
   ```json
   {
     "playwright": {
       "command": "npx",
       "args": ["-y", "@playwright/mcp@latest", "--browser", "chromium"],
       "env": {
         "PLAYWRIGHT_BROWSERS_PATH": "/home/dawson/.cache/ms-playwright",
         "HOME": "/home/dawson"
       }
     }
   }
   ```
2. Verify browsers are installed: `npx playwright install chromium` (if needed)
3. Verify config: `cat ~/.cursor/mcp.json | jq`
4. Restart Cursor IDE
5. (Optional) Use explicit path as backup: `--executable-path /absolute/path/to/browser`

<!-- section_id: "f8e6c2b5-21f2-4e19-bb2f-e3a19f5297c0" -->
### Issue: "No server info found" (cursor-browser-extension)

**Cause**: Chrome extension not installed

**Solutions**:
1. Install Cursor Chrome extension (if available)
2. Use Playwright MCP or Browser MCP instead
3. Check if native browser automation works (separate from MCP)

<!-- section_id: "750c5e03-4e09-4012-bc0d-ed4ab28fd45c" -->
### Issue: Tools Not Available

**Checklist**:
- [ ] MCP server is configured in `~/.cursor/mcp.json`
- [ ] MCP server process is running
- [ ] Cursor has been restarted
- [ ] Check Cursor Settings → Features → Model Context Protocol
- [ ] Verify tool naming convention

**Solutions**:
1. Restart Cursor IDE
2. Check MCP server logs
3. Verify server name matches tool prefix
4. Try different MCP server (Playwright vs Browser vs Extension)

<!-- section_id: "0ffebaf4-32e8-44b6-a0fb-e650ad7683b5" -->
## Testing Results

<!-- section_id: "620a951d-5fb3-4335-a79a-facbbb65c7f1" -->
### Test 1: Browser MCP Navigation (2025-12-02)

**Command**: `mcp_browser_browser_navigate("https://example.com")`

**Result**: Error - "Browser specified in your config is not installed"

**Analysis**: 
- Browser executable exists at configured path
- Path is absolute and correct
- Browser runs manually
- Issue: MCP server may not be finding browser despite explicit path

**Status**: ⚠️ Needs further investigation

<!-- section_id: "436f0859-6e24-41d1-951f-e0d146c1528c" -->
### Test 2: Browser MCP Get Text (2025-12-02)

**Command**: `mcp_browser_browser_get_text()`

**Result**: Empty (no browser session active)

**Analysis**: Navigation failed, so no page to get text from

**Status**: ⚠️ Depends on navigation working

<!-- section_id: "4f9f4f54-60bc-4e0b-84a8-88e8bb6b41de" -->
### Test 3: Browser MCP Close (2025-12-02)

**Command**: `mcp_browser_browser_close()`

**Result**: Success - "No open tabs. Use the 'browser_navigate' tool to navigate to a page first."

**Analysis**: Tool works, but no browser session was active

**Status**: ✅ Tool is functional

<!-- section_id: "5740b0d4-b141-43ef-83f5-0b839089abfe" -->
### Test 4: Cursor Browser Extension Tools (2025-12-02)

**Commands Tested**:
- `mcp_cursor-browser-extension_browser_snapshot()`
- `mcp_cursor-browser-extension_browser_navigate()`
- `mcp_cursor-browser-extension_browser_tabs()`

**Result**: All tools return error - "Browser specified in your config is not installed"

**Analysis**:
- Same error as browser MCP tools
- Cursor browser extension MCP also requires browser to be properly configured
- Issue persists across all browser MCP servers

**Status**: ⚠️ All browser MCP tools currently non-functional on this Linux system

<!-- section_id: "09642d5e-f8dd-4a6d-b987-fd3effc9d13f" -->
### Test 5: Playwright MCP Configuration Fix (2025-12-02)

**Issue**: Playwright MCP server may not have access to Node.js/npx if NVM is not loaded in the MCP process environment.

**Root Cause**: 
- Cursor's MCP process may not inherit NVM environment variables
- `npx` command may not be in PATH when MCP server starts
- Node.js may not be accessible without loading NVM first

**Fix Applied**: The issue was resolved by ensuring the `settings.json` file was correctly structured in `~/.gemini/settings.json` and contained the `mcpServers` configuration with the `command` set to `"npx"` and the appropriate arguments directly for `@playwright/mcp@latest`. The previous attempt to use a `bash` wrapper to load NVM was found to be unnecessary.

**Key Changes**:
1. Changed `command` to `"npx"`.
2. Ensured `--browser chromium` and `--headless` were included in the `args` array.
3. Confirmed `~/.gemini/settings.json` contained both the MCP server configuration and other essential Gemini CLI settings (e.g., API key, IDE settings).

**Status**: ✅ Configuration fix successful - Playwright MCP server connects after restart.

**Test Results After Restart (2025-12-02)**:
- ✅ Playwright MCP server starts successfully with bash wrapper
- ✅ Server connects: "Successfully connected to stdio server"
- ✅ Server reports: "Found 22 tools, 0 prompts, and 0 resources"
- ⚠️ **Issue**: Tools are NOT accessible to AI agent with `mcp_playwright_*` prefix
- ⚠️ **Available tools**: Only `mcp_browser_*` (21 tools) and `mcp_cursor-browser-extension_*` (18 tools) are accessible

**Root Cause**: Playwright MCP tools are registered with the server but Cursor IDE is not exposing them to the AI agent. This appears to be a **Linux/Ubuntu-specific issue** with Cursor IDE's MCP tool exposure mechanism.

**Linux/Ubuntu-Specific Issues Confirmed**:
- Browser initialization failures on Ubuntu (GitHub issues #942, #1113)
- Server startup and connection problems on Linux
- Tool execution errors in Linux environments
- MCP tool exposure may work differently on Linux vs Windows/macOS

**Workaround**: Use `mcp_browser_*` tools from `@agent-infra/mcp-server-browser` server, which are accessible and functional.

<!-- section_id: "b3282ac5-727a-4c86-ab0d-6f1f822a3849" -->
### Test 6: Precalc Work Attempt (2025-12-02)

**Context**: Attempted to continue precalc ALEKS work in browser

**Commands Tested**:
- `mcp_browser_browser_navigate("https://byui.instructure.com/courses/353368/external_tools/20009")` - Failed
- `mcp_cursor-browser-extension_browser_snapshot()` - Failed
- `mcp_cursor-browser-extension_browser_navigate()` - Failed

**System State**:
- Firefox browser process running (user may have opened manually)
- Chromium installed at configured path: `/home/dawson/.cache/ms-playwright/chromium-1200/chrome-linux64/chrome`
- All MCP browser tools returning "Browser not installed" error
- Browser tab list showed Google search page, but tools cannot interact with it

**Impact**: Cannot automate browser for precalc ALEKS work until MCP browser tools are fixed

**Blocking Issue**: Browser MCP servers cannot find/connect to browser despite:
- Browser executable existing at configured path
- Browser being executable and runnable manually
- Explicit path configuration in MCP config

**Next Steps Needed**:
1. Fix browser MCP configuration to resolve "Browser not installed" error
2. Test navigation to Canvas ALEKS URL: `https://byui.instructure.com/courses/353368/external_tools/20009`
3. Resume precalc problem-solving workflow once browser automation works

<!-- section_id: "cd4ae62e-1b6d-4705-8aa8-12626a6b5b90" -->
## Recommendations

<!-- section_id: "cbc8c91c-3f4b-4e22-ad9f-ffac3e7487fd" -->
### For New Setups

1. **Start with Playwright MCP**:
   - Most reliable on Linux
   - Comprehensive toolset
   - Well-documented
   - Cross-browser support

2. **Configure Explicit Paths**:
   - Always use `--executable-path` on Linux
   - Verify browser installation
   - Test browser manually first

3. **Avoid cursor-browser-extension on Linux**:
   - Use Playwright or Browser MCP instead
   - Wait for official Linux support

<!-- section_id: "2a4bd4ca-9b68-4d96-95ae-a5ad40a30ee3" -->
### For Existing Setups

1. **Verify Current Configuration**:
   - Check `~/.cursor/mcp.json`
   - Verify browser paths
   - Test tools availability

2. **Update if Needed**:
   - Add explicit paths if missing
   - Install Playwright browsers if needed
   - Restart Cursor after changes

3. **Document Your Setup**:
   - Record working configurations
   - Note any platform-specific issues
   - Share solutions with team

<!-- section_id: "993f8049-fffa-4746-96f8-5d5b16de3018" -->
## Future Work

<!-- section_id: "acf3201d-3ca9-448b-8c51-852659f7cb64" -->
### Areas Needing Investigation

1. **Playwright Tool Naming**:
   - Verify exact tool names for Playwright MCP
   - Test if tools work despite naming differences
   - Document correct usage

2. **Linux Path Detection**:
   - Investigate why explicit paths sometimes fail
   - Test different path formats
   - Document working configurations

3. **Cursor Browser Extension**:
   - Test with Chrome extension installed
   - Verify if it works on Linux with extension
   - Document extension installation process

4. **Multiple Browser Support**:
   - Test using multiple browsers (Chrome, Firefox, Safari)
   - Document browser-specific configurations
   - Test cross-browser compatibility

<!-- section_id: "6a13f03d-e434-4c76-9924-75b5029f23d7" -->
## Related Documentation

- [Cursor Browser MCP Setup](CURSOR_BROWSER_MCP_SETUP.md) - Detailed setup guide
- [Playwright MCP Testing](PLAYWRIGHT_MCP_TESTING.md) - Testing documentation
- [MCP Configuration Guide](MCP_CONFIGURATION_GUIDE.md) - General MCP configuration
- [MCP System Guide](MCP_SYSTEM_GUIDE.md) - Complete MCP management system

<!-- section_id: "8935badd-4ae6-4b49-99c0-c10ec431a02e" -->
## Changelog

<!-- section_id: "c65ebeb2-3795-40bb-84b7-cb6f206b2d83" -->
### 2025-12-02
- Initial documentation of browser MCP setup experience
- Documented Linux/Ubuntu-specific issues
- Recorded lessons learned from troubleshooting
- Added configuration best practices
- Created troubleshooting guide

---

**This document is a living record of our experience with browser MCP servers. Update it as we learn more and resolve issues.**

