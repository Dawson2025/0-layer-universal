---
resource_id: "8aea5eb8-2943-4b7a-b1e6-f4c9d4117b02"
resource_type: "document"
resource_name: "STRUCTURE_VISUALIZATION"
---
# Universal Setup File Tree Structure Visualization

<!-- section_id: "37dc6f7e-6e96-4e39-b821-9631b9b4cef6" -->
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

<!-- section_id: "1414967a-1121-4286-94d7-567cf93a041d" -->
## Navigation Examples

<!-- section_id: "546c2878-c017-47bc-a7b3-b137b974c277" -->
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

<!-- section_id: "9d252be4-32d6-4565-aefe-6d4bdb35d72c" -->
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

<!-- section_id: "349426f7-cf0a-4a0f-902e-23514d2ebe68" -->
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

<!-- section_id: "4fb8af62-2e68-4572-88cc-512580e33733" -->
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

<!-- section_id: "395ce30a-6880-45b9-83c1-3916c1616836" -->
## Key Design Principles

<!-- section_id: "08960b4e-5dc4-4ed7-8f9c-edb8e3420828" -->
### 1. Hierarchical Navigation
- Start at the most general level (OS)
- Navigate down through increasingly specific choices
- Each level represents a configuration dimension

<!-- section_id: "b22c13ee-cbab-431a-8d56-d26b6e87e842" -->
### 2. Shared Folders at Every Level
- `_shared/` folders contain documentation that applies to all options at that level
- Example: `0.06_environments/_shared/` = works in dev, prod, and testing environments
- Allows for maximum reuse while supporting specific overrides

<!-- section_id: "56b681a7-ba83-4cfe-989c-11c33c917c83" -->
### 3. Symmetric Structure
- Each OS can have the complete hierarchy underneath it
- Maintains consistent navigation regardless of starting point
- Easy to add new options at any level

<!-- section_id: "f9d827ac-f65f-4c18-95fe-b8525264271f" -->
### 4. Terminal Nodes
- `general_setup_and_config/` folders are the "leaves" of the tree
- Contain actual setup instructions, configuration examples, and issue documentation
- Each path combination has its own setup documentation

<!-- section_id: "03b0524d-d19c-41ea-b11b-44dfe02dcc6f" -->
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

<!-- section_id: "cd5c460b-d14d-4ce3-a8f1-bd51214062d6" -->
## Adding New Options

<!-- section_id: "f15715f4-c009-48af-a0ba-45c7936a3bf5" -->
### To add a new OS:
```bash
mkdir -p 0.05_operating_systems/<new_os>/0.06_environments/
# Copy structure from _shared/0.06_environments/
# Customize for the new OS
```

<!-- section_id: "711936c1-9167-4246-aa70-5dfe77d59791" -->
### To add a new coding app:
```bash
mkdir -p 0.05_operating_systems/_shared/0.06_environments/_shared/0.07_coding_apps/<new_app>/0.09_ai_apps/
# Copy structure from _shared/0.09_ai_apps/
# Customize for the new coding app
```

<!-- section_id: "d39cd015-7018-4b28-bbf2-4b0d39cf8272" -->
### To add a new MCP server:
```bash
mkdir -p 0.05_operating_systems/_shared/0.06_environments/_shared/0.07_coding_apps/_shared/0.09_ai_apps/_shared/0.10_mcp_servers_and_apis_and_secrets/<new_server>/general_setup_and_config/
# Add setup documentation for the new server
```

<!-- section_id: "646082f8-741e-43b0-b458-fd0069805d07" -->
## Relationship to Other Sublayers

This file tree acts as a **navigational index and quick reference** that complements the detailed documentation in individual sublayers:

- **This tree**: Navigation + specific combination setups
- **Individual sublayers**: Detailed setup guides, troubleshooting, best practices

Both systems work together to provide comprehensive setup documentation.
