---
resource_id: "c4296aa4-baaa-4d9b-8e2c-1b6c634dbdf8"
resource_type: "document"
resource_name: "CONTEXT7_QUICK_REFERENCE"
---
# Context7 MCP Server - Quick Reference

<!-- section_id: "1a3aca7b-248f-44f5-b63f-db424096ea41" -->
## 🔑 Your API Key
```
YOUR_CONTEXT7_API_KEY
```

<!-- section_id: "aa5c603c-bb82-4f1a-9cb3-36258dc6e3b6" -->
## 🚀 Claude Code Setup (Choose One)

<!-- section_id: "47d44cc3-3e26-4a7f-b8e0-304a941a9b8f" -->
### Remote Server (Production)
```bash
claude mcp add --transport http context7 https://mcp.context7.com/mcp --header "CONTEXT7_API_KEY: YOUR_CONTEXT7_API_KEY"
```

<!-- section_id: "7d6a7179-5d14-4c16-a9a1-ceff9e8c1d39" -->
### Local Server (Development)
```bash
claude mcp add context7 -- npx -y @upstash/context7-mcp --api-key YOUR_CONTEXT7_API_KEY
```

<!-- section_id: "ba17fe88-647e-4ce4-a6ac-50ea7d4b3aa7" -->
## 🔧 MCP Management System

<!-- section_id: "32ef504b-9362-4234-b805-0c8d762b352c" -->
### Quick Setup
```bash
# Local server
python3 scripts/context7-setup.py setup-local

# Remote server
python3 scripts/context7-setup.py setup-remote

# Both options
python3 scripts/context7-setup.py setup-hybrid
```

<!-- section_id: "4c27ed5b-4ce6-446f-ad50-f55b3c1cde92" -->
### Status & Testing
```bash
# Check status
python3 scripts/context7-setup.py status

# Test local package
npx -y @upstash/context7-mcp --help

# Test remote endpoint
curl -I https://mcp.context7.com/mcp
```

<!-- section_id: "deb35aa4-ed7c-449c-b702-4e70441f3d90" -->
## 📁 Configuration Files

| File | Purpose |
|------|---------|
| `.mcp.json` | Current active configuration |
| `config/mcp/examples/context7-local.json` | Local server example |
| `config/mcp/examples/context7-remote.json` | Remote server example |
| `config/mcp/examples/context7-hybrid.json` | Both options example |

<!-- section_id: "a564af5d-d705-450a-80ba-80b3e7a0dfa2" -->
## 🔄 Switch Configurations

```bash
# Switch to local
python3 scripts/context7-setup.py setup-local

# Switch to remote
python3 scripts/context7-setup.py setup-remote

# Switch to hybrid
python3 scripts/context7-setup.py setup-hybrid
```

<!-- section_id: "c55a4af0-1c4b-4c66-99b6-0acbc0a45d25" -->
## 🛠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| "Command not found: claude" | Install Claude Code CLI |
| "Package not found" | `npm install -g @upstash/context7-mcp` |
| "Connection refused" | Check internet, verify API key |
| "Invalid API key" | Verify: `YOUR_CONTEXT7_API_KEY` |

<!-- section_id: "e0ef206a-9bbc-4789-b7eb-189584254252" -->
## 📊 Check Status

```bash
# Context7 status
python3 scripts/context7-setup.py status

# Overall MCP status
python3 scripts/mcp-cli.py status

# System health
python3 scripts/mcp-cli.py health
```

<!-- section_id: "9e24c454-6412-43e0-b06b-3eeda5699a3b" -->
## 🎯 Recommendations

- **Development**: Use local server for better performance
- **Production**: Use remote server for simplicity
- **Flexibility**: Use hybrid setup for both options

<!-- section_id: "06e0c3d7-3e01-4c71-98f4-b786b5c6f4ff" -->
## 📚 Full Documentation

- **Complete Setup Guide**: `docs/CONTEXT7_CLAUDE_SETUP.md`
- **MCP System Guide**: `docs/MCP_SYSTEM_GUIDE.md`
- **Configuration Examples**: `config/mcp/examples/`

---
**Ready to use!** Your Context7 MCP server is configured and ready for Claude Code integration. 🎉
