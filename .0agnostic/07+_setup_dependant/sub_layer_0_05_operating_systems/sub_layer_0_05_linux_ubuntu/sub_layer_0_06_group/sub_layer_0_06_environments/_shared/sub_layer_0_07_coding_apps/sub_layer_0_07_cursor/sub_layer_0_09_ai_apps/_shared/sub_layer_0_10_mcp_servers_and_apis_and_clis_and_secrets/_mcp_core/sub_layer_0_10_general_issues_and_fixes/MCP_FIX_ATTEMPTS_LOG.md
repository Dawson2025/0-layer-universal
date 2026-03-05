---
resource_id: "8f933c7c-6227-4240-b1ec-5b714339bf26"
resource_type: "document"
resource_name: "MCP_FIX_ATTEMPTS_LOG"
---
# MCP Tool Exposure Fix Attempts Log

**Date**: 2025-12-05  
**Location**: Universal Layer → MCP Servers and Tools Setup  
**Status**: Active testing of all solutions

<!-- section_id: "4d885dd4-6bf5-4c28-8efe-c4c74458b6c2" -->
## Fix Attempts Timeline

<!-- section_id: "37ef1b3d-546c-4997-ab11-32891edf71de" -->
### Attempt 1: Check for Duplicate Entries ✅
**Solution**: Solution 12 - Check for duplicate MCP server entries  
**Time**: < 1 minute  
**Action**: Checked `~/.cursor/mcp.json` for duplicate server names  
**Result**: ✅ **No duplicates found** - All 7 servers have unique names:
- context7
- chrome-devtools
- playwright
- browser
- web-search
- github-search
- filesystem

**Status**: ✅ Completed - Not the issue

---

<!-- section_id: "ac7d7126-3e37-41f6-bdb3-32090270e71c" -->
### Attempt 2: Reorder MCP Servers ✅
**Solution**: Solution 10 - Move problematic servers to top  
**Time**: < 2 minutes  
**Action**: Moved `playwright` and `browser` servers to the top of `mcpServers` object  
**Before**:
```json
{
  "mcpServers": {
    "context7": {...},
    "chrome-devtools": {...},
    "playwright": {...},
    "browser": {...},
    ...
  }
}
```

**After**:
```json
{
  "mcpServers": {
    "playwright": {...},
    "browser": {...},
    "context7": {...},
    "chrome-devtools": {...},
    ...
  }
}
```

**Result**: ✅ **Configuration updated** - Awaiting Cursor restart to test

**Status**: ✅ Completed - Needs testing after restart

---

<!-- section_id: "3e74eba8-566f-482e-b3c2-34c79319ea4c" -->
### Attempt 3: Use Full Node.js/npx Paths ✅
**Solution**: Solution 5 - Use full paths instead of `npx` command  
**Time**: < 2 minutes  
**Action**: Updated `playwright` and `browser` servers to use full npx path:
- Changed from: `"command": "npx"`
- Changed to: `"command": "/home/dawson/.nvm/versions/node/v22.20.0/bin/npx"`

**Why**: NVM-managed Node.js may not be in PATH when MCP servers start

**Result**: ✅ **Configuration updated** - Full paths added for playwright and browser servers

**Status**: ✅ Completed - Needs testing after restart

---

<!-- section_id: "1bae838e-e456-4bcd-8ac6-5f7587a842d7" -->
### Attempt 4: Create Project-Specific Config ✅
**Solution**: Solution 11 - Use project-specific `.cursor/mcp.json`  
**Time**: < 1 minute  
**Action**: Created `.cursor/mcp.json` in project directory (`/home/dawson/code/0_layer_universal/.cursor/mcp.json`)  
**Result**: ✅ **Project-specific config created** - Copied from global config

**Status**: ✅ Completed - CLI may prefer project-specific configs

---

<!-- section_id: "06e75851-d53e-4f93-b3bd-48d3b3ea2688" -->
## Next Steps (Require Cursor Restart)

<!-- section_id: "fbd5036f-3c7c-4350-8e71-f2c7ec6cc560" -->
### Immediate Testing Needed:
1. **Restart Cursor IDE** - Required to pick up configuration changes
2. **Test Playwright Tools** - Check if `mcp_playwright_*` tools work
3. **Test Browser Tools** - Check if `mcp_browser_*` tools work (already working, verify still works)
4. **Check Tool Exposure** - Verify tools are available in available tools list

