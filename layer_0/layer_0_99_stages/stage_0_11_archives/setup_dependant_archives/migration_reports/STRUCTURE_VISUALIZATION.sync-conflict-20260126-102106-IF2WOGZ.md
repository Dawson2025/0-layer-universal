---
resource_id: "e323f317-4a0e-4cc6-a330-bf1dc3d8694e"
resource_type: "document"
resource_name: "STRUCTURE_VISUALIZATION.sync-conflict-20260126-102106-IF2WOGZ"
---
# Universal Setup File Tree Structure Visualization

<!-- section_id: "20d4a359-eb55-4af7-9869-cb3089e34ec0" -->
## Complete Hierarchy

```
0.01_universal_setup_file_tree_0/
│
├── README.md                           # Main navigation guide
├── STRUCTURE_VISUALIZATION.md          # This file
│
└── 0.05_operating_systems/
    ├── README.md
    │
    ├── _shared/                        # Cross-OS setup (works on all platforms)
    │   ├── README.md
    │   └── 0.06_environments/
    │       ├── README.md
    │       ├── _shared/                # Cross-environment setup
    │       ├── development/
    │       ├── production/
    │       └── testing/
    │           └── 0.07_coding_apps/
    │               ├── README.md
    │               ├── _shared/        # Cross-coding-app setup
    │               ├── vscode/
    │               ├── cursor/
    │               ├── vim/
    │               └── emacs/
    │                   └── 0.09_ai_apps/
    │                       ├── README.md
    │                       ├── _shared/           # Cross-AI-app setup
    │                       ├── claude_code_cli/
    │                       ├── cursor_agent/
    │                       ├── codex_cli/
    │                       └── gemini_cli/
    │                           ├── 0.10_mcp_servers_and_apis_and_secrets/
    │                           │   └── (MCP servers and configs)
    │                           ├── 0.11_ai_models/
    │                           │   └── (AI model access)
    │                           ├── 0.12_universal_tools/
    │                           │   └── (Tools, shared + per-tool)
    │                           ├── 0.13_protocols/
    │                           │   └── (Protocols)
    │                           └── 0.14_agent_setup/
    │                               └── (Agent setup)
    │
    ├── linux_ubuntu/                   # Linux Ubuntu-specific setup
    │   ├── README.md
    │   └── 0.06_environments/
    │       └── (mirrors _shared structure with Ubuntu-specific content)
    │
    ├── macos/                          # macOS-specific setup
    │   ├── README.md
    │   └── 0.06_environments/
    │       └── (mirrors _shared structure with macOS-specific content)
    │
    ├── windows/                        # Windows-specific setup
    │   ├── README.md
    │   └── 0.06_environments/
    │       └── (mirrors _shared structure with Windows-specific content)
    │
    └── wsl/                           # WSL-specific setup
        ├── README.md
        └── 0.06_environments/
            └── (mirrors _shared structure with WSL-specific content)
```

<!-- section_id: "48565a55-bd0f-4284-a399-e95f3a719bc7" -->
## Navigation Examples

<!-- section_id: "c5d4582e-7827-48f2-a6bc-c8a95395ed3c" -->
### Example 1: Universal Git Setup (All Platforms, All Environments)

**Path**:
```
0.05_operating_systems/_shared/
→ 0.06_environments/_shared/
→ 0.07_coding_apps/_shared/
→ 0.09_ai_apps/_shared/
→ 0.12_universal_tools/git/
→ general_setup_and_config/
```

**Use case**: Setup instructions that work for Git on any OS, any environment, any coding app

<!-- section_id: "a341a853-60f3-47ea-acc3-c733638ee479" -->
### Example 2: Linux + Cursor + Cursor Agent + Playwright MCP

**Path**:
```
0.05_operating_systems/linux_ubuntu/
→ 0.06_environments/development/
→ 0.07_coding_apps/cursor/
→ 0.09_ai_apps/cursor_agent/
→ 0.10_mcp_servers_and_apis_and_secrets/playwright-mcp/
→ general_setup_and_config/
```

**Use case**: Specific setup for Playwright MCP on Linux with Cursor IDE and Cursor Agent

<!-- section_id: "865ac5c9-7715-4ddd-b06f-bad80bc38085" -->
### Example 3: macOS + VS Code + Claude Code CLI + Browser MCP

