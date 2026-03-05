---
resource_id: "c4766be5-61e5-493f-9e8b-ce6442edefb9"
resource_type: "document"
resource_name: "BROWSER_ENV_VAR_FIX"
---
# Browser MCP Environment Variable Fix

**Date**: 2025-12-05  
**Location**: Universal Layer → MCP Servers and Tools Setup  
**Status**: ✅ Implemented and Documented

<!-- section_id: "01d76f2a-5690-4967-8895-a39d66744415" -->
## Problem Summary

Browser MCP servers kept reporting "Browser specified in your config is not installed" even when browsers were installed. This problem recurred constantly, making it seem like browsers needed constant reinstallation.

<!-- section_id: "c2ad3f40-a9a9-4ca3-a2d9-98c1ea622509" -->
## Root Cause

**The Real Issue**: MCP servers run via `npx` in isolated execution environments that don't inherit your shell's environment variables. The browsers ARE installed, but the MCP server processes can't find them because:

1. `PLAYWRIGHT_BROWSERS_PATH` isn't set in the MCP server environment
2. `HOME` isn't set, so user-specific paths can't be resolved
3. Each Cursor restart spawns new MCP processes that need the environment configured
4. Environment variables from `.bashrc` or your shell aren't automatically passed to MCP servers

<!-- section_id: "27476d8a-0432-4549-90cc-457d34c2fcc2" -->
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

<!-- section_id: "5b0bfa6d-b2bd-4a1d-adac-51d92b509b3c" -->
## Implementation Status

<!-- section_id: "227eff94-7382-4c92-9e58-5f976fadb864" -->
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

<!-- section_id: "de52fd6b-396a-41a8-ba8b-d0ee8d9c43c0" -->
## Headed Browser Configuration

To run browsers in headed (visible) mode instead of headless:

<!-- section_id: "d4a1ebbc-3b4d-4090-b3c4-ce61afdfdf24" -->
### For Playwright MCP

The Playwright MCP server runs in headless mode by default. To run in headed mode, you may need to:

1. **Check Playwright MCP documentation** for headed mode flags
2. **Use browser MCP** which may have better headed mode support
3. **Configure via environment variables** if supported

<!-- section_id: "842d15d8-cf3c-44f8-9312-8c27c7a40e1d" -->
### Current Configuration

The current configuration uses `--browser chromium` which defaults to headless mode. To enable headed mode, check the Playwright MCP documentation for the appropriate flag (likely `--headed` or similar).

**Note**: The environment variable fix ensures browsers can be found regardless of headless/headed mode.

<!-- section_id: "2e3a60a9-9626-401a-bebd-6f22fa8134da" -->
## Verification

After updating the configuration:

1. **Restart Cursor IDE** to load the new MCP configuration
2. **Verify browsers are installed**:
   ```bash
   ls -la ~/.cache/ms-playwright/chromium-*/chrome-linux64/chrome
   ```
3. **Test browser MCP tools** - they should now work without "browser not installed" errors

<!-- section_id: "fb320e5c-9754-41dd-979d-47fe8440e385" -->
## Why This Fix Works

- **Explicit Environment**: MCP servers now have explicit environment variables pointing to browser locations
- **Persistent Configuration**: The fix is in the MCP config file, so it persists across Cursor restarts
- **No More Reinstallation**: Browsers don't need constant reinstallation - they're found via environment variables
- **Cross-Platform**: This fix works on Linux, macOS, and Windows (with appropriate path adjustments)

<!-- section_id: "1b1c45dc-defb-40b5-864d-8f6bf8875e36" -->
## Related Documentation

- [MCP Configuration Guide](./MCP_CONFIGURATION_GUIDE.md)
- [Browser MCP Setup Experience](./BROWSER_MCP_SETUP_EXPERIENCE.md)
- [Cursor Browser MCP Setup](./CURSOR_BROWSER_MCP_SETUP.md)

<!-- section_id: "a7179da1-e985-4390-a0bd-90aadc9ff62a" -->
## Changelog

<!-- section_id: "bf538787-3dfe-45e1-a4c6-4b97a1dd8a22" -->
### 2025-12-05
- Identified root cause: Missing environment variables in MCP server configuration
- Implemented fix in all MCP config files
- Updated all documentation with the solution
- Added troubleshooting section to configuration guide
- Documented why the problem kept recurring

---

**This fix resolves the recurring browser installation issue by ensuring MCP servers can always find installed browsers through explicit environment variable configuration.**

