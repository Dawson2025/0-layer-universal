---
resource_id: "2ed01f11-63c8-4f64-a6b8-d268ae3295fe"
resource_type: "readme
document"
resource_name: "README"
---
# 0.01 Core System (MCP Servers & Tools Setup)

This folder contains **cross-OS / cross-app** documentation for how we manage MCP servers and tool availability across AI apps (Codex CLI, Claude Code CLI, Gemini CLI, Cursor Agent).

<!-- section_id: "37b71e9d-436d-4369-b656-d297ff801e28" -->
## Where Things Live

```text
sub_layer_0_10_mcp_servers_and_tools_setup/
├── 0.01_core-system/                      # This folder (system-level docs)
├── 0.02_mcp_config_options_0_file_tree_0/  # Traversable tree (OS → App → Server → issues)
└── 0.06_automation/                       # Automation scripts and runbooks
```

<!-- section_id: "91818ee1-248a-4539-9ed3-2127aa7b82c9" -->
## Start Here

- **MCP Server Matrix**: `MCP_SERVER_MATRIX.md` (what servers exist, where they’re used, and automation status)
- **Browser Routing Table**: `BROWSER_MCP_ROUTING_TABLE.md` (which browser MCP to use per AI app / OS)
- **Codex CLI MCP Setup**: `CODEX_CLI_MCP_SETUP.md` (where Codex config lives; enable/disable patterns)
- **System Guide**: `MCP_SYSTEM_GUIDE.md` (overall architecture and conventions)

<!-- section_id: "f2942582-84b6-4716-80f5-edec0ca56bfd" -->
## Detailed Per-OS / Per-App Docs

Use the traversable file tree:

- `../0.02_mcp_config_options_0_file_tree_0/README.md`
- `../0.02_mcp_config_options_0_file_tree_0/0.03_operating_systems/`

<!-- section_id: "2d8727a1-5a52-427f-a91a-1f2f7ea6cd18" -->
## Automation

Runbooks and scripts live in:

- `../0.06_automation/README.md`
- `../0.06_automation/CONCURRENT_BROWSER_SETUP.md`

<!-- section_id: "f6c927a5-6cbd-4c52-8b9c-0c64393fa20a" -->
## Secrets

Do not commit API keys. Use local env files (e.g., `~/.codex/mcp.env`) and have automation inject them into client configs.
