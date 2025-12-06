# sub_layer_0.09_mcp_servers_and_tools_setup

**Purpose**: MCP (Model Context Protocol) server setup and configuration for AI apps and tools.

## Overview

This sublayer contains documentation and configuration for setting up MCP servers across different AI applications and tools. MCP setup is dependent on which AI app/tool it's being configured for (Cursor IDE, Claude Code, etc.).

## Structure

```
sub_layer_0.09_mcp_servers_and_tools_setup/
└── trickle_down_0.75_universal_tools/
    └── 0_instruction_docs/
        └── mcp-tools/
            ├── README.md
            ├── MCP_SYSTEM_GUIDE.md
            ├── MCP_CONFIGURATION_GUIDE.md
            ├── MCP_TOOL_EXPOSURE_OS_ANALYSIS.md (NEW - 2025-12-05)
            ├── MCP_TOOL_EXPOSURE_SOLUTIONS.md (NEW - 2025-12-05)
            ├── BROWSER_ENV_VAR_FIX.md (NEW - 2025-12-05)
            ├── CURSOR_BROWSER_MCP_SETUP.md
            ├── CURSOR_IDE_LINUX_MCP_ISSUES.md
            ├── BROWSER_MCP_SETUP_EXPERIENCE.md
            ├── PLAYWRIGHT_MCP_TESTING.md
            ├── CONTEXT7_CLAUDE_SETUP.md
            └── CONTEXT7_QUICK_REFERENCE.md
```

## Relationship to Other Sublayers

- **Depends on**: `sub_layer_0.08_ai_apps_tools_setup` - MCP setup requires the AI app/tool to be installed first
- **Provides to**: All layers that need browser automation, documentation tools, or other MCP capabilities

## Key Documentation

### Core Setup Guides
- **[MCP System Guide](trickle_down_0.75_universal_tools/0_instruction_docs/mcp-tools/MCP_SYSTEM_GUIDE.md)**: Complete MCP management system
- **[MCP Configuration Guide](trickle_down_0.75_universal_tools/0_instruction_docs/mcp-tools/MCP_CONFIGURATION_GUIDE.md)**: How to configure MCP servers
- **[Cursor Browser MCP Setup](trickle_down_0.75_universal_tools/0_instruction_docs/mcp-tools/CURSOR_BROWSER_MCP_SETUP.md)**: Cursor IDE-specific browser MCP setup
- **[Browser MCP Setup Experience](trickle_down_0.75_universal_tools/0_instruction_docs/mcp-tools/BROWSER_MCP_SETUP_EXPERIENCE.md)**: Linux/Ubuntu-specific issues and lessons learned

### Critical Issue Documentation (2025-12-05)
- **[MCP Tool Exposure OS Analysis](trickle_down_0.75_universal_tools/0_instruction_docs/mcp-tools/MCP_TOOL_EXPOSURE_OS_ANALYSIS.md)**: Comprehensive analysis of MCP tool exposure across platforms - **CRITICAL: This is a Cursor IDE bug, not OS-specific**
- **[MCP Tool Exposure Solutions](trickle_down_0.75_universal_tools/0_instruction_docs/mcp-tools/MCP_TOOL_EXPOSURE_SOLUTIONS.md)**: 22 workarounds and solutions for MCP tool exposure issues
- **[Browser Environment Variable Fix](trickle_down_0.75_universal_tools/0_instruction_docs/mcp-tools/BROWSER_ENV_VAR_FIX.md)**: Fix for recurring browser installation issues
- **[Cursor IDE Linux MCP Issues](trickle_down_0.75_universal_tools/0_instruction_docs/mcp-tools/CURSOR_IDE_LINUX_MCP_ISSUES.md)**: Linux/WSL-specific MCP issues and workarounds

## ⚠️ Linux/Ubuntu-Specific Issues

**CRITICAL**: Linux/Ubuntu has platform-specific MCP limitations. See related documentation:

- **OS-Level Issues**: `../../sub_layer_0.05_os_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MCP_ISSUES.md`
- **Cursor IDE Issues**: `../../sub_layer_0.06_coding_app_setup/trickle_down_0.5_setup/0_instruction_docs/CURSOR_IDE_LINUX_MCP_ISSUES.md`
- **AI Apps Issues**: `../../sub_layer_0.08_ai_apps_tools_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_AI_APPS_MCP_ISSUES.md`

**Key Linux/WSL Limitations**:
- Playwright MCP tools are NOT exposed to AI agents on Linux/WSL (server connects but tools unavailable)
- **WSL Finding (2025-12-05)**: Browser MCP tools are also NOT exposed in WSL (more severe than native Linux)
- Browser path detection always fails - must use explicit paths (fixed with environment variables)
- NVM/Node.js requires bash wrappers in MCP configurations
- **WSL**: Only `mcp_cursor-browser-extension_*` tools are available for browser automation
- **Native Linux**: May be able to use `mcp_browser_*` tools (needs verification)

## App-Specific MCP Setup

MCP servers are configured per AI application:
- **Cursor IDE**: `~/.cursor/mcp.json`
- **Claude Code**: `~/.claude/mcp.json`
- **Other tools**: Check respective documentation

## Common MCP Servers

- **Browser Automation**: Playwright, Chrome DevTools, Browser MCP
- **Documentation**: Context7
- **Search**: Tavily, GitHub Search
- **System**: Filesystem, PostgreSQL, Slack

---

## Recent Updates (2025-12-05)

**Major Findings**:
- **MCP Tool Exposure Issue**: Confirmed to be a Cursor IDE bug (version 2.0.77), not OS-specific
- **WSL Discovery**: Browser MCP tools also not exposed in WSL (more severe than native Linux)
- **Environment Variable Fix**: Resolved recurring browser installation issues
- **22 Workarounds Documented**: Comprehensive solutions guide created

**New Documentation**:
- `MCP_TOOL_EXPOSURE_OS_ANALYSIS.md` - Cross-platform analysis
- `MCP_TOOL_EXPOSURE_SOLUTIONS.md` - 22 workarounds and solutions
- `BROWSER_ENV_VAR_FIX.md` - Environment variable configuration fix

**Updated Documentation**:
- `CURSOR_IDE_LINUX_MCP_ISSUES.md` - Added WSL findings
- `CURSOR_BROWSER_MCP_SETUP.md` - Added WSL limitations
- `MCP_CONFIGURATION_GUIDE.md` - Added environment variables
- `BROWSER_MCP_SETUP_EXPERIENCE.md` - Updated with environment variable solution

---

**Last Updated**: 2025-12-05  
**Version**: 2.0

