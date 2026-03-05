---
resource_id: "a7942ceb-f53d-4e58-acfd-7504c898f1b2"
resource_type: "readme
document"
resource_name: "README"
---
# MCP Servers, APIs & Secrets Management

This directory contains documentation for Model Context Protocol (MCP) servers, API integrations, and secrets management patterns.

---

<!-- section_id: "c7fc441f-b08b-4fca-8bf5-858a103e01fe" -->
## Documentation System Overview

<!-- section_id: "e3590a04-2efd-4b33-81b5-8e370c2e295a" -->
### Purpose

This system provides:
1. **MCP Server Documentation** - Setup, configuration, troubleshooting for each server
2. **API Key Management** - Secure handling of API keys without exposing them in the repo
3. **Secrets Template Pattern** - Share the repo safely while keeping secrets local
4. **Workflow Protocols** - Step-by-step guides for common tasks

<!-- section_id: "d4e3ba07-a6cb-4364-aed8-b5572f204b3f" -->
### Directory Structure

```
0.10_mcp_servers_and_apis_and_secrets/
├── README.md                     # This file - system overview
│
├── _mcp_core/                    # Core MCP configuration hub
│   ├── README.md                 # Overview, relationships between servers
│   ├── general_setup_and_config/ # Shared setup guides
│   ├── general_issues_and_fixes/ # Cross-server troubleshooting
│   └── setup/
│       └── TROUBLESHOOTING.md    # Common issues across all MCP servers
│
├── _shared/                      # Shared secrets & API configuration
│   ├── README.md                 # Secrets management guide
│   ├── API_KEYS_SETUP.md         # How to obtain & configure API keys
│   ├── config.template.json      # Template with ${VAR} placeholders (COMMITTED)
│   ├── config.local.json         # Actual keys (GITIGNORED - never commit!)
│   └── .gitignore                # Ignores *.local.json, .secrets/, .env
│
├── <mcp-server>/                 # Individual MCP server (e.g., playwright-mcp)
│   ├── README.md                 # Setup, configuration, capabilities
│   ├── TROUBLESHOOTING.md        # Server-specific issues & solutions
│   └── workflows/                # Usage protocols
│       └── <task>.md             # Step-by-step for specific tasks
```

---

<!-- section_id: "82784fff-855a-46ae-a50b-c5eac0c97584" -->
## Secrets Template Pattern

<!-- section_id: "c8902d48-4e1b-4cc3-82ed-369154cd894c" -->
### Why This Pattern?

Allows sharing the repository without exposing API keys, passwords, or other secrets.

<!-- section_id: "8bb94e83-2add-4200-bd19-b77ec109204a" -->
### How It Works

| File | Committed to Git? | Contains |
|------|-------------------|----------|
| `config.template.json` | ✅ **Yes** | Placeholders like `${TAVILY_API_KEY}` |
| `config.local.json` | ❌ **No** | Actual API keys (gitignored) |
| `.env` files | ❌ **No** | Environment variables (gitignored) |

<!-- section_id: "8a1424ab-e65f-453d-9cb5-600062c8ca23" -->
### Setup Flow for New Users

1. Navigate to `_shared/`
2. Copy `config.template.json` → `config.local.json`
3. Replace `${VAR}` placeholders with real API keys
4. Alternatively, set environment variables that the template references

<!-- section_id: "f4d14ae0-1546-4272-b022-30afd9b04caf" -->
### Example Template

```json
{
  "tavily": {
    "api_key": "${TAVILY_API_KEY}"
  },
  "context7": {
    "api_key": "${CONTEXT7_API_KEY}",
    "api_url": "${CONTEXT7_API_URL}"
  }
}
```

<!-- section_id: "118e20aa-4119-4e93-a012-2610b03005b4" -->
### Getting API Keys

See `_shared/API_KEYS_SETUP.md` for instructions on obtaining keys for each service.

---

<!-- section_id: "a2caa4a8-830c-41e7-b9ac-59f435580ff4" -->
## Documentation Standard Per MCP Server

Each MCP server directory should contain:

| File | Required? | Purpose |
|------|-----------|---------|
| `README.md` | ✅ Yes | Installation, configuration, capabilities, usage examples |
| `TROUBLESHOOTING.md` | ✅ Yes | Common errors, solutions, diagnostic commands |
| `workflows/` | Recommended | Step-by-step protocols for specific tasks |

<!-- section_id: "2060203d-de3f-41d4-acb6-cc238ea584ec" -->
### README.md Template

```markdown
# <Server Name>

## Overview
Brief description of what this MCP server does.

## Installation
How to install the server package.

## Configuration
How to configure in AI app config files.

## Capabilities
List of tools/features provided.

## Usage Examples
Common usage patterns.
```

