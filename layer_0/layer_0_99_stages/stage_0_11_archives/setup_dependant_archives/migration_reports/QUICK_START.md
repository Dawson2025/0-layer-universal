---
resource_id: "b568064f-ea6d-4d61-8715-dd746fc77c61"
resource_type: "document"
resource_name: "QUICK_START"
---
# Quick Start Guide - Universal Setup File Tree

<!-- section_id: "5e3b4e59-f64d-45d8-af84-b21658c46dce" -->
## What is This?

This is a **hierarchical navigable file tree** for all setup documentation. It allows you to drill down from general to specific setup configurations:

**OS → Environment → Coding App → AI App → MCP Server → AI Model → Tools → Protocols → Agents**

<!-- section_id: "4e6aca0e-e600-449c-bbd1-0f65c4fb043f" -->
## How to Use It

<!-- section_id: "7a97d10b-ec11-4f4a-8ce0-04adbb02d0d3" -->
### Start with Your OS

Navigate to: `0.05_operating_systems/<your_os>/`

- `linux_ubuntu/` - For Ubuntu/Linux systems
- `macos/` - For macOS systems
- `windows/` - For Windows systems
- `wsl/` - For Windows Subsystem for Linux
- `_shared/` - For cross-platform setup

<!-- section_id: "0e918002-6a66-499c-98f4-3c133294f7a5" -->
### Then Follow the Path

Each level has numbered directories that guide you deeper:

1. `0.05_operating_systems/` - Choose your OS
2. `0.06_environments/` - Choose your environment (dev/prod/test)
3. `0.07_coding_apps/` - Choose your IDE (vscode/cursor/vim/emacs)
4. `0.09_ai_apps/` - Choose your AI tool (claude_code_cli/cursor_agent/etc)
5. At the AI apps level, choose a sibling branch:
   - `0.10_mcp_servers_and_apis_and_secrets/` - MCP servers (browser-mcp/playwright-mcp/etc)
   - `0.11_ai_models/` - AI models (claude-sonnet/gpt-4/etc)
   - `0.12_universal_tools/` - Tools (git/docker/npm/python)
   - `0.13_protocols/` - Protocols (terminal/browser/git)
   - `0.14_agent_setup/` - Agent configuration

<!-- section_id: "6b4c9b37-dc49-4689-8a29-ac1c34587eac" -->
### Use _shared Folders

At **every level**, there's a `_shared/` folder for cross-cutting setup:

- `0.05_operating_systems/_shared/` = Works on all OSes
- `0.06_environments/_shared/` = Works in all environments
- `0.07_coding_apps/_shared/` = Works with all coding apps
- `0.09_ai_apps/_shared/` = Works with all AI apps
- `0.10_mcp_servers_and_apis_and_secrets/_shared/` = Works with all MCP servers
- `0.11_ai_models/_shared/` = Works with all AI models
- `0.12_universal_tools/_shared/` = Works with all tools
- `0.13_protocols/_shared/` = Works with all protocols
- `0.14_agent_setup/_shared/` = Works for all agent setups

<!-- section_id: "598a750c-f009-46f1-b59a-5e94e40bd943" -->
### Find Setup Documentation

Navigate to the deepest level `general_setup_and_config/` folder for actual setup instructions, configuration examples, and troubleshooting.

<!-- section_id: "2f8aa21c-192b-4c65-9680-5177ee60e41e" -->
## Quick Examples

<!-- section_id: "e9ff7550-c454-41c3-a881-f9786f08b1cb" -->
### Example 1: Git Setup (All Platforms)
```
0.05_operating_systems/_shared/
→ 0.06_environments/_shared/
→ 0.07_coding_apps/_shared/
→ 0.09_ai_apps/_shared/
→ 0.12_universal_tools/git/
→ general_setup_and_config/README.md
```

<!-- section_id: "752ba888-6950-4f58-9e85-3435fc63a5d4" -->
### Example 2: Linux + Cursor + Playwright MCP
```
0.05_operating_systems/linux_ubuntu/
→ 0.06_environments/development/
→ 0.07_coding_apps/cursor/
→ 0.09_ai_apps/cursor_agent/
→ 0.10_mcp_servers_and_apis_and_secrets/playwright-mcp/
→ general_setup_and_config/README.md
```

<!-- section_id: "5ca5aff3-ba9c-4029-95e5-f31db7922099" -->
### Example 3: Core MCP Issues (Any Setup)
```
0.05_operating_systems/_shared/
→ 0.06_environments/_shared/
→ 0.07_coding_apps/_shared/
→ 0.09_ai_apps/_shared/
→ 0.10_mcp_servers_and_apis_and_secrets/_mcp_core/
→ general_setup_and_config/README.md
```

<!-- section_id: "236b7672-98dd-4b38-a6a9-d78644c29e1d" -->
## Key Files

- **README.md** - Main documentation and navigation guide
- **STRUCTURE_VISUALIZATION.md** - Complete visual hierarchy
- **QUICK_START.md** - This file (how to get started)

<!-- section_id: "ee5b8ca2-80d9-46b2-b533-33168279aa05" -->
## Statistics

- Total directories: 99+
- Levels of hierarchy: 10 (OS through Agent Setup)
- _shared folders at each level: Yes
- README files: 10+

<!-- section_id: "82222299-720c-4b8c-94ac-9da81a9640c7" -->
## Next Steps

1. Read `README.md` for complete documentation
2. Navigate to your specific setup path
3. Follow the setup instructions in `general_setup_and_config/`
4. Consult `STRUCTURE_VISUALIZATION.md` to understand the full hierarchy

<!-- section_id: "23a04030-6ebf-450e-b71c-ef5282d735ad" -->
## Links to Detailed Setup Sublayers

This file tree is a **navigational index**. Detailed documentation lives in:

- **sub_layer_0_05_os_setup** - OS setup details
- **sub_layer_0_06_environment_setup** - Environment setup details
- **sub_layer_0_07_coding_app_setup** - Coding app setup details
- **sub_layer_0_08_apps_browsers_extensions_setup** - Browser/extension setup
- **sub_layer_0_09_ai_apps_tools_setup** - AI app setup details
- **sub_layer_0_10_mcp_servers_and_tools_setup** - MCP server setup details
- **sub_layer_0_11_ai_models** - AI model access details
- **sub_layer_0_12_universal_tools** - Universal tool details
- **sub_layer_0_13_universal_protocols** - Protocol details
- **sub_layer_0_14_agent_setup** - Agent setup details
