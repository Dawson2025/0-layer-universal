---
resource_id: "90979641-8644-4122-8447-9b799068a0fd"
resource_type: "document"
resource_name: "PLAYWRIGHT_MCP_WORKING_SOLUTION"
---
# Playwright MCP Working Solution

**Date**: 2025-12-05  
**Location**: Universal Layer → MCP Servers and Tools Setup  
**Status**: ✅ **CONFIRMED WORKING**

<!-- section_id: "2934e9bd-d330-4290-8c1f-9a54a72483b5" -->
## Problem

Playwright MCP tools were configured in `mcp.json` but not available to AI agents. Tools showed as "22 tools enabled" in Cursor Settings but were not accessible.

<!-- section_id: "7146b7dc-2035-49b1-8018-cc20e7dcc40f" -->
## Root Cause

**MCP servers must be enabled in Cursor Settings UI**, not just configured in `mcp.json`. Configuration in the JSON file is not sufficient - servers must be toggled ON in the Cursor IDE Settings interface.

<!-- section_id: "e56fa797-b53a-4171-9b0f-2fbf918ca7d2" -->
## Solution Steps

<!-- section_id: "d7b6a212-db43-41e6-991e-826265a8fb6b" -->
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

<!-- section_id: "ce4655f1-2e64-47b5-b0ac-693bd300983f" -->
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

<!-- section_id: "8a684a1a-cca5-4d98-8227-2cf88690aaf0" -->
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

<!-- section_id: "b9bb6281-e3b1-47cb-ba47-bff2d26def34" -->
### Step 4: Verify Tools Are Available ✅

**Test**:
- Tool: `mcp_playwright_browser_navigate("https://www.aleks.com")`
- Result: ✅ **SUCCESS** - Successfully navigated to page
- Status: 22 Playwright tools available and working

<!-- section_id: "20ac21b7-01bd-4c6f-b584-a0e8b271429d" -->
## Complete Working Configuration

<!-- section_id: "b5812701-ac12-4d79-bee2-3a9ab9d7d761" -->
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

<!-- section_id: "69334288-5beb-40b8-83fc-9631bd4e6bec" -->
### Cursor Settings UI
- **Location**: Cursor Settings → Tools & MCP → Installed MCP Servers
- **Status**: Playwright server toggle must be **ON** (green)
- **Expected**: "22 tools enabled" status

<!-- section_id: "5cb5168c-9c12-44cc-a575-c88e9ba7a80b" -->
## What We Tried (That Didn't Work Alone)

1. ✅ Configured in mcp.json - Required but not sufficient
2. ✅ Added environment variables - Required but not sufficient
3. ✅ Used full npx paths - Helpful but not sufficient
4. ✅ Reordered servers - Didn't help
5. ✅ Checked for duplicates - None found
6. ✅ Created project-specific config - Didn't help
7. ✅ Disabled unused MCP servers - **May have helped** (freed up capacity)
8. ❌ **Missing**: Enable in Cursor Settings UI - **This was the critical step!**

<!-- section_id: "f3f79d33-9e87-426f-9bde-8996a955f683" -->
## Complete Solution (All Steps)

**To get Playwright MCP tools working, you need:**

1. ✅ **Configure in mcp.json** - Full paths, environment variables
2. ✅ **Disable unused MCP servers** - Free up capacity (if Cursor warns about limits)
3. ✅ **Enable Playwright server in Cursor Settings UI** - **CRITICAL**
4. ✅ **Verify tools are available** - Test navigation

**All steps may be necessary for success.**

<!-- section_id: "0215375a-2bc0-4747-995c-86ee34d74e89" -->
## Key Learnings

<!-- section_id: "23794d9f-225d-4a24-a488-97571de759f1" -->
### Critical Discovery #1: UI Enablement Required
**MCP servers must be enabled in Cursor Settings UI**, not just configured in mcp.json.

<!-- section_id: "9c25e7fd-4841-4b0c-94d7-de23cdb9ba40" -->
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

<!-- section_id: "c1a02bd9-4583-443b-800c-4700b4c489b5" -->
### Configuration Requirements
1. **mcp.json configuration** - Required for server setup
2. **Environment variables** - Required for browser detection
3. **Full paths** - Recommended for NVM setups
4. **UI enablement** - **CRITICAL** - Required to expose tools

<!-- section_id: "40e73b9a-4606-4554-b080-2c8e31a869ab" -->
### Tool Availability
- After enabling in UI: Tools immediately available
- Before enabling in UI: Tools configured but not accessible
- After restart: May need to re-enable in UI (enablement may not persist)

<!-- section_id: "bc476000-a208-48e8-bdbd-35864f0b9d3e" -->
## Testing Results

<!-- section_id: "3e39907e-6eed-4a9b-8678-9d5dba65b62e" -->
### Successful Tests
- ✅ Navigation: `mcp_playwright_browser_navigate("https://www.aleks.com")`
- ✅ Page loading: Full page content retrieved
- ✅ Tool availability: 22 Playwright tools accessible

<!-- section_id: "faf40761-341a-46fe-b074-c443d2f90208" -->
### Test URLs
- ALEKS: `https://www.aleks.com`
- BYU-Idaho Canvas: `https://byui.instructure.com/courses/353368/grades`

<!-- section_id: "667fb4d6-7dba-4e5e-941b-9ec00d87150e" -->
## Troubleshooting

<!-- section_id: "702e1267-a7a9-461a-9561-62117e619d01" -->
### Tools Not Available After Configuration
1. Check Cursor Settings → Tools & MCP
2. Verify server is enabled (green toggle)
3. If disabled, toggle ON
4. Wait for "X tools enabled" status

<!-- section_id: "959749e8-1ca4-4f24-ad44-62560d58cd28" -->
### Tools Not Available After Restart
1. Check if server is still enabled in UI
2. Re-enable if needed
3. Enablement may not persist across restarts

<!-- section_id: "17a01ef2-fd11-432f-8010-281164d28449" -->
### Cursor Warning About Too Many MCP Servers/Tools
1. Go to Cursor Settings → Tools & MCP
2. Review all enabled servers
3. Disable servers you're not actively using
4. Try enabling the server you need again
5. This may free up capacity for new tools

<!-- section_id: "9ce16bd9-f604-446b-b579-e51217293a5b" -->
### Browser Detection Issues
1. Verify `PLAYWRIGHT_BROWSERS_PATH` is set correctly
2. Check browser installation: `ls ~/.cache/ms-playwright/chromium-*/`
3. Use full npx path if using NVM

<!-- section_id: "9711132d-67ce-4834-a127-268e9b3b079c" -->
## Related Documentation

- [MCP Tool Exposure Solutions](./MCP_TOOL_EXPOSURE_SOLUTIONS.md) - All solutions
- [MCP Tool Exposure Testing Log](./MCP_TOOL_EXPOSURE_TESTING_LOG.md) - Testing journey
- [MCP Fix Attempts Log](./MCP_FIX_ATTEMPTS_LOG.md) - All attempts
- [Browser Environment Variable Fix](./BROWSER_ENV_VAR_FIX.md) - Environment variables
- [MCP Configuration Guide](./MCP_CONFIGURATION_GUIDE.md) - General configuration

<!-- section_id: "28ca7023-7ef9-4b40-95b2-da3aa75f29a8" -->
## Changelog

<!-- section_id: "1e662aee-1e96-44ba-85dc-5ac1248558f6" -->
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

