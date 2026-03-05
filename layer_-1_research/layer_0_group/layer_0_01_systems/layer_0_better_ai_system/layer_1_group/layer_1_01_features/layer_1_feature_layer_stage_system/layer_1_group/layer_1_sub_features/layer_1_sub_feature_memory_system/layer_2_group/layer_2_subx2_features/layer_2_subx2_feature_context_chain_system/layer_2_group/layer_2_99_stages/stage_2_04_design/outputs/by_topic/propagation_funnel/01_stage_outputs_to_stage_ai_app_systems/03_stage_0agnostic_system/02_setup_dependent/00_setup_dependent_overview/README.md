---
resource_id: "cab93bec-27a7-4079-a968-940dc8fb3ffc"
resource_type: "readme
output"
resource_name: "README"
---
# Setup-Dependent Hierarchy Overview

<!-- section_id: "a64c648f-4ecb-4e0c-809c-4153cae4edff" -->
## Overview

Setup-dependent context captures what's specific to YOUR environment and configuration, layered on top of the core system (01-05). This hierarchical structure moves from foundational (operating system) to specific (individual tools and plugins).

<!-- section_id: "b220a573-cf20-414d-a5b8-5a3265af242c" -->
## Hierarchy Ordering

The numbering follows a progression from foundational to specific:

```
01_os/                    ← Foundation: Operating system (Linux, macOS, Windows)
  ↓
02_environment/           ← Shell configuration, PATH, env vars, system settings
  ↓
03_coding_apps/           ← IDEs and code editors (Cursor, Antigravity, NeoVim, VS Code)
  ↓
04_ai_apps/               ← AI service CLI tools (Claude Code, Codex, Gemini, Cursor Agent)
  ↓
05_plugins/               ← Extensions for both coding apps AND AI apps
  ↓
06_mcp_servers/           ← Model Context Protocol server configs and connections
  ↓
07_tools_and_apis/        ← External tools, utilities, API integrations
  ↓
08_other_setup_specifics/ ← Additional environment-dependent context
```

<!-- section_id: "8676e968-0586-4515-b75a-fd09515f4b27" -->
## What Each Layer Contains

<!-- section_id: "434db78e-e5f0-44e3-9eb2-44b20f26d1f1" -->
### 01_os/
Operating system specifics:
- Linux, macOS, Windows path conventions
- OS-specific command syntax
- System utilities and built-in tools
- Desktop environment settings (GNOME, KDE, etc.)
- Package managers and installation procedures

<!-- section_id: "45dc828f-cf47-44b8-879f-d3caf68cbef3" -->
### 02_environment/
Shell and system environment:
- Shell type and version (.bashrc, .zshrc, .config/fish, etc.)
- PATH configuration
- Environment variables (HOME, USER, SHELL, etc.)
- System PATH additions and precedence
- Shell aliases and functions
- Terminal emulator settings

<!-- section_id: "4809accc-ca4d-4607-ac58-028d3ea9194b" -->
### 03_coding_apps/
IDE and code editor configurations:
- Cursor IDE settings and extensions
- Antigravity IDE configuration
- NeoVim keybindings and plugins
- VS Code settings and extensions
- Other code editor setups
- Editor-specific file associations

<!-- section_id: "83ff0049-29ca-4869-b5fc-af322ab5fd0d" -->
### 04_ai_apps/
AI service CLI tool configurations:
- Claude Code CLI setup and authentication
- Codex CLI configuration
- Gemini CLI setup
- Cursor Agent CLI configuration
- Other AI app CLI tools
- API key management and authentication

<!-- section_id: "4cc99176-25c3-4777-96d7-5359beead2ba" -->
### 05_plugins/
Extensions and plugins for both coding apps and AI apps:
- **Coding app plugins**: VS Code extensions, Cursor extensions, NeoVim plugins
- **AI app plugins**: Claude plugins, Perplexity plugins, custom integrations
- Plugin configuration and activation
- Plugin compatibility matrix

<!-- section_id: "78a8c50c-11dd-41f7-82b9-dca9e918e7b9" -->
### 06_mcp_servers/
Model Context Protocol server configurations:
- MCP server configurations (Canvas, Perplexity, Browser, etc.)
- Server authentication and connection details
- Server availability and health checks
- Custom MCP server integrations

<!-- section_id: "7cff5573-d9d7-46ec-b51b-d515cbdbc3af" -->
### 07_tools_and_apis/
External tools and API integrations:
- External CLI tools and utilities
- API keys and credential management
- Service integrations (GitHub, GitLab, etc.)
- Tool-specific configuration files
- Custom scripts and wrapper utilities

<!-- section_id: "42e89b5d-1f4f-428f-b5e2-639ebddcfcd6" -->
### 08_other_setup_specifics/
Additional environment-dependent context:
- Machine-specific quirks and workarounds
- Network and proxy configuration
- Custom aliases and convenience scripts
- Hardware-specific settings (display, keyboard, etc.)
- Anything else setup-dependent that doesn't fit elsewhere

<!-- section_id: "4af6ad84-9b4e-4ef0-bd4e-704b1e1d506f" -->
## Next Step

After understanding the hierarchy, read individual subdirectory READMEs for specific details about what each section contains.
