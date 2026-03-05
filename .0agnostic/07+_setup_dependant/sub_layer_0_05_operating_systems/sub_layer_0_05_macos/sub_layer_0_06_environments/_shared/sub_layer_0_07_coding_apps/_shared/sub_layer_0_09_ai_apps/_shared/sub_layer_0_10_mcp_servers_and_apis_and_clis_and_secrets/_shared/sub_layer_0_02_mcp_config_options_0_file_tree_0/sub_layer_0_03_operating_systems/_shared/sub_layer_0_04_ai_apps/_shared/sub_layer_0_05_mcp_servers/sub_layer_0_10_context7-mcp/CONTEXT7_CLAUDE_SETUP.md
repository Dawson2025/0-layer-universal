---
resource_id: "9fbbf38b-4b93-4688-ba69-4ca35fb187a7"
resource_type: "document"
resource_name: "CONTEXT7_CLAUDE_SETUP"
---
# Context7 MCP Server - Claude Code Integration Guide

<!-- section_id: "166ded65-04dd-49a1-a6fd-e83444772ee4" -->
## Overview

This guide shows you how to set up Context7 MCP server for use with Claude Code, including both local and remote connection options.

<!-- section_id: "d77d87f4-10df-44b8-b0d3-a7dd643f205e" -->
## 🔑 Your API Credentials

- **API Key**: `YOUR_CONTEXT7_API_KEY`
- **API URL**: `https://context7.com/api/v1`
- **MCP URL**: `https://mcp.context7.com/mcp`

<!-- section_id: "773af79e-63b2-4d43-871a-f3880f27ec43" -->
## 🚀 Quick Setup Options

<!-- section_id: "dff36386-0ab7-43df-8455-3c9d62bc313d" -->
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

<!-- section_id: "12d3b73b-4088-4e88-97da-a429cf8dfbe2" -->
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

<!-- section_id: "04ab9077-6757-40c0-b8fd-e38e93293846" -->
## 🔧 Advanced Setup with MCP Management System

If you're using the centralized MCP management system in this project:

<!-- section_id: "82f175d8-a01c-4e6a-8362-ae6f129d34b3" -->
### 1. Set up Context7 in the Management System

```bash
# For local server
python3 scripts/context7-setup.py setup-local

# For remote server
python3 scripts/context7-setup.py setup-remote

# For both options (hybrid)
python3 scripts/context7-setup.py setup-hybrid
```

<!-- section_id: "411c088b-57e3-411e-9186-4f69fe0ed87b" -->
### 2. Check Status

```bash
python3 scripts/context7-setup.py status
```

<!-- section_id: "556ae847-ef09-4f74-a0fd-d9f9e14995d5" -->
### 3. Deploy Configuration

```bash
# Deploy development environment
python3 scripts/mcp-cli.py deploy development

# Check overall MCP status
python3 scripts/mcp-cli.py status
```

<!-- section_id: "95f00f31-aabc-4115-9f58-0d96812c7a49" -->
## 📁 Configuration Files

The MCP management system creates several configuration files:

<!-- section_id: "dbdc9b66-39df-4b69-bb2f-294dc3c244ba" -->
### Current Active Configuration
- **File**: `.mcp.json`
- **Contains**: Currently active MCP server configuration

<!-- section_id: "89f243f6-fb95-4967-b108-6fd1569ddd36" -->
### Example Configurations
- **Local**: `config/mcp/examples/context7-local.json`
- **Remote**: `config/mcp/examples/context7-remote.json`
- **Hybrid**: `config/mcp/examples/context7-hybrid.json`

<!-- section_id: "1d2a4aa7-da8e-4b46-906a-4b246fc7495d" -->
### Environment-Specific Configurations
- **Development**: `config/mcp/development.json`
- **Production**: `config/mcp/production.json`
- **Testing**: `config/mcp/testing.json`

<!-- section_id: "b2fe3def-c69e-4646-b90f-f05c502ae7ef" -->
## 🧪 Testing Your Setup

<!-- section_id: "fddf0e4e-3744-48fc-aeac-16bf543f2648" -->
### Test Local Setup
```bash
# Test if the local package is accessible
npx -y @upstash/context7-mcp --help
```

<!-- section_id: "282fc032-70e9-4294-acb3-b6ff3c7b2ffc" -->
### Test Remote Setup
```bash
# Test if the remote endpoint is accessible
curl -I https://mcp.context7.com/mcp
```

