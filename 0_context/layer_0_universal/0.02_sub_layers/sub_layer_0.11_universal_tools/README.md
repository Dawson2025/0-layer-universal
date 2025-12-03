# sub_layer_0.11_universal_tools

**Purpose**: Cross-project scripts, utilities, and universal tools.

## Overview

This sublayer contains universal tools, scripts, and utilities that can be used across multiple projects. This includes browser automation tools, Claude Code configuration, AI development frameworks, and other cross-cutting utilities.

## Structure

```
sub_layer_0.11_universal_tools/
└── trickle_down_0.75_universal_tools/
    └── 0_instruction_docs/
        ├── browser-automation/
        ├── claude-code-config/
        ├── ai-development-frameworks/
        ├── platform-version-control/
        └── ...
```

## Relationship to Other Sublayers

- **Depends on**: 
  - `sub_layer_0.08_ai_apps_tools_setup` - Tools may require AI apps to be set up first
  - `sub_layer_0.09_mcp_servers_and_tools_setup` - Some tools may use MCP servers
- **Provides to**: All layers that need universal utilities and scripts

## Key Documentation

- **[Browser Automation](trickle_down_0.75_universal_tools/0_instruction_docs/browser-automation/README.md)**: Browser automation tools and guides
- **[Claude Code Config](trickle_down_0.75_universal_tools/0_instruction_docs/claude-code-config/README.md)**: Claude Code CLI configuration
- **[AI Development Frameworks](trickle_down_0.75_universal_tools/0_instruction_docs/ai-development-frameworks/README.md)**: AI coding assistant frameworks

## ⚠️ Linux/Ubuntu-Specific Tool Access Issues

**CRITICAL**: Universal tools that depend on MCP have Linux-specific limitations. Read:

- **[Linux/Ubuntu Tool Access Issues](trickle_down_0.75_universal_tools/0_instruction_docs/LINUX_UBUNTU_TOOL_ACCESS_ISSUES.md)**: Universal tool access limitations on Linux

**Key Issues**:
- Browser automation tools must use `mcp_browser_*` instead of `mcp_playwright_*`
- Development frameworks need Linux-specific adaptations
- Cross-cutting utilities may require tool name updates
- Tool migration guide available for Playwright → Browser MCP

**Related Documentation**:
- **OS-Level Issues**: `../sub_layer_0.05_os_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MCP_ISSUES.md`
- **Cursor IDE Issues**: `../sub_layer_0.06_coding_app_setup/trickle_down_0.5_setup/0_instruction_docs/CURSOR_IDE_LINUX_MCP_ISSUES.md`
- **MCP Setup**: `../sub_layer_0.09_mcp_servers_and_tools_setup/`

## Notes

- MCP-related tools have been moved to `sub_layer_0.09_mcp_servers_and_tools_setup`
- Universal tools are used by agents configured in `sub_layer_0.12_agent_setup`
- Add slot-specific docs here over time
- Keep mappings up to date if paths change

---

**Last Updated**: 2025-12-02  
**Version**: 1.0
