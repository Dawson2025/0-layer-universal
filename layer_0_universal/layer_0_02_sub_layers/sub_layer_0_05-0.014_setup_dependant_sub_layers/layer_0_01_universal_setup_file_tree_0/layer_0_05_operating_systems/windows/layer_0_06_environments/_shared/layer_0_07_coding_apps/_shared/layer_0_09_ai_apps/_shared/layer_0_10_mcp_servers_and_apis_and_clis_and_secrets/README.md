# MCP Servers, APIs & Secrets Management

This directory contains documentation for Model Context Protocol (MCP) servers, API integrations, and secrets management patterns.

---

## Documentation System Overview

### Purpose

This system provides:
1. **MCP Server Documentation** - Setup, configuration, troubleshooting for each server
2. **API Key Management** - Secure handling of API keys without exposing them in the repo
3. **Secrets Template Pattern** - Share the repo safely while keeping secrets local
4. **Workflow Protocols** - Step-by-step guides for common tasks

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

## Secrets Template Pattern

### Why This Pattern?

Allows sharing the repository without exposing API keys, passwords, or other secrets.

### How It Works

| File | Committed to Git? | Contains |
|------|-------------------|----------|
| `config.template.json` | ✅ **Yes** | Placeholders like `${TAVILY_API_KEY}` |
| `config.local.json` | ❌ **No** | Actual API keys (gitignored) |
| `.env` files | ❌ **No** | Environment variables (gitignored) |

### Setup Flow for New Users

1. Navigate to `_shared/`
2. Copy `config.template.json` → `config.local.json`
3. Replace `${VAR}` placeholders with real API keys
4. Alternatively, set environment variables that the template references

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

### Getting API Keys

See `_shared/API_KEYS_SETUP.md` for instructions on obtaining keys for each service.

---

## Documentation Standard Per MCP Server

Each MCP server directory should contain:

| File | Required? | Purpose |
|------|-----------|---------|
| `README.md` | ✅ Yes | Installation, configuration, capabilities, usage examples |
| `TROUBLESHOOTING.md` | ✅ Yes | Common errors, solutions, diagnostic commands |
| `workflows/` | Recommended | Step-by-step protocols for specific tasks |

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

## Available MCP Servers

### Browser Automation
| Server | Description | Best For |
|--------|-------------|----------|
| `browser-mcp` | General browser automation | All platforms, especially Linux |
| `playwright-mcp` | Playwright-based automation | Cross-browser testing |
| `chrome-devtools-mcp` | Chrome DevTools Protocol | Chrome-specific debugging |
| `claude_in_chrome` | Claude browser extension | Chrome integration |

### Search & Knowledge
| Server | Description | API Key Required |
|--------|-------------|------------------|
| `tavily-mcp` | Web search API | Yes - TAVILY_API_KEY |
| `context7-mcp` | Library documentation | Yes - CONTEXT7_API_KEY |

### Core MCP (`_mcp_core/`)
Cross-server issues:
- Tool exposure issues (tools not showing in AI apps)
- Environment variable handling
- Node.js/NVM path issues
- Server timeout and connection problems
- Configuration file syntax
- Platform-specific bugs

---

## MCP Setup Checklist

For each MCP server:

- [ ] Install the server package (npm, pip, etc.)
- [ ] Configure in AI app's MCP config file
- [ ] Set up required API keys (use secrets template pattern)
- [ ] Test server connection
- [ ] Verify tools are exposed to AI
- [ ] Document any issues in TROUBLESHOOTING.md

---

## Platform-Specific Notes

### Linux/Ubuntu
- Playwright MCP tools may not work in Cursor IDE (known bug)
- Use browser-mcp instead for Linux environments
- WSLg may be required for headed browser automation

### macOS
- Most MCP servers work out of the box
- May need to allow browser automation in System Preferences

### Windows/WSL
- Path translation between Windows and Linux paths
- NVM requires bash wrapper in MCP config
- Display server (WSLg) needed for headed browsers

---

## Maintenance

### When Adding a New MCP Server

1. Create directory: `<server-name>/`
2. Add `README.md` with setup instructions
3. Add `TROUBLESHOOTING.md` for common issues
4. Add `workflows/` directory if applicable
5. Update this README's server list
6. If server needs API keys, update `_shared/config.template.json`

### When Making Structural Changes

See the **Structural Change Checklist** in:
`0_context/0.00_layer_stage_system/README.md`

Key files to update:
1. `0.00_layer_stage_system/README.md` - change log
2. `universal_init_prompt.md` - directory paths
3. `sub_layer_registry.yaml` - registry entries
4. All docs via `find` + `sed` for bulk path updates

---

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
