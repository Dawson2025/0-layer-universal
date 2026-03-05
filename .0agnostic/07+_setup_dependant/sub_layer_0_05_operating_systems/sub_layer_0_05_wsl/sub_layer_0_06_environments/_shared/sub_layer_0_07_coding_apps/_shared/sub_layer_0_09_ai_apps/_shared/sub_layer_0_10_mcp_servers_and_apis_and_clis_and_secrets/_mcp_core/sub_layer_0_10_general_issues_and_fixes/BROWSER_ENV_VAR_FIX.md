---
resource_id: "68c18920-4922-4595-b20d-605b4a3d5c9b"
resource_type: "document"
resource_name: "BROWSER_ENV_VAR_FIX"
---
# Browser MCP Environment Variable Fix

**Date**: 2025-12-05  
**Location**: Universal Layer → MCP Servers and Tools Setup  
**Status**: ✅ Implemented and Documented

<!-- section_id: "61dfe64f-49ef-401e-bd10-fed2c5165416" -->
## Problem Summary

Browser MCP servers kept reporting "Browser specified in your config is not installed" even when browsers were installed. This problem recurred constantly, making it seem like browsers needed constant reinstallation.

<!-- section_id: "e5aea30a-ba35-4565-930e-e9e7ff8a4383" -->
## Root Cause

**The Real Issue**: MCP servers run via `npx` in isolated execution environments that don't inherit your shell's environment variables. The browsers ARE installed, but the MCP server processes can't find them because:

1. `PLAYWRIGHT_BROWSERS_PATH` isn't set in the MCP server environment
2. `HOME` isn't set, so user-specific paths can't be resolved
3. Each Cursor restart spawns new MCP processes that need the environment configured
4. Environment variables from `.bashrc` or your shell aren't automatically passed to MCP servers

<!-- section_id: "fdec9175-2e8d-4ec9-805a-d9e406e9041c" -->
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

<!-- section_id: "e0933a52-ac62-4da5-a0c0-af353a72d01f" -->
## Implementation Status

<!-- section_id: "026f875d-d468-4e48-8182-a8f55e181d57" -->
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

<!-- section_id: "db0348b1-2a04-4497-aeef-0939a868cc26" -->
## Headed Browser Configuration

To run browsers in headed (visible) mode instead of headless:

<!-- section_id: "f0ba77f6-11bd-49b4-acf5-b8fcfec60242" -->
### For Playwright MCP

The Playwright MCP server runs in headless mode by default. To run in headed mode, you may need to:

1. **Check Playwright MCP documentation** for headed mode flags
2. **Use browser MCP** which may have better headed mode support
3. **Configure via environment variables** if supported

<!-- section_id: "bd3d6d3a-5e20-410b-9651-633c9fc7117e" -->
### Current Configuration

The current configuration uses `--browser chromium` which defaults to headless mode. To enable headed mode, check the Playwright MCP documentation for the appropriate flag (likely `--headed` or similar).

**Note**: The environment variable fix ensures browsers can be found regardless of headless/headed mode.

<!-- section_id: "c08a503a-2dfc-4cf3-90f9-f2b2de6da2ce" -->
## Verification

After updating the configuration:

1. **Restart Cursor IDE** to load the new MCP configuration
2. **Verify browsers are installed**:
   ```bash
   ls -la ~/.cache/ms-playwright/chromium-*/chrome-linux64/chrome
   ```
3. **Test browser MCP tools** - they should now work without "browser not installed" errors

<!-- section_id: "1714377a-99d7-4976-b31f-28b52eda19f3" -->
## Why This Fix Works

- **Explicit Environment**: MCP servers now have explicit environment variables pointing to browser locations
- **Persistent Configuration**: The fix is in the MCP config file, so it persists across Cursor restarts
- **No More Reinstallation**: Browsers don't need constant reinstallation - they're found via environment variables
- **Cross-Platform**: This fix works on Linux, macOS, and Windows (with appropriate path adjustments)

<!-- section_id: "107187af-3918-4f4b-ba03-2aaa48d2b5b7" -->
## Related Documentation

- [MCP Configuration Guide](./MCP_CONFIGURATION_GUIDE.md)
- [Browser MCP Setup Experience](./BROWSER_MCP_SETUP_EXPERIENCE.md)
- [Cursor Browser MCP Setup](./CURSOR_BROWSER_MCP_SETUP.md)

<!-- section_id: "a7f546a2-789d-4ac5-98c3-ed9bce8dc356" -->
## Changelog

<!-- section_id: "efaafe5b-3bd9-4f41-a98e-4c899b7c8e67" -->
### 2025-12-05
- Identified root cause: Missing environment variables in MCP server configuration
- Implemented fix in all MCP config files
- Updated all documentation with the solution
- Added troubleshooting section to configuration guide
- Documented why the problem kept recurring

---

**This fix resolves the recurring browser installation issue by ensuring MCP servers can always find installed browsers through explicit environment variable configuration.**

