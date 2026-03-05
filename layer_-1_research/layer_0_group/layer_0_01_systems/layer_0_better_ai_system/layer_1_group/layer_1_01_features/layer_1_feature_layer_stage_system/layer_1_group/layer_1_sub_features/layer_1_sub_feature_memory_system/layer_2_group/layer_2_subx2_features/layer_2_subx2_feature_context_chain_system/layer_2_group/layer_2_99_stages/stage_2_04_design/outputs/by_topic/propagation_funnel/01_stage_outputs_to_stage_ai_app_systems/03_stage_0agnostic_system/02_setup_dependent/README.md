---
resource_id: "18e815e4-cc98-4211-9822-081367908e2a"
resource_type: "readme
output"
resource_name: "README"
---
# Setup-Dependent (02-08)

## What This Contains

The setup-dependent layer adds **environment and configuration-specific context** to the core system. While the core system (01-05) contains universal knowledge, rules, protocols, and memory that applies everywhere, the setup-dependent layer captures what's specific to YOUR setup:

- **Operating System**: Linux, macOS, Windows (OS-specific commands, file paths, utilities)
- **Environment**: Shell configuration, PATH, environment variables, system settings
- **Coding Apps**: IDEs and editors (Cursor, Antigravity, NeoVim, VS Code)
- **AI Apps**: CLI tools for accessing AI services (Claude Code CLI, Codex CLI, Gemini CLI, Cursor Agent CLI)
- **Plugins**: Extensions for both coding apps and AI apps (VS Code extensions, Cursor extensions, Claude plugins)
- **MCP Servers**: Model Context Protocol server configurations and connections
- **Tools & APIs**: External tools, utilities, and API integrations
- **Other Setup Specifics**: Additional environment-dependent context

## Propagation Hierarchy

These setup-dependent resources layer on top of core system knowledge:

```
Core System (01-05)
        ↓
Setup-Dependent (02-08) — Environment-specific adaptations
        ↓
Context Avenue Web (09-13) — Avenue-specific formatting
        ↓
.1merge System — AI app-specific final versions
```

## Subdirectories

Each numbered subdirectory represents a layer in the setup hierarchy:

- **01_os/** → Operating system specifics
- **02_environment/** → Shell, PATH, environment variables, system settings
- **03_coding_apps/** → IDE and code editor configurations
- **04_ai_apps/** → AI service CLI tools and configurations
- **05_plugins/** → Extensions for coding apps and AI apps
- **06_mcp_servers/** → Model Context Protocol server setups
- **07_tools_and_apis/** → External tools, utilities, API keys, integrations
- **08_other_setup_specifics/** → Additional environment-dependent content

## Next Step

After understanding setup-dependent organization, see `00_setup_dependent_overview/README.md` for detailed explanation of the hierarchy.
