---
resource_id: "2cf2a075-0580-494e-9283-5c9e08f22cf9"
resource_type: "document"
resource_name: "CONTEXT7_QUICK_REFERENCE"
---
# Context7 MCP Server - Quick Reference

<!-- section_id: "be165d0f-c9be-4ce2-b0f6-e5f781fb4e6d" -->
## 🔑 Your API Key
```
ctx7sk-d20b6dec-5980-4ee1-9beb-0e635d626f46
```

<!-- section_id: "c502c8e9-680d-41e2-9217-8362c6cbdd04" -->
## 🚀 Claude Code Setup (Choose One)

<!-- section_id: "ee09ae9f-b4dd-4417-bfd1-c46b3fb4d56f" -->
### Remote Server (Production)
```bash
claude mcp add --transport http context7 https://mcp.context7.com/mcp --header "CONTEXT7_API_KEY: ctx7sk-d20b6dec-5980-4ee1-9beb-0e635d626f46"
```

<!-- section_id: "5fb14138-132c-4edd-abb0-c8ba2026c010" -->
### Local Server (Development)
```bash
claude mcp add context7 -- npx -y @upstash/context7-mcp --api-key ctx7sk-d20b6dec-5980-4ee1-9beb-0e635d626f46
```

<!-- section_id: "25a3f85b-8224-4593-8954-58d7d50553a5" -->
## 🔧 MCP Management System

<!-- section_id: "de3cef26-3fca-4d3b-89ff-046ecc462cbe" -->
### Quick Setup
```bash
# Local server
python3 scripts/context7-setup.py setup-local

# Remote server
python3 scripts/context7-setup.py setup-remote

# Both options
python3 scripts/context7-setup.py setup-hybrid
```

<!-- section_id: "d5352050-c2d2-425c-9a38-f0defa7dd637" -->
### Status & Testing
```bash
# Check status
python3 scripts/context7-setup.py status

# Test local package
npx -y @upstash/context7-mcp --help

# Test remote endpoint
curl -I https://mcp.context7.com/mcp
```

<!-- section_id: "0f56c4e5-b0ef-4f58-9dea-24ce7f56ca0e" -->
## 📁 Configuration Files

| File | Purpose |
|------|---------|
| `.mcp.json` | Current active configuration |
| `config/mcp/examples/context7-local.json` | Local server example |
| `config/mcp/examples/context7-remote.json` | Remote server example |
| `config/mcp/examples/context7-hybrid.json` | Both options example |

<!-- section_id: "63934f68-1e2a-4e3d-886e-9c2390b37995" -->
## 🔄 Switch Configurations

```bash
# Switch to local
python3 scripts/context7-setup.py setup-local

# Switch to remote
python3 scripts/context7-setup.py setup-remote

# Switch to hybrid
python3 scripts/context7-setup.py setup-hybrid
```

<!-- section_id: "60537580-62be-4983-9b30-e5002fa08f5e" -->
## 🛠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| "Command not found: claude" | Install Claude Code CLI |
| "Package not found" | `npm install -g @upstash/context7-mcp` |
| "Connection refused" | Check internet, verify API key |
| "Invalid API key" | Verify: `ctx7sk-d20b6dec-5980-4ee1-9beb-0e635d626f46` |

<!-- section_id: "af0aace6-77b8-428b-8edc-603561627787" -->
## 📊 Check Status

```bash
# Context7 status
python3 scripts/context7-setup.py status

# Overall MCP status
python3 scripts/mcp-cli.py status

# System health
python3 scripts/mcp-cli.py health
```

<!-- section_id: "2d47bc8f-6201-4427-b1ee-0f849399f5f8" -->
## 🎯 Recommendations

- **Development**: Use local server for better performance
- **Production**: Use remote server for simplicity
- **Flexibility**: Use hybrid setup for both options

<!-- section_id: "a3e62e0c-74b5-46a5-ab52-9def2d9d223c" -->
## 📚 Full Documentation

- **Complete Setup Guide**: `docs/CONTEXT7_CLAUDE_SETUP.md`
- **MCP System Guide**: `docs/MCP_SYSTEM_GUIDE.md`
- **Configuration Examples**: `config/mcp/examples/`

---
**Ready to use!** Your Context7 MCP server is configured and ready for Claude Code integration. 🎉
