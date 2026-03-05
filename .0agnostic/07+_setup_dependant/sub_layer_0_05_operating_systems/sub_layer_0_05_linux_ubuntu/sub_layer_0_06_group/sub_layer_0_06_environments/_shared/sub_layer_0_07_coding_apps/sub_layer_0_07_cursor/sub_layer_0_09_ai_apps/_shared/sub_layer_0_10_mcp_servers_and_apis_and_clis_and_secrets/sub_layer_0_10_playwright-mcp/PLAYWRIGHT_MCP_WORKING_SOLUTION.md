---
resource_id: "64b09518-0a8d-4a7d-9de1-1eea6a33d879"
resource_type: "document"
resource_name: "PLAYWRIGHT_MCP_WORKING_SOLUTION"
---
# Playwright MCP Working Solution

**Date**: 2025-12-05  
**Location**: Universal Layer → MCP Servers and Tools Setup  
**Status**: ✅ **CONFIRMED WORKING**

<!-- section_id: "8542c3db-8735-4625-bad0-53c0687c911e" -->
## Problem

Playwright MCP tools were configured in `mcp.json` but not available to AI agents. Tools showed as "22 tools enabled" in Cursor Settings but were not accessible.

<!-- section_id: "4626c794-ef9e-4729-b352-745e498b0195" -->
## Root Cause

**MCP servers must be enabled in Cursor Settings UI**, not just configured in `mcp.json`. Configuration in the JSON file is not sufficient - servers must be toggled ON in the Cursor IDE Settings interface.

<!-- section_id: "66893759-8a39-4049-81c7-55d9b6e8022e" -->
## Solution Steps

<!-- section_id: "0b4e5d1a-a0d8-4a81-b4b8-0326db954eca" -->
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

<!-- section_id: "32be6334-3e2c-4ba4-b4f8-d73ae7221c4d" -->
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

<!-- section_id: "c1e358e5-7490-41f4-9509-9caafeaf11ba" -->
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

<!-- section_id: "501dd7a8-4e1e-442f-93de-0dec782e0543" -->
### Step 4: Verify Tools Are Available ✅

**Test**:
- Tool: `mcp_playwright_browser_navigate("https://www.aleks.com")`
- Result: ✅ **SUCCESS** - Successfully navigated to page
- Status: 22 Playwright tools available and working

<!-- section_id: "d8cee10a-dc46-4a7e-a7d2-984510cc7c64" -->
## Complete Working Configuration

<!-- section_id: "c543e8ac-fde5-4714-9a34-2ce59acadfc1" -->
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

<!-- section_id: "cffa39d3-f7e3-4f99-8beb-8fbd79424678" -->
### Cursor Settings UI
- **Location**: Cursor Settings → Tools & MCP → Installed MCP Servers
- **Status**: Playwright server toggle must be **ON** (green)
- **Expected**: "22 tools enabled" status

<!-- section_id: "1de5a693-dd65-4c99-9d87-d4a482e49894" -->
## What We Tried (That Didn't Work Alone)

1. ✅ Configured in mcp.json - Required but not sufficient
2. ✅ Added environment variables - Required but not sufficient
3. ✅ Used full npx paths - Helpful but not sufficient
4. ✅ Reordered servers - Didn't help
5. ✅ Checked for duplicates - None found
6. ✅ Created project-specific config - Didn't help
7. ✅ Disabled unused MCP servers - **May have helped** (freed up capacity)
8. ❌ **Missing**: Enable in Cursor Settings UI - **This was the critical step!**

<!-- section_id: "9365acaf-b517-458f-b994-caa90684edc3" -->
## Complete Solution (All Steps)

**To get Playwright MCP tools working, you need:**

1. ✅ **Configure in mcp.json** - Full paths, environment variables
2. ✅ **Disable unused MCP servers** - Free up capacity (if Cursor warns about limits)
3. ✅ **Enable Playwright server in Cursor Settings UI** - **CRITICAL**
4. ✅ **Verify tools are available** - Test navigation

**All steps may be necessary for success.**

