---
resource_id: "4c637b97-7bff-460b-add2-b7eb02444458"
resource_type: "readme_document"
resource_name: "README"
---
# MCP Servers, APIs & Secrets Management

This directory contains documentation for Model Context Protocol (MCP) servers, API integrations, and secrets management patterns.

---

<!-- section_id: "9d8d3461-f63e-4505-ac44-26c9d971a18f" -->
## Documentation System Overview

<!-- section_id: "3b748142-0b75-4265-a8fc-89949ce07948" -->
### Purpose

This system provides:
1. **MCP Server Documentation** - Setup, configuration, troubleshooting for each server
2. **API Key Management** - Secure handling of API keys without exposing them in the repo
3. **Secrets Template Pattern** - Share the repo safely while keeping secrets local
4. **Workflow Protocols** - Step-by-step guides for common tasks

<!-- section_id: "f5625d25-25d2-457d-88b3-a088fae41255" -->
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

<!-- section_id: "26c89e8d-072d-4db7-91bd-304b5689caaa" -->
## Secrets Template Pattern

<!-- section_id: "28798100-f3bc-4f7a-8282-1fdf4896b9e5" -->
### Why This Pattern?

Allows sharing the repository without exposing API keys, passwords, or other secrets.

<!-- section_id: "b8cd54f9-bd51-48ea-902a-5dd84fa51a9d" -->
### How It Works

| File | Committed to Git? | Contains |
|------|-------------------|----------|
| `config.template.json` | ✅ **Yes** | Placeholders like `${TAVILY_API_KEY}` |
| `config.local.json` | ❌ **No** | Actual API keys (gitignored) |
| `.env` files | ❌ **No** | Environment variables (gitignored) |

<!-- section_id: "c2788062-6091-4252-85dd-9132bc0173fd" -->
### Setup Flow for New Users

1. Navigate to `_shared/`
2. Copy `config.template.json` → `config.local.json`
3. Replace `${VAR}` placeholders with real API keys
4. Alternatively, set environment variables that the template references

<!-- section_id: "0e0c611e-1a5d-4b0c-86da-4f70b5ac1187" -->
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

<!-- section_id: "99539550-c27b-4b5b-a730-3bc6e41b09d9" -->
### Getting API Keys

See `_shared/API_KEYS_SETUP.md` for instructions on obtaining keys for each service.

---

<!-- section_id: "839c3b5c-d90e-4f8a-acae-c8b4c2e38b7b" -->
## Documentation Standard Per MCP Server

Each MCP server directory should contain:

| File | Required? | Purpose |
|------|-----------|---------|
| `README.md` | ✅ Yes | Installation, configuration, capabilities, usage examples |
| `TROUBLESHOOTING.md` | ✅ Yes | Common errors, solutions, diagnostic commands |
| `workflows/` | Recommended | Step-by-step protocols for specific tasks |

<!-- section_id: "cb43c19c-d5bb-4fc7-99b6-9e132b2524e1" -->
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

<!-- section_id: "fdef11e4-1f33-4088-8aab-767af6c75e2b" -->
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

<!-- section_id: "d63afea1-960f-43d1-9708-7b07cfc7ffdb" -->
## Available MCP Servers

<!-- section_id: "da35d994-0b7d-4376-914a-51a647de4037" -->
### Browser Automation
| Server | Description | Best For |
|--------|-------------|----------|
| `browser-mcp` | General browser automation | All platforms, especially Linux |
| `playwright-mcp` | Playwright-based automation | Cross-browser testing |
| `chrome-devtools-mcp` | Chrome DevTools Protocol | Chrome-specific debugging |
| `claude_in_chrome` | Claude browser extension | Chrome integration |

<!-- section_id: "71b8617f-b1c1-4ea8-a61f-5236672eeb7d" -->
### Search & Knowledge
| Server | Description | API Key Required |
|--------|-------------|------------------|
| `tavily-mcp` | Web search API | Yes - TAVILY_API_KEY |
| `context7-mcp` | Library documentation | Yes - CONTEXT7_API_KEY |

<!-- section_id: "05841a2b-fb00-4aa3-a2ee-f9d2d17a6294" -->
### Core MCP (`_mcp_core/`)
Cross-server issues:
- Tool exposure issues (tools not showing in AI apps)
- Environment variable handling
- Node.js/NVM path issues
- Server timeout and connection problems
- Configuration file syntax
- Platform-specific bugs

---

<!-- section_id: "746f4e7f-1f82-44d6-879d-2fd34f34258b" -->
## MCP Setup Checklist

For each MCP server:

- [ ] Install the server package (npm, pip, etc.)
- [ ] Configure in AI app's MCP config file
- [ ] Set up required API keys (use secrets template pattern)
- [ ] Test server connection
- [ ] Verify tools are exposed to AI
- [ ] Document any issues in TROUBLESHOOTING.md

---

<!-- section_id: "b5e8a723-208f-456e-9f6c-88d15bd24093" -->
## Platform-Specific Notes

<!-- section_id: "8aba6040-acb6-4f69-a29c-0d1e16118345" -->
### Linux/Ubuntu
- Playwright MCP tools may not work in Cursor IDE (known bug)
- Use browser-mcp instead for Linux environments
- WSLg may be required for headed browser automation

<!-- section_id: "20b8b381-c720-42b7-9dfc-3e369750703c" -->
### macOS
- Most MCP servers work out of the box
- May need to allow browser automation in System Preferences

<!-- section_id: "bc8236ad-aae3-4363-b3b9-44fa04ad1468" -->
### Windows/WSL
- Path translation between Windows and Linux paths
- NVM requires bash wrapper in MCP config
- Display server (WSLg) needed for headed browsers

---

<!-- section_id: "25b4d4d0-f314-45ff-8368-be910f9d1688" -->
## Maintenance

<!-- section_id: "a613f404-7364-4fd3-a354-4e9a7ad74bef" -->
### When Adding a New MCP Server

1. Create directory: `<server-name>/`
2. Add `README.md` with setup instructions
3. Add `TROUBLESHOOTING.md` for common issues
4. Add `workflows/` directory if applicable
5. Update this README's server list
6. If server needs API keys, update `_shared/config.template.json`

<!-- section_id: "ee8dd975-397e-4f13-8780-75caa3610390" -->
### When Making Structural Changes

See the **Structural Change Checklist** in:
`0_context/layer_1/layer_1_features/layer_1_feature_layer_stage_system/README.md`

Key files to update:
1. `layer_1/layer_1_features/layer_1_feature_layer_stage_system/README.md` - change log
2. `universal_init_prompt.md` - directory paths
3. `sub_layer_registry.yaml` - registry entries
4. All docs via `find` + `sed` for bulk path updates

---

<!-- section_id: "4a67cdcc-0b7c-4749-b80e-a043e00ba449" -->
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