<!-- section_id: "23f879df-2892-46bf-a183-d350e8db2433" -->
### Test in Claude Code
1. Open Claude Code
2. Check if Context7 appears in the MCP servers list
3. Try using Context7 tools in your conversations

<!-- section_id: "608c3e63-f6d1-4286-8282-bdce08ba539a" -->
## 🔄 Switching Between Configurations

<!-- section_id: "26bed1e2-112d-4468-aaea-99fce221cb82" -->
### Switch to Local Server
```bash
# Using MCP management system
python3 scripts/context7-setup.py setup-local

# Or manually update .mcp.json
cp config/mcp/examples/context7-local.json .mcp.json
```

<!-- section_id: "8f6f6e2b-ee29-41e9-8b44-2f2680425b54" -->
### Switch to Remote Server
```bash
# Using MCP management system
python3 scripts/context7-setup.py setup-remote

# Or manually update .mcp.json
cp config/mcp/examples/context7-remote.json .mcp.json
```

<!-- section_id: "48737925-b301-4b00-bc8e-bbb68debbe3c" -->
### Switch to Hybrid (Both Options)
```bash
# Using MCP management system
python3 scripts/context7-setup.py setup-hybrid

# Or manually update .mcp.json
cp config/mcp/examples/context7-hybrid.json .mcp.json
```

<!-- section_id: "280031e3-4735-4db2-b74d-71ba9bd1486d" -->
## 🛠️ Troubleshooting

<!-- section_id: "d89eefb5-a6c9-43e0-8a33-c719bc6eccba" -->
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

<!-- section_id: "736a0088-5085-48ff-980b-fa4e19d806c7" -->
### Debug Commands

```bash
# Check MCP management system status
python3 scripts/context7-setup.py status

# Check overall MCP system health
python3 scripts/mcp-cli.py health

# Validate configuration
python3 scripts/mcp-cli.py validate development
```

<!-- section_id: "623486b7-7c7d-4cae-8b58-af828a3664f7" -->
## 📊 Monitoring and Management

<!-- section_id: "4c0e9ab1-15ad-42e9-88f8-c60e682a9e9d" -->
### Check Server Status
```bash
# Context7 specific status
python3 scripts/context7-setup.py status

# Overall MCP system status
python3 scripts/mcp-cli.py status
```

<!-- section_id: "f2933fce-fc0f-4001-8687-04d940c0f845" -->
### View Logs
```bash
# Check MCP logs
tail -f backups/mcp/mcp.log

# Check system logs
journalctl -u claude-code
```

<!-- section_id: "7f516bc5-f6f4-4a60-9b56-c45be731e27e" -->
## 🎯 Best Practices

<!-- section_id: "32d3592f-ef2b-465d-a482-63371996c6e2" -->
### Development
- Use **local server** for better performance and debugging
- Keep the MCP management system updated
- Test both configurations regularly

<!-- section_id: "6ff4d1ed-c430-41dd-a4fc-bd4af16730ce" -->
### Production
- Use **remote server** for simplicity and reliability
- Monitor server status regularly
- Have backup configurations ready

<!-- section_id: "17ab15ef-ec5b-4065-92c9-9f4a368b08a7" -->
### Hybrid Approach
- Use **hybrid setup** for maximum flexibility
- Switch between local and remote as needed
- Keep both configurations tested and ready

<!-- section_id: "be2585d1-cf24-4319-b9fb-f08984b48aa8" -->
## 📚 Additional Resources

- **MCP System Guide**: `docs/MCP_SYSTEM_GUIDE.md`
- **Configuration Examples**: `config/mcp/examples/`
- **Management Scripts**: `scripts/context7-setup.py`
- **Context7 Documentation**: [Context7 Docs](https://context7.com/docs)

<!-- section_id: "a0758003-a62d-461e-85c2-8559222638fb" -->
## 🆘 Support

If you encounter issues:

1. **Check Status**: `python3 scripts/context7-setup.py status`
2. **Review Logs**: Check `backups/mcp/mcp.log`
3. **Validate Config**: `python3 scripts/mcp-cli.py validate development`
4. **Test Connectivity**: Use the debug commands above

<!-- section_id: "ffe7a755-f93d-4219-a471-4bab6120c2b6" -->
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
