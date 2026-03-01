# Setup-Dependent (02) Overview

## What Is Setup-Dependent?

Setup-Dependent context covers all aspects of the specific environment and configuration where the system runs. It's organized hierarchically from foundational (OS) to specific (plugins and tools).

## Why It's Needed

The core system contains **universal** context. But every system runs in a **specific environment**:
- Different operating systems (Linux, macOS, Windows)
- Different shells and configurations
- Different coding apps and IDEs
- Different AI services and APIs
- Different local tools and MCP servers
- Different plugins and extensions

Setup-Dependent context adapts the universal core system for these specific circumstances.

## Hierarchical Organization

Setup-Dependent is organized from broadest to most specific:

### 01_os/
Operating system specifics (Linux, macOS, Windows)
- File paths and separators
- Shell differences
- System-level configuration
- OS-specific tools and behaviors

### 02_environment/
Shell and environment configuration
- PATH variables
- Environment variables
- Shell configuration files (.bashrc, .zshrc, etc.)
- Shell-specific behaviors and aliases

### 03_coding_apps/
IDE and coding editor configuration
- Claude Code
- Cursor
- Gemini IDE (Google)
- VS Code and extensions
- Other code editors
- Editor-specific keybindings, themes, extensions

### 04_ai_apps/
AI service and application configuration
- Claude (Claude.ai, Claude API)
- Perplexity
- ChatGPT
- Other AI services
- API keys, authentication, preferences

### 05_mcp_servers/
Model Context Protocol server configuration
- Which servers are enabled
- Server-specific configuration
- Tool availability per server
- Authentication and API keys

### 06_tools_and_apis/
External tools, utilities, and API integrations
- Development tools (git, npm, etc.)
- External APIs (GitHub, Slack, etc.)
- Utilities and command-line tools
- API keys and authentication

### 07_plugins/
IDE plugins, extensions, and add-ons
- VS Code extensions
- Cursor extensions
- IDE-specific plugins
- Third-party integrations

### 08_other_setup_specifics/
Additional setup-specific context
- Hardware specifications (if relevant)
- Custom configurations
- Local overrides
- Environment-specific rules and behaviors

## How It Relates to Core System

**Core System** defines WHAT should happen universally.
**Setup-Dependent** defines HOW it happens in this specific environment.

Example:
- **Core**: "Use git for version control" (core protocol)
- **Setup-Dependent**: "Git is installed at /usr/bin/git on Linux" (os-specific)

## Integration

Setup-Dependent context feeds into the Context Avenue Web, which then uses both core system and setup-dependent information to create avenue-specific versions.

The .1merge system then uses both to create AI app-specific final versions.