<!-- section_id: "0285f056-d0ad-4f7c-8572-6fe25bef00b1" -->
### Remaining Quick Fixes to Try:
1. **Disable Internal Browser Automation** (Solution 9)
   - Go to Cursor Settings → Tools & MCP → Browser Automation
   - Disable if possible
   - Prevents interference with MCP browser tools

2. **Delete and Regenerate mcp.json** (Solution 8)
   - Backup current config (already done)
   - Delete `~/.cursor/mcp.json`
   - Let Cursor regenerate it
   - Re-add MCP servers
   - **User-reported success** - Worth trying

<!-- section_id: "61a0e9d8-d858-48fa-94ca-00631ce33697" -->
### Medium Effort Fixes:
1. **Update Cursor** (Solution 2)
   - Check for updates
   - Update to latest version
   - May have bug fixes

2. **Check Cursor Version** (Solution 21)
   - Verify version compatibility
   - Check release notes for MCP fixes

<!-- section_id: "0b88d092-182f-4459-8e18-91c1522ef983" -->
## Configuration Changes Summary

<!-- section_id: "b47dbba4-4b7e-410a-80a8-da7bfd599598" -->
### Current Config State:
- ✅ No duplicate entries
- ✅ Playwright and browser servers at top
- ✅ Full npx paths for playwright and browser
- ✅ Project-specific config created
- ✅ Environment variables set (PLAYWRIGHT_BROWSERS_PATH, HOME)

<!-- section_id: "af510dbd-f250-4690-9635-98b0b90c1d89" -->
### Files Modified:
- `~/.cursor/mcp.json` - Reordered, full paths added
- `/home/dawson/code/0_layer_universal/.cursor/mcp.json` - Project-specific config created
- `~/.cursor/mcp.json.backup.*` - Backup created

<!-- section_id: "65f91bd9-9dd0-41c1-b4c5-c632361cf7d7" -->
## Expected Results After Restart

<!-- section_id: "05ddb1de-a85a-40ff-873d-9a8f6b61512d" -->
### If Fixes Work:
- Playwright MCP tools (`mcp_playwright_*`) should be available
- Browser MCP tools (`mcp_browser_*`) should continue working
- Tools should appear in available tools list
- Browser detection should work for Playwright tools

<!-- section_id: "6ae3898a-0de7-4fe5-a556-e4dfa7cd5cfe" -->
### If Fixes Don't Work:
- Continue with remaining solutions
- Try delete/regenerate mcp.json
- Try disabling internal browser automation
- Check for Cursor updates

<!-- section_id: "6f95bef6-0df6-47ae-a077-15bdbe3ba8f6" -->
## Related Documentation

- [MCP Tool Exposure Solutions](./MCP_TOOL_EXPOSURE_SOLUTIONS.md) - All solutions
- [MCP Tool Exposure Testing Log](./MCP_TOOL_EXPOSURE_TESTING_LOG.md) - Previous testing
- [Browser Environment Variable Fix](./BROWSER_ENV_VAR_FIX.md) - Environment variable solution

---

<!-- section_id: "24743982-db88-4911-8542-89cca9207fb4" -->
### Attempt 5: Test After Restart ❌
**Solution**: Solution 6 - Restart Cursor completely  
**Time**: User restarted Cursor  
**Action**: User restarted Cursor IDE to test configuration changes  
**Result**: ❌ **REGRESSION** - MCP tools no longer available after restart

**Issue Discovered**: 
- `~/.cursor/mcp.json` is a **symlink** to `~/.config/mcp/mcp.json`
- We edited the symlink target, but Cursor may be reading from a different location
- Need to check actual config file location

**Status**: ⚠️ **Issue Found** - Need to fix config location

---

<!-- section_id: "255c8ab9-014c-4de1-bf14-5e10288395b6" -->
### Attempt 6: Fix Config File Location (In Progress)
**Solution**: Update the actual config file that Cursor reads  
**Time**: < 2 minutes  
**Action**: Check `~/.config/mcp/mcp.json` (actual config file)  
**Result**: Need to apply same fixes to actual config file

**Status**: 🔄 In Progress

---

<!-- section_id: "bf98529b-d5bf-441e-a305-8cfd5555795d" -->
### Attempt 7: Delete and Regenerate mcp.json ✅
**Solution**: Solution 8 - Delete and let Cursor regenerate  
**Time**: < 1 minute  
**Action**: 
- Deleted `~/.config/mcp/mcp.json` (actual config file)
- Deleted `~/.cursor/mcp.json` (symlink)
- Created backup before deletion
- Cursor should regenerate config automatically

**Result**: ✅ **Config files deleted** - Awaiting Cursor to regenerate

**Status**: ✅ Completed - User needs to restart Cursor or let it regenerate

