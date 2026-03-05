---
resource_id: "f842bf3e-b6b7-46e0-bb2a-6036ee753107"
resource_type: "document"
resource_name: "CONTEXT7_CLAUDE_SETUP"
---
# Context7 MCP Server - Claude Code Integration Guide

<!-- section_id: "3ca31c34-7c4a-4a98-b9f8-bda13eedbb90" -->
## Overview

This guide shows you how to set up Context7 MCP server for use with Claude Code, including both local and remote connection options.

<!-- section_id: "4cc0cce0-91cf-4967-a520-12330e2806fb" -->
## 🔑 Your API Credentials

- **API Key**: `YOUR_CONTEXT7_API_KEY`
- **API URL**: `https://context7.com/api/v1`
- **MCP URL**: `https://mcp.context7.com/mcp`

<!-- section_id: "cd11d939-b9bd-4056-ad8a-4be4a83c7f8f" -->
## 🚀 Quick Setup Options

<!-- section_id: "bfb83276-5d66-4949-8552-5b42f986319e" -->
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

<!-- section_id: "ad88b852-90e3-4c04-baa7-fd91155c3f31" -->
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

<!-- section_id: "3d229f45-5d1a-4bb4-b225-8ee70da5dbca" -->
## 🔧 Advanced Setup with MCP Management System

If you're using the centralized MCP management system in this project:

<!-- section_id: "41ad481f-7258-4390-a7db-c2068f0bcb9e" -->
### 1. Set up Context7 in the Management System

```bash
# For local server
python3 scripts/context7-setup.py setup-local

# For remote server
python3 scripts/context7-setup.py setup-remote

# For both options (hybrid)
python3 scripts/context7-setup.py setup-hybrid
```

<!-- section_id: "18f762d5-6872-449e-9070-b5e37e715a6a" -->
### 2. Check Status

```bash
python3 scripts/context7-setup.py status
```

<!-- section_id: "836406b6-15dc-44f1-bb00-3ee5786e5a3f" -->
### 3. Deploy Configuration

```bash
# Deploy development environment
python3 scripts/mcp-cli.py deploy development

# Check overall MCP status
python3 scripts/mcp-cli.py status
```

<!-- section_id: "d5dea35a-841f-4708-98db-5a28a0312d77" -->
## 📁 Configuration Files

The MCP management system creates several configuration files:

<!-- section_id: "c07fdeea-f4f3-4bab-a6be-baa3db7e6019" -->
### Current Active Configuration
- **File**: `.mcp.json`
- **Contains**: Currently active MCP server configuration

<!-- section_id: "99fd223d-f798-4569-a291-c2f67866c4ac" -->
### Example Configurations
- **Local**: `config/mcp/examples/context7-local.json`
- **Remote**: `config/mcp/examples/context7-remote.json`
- **Hybrid**: `config/mcp/examples/context7-hybrid.json`

<!-- section_id: "4f7547c5-0099-4bd7-a20a-0abc53bd7f44" -->
### Environment-Specific Configurations
- **Development**: `config/mcp/development.json`
- **Production**: `config/mcp/production.json`
- **Testing**: `config/mcp/testing.json`

<!-- section_id: "f2c88f58-1ed2-49d1-a823-9324e55b73c3" -->
## 🧪 Testing Your Setup

<!-- section_id: "84a9e252-721b-43cd-93ab-e3c2ecedcda6" -->
### Test Local Setup
```bash
# Test if the local package is accessible
npx -y @upstash/context7-mcp --help
```

<!-- section_id: "05fc922e-4355-46a4-813d-bebdb6d803f7" -->
### Test Remote Setup
```bash
# Test if the remote endpoint is accessible
curl -I https://mcp.context7.com/mcp
```

<!-- section_id: "3a3e8af5-093c-4ff8-b47c-959a4eb8a81a" -->
### Test in Claude Code
1. Open Claude Code
2. Check if Context7 appears in the MCP servers list
3. Try using Context7 tools in your conversations

