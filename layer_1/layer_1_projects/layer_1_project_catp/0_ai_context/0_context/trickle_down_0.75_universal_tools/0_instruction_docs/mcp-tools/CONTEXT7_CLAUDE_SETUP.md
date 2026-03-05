---
resource_id: "1a940ad9-ce24-4a30-b673-659bd2283eb6"
resource_type: "document"
resource_name: "CONTEXT7_CLAUDE_SETUP"
---
# Context7 MCP Server - Claude Code Integration Guide

<!-- section_id: "a8ca2421-7bbd-449d-abe7-1402ed1bd2fe" -->
## Overview

This guide shows you how to set up Context7 MCP server for use with Claude Code, including both local and remote connection options.

<!-- section_id: "135e09f0-5904-442c-a044-a3a2459d9a76" -->
## 🔑 Your API Credentials

- **API Key**: `ctx7sk-d20b6dec-5980-4ee1-9beb-0e635d626f46`
- **API URL**: `https://context7.com/api/v1`
- **MCP URL**: `https://mcp.context7.com/mcp`

<!-- section_id: "d0488ad1-7672-4af3-aeab-b097e7501cef" -->
## 🚀 Quick Setup Options

<!-- section_id: "18282c9c-1af7-4e26-bf72-f4d1343923df" -->
### Option 1: Remote Server (Recommended for Production)

Connect directly to Context7's hosted MCP server:

```bash
claude mcp add --transport http context7 https://mcp.context7.com/mcp --header "CONTEXT7_API_KEY: ctx7sk-d20b6dec-5980-4ee1-9beb-0e635d626f46"
```

**Pros:**
- No local installation required
- Always up-to-date
- No local resource usage
- Simple setup

**Cons:**
- Requires internet connection
- Dependent on Context7 server availability
- Potential latency

<!-- section_id: "ad92139f-3af5-428c-87ab-8156f969d314" -->
### Option 2: Local Server (Recommended for Development)

Run Context7 MCP server locally:

```bash
claude mcp add context7 -- npx -y @upstash/context7-mcp --api-key ctx7sk-d20b6dec-5980-4ee1-9beb-0e635d626f46
```

**Pros:**
- Better performance
- Full control over the server
- No external dependencies
- Better for debugging

**Cons:**
- Requires Node.js and npm
- Uses local resources
- Need to manage server process

<!-- section_id: "956f48ae-9f34-4007-9c92-e86c2b6733bd" -->
## 🔧 Advanced Setup with MCP Management System

If you're using the centralized MCP management system in this project:

<!-- section_id: "8d0f7a1a-fc2d-4598-928f-b1ba95ec52c4" -->
### 1. Set up Context7 in the Management System

```bash
# For local server
python3 scripts/context7-setup.py setup-local

# For remote server
python3 scripts/context7-setup.py setup-remote

# For both options (hybrid)
python3 scripts/context7-setup.py setup-hybrid
```

<!-- section_id: "bf3675c4-03af-43f7-b666-e20ded88a004" -->
### 2. Check Status

```bash
python3 scripts/context7-setup.py status
```

<!-- section_id: "c9228354-7c1f-4077-9409-2f8831f54dcb" -->
### 3. Deploy Configuration

```bash
# Deploy development environment
python3 scripts/mcp-cli.py deploy development

# Check overall MCP status
python3 scripts/mcp-cli.py status
```

<!-- section_id: "277df247-6a23-4b64-b662-bdf1190e4638" -->
## 📁 Configuration Files

The MCP management system creates several configuration files:

<!-- section_id: "d809c557-1f6e-4129-b6a5-c5eac2aaaff6" -->
### Current Active Configuration
- **File**: `.mcp.json`
- **Contains**: Currently active MCP server configuration

<!-- section_id: "4013ba8a-3507-4a8b-847f-e48ad6985cdf" -->
### Example Configurations
- **Local**: `config/mcp/examples/context7-local.json`
- **Remote**: `config/mcp/examples/context7-remote.json`
- **Hybrid**: `config/mcp/examples/context7-hybrid.json`

<!-- section_id: "72f5dcc6-7eae-417a-a947-e0bc32c1626d" -->
### Environment-Specific Configurations
- **Development**: `config/mcp/development.json`
- **Production**: `config/mcp/production.json`
- **Testing**: `config/mcp/testing.json`

<!-- section_id: "bc335897-26fe-41ef-a8f8-d1de6ef6e707" -->
## 🧪 Testing Your Setup

<!-- section_id: "c457969d-4dcb-4b07-b8cf-b12e99cc7e21" -->
### Test Local Setup
```bash
# Test if the local package is accessible
npx -y @upstash/context7-mcp --help
```

<!-- section_id: "d81fe69b-2975-49c9-90af-3e6ab9514145" -->
### Test Remote Setup
```bash
# Test if the remote endpoint is accessible
curl -I https://mcp.context7.com/mcp
```

<!-- section_id: "c5f2a016-8b8a-4896-a628-8c812a20519b" -->
### Test in Claude Code
1. Open Claude Code
2. Check if Context7 appears in the MCP servers list
3. Try using Context7 tools in your conversations

<!-- section_id: "16b2d984-1aca-4258-8624-221d1de759c0" -->
## 🔄 Switching Between Configurations

