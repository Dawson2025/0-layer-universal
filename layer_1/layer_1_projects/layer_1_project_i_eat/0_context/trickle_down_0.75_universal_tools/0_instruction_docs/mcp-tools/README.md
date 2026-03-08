---
resource_id: "1ffd3862-3fb9-4ce1-992a-263f8f04981e"
resource_type: "readme_document"
resource_name: "README"
---
# MCP (Model Context Protocol) Tools - Universal Documentation

<!-- section_id: "a650ce88-b8f6-4470-9d2b-eb9fd68c0b5a" -->
## Overview

This directory contains comprehensive documentation for MCP (Model Context Protocol) tools and servers used across all AI agents in the lang-trak-in-progress project. MCP provides a standardized way for AI agents to interact with external tools and services.

<!-- section_id: "e96deb06-407b-4c0c-b4dd-d19c1bf5b2be" -->
## 🎯 Purpose

MCP tools enable AI agents to:
- Access external APIs and services
- Interact with databases and file systems
- Perform web searches and browser automation
- Manage documentation and context
- Integrate with communication platforms

<!-- section_id: "4f0eff1c-41cd-4295-af17-31a6e5b308f1" -->
## 📁 Documentation Structure

<!-- section_id: "4808c0a8-675c-4acd-9f9e-47eeb7637a67" -->
### Core MCP System
- **MCP Management System**: Centralized configuration management
- **Environment Configurations**: Development, production, and testing setups
- **Deployment Scripts**: Automated deployment and management tools

<!-- section_id: "2d40986d-4e5e-4e51-8306-3e40cbe53526" -->
### Individual MCP Servers
- **Context7**: Documentation and context management
- **Browser Automation**: Chrome DevTools, Playwright, Browser tools
- **Search & Research**: Web search, GitHub search, filesystem access
- **Communication**: Slack integration
- **Database**: PostgreSQL integration

<!-- section_id: "713a36a8-9231-40b3-8818-49cfd0e3622d" -->
## 🚀 Quick Start

<!-- section_id: "011217df-11d3-45cf-b966-248a0a4a01e7" -->
### 1. Set Up MCP Management System
```bash
# Initialize the complete MCP system
python3 scripts/mcp-cli.py setup

# Deploy development environment
python3 scripts/mcp-cli.py deploy development

# Check system status
python3 scripts/mcp-cli.py status
```

<!-- section_id: "b5b4fa18-c4e3-4842-b375-9eca75f86b85" -->
### 2. Set Up Context7 (Documentation Tool)
```bash
# Set up Context7 MCP server
python3 scripts/context7-setup.py setup-local

# Check Context7 status
python3 scripts/context7-setup.py status
```

<!-- section_id: "e512e88c-1c99-4d95-a6a8-d02c3da0fa3b" -->
### 3. Integrate with Claude Code
```bash
# Add Context7 to Claude Code (local)
claude mcp add context7 -- npx -y @upstash/context7-mcp --api-key ctx7sk-d20b6dec-5980-4ee1-9beb-0e635d626f46

# Add Context7 to Claude Code (remote)
claude mcp add --transport http context7 https://mcp.context7.com/mcp --header "CONTEXT7_API_KEY: ctx7sk-d20b6dec-5980-4ee1-9beb-0e635d626f46"
```

<!-- section_id: "a0a8519c-997a-4013-bf25-4a994603b87b" -->
## 📚 Available Documentation

<!-- section_id: "bb55af8f-cb66-4c7f-844b-6ebe3526696c" -->
### Context7 MCP Server
- **[Complete Setup Guide](CONTEXT7_CLAUDE_SETUP.md)**: Detailed setup instructions for Context7
- **[Quick Reference](CONTEXT7_QUICK_REFERENCE.md)**: Quick commands and troubleshooting

<!-- section_id: "45029a07-461e-4fc7-a04e-f8de5718a901" -->
### MCP Management System
- **[MCP System Guide](../../../../MCP_SYSTEM_GUIDE.md)**: Complete MCP management system documentation
- **Configuration Files**: Located in `config/mcp/`
- **Management Scripts**: Located in `scripts/`

<!-- section_id: "7cfcd421-98ce-47d8-9277-640917b5243e" -->
## 🔧 Available MCP Servers

<!-- section_id: "815a73d3-81f3-49ea-98a4-433ee311d652" -->
### Browser Automation
- **chrome-devtools**: Chrome DevTools integration for debugging
- **playwright**: Cross-browser testing and automation
- **browser**: Simple browser automation

<!-- section_id: "b23edee3-b824-416d-bb35-07de00b5ac3f" -->
### Search & Research
- **web-search**: Tavily web search integration
- **github-search**: GitHub repository search
- **context7**: Documentation and context management
- **filesystem**: File system access and management

<!-- section_id: "0973f9bf-94a0-4c44-a356-01433d85bd95" -->
### Communication & Database
- **slack**: Slack integration for notifications
- **postgres**: PostgreSQL database integration

<!-- section_id: "a773675a-56ca-4b38-8d4e-66567ff0f19e" -->
## 🌍 Environment Configurations

<!-- section_id: "31294dd2-13a8-4a86-9e25-1704b2866f5a" -->
### Development Environment
- **Purpose**: Full debugging and development tools
- **Servers**: All browser automation, search, and development tools
- **Configuration**: `config/mcp/development.json`

