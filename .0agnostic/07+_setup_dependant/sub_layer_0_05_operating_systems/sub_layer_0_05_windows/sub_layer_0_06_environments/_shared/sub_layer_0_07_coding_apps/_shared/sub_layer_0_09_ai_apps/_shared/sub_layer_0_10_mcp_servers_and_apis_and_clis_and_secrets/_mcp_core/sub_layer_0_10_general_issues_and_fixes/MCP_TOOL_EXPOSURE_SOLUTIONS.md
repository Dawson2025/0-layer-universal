---
resource_id: "65816c8f-cba7-423a-b653-21a8c8d23f0c"
resource_type: "document"
resource_name: "MCP_TOOL_EXPOSURE_SOLUTIONS"
---
# MCP Tool Exposure Solutions and Workarounds

**Date**: 2025-12-05  
**Location**: Universal Layer → MCP Servers and Tools Setup  
**Status**: Comprehensive solutions guide

<!-- section_id: "ffdcefa0-1880-40ae-965a-6cf92a20f15e" -->
## Overview

This document provides solutions and workarounds for the Cursor IDE MCP tool exposure issue, where MCP tools are registered but not exposed to AI agents.

<!-- section_id: "56784355-a200-4629-af05-f4c609e4415e" -->
## Quick Reference: Most Promising Solutions

**CRITICAL: Enable MCP Servers in UI** (Solution 22):
- **Enable MCP servers in Cursor Settings → Tools & MCP** - This is REQUIRED!
- Configuration in mcp.json is not enough - servers must be toggled ON in UI
- After enabling Playwright in UI: "22 tools enabled" and tools became available
- **This is the critical step that was missing!**

**Also Important: Ensure You're Logged In** (Solution 23):
- **Login to Cursor IDE** - This may also be required for MCP tool exposure!
- After login, MCP servers can be enabled in UI

**Try These First** (in order):
1. **Ensure You're Logged Into Cursor IDE** (Solution 22) - ✅ **BREAKTHROUGH DISCOVERY**
2. **Delete and Regenerate mcp.json** (Solution 8) - ✅ User-reported success
3. **Use Playwright Browser Install Tool** (Solution 25) - If tools available but browser not found
4. **Disable Internal Browser Automation** (Solution 9) - Prevents interference
5. **Use Cursor CLI** (Solution 1) - May bypass IDE bug entirely
6. **Reorder MCP Servers** (Solution 10) - Move problematic server to top
7. **Check for Duplicates** (Solution 12) - Remove duplicate entries

**If Above Don't Work**:
- Use Cursor Browser Extension tools (Solution 3) - These work
- Try project-specific `.cursor/mcp.json` (Solution 11)
- Update Cursor to latest version (Solution 2)
- Check all diagnostic solutions (Solutions 6, 7, 15-21)

<!-- section_id: "f5335af4-c752-408c-bba5-6592cef9bacc" -->
## Confirmed: This is a Cursor IDE Bug

**Root Cause**: Cursor IDE bug (specifically version 2.0.77 has a known issue) where MCP tools aren't exposed to agents even though they appear connected.

**Affected Platforms**: Linux, WSL, Windows, and potentially macOS

**Evidence**: Internet research shows this is a cross-platform Cursor IDE bug, not OS-specific.

<!-- section_id: "fa2567cf-33d8-41fc-ae88-4f30fca94bd3" -->
## Solutions and Workarounds

<!-- section_id: "280fdb72-425a-4d90-b39e-790847e74bfb" -->
### Solution 1: Use Cursor CLI (Recommended Workaround)

**Status**: ✅ **Official Tool** - CLI is legitimate and officially supported by Cursor

**Verification (2025-12-05)**:
- ✅ **Legitimate**: Official product from Cursor team, documented on cursor.com
- ✅ **Real-world usage**: Used by developers for terminal-centric AI coding workflows
- ✅ **Production-ready**: Guides and tutorials treat it as production-ready tool
- ✅ **Security**: Ships with permission system for file operations and shell commands

