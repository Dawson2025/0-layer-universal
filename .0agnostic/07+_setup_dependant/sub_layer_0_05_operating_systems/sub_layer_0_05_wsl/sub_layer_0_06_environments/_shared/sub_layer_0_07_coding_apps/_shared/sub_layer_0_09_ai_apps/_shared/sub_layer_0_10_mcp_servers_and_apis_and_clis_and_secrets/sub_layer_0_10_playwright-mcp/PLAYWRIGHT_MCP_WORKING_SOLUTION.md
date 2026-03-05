---
resource_id: "d3bc4341-40c4-4fdc-86d7-5f1caf8ed155"
resource_type: "document"
resource_name: "PLAYWRIGHT_MCP_WORKING_SOLUTION"
---
# Playwright MCP Working Solution

**Date**: 2025-12-05  
**Location**: Universal Layer → MCP Servers and Tools Setup  
**Status**: ✅ **CONFIRMED WORKING**

<!-- section_id: "586ff329-f114-4700-a50a-e69f09cc7dac" -->
## Problem

Playwright MCP tools were configured in `mcp.json` but not available to AI agents. Tools showed as "22 tools enabled" in Cursor Settings but were not accessible.

<!-- section_id: "96983ceb-0ac0-4cb6-b858-799ced78e9ee" -->
## Root Cause

**MCP servers must be enabled in Cursor Settings UI**, not just configured in `mcp.json`. Configuration in the JSON file is not sufficient - servers must be toggled ON in the Cursor IDE Settings interface.

<!-- section_id: "de59ad5b-aeb5-4392-b580-1e6fa234447d" -->
## Solution Steps

<!-- section_id: "a1734036-cfba-4215-b4ab-c0314e936ae4" -->
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

<!-- section_id: "7fb33c6a-096d-4e2f-9308-db3c1571ed13" -->
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

<!-- section_id: "2b9c1c2c-36cd-4db8-9a6d-03559a60f928" -->
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

<!-- section_id: "310c78eb-d9a1-4fe3-b5e1-12ef04d0da12" -->
### Step 4: Verify Tools Are Available ✅

**Test**:
- Tool: `mcp_playwright_browser_navigate("https://www.aleks.com")`
- Result: ✅ **SUCCESS** - Successfully navigated to page
- Status: 22 Playwright tools available and working

<!-- section_id: "939c5ad0-a40d-4df5-b14f-7f05fea4a330" -->
## Complete Working Configuration

<!-- section_id: "0bb9ff9d-cb22-4149-b0e7-1332a57ce754" -->
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

<!-- section_id: "77609e60-962c-4a0f-812d-abbc40503ab2" -->
### Cursor Settings UI
- **Location**: Cursor Settings → Tools & MCP → Installed MCP Servers
- **Status**: Playwright server toggle must be **ON** (green)
- **Expected**: "22 tools enabled" status

<!-- section_id: "205e614a-6824-4bd5-9d63-f36c16abc00b" -->
## What We Tried (That Didn't Work Alone)

1. ✅ Configured in mcp.json - Required but not sufficient
2. ✅ Added environment variables - Required but not sufficient
3. ✅ Used full npx paths - Helpful but not sufficient
4. ✅ Reordered servers - Didn't help
5. ✅ Checked for duplicates - None found
6. ✅ Created project-specific config - Didn't help
7. ✅ Disabled unused MCP servers - **May have helped** (freed up capacity)
8. ❌ **Missing**: Enable in Cursor Settings UI - **This was the critical step!**

<!-- section_id: "bb6a9216-c059-4146-a4fa-06116e14a7bb" -->
## Complete Solution (All Steps)

**To get Playwright MCP tools working, you need:**

1. ✅ **Configure in mcp.json** - Full paths, environment variables
2. ✅ **Disable unused MCP servers** - Free up capacity (if Cursor warns about limits)
3. ✅ **Enable Playwright server in Cursor Settings UI** - **CRITICAL**
4. ✅ **Verify tools are available** - Test navigation

**All steps may be necessary for success.**