<!-- section_id: "e6475fec-6006-4a1b-a447-c1042a5fc26d" -->
### TROUBLESHOOTING.md Template

```markdown
# Troubleshooting <Server Name>

## Common Issues

### Issue: <Description>
**Symptoms:** What the user sees
**Cause:** Why this happens
**Solution:** How to fix it

## Diagnostic Commands
Commands to help debug issues.
```

---

<!-- section_id: "774b9159-9b42-4886-aa43-925c7a7dd545" -->
## Available MCP Servers

<!-- section_id: "27581832-2395-4efe-b104-663a4afc8875" -->
### Browser Automation
| Server | Description | Best For |
|--------|-------------|----------|
| `browser-mcp` | General browser automation | All platforms, especially Linux |
| `playwright-mcp` | Playwright-based automation | Cross-browser testing |
| `chrome-devtools-mcp` | Chrome DevTools Protocol | Chrome-specific debugging |
| `claude_in_chrome` | Claude browser extension | Chrome integration |

<!-- section_id: "9afa04c3-e1b8-4d4a-8773-72338c5097e1" -->
### Search & Knowledge
| Server | Description | API Key Required |
|--------|-------------|------------------|
| `tavily-mcp` | Web search API | Yes - TAVILY_API_KEY |
| `context7-mcp` | Library documentation | Yes - CONTEXT7_API_KEY |

<!-- section_id: "24be4a47-e9a4-4521-a610-af04eb8d840b" -->
### Core MCP (`_mcp_core/`)
Cross-server issues:
- Tool exposure issues (tools not showing in AI apps)
- Environment variable handling
- Node.js/NVM path issues
- Server timeout and connection problems
- Configuration file syntax
- Platform-specific bugs

---

<!-- section_id: "64555410-9854-4e37-9e94-202aa6e5e8db" -->
## MCP Setup Checklist

For each MCP server:

- [ ] Install the server package (npm, pip, etc.)
- [ ] Configure in AI app's MCP config file
- [ ] Set up required API keys (use secrets template pattern)
- [ ] Test server connection
- [ ] Verify tools are exposed to AI
- [ ] Document any issues in TROUBLESHOOTING.md

---

<!-- section_id: "a8d8eea9-54b9-48da-b9d3-57c8c149ebbd" -->
## Platform-Specific Notes

<!-- section_id: "7f70b517-81bc-41a7-abff-6dc58e3737db" -->
### Linux/Ubuntu
- Playwright MCP tools may not work in Cursor IDE (known bug)
- Use browser-mcp instead for Linux environments
- WSLg may be required for headed browser automation

<!-- section_id: "5e1b1fbf-8c74-4bf9-9500-0eb8619288ac" -->
### macOS
- Most MCP servers work out of the box
- May need to allow browser automation in System Preferences

<!-- section_id: "777231c9-faed-4547-a079-62db6d2aac01" -->
### Windows/WSL
- Path translation between Windows and Linux paths
- NVM requires bash wrapper in MCP config
- Display server (WSLg) needed for headed browsers

---

<!-- section_id: "7f64ede8-f73b-47e3-b4ad-577ab1dff2d3" -->
## Maintenance

<!-- section_id: "b076ecf5-f21c-4991-9d01-44bfb889ab20" -->
### When Adding a New MCP Server

1. Create directory: `<server-name>/`
2. Add `README.md` with setup instructions
3. Add `TROUBLESHOOTING.md` for common issues
4. Add `workflows/` directory if applicable
5. Update this README's server list
6. If server needs API keys, update `_shared/config.template.json`

<!-- section_id: "e36da9e1-078a-4727-b72c-f1b903e4e6e9" -->
### When Making Structural Changes

See the **Structural Change Checklist** in:
`0_context/layer_1/layer_1_features/layer_1_feature_layer_stage_system/README.md`

Key files to update:
1. `layer_1/layer_1_features/layer_1_feature_layer_stage_system/README.md` - change log
2. `universal_init_prompt.md` - directory paths
3. `sub_layer_registry.yaml` - registry entries
4. All docs via `find` + `sed` for bulk path updates

---

<!-- section_id: "21cb5d8c-cc72-40d1-9e1a-9e1385096c93" -->
## Quick Reference

| Need | Go To |
|------|-------|
| Set up API keys | `_shared/API_KEYS_SETUP.md` |
| Core MCP issues | `_mcp_core/general_issues_and_fixes/` |
| Server-specific setup | `<server-name>/README.md` |
| Troubleshooting | `<server-name>/TROUBLESHOOTING.md` |
| Workflow guides | `<server-name>/workflows/` |

---

*Last updated: 2026-01-13*
