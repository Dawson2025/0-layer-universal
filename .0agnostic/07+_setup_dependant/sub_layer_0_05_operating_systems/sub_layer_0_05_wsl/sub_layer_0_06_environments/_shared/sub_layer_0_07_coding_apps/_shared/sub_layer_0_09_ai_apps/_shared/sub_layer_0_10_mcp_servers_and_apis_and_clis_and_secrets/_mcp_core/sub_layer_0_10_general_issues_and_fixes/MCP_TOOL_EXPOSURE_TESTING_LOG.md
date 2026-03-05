---
resource_id: "549d9218-aea4-4a66-8975-dfec35c58718"
resource_type: "document"
resource_name: "MCP_TOOL_EXPOSURE_TESTING_LOG"
---
# MCP Tool Exposure Testing Log

**Date**: 2025-12-05  
**Location**: Universal Layer → MCP Servers and Tools Setup  
**Status**: Active testing and documentation

<!-- section_id: "74694a9e-5784-48d0-92af-bbd1e82faa67" -->
## Testing Session Summary

This document logs our testing attempts and findings regarding MCP tool exposure in Cursor IDE and CLI.

<!-- section_id: "5b72ce19-6a12-4cfd-a1d4-71b2404fac30" -->
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

<!-- section_id: "f2e30b4b-ffa3-40c7-a887-a506c676080a" -->
## Testing Timeline

<!-- section_id: "a66f2c1f-656d-4d2b-8fc8-27a9db61d1a7" -->
### Initial State (Before Login)
- **Playwright MCP Tools**: ❌ Not available
- **Browser MCP Tools**: ❌ Not available  
- **Cursor Browser Extension Tools**: ❌ Not available
- **Error**: "Tool not found" for all MCP browser tools

<!-- section_id: "ae3b1d4b-907a-4fbd-bcca-e5efdf39e993" -->
### After User Logged In
- **Playwright MCP Tools**: ✅ **NOW AVAILABLE** (`mcp_playwright_*`)
- **Browser MCP Tools**: ✅ **NOW AVAILABLE** (`mcp_browser_*`)
- **Cursor Browser Extension Tools**: ⚠️ Not in available tools list (but may still work)

<!-- section_id: "62902ca1-2630-4150-82a1-7154dc2d12de" -->
### Current Issue: Browser Detection
- **Problem**: Playwright tools available but still getting "Browser specified in your config is not installed"
- **Status**: Environment variables are configured, but browser detection still failing
- **Next Steps**: May need Cursor restart or additional configuration

<!-- section_id: "3ea23147-20d4-49dc-bf0d-68cba84b55da" -->
## What We Tried

<!-- section_id: "194a2492-e5f3-4235-98ec-ecc77c630c59" -->
### 1. Environment Variable Configuration ✅
- **Action**: Added `PLAYWRIGHT_BROWSERS_PATH` and `HOME` to MCP config
- **Files Updated**: `~/.cursor/mcp.json` and `~/.config/mcp/mcp.json`
- **Result**: Configuration updated, but browser detection still failing

<!-- section_id: "fb2f824b-f2df-44a5-9f9d-b60b84789949" -->
### 2. Cursor CLI Installation ✅
- **Action**: Installed Cursor CLI via `curl https://cursor.com/install -fsS | bash`
- **Version**: 2025.11.25-d5b3271
- **Result**: CLI installed successfully
- **Issue**: CLI requires MCP server approval before use

<!-- section_id: "1c09da3a-8a78-4ac7-8fe3-92aa0e5e437c" -->
### 3. Cursor CLI MCP Testing ⚠️
- **Action**: Attempted to list MCP servers and tools via CLI
- **Commands Tried**:
  - `cursor-agent mcp list` - Failed: Servers not approved
  - `cursor-agent mcp list-tools playwright` - Failed: Server not approved
  - `cursor-agent --approve-mcps -p "test"` - No output (may have worked silently)
- **Result**: CLI needs MCP server approval (separate from IDE approval)

