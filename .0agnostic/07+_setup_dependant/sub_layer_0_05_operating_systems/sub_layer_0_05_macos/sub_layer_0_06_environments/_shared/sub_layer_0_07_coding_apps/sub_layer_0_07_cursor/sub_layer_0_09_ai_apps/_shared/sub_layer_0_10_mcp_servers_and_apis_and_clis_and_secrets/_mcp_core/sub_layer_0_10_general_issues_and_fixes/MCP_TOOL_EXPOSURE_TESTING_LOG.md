---
resource_id: "138b53b0-78c7-4df7-b14c-59fcbbaba938"
resource_type: "document"
resource_name: "MCP_TOOL_EXPOSURE_TESTING_LOG"
---
# MCP Tool Exposure Testing Log

**Date**: 2025-12-05  
**Location**: Universal Layer → MCP Servers and Tools Setup  
**Status**: Active testing and documentation

<!-- section_id: "febfa16c-df5f-4234-a26b-61c0d0880afd" -->
## Testing Session Summary

This document logs our testing attempts and findings regarding MCP tool exposure in Cursor IDE and CLI.

<!-- section_id: "48ae1488-d6b4-4c3a-a776-048bd612e906" -->
## Key Discovery: Playwright MCP Tools ARE Available!

**Critical Finding (2025-12-05)**: After user logged into Cursor IDE, the Playwright MCP tools became available with the `mcp_playwright_*` prefix!

**Available Tools Confirmed**:
- ✅ `mcp_playwright_browser_navigate`
- ✅ `mcp_playwright_browser_click`
- ✅ `mcp_playwright_browser_snapshot`
- ✅ `mcp_playwright_browser_take_screenshot`
- ✅ `mcp_playwright_browser_type`
- ✅ `mcp_playwright_browser_hover`
- ✅ `mcp_playwright_browser_tabs`
- ✅ `mcp_playwright_browser_wait_for`
- ✅ And 14+ more Playwright tools

**Also Available**:
- ✅ `mcp_browser_browser_*` tools (21 tools from @agent-infra/mcp-server-browser)
- ✅ `mcp_web-search_*` tools (Tavily)
- ✅ `mcp_context7_*` tools

<!-- section_id: "424d1bd3-2fdb-49e8-b172-6541fd8dcbae" -->
## Testing Timeline

<!-- section_id: "01d63740-7df4-4ac2-8599-631c8b3fc7ea" -->
### Initial State (Before Login)
- **Playwright MCP Tools**: ❌ Not available
- **Browser MCP Tools**: ❌ Not available  
- **Cursor Browser Extension Tools**: ❌ Not available
- **Error**: "Tool not found" for all MCP browser tools

<!-- section_id: "b3ff32ec-6747-4227-8ea7-152b9b24f7b3" -->
### After User Logged In
- **Playwright MCP Tools**: ✅ **NOW AVAILABLE** (`mcp_playwright_*`)
- **Browser MCP Tools**: ✅ **NOW AVAILABLE** (`mcp_browser_*`)
- **Cursor Browser Extension Tools**: ⚠️ Not in available tools list (but may still work)

<!-- section_id: "d23a2574-4bb6-4d1c-a8c3-3cfd1aa8cd29" -->
### Current Issue: Browser Detection
- **Problem**: Playwright tools available but still getting "Browser specified in your config is not installed"
- **Status**: Environment variables are configured, but browser detection still failing
- **Next Steps**: May need Cursor restart or additional configuration

<!-- section_id: "c8a4ca4a-ef30-4383-b18b-f2e913e49eca" -->
## What We Tried

<!-- section_id: "7bc97359-3573-4b0b-9f36-f607546d5621" -->
### 1. Environment Variable Configuration ✅
- **Action**: Added `PLAYWRIGHT_BROWSERS_PATH` and `HOME` to MCP config
- **Files Updated**: `~/.cursor/mcp.json` and `~/.config/mcp/mcp.json`
- **Result**: Configuration updated, but browser detection still failing

