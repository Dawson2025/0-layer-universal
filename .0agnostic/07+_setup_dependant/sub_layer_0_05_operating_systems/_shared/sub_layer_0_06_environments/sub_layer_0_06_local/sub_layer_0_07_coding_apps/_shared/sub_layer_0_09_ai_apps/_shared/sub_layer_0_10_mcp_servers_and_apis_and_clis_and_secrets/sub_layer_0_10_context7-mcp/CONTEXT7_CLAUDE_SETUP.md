---
resource_id: "3f8f52b7-f43e-4e81-8eac-f76a2fbd579c"
resource_type: "document"
resource_name: "CONTEXT7_CLAUDE_SETUP"
---
# Context7 MCP Server - Claude Code Integration Guide

<!-- section_id: "cc14678c-be46-4965-86ba-303d89dfc469" -->
## Overview

This guide shows you how to set up Context7 MCP server for use with Claude Code, including both local and remote connection options.

<!-- section_id: "66e0ee23-20fd-4a4a-952a-93919ac82a58" -->
## 🔑 Your API Credentials

- **API Key**: `YOUR_CONTEXT7_API_KEY`
- **API URL**: `https://context7.com/api/v1`
- **MCP URL**: `https://mcp.context7.com/mcp`

<!-- section_id: "135a6c78-2089-49a4-84cb-e2675ae7d274" -->
## 🚀 Quick Setup Options

<!-- section_id: "ca9fc7e5-fe33-457a-a9c0-d17fd9206c8c" -->
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

<!-- section_id: "38e255d4-355d-442f-b659-3eb0c206d640" -->
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

<!-- section_id: "74465e47-894a-49f3-a66b-bfd7f17ecb17" -->
## 🔧 Advanced Setup with MCP Management System

If you're using the centralized MCP management system in this project:

<!-- section_id: "dd8a2af4-64c7-49a7-bf0f-79ed70aa684a" -->
### 1. Set up Context7 in the Management System

```bash
# For local server
python3 scripts/context7-setup.py setup-local

# For remote server
python3 scripts/context7-setup.py setup-remote

# For both options (hybrid)
python3 scripts/context7-setup.py setup-hybrid
```

<!-- section_id: "ecfe45b0-7438-476d-8ab1-8540002bd448" -->
### 2. Check Status

```bash
python3 scripts/context7-setup.py status
```

<!-- section_id: "36f9eeae-3f76-48ba-b579-a43095bd0233" -->
### 3. Deploy Configuration

```bash
# Deploy development environment
python3 scripts/mcp-cli.py deploy development

# Check overall MCP status
python3 scripts/mcp-cli.py status
```

<!-- section_id: "001c1ec5-6c3a-4f96-a1e1-587be28d97c5" -->
## 📁 Configuration Files

The MCP management system creates several configuration files:

<!-- section_id: "1b6d7e6a-5a6b-4589-b020-b28bc129e965" -->
### Current Active Configuration
- **File**: `.mcp.json`
- **Contains**: Currently active MCP server configuration

<!-- section_id: "bb339564-8067-482d-9461-59b5a73ce4cd" -->
### Example Configurations
- **Local**: `config/mcp/examples/context7-local.json`
- **Remote**: `config/mcp/examples/context7-remote.json`
- **Hybrid**: `config/mcp/examples/context7-hybrid.json`

<!-- section_id: "7ae4f32a-98b5-4c0c-be70-1deeab0e8bd8" -->
### Environment-Specific Configurations
- **Development**: `config/mcp/development.json`
- **Production**: `config/mcp/production.json`
- **Testing**: `config/mcp/testing.json`

<!-- section_id: "af717184-cfaa-4c83-8072-39d71fd19f92" -->
## 🧪 Testing Your Setup

<!-- section_id: "24c383a2-b289-48ed-b10a-28b76a0e573b" -->
### Test Local Setup
```bash
# Test if the local package is accessible
npx -y @upstash/context7-mcp --help
```

<!-- section_id: "56ac4d27-9571-470f-88f0-98f5d827b707" -->
### Test Remote Setup
```bash
# Test if the remote endpoint is accessible
curl -I https://mcp.context7.com/mcp
```

