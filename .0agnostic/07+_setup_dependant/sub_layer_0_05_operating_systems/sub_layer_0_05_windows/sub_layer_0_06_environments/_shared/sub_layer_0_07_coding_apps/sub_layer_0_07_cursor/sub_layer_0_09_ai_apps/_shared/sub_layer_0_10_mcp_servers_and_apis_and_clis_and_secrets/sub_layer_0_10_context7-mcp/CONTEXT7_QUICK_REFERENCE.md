---
resource_id: "960e8ccf-ad62-41f3-b001-a3931d3ed4df"
resource_type: "document"
resource_name: "CONTEXT7_QUICK_REFERENCE"
---
# Context7 MCP Server - Quick Reference

## 🔑 Your API Key
```
YOUR_CONTEXT7_API_KEY
```

## 🚀 Claude Code Setup (Choose One)

### Remote Server (Production)
```bash
claude mcp add --transport http context7 https://mcp.context7.com/mcp --header "CONTEXT7_API_KEY: YOUR_CONTEXT7_API_KEY"
```

### Local Server (Development)
```bash
claude mcp add context7 -- npx -y @upstash/context7-mcp --api-key YOUR_CONTEXT7_API_KEY
```

## 🔧 MCP Management System

### Quick Setup
```bash
# Local server
python3 scripts/context7-setup.py setup-local

# Remote server
python3 scripts/context7-setup.py setup-remote

# Both options
python3 scripts/context7-setup.py setup-hybrid
```

### Status & Testing
```bash
# Check status
python3 scripts/context7-setup.py status

# Test local package
npx -y @upstash/context7-mcp --help

# Test remote endpoint
curl -I https://mcp.context7.com/mcp
```

## 📁 Configuration Files

| File | Purpose |
|------|---------|
| `.mcp.json` | Current active configuration |
| `config/mcp/examples/context7-local.json` | Local server example |
| `config/mcp/examples/context7-remote.json` | Remote server example |
| `config/mcp/examples/context7-hybrid.json` | Both options example |

## 🔄 Switch Configurations

```bash
# Switch to local
python3 scripts/context7-setup.py setup-local

# Switch to remote
python3 scripts/context7-setup.py setup-remote

# Switch to hybrid
python3 scripts/context7-setup.py setup-hybrid
```

## 🛠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| "Command not found: claude" | Install Claude Code CLI |
| "Package not found" | `npm install -g @upstash/context7-mcp` |
| "Connection refused" | Check internet, verify API key |
| "Invalid API key" | Verify: `YOUR_CONTEXT7_API_KEY` |

## 📊 Check Status

```bash
# Context7 status
python3 scripts/context7-setup.py status

# Overall MCP status
python3 scripts/mcp-cli.py status

# System health
python3 scripts/mcp-cli.py health
```

## 🎯 Recommendations

- **Development**: Use local server for better performance
- **Production**: Use remote server for simplicity
- **Flexibility**: Use hybrid setup for both options

## 📚 Full Documentation

- **Complete Setup Guide**: `docs/CONTEXT7_CLAUDE_SETUP.md`
- **MCP System Guide**: `docs/MCP_SYSTEM_GUIDE.md`
- **Configuration Examples**: `config/mcp/examples/`

---
**Ready to use!** Your Context7 MCP server is configured and ready for Claude Code integration. 🎉
