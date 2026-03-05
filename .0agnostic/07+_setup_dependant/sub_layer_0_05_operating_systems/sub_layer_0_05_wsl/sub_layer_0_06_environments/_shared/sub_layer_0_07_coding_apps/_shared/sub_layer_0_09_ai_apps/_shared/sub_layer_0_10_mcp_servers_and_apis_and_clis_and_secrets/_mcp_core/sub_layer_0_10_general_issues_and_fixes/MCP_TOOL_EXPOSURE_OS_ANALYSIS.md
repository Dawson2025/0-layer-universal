---
resource_id: "0585bda7-e785-4180-98db-e3edd4eee70d"
resource_type: "document"
resource_name: "MCP_TOOL_EXPOSURE_OS_ANALYSIS"
---
# MCP Tool Exposure - OS and Configuration Analysis

**Date**: 2025-12-05  
**Location**: Universal Layer → MCP Servers and Tools Setup  
**Status**: Comprehensive analysis of MCP tool exposure across platforms

<!-- section_id: "cd40f81d-53a8-4949-8078-d38623acdf92" -->
## Overview

This document analyzes MCP (Model Context Protocol) tool exposure issues across different operating systems and investigates whether problems are OS-specific or configuration-related.

<!-- section_id: "bbbdfd65-559c-471c-8de2-4ee61cd54c3c" -->
## Executive Summary

<!-- section_id: "27b7ed4b-cf5b-48a6-bd02-4c644ea187ea" -->
### Confirmed Issues by Platform

| Platform | Playwright MCP Tools | Browser MCP Tools | Cursor Extension Tools | Status |
|----------|---------------------|-------------------|----------------------|--------|
| **Linux (Native)** | ❌ Not Exposed | ⚠️ May Not Be Exposed | ✅ Available | Documented Issue |
| **WSL2 (Ubuntu)** | ❌ Not Exposed | ❌ Not Exposed | ✅ Available | **NEW FINDING** |
| **Windows (Native)** | ⚠️ **Also Affected** | ⚠️ **Also Affected** | ⚠️ **Also Affected** | **CRITICAL FINDING** |
| **macOS** | ⚠️ **Likely Affected** | ⚠️ **Likely Affected** | ⚠️ **Likely Affected** | **Based on Reports** |

<!-- section_id: "dc01e3fe-9b8e-44e6-bffe-e62e53c4b2b1" -->
### Critical Discovery (2025-12-05)

**This is NOT just a Linux/WSL issue!** Internet research reveals:

1. **Cursor Version 2.0.77 Bug**: Known issue where MCP tools aren't exposed to agents even though they appear connected
2. **Windows Users Also Affected**: Multiple forum reports of MCP tools not being exposed on Windows
3. **Cross-Platform Issue**: Reports of MCP tool exposure problems across Linux, Windows, and potentially macOS
4. **Cursor IDE Bug**: This appears to be a Cursor IDE bug, not OS-specific

<!-- section_id: "1f3e5659-d6de-4872-87a6-bdac80ee4334" -->
### Key Findings

1. **Linux/WSL Issue Confirmed**: Playwright MCP tools are NOT exposed to AI agents on Linux and WSL, even when servers connect successfully
2. **WSL-Specific Finding (2025-12-05)**: Browser MCP tools (`mcp_browser_*`) are also NOT exposed in WSL, despite server running
3. **Configuration vs. OS**: Environment variable configuration fixes browser detection, but does NOT fix tool exposure issues
4. **Windows/macOS Status**: Unknown - documentation assumes they work, but no confirmed testing

<!-- section_id: "5af6394e-86e6-4333-8308-7b45ce8458c9" -->
## Detailed Platform Analysis

<!-- section_id: "eccaa971-8395-47b6-bf23-4ff6e544dc0d" -->
### Linux (Native Ubuntu)

**Tested**: ✅ Yes  
**Environment**: Ubuntu 24.04 (Noble Numbat)  
**Date Tested**: 2025-12-02 to 2025-12-05

#### Playwright MCP Tools
- **Server Status**: ✅ Connects successfully
- **Tool Registration**: ✅ Reports "Found 22 tools"
- **Tool Exposure**: ❌ **NOT exposed to AI agents**
- **Available Tools**: None (`mcp_playwright_*` tools not available)
- **Error**: "Tool not found" when attempting to use