<!-- section_id: "093d7909-d26f-49e7-89e5-0482162354be" -->
### Test in Claude Code
1. Open Claude Code
2. Check if Context7 appears in the MCP servers list
3. Try using Context7 tools in your conversations

<!-- section_id: "caf2c2d4-7b03-4e13-9a7b-23940ce7ea2c" -->
## 🔄 Switching Between Configurations

<!-- section_id: "de11cca3-bb1e-4ce3-95a5-da52019d955d" -->
### Switch to Local Server
```bash
# Using MCP management system
python3 scripts/context7-setup.py setup-local

# Or manually update .mcp.json
cp config/mcp/examples/context7-local.json .mcp.json
```

<!-- section_id: "c6135b12-91cd-4679-80de-88bbe8cf3d7c" -->
### Switch to Remote Server
```bash
# Using MCP management system
python3 scripts/context7-setup.py setup-remote

# Or manually update .mcp.json
cp config/mcp/examples/context7-remote.json .mcp.json
```

<!-- section_id: "5368a863-892d-40d2-9f6a-d5d46e541f6f" -->
### Switch to Hybrid (Both Options)
```bash
# Using MCP management system
python3 scripts/context7-setup.py setup-hybrid

# Or manually update .mcp.json
cp config/mcp/examples/context7-hybrid.json .mcp.json
```

<!-- section_id: "b9867336-bb57-4c49-aa64-e3ec98bca312" -->
## 🛠️ Troubleshooting

<!-- section_id: "f1ad1e9e-aa92-4e84-8abd-e25573914723" -->
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

<!-- section_id: "91a51097-ef32-438f-a50c-8874dd1c10b9" -->
### Debug Commands

```bash
# Check MCP management system status
python3 scripts/context7-setup.py status

# Check overall MCP system health
python3 scripts/mcp-cli.py health

# Validate configuration
python3 scripts/mcp-cli.py validate development
```

<!-- section_id: "8caa774c-ac38-44be-94c7-f823603e10f8" -->
## 📊 Monitoring and Management

<!-- section_id: "890c4f64-3223-4ff1-9bfe-d125e1de945a" -->
### Check Server Status
```bash
# Context7 specific status
python3 scripts/context7-setup.py status

# Overall MCP system status
python3 scripts/mcp-cli.py status
```

<!-- section_id: "e3a72577-fc2f-448a-bc93-c18f78dd7514" -->
### View Logs
```bash
# Check MCP logs
tail -f backups/mcp/mcp.log

# Check system logs
journalctl -u claude-code
```

<!-- section_id: "e5bad8b7-2650-4a4b-8aa2-c50b7f68a9bb" -->
## 🎯 Best Practices

<!-- section_id: "2437848b-211d-4156-9451-2cd86a64fc51" -->
### Development
- Use **local server** for better performance and debugging
- Keep the MCP management system updated
- Test both configurations regularly

<!-- section_id: "0d64205e-a6c4-4035-9be9-1898ab7f5128" -->
### Production
- Use **remote server** for simplicity and reliability
- Monitor server status regularly
- Have backup configurations ready

<!-- section_id: "6196b872-a3ab-4198-a631-b965c2b1a8c2" -->
### Hybrid Approach
- Use **hybrid setup** for maximum flexibility
- Switch between local and remote as needed
- Keep both configurations tested and ready

<!-- section_id: "3aa8c253-92e7-4e84-8bc9-998fd6662bee" -->
## 📚 Additional Resources

- **MCP System Guide**: `docs/MCP_SYSTEM_GUIDE.md`
- **Configuration Examples**: `config/mcp/examples/`
- **Management Scripts**: `scripts/context7-setup.py`
- **Context7 Documentation**: [Context7 Docs](https://context7.com/docs)

<!-- section_id: "fa87b381-4a9b-446e-a288-5d469ae9710b" -->
## 🆘 Support

If you encounter issues:

1. **Check Status**: `python3 scripts/context7-setup.py status`
2. **Review Logs**: Check `backups/mcp/mcp.log`
3. **Validate Config**: `python3 scripts/mcp-cli.py validate development`
4. **Test Connectivity**: Use the debug commands above

<!-- section_id: "19f87947-49d8-4ab0-86a6-3d4dd6d0a13a" -->
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