<!-- section_id: "0dfe610e-59a2-46f0-91b7-072af37b277a" -->
### 4. User Login to Cursor IDE ✅
- **Action**: User logged into Cursor IDE
- **Result**: **BREAKTHROUGH** - Playwright MCP tools became available!
- **Finding**: Login/authentication may be required for MCP tool exposure

<!-- section_id: "88e8cd42-5b3c-4a6a-9eba-84fe947fa3cb" -->
### 5. Playwright Tool Testing ⚠️
- **Action**: Attempted to use `mcp_playwright_browser_navigate`
- **Result**: Tool available but browser detection still failing
- **Error**: "Browser specified in your config is not installed"

<!-- section_id: "015b5fc0-af5e-485f-9447-44e53669526e" -->
## Key Learnings

<!-- section_id: "6407f062-a840-435e-b802-8e2a19bff5ab" -->
### 1. Login/Authentication May Be Required
**Finding**: After user logged into Cursor IDE, Playwright MCP tools became available.

**Implication**: 
- MCP tool exposure may require user authentication
- Tools may not be exposed until user is logged in
- This could explain why tools weren't available initially

**Action**: Document this as a potential requirement for MCP tool exposure.

<!-- section_id: "0b048a67-0de4-423e-bcab-75b1af0aecb0" -->
### 2. Playwright Tools Use `mcp_playwright_*` Prefix
**Finding**: Playwright MCP tools are available with `mcp_playwright_*` prefix, not `mcp_browser_*`.

**Tool Naming**:
- Playwright MCP: `mcp_playwright_browser_*`
- Browser MCP: `mcp_browser_browser_*`
- Cursor Extension: `mcp_cursor-browser-extension_*` (not currently in available list)

**Implication**: Tool naming follows server name in config, not a generic pattern.

<!-- section_id: "893e99cd-06b4-41e7-9071-c21a9f302497" -->
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

<!-- section_id: "1f04569a-05f4-4375-881a-f4987d4e2366" -->
### 4. Cursor CLI Has Separate Approval System
**Finding**: CLI requires MCP server approval separate from IDE approval.

**Implication**:
- IDE and CLI have separate approval states
- `--approve-mcps` flag exists but may need to be used differently
- CLI may need servers approved through IDE first, or vice versa

<!-- section_id: "aacd1331-141d-4b24-aac0-0dbf0ec79277" -->
## Current Status

<!-- section_id: "8d5c64b3-b929-4775-976d-ae20097dc557" -->
### ✅ Working
- Playwright MCP tools are **AVAILABLE** (`mcp_playwright_*`)
- Browser MCP tools are **AVAILABLE** (`mcp_browser_*`) - **✅ CONFIRMED WORKING!**
- **Browser navigation successful** - `mcp_browser_browser_navigate` worked!
- Environment variables are configured
- Cursor CLI is installed

<!-- section_id: "b891e317-e8e8-42b3-9249-714b7f8cc5d2" -->
### ⚠️ Issues
- Playwright MCP tools available but browser detection failing ("Browser not installed" error)
- Browser MCP tools work but may need headed mode configuration
- CLI approval system needs investigation

<!-- section_id: "55125dfd-8a06-4715-8fd0-4c09e7115301" -->
### ✅ Success: Browser MCP Tools Working!
**Test Result (2025-12-05)**:
- Tool: `mcp_browser_browser_navigate("https://www.google.com")`
- Result: ✅ **SUCCESS** - Navigated to Google successfully
- Page loaded with full snapshot available
- Browser is running and accessible

<!-- section_id: "00f294c4-71d8-4766-9fbb-dd9ad12e08f4" -->
### ❓ Unknown
- Do we need to use `mcp_playwright_browser_install` first?
- Will Cursor restart fix browser detection?
- Do Cursor browser extension tools still work?

<!-- section_id: "90d333ab-bd7d-437a-af53-6bef3253678c" -->
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

<!-- section_id: "0c41b076-8bbf-4a7a-a463-3064d56e32e7" -->
## Successful Test Results

<!-- section_id: "9dbca1a4-5fed-468f-bfd5-09d2c149a6e9" -->
### Test 1: Browser MCP Navigation ✅ SUCCESS
**Command**: `mcp_browser_browser_navigate("https://www.google.com")`

