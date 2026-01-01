# 0.01 Universal Setup File Tree (Traversable Hierarchy)

This folder is the **traversable universal setup documentation file tree**. It is organized so you can always navigate through the complete setup hierarchy:

`Operating System → Environment → Coding App → AI App → MCP Server → AI Model → Universal Tools → Protocols → Agent Setup`

## Canonical Tree

```text
0.01_universal_setup_file_tree_0/
└── 0.02_operating_systems/
    ├── _shared/                                    # Cross-OS defaults and documentation
    │   └── 0.03_environments/
    │       ├── _shared/                            # Cross-environment defaults
    │       │   └── 0.04_coding_apps/
    │       │       ├── _shared/                    # Cross-coding-app defaults
    │       │       │   └── 0.05_ai_apps/
    │       │       │       ├── _shared/            # Cross-AI-app defaults
    │       │       │       │   └── 0.06_mcp_servers/
    │       │       │       │       ├── _shared/    # Cross-MCP-server defaults
    │       │       │       │       │   └── 0.07_ai_models/
    │       │       │       │       │       ├── _shared/           # Cross-model defaults
    │       │       │       │       │       │   └── 0.08_universal_tools/
    │       │       │       │       │       │       ├── _shared/   # Cross-tool defaults
    │       │       │       │       │       │       │   └── 0.09_protocols/
    │       │       │       │       │       │       │       ├── _shared/          # Cross-protocol defaults
    │       │       │       │       │       │       │       │   └── 0.10_agent_setup/
    │       │       │       │       │       │       │       │       └── general_setup_and_config/
    │       │       │       │       │       │       │       └── <protocol>/
    │       │       │       │       │       │       │           └── general_setup_and_config/
    │       │       │       │       │       │       └── <tool>/
    │       │       │       │       │       │           └── general_setup_and_config/
    │       │       │       │       │       └── <ai_model>/
    │       │       │       │       │           └── general_setup_and_config/
    │       │       │       │       ├── _mcp_core/              # Cross-server MCP issues
    │       │       │       │       │   └── general_setup_and_config/
    │       │       │       │       └── <mcp_server>/
    │       │       │       │           └── general_setup_and_config/
    │       │       │       └── <ai_app>/                       # Specific AI app setup
    │       │       │           └── 0.06_mcp_servers/
    │       │       │               └── (same structure)
    │       │       └── <coding_app>/                           # Specific coding app setup
    │       │           └── 0.05_ai_apps/
    │       │               └── (same structure)
    │       └── <environment>/                                  # Specific environment setup
    │           └── 0.04_coding_apps/
    │               └── (same structure)
    └── <os>/                                                   # OS-specific overrides and notes
        └── 0.03_environments/
            └── (same structure)
```

## How To Use This Tree

### Quick Navigation

1. **Start at your OS**: `0.02_operating_systems/<os>/README.md`
   - Linux/Ubuntu: `0.02_operating_systems/linux_ubuntu/`
   - macOS: `0.02_operating_systems/macos/`
   - Windows: `0.02_operating_systems/windows/`
   - WSL: `0.02_operating_systems/wsl/`

2. **Navigate to environment**: `0.03_environments/<environment>/README.md`
   - Development: `0.03_environments/development/`
   - Production: `0.03_environments/production/`
   - Testing: `0.03_environments/testing/`

3. **Navigate to coding app**: `0.04_coding_apps/<coding_app>/README.md`
   - VS Code: `0.04_coding_apps/vscode/`
   - Cursor: `0.04_coding_apps/cursor/`
   - Vim: `0.04_coding_apps/vim/`
   - Emacs: `0.04_coding_apps/emacs/`

4. **Navigate to AI app**: `0.05_ai_apps/<ai_app>/README.md`
   - Claude Code CLI: `0.05_ai_apps/claude_code_cli/`
   - Cursor Agent: `0.05_ai_apps/cursor_agent/`
   - Codex CLI: `0.05_ai_apps/codex_cli/`

5. **Navigate to MCP server**: `0.06_mcp_servers/<mcp_server>/general_setup_and_config/`
   - Browser MCP: `0.06_mcp_servers/browser-mcp/`
   - Playwright MCP: `0.06_mcp_servers/playwright-mcp/`
   - Core issues: `0.06_mcp_servers/_mcp_core/`

6. **Navigate to AI model**: `0.07_ai_models/<ai_model>/general_setup_and_config/`
   - Claude Sonnet: `0.07_ai_models/claude-sonnet/`
   - Claude Opus: `0.07_ai_models/claude-opus/`
   - GPT-4: `0.07_ai_models/gpt-4/`

7. **Navigate to universal tools**: `0.08_universal_tools/<tool>/general_setup_and_config/`
   - Git: `0.08_universal_tools/git/`
   - Docker: `0.08_universal_tools/docker/`
   - NPM: `0.08_universal_tools/npm/`

