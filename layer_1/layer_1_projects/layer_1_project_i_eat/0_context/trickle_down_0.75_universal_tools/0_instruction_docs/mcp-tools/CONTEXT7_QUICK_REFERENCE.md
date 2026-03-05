---
resource_id: "3c60a70d-15a6-4626-809b-9d788dc18f09"
resource_type: "document"
resource_name: "CONTEXT7_QUICK_REFERENCE"
---
# Context7 MCP Server - Quick Reference

<!-- section_id: "3d27f3e9-d96a-4021-900c-52dea24c3c9d" -->
## 🔑 Your API Key
```
ctx7sk-d20b6dec-5980-4ee1-9beb-0e635d626f46
```

<!-- section_id: "8a340fc5-9100-499a-ad67-7d6f1230c3b9" -->
## 🚀 Claude Code Setup (Choose One)

<!-- section_id: "5b9b037f-fe23-4c2f-a1a4-5df4415fdb90" -->
### Remote Server (Production)
```bash
claude mcp add --transport http context7 https://mcp.context7.com/mcp --header "CONTEXT7_API_KEY: ctx7sk-d20b6dec-5980-4ee1-9beb-0e635d626f46"
```

<!-- section_id: "d1c9ad10-e444-4191-99ba-6e90b1659ed7" -->
### Local Server (Development)
```bash
claude mcp add context7 -- npx -y @upstash/context7-mcp --api-key ctx7sk-d20b6dec-5980-4ee1-9beb-0e635d626f46
```

<!-- section_id: "4846cdc9-339a-43ad-b323-d130c884b91d" -->
## 🔧 MCP Management System

<!-- section_id: "b3811722-acd0-4bf3-a207-8392d47b0598" -->
### Quick Setup
```bash
# Local server
python3 scripts/context7-setup.py setup-local

# Remote server
python3 scripts/context7-setup.py setup-remote

# Both options
python3 scripts/context7-setup.py setup-hybrid
```

<!-- section_id: "e77db44e-c01e-44a0-aa89-9d5f7174c36b" -->
### Status & Testing
```bash
# Check status
python3 scripts/context7-setup.py status

# Test local package
npx -y @upstash/context7-mcp --help

# Test remote endpoint
curl -I https://mcp.context7.com/mcp
```

<!-- section_id: "399228c8-3e60-448c-933f-d3945fd55bad" -->
## 📁 Configuration Files

| File | Purpose |
|------|---------|
| `.mcp.json` | Current active configuration |
| `config/mcp/examples/context7-local.json` | Local server example |
| `config/mcp/examples/context7-remote.json` | Remote server example |
| `config/mcp/examples/context7-hybrid.json` | Both options example |

<!-- section_id: "81d38c38-cebe-4332-a88a-ca0db70d77cf" -->
## 🔄 Switch Configurations

```bash
# Switch to local
python3 scripts/context7-setup.py setup-local

# Switch to remote
python3 scripts/context7-setup.py setup-remote

# Switch to hybrid
python3 scripts/context7-setup.py setup-hybrid
```

<!-- section_id: "1079a855-0840-4405-864e-9b8df6ad1199" -->
## 🛠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| "Command not found: claude" | Install Claude Code CLI |
| "Package not found" | `npm install -g @upstash/context7-mcp` |
| "Connection refused" | Check internet, verify API key |
| "Invalid API key" | Verify: `ctx7sk-d20b6dec-5980-4ee1-9beb-0e635d626f46` |

<!-- section_id: "296caa60-e56d-4c57-b1ef-1d7c74d003b0" -->
## 📊 Check Status

```bash
# Context7 status
python3 scripts/context7-setup.py status

# Overall MCP status
python3 scripts/mcp-cli.py status

# System health
python3 scripts/mcp-cli.py health
```

<!-- section_id: "a17ad92d-bdd7-4b88-9bf6-9574a1c2a418" -->
## 🎯 Recommendations

- **Development**: Use local server for better performance
- **Production**: Use remote server for simplicity
- **Flexibility**: Use hybrid setup for both options

<!-- section_id: "216448a9-00c4-406b-a7f1-83d517826f55" -->
## 📚 Full Documentation

- **Complete Setup Guide**: `docs/CONTEXT7_CLAUDE_SETUP.md`
- **MCP System Guide**: `docs/MCP_SYSTEM_GUIDE.md`
- **Configuration Examples**: `config/mcp/examples/`

---
**Ready to use!** Your Context7 MCP server is configured and ready for Claude Code integration. 🎉
