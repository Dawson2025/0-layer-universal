---
resource_id: "edb63735-464f-4ba5-a3d1-7cf6dd5c984d"
resource_type: "readme
document"
resource_name: "README"
---
# 0.01 Core System (MCP Servers & Tools Setup)

This folder contains **cross-OS / cross-app** documentation for how we manage MCP servers and tool availability across AI apps (Codex CLI, Claude Code CLI, Gemini CLI, Cursor Agent).

<!-- section_id: "e42fd952-2b04-425c-a8a9-fd842ddf89b9" -->
## Where Things Live

```text
sub_layer_0_10_mcp_servers_and_tools_setup/
├── 0.01_core-system/                      # This folder (system-level docs)
├── 0.02_mcp_config_options_0_file_tree_0/  # Traversable tree (OS → App → Server → issues)
└── 0.06_automation/                       # Automation scripts and runbooks
```

<!-- section_id: "eb6e44a6-b7a9-456c-90d3-d072574f48fe" -->
## Start Here

- **MCP Server Matrix**: `MCP_SERVER_MATRIX.md` (what servers exist, where they’re used, and automation status)
- **Browser Routing Table**: `BROWSER_MCP_ROUTING_TABLE.md` (which browser MCP to use per AI app / OS)
- **Codex CLI MCP Setup**: `CODEX_CLI_MCP_SETUP.md` (where Codex config lives; enable/disable patterns)
- **System Guide**: `MCP_SYSTEM_GUIDE.md` (overall architecture and conventions)

<!-- section_id: "1c6d933c-b60c-4118-a540-594e624ceeef" -->
## Detailed Per-OS / Per-App Docs

Use the traversable file tree:

- `../0.02_mcp_config_options_0_file_tree_0/README.md`
- `../0.02_mcp_config_options_0_file_tree_0/0.03_operating_systems/`

<!-- section_id: "406c146d-ceed-4a2f-a98c-7aa31365327d" -->
## Automation

Runbooks and scripts live in:

- `../0.06_automation/README.md`
- `../0.06_automation/CONCURRENT_BROWSER_SETUP.md`

<!-- section_id: "0f205f39-b059-41d0-878e-3ca955e40462" -->
## Secrets

Do not commit API keys. Use local env files (e.g., `~/.codex/mcp.env`) and have automation inject them into client configs.