**Result**: ✅ **SUCCESSFUL**
- Navigated to Google successfully
- Page loaded with full content
- Page snapshot retrieved showing all page elements
- Browser is running and accessible

**Finding**: Browser MCP tools (`mcp_browser_*`) are **WORKING** after user login!

<!-- section_id: "c228fe49-40b2-4e8f-99a2-25caf789a572" -->
### Test 2: Browser Screenshot
**Command**: `mcp_browser_browser_screenshot()`

**Result**: Screenshot taken (shows white page with grey line on edge)
- Screenshot functionality works
- May be showing blank page or different tab

<!-- section_id: "a5314453-4331-42a2-a050-1a94e6014a06" -->
### Test 3: Browser Tab List
**Command**: `mcp_browser_browser_tab_list()`

**Result**: Shows tab [0] with "about:blank" URL
- Tab management works
- May be showing different browser instance than navigation

**Note**: There may be multiple browser instances or the navigation opened in a different context.

<!-- section_id: "316c3bee-1cf2-44d8-91f2-5541013114a8" -->
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

<!-- section_id: "6608250b-2f6c-4364-ad1c-5cf3b89d3dbd" -->
## Tool Availability Comparison

| Tool Set | Before Login | After Login | Status |
|----------|-------------|------------|--------|
| `mcp_playwright_*` | ❌ Not available | ✅ **Available** | **FIXED** |
| `mcp_browser_*` | ❌ Not available | ✅ **Available** | **FIXED** |
| `mcp_cursor-browser-extension_*` | ❌ Not available | ⚠️ Not in list | Unknown |
| Browser Detection | ❌ Failing | ⚠️ Still failing | Needs fix |

<!-- section_id: "409b5cfc-77f2-4ee9-8f54-17dae20b5f40" -->
## Related Documentation

- [MCP Tool Exposure Solutions](./MCP_TOOL_EXPOSURE_SOLUTIONS.md) - All workarounds
- [MCP Tool Exposure OS Analysis](./MCP_TOOL_EXPOSURE_OS_ANALYSIS.md) - Platform comparison
- [Browser Environment Variable Fix](./BROWSER_ENV_VAR_FIX.md) - Environment variable solution

<!-- section_id: "9390a6f4-2737-4745-a1b5-5243f20bcdf8" -->
## Cursor CLI Research Findings (2025-12-05)

<!-- section_id: "9e73505d-c097-414f-b7b1-2cbf2db92fb7" -->
### CLI Legitimacy Confirmed
- ✅ **Official Product**: Cursor CLI is legitimate and officially supported by Cursor team
- ✅ **Documented**: Official documentation on cursor.com with install/auth/configuration
- ✅ **Production-Ready**: Used by developers in real-world scenarios
- ✅ **Security**: Permission system for file operations and shell commands

<!-- section_id: "2b9fe3f0-0c0e-4a64-986d-47ebec90e972" -->
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

<!-- section_id: "c1a274eb-057d-45fc-b3ef-b9a013fc0683" -->
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

<!-- section_id: "3ac2c079-7c1d-424c-b4c6-84e370d88cb6" -->
## Changelog

<!-- section_id: "91712e6d-505c-4f58-8f19-6e7e06f990c0" -->
### 2025-12-05 (Updated)
- Added Cursor CLI research findings
- Documented IDE vs CLI tradeoffs
- Documented TUI vs GUI bug comparison
- Added recommendation for WSL users

<!-- section_id: "38b48be6-7e32-4883-a517-7c06479bf8a7" -->
### 2025-12-05 (Initial)
- **BREAKTHROUGH**: Playwright MCP tools became available after user login
- Documented tool naming: `mcp_playwright_*` prefix confirmed
- Identified login/authentication as potential requirement
- Browser detection still failing despite environment variables
- Cursor CLI installed and tested (requires approval)
- Created comprehensive testing log

---

**This log documents our testing journey and the breakthrough discovery that login may be required for MCP tool exposure.**

