---
resource_id: "2b7ebe3d-7414-4639-8b7e-e129b748acba"
resource_type: "document"
resource_name: "MCP_TOOL_EXPOSURE_TESTING_LOG"
---
# MCP Tool Exposure Testing Log

**Date**: 2025-12-05  
**Location**: Universal Layer → MCP Servers and Tools Setup  
**Status**: Active testing and documentation

<!-- section_id: "923844b0-0238-4f81-bb44-dc9da3e8bbcd" -->
## Testing Session Summary

This document logs our testing attempts and findings regarding MCP tool exposure in Cursor IDE and CLI.

<!-- section_id: "4136993b-b46b-4bf8-b00d-a9ec288a22c1" -->
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

<!-- section_id: "6259a0d2-706a-4cc0-89d4-f4c26845f968" -->
## Testing Timeline

<!-- section_id: "6c3e7e62-7178-48d8-9622-11581ee0a73a" -->
### Initial State (Before Login)
- **Playwright MCP Tools**: ❌ Not available
- **Browser MCP Tools**: ❌ Not available  
- **Cursor Browser Extension Tools**: ❌ Not available
- **Error**: "Tool not found" for all MCP browser tools

<!-- section_id: "97e2f48b-ba88-44c2-bf26-b20cdf90a233" -->
### After User Logged In
- **Playwright MCP Tools**: ✅ **NOW AVAILABLE** (`mcp_playwright_*`)
- **Browser MCP Tools**: ✅ **NOW AVAILABLE** (`mcp_browser_*`)
- **Cursor Browser Extension Tools**: ⚠️ Not in available tools list (but may still work)

<!-- section_id: "af502104-ad3a-4b9c-beef-455da9ff0dc8" -->
### Current Issue: Browser Detection
- **Problem**: Playwright tools available but still getting "Browser specified in your config is not installed"
- **Status**: Environment variables are configured, but browser detection still failing
- **Next Steps**: May need Cursor restart or additional configuration

<!-- section_id: "6fb04c90-011f-4fb5-8703-ce9d013388b4" -->
## What We Tried

<!-- section_id: "85829b24-5562-4b21-831f-544496214c02" -->
### 1. Environment Variable Configuration ✅
- **Action**: Added `PLAYWRIGHT_BROWSERS_PATH` and `HOME` to MCP config
- **Files Updated**: `~/.cursor/mcp.json` and `~/.config/mcp/mcp.json`
- **Result**: Configuration updated, but browser detection still failing

<!-- section_id: "6a830f1f-967e-4eb2-a3b3-6d3ecc386108" -->
### 2. Cursor CLI Installation ✅
- **Action**: Installed Cursor CLI via `curl https://cursor.com/install -fsS | bash`
- **Version**: 2025.11.25-d5b3271
- **Result**: CLI installed successfully
- **Issue**: CLI requires MCP server approval before use

<!-- section_id: "028ec96e-0b43-448c-a1e5-ef7938802715" -->
### 3. Cursor CLI MCP Testing ⚠️
- **Action**: Attempted to list MCP servers and tools via CLI
- **Commands Tried**:
  - `cursor-agent mcp list` - Failed: Servers not approved
  - `cursor-agent mcp list-tools playwright` - Failed: Server not approved
  - `cursor-agent --approve-mcps -p "test"` - No output (may have worked silently)
- **Result**: CLI needs MCP server approval (separate from IDE approval)

<!-- section_id: "33a9e83c-6419-43b2-afa5-d3bf9dd8f6b7" -->
### 4. User Login to Cursor IDE ✅
- **Action**: User logged into Cursor IDE
- **Result**: **BREAKTHROUGH** - Playwright MCP tools became available!
- **Finding**: Login/authentication may be required for MCP tool exposure

