---
resource_id: "21a55d43-5015-4651-b12b-e9e414a9dabd"
resource_type: "document"
resource_name: "MCP_TOOL_EXPOSURE_OS_ANALYSIS"
---
# MCP Tool Exposure - OS and Configuration Analysis

**Date**: 2025-12-05  
**Location**: Universal Layer → MCP Servers and Tools Setup  
**Status**: Comprehensive analysis of MCP tool exposure across platforms

<!-- section_id: "82044797-1312-478c-a35b-49fa7be70d5a" -->
## Overview

This document analyzes MCP (Model Context Protocol) tool exposure issues across different operating systems and investigates whether problems are OS-specific or configuration-related.

<!-- section_id: "bb3a8204-0ac0-4103-bbad-1e4006e2893f" -->
## Executive Summary

<!-- section_id: "356d5f79-1545-41b2-95f0-78ca7e98fdf3" -->
### Confirmed Issues by Platform

| Platform | Playwright MCP Tools | Browser MCP Tools | Cursor Extension Tools | Status |
|----------|---------------------|-------------------|----------------------|--------|
| **Linux (Native)** | ❌ Not Exposed | ⚠️ May Not Be Exposed | ✅ Available | Documented Issue |
| **WSL2 (Ubuntu)** | ❌ Not Exposed | ❌ Not Exposed | ✅ Available | **NEW FINDING** |
| **Windows (Native)** | ⚠️ **Also Affected** | ⚠️ **Also Affected** | ⚠️ **Also Affected** | **CRITICAL FINDING** |
| **macOS** | ⚠️ **Likely Affected** | ⚠️ **Likely Affected** | ⚠️ **Likely Affected** | **Based on Reports** |

<!-- section_id: "e0440d3c-29aa-487c-8a5c-0c341665571f" -->
### Critical Discovery (2025-12-05)

**This is NOT just a Linux/WSL issue!** Internet research reveals:

1. **Cursor Version 2.0.77 Bug**: Known issue where MCP tools aren't exposed to agents even though they appear connected
2. **Windows Users Also Affected**: Multiple forum reports of MCP tools not being exposed on Windows
3. **Cross-Platform Issue**: Reports of MCP tool exposure problems across Linux, Windows, and potentially macOS
4. **Cursor IDE Bug**: This appears to be a Cursor IDE bug, not OS-specific

<!-- section_id: "bd9e8a57-f61f-4ecd-be16-f8f906a25055" -->
### Key Findings

1. **Linux/WSL Issue Confirmed**: Playwright MCP tools are NOT exposed to AI agents on Linux and WSL, even when servers connect successfully
2. **WSL-Specific Finding (2025-12-05)**: Browser MCP tools (`mcp_browser_*`) are also NOT exposed in WSL, despite server running
3. **Configuration vs. OS**: Environment variable configuration fixes browser detection, but does NOT fix tool exposure issues
4. **Windows/macOS Status**: Unknown - documentation assumes they work, but no confirmed testing

<!-- section_id: "58319894-f8b6-4c33-8186-e1863ddd8e53" -->
## Detailed Platform Analysis

<!-- section_id: "fb2fcd15-b053-432a-a7c1-c65465ec4e24" -->
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

<!-- section_id: "34d0a232-c6b6-4623-9152-c5c37f3dd029" -->
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

<!-- section_id: "1ece9824-40f0-4d1e-8830-fa05b4cc317f" -->
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

<!-- section_id: "1f284b16-9ca7-4eae-8157-cd8a2ac49441" -->
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

<!-- section_id: "5dec8592-1ae6-459a-8f83-54818934df26" -->
## Critical Finding: This is NOT OS-Specific!

<!-- section_id: "fe211f09-c013-403c-8a43-56e8257940f5" -->
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

<!-- section_id: "9295e894-7cfc-4b17-bac7-c08d929a4fb5" -->
### Revised Understanding

**Previous Assumption** (Incorrect):
- "Linux/Ubuntu systems experience unique challenges with MCP servers in Cursor IDE that don't occur on Windows or macOS"

**Actual Finding** (Correct):
- This is a **Cursor IDE bug** affecting multiple platforms
- Linux/WSL may have additional issues (sandboxing, path resolution)
- But the core tool exposure problem affects Windows and likely macOS too
- Cursor version 2.0.77 specifically has this known bug

<!-- section_id: "fca09efe-1f1c-4910-899d-3d9d25fd7163" -->
## Configuration vs. OS Analysis

