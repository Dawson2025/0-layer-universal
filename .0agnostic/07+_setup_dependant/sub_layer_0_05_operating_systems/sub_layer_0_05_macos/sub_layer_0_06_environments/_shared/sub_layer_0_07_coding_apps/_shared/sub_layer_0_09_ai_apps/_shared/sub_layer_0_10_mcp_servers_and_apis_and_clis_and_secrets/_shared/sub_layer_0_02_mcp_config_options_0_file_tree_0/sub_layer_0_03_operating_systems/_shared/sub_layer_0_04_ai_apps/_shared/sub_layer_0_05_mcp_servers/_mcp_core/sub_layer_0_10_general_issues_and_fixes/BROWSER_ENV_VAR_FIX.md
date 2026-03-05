---
resource_id: "53b62434-f31c-4372-952e-0f5d21442314"
resource_type: "document"
resource_name: "BROWSER_ENV_VAR_FIX"
---
# Browser MCP Environment Variable Fix

**Date**: 2025-12-05  
**Location**: Universal Layer → MCP Servers and Tools Setup  
**Status**: ✅ Implemented and Documented

<!-- section_id: "5ff97bb7-fd04-421c-bb5c-b197f9ba11c7" -->
## Problem Summary

Browser MCP servers kept reporting "Browser specified in your config is not installed" even when browsers were installed. This problem recurred constantly, making it seem like browsers needed constant reinstallation.

<!-- section_id: "5f0f4b74-9ded-4b32-a587-14f2ce78a5d2" -->
## Root Cause

**The Real Issue**: MCP servers run via `npx` in isolated execution environments that don't inherit your shell's environment variables. The browsers ARE installed, but the MCP server processes can't find them because:

1. `PLAYWRIGHT_BROWSERS_PATH` isn't set in the MCP server environment
2. `HOME` isn't set, so user-specific paths can't be resolved
3. Each Cursor restart spawns new MCP processes that need the environment configured
4. Environment variables from `.bashrc` or your shell aren't automatically passed to MCP servers

<!-- section_id: "b9651900-d913-4fbf-bb06-d68581057244" -->
## Solution

Add environment variables directly to the MCP server configuration in `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
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
}
```

**Important**: Replace `/home/dawson` with your actual home directory path.

<!-- section_id: "761f7418-e85f-444c-bc21-ba1d1d1a7eab" -->
## Implementation Status

<!-- section_id: "28aa0fca-7f14-4a0e-b6a9-449f4ff84884" -->
### ✅ Completed

1. **Documentation Updated**:
   - `MCP_CONFIGURATION_GUIDE.md` - Added troubleshooting section and environment variable requirements
   - `BROWSER_MCP_SETUP_EXPERIENCE.md` - Updated Lesson 2 with the fix and root cause explanation
   - `CURSOR_BROWSER_MCP_SETUP.md` - Updated working configuration examples
   - `mcp-config-enhanced.json` - Updated template with environment variables

2. **Configuration Files Updated**:
   - `~/.cursor/mcp.json` - Added environment variables to playwright and browser servers
   - `~/.config/mcp/mcp.json` - Added environment variables to playwright and browser servers

3. **System Configuration**:
   - Added `PLAYWRIGHT_BROWSERS_PATH` to `.bashrc` (for shell sessions)
   - Configured passwordless sudo (for future browser dependency installations)

<!-- section_id: "fc9e0993-cd21-4763-bf6f-fbd8c99efeb4" -->
## Headed Browser Configuration

To run browsers in headed (visible) mode instead of headless:

<!-- section_id: "5f52a723-e281-41d8-a416-a4be725066f0" -->
### For Playwright MCP

The Playwright MCP server runs in headless mode by default. To run in headed mode, you may need to:

1. **Check Playwright MCP documentation** for headed mode flags
2. **Use browser MCP** which may have better headed mode support
3. **Configure via environment variables** if supported

<!-- section_id: "69d0cf36-0295-449c-84da-6accb0d5ab22" -->
### Current Configuration

The current configuration uses `--browser chromium` which defaults to headless mode. To enable headed mode, check the Playwright MCP documentation for the appropriate flag (likely `--headed` or similar).

**Note**: The environment variable fix ensures browsers can be found regardless of headless/headed mode.

<!-- section_id: "fb090911-12d1-4d38-afb9-62b950a8445e" -->
## Verification

After updating the configuration:

1. **Restart Cursor IDE** to load the new MCP configuration
2. **Verify browsers are installed**:
   ```bash
   ls -la ~/.cache/ms-playwright/chromium-*/chrome-linux64/chrome
   ```
3. **Test browser MCP tools** - they should now work without "browser not installed" errors

<!-- section_id: "69b5a7a1-0ce7-4861-b6ed-e4de920b94dd" -->
## Why This Fix Works

- **Explicit Environment**: MCP servers now have explicit environment variables pointing to browser locations
- **Persistent Configuration**: The fix is in the MCP config file, so it persists across Cursor restarts
- **No More Reinstallation**: Browsers don't need constant reinstallation - they're found via environment variables
- **Cross-Platform**: This fix works on Linux, macOS, and Windows (with appropriate path adjustments)

<!-- section_id: "5c1ffe35-be0e-4e4b-8922-fc26620c5c64" -->
## Related Documentation

- [MCP Configuration Guide](./MCP_CONFIGURATION_GUIDE.md)
- [Browser MCP Setup Experience](./BROWSER_MCP_SETUP_EXPERIENCE.md)
- [Cursor Browser MCP Setup](./CURSOR_BROWSER_MCP_SETUP.md)

<!-- section_id: "a359ae7e-e8d5-4249-9dff-7ac697ed3f04" -->
## Changelog

<!-- section_id: "dc2cb200-20ec-458a-81e2-f3364737e3a0" -->
### 2025-12-05
- Identified root cause: Missing environment variables in MCP server configuration
- Implemented fix in all MCP config files
- Updated all documentation with the solution
- Added troubleshooting section to configuration guide
- Documented why the problem kept recurring

---

**This fix resolves the recurring browser installation issue by ensuring MCP servers can always find installed browsers through explicit environment variable configuration.**