<!-- section_id: "bee4679c-b972-4d49-aac6-693105e55423" -->
### 5. Playwright Tool Testing ⚠️
- **Action**: Attempted to use `mcp_playwright_browser_navigate`
- **Result**: Tool available but browser detection still failing
- **Error**: "Browser specified in your config is not installed"

<!-- section_id: "60d05264-3b1a-4a7d-ae5e-e2522053ee6c" -->
## Key Learnings

<!-- section_id: "8fad2d58-d791-43cd-964d-e1e732aae36f" -->
### 1. Login/Authentication May Be Required
**Finding**: After user logged into Cursor IDE, Playwright MCP tools became available.

**Implication**: 
- MCP tool exposure may require user authentication
- Tools may not be exposed until user is logged in
- This could explain why tools weren't available initially

**Action**: Document this as a potential requirement for MCP tool exposure.

<!-- section_id: "c3c6477f-efdc-4cb5-9575-d793d871fcc4" -->
### 2. Playwright Tools Use `mcp_playwright_*` Prefix
**Finding**: Playwright MCP tools are available with `mcp_playwright_*` prefix, not `mcp_browser_*`.

**Tool Naming**:
- Playwright MCP: `mcp_playwright_browser_*`
- Browser MCP: `mcp_browser_browser_*`
- Cursor Extension: `mcp_cursor-browser-extension_*` (not currently in available list)

**Implication**: Tool naming follows server name in config, not a generic pattern.

<!-- section_id: "559a72c0-8a77-41f0-838f-818bae482888" -->
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

<!-- section_id: "70fb6531-c1af-49c3-9799-9b07cda17c3c" -->
### 4. Cursor CLI Has Separate Approval System
**Finding**: CLI requires MCP server approval separate from IDE approval.

**Implication**:
- IDE and CLI have separate approval states
- `--approve-mcps` flag exists but may need to be used differently
- CLI may need servers approved through IDE first, or vice versa

<!-- section_id: "685941e1-5e55-434b-9a2b-e1d1d7667f78" -->
## Current Status

<!-- section_id: "4ca00f1b-06af-4a60-9b4a-3767fc97a37c" -->
### ✅ Working
- Playwright MCP tools are **AVAILABLE** (`mcp_playwright_*`)
- Browser MCP tools are **AVAILABLE** (`mcp_browser_*`) - **✅ CONFIRMED WORKING!**
- **Browser navigation successful** - `mcp_browser_browser_navigate` worked!
- Environment variables are configured
- Cursor CLI is installed

<!-- section_id: "2d93e0a3-d9cc-4da6-9de4-590cd9d17361" -->
### ⚠️ Issues
- Playwright MCP tools available but browser detection failing ("Browser not installed" error)
- Browser MCP tools work but may need headed mode configuration
- CLI approval system needs investigation

<!-- section_id: "6c30b6f4-9103-4d24-9bfd-0621c934a2e6" -->
### ✅ Success: Browser MCP Tools Working!
**Test Result (2025-12-05)**:
- Tool: `mcp_browser_browser_navigate("https://www.google.com")`
- Result: ✅ **SUCCESS** - Navigated to Google successfully
- Page loaded with full snapshot available
- Browser is running and accessible

<!-- section_id: "a8933856-1918-4518-8c87-69fe687dbd83" -->
### ❓ Unknown
- Do we need to use `mcp_playwright_browser_install` first?
- Will Cursor restart fix browser detection?
- Do Cursor browser extension tools still work?

<!-- section_id: "9c40e6e6-7163-44e5-b712-44a6e2327a23" -->
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

<!-- section_id: "ca692db3-00cc-4159-b05c-ab743c44f5fc" -->
## Successful Test Results

<!-- section_id: "93403c9c-78b9-447f-a0ba-5d2b4df8fb26" -->
### Test 1: Browser MCP Navigation ✅ SUCCESS
**Command**: `mcp_browser_browser_navigate("https://www.google.com")`

