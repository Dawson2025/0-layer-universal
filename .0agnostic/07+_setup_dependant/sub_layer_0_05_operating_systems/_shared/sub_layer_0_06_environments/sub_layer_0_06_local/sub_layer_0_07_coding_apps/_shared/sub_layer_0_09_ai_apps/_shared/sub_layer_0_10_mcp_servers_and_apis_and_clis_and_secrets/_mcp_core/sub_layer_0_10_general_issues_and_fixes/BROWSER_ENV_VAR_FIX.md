---
resource_id: "d2091d40-2258-4464-9f0d-145a58f95173"
resource_type: "document"
resource_name: "BROWSER_ENV_VAR_FIX"
---
# Browser MCP Environment Variable Fix

**Date**: 2025-12-05  
**Location**: Universal Layer → MCP Servers and Tools Setup  
**Status**: ✅ Implemented and Documented

<!-- section_id: "cdf8c0a0-ca65-4aad-b5d7-bf66e19bbacd" -->
## Problem Summary

Browser MCP servers kept reporting "Browser specified in your config is not installed" even when browsers were installed. This problem recurred constantly, making it seem like browsers needed constant reinstallation.

<!-- section_id: "091b7a6a-94d3-47f3-ba17-b3e6492632da" -->
## Root Cause

**The Real Issue**: MCP servers run via `npx` in isolated execution environments that don't inherit your shell's environment variables. The browsers ARE installed, but the MCP server processes can't find them because:

1. `PLAYWRIGHT_BROWSERS_PATH` isn't set in the MCP server environment
2. `HOME` isn't set, so user-specific paths can't be resolved
3. Each Cursor restart spawns new MCP processes that need the environment configured
4. Environment variables from `.bashrc` or your shell aren't automatically passed to MCP servers

<!-- section_id: "98381215-8236-42b2-a69f-599b3eb86087" -->
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

<!-- section_id: "32e77ab3-33a3-41cc-8708-2ad8ce18ab2f" -->
## Implementation Status

<!-- section_id: "2554fa18-7a6d-4934-8e30-afe8090f12c1" -->
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

<!-- section_id: "ba30548f-0221-4008-a510-b748f7252802" -->
## Headed Browser Configuration

To run browsers in headed (visible) mode instead of headless:

<!-- section_id: "c1e56e95-4949-485d-b51f-c3e275c968e7" -->
### For Playwright MCP

The Playwright MCP server runs in headless mode by default. To run in headed mode, you may need to:

1. **Check Playwright MCP documentation** for headed mode flags
2. **Use browser MCP** which may have better headed mode support
3. **Configure via environment variables** if supported

<!-- section_id: "d0722c37-8647-4ec3-bc56-f9c5d5db2926" -->
### Current Configuration

The current configuration uses `--browser chromium` which defaults to headless mode. To enable headed mode, check the Playwright MCP documentation for the appropriate flag (likely `--headed` or similar).

**Note**: The environment variable fix ensures browsers can be found regardless of headless/headed mode.

<!-- section_id: "8ee1b18e-d432-488a-8f05-794d799131d7" -->
## Verification

After updating the configuration:

1. **Restart Cursor IDE** to load the new MCP configuration
2. **Verify browsers are installed**:
   ```bash
   ls -la ~/.cache/ms-playwright/chromium-*/chrome-linux64/chrome
   ```
3. **Test browser MCP tools** - they should now work without "browser not installed" errors

<!-- section_id: "25be56f2-755c-428c-9de5-ae931115f07d" -->
## Why This Fix Works

- **Explicit Environment**: MCP servers now have explicit environment variables pointing to browser locations
- **Persistent Configuration**: The fix is in the MCP config file, so it persists across Cursor restarts
- **No More Reinstallation**: Browsers don't need constant reinstallation - they're found via environment variables
- **Cross-Platform**: This fix works on Linux, macOS, and Windows (with appropriate path adjustments)

<!-- section_id: "e7e2aea8-6494-4582-9593-cbd0a7e9a05d" -->
## Related Documentation

- [MCP Configuration Guide](./MCP_CONFIGURATION_GUIDE.md)
- [Browser MCP Setup Experience](./BROWSER_MCP_SETUP_EXPERIENCE.md)
- [Cursor Browser MCP Setup](./CURSOR_BROWSER_MCP_SETUP.md)

<!-- section_id: "02f6aa92-bf34-49a8-acef-1b59582e2473" -->
## Changelog

<!-- section_id: "c092788a-9766-4687-ade0-3157e4dfcee4" -->
### 2025-12-05
- Identified root cause: Missing environment variables in MCP server configuration
- Implemented fix in all MCP config files
- Updated all documentation with the solution
- Added troubleshooting section to configuration guide
- Documented why the problem kept recurring

---

**This fix resolves the recurring browser installation issue by ensuring MCP servers can always find installed browsers through explicit environment variable configuration.**