**Why This Might Work**:
- Cursor CLI uses the same MCP configuration as the IDE
- CLI may have different tool exposure mechanism
- Some users report better MCP tool access via CLI
- Can be used from any editor (Neovim, VS Code, JetBrains) or remote environments

**IDE vs CLI Tradeoffs**:
- **IDE Better For**: Interactive coding, navigation, inline diffs, day-to-day editing
- **CLI Better For**: Automation, CI/CD, scripted refactors, headless runs, remote environments
- **Hybrid Approach**: Use IDE for interactive work, CLI for automation and batch tasks

**TUI vs GUI Bugs**:
- **TUI (CLI)**: More frequent UI glitches (endless scrolling, rendering issues, bugged states)
- **GUI (IDE)**: Less frequent but broader stability issues (freezes, crashes)
- **Recommendation**: For WSL, prioritize GUI for interactive work, use CLI for automation

**Note**: CLI requires MCP server approval separate from IDE approval

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
- [Cursor CLI Overview](https://cursor.com/cli)
- [Getting Started with Cursor CLI](https://www.codecademy.com/article/getting-started-with-cursor-cli)

**Research Sources (2025-12-05)**:
- Perplexity AI research confirming CLI legitimacy
- Developer reviews and tutorials
- Forum discussions on IDE vs CLI tradeoffs
- Bug reports comparing TUI vs GUI stability

<!-- section_id: "0320157b-9c21-49ee-a476-38f2f3415c74" -->
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

<!-- section_id: "d2c7e400-d1e3-4b08-8f2a-2fc02f4a0c51" -->
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

<!-- section_id: "8e765d94-6fdf-488e-bfdc-1a650e103793" -->
### Solution 4: Change HTTP Compatibility Mode (For HTTP Remote MCP Servers)

**Status**: ⚠️ **For HTTP Servers Only**

**Action**:
1. Go to Cursor Settings → Tools & MCP
2. Change HTTP Compatibility Mode
3. Restart Cursor

**Note**: This only helps if you're using HTTP remote MCP servers, not local stdio servers like Playwright.

<!-- section_id: "6b79d6ae-d319-4003-bb08-663139a0fcb5" -->
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

<!-- section_id: "25536f76-829e-464a-82ce-135cdddd9147" -->
### Solution 6: Restart Cursor Completely

**Status**: ⚠️ **Basic Troubleshooting**

**Action**:
1. Close all Cursor windows
2. Ensure all Cursor processes are terminated: `ps aux | grep cursor`
3. Kill any remaining processes if needed
4. Restart Cursor IDE
5. Check if tools are now exposed

**Note**: This is basic troubleshooting but sometimes helps.

<!-- section_id: "2d977232-7b14-46fb-8731-8a039fda45c4" -->
### Solution 7: Check Cursor Settings for Tool Availability

**Status**: ⚠️ **Diagnostic**

**Action**:
1. Go to Cursor Settings → Tools & MCP
2. Check "Installed MCP Servers" section
3. Verify which tools are listed
4. Compare what's listed vs. what's accessible to agents

**Note**: Tools may show as "22 tools" but not be accessible to agents - this confirms the bug.

<!-- section_id: "a4a86677-ebdf-4990-aa56-71894470d516" -->
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

<!-- section_id: "756969cd-451f-442b-a3de-b3f13c7b5eff" -->
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

<!-- section_id: "dc8ca05c-f2a1-4352-b165-9d224adf1331" -->
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

<!-- section_id: "18aefa05-89d4-4fec-8cd4-68e861b5386d" -->
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

<!-- section_id: "138a0472-fd92-45ff-9262-68fe8d8bf2d9" -->
### Solution 12: Check for Duplicate MCP Server Entries

**Status**: ⚠️ **Common Issue** - Duplicates can cause problems

**Action**:
1. Open `~/.cursor/mcp.json`
2. Check for duplicate server names or entries
3. Ensure each MCP server is described in only one place
4. Remove any duplicates
5. Restart Cursor

**Source**: Forum post: "Make sure 'hf-mcp-server' is described in only one place. Either remove the duplicate or rename"

<!-- section_id: "39cc4228-4fdf-4195-a7ae-ed849a41019b" -->
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

<!-- section_id: "7010c3a4-ddf1-4861-a9a7-7deba73dd692" -->
### Solution 14: Use MCP Server Refresh Extension

**Status**: ⚠️ **Community Solution** - For stuck MCP servers

**Action**: Install community extension "MCP Server Refresh" to fix stuck MCP servers that show "Loading Tools..." indefinitely.

**Problem**: MCP servers can randomly stop responding and get stuck on "Loading Tools..." requiring full Cursor restart.

**Source**: Forum: "Community Extension MCP Server Refresh - Fix for Stuck MCP Servers"

<!-- section_id: "483df7f4-75bb-4e6f-abf3-2c7149cf5a9f" -->
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

<!-- section_id: "2d1472dc-6bc5-427c-8a08-452bd07252b9" -->
### Solution 16: Verify MCP Tool Protection Settings

**Status**: ⚠️ **Security Setting** - May block tools

**Action**:
1. Go to Cursor Settings → Security or Tools & MCP
2. Check "MCP Tool Protection" settings
3. Ensure tools aren't being blocked by security settings
4. Adjust allowlist/blocklist if needed

**Note**: Security settings may prevent MCP tools from running even if exposed.

<!-- section_id: "ca73b0b9-994d-419d-bf87-39040393cbfd" -->
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

<!-- section_id: "d84c111b-89d4-4458-9a38-c5fc6960b7a5" -->
### Solution 18: Use Community Extension for MCP Refresh

**Status**: ⚠️ **Community Solution**

**Action**: Install community extension that provides MCP server refresh functionality to avoid full Cursor restarts.

**Benefits**: Can refresh MCP servers without restarting entire Cursor IDE.

<!-- section_id: "dabcb3b5-8e73-4a24-96b4-ae329bebda66" -->
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

<!-- section_id: "35e4ecf0-eaf8-481f-93f5-2492cd5ffa68" -->
### Solution 20: Verify HTTP Remote MCP Server Configuration

**Status**: ⚠️ **For HTTP Servers** - Different configuration needed

**Action**: If using HTTP remote MCP servers:
1. Verify HTTP Compatibility Mode setting
2. Check server URL and authentication
3. Verify network connectivity
4. Check for CORS or connection errors in logs

**Note**: HTTP remote servers have different requirements than local stdio servers.

<!-- section_id: "5348dfea-bb30-45b3-b859-c7cdfbcf525e" -->
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

<!-- section_id: "86f519fb-daaa-41ed-bd50-873435370014" -->
### Solution 22: Disable Unused MCP Servers (If Cursor Warns About Limits)

**Status**: ⚠️ **May Be Required** - If Cursor warns about too many servers/tools

**Finding (2025-12-05)**: User reported Cursor was warning about "too many MCP servers and too many tools" before disabling unused servers.

**Action**:
1. Go to Cursor Settings → Tools & MCP
2. Review all installed MCP servers
3. **Disable servers you're not actively using** (toggle OFF)
4. This may free up capacity for needed tools

**Why This Matters**:
- Cursor may have limits on active MCP servers/tools
- Too many enabled servers may prevent new tools from being exposed
- Disabling unused servers may resolve tool availability issues

**Evidence**:
- User disabled unused servers and Playwright tools became available
- Cursor was warning about too many servers/tools before
- After disabling unused servers, warning disappeared and tools worked

**Recommendation**: Only enable MCP servers that you actively need.

<!-- section_id: "df3c9320-509a-484e-81e4-87f0a203a413" -->
### Solution 23: Enable MCP Servers in Cursor Settings UI ⚠️ **CRITICAL STEP!**

**Status**: ✅ **BREAKTHROUGH DISCOVERY** - UI enablement is required!

**Finding (2025-12-05)**: MCP servers must be **enabled in Cursor Settings UI**, not just configured in mcp.json!

**Action**:
1. Go to Cursor Settings → Tools & MCP
2. Find your MCP servers in the list
3. **Toggle each server ON** (green toggle switch)
4. Wait for server to show "X tools enabled" status
5. Tools will then be available to AI agents

**Evidence**:
- Playwright server was configured in mcp.json but disabled in UI
- After enabling in UI: "22 tools enabled" appeared
- Tools immediately became available after UI enablement
- Navigation test successful after enabling

**Why This Matters**:
- Configuration in `mcp.json` is not enough
- Servers can be configured but disabled by default
- UI toggle is the final step to expose tools

**Note**: This is separate from login requirement (Solution 23 below).

<!-- section_id: "3da659c5-55a5-42d3-946a-d6b719ac11f2" -->
### Solution 24: Ensure You're Logged Into Cursor IDE

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

**Note**: Even after login, browser detection may still fail - see Solution 24.

<!-- section_id: "4ca80dc4-119d-48ea-9a7a-6ccc54ff01c4" -->
### Solution 25: Use Browser MCP Tools (Working Solution!)

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

<!-- section_id: "c987f86d-601a-4952-9def-f5c58bd5cab8" -->
### Solution 26: Use Playwright Browser Install Tool

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

<!-- section_id: "f4a76691-f094-4703-a3f1-b8cb937c44d5" -->
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

<!-- section_id: "0644b951-79ac-4748-903a-f07c51ff6a83" -->
## Recommended Approach

<!-- section_id: "9f47c3a4-6a1d-465d-aeda-496ed971d5ee" -->
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

<!-- section_id: "424a831f-5fde-493a-bbde-b7695f6c3ce6" -->
### For Immediate Use

1. **✅ USE BROWSER MCP TOOLS** (Solution 24) - **CONFIRMED WORKING!**
   - Tools: `mcp_browser_browser_*` (21 tools)
   - Status: ✅ **WORKING** after user login
   - Tested: Navigation, screenshots, tab management all work
   - **This is your best option right now!**

2. **Ensure You're Logged In** (Solution 23):
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

<!-- section_id: "f5ba2283-34ab-4475-98d6-a58dc02243ce" -->
### For Long-term Fix

1. **Report the Issue** (Solution 8):
   - Help Cursor team identify and fix the bug
   - Reference existing forum posts
   - Provide detailed information

2. **Monitor Updates**:
   - Check Cursor release notes
   - Watch for MCP tool exposure fixes
   - Test new versions

<!-- section_id: "9e09a154-693d-4f89-bfd1-063ea7059f18" -->
## Testing Checklist

<!-- section_id: "66f97534-45f9-4716-ad84-5ff447e902e8" -->
### Test Cursor CLI

- [ ] Install Cursor CLI: `curl https://cursor.com/install -fsS | bash`
- [ ] Verify installation: `cursor-agent --version`
- [ ] List MCP servers: `cursor-agent mcp list`
- [ ] List Playwright tools: `cursor-agent mcp list-tools playwright`
- [ ] List Browser tools: `cursor-agent mcp list-tools browser`
- [ ] Test interactive mode: `cursor-agent`
- [ ] Test if tools are accessible in CLI vs. IDE
- [ ] Document findings

<!-- section_id: "5f2c31d1-3595-45c2-8539-f0b165e5b170" -->
### Test Cursor IDE Updates

- [ ] Check current version: `cursor --version`
- [ ] Check for updates
- [ ] Update to latest version
- [ ] Test if MCP tools are now exposed
- [ ] Document version and results

<!-- section_id: "bea892ac-c44d-46a0-97fc-669fbc732c27" -->
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

<!-- section_id: "e934d9eb-0724-4a64-864c-3b6a9a609e7f" -->
## Related Documentation

- [MCP Tool Exposure OS Analysis](./MCP_TOOL_EXPOSURE_OS_ANALYSIS.md) - Platform comparison
- [Cursor IDE Linux MCP Issues](./CURSOR_IDE_LINUX_MCP_ISSUES.md) - Linux-specific issues
- [Cursor Browser MCP Setup](./CURSOR_BROWSER_MCP_SETUP.md) - Browser automation setup
- [MCP Configuration Guide](./MCP_CONFIGURATION_GUIDE.md) - Configuration details

<!-- section_id: "e41644b3-6142-4eef-af8e-4fea8ef11c1a" -->
## References

<!-- section_id: "bd3bd46f-f573-4872-9a4f-6640c86a269b" -->
### Cursor Documentation
- [Cursor CLI Documentation](https://cursor.com/docs/cli)
- [Cursor CLI MCP Guide](https://cursor.com/docs/cli/mcp)
- [Cursor MCP Documentation](https://cursor.com/docs/context/mcp)

<!-- section_id: "b785731f-3984-4fad-a0d9-a6efbed9e167" -->
### Forum Posts
- [MCP servers are not exposed to agents](https://forum.cursor.com/t/mcp-servers-are-not-exposed-to-agents/143482)
- [Browser Agent Tools Not Accessible](https://forum.cursor.com/t/browser-agent-tools-not-accessible-despite-ready-status/143140)
- [Playwright MCP not working on Cursor](https://forum.cursor.com/t/playwright-mcp-not-working-on-cursor/145072)
- [Browser Automation interferes with other MCP tools](https://forum.cursor.com/t/browser-automation-interferes-with-other-mcp-tools-and-there-is-no-global-disable-for-it/143126)
- [MCP tools throwing "tool not found" - previously worked](https://www.reddit.com/r/cursor/comments/1kvesoc/mcp_tools_throwing_tool_not_found_previously/)
- [MCP Allowlist doesn't work](https://forum.cursor.com/t/mcp-allowlist-doesnt-work-also-cant-be-edited/135594)
- [Community Extension MCP Server Refresh](https://forum.cursor.com/t/community-extension-mcp-server-refresh-fix-for-stuck-mcp-servers-in-cursor/107283)

<!-- section_id: "5a3615ff-1310-413f-940d-d2c78e921fab" -->
## Changelog

<!-- section_id: "cdac401e-fb10-4d03-8108-69be3228b2a9" -->
### 2025-12-07 (Updated - Gemini CLI Workaround)
- **NEW WORKAROUND**: Use Gemini CLI for browser automation when Cursor tools unavailable
- Gemini CLI has independent MCP configuration in `~/.gemini/settings.json`
- User confirmed Gemini CLI successfully accessed browser tools when Cursor could not
- Updated Cursor MCP config to match Gemini CLI's working configuration (added `--executable-path`)
- Created GEMINI_CLI_BROWSER_WORKAROUND.md documenting this approach
- See [Gemini CLI Browser Workaround](./GEMINI_CLI_BROWSER_WORKAROUND.md) for details

<!-- section_id: "d631281d-2593-4cf4-97b4-65ae9a3c5299" -->
### 2025-12-05 (Updated - Second Update)
- **BREAKTHROUGH DISCOVERY**: Login to Cursor IDE may be required for MCP tool exposure!
- After user login, Playwright MCP tools became available (`mcp_playwright_*`)
- Browser MCP tools also became available (`mcp_browser_*`)
- Added Solution 22: Ensure logged into Cursor IDE (CRITICAL)
- Added Solution 23: Use Playwright browser install tool
- Updated quick reference with login requirement as #1 priority
- Created MCP_TOOL_EXPOSURE_TESTING_LOG.md documenting testing journey

<!-- section_id: "a9154e60-ae0c-4990-88f3-cc508edc32f7" -->
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

<!-- section_id: "535a815e-e686-4d3f-bcd0-f7ae8691a4e7" -->
### 2025-12-05 (Initial)
- Created comprehensive solutions document
- Added Cursor CLI as recommended workaround
- Documented all known solutions and workarounds
- Added testing checklist
- Included references to Cursor documentation and forum posts

---

**This document provides actionable solutions for the MCP tool exposure issue. The Cursor CLI workaround is particularly promising as it may bypass the IDE bug entirely.**

