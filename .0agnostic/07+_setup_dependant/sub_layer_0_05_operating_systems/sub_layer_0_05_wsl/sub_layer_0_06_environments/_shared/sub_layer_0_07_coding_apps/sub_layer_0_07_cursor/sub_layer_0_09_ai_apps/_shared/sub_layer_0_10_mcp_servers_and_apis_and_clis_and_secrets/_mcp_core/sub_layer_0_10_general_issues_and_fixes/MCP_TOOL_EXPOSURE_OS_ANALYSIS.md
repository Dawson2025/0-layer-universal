---
resource_id: "f4a5bf0e-3da8-48d4-97c4-3addec399a89"
resource_type: "document"
resource_name: "MCP_TOOL_EXPOSURE_OS_ANALYSIS"
---
# MCP Tool Exposure - OS and Configuration Analysis

**Date**: 2025-12-05  
**Location**: Universal Layer → MCP Servers and Tools Setup  
**Status**: Comprehensive analysis of MCP tool exposure across platforms

<!-- section_id: "1188c181-b5a2-4176-81e2-ac09832a863a" -->
## Overview

This document analyzes MCP (Model Context Protocol) tool exposure issues across different operating systems and investigates whether problems are OS-specific or configuration-related.

<!-- section_id: "4790e067-e38b-43eb-a716-da09d95d3385" -->
## Executive Summary

<!-- section_id: "91b630af-737e-4838-883b-cc3bc87c647c" -->
### Confirmed Issues by Platform

| Platform | Playwright MCP Tools | Browser MCP Tools | Cursor Extension Tools | Status |
|----------|---------------------|-------------------|----------------------|--------|
| **Linux (Native)** | ❌ Not Exposed | ⚠️ May Not Be Exposed | ✅ Available | Documented Issue |
| **WSL2 (Ubuntu)** | ❌ Not Exposed | ❌ Not Exposed | ✅ Available | **NEW FINDING** |
| **Windows (Native)** | ⚠️ **Also Affected** | ⚠️ **Also Affected** | ⚠️ **Also Affected** | **CRITICAL FINDING** |
| **macOS** | ⚠️ **Likely Affected** | ⚠️ **Likely Affected** | ⚠️ **Likely Affected** | **Based on Reports** |

<!-- section_id: "c718104d-3f11-4919-80d1-3f7eed37caea" -->
### Critical Discovery (2025-12-05)

**This is NOT just a Linux/WSL issue!** Internet research reveals:

1. **Cursor Version 2.0.77 Bug**: Known issue where MCP tools aren't exposed to agents even though they appear connected
2. **Windows Users Also Affected**: Multiple forum reports of MCP tools not being exposed on Windows
3. **Cross-Platform Issue**: Reports of MCP tool exposure problems across Linux, Windows, and potentially macOS
4. **Cursor IDE Bug**: This appears to be a Cursor IDE bug, not OS-specific

<!-- section_id: "217fd305-a74b-408e-8d4e-5d646a2a04c3" -->
### Key Findings

1. **Linux/WSL Issue Confirmed**: Playwright MCP tools are NOT exposed to AI agents on Linux and WSL, even when servers connect successfully
2. **WSL-Specific Finding (2025-12-05)**: Browser MCP tools (`mcp_browser_*`) are also NOT exposed in WSL, despite server running
3. **Configuration vs. OS**: Environment variable configuration fixes browser detection, but does NOT fix tool exposure issues
4. **Windows/macOS Status**: Unknown - documentation assumes they work, but no confirmed testing

<!-- section_id: "95638676-b101-45d7-b97e-b82ec477559a" -->
## Detailed Platform Analysis

<!-- section_id: "4d61d0ee-5241-4448-bad9-d08e764cf938" -->
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

<!-- section_id: "e5c6a0e2-3b73-4b9a-be4f-8257ba5780fc" -->
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

<!-- section_id: "e0be4043-0695-45c6-84b2-0b1b2c41b8b4" -->
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

<!-- section_id: "b827d72c-59c4-4c56-baa2-78b288d411c4" -->
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

<!-- section_id: "00cfa681-186d-458f-813a-648b252b2d4f" -->
## Critical Finding: This is NOT OS-Specific!

<!-- section_id: "ce98e95d-6955-4025-abda-0cc905f9bcd4" -->
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

<!-- section_id: "55e842ac-8bc0-4fd9-863d-9bb15227299e" -->
### Revised Understanding

**Previous Assumption** (Incorrect):
- "Linux/Ubuntu systems experience unique challenges with MCP servers in Cursor IDE that don't occur on Windows or macOS"

