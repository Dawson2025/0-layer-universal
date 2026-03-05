---
resource_id: "0636fce4-8993-4617-8d70-6d37e2e444f8"
resource_type: "document"
resource_name: "CONTEXT7_CLAUDE_SETUP"
---
# Context7 MCP Server - Claude Code Integration Guide

<!-- section_id: "aff560b2-66b9-4b76-b490-b3586716a09f" -->
## Overview

This guide shows you how to set up Context7 MCP server for use with Claude Code, including both local and remote connection options.

<!-- section_id: "7515005b-a9b6-4877-b4f6-b62d6996700c" -->
## 🔑 Your API Credentials

- **API Key**: `YOUR_CONTEXT7_API_KEY`
- **API URL**: `https://context7.com/api/v1`
- **MCP URL**: `https://mcp.context7.com/mcp`

<!-- section_id: "547490f1-8feb-444e-b713-738b92cf6d69" -->
## 🚀 Quick Setup Options

<!-- section_id: "5b06e3a7-6094-4d7c-a15e-2461ff8d8099" -->
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

<!-- section_id: "27247f3a-d8d4-4bc9-8419-abd6789af547" -->
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

<!-- section_id: "e7f8e02e-73b0-45b7-848c-e05efac2dd1c" -->
## 🔧 Advanced Setup with MCP Management System

If you're using the centralized MCP management system in this project:

<!-- section_id: "1c1f938c-bdee-4b64-9b63-a1c6e195f838" -->
### 1. Set up Context7 in the Management System

```bash
# For local server
python3 scripts/context7-setup.py setup-local

# For remote server
python3 scripts/context7-setup.py setup-remote

# For both options (hybrid)
python3 scripts/context7-setup.py setup-hybrid
```

<!-- section_id: "ee416d1d-745d-45f0-a8c2-057663ef504c" -->
### 2. Check Status

```bash
python3 scripts/context7-setup.py status
```

<!-- section_id: "9c1f6160-3003-4e2e-ab42-7e63ea1c24bd" -->
### 3. Deploy Configuration

```bash
# Deploy development environment
python3 scripts/mcp-cli.py deploy development

# Check overall MCP status
python3 scripts/mcp-cli.py status
```

<!-- section_id: "bf80c613-46cc-4ee3-8b8d-847114ef03ad" -->
## 📁 Configuration Files

The MCP management system creates several configuration files:

<!-- section_id: "f3ec7e81-4775-4a39-a742-64ea69249b5a" -->
### Current Active Configuration
- **File**: `.mcp.json`
- **Contains**: Currently active MCP server configuration

<!-- section_id: "058ba37f-5e78-4eb5-9e91-1e8328a2f017" -->
### Example Configurations
- **Local**: `config/mcp/examples/context7-local.json`
- **Remote**: `config/mcp/examples/context7-remote.json`
- **Hybrid**: `config/mcp/examples/context7-hybrid.json`

<!-- section_id: "ab97a993-3fe5-4f5c-94ec-450dbe8aa254" -->
### Environment-Specific Configurations
- **Development**: `config/mcp/development.json`
- **Production**: `config/mcp/production.json`
- **Testing**: `config/mcp/testing.json`

<!-- section_id: "71097525-6313-49a0-8b71-85a8f3a3ed5b" -->
## 🧪 Testing Your Setup

<!-- section_id: "94b7b5a1-0a2f-445a-8d2c-163fa2d768a8" -->
### Test Local Setup
```bash
# Test if the local package is accessible
npx -y @upstash/context7-mcp --help
```

<!-- section_id: "0abf4ddf-bef5-4e03-bf1b-f4b700304d2f" -->
### Test Remote Setup
```bash
# Test if the remote endpoint is accessible
curl -I https://mcp.context7.com/mcp
```

<!-- section_id: "385b8259-e874-451b-bec0-31a04119f850" -->
### Test in Claude Code
1. Open Claude Code
2. Check if Context7 appears in the MCP servers list
3. Try using Context7 tools in your conversations