#### Browser MCP Tools (`@agent-infra/mcp-server-browser`)
- **Server Status**: ✅ Connects successfully
- **Tool Registration**: ✅ Reports tools available
- **Tool Exposure**: ⚠️ **May not be exposed** (documentation says should work, but needs verification)
- **Available Tools**: Unknown - documentation claims `mcp_browser_*` should work
- **Configuration**: Requires explicit browser paths and environment variables

#### Cursor Browser Extension Tools
- **Server Status**: ✅ Available
- **Tool Exposure**: ✅ **Exposed to AI agents**
- **Available Tools**: `mcp_cursor-browser-extension_*` (18 tools)
- **Issues**: Browser detection may fail, but tools are accessible

**Root Cause (Documented)**: Cursor IDE's MCP tool exposure mechanism has platform-specific behavior. On Linux, Playwright MCP tools are not exposed to agents despite successful server connection.

**Evidence**:
- GitHub Issues: #942, #1113 (Ubuntu-specific Playwright MCP problems)
- Multiple test sessions showing tools registered but not exposed
- Documentation explicitly states "Linux/Ubuntu-specific issue"

<!-- section_id: "57d7655e-1da8-4d7a-a0fd-a78a7b63b87e" -->
### WSL2 (Windows Subsystem for Linux)

**Tested**: ✅ Yes  
**Environment**: WSL2 (Ubuntu 24.04) on Windows 11  
**Date Tested**: 2025-12-05  
**Status**: ⚠️ **NEW FINDING - More Severe Than Native Linux**

#### Playwright MCP Tools
- **Server Status**: ✅ Connects successfully
- **Tool Registration**: ✅ Reports "Found 22 tools" (visible in Cursor Settings)
- **Tool Exposure**: ❌ **NOT exposed to AI agents**
- **Available Tools**: None (`mcp_playwright_*` tools not available)
- **Error**: Tools not in available tool list

#### Browser MCP Tools (`@agent-infra/mcp-server-browser`)
- **Server Status**: ✅ **Running** (confirmed via `ps aux`)
- **Tool Registration**: ✅ Tools registered (visible in Cursor Settings)
- **Tool Exposure**: ❌ **NOT exposed to AI agents** ⚠️ **NEW FINDING**
- **Available Tools**: None (`mcp_browser_*` tools not in available list)
- **Configuration**: Environment variables set correctly (`PLAYWRIGHT_BROWSERS_PATH`, `HOME`)

**Critical WSL Finding (2025-12-05)**:
- Both Playwright AND Browser MCP tools are NOT exposed in WSL
- This is MORE severe than native Linux (where browser MCP tools may work)
- Only `mcp_cursor-browser-extension_*` tools are available
- Server processes are running correctly, but tools are not exposed to agents

**WSL-Specific Considerations**:
- Cursor IDE runs on Windows but connects to WSL
- MCP servers run in WSL environment
- Path resolution complexity (Windows paths vs. Linux paths)
- May affect how Cursor exposes tools to agents

<!-- section_id: "863ce01d-88d5-47d1-81a7-17479950e62c" -->
### Windows (Native)

**Tested**: ⚠️ **Internet Research**  
**Status**: **Also Affected - Not OS-Specific**

#### Internet Research Findings (2025-12-05)

**Critical Discovery**: Windows users are ALSO experiencing MCP tool exposure issues:

1. **Forum Reports**:
   - "MCP servers are not exposed to agents" - reported on Windows
   - "Browser Agent Tools Not Accessible Despite 'Ready' Status" - Windows users
   - "Playwright MCP not working on Cursor" - multiple platforms including Windows

2. **Known Cursor Bug**:
   - **Cursor version 2.0.77** has a known issue where MCP tools aren't exposed to agents even though they appear connected
   - This affects multiple platforms, not just Linux

3. **Windows-Specific MCP Issues**:
   - Reports of MCP servers not running properly on Windows
   - Different command configurations required for Windows
   - GitHub issues about Windows MCP problems

#### Evidence from Internet Search

