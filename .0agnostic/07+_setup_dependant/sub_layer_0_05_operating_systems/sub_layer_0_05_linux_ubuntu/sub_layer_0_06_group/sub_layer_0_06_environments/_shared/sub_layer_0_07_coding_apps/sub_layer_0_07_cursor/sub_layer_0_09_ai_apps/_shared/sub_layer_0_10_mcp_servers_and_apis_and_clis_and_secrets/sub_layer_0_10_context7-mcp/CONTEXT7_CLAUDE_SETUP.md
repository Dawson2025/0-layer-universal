---
resource_id: "9b279a69-fbf7-427f-98c8-04758bbe174c"
resource_type: "document"
resource_name: "CONTEXT7_CLAUDE_SETUP"
---
# Context7 MCP Server - Claude Code Integration Guide

<!-- section_id: "3a88adcd-84ce-4326-8ca4-6e7c2e011497" -->
## Overview

This guide shows you how to set up Context7 MCP server for use with Claude Code, including both local and remote connection options.

<!-- section_id: "099c62c1-56d4-4d24-90c9-380e009cdb4b" -->
## 🔑 Your API Credentials

- **API Key**: `YOUR_CONTEXT7_API_KEY`
- **API URL**: `https://context7.com/api/v1`
- **MCP URL**: `https://mcp.context7.com/mcp`

<!-- section_id: "4941fad0-0228-4bd3-82fb-b33a4ea28a27" -->
## 🚀 Quick Setup Options

<!-- section_id: "8a98c859-4363-4974-876a-d56bac4d05e5" -->
### Option 1: Remote Server (Recommended for Production)

Connect directly to Context7's hosted MCP server:

```bash
claude mcp add --transport http context7 https://mcp.context7.com/mcp --header "CONTEXT7_API_KEY: YOUR_CONTEXT7_API_KEY"
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

<!-- section_id: "881a5a37-b859-41df-b60f-232122adefd4" -->
### Option 2: Local Server (Recommended for Development)

Run Context7 MCP server locally:

```bash
claude mcp add context7 -- npx -y @upstash/context7-mcp --api-key YOUR_CONTEXT7_API_KEY
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

<!-- section_id: "9360b84e-7563-4d43-9256-412015d9f744" -->
## 🔧 Advanced Setup with MCP Management System

If you're using the centralized MCP management system in this project:

<!-- section_id: "e5fe9cc1-827c-4b7a-9570-b3587e10d06e" -->
### 1. Set up Context7 in the Management System

```bash
# For local server
python3 scripts/context7-setup.py setup-local

# For remote server
python3 scripts/context7-setup.py setup-remote

# For both options (hybrid)
python3 scripts/context7-setup.py setup-hybrid
```

<!-- section_id: "d0bc26ee-e2cf-4757-a986-7b40561044ff" -->
### 2. Check Status

```bash
python3 scripts/context7-setup.py status
```

<!-- section_id: "d6226fe8-5194-43fd-8c31-fe363d54afae" -->
### 3. Deploy Configuration

```bash
# Deploy development environment
python3 scripts/mcp-cli.py deploy development

# Check overall MCP status
python3 scripts/mcp-cli.py status
```

<!-- section_id: "b7aa15c1-0eac-43bf-863a-7021ef75f560" -->
## 📁 Configuration Files

The MCP management system creates several configuration files:

<!-- section_id: "1bd0c1d2-6724-4c59-a0b1-bf7ac3f31263" -->
### Current Active Configuration
- **File**: `.mcp.json`
- **Contains**: Currently active MCP server configuration

<!-- section_id: "958e79bc-33db-45fe-8e0d-a6913b086794" -->
### Example Configurations
- **Local**: `config/mcp/examples/context7-local.json`
- **Remote**: `config/mcp/examples/context7-remote.json`
- **Hybrid**: `config/mcp/examples/context7-hybrid.json`

<!-- section_id: "79661bec-ff5a-4251-b36a-d3f7ab5d976d" -->
### Environment-Specific Configurations
- **Development**: `config/mcp/development.json`
- **Production**: `config/mcp/production.json`
- **Testing**: `config/mcp/testing.json`

<!-- section_id: "2901afc9-44fa-48c7-a13b-d37705cd4514" -->
## 🧪 Testing Your Setup

<!-- section_id: "51453097-56ae-4973-b2af-4dad7c8aa88c" -->
### Test Local Setup
```bash
# Test if the local package is accessible
npx -y @upstash/context7-mcp --help
```

<!-- section_id: "0e05d24e-cba1-486c-a4a1-49dfba85c30e" -->
### Test Remote Setup
```bash
# Test if the remote endpoint is accessible
curl -I https://mcp.context7.com/mcp
```

<!-- section_id: "50836a9f-cc22-4dd4-b109-9fe088ad3c76" -->
### Test in Claude Code
1. Open Claude Code
2. Check if Context7 appears in the MCP servers list
3. Try using Context7 tools in your conversations

