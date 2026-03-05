---
resource_id: "9b0b3a0b-ef92-4997-ba54-40fa57ff96f2"
resource_type: "document"
resource_name: "QUICK_START.sync-conflict-20260126-102106-IF2WOGZ"
---
# Quick Start Guide - Universal Setup File Tree

<!-- section_id: "cdc78ca8-ac85-4759-94a2-870a7fed2b49" -->
## What is This?

This is a **hierarchical navigable file tree** for all setup documentation. It allows you to drill down from general to specific setup configurations:

**OS → Environment → Coding App → AI App → MCP Server → AI Model → Tools → Protocols → Agents**

<!-- section_id: "2abfbdf0-5a6a-462e-acce-3fe7cf1e375f" -->
## How to Use It

<!-- section_id: "ead25b56-2fc9-42b2-a111-b67b9376aebe" -->
### Start with Your OS

Navigate to: `0.05_operating_systems/<your_os>/`

- `linux_ubuntu/` - For Ubuntu/Linux systems
- `macos/` - For macOS systems
- `windows/` - For Windows systems
- `wsl/` - For Windows Subsystem for Linux
- `_shared/` - For cross-platform setup

<!-- section_id: "fbe40db7-b92a-4111-b50a-092fd4615b01" -->
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

<!-- section_id: "9c3cac01-c730-42af-8a57-955e69c45105" -->
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

<!-- section_id: "480ec80c-6ff2-4cb3-b225-c8cfe86ee0bf" -->
### Find Setup Documentation

Navigate to the deepest level `general_setup_and_config/` folder for actual setup instructions, configuration examples, and troubleshooting.

<!-- section_id: "6ec7fa30-9d4e-4f18-a253-efcd17de1aad" -->
## Quick Examples

<!-- section_id: "7ed9981d-17fe-44c7-bc12-8dc61b9c3551" -->
### Example 1: Git Setup (All Platforms)
```
0.05_operating_systems/_shared/
→ 0.06_environments/_shared/
→ 0.07_coding_apps/_shared/
→ 0.09_ai_apps/_shared/
→ 0.12_universal_tools/git/
→ general_setup_and_config/README.md
```

<!-- section_id: "948bfcca-38ca-4830-8e5c-7443fa2188fb" -->
### Example 2: Linux + Cursor + Playwright MCP
```
0.05_operating_systems/linux_ubuntu/
→ 0.06_environments/development/
→ 0.07_coding_apps/cursor/
→ 0.09_ai_apps/cursor_agent/
→ 0.10_mcp_servers_and_apis_and_secrets/playwright-mcp/
→ general_setup_and_config/README.md
```

<!-- section_id: "4c607adb-fcef-4eb0-8e86-a391833d1b5e" -->
### Example 3: Core MCP Issues (Any Setup)
```
0.05_operating_systems/_shared/
→ 0.06_environments/_shared/
→ 0.07_coding_apps/_shared/
→ 0.09_ai_apps/_shared/
→ 0.10_mcp_servers_and_apis_and_secrets/_mcp_core/
→ general_setup_and_config/README.md
```

<!-- section_id: "49b73291-a5e5-4b48-9510-0ff587cbdf18" -->
## Key Files

- **README.md** - Main documentation and navigation guide
- **STRUCTURE_VISUALIZATION.md** - Complete visual hierarchy
- **QUICK_START.md** - This file (how to get started)

<!-- section_id: "2bb29d7e-cf58-4ae3-a764-aafd2912c5a9" -->
## Statistics

- Total directories: 99+
- Levels of hierarchy: 10 (OS through Agent Setup)
- _shared folders at each level: Yes
- README files: 10+

<!-- section_id: "1810856d-0b35-449b-a6e3-9c42f6f65832" -->
## Next Steps

1. Read `README.md` for complete documentation
2. Navigate to your specific setup path
3. Follow the setup instructions in `general_setup_and_config/`
4. Consult `STRUCTURE_VISUALIZATION.md` to understand the full hierarchy

<!-- section_id: "d9cfc1b1-82e3-4eb6-8013-7c5e52577db2" -->
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