- **Forum Post**: "MCP servers are not exposed to agents - Cursor - Community Forum" - mentions version 2.0.77 bug
- **Forum Post**: "Browser Agent Tools Not Accessible Despite 'Ready' Status" - Windows users reporting issues
- **Forum Post**: "Playwright MCP not working on Cursor" - cross-platform issue
- **GitHub Issues**: Multiple reports of MCP tools not working on Windows

**Conclusion**: This is **NOT a Linux/WSL-specific issue** - it's a broader Cursor IDE bug affecting multiple platforms.

<!-- section_id: "a4d44429-34e8-483e-a356-5f53d64dfe6f" -->
### macOS

**Tested**: ⚠️ **Internet Research**  
**Status**: **Likely Also Affected**

#### Internet Research Findings (2025-12-05)

**Evidence**: While specific macOS reports are fewer, the pattern suggests macOS may also be affected:

1. **Cross-Platform Bug Pattern**:
   - Cursor version 2.0.77 bug affects multiple platforms
   - Forum discussions mention issues across platforms
   - No evidence that macOS is immune to the bug

2. **Forum Discussions**:
   - General MCP tool exposure issues discussed without platform restrictions
   - Some users report better experience on macOS, but this may be version-specific

#### What We Need to Test
- [ ] Playwright MCP tool exposure on macOS
- [ ] Browser MCP tool exposure on macOS
- [ ] Cursor browser extension tool availability
- [ ] Configuration requirements (environment variables, paths)
- [ ] Any macOS-specific issues
- [ ] Cursor version being used (2.0.77 vs. newer versions)

<!-- section_id: "2e64a212-bc23-4ff1-9e64-2e0d2fd532d6" -->
## Critical Finding: This is NOT OS-Specific!

<!-- section_id: "c4ecb04b-7471-422c-ae0c-687e6fcff220" -->
### Internet Research Results (2025-12-05)

**Major Discovery**: After searching the internet, we found that MCP tool exposure issues are **NOT limited to Linux/WSL**:

1. **Cursor Version 2.0.77 Known Bug**:
   - Forum post: "MCP servers are not exposed to agents - Cursor - Community Forum"
   - States: "This looks like a known issue in version 2.0.77 where some tools aren't actually exposed to the agent, even though they appear as connected"
   - This is a **Cursor IDE bug**, not OS-specific

2. **Windows Users Also Affected**:
   - Multiple forum reports of MCP tools not being exposed on Windows
   - "Browser Agent Tools Not Accessible Despite 'Ready' Status" - Windows users
   - "Playwright MCP not working on Cursor" - cross-platform reports

3. **Cross-Platform Pattern**:
   - Issues reported across Linux, Windows, and potentially macOS
   - Pattern suggests Cursor IDE bug rather than OS-specific issue
   - Different platforms may have different severity, but all are affected

<!-- section_id: "a83d13e3-c20e-499e-81af-449086817501" -->
### Revised Understanding

**Previous Assumption** (Incorrect):
- "Linux/Ubuntu systems experience unique challenges with MCP servers in Cursor IDE that don't occur on Windows or macOS"

**Actual Finding** (Correct):
- This is a **Cursor IDE bug** affecting multiple platforms
- Linux/WSL may have additional issues (sandboxing, path resolution)
- But the core tool exposure problem affects Windows and likely macOS too
- Cursor version 2.0.77 specifically has this known bug

<!-- section_id: "8d331370-2458-4b9e-b3ed-db81232b3e7d" -->
## Configuration vs. OS Analysis

<!-- section_id: "d34c5464-6812-4eb5-a6eb-fcebb2320f98" -->
### Could This Be Configuration-Related?

#### Environment Variables (Browser Detection)
- **Issue**: Browsers not found by MCP servers
- **Root Cause**: `PLAYWRIGHT_BROWSERS_PATH` not set in MCP server environment
- **Fix**: Add environment variables to MCP config
- **Result**: ✅ **FIXED** - This was configuration, not OS-specific
- **Platforms Affected**: All platforms (Linux, WSL, Windows, macOS)