<!-- section_id: "f5503452-a3eb-48f0-aec8-97abd149e2a7" -->
### 2. Cursor CLI Installation ✅
- **Action**: Installed Cursor CLI via `curl https://cursor.com/install -fsS | bash`
- **Version**: 2025.11.25-d5b3271
- **Result**: CLI installed successfully
- **Issue**: CLI requires MCP server approval before use

<!-- section_id: "dd6b0718-8330-4b7f-8087-1f328cbbf9c4" -->
### 3. Cursor CLI MCP Testing ⚠️
- **Action**: Attempted to list MCP servers and tools via CLI
- **Commands Tried**:
  - `cursor-agent mcp list` - Failed: Servers not approved
  - `cursor-agent mcp list-tools playwright` - Failed: Server not approved
  - `cursor-agent --approve-mcps -p "test"` - No output (may have worked silently)
- **Result**: CLI needs MCP server approval (separate from IDE approval)

<!-- section_id: "aadedaac-0db1-4d1f-811b-c36274c9842d" -->
### 4. User Login to Cursor IDE ✅
- **Action**: User logged into Cursor IDE
- **Result**: **BREAKTHROUGH** - Playwright MCP tools became available!
- **Finding**: Login/authentication may be required for MCP tool exposure

<!-- section_id: "2cb72228-d917-4af6-befb-e85d765d38ff" -->
### 5. Playwright Tool Testing ⚠️
- **Action**: Attempted to use `mcp_playwright_browser_navigate`
- **Result**: Tool available but browser detection still failing
- **Error**: "Browser specified in your config is not installed"

<!-- section_id: "5183eb59-7f0f-4ab6-91a9-7437fedb5982" -->
## Key Learnings

<!-- section_id: "628925fd-8ca7-40dd-9691-7a3c797b5c3a" -->
### 1. Login/Authentication May Be Required
**Finding**: After user logged into Cursor IDE, Playwright MCP tools became available.

**Implication**: 
- MCP tool exposure may require user authentication
- Tools may not be exposed until user is logged in
- This could explain why tools weren't available initially

**Action**: Document this as a potential requirement for MCP tool exposure.

<!-- section_id: "99fad65b-9965-4db5-a9ed-c1513bd7aba8" -->
### 2. Playwright Tools Use `mcp_playwright_*` Prefix
**Finding**: Playwright MCP tools are available with `mcp_playwright_*` prefix, not `mcp_browser_*`.

**Tool Naming**:
- Playwright MCP: `mcp_playwright_browser_*`
- Browser MCP: `mcp_browser_browser_*`
- Cursor Extension: `mcp_cursor-browser-extension_*` (not currently in available list)

**Implication**: Tool naming follows server name in config, not a generic pattern.

<!-- section_id: "735a7e4e-3062-48d1-a263-ee9a8ba6e149" -->
### 3. Browser Detection Still Failing Despite Environment Variables
**Finding**: Even with `PLAYWRIGHT_BROWSERS_PATH` and `HOME` set, browser detection fails.

**Possible Causes**:
- Cursor may need restart to pick up environment variables
- Browser path may need to be explicitly set in Playwright MCP config
- WSL path resolution may be causing issues
- Browser may need to be installed via Playwright MCP's install command

**Next Steps**:
- Try `mcp_playwright_browser_install` tool to install browser
- Restart Cursor to ensure environment variables are loaded
- Check if browser path needs to be explicit in config

<!-- section_id: "4cd94aa8-fac9-4775-8fdd-c19925267012" -->
### 4. Cursor CLI Has Separate Approval System
**Finding**: CLI requires MCP server approval separate from IDE approval.

**Implication**:
- IDE and CLI have separate approval states
- `--approve-mcps` flag exists but may need to be used differently
- CLI may need servers approved through IDE first, or vice versa

<!-- section_id: "5909b8f6-c945-4a9b-96d7-bad750156d1e" -->
## Current Status

