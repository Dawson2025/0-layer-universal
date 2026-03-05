---
resource_id: "c028fbc8-c5a3-4b13-8bfc-5c0d718ca1c1"
resource_type: "document"
resource_name: "README_root_previous"
---
# archived: sub_layer_0_10_mcp_servers_and_tools_setup (previous README)

**Purpose**: MCP (Model Context Protocol) server setup and configuration for AI apps and tools.

<!-- section_id: "62f3b7c7-0850-448a-9ae9-1eb41c039c6e" -->
## Overview

This sublayer contains documentation and configuration for setting up MCP servers across different AI applications and tools. MCP setup is dependent on which AI app/tool it's being configured for (Cursor IDE, Claude Code, etc.).

<!-- section_id: "fad90256-88d7-4a24-bc9c-001f6a53fb5a" -->
## Structure

```
sub_layer_0_10_mcp_servers_and_tools_setup/
├── 0.01_core-system/                      # Cross-app system docs (source of truth)
├── 0.02_ai_apps/                          # App-specific MCP setup runbooks
│   ├── claude_code_cli/
│   ├── gemini_cli/
│   ├── codex_cli/
│   └── cursor_agent/
├── 0.02_mcp_config_options_0_file_tree_0/  # Traversable file tree (OS → AI app → MCP options → issues)
│   └── operating_system/
│       ├── windows/
│       ├── wsl/
│       ├── macos/
│       └── linux_ubuntu/
├── 0.06_automation/                       # Setup automation scripts
├── 0.04_general-issues ->                 # Compatibility link (contents live in file tree)
└── 0.05_mcp_servers ->                    # Compatibility link (contents live in file tree)
```

<!-- section_id: "74110103-eeae-4db4-9e51-4122b54a6427" -->
## Relationship to Other Sublayers

- **Depends on**: `sub_layer_0_09_ai_apps_tools_setup` - MCP setup requires the AI app/tool to be installed first
- **Provides to**: All layers that need browser automation, documentation tools, or other MCP capabilities

<!-- section_id: "8f29bdb6-b1b7-4c8a-b588-c2a8fb9a7d6d" -->
## Key Documentation

<!-- section_id: "2b209541-8adb-4132-9647-273b4de629fe" -->
### Core Setup Guides
- **[MCP System Guide](trickle_down_0.75_universal_tools/0_instruction_docs/mcp-tools/MCP_SYSTEM_GUIDE.md)**: Complete MCP management system
- **[MCP Configuration Guide](trickle_down_0.75_universal_tools/0_instruction_docs/mcp-tools/MCP_CONFIGURATION_GUIDE.md)**: How to configure MCP servers
- **[Cursor Browser MCP Setup](trickle_down_0.75_universal_tools/0_instruction_docs/mcp-tools/CURSOR_BROWSER_MCP_SETUP.md)**: Cursor IDE-specific browser MCP setup
- **[Browser MCP Setup Experience](trickle_down_0.75_universal_tools/0_instruction_docs/mcp-tools/BROWSER_MCP_SETUP_EXPERIENCE.md)**: Linux/Ubuntu-specific issues and lessons learned

<!-- section_id: "93c12f55-3851-4179-a484-36954d566e58" -->
### Critical Issue Documentation (2025-12-05)
- **[Playwright MCP Working Solution](trickle_down_0.75_universal_tools/0_instruction_docs/mcp-tools/PLAYWRIGHT_MCP_WORKING_SOLUTION.md)**: ✅ **CONFIRMED WORKING** - Complete solution for getting Playwright MCP tools working
- **[MCP Tool Limits Research](trickle_down_0.75_universal_tools/0_instruction_docs/mcp-tools/MCP_TOOL_LIMITS_RESEARCH.md)**: ✅ **RESEARCHED** - Comprehensive findings on Cursor's 40-tool hard limit
- **[MCP Tool Exposure OS Analysis](trickle_down_0.75_universal_tools/0_instruction_docs/mcp-tools/MCP_TOOL_EXPOSURE_OS_ANALYSIS.md)**: Comprehensive analysis of MCP tool exposure across platforms - **CRITICAL: This is a Cursor IDE bug, not OS-specific**
- **[MCP Tool Exposure Solutions](trickle_down_0.75_universal_tools/0_instruction_docs/mcp-tools/MCP_TOOL_EXPOSURE_SOLUTIONS.md)**: 22 workarounds and solutions for MCP tool exposure issues
- **[Browser Environment Variable Fix](trickle_down_0.75_universal_tools/0_instruction_docs/mcp-tools/BROWSER_ENV_VAR_FIX.md)**: Fix for recurring browser installation issues
- **[Cursor IDE Linux MCP Issues](trickle_down_0.75_universal_tools/0_instruction_docs/mcp-tools/CURSOR_IDE_LINUX_MCP_ISSUES.md)**: Linux/WSL-specific MCP issues and workarounds

