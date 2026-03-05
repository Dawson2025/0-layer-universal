---
resource_id: "0bec09af-d86c-458b-8e64-10cb75009bd3"
resource_type: "readme
document"
resource_name: "README"
---
# 0.01 Core System (MCP Servers & Tools Setup)

This folder contains **cross-OS / cross-app** documentation for how we manage MCP servers and tool availability across AI apps (Codex CLI, Claude Code CLI, Gemini CLI, Cursor Agent).

<!-- section_id: "2571c2a5-449c-47ed-bac2-325f1f2c7f18" -->
## Where Things Live

```text
sub_layer_0_10_mcp_servers_and_tools_setup/
├── 0.01_core-system/                      # This folder (system-level docs)
├── 0.02_mcp_config_options_0_file_tree_0/  # Traversable tree (OS → App → Server → issues)
└── 0.06_automation/                       # Automation scripts and runbooks
```

<!-- section_id: "d3e2f9e5-6d50-4a0b-b8ad-cc0084189c48" -->
## Start Here

- **MCP Server Matrix**: `MCP_SERVER_MATRIX.md` (what servers exist, where they’re used, and automation status)
- **Browser Routing Table**: `BROWSER_MCP_ROUTING_TABLE.md` (which browser MCP to use per AI app / OS)
- **Codex CLI MCP Setup**: `CODEX_CLI_MCP_SETUP.md` (where Codex config lives; enable/disable patterns)
- **System Guide**: `MCP_SYSTEM_GUIDE.md` (overall architecture and conventions)

<!-- section_id: "cb93caa9-95d5-49b7-8044-0bb07ae9356d" -->
## Detailed Per-OS / Per-App Docs

Use the traversable file tree:

- `../0.02_mcp_config_options_0_file_tree_0/README.md`
- `../0.02_mcp_config_options_0_file_tree_0/0.03_operating_systems/`

<!-- section_id: "5f092cd7-6ef2-4f67-be78-45aee53c9b04" -->
## Automation

Runbooks and scripts live in:

- `../0.06_automation/README.md`
- `../0.06_automation/CONCURRENT_BROWSER_SETUP.md`

<!-- section_id: "39f6a2d9-a30d-46a9-8371-e4b40b20ef11" -->
## Secrets

Do not commit API keys. Use local env files (e.g., `~/.codex/mcp.env`) and have automation inject them into client configs.
