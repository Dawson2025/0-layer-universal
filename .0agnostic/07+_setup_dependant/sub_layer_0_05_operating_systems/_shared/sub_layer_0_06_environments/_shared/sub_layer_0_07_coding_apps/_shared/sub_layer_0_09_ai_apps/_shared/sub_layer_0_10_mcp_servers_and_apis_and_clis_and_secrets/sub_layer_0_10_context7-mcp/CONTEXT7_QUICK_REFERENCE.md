---
resource_id: "ece36160-c374-412a-81f9-0cfd9d888adb"
resource_type: "document"
resource_name: "CONTEXT7_QUICK_REFERENCE"
---
# Context7 MCP Server - Quick Reference

<!-- section_id: "a7ac01a1-3800-42b0-af79-f524a65963b1" -->
## 🔑 Your API Key
```
YOUR_CONTEXT7_API_KEY
```

<!-- section_id: "9b9d2085-2491-4565-88c7-ee931b547e0f" -->
## 🚀 Claude Code Setup (Choose One)

<!-- section_id: "a173a18e-7306-4c51-b009-4793824fb427" -->
### Remote Server (Production)
```bash
claude mcp add --transport http context7 https://mcp.context7.com/mcp --header "CONTEXT7_API_KEY: YOUR_CONTEXT7_API_KEY"
```

<!-- section_id: "8c4ca311-0d99-4de3-9d8c-4a5595215384" -->
### Local Server (Development)
```bash
claude mcp add context7 -- npx -y @upstash/context7-mcp --api-key YOUR_CONTEXT7_API_KEY
```

<!-- section_id: "9d57e0e6-4efb-47a4-be72-863aa190495b" -->
## 🔧 MCP Management System

<!-- section_id: "5dad6495-da2f-41db-8ca5-df6c0d4e176f" -->
### Quick Setup
```bash
# Local server
python3 scripts/context7-setup.py setup-local

# Remote server
python3 scripts/context7-setup.py setup-remote

# Both options
python3 scripts/context7-setup.py setup-hybrid
```

<!-- section_id: "8e19edbd-65e6-4f19-8724-0bf2e7d8828b" -->
### Status & Testing
```bash
# Check status
python3 scripts/context7-setup.py status

# Test local package
npx -y @upstash/context7-mcp --help

# Test remote endpoint
curl -I https://mcp.context7.com/mcp
```

<!-- section_id: "35f4c882-fe2a-46e4-bf25-72ddc579745c" -->
## 📁 Configuration Files

| File | Purpose |
|------|---------|
| `.mcp.json` | Current active configuration |
| `config/mcp/examples/context7-local.json` | Local server example |
| `config/mcp/examples/context7-remote.json` | Remote server example |
| `config/mcp/examples/context7-hybrid.json` | Both options example |

<!-- section_id: "8a22dc6f-430e-466b-aaa5-65095cb55df2" -->
## 🔄 Switch Configurations

```bash
# Switch to local
python3 scripts/context7-setup.py setup-local

# Switch to remote
python3 scripts/context7-setup.py setup-remote

# Switch to hybrid
python3 scripts/context7-setup.py setup-hybrid
```

<!-- section_id: "9b9a2df0-31d2-4411-beb7-dc9dcd93376a" -->
## 🛠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| "Command not found: claude" | Install Claude Code CLI |
| "Package not found" | `npm install -g @upstash/context7-mcp` |
| "Connection refused" | Check internet, verify API key |
| "Invalid API key" | Verify: `YOUR_CONTEXT7_API_KEY` |

<!-- section_id: "c910a03a-1f08-4b54-85a0-4369f7167f1b" -->
## 📊 Check Status

```bash
# Context7 status
python3 scripts/context7-setup.py status

# Overall MCP status
python3 scripts/mcp-cli.py status

# System health
python3 scripts/mcp-cli.py health
```

<!-- section_id: "539daaa7-3e13-4bd4-a9b3-dbce813e2236" -->
## 🎯 Recommendations

- **Development**: Use local server for better performance
- **Production**: Use remote server for simplicity
- **Flexibility**: Use hybrid setup for both options

<!-- section_id: "cbf4b51a-8114-4840-b607-ac36ce9e79f9" -->
## 📚 Full Documentation

- **Complete Setup Guide**: `docs/CONTEXT7_CLAUDE_SETUP.md`
- **MCP System Guide**: `docs/MCP_SYSTEM_GUIDE.md`
- **Configuration Examples**: `config/mcp/examples/`

---
**Ready to use!** Your Context7 MCP server is configured and ready for Claude Code integration. 🎉