<!-- section_id: "92876c6d-62fc-48a9-81f9-6f405c21ef70" -->
## ⚠️ Linux/Ubuntu-Specific Issues

**CRITICAL**: Linux/Ubuntu has platform-specific MCP limitations. See related documentation:

- **OS-Level Issues**: `../../sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MCP_ISSUES.md`
- **Cursor IDE Issues**: `../../sub_layer_0_07_coding_app_setup/trickle_down_0.5_setup/0_instruction_docs/CURSOR_IDE_LINUX_MCP_ISSUES.md`
- **AI Apps Issues**: `../../sub_layer_0_09_ai_apps_tools_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_AI_APPS_MCP_ISSUES.md`

**Key Linux/WSL Limitations**:
- Playwright MCP tools are NOT exposed to AI agents on Linux/WSL (server connects but tools unavailable)
- **WSL Finding (2025-12-05)**: Browser MCP tools are also NOT exposed in WSL (more severe than native Linux)
- Browser path detection always fails - must use explicit paths (fixed with environment variables)
- NVM/Node.js requires bash wrappers in MCP configurations
- **WSL**: Only `mcp_cursor-browser-extension_*` tools are available for browser automation
- **Native Linux**: May be able to use `mcp_browser_*` tools (needs verification)

<!-- section_id: "8ef7b855-591b-4a4e-bbf8-78d61c32108d" -->
## App-Specific MCP Setup

MCP servers are configured per AI application:
- **Codex CLI**: `~/.codex/config.toml` (generated via `automation/scripts/codex_mcp_sync.py`)
- **Gemini CLI**: `~/.gemini/settings.json` (`mcpServers` block; often points to wrapper scripts)
- **Claude Code CLI**: `~/.claude.json` (project/server entries and `claude mcp` commands)
- **Cursor**: `~/.cursor/mcp.json` (IDE tool exposure quirks may apply)

See `0.02_ai_apps/` for per-app runbooks.

<!-- section_id: "235d578d-e78b-4bcd-8f47-4beea21eb305" -->
## OS-Specific MCP Setup
When a setup depends on the OS/runtime (especially browser automation), start here:
- `0.02_mcp_config_options_0_file_tree_0/0.03_operating_systems/wsl/` (WSLg headed browser notes)
- `0.02_mcp_config_options_0_file_tree_0/0.03_operating_systems/windows/`
- `0.02_mcp_config_options_0_file_tree_0/0.03_operating_systems/macos/`
- `0.02_mcp_config_options_0_file_tree_0/0.03_operating_systems/linux_ubuntu/`

<!-- section_id: "27dbf7dc-8726-4ed3-8f53-edaf5718e2c5" -->
## Common MCP Servers

- **Browser Automation**: Playwright, Chrome DevTools, Browser MCP
- **Documentation**: Context7
- **Search**: Tavily, GitHub Search
- **System**: Filesystem, PostgreSQL, Slack

---

<!-- section_id: "2f06ce55-8146-4fe2-abd4-52a0f668ab02" -->
## Recent Updates (2025-12-05)

**Major Findings**:
- **MCP Tool Exposure Issue**: Confirmed to be a Cursor IDE bug (version 2.0.77), not OS-specific
- **WSL Discovery**: Browser MCP tools also not exposed in WSL (more severe than native Linux)
- **Environment Variable Fix**: Resolved recurring browser installation issues
- **22 Workarounds Documented**: Comprehensive solutions guide created

**New Documentation**:
- `PLAYWRIGHT_MCP_WORKING_SOLUTION.md` - ✅ **CONFIRMED WORKING** - Complete solution
- `MCP_TOOL_EXPOSURE_OS_ANALYSIS.md` - Cross-platform analysis
- `MCP_TOOL_EXPOSURE_SOLUTIONS.md` - 22 workarounds and solutions
- `BROWSER_ENV_VAR_FIX.md` - Environment variable configuration fix
- `MCP_FIX_ATTEMPTS_LOG.md` - Complete testing log

**Updated Documentation**:
- `CURSOR_IDE_LINUX_MCP_ISSUES.md` - Added WSL findings
- `CURSOR_BROWSER_MCP_SETUP.md` - Added WSL limitations
- `MCP_CONFIGURATION_GUIDE.md` - Added environment variables
- `BROWSER_MCP_SETUP_EXPERIENCE.md` - Updated with environment variable solution

---

**Last Updated**: 2025-12-05  
**Version**: 2.0
