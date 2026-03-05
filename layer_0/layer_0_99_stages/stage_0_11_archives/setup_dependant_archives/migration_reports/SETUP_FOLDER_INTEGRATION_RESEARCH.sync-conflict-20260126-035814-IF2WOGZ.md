---
resource_id: "9f5a97f7-9ad3-4797-b696-1c67236bb054"
resource_type: "document"
resource_name: "SETUP_FOLDER_INTEGRATION_RESEARCH.sync-conflict-20260126-035814-IF2WOGZ"
---
# Setup Folder Integration Research

This report summarizes local context instructions and external guidance related to what should live in `setup/` folders across the hierarchy.

<!-- section_id: "eaf91de1-74a5-470e-bcbb-5f238f2b018e" -->
## Local Context Sources (Highest Priority)

Key references in the existing context system:

- `0_context/MASTER_DOCUMENTATION_INDEX.md`
  - Points to `trickle_down_0.5_setup/0_instruction_docs/` as the canonical setup procedures.
  - Explicitly lists setup sublayers for environment, AI apps/tools, MCP servers, universal tools, and agent setup.

- `0_context/layer_0/0.02_sub_layers/sub_layer_0_10_mcp_servers_and_tools_setup/0.01_core-system/`
  - Core MCP setup docs (`MCP_SYSTEM_GUIDE.md`, `MCP_CONFIGURATION_GUIDE.md`, `MCP_SERVER_MATRIX.md`, `BROWSER_MCP_ROUTING_TABLE.md`).
  - Serves as the baseline "setup" guidance for MCP server levels.

- `0_context/layer_0/0.02_sub_layers/sub_layer_0_10_mcp_servers_and_tools_setup/0.06_automation/`
  - Automation scripts and setup helpers (used to populate per-server `setup/` folders).

- `0_context/layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/`
  - OS-level setup content (WSL stability, Firebase, deployment, etc.).
  - Use this as the source for OS and environment `setup/` folders where applicable.

- `0_context/layer_0/0.02_sub_layers/sub_layer_0_12_universal_tools/`
  - Universal tools setup docs (frameworks, tooling, scripts).
  - Merged into shared universal tools in the hierarchy.

- `0_context/layer_0/0.02_sub_layers/sub_layer_0_13_universal_protocols/`
  - Protocol documentation (cli recursion, memory handling, file documentation, etc.).

- `0_context/layer_0/0.02_sub_layers/sub_layer_0_11_ai_models/`
  - Model access issues and model-specific constraints.

<!-- section_id: "d2f97429-67cb-49c7-9e28-26145e03f2be" -->
## External Guidance (Best Practice Summary)

The internet sources found are general documentation best practices and SOP templates. The recurring structure is:

- Prerequisites / system requirements
- Installation steps
- Configuration
- Verification / test checks
- Troubleshooting
- References / related docs

While generic, this aligns with how setup content is already organized in the MCP and OS sublayers.

<!-- section_id: "4ae8b9cd-800c-43c4-ab5b-6ab206333a56" -->
## Implications for the Hierarchy

Based on the local sources, the `setup/` folder at each hierarchy level should contain:

- **OS `setup/`**: OS-level install and stability guides from `sub_layer_0_05_os_setup`.
- **Environment `setup/`**: environment-specific auth/credential setup (from `sub_layer_0_07_environment_setup`).
- **Coding app `setup/`**: IDE setup, editor constraints, and platform notes (from `sub_layer_0_06_coding_app_setup`).
- **AI app `setup/`**: CLI/tool setup, auth, and provider configs (from `sub_layer_0_09_ai_apps_tools_setup`).
- **MCP server `setup/`**: automation scripts and step-by-step server setup (from `sub_layer_0_10_mcp_servers_and_tools_setup/0.06_automation`).

This report does not move content; it documents where to draw setup content from in the hierarchy.
