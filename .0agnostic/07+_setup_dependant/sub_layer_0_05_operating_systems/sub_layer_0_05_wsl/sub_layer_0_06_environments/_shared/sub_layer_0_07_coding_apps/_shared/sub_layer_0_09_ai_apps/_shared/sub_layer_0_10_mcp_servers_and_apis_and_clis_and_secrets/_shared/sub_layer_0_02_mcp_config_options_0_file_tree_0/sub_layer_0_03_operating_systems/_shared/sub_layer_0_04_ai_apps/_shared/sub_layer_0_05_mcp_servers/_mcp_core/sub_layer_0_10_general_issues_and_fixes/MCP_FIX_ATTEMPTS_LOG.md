---
resource_id: "f9cce2db-e84c-407d-8e6a-86e2445f8490"
resource_type: "document"
resource_name: "MCP_FIX_ATTEMPTS_LOG"
---
# MCP Tool Exposure Fix Attempts Log

**Date**: 2025-12-05  
**Location**: Universal Layer → MCP Servers and Tools Setup  
**Status**: Active testing of all solutions

<!-- section_id: "1340e13e-591b-4f18-b052-0c36efcadcff" -->
## Fix Attempts Timeline

<!-- section_id: "c73c75d2-6188-4c1a-8b4d-4aa16924fe9b" -->
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

<!-- section_id: "5af44e7f-5feb-46bd-8893-9971688b7894" -->
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

<!-- section_id: "58314eda-07f4-4d4c-bb6c-90213cc14bef" -->
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

<!-- section_id: "4f01cd02-d330-44a5-bb98-6912d600c059" -->
### Attempt 4: Create Project-Specific Config ✅
**Solution**: Solution 11 - Use project-specific `.cursor/mcp.json`  
**Time**: < 1 minute  
**Action**: Created `.cursor/mcp.json` in project directory (`/home/dawson/dawson-workspace/code/0_layer_universal/.cursor/mcp.json`)  
**Result**: ✅ **Project-specific config created** - Copied from global config

**Status**: ✅ Completed - CLI may prefer project-specific configs

---

<!-- section_id: "ff82af1a-2b74-46f3-ae6e-1d29d9853a9e" -->
## Next Steps (Require Cursor Restart)

<!-- section_id: "93ec98d2-2465-4b11-bd20-056b2c4b92fd" -->
### Immediate Testing Needed:
1. **Restart Cursor IDE** - Required to pick up configuration changes
2. **Test Playwright Tools** - Check if `mcp_playwright_*` tools work
3. **Test Browser Tools** - Check if `mcp_browser_*` tools work (already working, verify still works)
4. **Check Tool Exposure** - Verify tools are available in available tools list

<!-- section_id: "73371518-b7c6-4e35-a671-08ca1f782538" -->
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

<!-- section_id: "b45d78a8-5bf1-4fac-85f7-2024624d5f47" -->
### Medium Effort Fixes:
1. **Update Cursor** (Solution 2)
   - Check for updates
   - Update to latest version
   - May have bug fixes

2. **Check Cursor Version** (Solution 21)
   - Verify version compatibility
   - Check release notes for MCP fixes

<!-- section_id: "fa4ecdb7-d0ef-44a2-8108-a747f7cd83c3" -->
## Configuration Changes Summary

<!-- section_id: "78fc0dc5-3c43-41b7-95ef-6e0ac1f3d7b7" -->
### Current Config State:
- ✅ No duplicate entries
- ✅ Playwright and browser servers at top
- ✅ Full npx paths for playwright and browser
- ✅ Project-specific config created
- ✅ Environment variables set (PLAYWRIGHT_BROWSERS_PATH, HOME)

<!-- section_id: "a21951df-1aff-429d-b350-384c4795a2d5" -->
### Files Modified:
- `~/.cursor/mcp.json` - Reordered, full paths added
- `/home/dawson/dawson-workspace/code/0_layer_universal/.cursor/mcp.json` - Project-specific config created
- `~/.cursor/mcp.json.backup.*` - Backup created

<!-- section_id: "f2df3a26-b679-4b1d-b33a-47ee8f6455b8" -->
## Expected Results After Restart

<!-- section_id: "457db6ec-dca1-4dd4-a335-342726789693" -->
### If Fixes Work:
- Playwright MCP tools (`mcp_playwright_*`) should be available
- Browser MCP tools (`mcp_browser_*`) should continue working
- Tools should appear in available tools list
- Browser detection should work for Playwright tools

<!-- section_id: "e5de8182-a3bf-41c5-873c-52138542811b" -->
### If Fixes Don't Work:
- Continue with remaining solutions
- Try delete/regenerate mcp.json
- Try disabling internal browser automation
- Check for Cursor updates

<!-- section_id: "b9f0be3c-d17a-4e8b-a292-b5a82001bb90" -->
## Related Documentation

- [MCP Tool Exposure Solutions](./MCP_TOOL_EXPOSURE_SOLUTIONS.md) - All solutions
- [MCP Tool Exposure Testing Log](./MCP_TOOL_EXPOSURE_TESTING_LOG.md) - Previous testing
- [Browser Environment Variable Fix](./BROWSER_ENV_VAR_FIX.md) - Environment variable solution