<!-- section_id: "cbfd3ffa-4e94-464b-8227-20cd08cfe9c3" -->
## Key Learnings

<!-- section_id: "3dae62c7-3ff2-4baf-a7c5-5cb05e5c093e" -->
### Critical Discovery #1: UI Enablement Required
**MCP servers must be enabled in Cursor Settings UI**, not just configured in mcp.json.

<!-- section_id: "905c40be-21eb-42b5-85f8-a25f2bc6e2a9" -->
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

<!-- section_id: "b49ebdfc-d45a-45ae-83c7-874edcb37a27" -->
### Configuration Requirements
1. **mcp.json configuration** - Required for server setup
2. **Environment variables** - Required for browser detection
3. **Full paths** - Recommended for NVM setups
4. **UI enablement** - **CRITICAL** - Required to expose tools

<!-- section_id: "a6f6ee52-9357-4ece-a16d-8e78f0de9ac0" -->
### Tool Availability
- After enabling in UI: Tools immediately available
- Before enabling in UI: Tools configured but not accessible
- After restart: May need to re-enable in UI (enablement may not persist)

<!-- section_id: "2b19afc0-58f9-4f06-b7dc-ffa16adc324b" -->
## Testing Results

<!-- section_id: "7cc88f88-4ce8-4fec-9f64-6f821d8e664a" -->
### Successful Tests
- ✅ Navigation: `mcp_playwright_browser_navigate("https://www.aleks.com")`
- ✅ Page loading: Full page content retrieved
- ✅ Tool availability: 22 Playwright tools accessible

<!-- section_id: "c436c6c4-86e6-475a-b200-a987dd57361c" -->
### Test URLs
- ALEKS: `https://www.aleks.com`
- BYU-Idaho Canvas: `https://byui.instructure.com/courses/353368/grades`

<!-- section_id: "9e7e70ca-9c87-4a69-af10-b7a353c8aa7a" -->
## Troubleshooting

<!-- section_id: "ed9e91c1-8585-449a-9b61-08f23cac019c" -->
### Tools Not Available After Configuration
1. Check Cursor Settings → Tools & MCP
2. Verify server is enabled (green toggle)
3. If disabled, toggle ON
4. Wait for "X tools enabled" status

<!-- section_id: "820f4eb6-ff07-4fee-9e5a-c108690732fe" -->
### Tools Not Available After Restart
1. Check if server is still enabled in UI
2. Re-enable if needed
3. Enablement may not persist across restarts

<!-- section_id: "257aee6c-0945-4aee-bef2-ea70a1cf70f9" -->
### Cursor Warning About Too Many MCP Servers/Tools
1. Go to Cursor Settings → Tools & MCP
2. Review all enabled servers
3. Disable servers you're not actively using
4. Try enabling the server you need again
5. This may free up capacity for new tools

<!-- section_id: "99b727ce-0ee0-47eb-95da-95004d141478" -->
### Browser Detection Issues
1. Verify `PLAYWRIGHT_BROWSERS_PATH` is set correctly
2. Check browser installation: `ls ~/.cache/ms-playwright/chromium-*/`
3. Use full npx path if using NVM

<!-- section_id: "3f2021d3-a12b-4324-8a46-821b827fd817" -->
## Related Documentation

- [MCP Tool Exposure Solutions](./MCP_TOOL_EXPOSURE_SOLUTIONS.md) - All solutions
- [MCP Tool Exposure Testing Log](./MCP_TOOL_EXPOSURE_TESTING_LOG.md) - Testing journey
- [MCP Fix Attempts Log](./MCP_FIX_ATTEMPTS_LOG.md) - All attempts
- [Browser Environment Variable Fix](./BROWSER_ENV_VAR_FIX.md) - Environment variables
- [MCP Configuration Guide](./MCP_CONFIGURATION_GUIDE.md) - General configuration

<!-- section_id: "d5f59128-e0d2-45da-81d7-514871bdfd41" -->
## Changelog

<!-- section_id: "1e0c8607-c78e-4dd9-ae4b-ba8ee04554ac" -->
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

