---
resource_id: "b3f82358-76e2-48f5-a087-f711902e6d1a"
resource_type: "document"
resource_name: "PLAYWRIGHT_MCP_WORKING_SOLUTION"
---
# Playwright MCP Working Solution

**Date**: 2025-12-05  
**Location**: Universal Layer → MCP Servers and Tools Setup  
**Status**: ✅ **CONFIRMED WORKING**

<!-- section_id: "4a3de1f9-5b19-4cd9-8179-db9d682cdae6" -->
## Problem

Playwright MCP tools were configured in `mcp.json` but not available to AI agents. Tools showed as "22 tools enabled" in Cursor Settings but were not accessible.

<!-- section_id: "91f7abca-b901-408a-82bb-48ca0233dd3f" -->
## Root Cause

**MCP servers must be enabled in Cursor Settings UI**, not just configured in `mcp.json`. Configuration in the JSON file is not sufficient - servers must be toggled ON in the Cursor IDE Settings interface.

<!-- section_id: "1a55a257-f075-4738-9801-5994075fd716" -->
## Solution Steps

<!-- section_id: "919f41f1-9565-4d91-902d-6053cd6dfec9" -->
### Step 1: Configure MCP Server in mcp.json ✅

**File**: `~/.config/mcp/mcp.json` (or `~/.cursor/mcp.json` if symlinked)

**Configuration**:
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

**Key Configuration Elements**:
1. **Full npx path**: Use full path to npx (especially important with NVM)
   - Example: `/home/dawson/.nvm/versions/node/v22.20.0/bin/npx`
   - Prevents PATH issues when MCP servers start
2. **Environment variables**: Set `PLAYWRIGHT_BROWSERS_PATH` and `HOME`
   - `PLAYWRIGHT_BROWSERS_PATH`: Points to browser installation directory
   - `HOME`: Ensures proper home directory resolution
3. **Browser specification**: `--browser chromium` flag

<!-- section_id: "01626c77-1d3b-4faa-a881-014e37fac7bd" -->
### Step 2: Disable Unused MCP Servers (If Needed) ⚠️ **May Be Required**

**If Cursor warns about too many MCP servers/tools:**

**Action**:
1. Go to **Cursor Settings** → **Tools & MCP**
2. Review all installed MCP servers
3. **Disable servers you're not actively using** (toggle OFF)
4. This may free up capacity for needed tools

**Why This Matters**:
- Cursor may have limits on active MCP servers/tools
- Too many enabled servers may prevent new tools from being exposed
- Disabling unused servers may resolve tool availability issues

<!-- section_id: "dffe5845-3a0b-4c0e-af11-deb043eec0e8" -->
### Step 3: Enable MCP Server in Cursor Settings UI ⚠️ **CRITICAL**

**This is the step that was missing!**

**Action**:
1. Open Cursor IDE
2. Go to **Cursor Settings** → **Tools & MCP**
3. Find "playwright" in the "Installed MCP Servers" list
4. **Toggle the switch ON** (should turn green)
5. Wait for status to show "22 tools enabled"

**Why This Matters**:
- Configuration in `mcp.json` is not enough
- Servers can be configured but disabled by default
- UI toggle is the final step to expose tools to AI agents
- Tools will not be available until server is enabled in UI

<!-- section_id: "397552d1-f236-49cc-aefb-43894caa5dbb" -->
### Step 4: Verify Tools Are Available ✅

**Test**:
- Tool: `mcp_playwright_browser_navigate("https://www.aleks.com")`
- Result: ✅ **SUCCESS** - Successfully navigated to page
- Status: 22 Playwright tools available and working

<!-- section_id: "0e37b493-9ea1-42b4-b88d-d7217bf25295" -->
## Complete Working Configuration

<!-- section_id: "1a2377b5-d7d3-4437-9cf4-1fbca92cc495" -->
### mcp.json Configuration
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

<!-- section_id: "9718351d-7cfc-46e4-90e0-72ce6d04a067" -->
### Cursor Settings UI
- **Location**: Cursor Settings → Tools & MCP → Installed MCP Servers
- **Status**: Playwright server toggle must be **ON** (green)
- **Expected**: "22 tools enabled" status

<!-- section_id: "89723c21-5839-46ed-9924-25254db55a93" -->
## What We Tried (That Didn't Work Alone)

1. ✅ Configured in mcp.json - Required but not sufficient
2. ✅ Added environment variables - Required but not sufficient
3. ✅ Used full npx paths - Helpful but not sufficient
4. ✅ Reordered servers - Didn't help
5. ✅ Checked for duplicates - None found
6. ✅ Created project-specific config - Didn't help
7. ✅ Disabled unused MCP servers - **May have helped** (freed up capacity)
8. ❌ **Missing**: Enable in Cursor Settings UI - **This was the critical step!**

<!-- section_id: "f329b389-bfea-4da4-a9e4-44bb26b0886d" -->
## Complete Solution (All Steps)

**To get Playwright MCP tools working, you need:**

1. ✅ **Configure in mcp.json** - Full paths, environment variables
2. ✅ **Disable unused MCP servers** - Free up capacity (if Cursor warns about limits)
3. ✅ **Enable Playwright server in Cursor Settings UI** - **CRITICAL**
4. ✅ **Verify tools are available** - Test navigation

**All steps may be necessary for success.**

<!-- section_id: "5d8e7aa5-9342-4e2c-a328-e1e2fcfc0b79" -->
## Key Learnings

<!-- section_id: "cae965ab-a088-42ef-aa5e-f8b32fc3f78f" -->
### Critical Discovery #1: UI Enablement Required
**MCP servers must be enabled in Cursor Settings UI**, not just configured in mcp.json.