---

<!-- section_id: "ecab85d1-cf85-41e6-a1dc-57115454e6aa" -->
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

<!-- section_id: "7ca2425c-a88e-449f-a1d0-876d63ae1a56" -->
### Attempt 6: Fix Config File Location (In Progress)
**Solution**: Update the actual config file that Cursor reads  
**Time**: < 2 minutes  
**Action**: Check `~/.config/mcp/mcp.json` (actual config file)  
**Result**: Need to apply same fixes to actual config file

**Status**: 🔄 In Progress

---

<!-- section_id: "61a1f90f-7f5d-4f2d-8651-9ee7527673e6" -->
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

<!-- section_id: "98d86dd6-1aea-45f1-ba8d-8ab2979f526f" -->
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

<!-- section_id: "066c05ff-ca18-4302-8e8b-b501a06ac4bf" -->
## Summary of All Attempts

<!-- section_id: "42fcd226-5c5b-4021-930e-31d3d34ef769" -->
### ✅ Completed:
1. Checked for duplicates - None found
2. Reordered MCP servers - Moved playwright/browser to top
3. Added full npx paths - For playwright and browser
4. Created project-specific config
5. Deleted and attempted regeneration
6. Restored working config

<!-- section_id: "5e8c8076-2e74-43be-b22c-1cdfba6285c2" -->
### ⚠️ Current Status:
- Config restored to working state
- MCP tools not currently available (may need login or restart)
- Need to verify user is logged into Cursor IDE

<!-- section_id: "dc9e3f06-dd4c-4a51-8f0e-d129fa266033" -->
### 🔄 Next Steps:
1. **Verify login status** - User must be logged into Cursor IDE
2. **Test tool availability** - Check if tools appear after ensuring login
3. **Try conservative fixes** - One at a time, test after each
4. **Check Cursor Settings** - Verify MCP servers are enabled in UI

---

<!-- section_id: "9078a478-e1df-4526-ac29-b0e527d4075b" -->
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

<!-- section_id: "ff5e19de-b8f3-4200-805f-2ccdde3015a7" -->
## Final Status

<!-- section_id: "baa6f8f1-3c04-42e4-9721-94420e5f869f" -->
### ✅ **SUCCESS**: Playwright MCP Tools Working!
- Playwright server enabled in Cursor Settings UI
- 22 tools available and working
- Navigation test successful
- Browser detection working

<!-- section_id: "2b2ec773-173d-487a-88b6-f394ae86c79e" -->
### 🔄 Next Steps:
1. Enable "browser" MCP server in Cursor Settings UI (currently disabled)
2. Test browser MCP tools after enabling
3. Document that UI enablement is required

---

**Critical Discovery**: MCP servers must be **enabled in Cursor Settings UI**, not just configured in mcp.json!

---

<!-- section_id: "4d566ba8-2b6b-4f3f-af16-e580a194bfd7" -->
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

---

<!-- section_id: "ddcd9374-87b6-49aa-975d-f327bcf4db36" -->
## Legacy MCP Source

# MCP Tool Exposure Fix Attempts Log

**Date**: 2025-12-05  
**Location**: Universal Layer → MCP Servers and Tools Setup  
**Status**: Active testing of all solutions

<!-- section_id: "520fc8f8-8d3a-4967-a619-3a8b8ebf92ff" -->
## Fix Attempts Timeline

<!-- section_id: "b158861b-3b27-4129-8297-620ea98cec4e" -->
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

<!-- section_id: "2e8e8ad6-13f8-462a-aa79-48da1b8c031f" -->
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

<!-- section_id: "449b29c9-bfc5-4318-a48c-a5a1889ad641" -->
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

<!-- section_id: "6ac99cf6-62af-4c95-a539-c7ec263cbc27" -->
### Attempt 4: Create Project-Specific Config ✅
**Solution**: Solution 11 - Use project-specific `.cursor/mcp.json`  
**Time**: < 1 minute  
**Action**: Created `.cursor/mcp.json` in project directory (`/home/dawson/code/0_layer_universal/.cursor/mcp.json`)  
**Result**: ✅ **Project-specific config created** - Copied from global config

**Status**: ✅ Completed - CLI may prefer project-specific configs

---

<!-- section_id: "48d99e49-6fc2-4d8b-bc91-a87049c4a728" -->
## Next Steps (Require Cursor Restart)

<!-- section_id: "695797f7-705b-41c1-a6ce-1e4d5a5f70d0" -->
### Immediate Testing Needed:
1. **Restart Cursor IDE** - Required to pick up configuration changes
2. **Test Playwright Tools** - Check if `mcp_playwright_*` tools work
3. **Test Browser Tools** - Check if `mcp_browser_*` tools work (already working, verify still works)
4. **Check Tool Exposure** - Verify tools are available in available tools list

<!-- section_id: "a06fafab-2cb0-401d-9df3-2e2148bc3271" -->
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

