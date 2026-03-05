---
resource_id: "c05d5b7a-d3cb-4ca9-b318-b1c09b0f1aa7"
resource_type: "readme
document"
resource_name: "README"
---
# MCP Servers, APIs & Secrets Management

This directory contains documentation for Model Context Protocol (MCP) servers, API integrations, and secrets management patterns.

---

<!-- section_id: "e14ab1c1-d185-4f5c-b10b-9c0ca15921c3" -->
## Documentation System Overview

<!-- section_id: "46fe56c9-6847-4a13-bb8d-fd8d3f152cda" -->
### Purpose

This system provides:
1. **MCP Server Documentation** - Setup, configuration, troubleshooting for each server
2. **API Key Management** - Secure handling of API keys without exposing them in the repo
3. **Secrets Template Pattern** - Share the repo safely while keeping secrets local
4. **Workflow Protocols** - Step-by-step guides for common tasks

<!-- section_id: "957c3b23-7e70-4a38-92d0-ecdef2d5582d" -->
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

<!-- section_id: "4ca276d5-afdd-4e31-9519-50d84f4d2de3" -->
## Secrets Template Pattern

<!-- section_id: "760fe712-8873-4073-b620-ad4144f3fa6a" -->
### Why This Pattern?

Allows sharing the repository without exposing API keys, passwords, or other secrets.

<!-- section_id: "c43e5e96-559b-4ff9-8ab3-82939abe4ebc" -->
### How It Works

| File | Committed to Git? | Contains |
|------|-------------------|----------|
| `config.template.json` | ✅ **Yes** | Placeholders like `${TAVILY_API_KEY}` |
| `config.local.json` | ❌ **No** | Actual API keys (gitignored) |
| `.env` files | ❌ **No** | Environment variables (gitignored) |

<!-- section_id: "7aaaa488-fd0a-4045-a572-52d3fd43b593" -->
### Setup Flow for New Users

1. Navigate to `_shared/`
2. Copy `config.template.json` → `config.local.json`
3. Replace `${VAR}` placeholders with real API keys
4. Alternatively, set environment variables that the template references

<!-- section_id: "435b824c-1c48-4c33-8001-71b215d20944" -->
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

<!-- section_id: "754c4884-ff7c-478c-8125-deff7e3c5116" -->
### Getting API Keys

See `_shared/API_KEYS_SETUP.md` for instructions on obtaining keys for each service.

---

<!-- section_id: "a749a437-bb79-485f-8a5b-676b8c729f1e" -->
## Documentation Standard Per MCP Server

Each MCP server directory should contain:

| File | Required? | Purpose |
|------|-----------|---------|
| `README.md` | ✅ Yes | Installation, configuration, capabilities, usage examples |
| `TROUBLESHOOTING.md` | ✅ Yes | Common errors, solutions, diagnostic commands |
| `workflows/` | Recommended | Step-by-step protocols for specific tasks |

<!-- section_id: "da899775-3e96-47d8-896f-41847f914ddf" -->
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

<!-- section_id: "3210c70f-5942-4c46-81b0-9cd51dddecf2" -->
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

<!-- section_id: "4970cfd3-b69f-4865-aad5-4539251f6618" -->
## Available MCP Servers

<!-- section_id: "8f20286e-2b3a-48b4-921a-81603c585f43" -->
### Browser Automation
| Server | Description | Best For |
|--------|-------------|----------|
| `browser-mcp` | General browser automation | All platforms, especially Linux |
| `playwright-mcp` | Playwright-based automation | Cross-browser testing |
| `chrome-devtools-mcp` | Chrome DevTools Protocol | Chrome-specific debugging |
| `claude_in_chrome` | Claude browser extension | Chrome integration |

<!-- section_id: "975f0d58-6d9a-4f3f-ad89-4014b575ec87" -->
### Search & Knowledge
| Server | Description | API Key Required |
|--------|-------------|------------------|
| `tavily-mcp` | Web search API | Yes - TAVILY_API_KEY |
| `context7-mcp` | Library documentation | Yes - CONTEXT7_API_KEY |

<!-- section_id: "23b653dd-aa4d-4576-9802-e0711120403e" -->
### Core MCP (`_mcp_core/`)
Cross-server issues:
- Tool exposure issues (tools not showing in AI apps)
- Environment variable handling
- Node.js/NVM path issues
- Server timeout and connection problems
- Configuration file syntax
- Platform-specific bugs

---

<!-- section_id: "9545e2b4-c9c9-4169-8b15-841209bb1792" -->
## MCP Setup Checklist

For each MCP server:

- [ ] Install the server package (npm, pip, etc.)
- [ ] Configure in AI app's MCP config file
- [ ] Set up required API keys (use secrets template pattern)
- [ ] Test server connection
- [ ] Verify tools are exposed to AI
- [ ] Document any issues in TROUBLESHOOTING.md

---

<!-- section_id: "22820bf9-87fd-461d-9e04-ff7173db1f4d" -->
## Platform-Specific Notes

<!-- section_id: "a9021eea-41d4-443f-a0f2-99ed6a2fa478" -->
### Linux/Ubuntu
- Playwright MCP tools may not work in Cursor IDE (known bug)
- Use browser-mcp instead for Linux environments
- WSLg may be required for headed browser automation

<!-- section_id: "11859763-c8b4-4a04-a469-e10e4464ce1c" -->
### macOS
- Most MCP servers work out of the box
- May need to allow browser automation in System Preferences

<!-- section_id: "2c215555-7795-4857-b45c-ce7f731c4320" -->
### Windows/WSL
- Path translation between Windows and Linux paths
- NVM requires bash wrapper in MCP config
- Display server (WSLg) needed for headed browsers

---

<!-- section_id: "f1969356-ed65-4bcc-97f5-6bec0722c900" -->
## Maintenance

<!-- section_id: "d9c355fc-deeb-4601-812b-afbd37a3005a" -->
### When Adding a New MCP Server

1. Create directory: `<server-name>/`
2. Add `README.md` with setup instructions
3. Add `TROUBLESHOOTING.md` for common issues
4. Add `workflows/` directory if applicable
5. Update this README's server list
6. If server needs API keys, update `_shared/config.template.json`

<!-- section_id: "97c17505-115b-4b0d-86a2-bbbf615283f5" -->
### When Making Structural Changes

See the **Structural Change Checklist** in:
`0_context/layer_1/layer_1_features/layer_1_feature_layer_stage_system/README.md`

Key files to update:
1. `layer_1/layer_1_features/layer_1_feature_layer_stage_system/README.md` - change log
2. `universal_init_prompt.md` - directory paths
3. `sub_layer_registry.yaml` - registry entries
4. All docs via `find` + `sed` for bulk path updates

---

<!-- section_id: "9d6e24ad-2c99-475f-b577-4901b82ce22c" -->
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
