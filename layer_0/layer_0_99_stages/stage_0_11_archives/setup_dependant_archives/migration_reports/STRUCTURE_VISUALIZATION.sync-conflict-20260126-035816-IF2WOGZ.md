---
resource_id: "fd89e011-d63b-49dd-8068-7b82a74bd61b"
resource_type: "document"
resource_name: "STRUCTURE_VISUALIZATION.sync-conflict-20260126-035816-IF2WOGZ"
---
# Universal Setup File Tree Structure Visualization

<!-- section_id: "48a332d9-48a5-4767-b338-06b75693dbd7" -->
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

<!-- section_id: "66703c92-3618-4eed-be2c-d823954aa7a3" -->
## Navigation Examples

<!-- section_id: "477b4794-3863-4a62-b111-0255aefedd3c" -->
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

<!-- section_id: "17a13f4b-0c4c-4f69-985c-1ec822bbaaa9" -->
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

<!-- section_id: "640feb94-3570-4445-82e4-7d12ac8e7820" -->
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

<!-- section_id: "ebac4704-5b6f-4a53-8b3a-99de3422c029" -->
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

<!-- section_id: "b9bebd65-6793-49bb-9ba1-34a5ad99f5f1" -->
## Key Design Principles

<!-- section_id: "65b2d39d-5801-4cd0-a25f-6311f8f38662" -->
### 1. Hierarchical Navigation
- Start at the most general level (OS)
- Navigate down through increasingly specific choices
- Each level represents a configuration dimension

<!-- section_id: "e8d4814b-7d82-47d7-ae2a-fd29af233faa" -->
### 2. Shared Folders at Every Level
- `_shared/` folders contain documentation that applies to all options at that level
- Example: `0.06_environments/_shared/` = works in dev, prod, and testing environments
- Allows for maximum reuse while supporting specific overrides

<!-- section_id: "a3aad17c-895c-4131-8962-f8374394b404" -->
### 3. Symmetric Structure
- Each OS can have the complete hierarchy underneath it
- Maintains consistent navigation regardless of starting point
- Easy to add new options at any level

<!-- section_id: "9cd5aae4-04ee-4b52-9643-12096548715a" -->
### 4. Terminal Nodes
- `general_setup_and_config/` folders are the "leaves" of the tree
- Contain actual setup instructions, configuration examples, and issue documentation
- Each path combination has its own setup documentation

<!-- section_id: "3ede16a9-b3fc-4d98-876a-2b2c2ad40957" -->
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

<!-- section_id: "fcea8190-e01a-489e-a9c0-3bbf640ff976" -->
## Adding New Options

<!-- section_id: "d209ddb2-cc40-42a5-91dc-28cb44cb0ef2" -->
### To add a new OS:
```bash
mkdir -p 0.05_operating_systems/<new_os>/0.06_environments/
# Copy structure from _shared/0.06_environments/
# Customize for the new OS
```

<!-- section_id: "c8ea008a-5978-4314-a5c2-acc328ef2c54" -->
### To add a new coding app:
```bash
mkdir -p 0.05_operating_systems/_shared/0.06_environments/_shared/0.07_coding_apps/<new_app>/0.09_ai_apps/
# Copy structure from _shared/0.09_ai_apps/
# Customize for the new coding app
```

<!-- section_id: "73b0576b-e649-486d-896b-a77c5b6e35f3" -->
### To add a new MCP server:
```bash
mkdir -p 0.05_operating_systems/_shared/0.06_environments/_shared/0.07_coding_apps/_shared/0.09_ai_apps/_shared/0.10_mcp_servers_and_apis_and_secrets/<new_server>/general_setup_and_config/
# Add setup documentation for the new server
```

<!-- section_id: "8fbe343b-adc2-415b-a343-a77229842e57" -->
## Relationship to Other Sublayers

This file tree acts as a **navigational index and quick reference** that complements the detailed documentation in individual sublayers:

- **This tree**: Navigation + specific combination setups
- **Individual sublayers**: Detailed setup guides, troubleshooting, best practices

Both systems work together to provide comprehensive setup documentation.