<!-- section_id: "b587a1c1-9593-474d-87ae-d60b618b516a" -->
## Key Learnings

<!-- section_id: "5bd46c0f-6e5c-42e4-bbf9-1b1ed9ac1447" -->
### Critical Discovery #1: UI Enablement Required
**MCP servers must be enabled in Cursor Settings UI**, not just configured in mcp.json.

<!-- section_id: "5b386248-9b19-4677-ac26-936e85ff76a0" -->
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

<!-- section_id: "8dcf0027-46dd-4111-b225-748c079b2b6b" -->
### Configuration Requirements
1. **mcp.json configuration** - Required for server setup
2. **Environment variables** - Required for browser detection
3. **Full paths** - Recommended for NVM setups
4. **UI enablement** - **CRITICAL** - Required to expose tools

<!-- section_id: "d4659325-bcb4-4ec8-bb8b-83d1e70c0ec0" -->
### Tool Availability
- After enabling in UI: Tools immediately available
- Before enabling in UI: Tools configured but not accessible
- After restart: May need to re-enable in UI (enablement may not persist)

<!-- section_id: "b7bed1e3-1589-45fc-81ad-505a5f5b136e" -->
## Testing Results

<!-- section_id: "8bfb1e32-885b-4e90-9e6f-b90537d68a27" -->
### Successful Tests
- ✅ Navigation: `mcp_playwright_browser_navigate("https://www.aleks.com")`
- ✅ Page loading: Full page content retrieved
- ✅ Tool availability: 22 Playwright tools accessible

<!-- section_id: "b4ab3d81-b5ab-4597-b6c7-63845b1993f8" -->
### Test URLs
- ALEKS: `https://www.aleks.com`
- BYU-Idaho Canvas: `https://byui.instructure.com/courses/353368/grades`

<!-- section_id: "e6ddd0b7-0b39-4c53-ac44-c8b49125b3b2" -->
## Troubleshooting

<!-- section_id: "84b55f26-cbb2-4f40-b2f0-ca294a5001be" -->
### Tools Not Available After Configuration
1. Check Cursor Settings → Tools & MCP
2. Verify server is enabled (green toggle)
3. If disabled, toggle ON
4. Wait for "X tools enabled" status

<!-- section_id: "72685af8-fffa-47b3-9838-dc3101ae0941" -->
### Tools Not Available After Restart
1. Check if server is still enabled in UI
2. Re-enable if needed
3. Enablement may not persist across restarts

<!-- section_id: "3af54642-0b38-4e0d-8946-fd638363c7c1" -->
### Cursor Warning About Too Many MCP Servers/Tools
1. Go to Cursor Settings → Tools & MCP
2. Review all enabled servers
3. Disable servers you're not actively using
4. Try enabling the server you need again
5. This may free up capacity for new tools

<!-- section_id: "14ecd2a1-f947-4ab3-989a-6de71eed1557" -->
### Browser Detection Issues
1. Verify `PLAYWRIGHT_BROWSERS_PATH` is set correctly
2. Check browser installation: `ls ~/.cache/ms-playwright/chromium-*/`
3. Use full npx path if using NVM

<!-- section_id: "b2f8f541-c629-4998-bf66-ad93b687e078" -->
## Related Documentation

- [MCP Tool Exposure Solutions](./MCP_TOOL_EXPOSURE_SOLUTIONS.md) - All solutions
- [MCP Tool Exposure Testing Log](./MCP_TOOL_EXPOSURE_TESTING_LOG.md) - Testing journey
- [MCP Fix Attempts Log](./MCP_FIX_ATTEMPTS_LOG.md) - All attempts
- [Browser Environment Variable Fix](./BROWSER_ENV_VAR_FIX.md) - Environment variables
- [MCP Configuration Guide](./MCP_CONFIGURATION_GUIDE.md) - General configuration

<!-- section_id: "49795acc-b4ee-4590-95a0-0d9e52158a12" -->
## Changelog

<!-- section_id: "27dc7c0a-e354-4ce1-8cba-98794712e129" -->
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

