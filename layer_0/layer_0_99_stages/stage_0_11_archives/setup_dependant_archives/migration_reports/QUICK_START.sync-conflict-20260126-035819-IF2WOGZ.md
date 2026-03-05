---
resource_id: "f23ccf73-ec1e-4fc7-b475-22db8b71af4b"
resource_type: "document"
resource_name: "QUICK_START.sync-conflict-20260126-035819-IF2WOGZ"
---
# Quick Start Guide - Universal Setup File Tree

<!-- section_id: "581fe4b8-6f26-41f1-8eeb-0ddf45a81dba" -->
## What is This?

This is a **hierarchical navigable file tree** for all setup documentation. It allows you to drill down from general to specific setup configurations:

**OS → Environment → Coding App → AI App → MCP Server → AI Model → Tools → Protocols → Agents**

<!-- section_id: "23930ca0-eb1e-4351-a5e6-359e065f112e" -->
## How to Use It

<!-- section_id: "c6137dae-b71d-4f12-bd99-2fd298266486" -->
### Start with Your OS

Navigate to: `0.05_operating_systems/<your_os>/`

- `linux_ubuntu/` - For Ubuntu/Linux systems
- `macos/` - For macOS systems
- `windows/` - For Windows systems
- `wsl/` - For Windows Subsystem for Linux
- `_shared/` - For cross-platform setup

<!-- section_id: "8350187b-2661-4883-878e-1b60bd57b4c1" -->
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

<!-- section_id: "2fbfffc8-451f-4e40-8dbb-8e8dd8ef2899" -->
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

<!-- section_id: "578b5aea-29f6-4e77-8ec7-fe6a25758bca" -->
### Find Setup Documentation

Navigate to the deepest level `general_setup_and_config/` folder for actual setup instructions, configuration examples, and troubleshooting.

<!-- section_id: "10400016-3825-4f22-9ec4-19a90be9cee8" -->
## Quick Examples

<!-- section_id: "c70170eb-daa3-4cd9-85a3-ee034b87a950" -->
### Example 1: Git Setup (All Platforms)
```
0.05_operating_systems/_shared/
→ 0.06_environments/_shared/
→ 0.07_coding_apps/_shared/
→ 0.09_ai_apps/_shared/
→ 0.12_universal_tools/git/
→ general_setup_and_config/README.md
```

<!-- section_id: "675cd59e-2292-4961-a4af-94883d3a2e6f" -->
### Example 2: Linux + Cursor + Playwright MCP
```
0.05_operating_systems/linux_ubuntu/
→ 0.06_environments/development/
→ 0.07_coding_apps/cursor/
→ 0.09_ai_apps/cursor_agent/
→ 0.10_mcp_servers_and_apis_and_secrets/playwright-mcp/
→ general_setup_and_config/README.md
```

<!-- section_id: "471e07cc-ce40-452a-b7f1-7f744329881e" -->
### Example 3: Core MCP Issues (Any Setup)
```
0.05_operating_systems/_shared/
→ 0.06_environments/_shared/
→ 0.07_coding_apps/_shared/
→ 0.09_ai_apps/_shared/
→ 0.10_mcp_servers_and_apis_and_secrets/_mcp_core/
→ general_setup_and_config/README.md
```

<!-- section_id: "4b8eaca4-bf23-4942-9f55-3c93c8e44c56" -->
## Key Files

- **README.md** - Main documentation and navigation guide
- **STRUCTURE_VISUALIZATION.md** - Complete visual hierarchy
- **QUICK_START.md** - This file (how to get started)

<!-- section_id: "4ccb6faa-7a8e-4443-a14d-4cb66848b5c0" -->
## Statistics

- Total directories: 99+
- Levels of hierarchy: 10 (OS through Agent Setup)
- _shared folders at each level: Yes
- README files: 10+

<!-- section_id: "8fd6843b-37b4-41c3-bf97-04d7aafa0ee1" -->
## Next Steps

1. Read `README.md` for complete documentation
2. Navigate to your specific setup path
3. Follow the setup instructions in `general_setup_and_config/`
4. Consult `STRUCTURE_VISUALIZATION.md` to understand the full hierarchy

<!-- section_id: "c3f76f81-4ca2-4dfb-bba7-0544eb40e700" -->
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
