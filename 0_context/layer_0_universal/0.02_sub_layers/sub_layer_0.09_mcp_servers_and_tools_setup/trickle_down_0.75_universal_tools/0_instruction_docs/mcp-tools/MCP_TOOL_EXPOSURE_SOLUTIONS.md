# MCP Tool Exposure Solutions and Workarounds

**Date**: 2025-12-05  
**Location**: Universal Layer → MCP Servers and Tools Setup  
**Status**: Comprehensive solutions guide

## Overview

This document provides solutions and workarounds for the Cursor IDE MCP tool exposure issue, where MCP tools are registered but not exposed to AI agents.

## Quick Reference: Most Promising Solutions

**CRITICAL: Ensure You're Logged In** (Solution 22):
- **Login to Cursor IDE** - This may be required for MCP tool exposure!
- After login, Playwright MCP tools became available (`mcp_playwright_*`)
- This was the breakthrough that made tools accessible

**Try These First** (in order):
1. **Ensure You're Logged Into Cursor IDE** (Solution 22) - ✅ **BREAKTHROUGH DISCOVERY**
2. **Delete and Regenerate mcp.json** (Solution 8) - ✅ User-reported success
3. **Use Playwright Browser Install Tool** (Solution 23) - If tools available but browser not found
4. **Disable Internal Browser Automation** (Solution 9) - Prevents interference
5. **Use Cursor CLI** (Solution 1) - May bypass IDE bug entirely
6. **Reorder MCP Servers** (Solution 10) - Move problematic server to top
7. **Check for Duplicates** (Solution 12) - Remove duplicate entries

**If Above Don't Work**:
- Use Cursor Browser Extension tools (Solution 3) - These work
- Try project-specific `.cursor/mcp.json` (Solution 11)
- Update Cursor to latest version (Solution 2)
- Check all diagnostic solutions (Solutions 6, 7, 15-21)

## Confirmed: This is a Cursor IDE Bug

**Root Cause**: Cursor IDE bug (specifically version 2.0.77 has a known issue) where MCP tools aren't exposed to agents even though they appear connected.

**Affected Platforms**: Linux, WSL, Windows, and potentially macOS

**Evidence**: Internet research shows this is a cross-platform Cursor IDE bug, not OS-specific.

## Solutions and Workarounds

### Solution 1: Use Cursor CLI (Recommended Workaround)

**Status**: ✅ **Potential Workaround** - CLI may not have the same bug

**Why This Might Work**:
- Cursor CLI uses the same MCP configuration as the IDE
- CLI may have different tool exposure mechanism
- Some users report better MCP tool access via CLI

**Installation**:
```bash
curl https://cursor.com/install -fsS | bash
```

**Usage**:
```bash
# Interactive mode
cursor-agent

# Non-interactive mode
cursor-agent -p "Your prompt here"

# List MCP servers
cursor-agent mcp list

# List tools from specific server
cursor-agent mcp list-tools playwright
cursor-agent mcp list-tools browser
```

**Key Features**:
- Uses same `~/.cursor/mcp.json` configuration
- Automatically discovers and uses MCP tools when relevant
- Supports same rules system as IDE
- Can be used in scripts and automation

**Testing Needed**:
- [ ] Verify if CLI exposes Playwright MCP tools
- [ ] Verify if CLI exposes Browser MCP tools
- [ ] Compare CLI tool exposure vs. IDE tool exposure
- [ ] Test if CLI works around the IDE bug