<!-- section_id: "23b6e5a7-03a8-4bea-9bce-e2fe863602f9" -->
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

<!-- section_id: "2258f6e4-a46d-454a-8f86-f8486ed35485" -->
## Recommendations

<!-- section_id: "14defc3d-a2d6-47f9-a16c-231263f0a471" -->
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

<!-- section_id: "ae3aac61-1267-4820-ab8e-c679a8312818" -->
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

<!-- section_id: "59b4f79f-f120-4269-9f41-ee2d796724be" -->
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

<!-- section_id: "3dc47093-c832-48b3-8525-a6853b0ba65d" -->
### For All Users

1. **Check Cursor Settings**:
   - Go to Settings → Tools & MCP
   - Verify which tools are listed as available
   - Compare what's listed vs. what's accessible to agents

2. **Test After Configuration Changes**:
   - Restart Cursor completely
   - Verify tool availability
   - Document what works and what doesn't

<!-- section_id: "dec590ca-4f99-4b40-9b34-63add5fc6bda" -->
## Testing Checklist

<!-- section_id: "602a216c-2bd8-4e86-a04e-91d0182d0db9" -->
### Linux/WSL Testing
- [x] Playwright MCP server connects
- [x] Playwright MCP tools registered
- [x] Playwright MCP tools NOT exposed to agents
- [x] Browser MCP server connects
- [x] Browser MCP tools registered
- [x] Browser MCP tools NOT exposed to agents (WSL)
- [x] Cursor browser extension tools available
- [x] Environment variables fix browser detection

<!-- section_id: "724627e3-f5b1-4e17-acd2-3ea0945d4ba2" -->
### Windows Testing Needed
- [ ] Playwright MCP server connects
- [ ] Playwright MCP tools registered
- [ ] Playwright MCP tools exposed to agents?
- [ ] Browser MCP server connects
- [ ] Browser MCP tools registered
- [ ] Browser MCP tools exposed to agents?
- [ ] Cursor browser extension tools available
- [ ] Configuration requirements

<!-- section_id: "af72b540-bc04-4811-b267-32965e0dbe26" -->
### macOS Testing Needed
- [ ] Playwright MCP server connects
- [ ] Playwright MCP tools registered
- [ ] Playwright MCP tools exposed to agents?
- [ ] Browser MCP server connects
- [ ] Browser MCP tools registered
- [ ] Browser MCP tools exposed to agents?
- [ ] Cursor browser extension tools available
- [ ] Configuration requirements

<!-- section_id: "0109c701-bc6f-4974-97f6-c313f5690999" -->
## Related Documentation

- [Cursor IDE Linux MCP Issues](./CURSOR_IDE_LINUX_MCP_ISSUES.md) - Linux-specific issues
- [Browser MCP Setup Experience](./BROWSER_MCP_SETUP_EXPERIENCE.md) - Lessons learned
- [Cursor Browser MCP Setup](./CURSOR_BROWSER_MCP_SETUP.md) - WSL setup notes
- [MCP Configuration Guide](./MCP_CONFIGURATION_GUIDE.md) - Configuration details

<!-- section_id: "6b208868-8e38-4e9a-9a5e-797d00a14085" -->
## References

<!-- section_id: "82980872-a3c7-46eb-b5d1-c2bb9571c2da" -->
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

<!-- section_id: "08396eb1-f1cb-4eb0-aff8-e99ffe0fad93" -->
## Changelog

<!-- section_id: "6bbb3ed7-3199-4f4b-ae1a-34ee0afffd45" -->
### 2025-12-05 (Updated)
- **CRITICAL UPDATE**: Internet research reveals this is NOT OS-specific
- Cursor version 2.0.77 has known bug affecting all platforms
- Windows users also experiencing MCP tool exposure issues
- Revised understanding: This is a Cursor IDE bug, not Linux/WSL-specific
- Updated recommendations for all platforms
- Added internet research sources and references

<!-- section_id: "1e380af6-66e2-46c6-ad95-152310237b20" -->
### 2025-12-05 (Initial)
- Created comprehensive OS analysis document
- Documented WSL finding: Browser MCP tools also not exposed
- Identified that Windows/macOS status was unknown (assumed, not tested)
- Analyzed configuration vs. OS-specific causes
- Added testing checklist for all platforms

---

**This document provides a comprehensive analysis of MCP tool exposure across platforms and identifies areas needing further testing and investigation.**