**Actual Finding** (Correct):
- This is a **Cursor IDE bug** affecting multiple platforms
- Linux/WSL may have additional issues (sandboxing, path resolution)
- But the core tool exposure problem affects Windows and likely macOS too
- Cursor version 2.0.77 specifically has this known bug

<!-- section_id: "9600522b-731b-47c0-9c58-550d03d43026" -->
## Configuration vs. OS Analysis

<!-- section_id: "6e7e4954-bb6d-46b0-9f7f-e76c47a2cb6d" -->
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

<!-- section_id: "ef4376af-185b-4619-94bc-ac1ebce5ee6b" -->
## Recommendations

<!-- section_id: "3889a32d-42dc-4d71-aa50-2750d21abb84" -->
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

<!-- section_id: "daa2f255-cf75-41c2-8612-4ac561632b77" -->
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

<!-- section_id: "9a81d0e1-dc93-48a3-8329-48720611831d" -->
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

<!-- section_id: "a8db6bd0-e588-4fcf-a263-b1ab75467a73" -->
### For All Users

1. **Check Cursor Settings**:
   - Go to Settings → Tools & MCP
   - Verify which tools are listed as available
   - Compare what's listed vs. what's accessible to agents

2. **Test After Configuration Changes**:
   - Restart Cursor completely
   - Verify tool availability
   - Document what works and what doesn't

<!-- section_id: "db878783-a31b-4843-ad89-7c4a0fbdbd89" -->
## Testing Checklist

<!-- section_id: "4327c47a-3d1e-4c13-a454-21b27612eac2" -->
### Linux/WSL Testing
- [x] Playwright MCP server connects
- [x] Playwright MCP tools registered
- [x] Playwright MCP tools NOT exposed to agents
- [x] Browser MCP server connects
- [x] Browser MCP tools registered
- [x] Browser MCP tools NOT exposed to agents (WSL)
- [x] Cursor browser extension tools available
- [x] Environment variables fix browser detection

<!-- section_id: "f342bcef-af87-4564-b232-66587ee72477" -->
### Windows Testing Needed
- [ ] Playwright MCP server connects
- [ ] Playwright MCP tools registered
- [ ] Playwright MCP tools exposed to agents?
- [ ] Browser MCP server connects
- [ ] Browser MCP tools registered
- [ ] Browser MCP tools exposed to agents?
- [ ] Cursor browser extension tools available
- [ ] Configuration requirements

<!-- section_id: "02078ce8-0f34-4d3d-be9a-a0c0bcf5fa21" -->
### macOS Testing Needed
- [ ] Playwright MCP server connects
- [ ] Playwright MCP tools registered
- [ ] Playwright MCP tools exposed to agents?
- [ ] Browser MCP server connects
- [ ] Browser MCP tools registered
- [ ] Browser MCP tools exposed to agents?
- [ ] Cursor browser extension tools available
- [ ] Configuration requirements

<!-- section_id: "aeb1f83f-7425-47c9-827d-453ad570727d" -->
## Related Documentation

- [Cursor IDE Linux MCP Issues](./CURSOR_IDE_LINUX_MCP_ISSUES.md) - Linux-specific issues
- [Browser MCP Setup Experience](./BROWSER_MCP_SETUP_EXPERIENCE.md) - Lessons learned
- [Cursor Browser MCP Setup](./CURSOR_BROWSER_MCP_SETUP.md) - WSL setup notes
- [MCP Configuration Guide](./MCP_CONFIGURATION_GUIDE.md) - Configuration details

<!-- section_id: "f9d5e8b8-c639-4135-8c3d-d1162b9aff39" -->
## References

<!-- section_id: "c0feb876-c3e2-400c-8487-a26d6465ca41" -->
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

<!-- section_id: "6dffba75-bc47-4be1-98ed-eb025d0e3336" -->
## Changelog

<!-- section_id: "4f034bb4-ff79-4963-8bfb-4f1ee0140afe" -->
### 2025-12-05 (Updated)
- **CRITICAL UPDATE**: Internet research reveals this is NOT OS-specific
- Cursor version 2.0.77 has known bug affecting all platforms
- Windows users also experiencing MCP tool exposure issues
- Revised understanding: This is a Cursor IDE bug, not Linux/WSL-specific
- Updated recommendations for all platforms
- Added internet research sources and references

<!-- section_id: "973e7f6f-6134-4f3b-9252-2da60cc98ee8" -->
### 2025-12-05 (Initial)
- Created comprehensive OS analysis document
- Documented WSL finding: Browser MCP tools also not exposed
- Identified that Windows/macOS status was unknown (assumed, not tested)
- Analyzed configuration vs. OS-specific causes
- Added testing checklist for all platforms

---

**This document provides a comprehensive analysis of MCP tool exposure across platforms and identifies areas needing further testing and investigation.**

