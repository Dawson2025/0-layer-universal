---
resource_id: "fd771be4-0dd5-4ae7-9cf6-3788d646a453"
resource_type: "document"
resource_name: "CONTEXT7_CLAUDE_SETUP"
---
# Context7 MCP Server - Claude Code Integration Guide

<!-- section_id: "8f585301-91d5-4b18-a9ae-450a432ee10c" -->
## Overview

This guide shows you how to set up Context7 MCP server for use with Claude Code, including both local and remote connection options.

<!-- section_id: "d498cb2c-ea8e-4ed4-b12b-fcd122bfd09c" -->
## 🔑 Your API Credentials

- **API Key**: `ctx7sk-d20b6dec-5980-4ee1-9beb-0e635d626f46`
- **API URL**: `https://context7.com/api/v1`
- **MCP URL**: `https://mcp.context7.com/mcp`

<!-- section_id: "42b6f287-5747-4553-a76b-ff4184d4ebd5" -->
## 🚀 Quick Setup Options

<!-- section_id: "91a4d5bf-f808-44cd-bb3c-6a436939cdd4" -->
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

<!-- section_id: "e1fcfc14-8c67-4f20-bdb6-99369e7cb260" -->
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

<!-- section_id: "875782e1-0ce1-431c-ab5f-def58e4d133f" -->
## 🔧 Advanced Setup with MCP Management System

If you're using the centralized MCP management system in this project:

<!-- section_id: "0ba2d9a8-963b-4049-a3d8-e4741bb9a6f1" -->
### 1. Set up Context7 in the Management System

```bash
# For local server
python3 scripts/context7-setup.py setup-local

# For remote server
python3 scripts/context7-setup.py setup-remote

# For both options (hybrid)
python3 scripts/context7-setup.py setup-hybrid
```

<!-- section_id: "74cf34ec-dfa5-4df2-a88c-6ed7b9b2ec7c" -->
### 2. Check Status

```bash
python3 scripts/context7-setup.py status
```

<!-- section_id: "c499d8d6-d3da-4650-8f78-998eb9595508" -->
### 3. Deploy Configuration

```bash
# Deploy development environment
python3 scripts/mcp-cli.py deploy development

# Check overall MCP status
python3 scripts/mcp-cli.py status
```

<!-- section_id: "6c17f576-7f8d-4b75-bb4a-12ad0faef0cb" -->
## 📁 Configuration Files

The MCP management system creates several configuration files:

<!-- section_id: "92939b93-0fbc-456f-82ff-234691c34929" -->
### Current Active Configuration
- **File**: `.mcp.json`
- **Contains**: Currently active MCP server configuration

<!-- section_id: "a83bca60-e322-49ba-bcfd-0b0742bfb4b8" -->
### Example Configurations
- **Local**: `config/mcp/examples/context7-local.json`
- **Remote**: `config/mcp/examples/context7-remote.json`
- **Hybrid**: `config/mcp/examples/context7-hybrid.json`

<!-- section_id: "94575ad6-a2b7-4ed0-9817-5b08cd42e8a5" -->
### Environment-Specific Configurations
- **Development**: `config/mcp/development.json`
- **Production**: `config/mcp/production.json`
- **Testing**: `config/mcp/testing.json`

<!-- section_id: "99504c0e-7dc7-4766-b29f-30613802c999" -->
## 🧪 Testing Your Setup

<!-- section_id: "bc4adad5-e249-4ea2-9f89-50571f2caa59" -->
### Test Local Setup
```bash
# Test if the local package is accessible
npx -y @upstash/context7-mcp --help
```

<!-- section_id: "e50f623d-8e8a-4f10-8a93-39a22ee734f0" -->
### Test Remote Setup
```bash
# Test if the remote endpoint is accessible
curl -I https://mcp.context7.com/mcp
```

<!-- section_id: "763660c3-f51d-40e5-9f56-bb3fa11841e2" -->
### Test in Claude Code
1. Open Claude Code
2. Check if Context7 appears in the MCP servers list
3. Try using Context7 tools in your conversations

