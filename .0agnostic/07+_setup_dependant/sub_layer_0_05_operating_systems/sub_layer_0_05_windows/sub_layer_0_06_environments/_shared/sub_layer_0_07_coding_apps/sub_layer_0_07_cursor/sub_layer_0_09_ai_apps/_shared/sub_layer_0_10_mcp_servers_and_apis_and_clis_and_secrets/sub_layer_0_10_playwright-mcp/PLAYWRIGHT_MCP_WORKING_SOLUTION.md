---
resource_id: "01247f23-5098-4626-b4aa-ba8b8e9a5856"
resource_type: "document"
resource_name: "PLAYWRIGHT_MCP_WORKING_SOLUTION"
---
# Playwright MCP Working Solution

**Date**: 2025-12-05  
**Location**: Universal Layer → MCP Servers and Tools Setup  
**Status**: ✅ **CONFIRMED WORKING**

<!-- section_id: "5bbee970-4b5c-42f9-97ae-bf1e11b979ec" -->
## Problem

Playwright MCP tools were configured in `mcp.json` but not available to AI agents. Tools showed as "22 tools enabled" in Cursor Settings but were not accessible.

<!-- section_id: "b34da0f7-86e3-4192-afbc-3e3439080e9e" -->
## Root Cause

**MCP servers must be enabled in Cursor Settings UI**, not just configured in `mcp.json`. Configuration in the JSON file is not sufficient - servers must be toggled ON in the Cursor IDE Settings interface.

<!-- section_id: "e0809c4d-e01c-4850-9f55-78c110129f6e" -->
## Solution Steps

<!-- section_id: "7cda4797-6f18-41fe-a79f-00887bf10181" -->
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

<!-- section_id: "f345560e-28f8-41e7-8f02-6d8208beb8fb" -->
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

<!-- section_id: "79ac33e8-1a0c-466b-b0db-f43e794d88e0" -->
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

<!-- section_id: "571d184f-38e9-40aa-963c-69a1f3b2e9b7" -->
### Step 4: Verify Tools Are Available ✅

**Test**:
- Tool: `mcp_playwright_browser_navigate("https://www.aleks.com")`
- Result: ✅ **SUCCESS** - Successfully navigated to page
- Status: 22 Playwright tools available and working

<!-- section_id: "db92e31f-5f40-4a3b-803b-7dddd715a4b2" -->
## Complete Working Configuration

<!-- section_id: "f6c8e31e-5e8f-46ac-8cb9-d82454bc63d7" -->
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

<!-- section_id: "a845fddc-e35a-4abf-9f7c-9cfa4bb7be0a" -->
### Cursor Settings UI
- **Location**: Cursor Settings → Tools & MCP → Installed MCP Servers
- **Status**: Playwright server toggle must be **ON** (green)
- **Expected**: "22 tools enabled" status

<!-- section_id: "c6a70bf6-b660-4c5d-9db1-c9c2beacbb0c" -->
## What We Tried (That Didn't Work Alone)

1. ✅ Configured in mcp.json - Required but not sufficient
2. ✅ Added environment variables - Required but not sufficient
3. ✅ Used full npx paths - Helpful but not sufficient
4. ✅ Reordered servers - Didn't help
5. ✅ Checked for duplicates - None found
6. ✅ Created project-specific config - Didn't help
7. ✅ Disabled unused MCP servers - **May have helped** (freed up capacity)
8. ❌ **Missing**: Enable in Cursor Settings UI - **This was the critical step!**

<!-- section_id: "193322b3-8df4-49da-9d85-356eaed41bd4" -->
## Complete Solution (All Steps)

**To get Playwright MCP tools working, you need:**

1. ✅ **Configure in mcp.json** - Full paths, environment variables
2. ✅ **Disable unused MCP servers** - Free up capacity (if Cursor warns about limits)
3. ✅ **Enable Playwright server in Cursor Settings UI** - **CRITICAL**
4. ✅ **Verify tools are available** - Test navigation

**All steps may be necessary for success.**