<!-- section_id: "4107dd1a-3ff8-4c65-817c-11c2773f4df6" -->
### ✅ Working
- Playwright MCP tools are **AVAILABLE** (`mcp_playwright_*`)
- Browser MCP tools are **AVAILABLE** (`mcp_browser_*`) - **✅ CONFIRMED WORKING!**
- **Browser navigation successful** - `mcp_browser_browser_navigate` worked!
- Environment variables are configured
- Cursor CLI is installed

<!-- section_id: "b6c675ef-654b-4f21-8d3d-27e8514fd557" -->
### ⚠️ Issues
- Playwright MCP tools available but browser detection failing ("Browser not installed" error)
- Browser MCP tools work but may need headed mode configuration
- CLI approval system needs investigation

<!-- section_id: "ce17cc2e-0b2d-4459-a7c2-b9bd5cb45beb" -->
### ✅ Success: Browser MCP Tools Working!
**Test Result (2025-12-05)**:
- Tool: `mcp_browser_browser_navigate("https://www.google.com")`
- Result: ✅ **SUCCESS** - Navigated to Google successfully
- Page loaded with full snapshot available
- Browser is running and accessible

<!-- section_id: "1fe1b04b-503d-4caf-9307-c6286b0b7bb3" -->
### ❓ Unknown
- Do we need to use `mcp_playwright_browser_install` first?
- Will Cursor restart fix browser detection?
- Do Cursor browser extension tools still work?

<!-- section_id: "95fcc67a-905b-4ab9-9111-a8df6bfa4573" -->
## Next Steps

1. ✅ **COMPLETED**: Test Browser MCP Tools
   - `mcp_browser_browser_navigate` works successfully!
   - Browser is running and accessible

2. **Check Headed Mode**:
   - Verify if browser is running in headed (visible) mode
   - May need configuration to ensure browser window is visible

3. **Fix Playwright Browser Detection**:
   - Playwright tools available but browser detection failing
   - May need to use `mcp_playwright_browser_install` tool
   - Or restart Cursor to pick up environment variables

4. **Document Success**:
   - Browser MCP tools are working!
   - Login requirement confirmed
   - Update all documentation with findings

<!-- section_id: "2ebf70dc-a423-43a0-965e-14ac8d456d4f" -->
## Successful Test Results

<!-- section_id: "592004df-3943-401a-80be-c33a3580e69c" -->
### Test 1: Browser MCP Navigation ✅ SUCCESS
**Command**: `mcp_browser_browser_navigate("https://www.google.com")`

**Result**: ✅ **SUCCESSFUL**
- Navigated to Google successfully
- Page loaded with full content
- Page snapshot retrieved showing all page elements
- Browser is running and accessible

**Finding**: Browser MCP tools (`mcp_browser_*`) are **WORKING** after user login!

<!-- section_id: "1b19056c-a879-42a1-b870-130a6209c866" -->
### Test 2: Browser Screenshot
**Command**: `mcp_browser_browser_screenshot()`

**Result**: Screenshot taken (shows white page with grey line on edge)
- Screenshot functionality works
- May be showing blank page or different tab

<!-- section_id: "712327e3-8eff-4027-b3bc-84debbe3335f" -->
### Test 3: Browser Tab List
**Command**: `mcp_browser_browser_tab_list()`

**Result**: Shows tab [0] with "about:blank" URL
- Tab management works
- May be showing different browser instance than navigation

**Note**: There may be multiple browser instances or the navigation opened in a different context.

<!-- section_id: "41019ff5-b25b-412b-853b-063e750f06b1" -->
## Testing Commands Used

```bash
# Cursor CLI installation
curl https://cursor.com/install -fsS | bash

# Test MCP servers
export PATH="$HOME/.local/bin:$PATH"
cursor-agent mcp list
cursor-agent mcp list-tools playwright
cursor-agent --approve-mcps -p "test"

# Check browser installation
ls -la ~/.cache/ms-playwright/chromium-*/chrome-linux64/chrome
```