**Note**: This is a user-reported successful solution. After Cursor regenerates, we'll need to re-add MCP servers.

---

<!-- section_id: "94bfadd7-91ca-42d2-ae68-acad47a4798d" -->
### Attempt 8: Restore Working Config ✅
**Solution**: Restore config that was working before  
**Time**: < 1 minute  
**Action**: 
- Cursor didn't auto-regenerate config
- Restored from backup that had working configuration (with environment variables)
- Recreated symlink

**Result**: ✅ **Config restored** - Back to state before our changes

**Status**: ✅ Completed - Ready to test

**Note**: We're back to the configuration that had browser tools working earlier. The issue might be that user needs to be logged in, or we need to try fixes more conservatively.

---

<!-- section_id: "d5342156-57a7-4dd6-824f-ae84e3f17e75" -->
## Summary of All Attempts

<!-- section_id: "32f1dfc9-45db-4e19-97ca-42babc4946ad" -->
### ✅ Completed:
1. Checked for duplicates - None found
2. Reordered MCP servers - Moved playwright/browser to top
3. Added full npx paths - For playwright and browser
4. Created project-specific config
5. Deleted and attempted regeneration
6. Restored working config

<!-- section_id: "c1379c2a-3888-4b6f-91b6-cdbde026e9a0" -->
### ⚠️ Current Status:
- Config restored to working state
- MCP tools not currently available (may need login or restart)
- Need to verify user is logged into Cursor IDE

<!-- section_id: "69a04e98-4a17-4d9e-8b7c-d2c9a63e1277" -->
### 🔄 Next Steps:
1. **Verify login status** - User must be logged into Cursor IDE
2. **Test tool availability** - Check if tools appear after ensuring login
3. **Try conservative fixes** - One at a time, test after each
4. **Check Cursor Settings** - Verify MCP servers are enabled in UI

---

<!-- section_id: "52ed7f8b-462b-4b52-9df0-b93f200f5e76" -->
### Attempt 9: Enable MCP Servers in Cursor Settings UI ✅ **SUCCESS!**
**Solution**: Enable MCP servers via Cursor Settings UI  
**Time**: < 1 minute  
**Action**: User enabled "playwright" MCP server in Cursor Settings → Tools & MCP  
**Result**: ✅ **SUCCESS!** - Playwright MCP tools now working!

**Test Result**:
- Tool: `mcp_playwright_browser_navigate("https://www.google.com")`
- Result: ✅ **SUCCESS** - Successfully navigated to Google
- Page loaded with full content and snapshot
- **22 tools enabled** for Playwright server

**Key Finding**: 
- **MCP servers must be ENABLED in Cursor Settings UI**, not just configured in mcp.json
- Configuration in mcp.json is not enough - servers need to be toggled ON in the UI
- This is the critical step that was missing!

**Status**: ✅ **BREAKTHROUGH** - Playwright tools working!

---

<!-- section_id: "04d631bd-d97a-4881-84af-35bee354cc33" -->
## Final Status

<!-- section_id: "ea2b3d56-00c5-4df9-9a38-c5feef3a4c42" -->
### ✅ **SUCCESS**: Playwright MCP Tools Working!
- Playwright server enabled in Cursor Settings UI
- 22 tools available and working
- Navigation test successful
- Browser detection working

<!-- section_id: "bcc4bbfe-9cae-4ae2-b441-670e7b241b05" -->
### 🔄 Next Steps:
1. Enable "browser" MCP server in Cursor Settings UI (currently disabled)
2. Test browser MCP tools after enabling
3. Document that UI enablement is required

---

**Critical Discovery**: MCP servers must be **enabled in Cursor Settings UI**, not just configured in mcp.json!

---

<!-- section_id: "d473946c-c9ac-4a79-abbf-c08c9b4aac1d" -->
### Attempt 10: Test After Second Restart ❌
**Solution**: Test Playwright tools after user restarted Cursor again  
**Time**: < 1 minute  
**Action**: Attempted to use `mcp_playwright_browser_navigate` after restart  
**Result**: ❌ **Tools not available again** - Playwright MCP tools not in available tools list

**Issue**: 
- After restart, Playwright server may have been disabled again
- Tools were working before restart, but not after
- Suggests MCP server enablement may not persist across restarts

**Status**: ⚠️ **Issue Found** - Need to re-enable in UI or investigate persistence

**Next Steps**:
1. Check Cursor Settings → Tools & MCP to see if Playwright is still enabled
2. If disabled, re-enable it
3. Investigate why enablement doesn't persist across restarts


