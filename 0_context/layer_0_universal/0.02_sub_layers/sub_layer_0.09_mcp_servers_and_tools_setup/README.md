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
            ├── CURSOR_BROWSER_MCP_SETUP.md
            ├── PLAYWRIGHT_MCP_TESTING.md
            ├── CONTEXT7_CLAUDE_SETUP.md
            └── CONTEXT7_QUICK_REFERENCE.md
```

## Relationship to Other Sublayers

- **Depends on**: `sub_layer_0.08_ai_apps_tools_setup` - MCP setup requires the AI app/tool to be installed first
- **Provides to**: All layers that need browser automation, documentation tools, or other MCP capabilities

## Key Documentation

- **[MCP System Guide](trickle_down_0.75_universal_tools/0_instruction_docs/mcp-tools/MCP_SYSTEM_GUIDE.md)**: Complete MCP management system
- **[MCP Configuration Guide](trickle_down_0.75_universal_tools/0_instruction_docs/mcp-tools/MCP_CONFIGURATION_GUIDE.md)**: How to configure MCP servers
- **[Cursor Browser MCP Setup](trickle_down_0.75_universal_tools/0_instruction_docs/mcp-tools/CURSOR_BROWSER_MCP_SETUP.md)**: Cursor IDE-specific browser MCP setup
- **[Browser MCP Setup Experience](trickle_down_0.75_universal_tools/0_instruction_docs/mcp-tools/BROWSER_MCP_SETUP_EXPERIENCE.md)**: Linux/Ubuntu-specific issues and lessons learned

## ⚠️ Linux/Ubuntu-Specific Issues

**CRITICAL**: Linux/Ubuntu has platform-specific MCP limitations. See related documentation:

- **OS-Level Issues**: `../../sub_layer_0.05_os_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MCP_ISSUES.md`
- **Cursor IDE Issues**: `../../sub_layer_0.06_coding_app_setup/trickle_down_0.5_setup/0_instruction_docs/CURSOR_IDE_LINUX_MCP_ISSUES.md`
- **AI Apps Issues**: `../../sub_layer_0.08_ai_apps_tools_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_AI_APPS_MCP_ISSUES.md`

**Key Linux Limitations**:
- Playwright MCP tools are NOT exposed to AI agents on Linux (server connects but tools unavailable)
- Browser path detection always fails - must use explicit paths
- NVM/Node.js requires bash wrappers in MCP configurations
- Use `mcp_browser_*` tools instead of `mcp_playwright_*` on Linux

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

**Last Updated**: 2025-12-02  
**Version**: 1.0