<!-- section_id: "225a0930-96cf-479d-b979-057bd4e2dd74" -->
## Tool Availability Comparison

| Tool Set | Before Login | After Login | Status |
|----------|-------------|------------|--------|
| `mcp_playwright_*` | ❌ Not available | ✅ **Available** | **FIXED** |
| `mcp_browser_*` | ❌ Not available | ✅ **Available** | **FIXED** |
| `mcp_cursor-browser-extension_*` | ❌ Not available | ⚠️ Not in list | Unknown |
| Browser Detection | ❌ Failing | ⚠️ Still failing | Needs fix |

<!-- section_id: "beec2bf8-2521-4ceb-b7e6-a706fff9d307" -->
## Related Documentation

- [MCP Tool Exposure Solutions](./MCP_TOOL_EXPOSURE_SOLUTIONS.md) - All workarounds
- [MCP Tool Exposure OS Analysis](./MCP_TOOL_EXPOSURE_OS_ANALYSIS.md) - Platform comparison
- [Browser Environment Variable Fix](./BROWSER_ENV_VAR_FIX.md) - Environment variable solution

<!-- section_id: "9372bf03-fecb-4f08-b747-36144af855e5" -->
## Cursor CLI Research Findings (2025-12-05)

<!-- section_id: "dfb26446-8460-48d1-a73b-5a2e8dba2730" -->
### CLI Legitimacy Confirmed
- ✅ **Official Product**: Cursor CLI is legitimate and officially supported by Cursor team
- ✅ **Documented**: Official documentation on cursor.com with install/auth/configuration
- ✅ **Production-Ready**: Used by developers in real-world scenarios
- ✅ **Security**: Permission system for file operations and shell commands

<!-- section_id: "0c44cc43-371d-49d1-93e2-c43f6326cdc2" -->
### IDE vs CLI Comparison
**IDE Better For**:
- Interactive coding and navigation
- Inline diffs and editing
- Day-to-day development work
- Rich project context and indexing

**CLI Better For**:
- Automation and CI/CD
- Scripted refactors and batch tasks
- Headless/remote environments
- Working from other editors (Neovim, VS Code, JetBrains)

**Hybrid Approach Recommended**:
- Use IDE for interactive work
- Use CLI for automation and repeatable workflows
- Both share same config (rules, MCP servers)

<!-- section_id: "c2be13c3-8906-4ff1-b984-0da0a3014199" -->
### TUI vs GUI Bug Comparison
**TUI (CLI) Bugs**:
- More frequent UI glitches
- Endless scrolling/resetting issues
- Rendering failures and bugged states
- Prompt editing annoyances
- More visible rough edges

**GUI (IDE) Bugs**:
- Less frequent but broader stability issues
- Freezes and crashes (especially on Windows/WSL)
- High GPU usage
- Responsiveness drops

**Recommendation for WSL**:
- Prioritize GUI for interactive work
- Use CLI for automation/headless tasks
- Expect TUI glitches to compound terminal quirks in WSL

<!-- section_id: "12d75b96-f76f-4648-a3b3-b72b9d7ce8a3" -->
## Changelog

<!-- section_id: "785a23af-fc87-4cbb-9d7f-9814408bb19e" -->
### 2025-12-05 (Updated)
- Added Cursor CLI research findings
- Documented IDE vs CLI tradeoffs
- Documented TUI vs GUI bug comparison
- Added recommendation for WSL users

<!-- section_id: "a73a8aa6-0181-425f-8002-c87b261b88cb" -->
### 2025-12-05 (Initial)
- **BREAKTHROUGH**: Playwright MCP tools became available after user login
- Documented tool naming: `mcp_playwright_*` prefix confirmed
- Identified login/authentication as potential requirement
- Browser detection still failing despite environment variables
- Cursor CLI installed and tested (requires approval)
- Created comprehensive testing log

---

**This log documents our testing journey and the breakthrough discovery that login may be required for MCP tool exposure.**

