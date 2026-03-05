---
resource_id: "1d099c5f-14bb-47ea-8f65-a8bf83b2becd"
resource_type: "document"
resource_name: "MCP_FIX_ATTEMPTS_LOG"
---
# MCP Tool Exposure Fix Attempts Log

**Date**: 2025-12-05  
**Location**: Universal Layer → MCP Servers and Tools Setup  
**Status**: Active testing of all solutions

<!-- section_id: "6e132353-9656-4b39-bf21-cc0412c748e3" -->
## Fix Attempts Timeline

<!-- section_id: "8765af02-1ed0-4296-984e-2d12e460d096" -->
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

<!-- section_id: "0edbc5e1-8ff5-4428-8856-4a25367ad39b" -->
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

<!-- section_id: "664ab577-74be-4792-b779-9d4a785edf85" -->
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

<!-- section_id: "e0ff66ab-4f80-4d4d-b351-fce0f207c589" -->
### Attempt 4: Create Project-Specific Config ✅
**Solution**: Solution 11 - Use project-specific `.cursor/mcp.json`  
**Time**: < 1 minute  
**Action**: Created `.cursor/mcp.json` in project directory (`/home/dawson/code/0_layer_universal/.cursor/mcp.json`)  
**Result**: ✅ **Project-specific config created** - Copied from global config

**Status**: ✅ Completed - CLI may prefer project-specific configs

---

<!-- section_id: "70393d75-5208-409d-ba95-b1be85e42dbf" -->
## Next Steps (Require Cursor Restart)

<!-- section_id: "09d38a82-a620-4ecc-824d-5dce7bedd8e2" -->
### Immediate Testing Needed:
1. **Restart Cursor IDE** - Required to pick up configuration changes
2. **Test Playwright Tools** - Check if `mcp_playwright_*` tools work
3. **Test Browser Tools** - Check if `mcp_browser_*` tools work (already working, verify still works)
4. **Check Tool Exposure** - Verify tools are available in available tools list

<!-- section_id: "2f1ad91d-5a68-4f81-97e8-868ba59c4997" -->
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

<!-- section_id: "8215adcf-70d9-4368-8b74-5ffc63eff6ec" -->
### Medium Effort Fixes:
1. **Update Cursor** (Solution 2)
   - Check for updates
   - Update to latest version
   - May have bug fixes

2. **Check Cursor Version** (Solution 21)
   - Verify version compatibility
   - Check release notes for MCP fixes

<!-- section_id: "52ebc49a-e966-4541-bcea-33698de73287" -->
## Configuration Changes Summary

<!-- section_id: "318f78ee-bbdb-42cd-a337-28f5034c84f9" -->
### Current Config State:
- ✅ No duplicate entries
- ✅ Playwright and browser servers at top
- ✅ Full npx paths for playwright and browser
- ✅ Project-specific config created
- ✅ Environment variables set (PLAYWRIGHT_BROWSERS_PATH, HOME)

<!-- section_id: "d7c75d0f-1ba2-4d65-8a1e-a6686f4115e5" -->
### Files Modified:
- `~/.cursor/mcp.json` - Reordered, full paths added
- `/home/dawson/code/0_layer_universal/.cursor/mcp.json` - Project-specific config created
- `~/.cursor/mcp.json.backup.*` - Backup created

<!-- section_id: "465e1710-1e7b-48fb-8057-f83d48763e05" -->
## Expected Results After Restart

<!-- section_id: "8a6dff6f-dda2-416d-a290-3648dfdb10a1" -->
### If Fixes Work:
- Playwright MCP tools (`mcp_playwright_*`) should be available
- Browser MCP tools (`mcp_browser_*`) should continue working
- Tools should appear in available tools list
- Browser detection should work for Playwright tools

<!-- section_id: "50d06c8e-c61f-4b7d-a6e6-e26c73be0e08" -->
### If Fixes Don't Work:
- Continue with remaining solutions
- Try delete/regenerate mcp.json
- Try disabling internal browser automation
- Check for Cursor updates

<!-- section_id: "651a4cce-84be-4890-8104-2d4735a28457" -->
## Related Documentation

- [MCP Tool Exposure Solutions](./MCP_TOOL_EXPOSURE_SOLUTIONS.md) - All solutions
- [MCP Tool Exposure Testing Log](./MCP_TOOL_EXPOSURE_TESTING_LOG.md) - Previous testing
- [Browser Environment Variable Fix](./BROWSER_ENV_VAR_FIX.md) - Environment variable solution

---

<!-- section_id: "94d2a794-8b9b-40ad-9cf6-8698dc5cd07e" -->
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

<!-- section_id: "8c93dd8c-4e66-4041-a5a3-4e4eaebcf11f" -->
### Attempt 6: Fix Config File Location (In Progress)
**Solution**: Update the actual config file that Cursor reads  
**Time**: < 2 minutes  
**Action**: Check `~/.config/mcp/mcp.json` (actual config file)  
**Result**: Need to apply same fixes to actual config file

**Status**: 🔄 In Progress

---

<!-- section_id: "f90c076b-2e1f-478a-81de-41ed5630b3e8" -->
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

<!-- section_id: "0c4e2768-b68b-41e9-bc6b-8c1f693cb895" -->
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

<!-- section_id: "d24440bd-28fa-46f9-ac92-1238d8c8c39a" -->
## Summary of All Attempts

<!-- section_id: "60b4d3d0-b9b1-4645-98cb-d91b8e90f34a" -->
### ✅ Completed:
1. Checked for duplicates - None found
2. Reordered MCP servers - Moved playwright/browser to top
3. Added full npx paths - For playwright and browser
4. Created project-specific config
5. Deleted and attempted regeneration
6. Restored working config

<!-- section_id: "4a82e9b7-94da-4dc0-aa8a-39b7f7b2b677" -->
### ⚠️ Current Status:
- Config restored to working state
- MCP tools not currently available (may need login or restart)
- Need to verify user is logged into Cursor IDE

<!-- section_id: "c05928fe-c853-456c-8716-aa6b74760b0b" -->
### 🔄 Next Steps:
1. **Verify login status** - User must be logged into Cursor IDE
2. **Test tool availability** - Check if tools appear after ensuring login
3. **Try conservative fixes** - One at a time, test after each
4. **Check Cursor Settings** - Verify MCP servers are enabled in UI

---

<!-- section_id: "edd2c945-85dc-411c-a067-ac38577503f0" -->
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

<!-- section_id: "20c5d4c7-0a64-4c55-bf70-f2fc988ca3b4" -->
## Final Status

<!-- section_id: "0ec91e74-4c74-4749-a023-123c66712874" -->
### ✅ **SUCCESS**: Playwright MCP Tools Working!
- Playwright server enabled in Cursor Settings UI
- 22 tools available and working
- Navigation test successful
- Browser detection working

<!-- section_id: "4d74e17a-6de1-4ffe-8d26-6c7aea59e603" -->
### 🔄 Next Steps:
1. Enable "browser" MCP server in Cursor Settings UI (currently disabled)
2. Test browser MCP tools after enabling
3. Document that UI enablement is required

---

**Critical Discovery**: MCP servers must be **enabled in Cursor Settings UI**, not just configured in mcp.json!

---

<!-- section_id: "049c6a2c-3ebb-443b-9e0a-a2d0a77a5e6c" -->
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


