---
resource_id: "d2f0569a-9fb2-4a0c-aa86-ed33b8ad2f2f"
resource_type: "document"
resource_name: "CONTEXT7_QUICK_REFERENCE"
---
# Context7 MCP Server - Quick Reference

<!-- section_id: "f42017cf-a920-4f5a-8ace-1ba5093c5be1" -->
## 🔑 Your API Key
```
YOUR_CONTEXT7_API_KEY
```

<!-- section_id: "1b6fe63d-5b60-403e-949e-474517569e23" -->
## 🚀 Claude Code Setup (Choose One)

<!-- section_id: "48fe1a04-14f4-4270-9e80-7fe0ebf436d5" -->
### Remote Server (Production)
```bash
claude mcp add --transport http context7 https://mcp.context7.com/mcp --header "CONTEXT7_API_KEY: YOUR_CONTEXT7_API_KEY"
```

<!-- section_id: "c75be42b-5000-4e47-9674-acf63306826a" -->
### Local Server (Development)
```bash
claude mcp add context7 -- npx -y @upstash/context7-mcp --api-key YOUR_CONTEXT7_API_KEY
```

<!-- section_id: "00da384c-0458-481f-822a-4ed888406ea5" -->
## 🔧 MCP Management System

<!-- section_id: "dc29c356-88f7-4d8d-b7dd-43910286b8b7" -->
### Quick Setup
```bash
# Local server
python3 scripts/context7-setup.py setup-local

# Remote server
python3 scripts/context7-setup.py setup-remote

# Both options
python3 scripts/context7-setup.py setup-hybrid
```

<!-- section_id: "1a5d754e-bb07-4e45-8f82-c00a28f6c96e" -->
### Status & Testing
```bash
# Check status
python3 scripts/context7-setup.py status

# Test local package
npx -y @upstash/context7-mcp --help

# Test remote endpoint
curl -I https://mcp.context7.com/mcp
```

<!-- section_id: "8fd20829-36f8-4326-a07a-7a248d39fc1b" -->
## 📁 Configuration Files

| File | Purpose |
|------|---------|
| `.mcp.json` | Current active configuration |
| `config/mcp/examples/context7-local.json` | Local server example |
| `config/mcp/examples/context7-remote.json` | Remote server example |
| `config/mcp/examples/context7-hybrid.json` | Both options example |

<!-- section_id: "8b78f1ac-891c-4058-b75a-249eb760a721" -->
## 🔄 Switch Configurations

```bash
# Switch to local
python3 scripts/context7-setup.py setup-local

# Switch to remote
python3 scripts/context7-setup.py setup-remote

# Switch to hybrid
python3 scripts/context7-setup.py setup-hybrid
```

<!-- section_id: "ba8a8e08-8a1d-48c0-ad81-55863be7b662" -->
## 🛠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| "Command not found: claude" | Install Claude Code CLI |
| "Package not found" | `npm install -g @upstash/context7-mcp` |
| "Connection refused" | Check internet, verify API key |
| "Invalid API key" | Verify: `YOUR_CONTEXT7_API_KEY` |

<!-- section_id: "32f497f5-85b8-4d43-a055-c7cf9e3c6cbf" -->
## 📊 Check Status

```bash
# Context7 status
python3 scripts/context7-setup.py status

# Overall MCP status
python3 scripts/mcp-cli.py status

# System health
python3 scripts/mcp-cli.py health
```

<!-- section_id: "52ef73b6-d7e5-41d6-a876-d6cffbd20495" -->
## 🎯 Recommendations

- **Development**: Use local server for better performance
- **Production**: Use remote server for simplicity
- **Flexibility**: Use hybrid setup for both options

<!-- section_id: "a6bc154d-4041-4fd0-838c-918a51be1efe" -->
## 📚 Full Documentation

- **Complete Setup Guide**: `docs/CONTEXT7_CLAUDE_SETUP.md`
- **MCP System Guide**: `docs/MCP_SYSTEM_GUIDE.md`
- **Configuration Examples**: `config/mcp/examples/`

---
**Ready to use!** Your Context7 MCP server is configured and ready for Claude Code integration. 🎉