**Path**:
```
0.05_operating_systems/macos/
→ 0.06_environments/development/
→ 0.07_coding_apps/vscode/
→ 0.09_ai_apps/claude_code_cli/
→ 0.10_mcp_servers_and_apis_and_secrets/browser-mcp/
→ general_setup_and_config/
```

**Use case**: Specific setup for Browser MCP on macOS with VS Code and Claude Code CLI

<!-- section_id: "97bbaa68-2f43-47c3-a53c-892c970bf9bc" -->
### Example 4: Core MCP Issues (Any Configuration)

**Path**:
```
0.05_operating_systems/_shared/
→ 0.06_environments/_shared/
→ 0.07_coding_apps/_shared/
→ 0.09_ai_apps/_shared/
→ 0.10_mcp_servers_and_apis_and_secrets/_mcp_core/
→ general_setup_and_config/
```

**Use case**: MCP server issues that affect multiple servers (tool exposure, env vars, etc.)

<!-- section_id: "f1628003-165b-4dec-bb63-e6acee1dd35d" -->
## Key Design Principles

<!-- section_id: "4289f1f0-ad04-43b8-b555-b3dd6a4ccd9f" -->
### 1. Hierarchical Navigation
- Start at the most general level (OS)
- Navigate down through increasingly specific choices
- Each level represents a configuration dimension

<!-- section_id: "06a9848c-2371-4316-aa97-322a55a22ec8" -->
### 2. Shared Folders at Every Level
- `_shared/` folders contain documentation that applies to all options at that level
- Example: `0.06_environments/_shared/` = works in dev, prod, and testing environments
- Allows for maximum reuse while supporting specific overrides

<!-- section_id: "7af7cbe4-2709-4d95-b70d-465d596d5db6" -->
### 3. Symmetric Structure
- Each OS can have the complete hierarchy underneath it
- Maintains consistent navigation regardless of starting point
- Easy to add new options at any level

<!-- section_id: "3c846f45-3e5c-4930-843a-abaef970ea85" -->
### 4. Terminal Nodes
- `general_setup_and_config/` folders are the "leaves" of the tree
- Contain actual setup instructions, configuration examples, and issue documentation
- Each path combination has its own setup documentation

<!-- section_id: "2f3b0efc-5cc8-43cf-8365-298be8adcc90" -->
### 5. Cross-References
- README files at each level link to related sublayers
- Avoids duplication by referencing detailed docs in:
  - sub_layer_0_05_os_setup
  - sub_layer_0_06_environment_setup
  - sub_layer_0_07_coding_app_setup
  - sub_layer_0_08_apps_browsers_extensions_setup
  - sub_layer_0_09_ai_apps_tools_setup
  - sub_layer_0_10_mcp_servers_and_tools_setup
  - sub_layer_0_11_ai_models
  - sub_layer_0_12_universal_tools
  - sub_layer_0_13_universal_protocols
  - sub_layer_0_14_agent_setup

<!-- section_id: "541d39cd-b977-49f7-a74f-4a38776ff9d2" -->
## Adding New Options

<!-- section_id: "c192085c-e4b2-4d08-bd6d-60a0dc71785b" -->
### To add a new OS:
```bash
mkdir -p 0.05_operating_systems/<new_os>/0.06_environments/
# Copy structure from _shared/0.06_environments/
# Customize for the new OS
```

<!-- section_id: "770b9941-b74c-4c66-80b2-7df345398e92" -->
### To add a new coding app:
```bash
mkdir -p 0.05_operating_systems/_shared/0.06_environments/_shared/0.07_coding_apps/<new_app>/0.09_ai_apps/
# Copy structure from _shared/0.09_ai_apps/
# Customize for the new coding app
```

<!-- section_id: "9d43e57f-e19d-473c-b4b0-e17bc0e5dcde" -->
### To add a new MCP server:
```bash
mkdir -p 0.05_operating_systems/_shared/0.06_environments/_shared/0.07_coding_apps/_shared/0.09_ai_apps/_shared/0.10_mcp_servers_and_apis_and_secrets/<new_server>/general_setup_and_config/
# Add setup documentation for the new server
```

<!-- section_id: "3066e27a-11ef-4b23-8499-9bad614c9c2c" -->
## Relationship to Other Sublayers

This file tree acts as a **navigational index and quick reference** that complements the detailed documentation in individual sublayers:

- **This tree**: Navigation + specific combination setups
- **Individual sublayers**: Detailed setup guides, troubleshooting, best practices

Both systems work together to provide comprehensive setup documentation.