**References**:
- [Cursor CLI Documentation](https://cursor.com/docs/cli)
- [Cursor CLI MCP Guide](https://cursor.com/docs/cli/mcp)

### Solution 2: Update Cursor IDE

**Status**: ⚠️ **May Fix Issue** - If newer version fixes the bug

**Action**:
1. Check current Cursor version: `cursor --version`
2. Update to latest version if available
3. Check release notes for MCP tool exposure fixes
4. Test if tools are now exposed

**Known Bug Version**: 2.0.77 has confirmed bug

**Current Version**: Check with `cursor --version` (you have 2.1.49)

**Note**: If you're on 2.1.49, the bug may still exist or may have been partially fixed.

### Solution 3: Use Cursor Browser Extension Tools

**Status**: ✅ **Works** - These tools are available

**Available Tools**: `mcp_cursor-browser-extension_*` (18 tools)

**Configuration**:
1. Go to Cursor Settings → Tools & MCP → Browser Automation
2. Set Chrome Executable Path:
   - **WSL**: `C:\Program Files\Google\Chrome\Application\chrome.exe`
   - **Native Linux**: `/usr/bin/google-chrome` or Playwright Chromium path
3. Verify "Ready (Chrome detected)" status

**Limitations**:
- Only browser automation tools available
- May have browser detection issues
- Not as comprehensive as Playwright MCP tools

### Solution 4: Change HTTP Compatibility Mode (For HTTP Remote MCP Servers)

**Status**: ⚠️ **For HTTP Servers Only**

**Action**:
1. Go to Cursor Settings → Tools & MCP
2. Change HTTP Compatibility Mode
3. Restart Cursor

**Note**: This only helps if you're using HTTP remote MCP servers, not local stdio servers like Playwright.

### Solution 5: Use Full Path to Node.js in MCP Config

**Status**: ⚠️ **May Help** - Some users report this fixes issues

**Action**: Update MCP config to use full path to Node.js:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "/home/dawson/.nvm/versions/node/v22.20.0/bin/node",
      "args": [
        "/home/dawson/.nvm/versions/node/v22.20.0/bin/npx",
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
}
```

**Or use full path to npx**:
```json
{
  "mcpServers": {
    "playwright": {
      "command": "/home/dawson/.nvm/versions/node/v22.20.0/bin/npx",
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
}
```

### Solution 6: Restart Cursor Completely

**Status**: ⚠️ **Basic Troubleshooting**

**Action**:
1. Close all Cursor windows
2. Ensure all Cursor processes are terminated: `ps aux | grep cursor`
3. Kill any remaining processes if needed
4. Restart Cursor IDE
5. Check if tools are now exposed

**Note**: This is basic troubleshooting but sometimes helps.

### Solution 7: Check Cursor Settings for Tool Availability

**Status**: ⚠️ **Diagnostic**

**Action**:
1. Go to Cursor Settings → Tools & MCP
2. Check "Installed MCP Servers" section
3. Verify which tools are listed
4. Compare what's listed vs. what's accessible to agents

**Note**: Tools may show as "22 tools" but not be accessible to agents - this confirms the bug.

### Solution 8: Delete and Regenerate mcp.json

**Status**: ✅ **Reported Success** - User reported this fixed the issue

**Action**:
1. Backup your current `~/.cursor/mcp.json` file
2. Delete the `~/.cursor/mcp.json` file
3. Let Cursor regenerate it automatically
4. Re-add your MCP server configurations
5. Restart Cursor

**Source**: Reddit user reported: "I just deleted my mcp.json file and had Cursor regenerate it, and it completely fixed the issue"

**Note**: This may reset all MCP configurations, so backup first.

### Solution 9: Disable Cursor's Internal Browser Automation

**Status**: ⚠️ **May Help** - Prevents interference with MCP browser tools

**Problem**: Cursor's internal browser automation can interfere with MCP browser tools (Playwright, Chrome DevTools). When you mention "browser" in prompts, Cursor automatically enables its internal browser tools, which can disable MCP tools.

**Action**:
1. Go to Cursor Settings → Tools & MCP → Browser Automation
2. Disable the browser extension/automation if possible
3. **Note**: There's no global disable setting currently (feature request)
4. Try to avoid using the word "browser" in prompts if using MCP browser tools

**Workaround**: Click the browser icon in chat and disable it manually when it auto-enables.

**References**:
- Forum: "Browser Automation interferes with other MCP tools"
- Forum: "Ability to disable Browser Automation has been removed"

### Solution 10: Reorder MCP Servers in mcp.json

**Status**: ⚠️ **May Help** - Order can matter

**Action**: Move the problematic MCP server configuration to the **head/top** of the `mcpServers` object in `mcp.json`:

```json
{
  "mcpServers": {
    "playwright": {
      // Move this to the top
    },
    "other-server": {
      // Other servers below
    }
  }
}
```

**Source**: User reported: "As a last try, I moved the Figma config to the head of the mcp.json, and suddenly it worked"

### Solution 11: Use Project-Specific mcp.json

**Status**: ✅ **Recommended for CLI** - CLI requires project-specific config

**Action**: Create a `.cursor/mcp.json` file in your project directory instead of using the global `~/.cursor/mcp.json`:

```bash
# In your project root
mkdir -p .cursor
cp ~/.cursor/mcp.json .cursor/mcp.json
# Or create new project-specific config
```

**Why**: Cursor Agent CLI relies on project-specific MCP configurations. Some users report better tool exposure with project-specific configs.

**Note**: You may need both global and project-specific configs depending on your workflow.

### Solution 12: Check for Duplicate MCP Server Entries

**Status**: ⚠️ **Common Issue** - Duplicates can cause problems

**Action**:
1. Open `~/.cursor/mcp.json`
2. Check for duplicate server names or entries
3. Ensure each MCP server is described in only one place
4. Remove any duplicates
5. Restart Cursor

**Source**: Forum post: "Make sure 'hf-mcp-server' is described in only one place. Either remove the duplicate or rename"

### Solution 13: Manually Add Tools to Allowlist

**Status**: ⚠️ **Workaround** - May help with tool approval issues

**Action**:
1. When MCP tool is called, click "Add to Allowlist" button
2. Manually edit allowlist if needed (though editing may not work - known bug)
3. Check Cursor Settings → Tools & MCP for allowlist settings

**Note**: MCP allowlist functionality has bugs - may not work as expected.

**References**:
- Forum: "MCP Allowlist doesn't work, also can't be edited"
- Forum: "How to allow MCP to execute automatically in cursor"

### Solution 14: Use MCP Server Refresh Extension

**Status**: ⚠️ **Community Solution** - For stuck MCP servers

**Action**: Install community extension "MCP Server Refresh" to fix stuck MCP servers that show "Loading Tools..." indefinitely.

**Problem**: MCP servers can randomly stop responding and get stuck on "Loading Tools..." requiring full Cursor restart.

**Source**: Forum: "Community Extension MCP Server Refresh - Fix for Stuck MCP Servers"

### Solution 15: Check for Module Resolution Errors

**Status**: ⚠️ **Diagnostic** - May reveal underlying issues

**Action**:
1. Check Cursor MCP logs for errors
2. Look for `ERR_MODULE_NOT_FOUND` errors
3. Check for puppeteer-core or other dependency issues
4. Verify Node.js version compatibility
5. Try reinstalling MCP server dependencies

**Common Issues**:
- `puppeteer-core` module not found (chrome-devtools-mcp)
- ESM module resolution errors
- Node.js version incompatibility

**Source**: GitHub issue: "Cursor detects the MCP as 'no tools, prompts or resources'" - module resolution errors

### Solution 16: Verify MCP Tool Protection Settings

**Status**: ⚠️ **Security Setting** - May block tools

**Action**:
1. Go to Cursor Settings → Security or Tools & MCP
2. Check "MCP Tool Protection" settings
3. Ensure tools aren't being blocked by security settings
4. Adjust allowlist/blocklist if needed

**Note**: Security settings may prevent MCP tools from running even if exposed.

### Solution 17: Check AutoApprove Settings

**Status**: ⚠️ **Configuration** - May affect tool execution

**Action**: Verify `autoApprove` setting in MCP config:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp@latest"],
      "autoApprove": true
    }
  }
}
```

**Note**: `autoApprove: true` may not be respected (known bug), but worth trying.

**References**:
- Forum: "Atlassian MCP autoApprove: true Not Being Respected"
- Forum: "Run Everything does not work with MCP calls"

### Solution 18: Use Community Extension for MCP Refresh

**Status**: ⚠️ **Community Solution**

**Action**: Install community extension that provides MCP server refresh functionality to avoid full Cursor restarts.

**Benefits**: Can refresh MCP servers without restarting entire Cursor IDE.

### Solution 19: Check for Stuck "Loading Tools" Status

**Status**: ⚠️ **Diagnostic** - Indicates server connection issue

**Action**:
1. Check Cursor Settings → Tools & MCP
2. Look for servers stuck on "Loading tools..."
3. Try toggling server off/on
4. Use refresh button if available (may require extension)
5. Check MCP logs for connection errors
6. Restart Cursor if needed

**Source**: Forum: "How to refresh mcp (Cursor 1.0)" - servers stuck on loading

### Solution 20: Verify HTTP Remote MCP Server Configuration

**Status**: ⚠️ **For HTTP Servers** - Different configuration needed

**Action**: If using HTTP remote MCP servers:
1. Verify HTTP Compatibility Mode setting
2. Check server URL and authentication
3. Verify network connectivity
4. Check for CORS or connection errors in logs

**Note**: HTTP remote servers have different requirements than local stdio servers.

### Solution 21: Check Cursor Version Compatibility

**Status**: ⚠️ **Important** - Some versions have known bugs

**Action**:
1. Check Cursor version: `cursor --version`
2. Verify version is 1.3+ (includes security patches)
3. Update to latest version
4. Check release notes for MCP fixes

**Known Issues**:
- Version 2.0.77: MCP tools not exposed bug
- Version 1.4.0: MCP tools not recognized
- Older versions: Various MCP issues

### Solution 22: Ensure You're Logged Into Cursor IDE

**Status**: ✅ **CRITICAL DISCOVERY** - Login may be required!

**Finding (2025-12-05)**: After user logged into Cursor IDE, Playwright MCP tools became available!

**Action**:
1. Ensure you're logged into Cursor IDE
2. Check your account status in Cursor Settings
3. Verify MCP tools are exposed after login
4. Tools may not be available until authenticated

**Evidence**:
- Before login: Playwright MCP tools not available
- After login: Playwright MCP tools **NOW AVAILABLE** (`mcp_playwright_*`)
- This suggests authentication/login is required for MCP tool exposure

**Tool Naming After Login**:
- Playwright MCP: `mcp_playwright_browser_*` (22 tools)
- Browser MCP: `mcp_browser_browser_*` (21 tools)

**Note**: Even after login, browser detection may still fail - see Solution 23.

### Solution 23: Use Browser MCP Tools (Working Solution!)

**Status**: ✅ **CONFIRMED WORKING** - Browser MCP tools work after login!

**Success Confirmed (2025-12-05)**:
- Tool: `mcp_browser_browser_navigate` - ✅ **WORKS**
- Tool: `mcp_browser_browser_screenshot` - ✅ **WORKS**
- Tool: `mcp_browser_browser_tab_list` - ✅ **WORKS**

**Action**: Use `mcp_browser_*` tools instead of Playwright tools:
- `mcp_browser_browser_navigate` - Navigate to URLs
- `mcp_browser_browser_screenshot` - Take screenshots
- `mcp_browser_browser_click` - Click elements
- `mcp_browser_browser_type` - Type text
- And 17+ more browser tools

**Why This Works**: Browser MCP server (`@agent-infra/mcp-server-browser`) has better browser detection than Playwright MCP in this environment.

### Solution 24: Use Playwright Browser Install Tool

**Status**: ⚠️ **May Fix Browser Detection** - Try this if Playwright tools are available but browser not found

**Action**: If Playwright MCP tools are available but getting "Browser not installed" error:

1. Use the Playwright install tool:
   - Tool: `mcp_playwright_browser_install`
   - This may install/configure the browser properly

2. Or install via command line:
   ```bash
   npx playwright install chromium
   ```

3. Ensure environment variables are set (Solution 5)

4. Restart Cursor after installation

**Current Status**: Tools are available but browser detection failing - this may resolve it.

### Solution 25: Report to Cursor Team

**Status**: ✅ **Important for Long-term Fix**

**Action**:
1. Report issue to Cursor forum: https://forum.cursor.com
2. Include:
   - Cursor version (`cursor --version`)
   - OS and version
   - MCP server configuration
   - Which tools are registered vs. which are accessible
   - Screenshots of Cursor Settings showing tools
   - MCP logs if available
3. Reference known bug: Version 2.0.77 MCP tool exposure issue

**Forum Posts to Reference**:
- "MCP servers are not exposed to agents" (version 2.0.77 bug)
- "Browser Agent Tools Not Accessible Despite 'Ready' Status"
- "Playwright MCP not working on Cursor"

## Recommended Approach

### Quick Fixes to Try First

1. **Delete and Regenerate mcp.json** (Solution 8):
   - Backup current config
   - Delete `~/.cursor/mcp.json`
   - Let Cursor regenerate it
   - Re-add MCP servers
   - **Reported success by users**

2. **Disable Internal Browser Automation** (Solution 9):
   - Prevents interference with MCP browser tools
   - Disable in Cursor Settings → Tools & MCP → Browser Automation
   - Avoid using word "browser" in prompts if using MCP tools

3. **Reorder MCP Servers** (Solution 10):
   - Move problematic server to top of `mcpServers` object
   - Some users report this fixes the issue

4. **Check for Duplicates** (Solution 12):
   - Ensure each MCP server is only defined once
   - Remove any duplicate entries

### For Immediate Use

1. **✅ USE BROWSER MCP TOOLS** (Solution 23) - **CONFIRMED WORKING!**
   - Tools: `mcp_browser_browser_*` (21 tools)
   - Status: ✅ **WORKING** after user login
   - Tested: Navigation, screenshots, tab management all work
   - **This is your best option right now!**

2. **Ensure You're Logged In** (Solution 22):
   - Login to Cursor IDE
   - This made tools available in our testing
   - Critical requirement for MCP tool exposure

3. **Try Cursor CLI** (Solution 1):
   - Install: `curl https://cursor.com/install -fsS | bash`
   - Test if MCP tools are exposed via CLI
   - Use CLI for tasks requiring MCP tools
   - Note: Requires MCP server approval

4. **Use Cursor Browser Extension** (Solution 3):
   - Configure browser path in Cursor Settings
   - Use `mcp_cursor-browser-extension_*` tools
   - These are available and work

5. **Update Cursor** (Solution 2):
   - Check for updates
   - Update to latest version
   - Test if bug is fixed

### For Long-term Fix

1. **Report the Issue** (Solution 8):
   - Help Cursor team identify and fix the bug
   - Reference existing forum posts
   - Provide detailed information

2. **Monitor Updates**:
   - Check Cursor release notes
   - Watch for MCP tool exposure fixes
   - Test new versions

## Testing Checklist

### Test Cursor CLI

- [ ] Install Cursor CLI: `curl https://cursor.com/install -fsS | bash`
- [ ] Verify installation: `cursor-agent --version`
- [ ] List MCP servers: `cursor-agent mcp list`
- [ ] List Playwright tools: `cursor-agent mcp list-tools playwright`
- [ ] List Browser tools: `cursor-agent mcp list-tools browser`
- [ ] Test interactive mode: `cursor-agent`
- [ ] Test if tools are accessible in CLI vs. IDE
- [ ] Document findings

### Test Cursor IDE Updates

- [ ] Check current version: `cursor --version`
- [ ] Check for updates
- [ ] Update to latest version
- [ ] Test if MCP tools are now exposed
- [ ] Document version and results

### Test Configuration Changes

- [ ] Delete and regenerate mcp.json (Solution 8)
- [ ] Disable internal browser automation (Solution 9)
- [ ] Reorder MCP servers in config (Solution 10)
- [ ] Check for duplicate entries (Solution 12)
- [ ] Try project-specific .cursor/mcp.json (Solution 11)
- [ ] Try full Node.js path in MCP config (Solution 5)
- [ ] Try full npx path in MCP config (Solution 5)
- [ ] Change HTTP Compatibility Mode (if using HTTP servers) (Solution 4)
- [ ] Check for module resolution errors (Solution 15)
- [ ] Verify MCP tool protection settings (Solution 16)
- [ ] Check autoApprove settings (Solution 17)
- [ ] Restart Cursor completely (Solution 6)
- [ ] Test tool exposure after each change

## Related Documentation

- [MCP Tool Exposure OS Analysis](./MCP_TOOL_EXPOSURE_OS_ANALYSIS.md) - Platform comparison
- [Cursor IDE Linux MCP Issues](./CURSOR_IDE_LINUX_MCP_ISSUES.md) - Linux-specific issues
- [Cursor Browser MCP Setup](./CURSOR_BROWSER_MCP_SETUP.md) - Browser automation setup
- [MCP Configuration Guide](./MCP_CONFIGURATION_GUIDE.md) - Configuration details

## References

### Cursor Documentation
- [Cursor CLI Documentation](https://cursor.com/docs/cli)
- [Cursor CLI MCP Guide](https://cursor.com/docs/cli/mcp)
- [Cursor MCP Documentation](https://cursor.com/docs/context/mcp)

### Forum Posts
- [MCP servers are not exposed to agents](https://forum.cursor.com/t/mcp-servers-are-not-exposed-to-agents/143482)
- [Browser Agent Tools Not Accessible](https://forum.cursor.com/t/browser-agent-tools-not-accessible-despite-ready-status/143140)
- [Playwright MCP not working on Cursor](https://forum.cursor.com/t/playwright-mcp-not-working-on-cursor/145072)
- [Browser Automation interferes with other MCP tools](https://forum.cursor.com/t/browser-automation-interferes-with-other-mcp-tools-and-there-is-no-global-disable-for-it/143126)
- [MCP tools throwing "tool not found" - previously worked](https://www.reddit.com/r/cursor/comments/1kvesoc/mcp_tools_throwing_tool_not_found_previously/)
- [MCP Allowlist doesn't work](https://forum.cursor.com/t/mcp-allowlist-doesnt-work-also-cant-be-edited/135594)
- [Community Extension MCP Server Refresh](https://forum.cursor.com/t/community-extension-mcp-server-refresh-fix-for-stuck-mcp-servers-in-cursor/107283)

## Changelog

### 2025-12-05 (Updated - Second Update)
- **BREAKTHROUGH DISCOVERY**: Login to Cursor IDE may be required for MCP tool exposure!
- After user login, Playwright MCP tools became available (`mcp_playwright_*`)
- Browser MCP tools also became available (`mcp_browser_*`)
- Added Solution 22: Ensure logged into Cursor IDE (CRITICAL)
- Added Solution 23: Use Playwright browser install tool
- Updated quick reference with login requirement as #1 priority
- Created MCP_TOOL_EXPOSURE_TESTING_LOG.md documenting testing journey

### 2025-12-05 (Updated - First Update)
- **Added 15 additional workarounds** from comprehensive internet research:
  - Delete and regenerate mcp.json (reported success)
  - Disable internal browser automation
  - Reorder MCP servers in config
  - Use project-specific mcp.json
  - Check for duplicate entries
  - Manually add tools to allowlist
  - Use MCP server refresh extension
  - Check for module resolution errors
  - Verify MCP tool protection settings
  - Check autoApprove settings
  - Check for stuck "Loading Tools" status
  - Verify HTTP remote server configuration
  - Check Cursor version compatibility
- Reorganized recommended approach with quick fixes first
- Expanded testing checklist
- Added more forum post references

### 2025-12-05 (Initial)
- Created comprehensive solutions document
- Added Cursor CLI as recommended workaround
- Documented all known solutions and workarounds
- Added testing checklist
- Included references to Cursor documentation and forum posts

---

**This document provides actionable solutions for the MCP tool exposure issue. The Cursor CLI workaround is particularly promising as it may bypass the IDE bug entirely.**