<!-- section_id: "75ccc364-af0d-4856-9fe5-1a29a3d5fb1e" -->
## 🔄 Switching Between Configurations

<!-- section_id: "6f6da79d-14a7-4055-aff8-aeed615fc258" -->
### Switch to Local Server
```bash
# Using MCP management system
python3 scripts/context7-setup.py setup-local

# Or manually update .mcp.json
cp config/mcp/examples/context7-local.json .mcp.json
```

<!-- section_id: "a5f0c470-3694-45bd-bd1a-4ea0478fc886" -->
### Switch to Remote Server
```bash
# Using MCP management system
python3 scripts/context7-setup.py setup-remote

# Or manually update .mcp.json
cp config/mcp/examples/context7-remote.json .mcp.json
```

<!-- section_id: "7917bcf9-47eb-4573-b43b-09944459c725" -->
### Switch to Hybrid (Both Options)
```bash
# Using MCP management system
python3 scripts/context7-setup.py setup-hybrid

# Or manually update .mcp.json
cp config/mcp/examples/context7-hybrid.json .mcp.json
```

<!-- section_id: "3cd1eb5b-1446-49a2-8289-420d7584015f" -->
## 🛠️ Troubleshooting

<!-- section_id: "a638b1e9-75e5-4eda-82a2-b6e6e7904c48" -->
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

<!-- section_id: "c91e24fc-9c67-4115-a7da-0d49a063ad99" -->
### Debug Commands

```bash
# Check MCP management system status
python3 scripts/context7-setup.py status

# Check overall MCP system health
python3 scripts/mcp-cli.py health

# Validate configuration
python3 scripts/mcp-cli.py validate development
```

<!-- section_id: "34ecffc7-0c35-4c08-8a6e-fae5518647fe" -->
## 📊 Monitoring and Management

<!-- section_id: "c0d0d6ad-fd78-45c2-afe7-82b6108bf2eb" -->
### Check Server Status
```bash
# Context7 specific status
python3 scripts/context7-setup.py status

# Overall MCP system status
python3 scripts/mcp-cli.py status
```

<!-- section_id: "d8379ba4-e025-406a-8b9b-93c775c0f813" -->
### View Logs
```bash
# Check MCP logs
tail -f backups/mcp/mcp.log

# Check system logs
journalctl -u claude-code
```

<!-- section_id: "1b0eb741-2c1c-4fb1-974f-b7b0142282a6" -->
## 🎯 Best Practices

<!-- section_id: "d3c56a11-d7ef-41a8-9887-35cf9c314064" -->
### Development
- Use **local server** for better performance and debugging
- Keep the MCP management system updated
- Test both configurations regularly

<!-- section_id: "0377f587-387e-4351-a602-1438dc1fa500" -->
### Production
- Use **remote server** for simplicity and reliability
- Monitor server status regularly
- Have backup configurations ready

<!-- section_id: "956b933b-a5cc-4498-b58c-44f289e4e9fc" -->
### Hybrid Approach
- Use **hybrid setup** for maximum flexibility
- Switch between local and remote as needed
- Keep both configurations tested and ready

<!-- section_id: "d08c00ea-aaf8-4579-919d-5393d40a20a1" -->
## 📚 Additional Resources

- **MCP System Guide**: `docs/MCP_SYSTEM_GUIDE.md`
- **Configuration Examples**: `config/mcp/examples/`
- **Management Scripts**: `scripts/context7-setup.py`
- **Context7 Documentation**: [Context7 Docs](https://context7.com/docs)

<!-- section_id: "d3208c33-2e1d-4021-b518-8b3cda528eca" -->
## 🆘 Support

If you encounter issues:

1. **Check Status**: `python3 scripts/context7-setup.py status`
2. **Review Logs**: Check `backups/mcp/mcp.log`
3. **Validate Config**: `python3 scripts/mcp-cli.py validate development`
4. **Test Connectivity**: Use the debug commands above

<!-- section_id: "1c8a3a42-bff5-49c1-88c8-b579e11dcc52" -->
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