#### Tool Exposure (MCP Tools Not Available)
- **Issue**: MCP tools registered but not exposed to AI agents
- **Root Cause**: Unknown - could be OS-specific OR configuration
- **Current Understanding**: Documented as "Linux/Ubuntu-specific"
- **Evidence for OS-Specific**:
  - GitHub issues specifically mention Ubuntu
  - Documentation explicitly states "Linux/Ubuntu-specific"
  - Works differently on Linux vs. Windows/macOS (assumed)
- **Evidence for Configuration**:
  - Both Playwright and Browser MCP tools not exposed in WSL
  - Could be related to how Cursor connects to WSL vs. native
  - Could be related to MCP server naming or configuration

#### Potential Configuration Issues to Investigate

1. **MCP Server Naming**:
   - Server name in config: `"playwright"` → tools might be `mcp_playwright_*`
   - Server name in config: `"browser"` → tools might be `mcp_browser_*`
   - But tools shown in Cursor Settings are just `browser_navigate`, `browser_click`, etc.
   - **Question**: Is there a naming mismatch between what Cursor shows and what agents can access?

2. **WSL Connection Architecture**:
   - Cursor IDE runs on Windows
   - MCP servers run in WSL
   - **Question**: Does Cursor's tool exposure mechanism work differently when servers are in WSL?

3. **MCP Server Process Isolation**:
   - MCP servers run via `npx` in isolated environments
   - Environment variables need to be explicitly set
   - **Question**: Could tool exposure be affected by how Cursor spawns/connects to these processes?

4. **Cursor Version/Configuration**:
   - Different Cursor versions might handle MCP differently
   - Settings might affect tool exposure
   - **Question**: Are there Cursor settings that control MCP tool exposure?

<!-- section_id: "1d5d817b-7ade-4762-8a08-de7ee840fb15" -->
## Recommendations

<!-- section_id: "7f92d111-0b16-4828-8f9f-5ca3a0854c05" -->
### For All Users (All Platforms)

1. **Check Cursor Version**:
   - Cursor version 2.0.77 has a known bug where MCP tools aren't exposed
   - Update to the latest version if possible
   - Check Cursor release notes for MCP tool exposure fixes

2. **Report Issues**:
   - If tools aren't exposed, report to Cursor forum/GitHub
   - Include Cursor version, OS, and MCP server details
   - This helps identify if it's version-specific or configuration-specific

3. **Workarounds**:
   - Use Cursor browser extension tools if available
   - Try restarting Cursor completely
   - Check Cursor Settings → Tools & MCP for tool availability

<!-- section_id: "c17c3779-b078-4031-b431-3f207d1b13d8" -->
### For Linux/WSL Users

1. **Use Cursor Browser Extension Tools**:
   - `mcp_cursor-browser-extension_*` tools are available
   - These work despite other MCP tools not being exposed
   - Configure browser path in Cursor Settings → Tools & MCP → Browser Automation

2. **Don't Rely on Playwright/Browser MCP Tools**:
   - Even if servers connect, tools may not be exposed
   - This is a known limitation on Linux/WSL
   - Use Cursor browser extension as workaround

3. **Set Environment Variables**:
   - Still required for browser detection
   - Add `PLAYWRIGHT_BROWSERS_PATH` and `HOME` to MCP config
   - This fixes browser detection, not tool exposure

<!-- section_id: "d26f02f7-cc5f-431c-98b5-2fe5e0caa384" -->
### For Windows/macOS Users

1. **You're Also Affected**:
   - Internet research shows Windows users experiencing the same issues
   - This is likely a Cursor IDE bug, not OS-specific
   - Check your Cursor version (2.0.77 has known bug)

2. **Test and Report**:
   - Verify if Playwright MCP tools are actually exposed
   - Verify if Browser MCP tools are actually exposed
   - Document findings and Cursor version
   - Report to Cursor forum if tools aren't exposed

<!-- section_id: "506eff42-fcf9-4c58-a7fa-7fbe8a704c4b" -->
### For All Users

1. **Check Cursor Settings**:
   - Go to Settings → Tools & MCP
   - Verify which tools are listed as available
   - Compare what's listed vs. what's accessible to agents

2. **Test After Configuration Changes**:
   - Restart Cursor completely
   - Verify tool availability
   - Document what works and what doesn't