<!-- section_id: "0b378088-bde2-44ad-ba4a-1dad2c7cdbc6" -->
### Medium Effort Fixes:
1. **Update Cursor** (Solution 2)
   - Check for updates
   - Update to latest version
   - May have bug fixes

2. **Check Cursor Version** (Solution 21)
   - Verify version compatibility
   - Check release notes for MCP fixes

<!-- section_id: "487e3bfa-da0d-43c8-8a40-4a537bc461ad" -->
## Configuration Changes Summary

<!-- section_id: "bcd891ea-012a-48d8-86e2-796dd84d99a3" -->
### Current Config State:
- ✅ No duplicate entries
- ✅ Playwright and browser servers at top
- ✅ Full npx paths for playwright and browser
- ✅ Project-specific config created
- ✅ Environment variables set (PLAYWRIGHT_BROWSERS_PATH, HOME)

<!-- section_id: "595bdfc1-c06f-4b47-8b90-948f7fd26de6" -->
### Files Modified:
- `~/.cursor/mcp.json` - Reordered, full paths added
- `/home/dawson/code/0_layer_universal/.cursor/mcp.json` - Project-specific config created
- `~/.cursor/mcp.json.backup.*` - Backup created

<!-- section_id: "80805aab-0e5a-4a87-842f-763f21501dc8" -->
## Expected Results After Restart

<!-- section_id: "d47d7f92-cd2f-4d29-93cb-e61ea9e9ed94" -->
### If Fixes Work:
- Playwright MCP tools (`mcp_playwright_*`) should be available
- Browser MCP tools (`mcp_browser_*`) should continue working
- Tools should appear in available tools list
- Browser detection should work for Playwright tools

<!-- section_id: "ce6af48b-6faa-4899-836a-413c00e2550b" -->
### If Fixes Don't Work:
- Continue with remaining solutions
- Try delete/regenerate mcp.json
- Try disabling internal browser automation
- Check for Cursor updates

<!-- section_id: "49daa47e-dfe5-42ee-923e-eab007df867d" -->
## Related Documentation

- [MCP Tool Exposure Solutions](./MCP_TOOL_EXPOSURE_SOLUTIONS.md) - All solutions
- [MCP Tool Exposure Testing Log](./MCP_TOOL_EXPOSURE_TESTING_LOG.md) - Previous testing
- [Browser Environment Variable Fix](./BROWSER_ENV_VAR_FIX.md) - Environment variable solution

---

<!-- section_id: "e22ef869-08bc-4127-bdfb-8410d60fcce9" -->
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

<!-- section_id: "74eab2c8-45c4-4a14-959b-c17892943019" -->
### Attempt 6: Fix Config File Location (In Progress)
**Solution**: Update the actual config file that Cursor reads  
**Time**: < 2 minutes  
**Action**: Check `~/.config/mcp/mcp.json` (actual config file)  
**Result**: Need to apply same fixes to actual config file

**Status**: 🔄 In Progress

---

<!-- section_id: "d39520c8-65e8-4437-a86b-cdc00ce92b4d" -->
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

<!-- section_id: "2a93056a-37ad-4486-857d-49f4c2c4a6fa" -->
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

<!-- section_id: "fb9f04ea-7cc9-40b5-95c0-598313d591f4" -->
## Summary of All Attempts

<!-- section_id: "6dd85a57-2cbe-431a-a19f-776b3176529f" -->
### ✅ Completed:
1. Checked for duplicates - None found
2. Reordered MCP servers - Moved playwright/browser to top
3. Added full npx paths - For playwright and browser
4. Created project-specific config
5. Deleted and attempted regeneration
6. Restored working config

<!-- section_id: "631a4c27-3504-4704-9dd5-345b38d79e72" -->
### ⚠️ Current Status:
- Config restored to working state
- MCP tools not currently available (may need login or restart)
- Need to verify user is logged into Cursor IDE

<!-- section_id: "0815677a-795d-45c5-8483-9ac02929f25e" -->
### 🔄 Next Steps:
1. **Verify login status** - User must be logged into Cursor IDE
2. **Test tool availability** - Check if tools appear after ensuring login
3. **Try conservative fixes** - One at a time, test after each
4. **Check Cursor Settings** - Verify MCP servers are enabled in UI

---

<!-- section_id: "84df7313-461c-4881-b9dd-d38fd539039c" -->
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

<!-- section_id: "afe2ff12-b755-4720-b44d-5a6eef61a97c" -->
## Final Status

<!-- section_id: "3285d864-a67b-4b08-99e7-14d15e902e58" -->
### ✅ **SUCCESS**: Playwright MCP Tools Working!
- Playwright server enabled in Cursor Settings UI
- 22 tools available and working
- Navigation test successful
- Browser detection working

<!-- section_id: "ffa76ba6-c056-4e15-9d5c-403fe7e49033" -->
### 🔄 Next Steps:
1. Enable "browser" MCP server in Cursor Settings UI (currently disabled)
2. Test browser MCP tools after enabling
3. Document that UI enablement is required

---

**Critical Discovery**: MCP servers must be **enabled in Cursor Settings UI**, not just configured in mcp.json!

---

<!-- section_id: "98d21115-db90-425f-9c0a-11cc802c1c92" -->
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
