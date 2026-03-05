---
resource_id: "8cc17db2-a9d0-44c3-96de-6cefc9d61b08"
resource_type: "readme
document"
resource_name: "README"
---
# 0.01 Core System (MCP Servers & Tools Setup)

This folder contains **cross-OS / cross-app** documentation for how we manage MCP servers and tool availability across AI apps (Codex CLI, Claude Code CLI, Gemini CLI, Cursor Agent).

<!-- section_id: "ba7f1332-cf5c-48b0-91ad-9c1db4caf040" -->
## Where Things Live

```text
sub_layer_0_10_mcp_servers_and_tools_setup/
├── 0.01_core-system/                      # This folder (system-level docs)
├── 0.02_mcp_config_options_0_file_tree_0/  # Traversable tree (OS → App → Server → issues)
└── 0.06_automation/                       # Automation scripts and runbooks
```

<!-- section_id: "6f11bf6a-c80d-4cfd-bd7b-288306fa79df" -->
## Start Here

- **MCP Server Matrix**: `MCP_SERVER_MATRIX.md` (what servers exist, where they’re used, and automation status)
- **Browser Routing Table**: `BROWSER_MCP_ROUTING_TABLE.md` (which browser MCP to use per AI app / OS)
- **Codex CLI MCP Setup**: `CODEX_CLI_MCP_SETUP.md` (where Codex config lives; enable/disable patterns)
- **System Guide**: `MCP_SYSTEM_GUIDE.md` (overall architecture and conventions)

<!-- section_id: "84e9e1fb-0070-4a51-bf1e-a22ddbb99a34" -->
## Detailed Per-OS / Per-App Docs

Use the traversable file tree:

- `../0.02_mcp_config_options_0_file_tree_0/README.md`
- `../0.02_mcp_config_options_0_file_tree_0/0.03_operating_systems/`

<!-- section_id: "4845e6f5-21f5-4075-816c-b140c484f674" -->
## Automation

Runbooks and scripts live in:

- `../0.06_automation/README.md`
- `../0.06_automation/CONCURRENT_BROWSER_SETUP.md`

<!-- section_id: "0feaa3af-e986-48fa-b093-e16b99c40c2f" -->
## Secrets

Do not commit API keys. Use local env files (e.g., `~/.codex/mcp.env`) and have automation inject them into client configs.