<!-- section_id: "6a849601-8d75-48e8-87f7-c1af94d289d2" -->
### Switch to Local Server
```bash
# Using MCP management system
python3 scripts/context7-setup.py setup-local

# Or manually update .mcp.json
cp config/mcp/examples/context7-local.json .mcp.json
```

<!-- section_id: "682367e9-6889-4e85-8a65-af7ea4dba118" -->
### Switch to Remote Server
```bash
# Using MCP management system
python3 scripts/context7-setup.py setup-remote

# Or manually update .mcp.json
cp config/mcp/examples/context7-remote.json .mcp.json
```

<!-- section_id: "c911789f-877f-459a-a9ae-f5e3d6433e0a" -->
### Switch to Hybrid (Both Options)
```bash
# Using MCP management system
python3 scripts/context7-setup.py setup-hybrid

# Or manually update .mcp.json
cp config/mcp/examples/context7-hybrid.json .mcp.json
```

<!-- section_id: "fcd53c9b-d19b-4e4e-bd5b-65245b6cc94f" -->
## 🛠️ Troubleshooting

<!-- section_id: "f7d245da-052b-4d19-bea1-01a8b11599a7" -->
### Common Issues

1. **"Command not found: claude"**
   - Install Claude Code CLI
   - Ensure it's in your PATH

2. **"Package not found" (Local setup)**
   - Ensure Node.js and npm are installed
   - Try: `npm install -g @upstash/context7-mcp`

3. **"Connection refused" (Remote setup)**
   - Check internet connection
   - Verify API key is correct
   - Check if Context7 servers are operational

4. **"Invalid API key"**
   - Verify your API key: `ctx7sk-d20b6dec-5980-4ee1-9beb-0e635d626f46`
   - Check for typos in the configuration

<!-- section_id: "84dbcbb1-70be-40fd-a754-9130997eb929" -->
### Debug Commands

```bash
# Check MCP management system status
python3 scripts/context7-setup.py status

# Check overall MCP system health
python3 scripts/mcp-cli.py health

# Validate configuration
python3 scripts/mcp-cli.py validate development
```

<!-- section_id: "ce14f620-d2d5-4b2f-a6e1-a1b79454c426" -->
## 📊 Monitoring and Management

<!-- section_id: "854f24b0-3139-4aeb-86fc-0eb5b94ddcb1" -->
### Check Server Status
```bash
# Context7 specific status
python3 scripts/context7-setup.py status

# Overall MCP system status
python3 scripts/mcp-cli.py status
```

<!-- section_id: "88909058-60c2-4cd7-abd3-47f084ab25e9" -->
### View Logs
```bash
# Check MCP logs
tail -f backups/mcp/mcp.log

# Check system logs
journalctl -u claude-code
```

<!-- section_id: "4fa2cada-ea0a-4e5c-908d-8b2e95888886" -->
## 🎯 Best Practices

<!-- section_id: "7553bc80-5425-4f26-8d12-9b26271f003f" -->
### Development
- Use **local server** for better performance and debugging
- Keep the MCP management system updated
- Test both configurations regularly

<!-- section_id: "ebe53e58-6be6-4ed1-aa68-811f7439897b" -->
### Production
- Use **remote server** for simplicity and reliability
- Monitor server status regularly
- Have backup configurations ready

<!-- section_id: "a68a5ac2-1431-4a0a-b33f-259a0679133c" -->
### Hybrid Approach
- Use **hybrid setup** for maximum flexibility
- Switch between local and remote as needed
- Keep both configurations tested and ready

<!-- section_id: "f6c4cd46-ad7a-4191-8e02-e66310b9d4f6" -->
## 📚 Additional Resources

- **MCP System Guide**: `docs/MCP_SYSTEM_GUIDE.md`
- **Configuration Examples**: `config/mcp/examples/`
- **Management Scripts**: `scripts/context7-setup.py`
- **Context7 Documentation**: [Context7 Docs](https://context7.com/docs)

<!-- section_id: "5f3bc90e-7a58-44c1-8e28-ad36b8c9388a" -->
## 🆘 Support

If you encounter issues:

1. **Check Status**: `python3 scripts/context7-setup.py status`
2. **Review Logs**: Check `backups/mcp/mcp.log`
3. **Validate Config**: `python3 scripts/mcp-cli.py validate development`
4. **Test Connectivity**: Use the debug commands above

<!-- section_id: "94db86ef-704c-45fe-a6c2-b90c2a73b538" -->
## ✅ Quick Reference

| Task | Command |
|------|---------|
| Setup Local | `claude mcp add context7 -- npx -y @upstash/context7-mcp --api-key ctx7sk-d20b6dec-5980-4ee1-9beb-0e635d626f46` |
| Setup Remote | `claude mcp add --transport http context7 https://mcp.context7.com/mcp --header "CONTEXT7_API_KEY: ctx7sk-d20b6dec-5980-4ee1-9beb-0e635d626f46"` |
| Check Status | `python3 scripts/context7-setup.py status` |
| Switch Local | `python3 scripts/context7-setup.py setup-local` |
| Switch Remote | `python3 scripts/context7-setup.py setup-remote` |
| Switch Hybrid | `python3 scripts/context7-setup.py setup-hybrid` |

Your Context7 MCP server is now ready to use with Claude Code! 🎉