<!-- section_id: "579b1aa4-394b-4cf5-9d49-7dffb7e3db9d" -->
## 🔄 Switching Between Configurations

<!-- section_id: "50311e45-3d74-48ae-9cbf-397c22bb8a29" -->
### Switch to Local Server
```bash
# Using MCP management system
python3 scripts/context7-setup.py setup-local

# Or manually update .mcp.json
cp config/mcp/examples/context7-local.json .mcp.json
```

<!-- section_id: "1349adbd-e9c1-4201-beac-06c39518fe05" -->
### Switch to Remote Server
```bash
# Using MCP management system
python3 scripts/context7-setup.py setup-remote

# Or manually update .mcp.json
cp config/mcp/examples/context7-remote.json .mcp.json
```

<!-- section_id: "7630c219-0cd1-4891-a573-88d83dd5140f" -->
### Switch to Hybrid (Both Options)
```bash
# Using MCP management system
python3 scripts/context7-setup.py setup-hybrid

# Or manually update .mcp.json
cp config/mcp/examples/context7-hybrid.json .mcp.json
```

<!-- section_id: "99f4a455-971f-442c-b0ac-12fd34c3bbc0" -->
## 🛠️ Troubleshooting

<!-- section_id: "a2e609f1-5126-4c3f-b2f7-11653c08d625" -->
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

<!-- section_id: "f52d8f58-b268-49df-a8db-48df752c6a1c" -->
### Debug Commands

```bash
# Check MCP management system status
python3 scripts/context7-setup.py status

# Check overall MCP system health
python3 scripts/mcp-cli.py health

# Validate configuration
python3 scripts/mcp-cli.py validate development
```

<!-- section_id: "85cf5036-ee58-4737-9181-a05b21c7e0c8" -->
## 📊 Monitoring and Management

<!-- section_id: "1b183e81-73e8-42f7-8a3b-48a4c0ed6f7a" -->
### Check Server Status
```bash
# Context7 specific status
python3 scripts/context7-setup.py status

# Overall MCP system status
python3 scripts/mcp-cli.py status
```

<!-- section_id: "6c3a5932-1ae2-407e-9a72-112070aa65d8" -->
### View Logs
```bash
# Check MCP logs
tail -f backups/mcp/mcp.log

# Check system logs
journalctl -u claude-code
```

<!-- section_id: "e9f175e8-7fac-477e-82fd-f188e5c6a00c" -->
## 🎯 Best Practices

<!-- section_id: "02c34691-8118-4fca-92d9-ef8dea98bc7d" -->
### Development
- Use **local server** for better performance and debugging
- Keep the MCP management system updated
- Test both configurations regularly

<!-- section_id: "97d32c2d-1099-4fc8-847c-24e1ed63c1ef" -->
### Production
- Use **remote server** for simplicity and reliability
- Monitor server status regularly
- Have backup configurations ready

<!-- section_id: "ab1bc3b9-614a-4f78-8450-6dd79762cdbc" -->
### Hybrid Approach
- Use **hybrid setup** for maximum flexibility
- Switch between local and remote as needed
- Keep both configurations tested and ready

<!-- section_id: "75b96264-4e9c-4bed-8809-1c5e0813e887" -->
## 📚 Additional Resources

- **MCP System Guide**: `docs/MCP_SYSTEM_GUIDE.md`
- **Configuration Examples**: `config/mcp/examples/`
- **Management Scripts**: `scripts/context7-setup.py`
- **Context7 Documentation**: [Context7 Docs](https://context7.com/docs)

<!-- section_id: "955e74d6-79c1-4ce5-9d94-a1e212fb22a0" -->
## 🆘 Support

If you encounter issues:

1. **Check Status**: `python3 scripts/context7-setup.py status`
2. **Review Logs**: Check `backups/mcp/mcp.log`
3. **Validate Config**: `python3 scripts/mcp-cli.py validate development`
4. **Test Connectivity**: Use the debug commands above

<!-- section_id: "aec67de5-9981-4983-bfbb-0100487a2d9a" -->
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