<!-- section_id: "9d0c5949-a5bd-4017-b1aa-4ec6dcc9cb55" -->
### Critical Discovery #2: MCP Server/Tool Limits ✅ **RESEARCHED & CONFIRMED**

**Cursor has a hard limit of 40 tools total across all enabled MCP servers.**

**Research Findings (2025-12-05)**:
- **Hard Limit**: 40 tools total (confirmed by multiple sources)
- **Warning Threshold**: 40 tools triggers performance warning
- **Actual Hard Cap**: May be 80 tools, but 40 is the practical limit
- **Why**: Limits exist to manage context window and help AI choose tools effectively

**User Experience**:
- User reported Cursor warning: "too many MCP servers and too many tools"
- After disabling unused MCP servers, Playwright tools became available
- This freed up capacity within the 40-tool limit

**Implication**:
- **40-tool hard limit** - Tools beyond this won't be available to AI agents
- Disabling unused servers is **essential** to stay under the limit
- Only the first 40 tools are sent to the AI agent
- If you have 41+ tools, the 41st tool won't be accessible

**Recommendation**:
- **Only enable MCP servers you actively need**
- **Disable servers that aren't being used**
- **Monitor tool count** in Cursor Settings → Tools & MCP
- **If tools aren't appearing, disable other servers** to free up capacity

**See Also**: [MCP Tool Limits Research](./MCP_TOOL_LIMITS_RESEARCH.md) for comprehensive research findings.

<!-- section_id: "ba952070-45d1-4915-9e5a-1ea871a8e204" -->
### Configuration Requirements
1. **mcp.json configuration** - Required for server setup
2. **Environment variables** - Required for browser detection
3. **Full paths** - Recommended for NVM setups
4. **UI enablement** - **CRITICAL** - Required to expose tools

<!-- section_id: "e4b0cc67-9e1b-496e-8978-c982406b87b5" -->
### Tool Availability
- After enabling in UI: Tools immediately available
- Before enabling in UI: Tools configured but not accessible
- After restart: May need to re-enable in UI (enablement may not persist)

<!-- section_id: "97931b9d-fa22-4987-afc9-cb98293938d4" -->
## Testing Results

<!-- section_id: "d81c2e6d-3975-4886-b9fc-c665656e8298" -->
### Successful Tests
- ✅ Navigation: `mcp_playwright_browser_navigate("https://www.aleks.com")`
- ✅ Page loading: Full page content retrieved
- ✅ Tool availability: 22 Playwright tools accessible

<!-- section_id: "726d36a3-7b95-4a03-acfa-90cc16b0322f" -->
### Test URLs
- ALEKS: `https://www.aleks.com`
- BYU-Idaho Canvas: `https://byui.instructure.com/courses/353368/grades`

<!-- section_id: "a08636fd-42b4-42d8-9cba-13080594a15c" -->
## Troubleshooting

<!-- section_id: "b4cb11bc-7295-48b5-9cc3-59fc5fefcefb" -->
### Tools Not Available After Configuration
1. Check Cursor Settings → Tools & MCP
2. Verify server is enabled (green toggle)
3. If disabled, toggle ON
4. Wait for "X tools enabled" status

<!-- section_id: "c40b71fe-4cc0-4a89-ab3e-7e443624ceb1" -->
### Tools Not Available After Restart
1. Check if server is still enabled in UI
2. Re-enable if needed
3. Enablement may not persist across restarts

<!-- section_id: "9dcd355a-78d8-4cea-af5f-b8187942d1b8" -->
### Cursor Warning About Too Many MCP Servers/Tools
1. Go to Cursor Settings → Tools & MCP
2. Review all enabled servers
3. Disable servers you're not actively using
4. Try enabling the server you need again
5. This may free up capacity for new tools

<!-- section_id: "77aa1f4d-2c83-41c8-9c36-d96f9973d52d" -->
### Browser Detection Issues
1. Verify `PLAYWRIGHT_BROWSERS_PATH` is set correctly
2. Check browser installation: `ls ~/.cache/ms-playwright/chromium-*/`
3. Use full npx path if using NVM

<!-- section_id: "ec018f8c-c66f-4ff0-8589-90da367c0d5f" -->
## Related Documentation

- [MCP Tool Exposure Solutions](./MCP_TOOL_EXPOSURE_SOLUTIONS.md) - All solutions
- [MCP Tool Exposure Testing Log](./MCP_TOOL_EXPOSURE_TESTING_LOG.md) - Testing journey
- [MCP Fix Attempts Log](./MCP_FIX_ATTEMPTS_LOG.md) - All attempts
- [Browser Environment Variable Fix](./BROWSER_ENV_VAR_FIX.md) - Environment variables
- [MCP Configuration Guide](./MCP_CONFIGURATION_GUIDE.md) - General configuration

<!-- section_id: "cf842fd2-5fed-4c29-aba9-6903fff2b659" -->
## Changelog

<!-- section_id: "cccf86e0-7dc7-4dff-9214-ad3bd5140c5f" -->
### 2025-12-05
- Created comprehensive working solution document
- Documented critical UI enablement step
- Added complete configuration examples
- Documented all troubleshooting steps
- Confirmed solution works with successful tests

---

**Key Takeaways**: 
1. Configuration in `mcp.json` + **Enablement in Cursor Settings UI** = Working Playwright MCP tools!
2. **Disable unused MCP servers** if Cursor warns about too many servers/tools - this may free up capacity
3. Cursor may have limits on active MCP servers and tools - manage which servers are enabled