<!-- section_id: "34124a05-c901-415c-90e6-12396962b15a" -->
### Production Environment
- **Purpose**: Essential tools for production use
- **Servers**: Web search, filesystem, communication, database tools
- **Configuration**: `config/mcp/production.json`

<!-- section_id: "7be551d5-3064-4e3f-9a6e-c71970ebd863" -->
### Testing Environment
- **Purpose**: Automated testing and validation
- **Servers**: Browser automation and filesystem tools
- **Configuration**: `config/mcp/testing.json`

<!-- section_id: "1d918faf-b883-48a0-831f-15593ea82b24" -->
## 🛠️ Management Commands

<!-- section_id: "19a82728-9d24-4cd1-b484-d21102c9c24d" -->
### MCP System Management
```bash
# Deploy configuration
python3 scripts/mcp-cli.py deploy <environment>

# Check status
python3 scripts/mcp-cli.py status

# Run health check
python3 scripts/mcp-cli.py health

# Generate report
python3 scripts/mcp-cli.py report
```

<!-- section_id: "5787405e-5783-449a-a82a-53b558f2173e" -->
### Context7 Management
```bash
# Set up local server
python3 scripts/context7-setup.py setup-local

# Set up remote server
python3 scripts/context7-setup.py setup-remote

# Set up both options
python3 scripts/context7-setup.py setup-hybrid

# Check status
python3 scripts/context7-setup.py status
```

<!-- section_id: "c69488b3-fa6f-4d0a-bb7d-706d76f56da8" -->
## 📊 Configuration Files

<!-- section_id: "d447f7c6-fd62-4aea-a182-692c9c38a5a8" -->
### Main Configuration
- **`.mcp.json`**: Current active MCP configuration
- **`config/mcp/mcp-system.json`**: Main system configuration

<!-- section_id: "7aae848e-4953-44c9-a064-3d86e5a7c756" -->
### Environment Configurations
- **`config/mcp/development.json`**: Development environment
- **`config/mcp/production.json`**: Production environment
- **`config/mcp/testing.json`**: Testing environment

<!-- section_id: "a8fcdfc5-2272-4ae9-aa1d-7e4cd7592716" -->
### Example Configurations
- **`config/mcp/examples/`**: Example configurations for all MCP servers

<!-- section_id: "fd614d20-e2a9-4437-863c-3a606dfd7439" -->
## 🔒 Security & API Keys

<!-- section_id: "8215d3a6-ede9-4d64-90e8-f3535ed38c60" -->
### API Key Configuration
- **Context7**: `your_context7_api_key_here`
- **Tavily**: `your_tavily_api_key_here`
- **GitHub**: `your_github_token_here`

<!-- section_id: "b16a58fd-2916-494d-93b4-1cec94989088" -->
### Security Notes
- API keys are stored in environment-specific configurations
- Production keys should be replaced with actual values
- Consider using environment variables for sensitive data
- Regular backup of configurations is recommended

<!-- section_id: "50f89a85-1c5d-442a-af45-123cbe19eb93" -->
## 🚨 Troubleshooting

<!-- section_id: "b4734a6f-a233-4722-a6f4-d177d17f191e" -->
### Common Issues
1. **Server Won't Start**: Check dependencies and configuration
2. **Missing Dependencies**: Run setup scripts to install required packages
3. **Configuration Errors**: Validate configuration with health checks
4. **API Key Issues**: Verify API keys are correct and active

<!-- section_id: "caecc07c-36dd-4d6a-8e8d-46554406b21a" -->
### Debug Commands
```bash
# Check MCP system health
python3 scripts/mcp-cli.py health

# Check Context7 status
python3 scripts/context7-setup.py status

# Validate configuration
python3 scripts/mcp-cli.py validate development

# Check logs
tail -f backups/mcp/mcp.log
```

<!-- section_id: "56b7e756-ddce-4901-b549-21d6a5efa6a2" -->
## 📈 Benefits

<!-- section_id: "ac862142-8bc0-4dd3-b345-c1eeb0e3179a" -->
### For AI Agents
- **Consistent Tools**: Same tools available across all environments
- **Easy Management**: Simple commands to start/stop/configure
- **Reliability**: Health checks ensure servers are running
- **Flexibility**: Easy to add new MCP servers as needed

<!-- section_id: "923abe1d-fd11-4a40-899f-04ae5af49dde" -->
### For Development
- **Centralized Configuration**: All MCP configurations in one place
- **Environment Isolation**: Separate configs for different environments
- **Automated Deployment**: No manual configuration management
- **Comprehensive Documentation**: Complete setup and usage guides

<!-- section_id: "ea2e37a9-5fc8-40ef-9c28-943ef849de9d" -->
## 🎯 Next Steps

1. **Review Documentation**: Read the complete setup guides
2. **Set Up MCP System**: Run the setup commands
3. **Configure Context7**: Set up documentation tools
4. **Integrate with Claude Code**: Add MCP servers to your AI agents
5. **Test and Validate**: Ensure everything is working correctly

<!-- section_id: "c7c56ea9-74f3-4e09-bc70-789b026c8b53" -->
## 📞 Support

- **Health Check**: `python3 scripts/mcp-cli.py health`
- **Context7 Status**: `python3 scripts/context7-setup.py status`
- **System Logs**: Check `backups/mcp/mcp.log`
- **Documentation**: Review the complete guides in this directory

---

**MCP tools provide a powerful foundation for AI agent capabilities. This documentation ensures consistent setup and usage across all environments and agents.**
