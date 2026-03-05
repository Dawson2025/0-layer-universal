---
resource_id: "f955c8e5-1cc9-4713-b05b-92769b988e47"
resource_type: "readme
document"
resource_name: "README"
---
# MCP Servers, APIs & Secrets Management

This directory contains documentation for Model Context Protocol (MCP) servers, API integrations, and secrets management patterns.

---

<!-- section_id: "87bb3205-ddf7-4278-a681-84140316040e" -->
## Documentation System Overview

<!-- section_id: "3ec065a3-ac67-45cb-b655-f7bd6b84243f" -->
### Purpose

This system provides:
1. **MCP Server Documentation** - Setup, configuration, troubleshooting for each server
2. **API Key Management** - Secure handling of API keys without exposing them in the repo
3. **Secrets Template Pattern** - Share the repo safely while keeping secrets local
4. **Workflow Protocols** - Step-by-step guides for common tasks

<!-- section_id: "6a4ec005-c962-476c-af2c-fe4d4692befa" -->
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

<!-- section_id: "5a2b4757-13c9-4635-9f34-89fd24dd62cd" -->
## Secrets Template Pattern

<!-- section_id: "14e7f479-7a86-450c-a922-311cbb3a9fe4" -->
### Why This Pattern?

Allows sharing the repository without exposing API keys, passwords, or other secrets.

<!-- section_id: "7a632366-cd60-4421-a4e2-bf61b0fbbc0e" -->
### How It Works

| File | Committed to Git? | Contains |
|------|-------------------|----------|
| `config.template.json` | ✅ **Yes** | Placeholders like `${TAVILY_API_KEY}` |
| `config.local.json` | ❌ **No** | Actual API keys (gitignored) |
| `.env` files | ❌ **No** | Environment variables (gitignored) |

<!-- section_id: "9347ecc5-84d1-4107-b784-95cdecfe4371" -->
### Setup Flow for New Users

1. Navigate to `_shared/`
2. Copy `config.template.json` → `config.local.json`
3. Replace `${VAR}` placeholders with real API keys
4. Alternatively, set environment variables that the template references

<!-- section_id: "8adbf746-adc5-4798-93bb-e165a352cd95" -->
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

<!-- section_id: "e3519d2f-6d97-42f8-9e3b-05ae93aa3ea7" -->
### Getting API Keys

See `_shared/API_KEYS_SETUP.md` for instructions on obtaining keys for each service.

---

<!-- section_id: "626431af-b7d5-43d2-bd0c-a3abb9ac8094" -->
## Documentation Standard Per MCP Server

Each MCP server directory should contain:

| File | Required? | Purpose |
|------|-----------|---------|
| `README.md` | ✅ Yes | Installation, configuration, capabilities, usage examples |
| `TROUBLESHOOTING.md` | ✅ Yes | Common errors, solutions, diagnostic commands |
| `workflows/` | Recommended | Step-by-step protocols for specific tasks |

<!-- section_id: "92c86135-f71a-487f-829a-7950560f2ab3" -->
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

<!-- section_id: "306c09ae-0e51-4b44-bea3-cf802b50f040" -->
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

<!-- section_id: "57f0d376-170d-4954-ab64-ed8f3d107e99" -->
## Available MCP Servers

<!-- section_id: "1bce877a-30f4-4752-9ec0-7d403504ee1c" -->
### Browser Automation
| Server | Description | Best For |
|--------|-------------|----------|
| `browser-mcp` | General browser automation | All platforms, especially Linux |
| `playwright-mcp` | Playwright-based automation | Cross-browser testing |
| `chrome-devtools-mcp` | Chrome DevTools Protocol | Chrome-specific debugging |
| `claude_in_chrome` | Claude browser extension | Chrome integration |

<!-- section_id: "8e20d63c-67a1-4c60-9568-a2a548196f82" -->
### Search & Knowledge
| Server | Description | API Key Required |
|--------|-------------|------------------|
| `tavily-mcp` | Web search API | Yes - TAVILY_API_KEY |
| `context7-mcp` | Library documentation | Yes - CONTEXT7_API_KEY |

<!-- section_id: "649f250a-b23f-4cd0-a840-5604b61f9c09" -->
### Core MCP (`_mcp_core/`)
Cross-server issues:
- Tool exposure issues (tools not showing in AI apps)
- Environment variable handling
- Node.js/NVM path issues
- Server timeout and connection problems
- Configuration file syntax
- Platform-specific bugs

---

<!-- section_id: "e71134bd-6664-48d1-8dde-7f4e38b6c99d" -->
## MCP Setup Checklist

For each MCP server:

- [ ] Install the server package (npm, pip, etc.)
- [ ] Configure in AI app's MCP config file
- [ ] Set up required API keys (use secrets template pattern)
- [ ] Test server connection
- [ ] Verify tools are exposed to AI
- [ ] Document any issues in TROUBLESHOOTING.md

---

<!-- section_id: "22dbca13-b79f-40c4-b467-e8f851a7f64c" -->
## Platform-Specific Notes

<!-- section_id: "424db31d-15bd-4468-8c80-c995adf45739" -->
### Linux/Ubuntu
- Playwright MCP tools may not work in Cursor IDE (known bug)
- Use browser-mcp instead for Linux environments
- WSLg may be required for headed browser automation

<!-- section_id: "e4f40545-15bc-4771-9a4c-542c6ab6ca4e" -->
### macOS
- Most MCP servers work out of the box
- May need to allow browser automation in System Preferences

<!-- section_id: "52670521-8abe-49f6-8963-96f8bf38a65b" -->
### Windows/WSL
- Path translation between Windows and Linux paths
- NVM requires bash wrapper in MCP config
- Display server (WSLg) needed for headed browsers

---

<!-- section_id: "8c66ea73-e742-40c5-8227-04a0cbc0456e" -->
## Maintenance

<!-- section_id: "b7493fbf-8ffc-46fe-9a3b-3df0639c8140" -->
### When Adding a New MCP Server

1. Create directory: `<server-name>/`
2. Add `README.md` with setup instructions
3. Add `TROUBLESHOOTING.md` for common issues
4. Add `workflows/` directory if applicable
5. Update this README's server list
6. If server needs API keys, update `_shared/config.template.json`

<!-- section_id: "75435da9-b1f9-4645-979a-f2a2a3d91ff2" -->
### When Making Structural Changes

See the **Structural Change Checklist** in:
`0_context/layer_1/layer_1_features/layer_1_feature_layer_stage_system/README.md`

Key files to update:
1. `layer_1/layer_1_features/layer_1_feature_layer_stage_system/README.md` - change log
2. `universal_init_prompt.md` - directory paths
3. `sub_layer_registry.yaml` - registry entries
4. All docs via `find` + `sed` for bulk path updates

---

<!-- section_id: "fac70f3f-cc9f-4fbb-b400-7c341c7f1b22" -->
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