<!-- section_id: "8f8d1540-bf04-4494-a073-28ff07f37136" -->
## 🔄 Switching Between Configurations

<!-- section_id: "cd754913-e046-4789-bff8-1d1c7061c7b5" -->
### Switch to Local Server
```bash
# Using MCP management system
python3 scripts/context7-setup.py setup-local

# Or manually update .mcp.json
cp config/mcp/examples/context7-local.json .mcp.json
```

<!-- section_id: "2c930894-c049-40d0-904b-930403864d01" -->
### Switch to Remote Server
```bash
# Using MCP management system
python3 scripts/context7-setup.py setup-remote

# Or manually update .mcp.json
cp config/mcp/examples/context7-remote.json .mcp.json
```

<!-- section_id: "3de97a19-5ac7-43c9-a434-0bc9e96db7e7" -->
### Switch to Hybrid (Both Options)
```bash
# Using MCP management system
python3 scripts/context7-setup.py setup-hybrid

# Or manually update .mcp.json
cp config/mcp/examples/context7-hybrid.json .mcp.json
```

<!-- section_id: "1fa70a62-7d96-4ceb-8ada-e94992d3c7e0" -->
## 🛠️ Troubleshooting

<!-- section_id: "a96e2ffa-ba05-48e0-bcd8-d35ed95c986c" -->
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

<!-- section_id: "70c6e616-9a3b-4cc1-8783-193bff426944" -->
### Debug Commands

```bash
# Check MCP management system status
python3 scripts/context7-setup.py status

# Check overall MCP system health
python3 scripts/mcp-cli.py health

# Validate configuration
python3 scripts/mcp-cli.py validate development
```

<!-- section_id: "68264618-8ac0-4ce0-9346-bea4eb697647" -->
## 📊 Monitoring and Management

<!-- section_id: "009f6d53-9add-49b2-9825-ce0875540ff0" -->
### Check Server Status
```bash
# Context7 specific status
python3 scripts/context7-setup.py status

# Overall MCP system status
python3 scripts/mcp-cli.py status
```

<!-- section_id: "7df96fd7-897a-4ca4-b732-b5e93bf450d6" -->
### View Logs
```bash
# Check MCP logs
tail -f backups/mcp/mcp.log

# Check system logs
journalctl -u claude-code
```

<!-- section_id: "e16bdd5b-dad8-4ca1-acd9-c24a6a7841a2" -->
## 🎯 Best Practices

<!-- section_id: "5b403fcd-3e9b-490e-a7a7-a724214e9fa0" -->
### Development
- Use **local server** for better performance and debugging
- Keep the MCP management system updated
- Test both configurations regularly

<!-- section_id: "b544f731-ed08-49b5-a6ce-1d18580299be" -->
### Production
- Use **remote server** for simplicity and reliability
- Monitor server status regularly
- Have backup configurations ready

<!-- section_id: "8ad23a5c-2bff-42b8-8a8c-ff84aad12c29" -->
### Hybrid Approach
- Use **hybrid setup** for maximum flexibility
- Switch between local and remote as needed
- Keep both configurations tested and ready

<!-- section_id: "430dcc72-5982-4e96-bf41-880def888f84" -->
## 📚 Additional Resources

- **MCP System Guide**: `docs/MCP_SYSTEM_GUIDE.md`
- **Configuration Examples**: `config/mcp/examples/`
- **Management Scripts**: `scripts/context7-setup.py`
- **Context7 Documentation**: [Context7 Docs](https://context7.com/docs)

<!-- section_id: "97725bde-39b5-4afc-ae3a-675c2cac3508" -->
## 🆘 Support

If you encounter issues:

1. **Check Status**: `python3 scripts/context7-setup.py status`
2. **Review Logs**: Check `backups/mcp/mcp.log`
3. **Validate Config**: `python3 scripts/mcp-cli.py validate development`
4. **Test Connectivity**: Use the debug commands above

<!-- section_id: "cf4974e5-3c8b-4ae6-8220-d65492d0fc2b" -->
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
