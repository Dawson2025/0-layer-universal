# Playwright MCP Working Solution

**Date**: 2025-12-05  
**Location**: Universal Layer → MCP Servers and Tools Setup  
**Status**: ✅ **CONFIRMED WORKING**

## Problem

Playwright MCP tools were configured in `mcp.json` but not available to AI agents. Tools showed as "22 tools enabled" in Cursor Settings but were not accessible.

## Root Cause

**MCP servers must be enabled in Cursor Settings UI**, not just configured in `mcp.json`. Configuration in the JSON file is not sufficient - servers must be toggled ON in the Cursor IDE Settings interface.

## Solution Steps

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

### Step 2: Enable MCP Server in Cursor Settings UI ⚠️ **CRITICAL**

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

### Step 3: Verify Tools Are Available ✅

**Test**:
- Tool: `mcp_playwright_browser_navigate("https://www.aleks.com")`
- Result: ✅ **SUCCESS** - Successfully navigated to page
- Status: 22 Playwright tools available and working

## Complete Working Configuration

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

### Cursor Settings UI
- **Location**: Cursor Settings → Tools & MCP → Installed MCP Servers
- **Status**: Playwright server toggle must be **ON** (green)
- **Expected**: "22 tools enabled" status

## What We Tried (That Didn't Work Alone)

1. ✅ Configured in mcp.json - Required but not sufficient
2. ✅ Added environment variables - Required but not sufficient
3. ✅ Used full npx paths - Helpful but not sufficient
4. ✅ Reordered servers - Didn't help
5. ✅ Checked for duplicates - None found
6. ✅ Created project-specific config - Didn't help
7. ❌ **Missing**: Enable in Cursor Settings UI - **This was the critical step!**

## Key Learnings

### Critical Discovery
**MCP servers must be enabled in Cursor Settings UI**, not just configured in mcp.json.

### Configuration Requirements
1. **mcp.json configuration** - Required for server setup
2. **Environment variables** - Required for browser detection
3. **Full paths** - Recommended for NVM setups
4. **UI enablement** - **CRITICAL** - Required to expose tools

### Tool Availability
- After enabling in UI: Tools immediately available
- Before enabling in UI: Tools configured but not accessible
- After restart: May need to re-enable in UI (enablement may not persist)

## Testing Results

### Successful Tests
- ✅ Navigation: `mcp_playwright_browser_navigate("https://www.aleks.com")`
- ✅ Page loading: Full page content retrieved
- ✅ Tool availability: 22 Playwright tools accessible

### Test URLs
- ALEKS: `https://www.aleks.com`
- BYU-Idaho Canvas: `https://byui.instructure.com/courses/353368/grades`

## Troubleshooting

### Tools Not Available After Configuration
1. Check Cursor Settings → Tools & MCP
2. Verify server is enabled (green toggle)
3. If disabled, toggle ON
4. Wait for "X tools enabled" status

### Tools Not Available After Restart
1. Check if server is still enabled in UI
2. Re-enable if needed
3. Enablement may not persist across restarts

### Browser Detection Issues
1. Verify `PLAYWRIGHT_BROWSERS_PATH` is set correctly
2. Check browser installation: `ls ~/.cache/ms-playwright/chromium-*/`
3. Use full npx path if using NVM

## Related Documentation

- [MCP Tool Exposure Solutions](./MCP_TOOL_EXPOSURE_SOLUTIONS.md) - All solutions
- [MCP Tool Exposure Testing Log](./MCP_TOOL_EXPOSURE_TESTING_LOG.md) - Testing journey
- [MCP Fix Attempts Log](./MCP_FIX_ATTEMPTS_LOG.md) - All attempts
- [Browser Environment Variable Fix](./BROWSER_ENV_VAR_FIX.md) - Environment variables
- [MCP Configuration Guide](./MCP_CONFIGURATION_GUIDE.md) - General configuration

## Changelog

### 2025-12-05
- Created comprehensive working solution document
- Documented critical UI enablement step
- Added complete configuration examples
- Documented all troubleshooting steps
- Confirmed solution works with successful tests

---

**Key Takeaway**: Configuration in `mcp.json` + **Enablement in Cursor Settings UI** = Working Playwright MCP tools!

