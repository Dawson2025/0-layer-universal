---
resource_id: "afce012d-eb60-4d76-8147-82167a46ff94"
resource_type: "document"
resource_name: "CONTEXT7_QUICK_REFERENCE"
---
# Context7 MCP Server - Quick Reference

<!-- section_id: "994373d9-afae-4c24-938b-938323167587" -->
## 🔑 Your API Key
```
YOUR_CONTEXT7_API_KEY
```

<!-- section_id: "5d37c0bf-bff1-4fc1-803e-da6927940bf6" -->
## 🚀 Claude Code Setup (Choose One)

<!-- section_id: "38f461cf-5cb1-4023-8bb8-2f5c67078df0" -->
### Remote Server (Production)
```bash
claude mcp add --transport http context7 https://mcp.context7.com/mcp --header "CONTEXT7_API_KEY: YOUR_CONTEXT7_API_KEY"
```

<!-- section_id: "ea44a3b9-8d58-4743-ba3f-62d05f984169" -->
### Local Server (Development)
```bash
claude mcp add context7 -- npx -y @upstash/context7-mcp --api-key YOUR_CONTEXT7_API_KEY
```

<!-- section_id: "6534c189-d57f-43d2-aef8-a88ab64c2ccb" -->
## 🔧 MCP Management System

<!-- section_id: "9b944f44-9a3f-4731-91ed-8814e82dc02e" -->
### Quick Setup
```bash
# Local server
python3 scripts/context7-setup.py setup-local

# Remote server
python3 scripts/context7-setup.py setup-remote

# Both options
python3 scripts/context7-setup.py setup-hybrid
```

<!-- section_id: "4baf1ea5-200b-41a9-a682-c58c1af16c9b" -->
### Status & Testing
```bash
# Check status
python3 scripts/context7-setup.py status

# Test local package
npx -y @upstash/context7-mcp --help

# Test remote endpoint
curl -I https://mcp.context7.com/mcp
```

<!-- section_id: "a86cf9a4-cb49-4e75-abd1-113745f032ad" -->
## 📁 Configuration Files

| File | Purpose |
|------|---------|
| `.mcp.json` | Current active configuration |
| `config/mcp/examples/context7-local.json` | Local server example |
| `config/mcp/examples/context7-remote.json` | Remote server example |
| `config/mcp/examples/context7-hybrid.json` | Both options example |

<!-- section_id: "baf1fd33-ae75-444f-b87d-4eec349cfd0c" -->
## 🔄 Switch Configurations

```bash
# Switch to local
python3 scripts/context7-setup.py setup-local

# Switch to remote
python3 scripts/context7-setup.py setup-remote

# Switch to hybrid
python3 scripts/context7-setup.py setup-hybrid
```

<!-- section_id: "b71861d2-143f-4485-8810-7e1943a0ccf3" -->
## 🛠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| "Command not found: claude" | Install Claude Code CLI |
| "Package not found" | `npm install -g @upstash/context7-mcp` |
| "Connection refused" | Check internet, verify API key |
| "Invalid API key" | Verify: `YOUR_CONTEXT7_API_KEY` |

<!-- section_id: "eb92c190-d026-4963-b191-3fe70702a5a9" -->
## 📊 Check Status

```bash
# Context7 status
python3 scripts/context7-setup.py status

# Overall MCP status
python3 scripts/mcp-cli.py status

# System health
python3 scripts/mcp-cli.py health
```

<!-- section_id: "97064bc2-8e2f-4a7e-a0ab-18395242c6ff" -->
## 🎯 Recommendations

- **Development**: Use local server for better performance
- **Production**: Use remote server for simplicity
- **Flexibility**: Use hybrid setup for both options

<!-- section_id: "87d5bd59-71c5-4f92-be47-e0cc2ed1ab70" -->
## 📚 Full Documentation

- **Complete Setup Guide**: `docs/CONTEXT7_CLAUDE_SETUP.md`
- **MCP System Guide**: `docs/MCP_SYSTEM_GUIDE.md`
- **Configuration Examples**: `config/mcp/examples/`

---
**Ready to use!** Your Context7 MCP server is configured and ready for Claude Code integration. 🎉