<!-- section_id: "fb50ec45-8a14-43be-945a-fc820290ba47" -->
## Key Learnings

<!-- section_id: "432d9eb0-b74d-40be-a0ca-acd7ade0214b" -->
### Critical Discovery #1: UI Enablement Required
**MCP servers must be enabled in Cursor Settings UI**, not just configured in mcp.json.

<!-- section_id: "ea4b9e12-8a70-43e6-ba84-d3ab5e8a39e0" -->
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

<!-- section_id: "790579b9-db18-4069-8c5b-2b7e76b8e8ec" -->
### Configuration Requirements
1. **mcp.json configuration** - Required for server setup
2. **Environment variables** - Required for browser detection
3. **Full paths** - Recommended for NVM setups
4. **UI enablement** - **CRITICAL** - Required to expose tools

<!-- section_id: "a40b36dd-af6b-4edf-8e75-76f8293bdec7" -->
### Tool Availability
- After enabling in UI: Tools immediately available
- Before enabling in UI: Tools configured but not accessible
- After restart: May need to re-enable in UI (enablement may not persist)

<!-- section_id: "d26f3f39-7e4e-418c-a84d-d51f121fc8d8" -->
## Testing Results

<!-- section_id: "37f89e56-5cb4-4df6-ad73-b515b92b7da7" -->
### Successful Tests
- ✅ Navigation: `mcp_playwright_browser_navigate("https://www.aleks.com")`
- ✅ Page loading: Full page content retrieved
- ✅ Tool availability: 22 Playwright tools accessible

<!-- section_id: "cc8d70ee-338b-4429-bb29-b9cbef08b179" -->
### Test URLs
- ALEKS: `https://www.aleks.com`
- BYU-Idaho Canvas: `https://byui.instructure.com/courses/353368/grades`

<!-- section_id: "2097fe94-ac00-4b72-9c02-3fdad37e41de" -->
## Troubleshooting

<!-- section_id: "038196b4-0990-466f-ae44-1b9895bafec8" -->
### Tools Not Available After Configuration
1. Check Cursor Settings → Tools & MCP
2. Verify server is enabled (green toggle)
3. If disabled, toggle ON
4. Wait for "X tools enabled" status

<!-- section_id: "11d29114-1eff-444a-8726-852ffdc823ee" -->
### Tools Not Available After Restart
1. Check if server is still enabled in UI
2. Re-enable if needed
3. Enablement may not persist across restarts

<!-- section_id: "494bd281-28ea-4d88-9002-b8ea01de52f1" -->
### Cursor Warning About Too Many MCP Servers/Tools
1. Go to Cursor Settings → Tools & MCP
2. Review all enabled servers
3. Disable servers you're not actively using
4. Try enabling the server you need again
5. This may free up capacity for new tools

<!-- section_id: "e0f5e8e8-84da-4442-8ff1-5c94485b4178" -->
### Browser Detection Issues
1. Verify `PLAYWRIGHT_BROWSERS_PATH` is set correctly
2. Check browser installation: `ls ~/.cache/ms-playwright/chromium-*/`
3. Use full npx path if using NVM

<!-- section_id: "ab75cdb8-fdb0-4b21-a788-5247704e462b" -->
## Related Documentation

- [MCP Tool Exposure Solutions](./MCP_TOOL_EXPOSURE_SOLUTIONS.md) - All solutions
- [MCP Tool Exposure Testing Log](./MCP_TOOL_EXPOSURE_TESTING_LOG.md) - Testing journey
- [MCP Fix Attempts Log](./MCP_FIX_ATTEMPTS_LOG.md) - All attempts
- [Browser Environment Variable Fix](./BROWSER_ENV_VAR_FIX.md) - Environment variables
- [MCP Configuration Guide](./MCP_CONFIGURATION_GUIDE.md) - General configuration

<!-- section_id: "25e42bdf-27ec-4333-83c2-9721ae6ee005" -->
## Changelog

<!-- section_id: "52dabaf1-22f9-4cba-88ce-be077429cc65" -->
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

