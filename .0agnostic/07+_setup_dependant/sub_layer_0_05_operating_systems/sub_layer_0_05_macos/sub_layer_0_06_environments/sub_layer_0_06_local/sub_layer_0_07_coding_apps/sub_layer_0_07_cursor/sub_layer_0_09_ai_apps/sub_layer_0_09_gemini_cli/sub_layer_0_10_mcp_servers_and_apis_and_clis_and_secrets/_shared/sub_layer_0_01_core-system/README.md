---
resource_id: "a6d9658a-74c3-409a-a29e-f88b2595db69"
resource_type: "readme
document"
resource_name: "README"
---
# 0.01 Core System (MCP Servers & Tools Setup)

This folder contains **cross-OS / cross-app** documentation for how we manage MCP servers and tool availability across AI apps (Codex CLI, Claude Code CLI, Gemini CLI, Cursor Agent).

<!-- section_id: "51400185-f696-483b-8d47-3dec06ed91f7" -->
## Where Things Live

```text
sub_layer_0_10_mcp_servers_and_tools_setup/
├── 0.01_core-system/                      # This folder (system-level docs)
├── 0.02_mcp_config_options_0_file_tree_0/  # Traversable tree (OS → App → Server → issues)
└── 0.06_automation/                       # Automation scripts and runbooks
```

<!-- section_id: "64394e98-f93c-4961-8efc-dfefaff1de57" -->
## Start Here

- **MCP Server Matrix**: `MCP_SERVER_MATRIX.md` (what servers exist, where they’re used, and automation status)
- **Browser Routing Table**: `BROWSER_MCP_ROUTING_TABLE.md` (which browser MCP to use per AI app / OS)
- **Codex CLI MCP Setup**: `CODEX_CLI_MCP_SETUP.md` (where Codex config lives; enable/disable patterns)
- **System Guide**: `MCP_SYSTEM_GUIDE.md` (overall architecture and conventions)

<!-- section_id: "1a92e7ab-14e1-41a4-94a4-ac1b01c94082" -->
## Detailed Per-OS / Per-App Docs

Use the traversable file tree:

- `../0.02_mcp_config_options_0_file_tree_0/README.md`
- `../0.02_mcp_config_options_0_file_tree_0/0.03_operating_systems/`

<!-- section_id: "a1dea4ed-cd07-4b56-886f-44b9283708e6" -->
## Automation

Runbooks and scripts live in:

- `../0.06_automation/README.md`
- `../0.06_automation/CONCURRENT_BROWSER_SETUP.md`

<!-- section_id: "d81a6c84-a408-419e-b02b-c65cb89cbe43" -->
## Secrets

Do not commit API keys. Use local env files (e.g., `~/.codex/mcp.env`) and have automation inject them into client configs.