<!-- section_id: "cd42f441-72c8-41ed-ba25-d261d1453b28" -->
## 🔄 Switching Between Configurations

<!-- section_id: "e5a85e18-efdd-43ae-8e09-4c30581923f2" -->
### Switch to Local Server
```bash
# Using MCP management system
python3 scripts/context7-setup.py setup-local

# Or manually update .mcp.json
cp config/mcp/examples/context7-local.json .mcp.json
```

<!-- section_id: "064fdd8f-6ce1-4375-b00c-fdda8255b380" -->
### Switch to Remote Server
```bash
# Using MCP management system
python3 scripts/context7-setup.py setup-remote

# Or manually update .mcp.json
cp config/mcp/examples/context7-remote.json .mcp.json
```

<!-- section_id: "18179af5-b58d-4ca9-89a4-1a6e3966cf93" -->
### Switch to Hybrid (Both Options)
```bash
# Using MCP management system
python3 scripts/context7-setup.py setup-hybrid

# Or manually update .mcp.json
cp config/mcp/examples/context7-hybrid.json .mcp.json
```

<!-- section_id: "cbd68127-4148-456c-b42f-32cd6e51381c" -->
## 🛠️ Troubleshooting

<!-- section_id: "5a56ef7f-00a6-429e-bbe1-a3217b11bdc7" -->
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
   - Verify your API key: `YOUR_CONTEXT7_API_KEY`
   - Check for typos in the configuration

<!-- section_id: "cc354427-daef-47dc-aa7a-bfec8c308a71" -->
### Debug Commands

```bash
# Check MCP management system status
python3 scripts/context7-setup.py status

# Check overall MCP system health
python3 scripts/mcp-cli.py health

# Validate configuration
python3 scripts/mcp-cli.py validate development
```

<!-- section_id: "1fc6fa05-a6bf-400b-9631-a9e32dce51ac" -->
## 📊 Monitoring and Management

<!-- section_id: "0484dc12-329b-4f4c-91d2-582b64ba1eb6" -->
### Check Server Status
```bash
# Context7 specific status
python3 scripts/context7-setup.py status

# Overall MCP system status
python3 scripts/mcp-cli.py status
```

<!-- section_id: "1aceaedd-29ff-494f-9c7a-a8f6b3d70177" -->
### View Logs
```bash
# Check MCP logs
tail -f backups/mcp/mcp.log

# Check system logs
journalctl -u claude-code
```

<!-- section_id: "ebbe9a9f-174e-4160-b71f-cd968922569d" -->
## 🎯 Best Practices

<!-- section_id: "e8b48d65-c0ff-4484-9ae4-26fe7166a281" -->
### Development
- Use **local server** for better performance and debugging
- Keep the MCP management system updated
- Test both configurations regularly

<!-- section_id: "c24dc7f6-f6a1-4adb-b79e-8685541b1f56" -->
### Production
- Use **remote server** for simplicity and reliability
- Monitor server status regularly
- Have backup configurations ready

<!-- section_id: "62604b84-8ebe-4eb9-a421-003568ee7921" -->
### Hybrid Approach
- Use **hybrid setup** for maximum flexibility
- Switch between local and remote as needed
- Keep both configurations tested and ready

<!-- section_id: "6d6d0989-334c-4ee3-b6f4-a6d649e1c10b" -->
## 📚 Additional Resources

- **MCP System Guide**: `docs/MCP_SYSTEM_GUIDE.md`
- **Configuration Examples**: `config/mcp/examples/`
- **Management Scripts**: `scripts/context7-setup.py`
- **Context7 Documentation**: [Context7 Docs](https://context7.com/docs)

<!-- section_id: "6c4e7066-e816-422a-b490-9276ad9b9c02" -->
## 🆘 Support

If you encounter issues:

1. **Check Status**: `python3 scripts/context7-setup.py status`
2. **Review Logs**: Check `backups/mcp/mcp.log`
3. **Validate Config**: `python3 scripts/mcp-cli.py validate development`
4. **Test Connectivity**: Use the debug commands above

<!-- section_id: "61092a4b-5641-4161-b6ac-f639698ba65f" -->
## ✅ Quick Reference

| Task | Command |
|------|---------|
| Setup Local | `claude mcp add context7 -- npx -y @upstash/context7-mcp --api-key YOUR_CONTEXT7_API_KEY` |
| Setup Remote | `claude mcp add --transport http context7 https://mcp.context7.com/mcp --header "CONTEXT7_API_KEY: YOUR_CONTEXT7_API_KEY"` |
| Check Status | `python3 scripts/context7-setup.py status` |
| Switch Local | `python3 scripts/context7-setup.py setup-local` |
| Switch Remote | `python3 scripts/context7-setup.py setup-remote` |
| Switch Hybrid | `python3 scripts/context7-setup.py setup-hybrid` |

Your Context7 MCP server is now ready to use with Claude Code! 🎉
