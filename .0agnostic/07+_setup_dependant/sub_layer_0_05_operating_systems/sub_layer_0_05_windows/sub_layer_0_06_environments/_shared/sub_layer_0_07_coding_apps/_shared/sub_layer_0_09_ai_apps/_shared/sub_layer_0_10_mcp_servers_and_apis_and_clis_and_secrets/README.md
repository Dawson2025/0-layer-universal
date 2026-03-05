---
resource_id: "e67c5711-ad41-4d06-84b4-4bd6d7b6ad8e"
resource_type: "readme
document"
resource_name: "README"
---
# MCP Servers, APIs & Secrets Management

This directory contains documentation for Model Context Protocol (MCP) servers, API integrations, and secrets management patterns.

---

<!-- section_id: "5baaf07f-6e81-4dab-8ab3-db76a3d215a3" -->
## Documentation System Overview

<!-- section_id: "56b49d0a-b525-444c-af0c-d4f35fd3672a" -->
### Purpose

This system provides:
1. **MCP Server Documentation** - Setup, configuration, troubleshooting for each server
2. **API Key Management** - Secure handling of API keys without exposing them in the repo
3. **Secrets Template Pattern** - Share the repo safely while keeping secrets local
4. **Workflow Protocols** - Step-by-step guides for common tasks

<!-- section_id: "8fe47677-832a-4767-8c30-aa9b9ac7989a" -->
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

<!-- section_id: "bc3e219c-0ee5-4962-8a98-51397c24da15" -->
## Secrets Template Pattern

<!-- section_id: "9eccbf05-22ef-4625-a406-1d18bf58d54a" -->
### Why This Pattern?

Allows sharing the repository without exposing API keys, passwords, or other secrets.

<!-- section_id: "1a68ae12-74e2-4bb7-a7d5-e6f1d7c043f6" -->
### How It Works

| File | Committed to Git? | Contains |
|------|-------------------|----------|
| `config.template.json` | ✅ **Yes** | Placeholders like `${TAVILY_API_KEY}` |
| `config.local.json` | ❌ **No** | Actual API keys (gitignored) |
| `.env` files | ❌ **No** | Environment variables (gitignored) |

<!-- section_id: "b369d0fc-885b-4977-9f91-736b42868be4" -->
### Setup Flow for New Users

1. Navigate to `_shared/`
2. Copy `config.template.json` → `config.local.json`
3. Replace `${VAR}` placeholders with real API keys
4. Alternatively, set environment variables that the template references

<!-- section_id: "126a0c4f-2c4e-499c-b8cd-66c4a8239b83" -->
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

<!-- section_id: "d15608ad-344f-487a-a03a-c6f30d4998b3" -->
### Getting API Keys

See `_shared/API_KEYS_SETUP.md` for instructions on obtaining keys for each service.

---

<!-- section_id: "1d08339b-3565-442a-aa30-74931399612a" -->
## Documentation Standard Per MCP Server

Each MCP server directory should contain:

| File | Required? | Purpose |
|------|-----------|---------|
| `README.md` | ✅ Yes | Installation, configuration, capabilities, usage examples |
| `TROUBLESHOOTING.md` | ✅ Yes | Common errors, solutions, diagnostic commands |
| `workflows/` | Recommended | Step-by-step protocols for specific tasks |

<!-- section_id: "77331254-23b2-4c20-86c5-6c8f76bbf963" -->
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

<!-- section_id: "a69b7a63-89c2-4075-927a-330a3896791a" -->
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

<!-- section_id: "9949abae-d481-413b-8a1d-6c7260ad80b4" -->
## Available MCP Servers

<!-- section_id: "3bbb04c3-a0af-4369-814f-0334dcc78fdb" -->
### Browser Automation
| Server | Description | Best For |
|--------|-------------|----------|
| `browser-mcp` | General browser automation | All platforms, especially Linux |
| `playwright-mcp` | Playwright-based automation | Cross-browser testing |
| `chrome-devtools-mcp` | Chrome DevTools Protocol | Chrome-specific debugging |
| `claude_in_chrome` | Claude browser extension | Chrome integration |

<!-- section_id: "d7a890d7-769c-4342-8b99-6746038e5754" -->
### Search & Knowledge
| Server | Description | API Key Required |
|--------|-------------|------------------|
| `tavily-mcp` | Web search API | Yes - TAVILY_API_KEY |
| `context7-mcp` | Library documentation | Yes - CONTEXT7_API_KEY |

<!-- section_id: "1b05c06c-87eb-4709-ba23-d9dda800b447" -->
### Core MCP (`_mcp_core/`)
Cross-server issues:
- Tool exposure issues (tools not showing in AI apps)
- Environment variable handling
- Node.js/NVM path issues
- Server timeout and connection problems
- Configuration file syntax
- Platform-specific bugs

---

<!-- section_id: "a844a5ec-41fb-4d6f-8e9e-3298f19dcee4" -->
## MCP Setup Checklist

For each MCP server:

- [ ] Install the server package (npm, pip, etc.)
- [ ] Configure in AI app's MCP config file
- [ ] Set up required API keys (use secrets template pattern)
- [ ] Test server connection
- [ ] Verify tools are exposed to AI
- [ ] Document any issues in TROUBLESHOOTING.md

---

<!-- section_id: "87890597-f9ec-4280-8aeb-eef7465f2597" -->
## Platform-Specific Notes

<!-- section_id: "0a4ac2fc-17c2-466b-9a82-f64e20c1d740" -->
### Linux/Ubuntu
- Playwright MCP tools may not work in Cursor IDE (known bug)
- Use browser-mcp instead for Linux environments
- WSLg may be required for headed browser automation

<!-- section_id: "f9fd2129-ff32-4cfb-9ccb-a559139ac97b" -->
### macOS
- Most MCP servers work out of the box
- May need to allow browser automation in System Preferences

<!-- section_id: "059f97aa-c359-4360-963c-5d980c63e4dc" -->
### Windows/WSL
- Path translation between Windows and Linux paths
- NVM requires bash wrapper in MCP config
- Display server (WSLg) needed for headed browsers

---

<!-- section_id: "daba4cd1-3aab-4134-aa04-2cd27d6d439d" -->
## Maintenance

<!-- section_id: "43d233c0-b1eb-4d8b-9c54-6f746aea2f28" -->
### When Adding a New MCP Server

1. Create directory: `<server-name>/`
2. Add `README.md` with setup instructions
3. Add `TROUBLESHOOTING.md` for common issues
4. Add `workflows/` directory if applicable
5. Update this README's server list
6. If server needs API keys, update `_shared/config.template.json`

<!-- section_id: "f3187362-59d8-43ed-8d0c-01e354119980" -->
### When Making Structural Changes

See the **Structural Change Checklist** in:
`0_context/layer_1/layer_1_features/layer_1_feature_layer_stage_system/README.md`

Key files to update:
1. `layer_1/layer_1_features/layer_1_feature_layer_stage_system/README.md` - change log
2. `universal_init_prompt.md` - directory paths
3. `sub_layer_registry.yaml` - registry entries
4. All docs via `find` + `sed` for bulk path updates

---

<!-- section_id: "bfdd65d6-b3f8-491e-83e1-234e1aa47a0e" -->
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