8. **Navigate to protocols**: `0.09_protocols/<protocol>/general_setup_and_config/`
   - Terminal Protocol: `0.09_protocols/terminal_protocol/`
   - Browser Protocol: `0.09_protocols/browser_protocol/`
   - Git Protocol: `0.09_protocols/git_protocol/`

9. **Navigate to agent setup**: `0.10_agent_setup/general_setup_and_config/`
   - Manager agents
   - Stage agents
   - Testing agents

### Using _shared Folders

Use `_shared/` folders when guidance applies across multiple options at that level:

- `0.02_operating_systems/_shared/` - Setup that works on all OSes
- `0.03_environments/_shared/` - Setup that works in all environments
- `0.04_coding_apps/_shared/` - Setup that works with all coding apps
- `0.05_ai_apps/_shared/` - Setup that works with all AI apps
- `0.06_mcp_servers/_shared/` - Setup that works with all MCP servers
- `0.07_ai_models/_shared/` - Setup that works with all AI models
- `0.08_universal_tools/_shared/` - Setup that works with all tools
- `0.09_protocols/_shared/` - Setup that works with all protocols

### Finding Setup Documentation

**Scenario 1**: Setting up Claude Code CLI on Linux Ubuntu with Playwright MCP
```
Path: 0.02_operating_systems/linux_ubuntu/
      → 0.03_environments/development/
      → 0.04_coding_apps/_shared/
      → 0.05_ai_apps/claude_code_cli/
      → 0.06_mcp_servers/playwright-mcp/
      → general_setup_and_config/
```

**Scenario 2**: Setting up universal Git tool for all environments
```
Path: 0.02_operating_systems/_shared/
      → 0.03_environments/_shared/
      → 0.04_coding_apps/_shared/
      → 0.05_ai_apps/_shared/
      → 0.06_mcp_servers/_shared/
      → 0.07_ai_models/_shared/
      → 0.08_universal_tools/git/
      → general_setup_and_config/
```

**Scenario 3**: Setting up Cursor Agent with Browser MCP on macOS
```
Path: 0.02_operating_systems/macos/
      → 0.03_environments/development/
      → 0.04_coding_apps/cursor/
      → 0.05_ai_apps/cursor_agent/
      → 0.06_mcp_servers/browser-mcp/
      → general_setup_and_config/
```

## Documentation Placement Guidelines

### Where to place OS-specific setup docs:
- `0.02_operating_systems/<os>/README.md` - OS installation, system requirements

### Where to place environment-specific setup docs:
- `0.03_environments/<environment>/README.md` - Environment variables, configuration

### Where to place coding app setup docs:
- `0.04_coding_apps/<coding_app>/README.md` - IDE installation, extensions, settings

### Where to place AI app setup docs:
- `0.05_ai_apps/<ai_app>/README.md` - AI tool installation, authentication, configuration

### Where to place MCP server setup docs:
- `0.06_mcp_servers/<mcp_server>/general_setup_and_config/` - MCP server installation, configuration, issues

### Where to place AI model setup docs:
- `0.07_ai_models/<ai_model>/general_setup_and_config/` - Model access, API keys, rate limits

### Where to place universal tool setup docs:
- `0.08_universal_tools/<tool>/general_setup_and_config/` - Tool installation, usage, issues

### Where to place protocol setup docs:
- `0.09_protocols/<protocol>/general_setup_and_config/` - Protocol rules, conventions, best practices

### Where to place agent setup docs:
- `0.10_agent_setup/general_setup_and_config/` - Agent configuration, registration, deployment

## Relationship to Other Sublayers

This file tree serves as a **navigational index** that points to detailed documentation in the individual setup sublayers:

- **sub_layer_0.05_os_setup** - Detailed OS setup documentation
- **sub_layer_0.06_environment_setup** - Detailed environment setup documentation
- **sub_layer_0.07_coding_app_setup** - Detailed coding app setup documentation
- **sub_layer_0.08_apps_browsers_extensions_setup** - Detailed browser/extension setup documentation
- **sub_layer_0.09_ai_apps_tools_setup** - Detailed AI app setup documentation
- **sub_layer_0.10_mcp_servers_and_tools_setup** - Detailed MCP server setup documentation
- **sub_layer_0.11_ai_models** - Detailed AI model access documentation
- **sub_layer_0.12_universal_tools** - Detailed universal tool documentation
- **sub_layer_0.13_universal_protocols** - Detailed protocol documentation
- **sub_layer_0.14_agent_setup** - Detailed agent setup documentation

## Notes

- Use symlinks or references to avoid duplicating content from the detailed sublayers
- Each `general_setup_and_config/` folder should contain:
  - Setup instructions specific to that combination of choices
  - Known issues and fixes for that combination
  - Configuration examples
  - Links to detailed documentation in the respective sublayers
- The `_mcp_core/` pseudo-server stores issues that apply across multiple MCP servers
- Always start navigation from the most general level (OS) and work down to specifics