<!-- section_id: "cc3058be-9a2d-4f8e-b676-8f1ea8ad1434" -->
## Testing Checklist

<!-- section_id: "46e18dd1-8c43-4cc8-ada2-3510ba1ef0d8" -->
### Linux/WSL Testing
- [x] Playwright MCP server connects
- [x] Playwright MCP tools registered
- [x] Playwright MCP tools NOT exposed to agents
- [x] Browser MCP server connects
- [x] Browser MCP tools registered
- [x] Browser MCP tools NOT exposed to agents (WSL)
- [x] Cursor browser extension tools available
- [x] Environment variables fix browser detection

<!-- section_id: "c1aa59dd-843b-4b80-a0a7-00907f0b65dd" -->
### Windows Testing Needed
- [ ] Playwright MCP server connects
- [ ] Playwright MCP tools registered
- [ ] Playwright MCP tools exposed to agents?
- [ ] Browser MCP server connects
- [ ] Browser MCP tools registered
- [ ] Browser MCP tools exposed to agents?
- [ ] Cursor browser extension tools available
- [ ] Configuration requirements

<!-- section_id: "fcbca82b-1ae2-4cd8-8392-d257f77ec8bf" -->
### macOS Testing Needed
- [ ] Playwright MCP server connects
- [ ] Playwright MCP tools registered
- [ ] Playwright MCP tools exposed to agents?
- [ ] Browser MCP server connects
- [ ] Browser MCP tools registered
- [ ] Browser MCP tools exposed to agents?
- [ ] Cursor browser extension tools available
- [ ] Configuration requirements

<!-- section_id: "a5b8b201-7f11-4436-937c-5a555dd05344" -->
## Related Documentation

- [Cursor IDE Linux MCP Issues](./CURSOR_IDE_LINUX_MCP_ISSUES.md) - Linux-specific issues
- [Browser MCP Setup Experience](./BROWSER_MCP_SETUP_EXPERIENCE.md) - Lessons learned
- [Cursor Browser MCP Setup](./CURSOR_BROWSER_MCP_SETUP.md) - WSL setup notes
- [MCP Configuration Guide](./MCP_CONFIGURATION_GUIDE.md) - Configuration details

<!-- section_id: "205e8319-f0d4-413f-b4fc-20753a82b858" -->
## References

<!-- section_id: "89b1ff99-aa56-40dc-9eb8-756846563125" -->
### Internet Research Sources (2025-12-05)

1. **Cursor Forum Posts**:
   - "MCP servers are not exposed to agents" - mentions version 2.0.77 bug
   - "Browser Agent Tools Not Accessible Despite 'Ready' Status"
   - "Playwright MCP not working on Cursor"
   - "Cursor agent unable to use the HuggingFace MCP tools"

2. **GitHub Issues**:
   - Multiple reports of MCP tools not working on Windows
   - Playwright MCP WSL compatibility issues
   - Browser tools MCP Windows issues

3. **Community Reports**:
   - Reddit discussions about MCP setup failures on Windows
   - Forum discussions about cross-platform MCP issues

<!-- section_id: "4450265a-93a0-492f-93fa-135714891273" -->
## Changelog

<!-- section_id: "a25ead2e-e882-4e7c-89d9-e8ed5e91d0ba" -->
### 2025-12-05 (Updated)
- **CRITICAL UPDATE**: Internet research reveals this is NOT OS-specific
- Cursor version 2.0.77 has known bug affecting all platforms
- Windows users also experiencing MCP tool exposure issues
- Revised understanding: This is a Cursor IDE bug, not Linux/WSL-specific
- Updated recommendations for all platforms
- Added internet research sources and references

<!-- section_id: "56bc03c0-7f24-42c2-b71a-5d61906f130f" -->
### 2025-12-05 (Initial)
- Created comprehensive OS analysis document
- Documented WSL finding: Browser MCP tools also not exposed
- Identified that Windows/macOS status was unknown (assumed, not tested)
- Analyzed configuration vs. OS-specific causes
- Added testing checklist for all platforms

---

**This document provides a comprehensive analysis of MCP tool exposure across platforms and identifies areas needing further testing and investigation.**

