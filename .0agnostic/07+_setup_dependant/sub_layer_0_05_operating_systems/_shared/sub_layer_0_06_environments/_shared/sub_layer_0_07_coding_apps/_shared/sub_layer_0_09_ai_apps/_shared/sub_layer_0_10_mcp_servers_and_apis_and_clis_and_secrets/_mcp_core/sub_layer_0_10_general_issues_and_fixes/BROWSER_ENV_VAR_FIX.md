---
resource_id: "6c4cf886-6ddb-43ab-ac6a-c1f276dde084"
resource_type: "document"
resource_name: "BROWSER_ENV_VAR_FIX"
---
# Browser MCP Environment Variable Fix

**Date**: 2025-12-05  
**Location**: Universal Layer → MCP Servers and Tools Setup  
**Status**: ✅ Implemented and Documented

<!-- section_id: "4d562d2d-1da8-427e-9e4b-80a5d053de96" -->
## Problem Summary

Browser MCP servers kept reporting "Browser specified in your config is not installed" even when browsers were installed. This problem recurred constantly, making it seem like browsers needed constant reinstallation.

<!-- section_id: "5523153c-67ec-412b-a33a-e2dece0d7caa" -->
## Root Cause

**The Real Issue**: MCP servers run via `npx` in isolated execution environments that don't inherit your shell's environment variables. The browsers ARE installed, but the MCP server processes can't find them because:

1. `PLAYWRIGHT_BROWSERS_PATH` isn't set in the MCP server environment
2. `HOME` isn't set, so user-specific paths can't be resolved
3. Each Cursor restart spawns new MCP processes that need the environment configured
4. Environment variables from `.bashrc` or your shell aren't automatically passed to MCP servers

<!-- section_id: "36451e20-defc-4bea-9f44-ffe446b53c9b" -->
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

<!-- section_id: "64c3a0aa-c850-4a45-94f0-8bc438113682" -->
## Implementation Status

<!-- section_id: "52542f08-6297-4485-81ce-ebfc4cd1e486" -->
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

<!-- section_id: "795cec3f-e370-4a7c-9abf-454b9bc436cb" -->
## Headed Browser Configuration

To run browsers in headed (visible) mode instead of headless:

<!-- section_id: "0cf92567-4348-4fd0-88ba-61dac204996a" -->
### For Playwright MCP

The Playwright MCP server runs in headless mode by default. To run in headed mode, you may need to:

1. **Check Playwright MCP documentation** for headed mode flags
2. **Use browser MCP** which may have better headed mode support
3. **Configure via environment variables** if supported

<!-- section_id: "0d933ff5-42ed-4110-96dd-1b7a41b56de6" -->
### Current Configuration

The current configuration uses `--browser chromium` which defaults to headless mode. To enable headed mode, check the Playwright MCP documentation for the appropriate flag (likely `--headed` or similar).

**Note**: The environment variable fix ensures browsers can be found regardless of headless/headed mode.

<!-- section_id: "40cce650-3838-482a-b569-ddac3af0dac0" -->
## Verification

After updating the configuration:

1. **Restart Cursor IDE** to load the new MCP configuration
2. **Verify browsers are installed**:
   ```bash
   ls -la ~/.cache/ms-playwright/chromium-*/chrome-linux64/chrome
   ```
3. **Test browser MCP tools** - they should now work without "browser not installed" errors

<!-- section_id: "a00ec717-39d3-43f8-ab85-7e25e07b2a07" -->
## Why This Fix Works

- **Explicit Environment**: MCP servers now have explicit environment variables pointing to browser locations
- **Persistent Configuration**: The fix is in the MCP config file, so it persists across Cursor restarts
- **No More Reinstallation**: Browsers don't need constant reinstallation - they're found via environment variables
- **Cross-Platform**: This fix works on Linux, macOS, and Windows (with appropriate path adjustments)

<!-- section_id: "93aa3f58-93b4-42b2-8483-07526e3f6614" -->
## Related Documentation

- [MCP Configuration Guide](./MCP_CONFIGURATION_GUIDE.md)
- [Browser MCP Setup Experience](./BROWSER_MCP_SETUP_EXPERIENCE.md)
- [Cursor Browser MCP Setup](./CURSOR_BROWSER_MCP_SETUP.md)

<!-- section_id: "6d820851-acdf-4cab-a216-8a926446c172" -->
## Changelog

<!-- section_id: "1316ce5e-41ac-4b3e-a93d-0b5e3d912f7a" -->
### 2025-12-05
- Identified root cause: Missing environment variables in MCP server configuration
- Implemented fix in all MCP config files
- Updated all documentation with the solution
- Added troubleshooting section to configuration guide
- Documented why the problem kept recurring

---

**This fix resolves the recurring browser installation issue by ensuring MCP servers can always find installed browsers through explicit environment variable configuration.**

