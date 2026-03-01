# Setup-Dependent Hierarchy Overview

## Overview

Setup-dependent context captures what's specific to YOUR environment and configuration, layered on top of the core system (01-05). This hierarchical structure moves from foundational (operating system) to specific (individual tools and plugins).

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

## What Each Layer Contains

### 01_os/
Operating system specifics:
- Linux, macOS, Windows path conventions
- OS-specific command syntax
- System utilities and built-in tools
- Desktop environment settings (GNOME, KDE, etc.)
- Package managers and installation procedures

### 02_environment/
Shell and system environment:
- Shell type and version (.bashrc, .zshrc, .config/fish, etc.)
- PATH configuration
- Environment variables (HOME, USER, SHELL, etc.)
- System PATH additions and precedence
- Shell aliases and functions
- Terminal emulator settings

### 03_coding_apps/
IDE and code editor configurations:
- Cursor IDE settings and extensions
- Antigravity IDE configuration
- NeoVim keybindings and plugins
- VS Code settings and extensions
- Other code editor setups
- Editor-specific file associations

### 04_ai_apps/
AI service CLI tool configurations:
- Claude Code CLI setup and authentication
- Codex CLI configuration
- Gemini CLI setup
- Cursor Agent CLI configuration
- Other AI app CLI tools
- API key management and authentication

### 05_plugins/
Extensions and plugins for both coding apps and AI apps:
- **Coding app plugins**: VS Code extensions, Cursor extensions, NeoVim plugins
- **AI app plugins**: Claude plugins, Perplexity plugins, custom integrations
- Plugin configuration and activation
- Plugin compatibility matrix

### 06_mcp_servers/
Model Context Protocol server configurations:
- MCP server configurations (Canvas, Perplexity, Browser, etc.)
- Server authentication and connection details
- Server availability and health checks
- Custom MCP server integrations

### 07_tools_and_apis/
External tools and API integrations:
- External CLI tools and utilities
- API keys and credential management
- Service integrations (GitHub, GitLab, etc.)
- Tool-specific configuration files
- Custom scripts and wrapper utilities

### 08_other_setup_specifics/
Additional environment-dependent context:
- Machine-specific quirks and workarounds
- Network and proxy configuration
- Custom aliases and convenience scripts
- Hardware-specific settings (display, keyboard, etc.)
- Anything else setup-dependent that doesn't fit elsewhere

## Next Step

After understanding the hierarchy, read individual subdirectory READMEs for specific details about what each section contains.
