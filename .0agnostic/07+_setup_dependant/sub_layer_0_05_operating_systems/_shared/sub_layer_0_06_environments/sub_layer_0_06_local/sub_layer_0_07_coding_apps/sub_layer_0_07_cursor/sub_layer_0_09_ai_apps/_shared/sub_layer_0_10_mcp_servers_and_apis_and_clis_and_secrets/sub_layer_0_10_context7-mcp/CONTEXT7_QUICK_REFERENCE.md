---
resource_id: "bf430aa8-3391-4594-9f6b-91fe0e3d08cc"
resource_type: "document"
resource_name: "CONTEXT7_QUICK_REFERENCE"
---
# Context7 MCP Server - Quick Reference

<!-- section_id: "b130e135-0cf8-42c0-9e62-3972900ab367" -->
## 🔑 Your API Key
```
YOUR_CONTEXT7_API_KEY
```

<!-- section_id: "a4fa4d84-ce4c-4bb3-ab0f-8cda5914038b" -->
## 🚀 Claude Code Setup (Choose One)

<!-- section_id: "2743e046-49ce-466a-b586-4b7d6eca3552" -->
### Remote Server (Production)
```bash
claude mcp add --transport http context7 https://mcp.context7.com/mcp --header "CONTEXT7_API_KEY: YOUR_CONTEXT7_API_KEY"
```

<!-- section_id: "eb05c2d3-b856-4b81-9cc5-4edefccdc693" -->
### Local Server (Development)
```bash
claude mcp add context7 -- npx -y @upstash/context7-mcp --api-key YOUR_CONTEXT7_API_KEY
```

<!-- section_id: "5e229379-da38-41f4-bfe4-b6846d08203d" -->
## 🔧 MCP Management System

<!-- section_id: "6a572d49-49e4-4571-a96a-3a2433129ec4" -->
### Quick Setup
```bash
# Local server
python3 scripts/context7-setup.py setup-local

# Remote server
python3 scripts/context7-setup.py setup-remote

# Both options
python3 scripts/context7-setup.py setup-hybrid
```

<!-- section_id: "c876ba67-80c5-45e2-b1c3-7437d1125ac7" -->
### Status & Testing
```bash
# Check status
python3 scripts/context7-setup.py status

# Test local package
npx -y @upstash/context7-mcp --help

# Test remote endpoint
curl -I https://mcp.context7.com/mcp
```

<!-- section_id: "5e517345-2415-4bfd-9170-065c6f1f15c0" -->
## 📁 Configuration Files

| File | Purpose |
|------|---------|
| `.mcp.json` | Current active configuration |
| `config/mcp/examples/context7-local.json` | Local server example |
| `config/mcp/examples/context7-remote.json` | Remote server example |
| `config/mcp/examples/context7-hybrid.json` | Both options example |

<!-- section_id: "129c1e84-04c5-4d1e-a59d-ca5f460560ee" -->
## 🔄 Switch Configurations

```bash
# Switch to local
python3 scripts/context7-setup.py setup-local

# Switch to remote
python3 scripts/context7-setup.py setup-remote

# Switch to hybrid
python3 scripts/context7-setup.py setup-hybrid
```

<!-- section_id: "642097ea-6913-401d-b79d-7aa1f7414678" -->
## 🛠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| "Command not found: claude" | Install Claude Code CLI |
| "Package not found" | `npm install -g @upstash/context7-mcp` |
| "Connection refused" | Check internet, verify API key |
| "Invalid API key" | Verify: `YOUR_CONTEXT7_API_KEY` |

<!-- section_id: "265a6d2e-25e4-42d1-b042-e452c260c8bc" -->
## 📊 Check Status

```bash
# Context7 status
python3 scripts/context7-setup.py status

# Overall MCP status
python3 scripts/mcp-cli.py status

# System health
python3 scripts/mcp-cli.py health
```

<!-- section_id: "dffe295a-e8b8-4425-b318-c6a26de07b9f" -->
## 🎯 Recommendations

- **Development**: Use local server for better performance
- **Production**: Use remote server for simplicity
- **Flexibility**: Use hybrid setup for both options

<!-- section_id: "1dccfc54-2c99-4a0b-856e-b005f574c3f1" -->
## 📚 Full Documentation

- **Complete Setup Guide**: `docs/CONTEXT7_CLAUDE_SETUP.md`
- **MCP System Guide**: `docs/MCP_SYSTEM_GUIDE.md`
- **Configuration Examples**: `config/mcp/examples/`

---
**Ready to use!** Your Context7 MCP server is configured and ready for Claude Code integration. 🎉
