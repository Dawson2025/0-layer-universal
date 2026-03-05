---
resource_id: "2f7c609d-5bb3-4133-a85a-0caf72f82064"
resource_type: "document"
resource_name: "README_root_previous"
---
# archived: sub_layer_0_10_mcp_servers_and_tools_setup (previous README)

**Purpose**: MCP (Model Context Protocol) server setup and configuration for AI apps and tools.

<!-- section_id: "cf8093a6-bb09-49ad-87b7-4f552ff682bf" -->
## Overview

This sublayer contains documentation and configuration for setting up MCP servers across different AI applications and tools. MCP setup is dependent on which AI app/tool it's being configured for (Cursor IDE, Claude Code, etc.).

<!-- section_id: "8b8d5ed7-223b-4f31-8630-b03696df0792" -->
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

<!-- section_id: "96d92fa5-b6cb-43ff-8248-23a494f4b3ea" -->
## Relationship to Other Sublayers

- **Depends on**: `sub_layer_0_09_ai_apps_tools_setup` - MCP setup requires the AI app/tool to be installed first
- **Provides to**: All layers that need browser automation, documentation tools, or other MCP capabilities

<!-- section_id: "7070360b-07a9-44d0-81df-8b8f43c5ee5a" -->
## Key Documentation

<!-- section_id: "136a1303-7e7d-450d-a3d7-bf37d8c981c7" -->
### Core Setup Guides
- **[MCP System Guide](trickle_down_0.75_universal_tools/0_instruction_docs/mcp-tools/MCP_SYSTEM_GUIDE.md)**: Complete MCP management system
- **[MCP Configuration Guide](trickle_down_0.75_universal_tools/0_instruction_docs/mcp-tools/MCP_CONFIGURATION_GUIDE.md)**: How to configure MCP servers
- **[Cursor Browser MCP Setup](trickle_down_0.75_universal_tools/0_instruction_docs/mcp-tools/CURSOR_BROWSER_MCP_SETUP.md)**: Cursor IDE-specific browser MCP setup
- **[Browser MCP Setup Experience](trickle_down_0.75_universal_tools/0_instruction_docs/mcp-tools/BROWSER_MCP_SETUP_EXPERIENCE.md)**: Linux/Ubuntu-specific issues and lessons learned

<!-- section_id: "31e3c964-df8e-4441-a9b8-f9c8daa776e8" -->
### Critical Issue Documentation (2025-12-05)
- **[Playwright MCP Working Solution](trickle_down_0.75_universal_tools/0_instruction_docs/mcp-tools/PLAYWRIGHT_MCP_WORKING_SOLUTION.md)**: ✅ **CONFIRMED WORKING** - Complete solution for getting Playwright MCP tools working
- **[MCP Tool Limits Research](trickle_down_0.75_universal_tools/0_instruction_docs/mcp-tools/MCP_TOOL_LIMITS_RESEARCH.md)**: ✅ **RESEARCHED** - Comprehensive findings on Cursor's 40-tool hard limit
- **[MCP Tool Exposure OS Analysis](trickle_down_0.75_universal_tools/0_instruction_docs/mcp-tools/MCP_TOOL_EXPOSURE_OS_ANALYSIS.md)**: Comprehensive analysis of MCP tool exposure across platforms - **CRITICAL: This is a Cursor IDE bug, not OS-specific**
- **[MCP Tool Exposure Solutions](trickle_down_0.75_universal_tools/0_instruction_docs/mcp-tools/MCP_TOOL_EXPOSURE_SOLUTIONS.md)**: 22 workarounds and solutions for MCP tool exposure issues
- **[Browser Environment Variable Fix](trickle_down_0.75_universal_tools/0_instruction_docs/mcp-tools/BROWSER_ENV_VAR_FIX.md)**: Fix for recurring browser installation issues
- **[Cursor IDE Linux MCP Issues](trickle_down_0.75_universal_tools/0_instruction_docs/mcp-tools/CURSOR_IDE_LINUX_MCP_ISSUES.md)**: Linux/WSL-specific MCP issues and workarounds

<!-- section_id: "86dc3dc3-20e8-47ee-a33b-04fc13b1ab59" -->
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

<!-- section_id: "01a4863a-93e1-43e4-bb92-9945fab693a1" -->
## App-Specific MCP Setup

MCP servers are configured per AI application:
- **Codex CLI**: `~/.codex/config.toml` (generated via `automation/scripts/codex_mcp_sync.py`)
- **Gemini CLI**: `~/.gemini/settings.json` (`mcpServers` block; often points to wrapper scripts)
- **Claude Code CLI**: `~/.claude.json` (project/server entries and `claude mcp` commands)
- **Cursor**: `~/.cursor/mcp.json` (IDE tool exposure quirks may apply)

See `0.02_ai_apps/` for per-app runbooks.

<!-- section_id: "440f18c7-730c-40ab-9723-265deaed8fe8" -->
## OS-Specific MCP Setup
When a setup depends on the OS/runtime (especially browser automation), start here:
- `0.02_mcp_config_options_0_file_tree_0/0.03_operating_systems/wsl/` (WSLg headed browser notes)
- `0.02_mcp_config_options_0_file_tree_0/0.03_operating_systems/windows/`
- `0.02_mcp_config_options_0_file_tree_0/0.03_operating_systems/macos/`
- `0.02_mcp_config_options_0_file_tree_0/0.03_operating_systems/linux_ubuntu/`

<!-- section_id: "dbb8f3ef-2569-48af-8435-bbf805b69245" -->
## Common MCP Servers

- **Browser Automation**: Playwright, Chrome DevTools, Browser MCP
- **Documentation**: Context7
- **Search**: Tavily, GitHub Search
- **System**: Filesystem, PostgreSQL, Slack

---

<!-- section_id: "2f7c79d9-edfe-4b94-a9b5-05383497c163" -->
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