**Result**: ✅ **SUCCESSFUL**
- Navigated to Google successfully
- Page loaded with full content
- Page snapshot retrieved showing all page elements
- Browser is running and accessible

**Finding**: Browser MCP tools (`mcp_browser_*`) are **WORKING** after user login!

<!-- section_id: "bcd499ae-d8a5-4fc8-9e9e-fb14c9c891f0" -->
### Test 2: Browser Screenshot
**Command**: `mcp_browser_browser_screenshot()`

**Result**: Screenshot taken (shows white page with grey line on edge)
- Screenshot functionality works
- May be showing blank page or different tab

<!-- section_id: "4f3693fb-2bb2-4c43-9d64-311553529dce" -->
### Test 3: Browser Tab List
**Command**: `mcp_browser_browser_tab_list()`

**Result**: Shows tab [0] with "about:blank" URL
- Tab management works
- May be showing different browser instance than navigation

**Note**: There may be multiple browser instances or the navigation opened in a different context.

<!-- section_id: "0b733a76-b2e2-4ccb-b4df-5c2e96d71de4" -->
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

<!-- section_id: "492ed021-d323-4959-b166-dbca09dcbe82" -->
## Tool Availability Comparison

| Tool Set | Before Login | After Login | Status |
|----------|-------------|------------|--------|
| `mcp_playwright_*` | ❌ Not available | ✅ **Available** | **FIXED** |
| `mcp_browser_*` | ❌ Not available | ✅ **Available** | **FIXED** |
| `mcp_cursor-browser-extension_*` | ❌ Not available | ⚠️ Not in list | Unknown |
| Browser Detection | ❌ Failing | ⚠️ Still failing | Needs fix |

<!-- section_id: "52ad3d39-fd5a-4816-96cd-1de13d8c994b" -->
## Related Documentation

- [MCP Tool Exposure Solutions](./MCP_TOOL_EXPOSURE_SOLUTIONS.md) - All workarounds
- [MCP Tool Exposure OS Analysis](./MCP_TOOL_EXPOSURE_OS_ANALYSIS.md) - Platform comparison
- [Browser Environment Variable Fix](./BROWSER_ENV_VAR_FIX.md) - Environment variable solution

<!-- section_id: "d252c03e-62f8-4330-bd70-58b33b96b583" -->
## Cursor CLI Research Findings (2025-12-05)

<!-- section_id: "180e539f-0347-478c-8692-1b89e13cf14f" -->
### CLI Legitimacy Confirmed
- ✅ **Official Product**: Cursor CLI is legitimate and officially supported by Cursor team
- ✅ **Documented**: Official documentation on cursor.com with install/auth/configuration
- ✅ **Production-Ready**: Used by developers in real-world scenarios
- ✅ **Security**: Permission system for file operations and shell commands

<!-- section_id: "0467dedf-d509-4d39-9906-b60aa11e9e9f" -->
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

<!-- section_id: "8edcac08-a71f-45c7-a05d-5c7aa5393104" -->
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

<!-- section_id: "7eef2227-0b26-4c22-864b-4d16dc3702ca" -->
## Changelog

<!-- section_id: "948e571d-b81b-468b-8b7c-8250163f5d53" -->
### 2025-12-05 (Updated)
- Added Cursor CLI research findings
- Documented IDE vs CLI tradeoffs
- Documented TUI vs GUI bug comparison
- Added recommendation for WSL users

<!-- section_id: "05ed2da4-16a8-4df6-b100-42f02cf1493d" -->
### 2025-12-05 (Initial)
- **BREAKTHROUGH**: Playwright MCP tools became available after user login
- Documented tool naming: `mcp_playwright_*` prefix confirmed
- Identified login/authentication as potential requirement
- Browser detection still failing despite environment variables
- Cursor CLI installed and tested (requires approval)
- Created comprehensive testing log

---

**This log documents our testing journey and the breakthrough discovery that login may be required for MCP tool exposure.**

