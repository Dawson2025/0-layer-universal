---
resource_id: "42030bdd-9d68-47e9-863f-d8b7b92ad62c"
resource_type: "readme_document"
resource_name: "README"
---
# MCP (Model Context Protocol) Tools - Universal Documentation

<!-- section_id: "d64d1717-e1cb-42a8-adc7-44048d107044" -->
## Overview

This directory contains comprehensive documentation for MCP (Model Context Protocol) tools and servers used across all AI agents in the lang-trak-in-progress project. MCP provides a standardized way for AI agents to interact with external tools and services.

<!-- section_id: "e3b1bbc6-8eae-49f3-b0fb-ab001bce09de" -->
## 🎯 Purpose

MCP tools enable AI agents to:
- Access external APIs and services
- Interact with databases and file systems
- Perform web searches and browser automation
- Manage documentation and context
- Integrate with communication platforms

<!-- section_id: "5b766f0c-8c8f-47ab-850a-2127ba4ddcca" -->
## 📁 Documentation Structure

<!-- section_id: "5b2f48cd-94ba-4fa5-9828-1f9cba69379e" -->
### Core MCP System
- **MCP Management System**: Centralized configuration management
- **Environment Configurations**: Development, production, and testing setups
- **Deployment Scripts**: Automated deployment and management tools

<!-- section_id: "b0a93595-db61-4e70-81d6-8c14f4435ddb" -->
### Individual MCP Servers
- **Context7**: Documentation and context management
- **Browser Automation**: Chrome DevTools, Playwright, Browser tools
- **Search & Research**: Web search, GitHub search, filesystem access
- **Communication**: Slack integration
- **Database**: PostgreSQL integration

<!-- section_id: "394e1628-e5a9-4f83-8c41-ebb25302afb6" -->
## 🚀 Quick Start

<!-- section_id: "5f569136-09c4-4aa5-9a51-b52f1aed4549" -->
### 1. Set Up MCP Management System
```bash
# Initialize the complete MCP system
python3 scripts/mcp-cli.py setup

# Deploy development environment
python3 scripts/mcp-cli.py deploy development

# Check system status
python3 scripts/mcp-cli.py status
```

<!-- section_id: "c0edd590-994f-4aa1-bb14-cae6a44f9f45" -->
### 2. Set Up Context7 (Documentation Tool)
```bash
# Set up Context7 MCP server
python3 scripts/context7-setup.py setup-local

# Check Context7 status
python3 scripts/context7-setup.py status
```

<!-- section_id: "7061ea08-b03a-4b60-8793-09d001cd9873" -->
### 3. Integrate with Claude Code
```bash
# Add Context7 to Claude Code (local)
claude mcp add context7 -- npx -y @upstash/context7-mcp --api-key ctx7sk-d20b6dec-5980-4ee1-9beb-0e635d626f46

# Add Context7 to Claude Code (remote)
claude mcp add --transport http context7 https://mcp.context7.com/mcp --header "CONTEXT7_API_KEY: ctx7sk-d20b6dec-5980-4ee1-9beb-0e635d626f46"
```

<!-- section_id: "3f18d2e2-f09e-4a63-8abf-493ad159c685" -->
## 📚 Available Documentation

<!-- section_id: "ae88d1ee-e405-4dbf-b595-056fb3ff4328" -->
### Context7 MCP Server
- **[Complete Setup Guide](CONTEXT7_CLAUDE_SETUP.md)**: Detailed setup instructions for Context7
- **[Quick Reference](CONTEXT7_QUICK_REFERENCE.md)**: Quick commands and troubleshooting

<!-- section_id: "d939a3b1-c8ad-43ff-bbbb-b189bed0a276" -->
### MCP Management System
- **[MCP System Guide](../../../../MCP_SYSTEM_GUIDE.md)**: Complete MCP management system documentation
- **Configuration Files**: Located in `config/mcp/`
- **Management Scripts**: Located in `scripts/`

<!-- section_id: "c35438b0-2c54-4efb-8883-5e6855a72d55" -->
## 🔧 Available MCP Servers

<!-- section_id: "51467664-3a2e-4428-88b8-921e4fef4e56" -->
### Browser Automation
- **chrome-devtools**: Chrome DevTools integration for debugging
- **playwright**: Cross-browser testing and automation
- **browser**: Simple browser automation

<!-- section_id: "5db708f9-c740-4373-8237-c694737ce5ee" -->
### Search & Research
- **web-search**: Tavily web search integration
- **github-search**: GitHub repository search
- **context7**: Documentation and context management
- **filesystem**: File system access and management

<!-- section_id: "406dae19-585c-4fef-bdde-fb937d187412" -->
### Communication & Database
- **slack**: Slack integration for notifications
- **postgres**: PostgreSQL database integration

<!-- section_id: "d2e6ea66-dbff-4ffc-a6e1-f8f41fb55772" -->
## 🌍 Environment Configurations

<!-- section_id: "a26051aa-3bf0-4b6f-bd80-16e64c8a401c" -->
### Development Environment
- **Purpose**: Full debugging and development tools
- **Servers**: All browser automation, search, and development tools
- **Configuration**: `config/mcp/development.json`

<!-- section_id: "ae095b38-fe93-411c-8134-0791376a6221" -->
### Production Environment
- **Purpose**: Essential tools for production use
- **Servers**: Web search, filesystem, communication, database tools
- **Configuration**: `config/mcp/production.json`

<!-- section_id: "533bf7c6-1651-4d18-ae0b-8a8bebb508ba" -->
### Testing Environment
- **Purpose**: Automated testing and validation
- **Servers**: Browser automation and filesystem tools
- **Configuration**: `config/mcp/testing.json`

<!-- section_id: "ae6592b7-c9fa-4660-920b-349c791143ed" -->
## 🛠️ Management Commands

<!-- section_id: "2130b0a9-fc44-4cbc-ba52-4bbf6cf9921a" -->
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

<!-- section_id: "1ab72e87-4d2f-4a99-ad6a-5270ff935df6" -->
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

<!-- section_id: "57ff9a71-2349-41fb-b2a8-97f8a7611a8c" -->
## 📊 Configuration Files

<!-- section_id: "2527a344-e4ef-42dc-9e93-3e762f8bfd77" -->
### Main Configuration
- **`.mcp.json`**: Current active MCP configuration
- **`config/mcp/mcp-system.json`**: Main system configuration

<!-- section_id: "8b11aacf-98c4-4d3a-b97e-dd69e2ecc162" -->
### Environment Configurations
- **`config/mcp/development.json`**: Development environment
- **`config/mcp/production.json`**: Production environment
- **`config/mcp/testing.json`**: Testing environment

<!-- section_id: "221f8fc0-9a68-4b74-aa89-50848722f43e" -->
### Example Configurations
- **`config/mcp/examples/`**: Example configurations for all MCP servers

<!-- section_id: "0500b55c-a765-459d-8cbf-8f8cbd46203e" -->
## 🔒 Security & API Keys

<!-- section_id: "e8c783fb-195e-4b39-b2ff-0056c4d802ad" -->
### API Key Configuration
- **Context7**: `your_context7_api_key_here`
- **Tavily**: `your_tavily_api_key_here`
- **GitHub**: `your_github_token_here`

<!-- section_id: "1d653ae4-c2e4-4aa0-b5a5-b193c4e1ed83" -->
### Security Notes
- API keys are stored in environment-specific configurations
- Production keys should be replaced with actual values
- Consider using environment variables for sensitive data
- Regular backup of configurations is recommended

<!-- section_id: "25e3747c-fbb7-4643-b4c7-c72aa16e7b2c" -->
## 🚨 Troubleshooting

<!-- section_id: "b4d57441-6680-4d6c-b956-a12d891f0298" -->
### Common Issues
1. **Server Won't Start**: Check dependencies and configuration
2. **Missing Dependencies**: Run setup scripts to install required packages
3. **Configuration Errors**: Validate configuration with health checks
4. **API Key Issues**: Verify API keys are correct and active

<!-- section_id: "88da0184-5555-4b76-b24e-fee748365796" -->
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

<!-- section_id: "b371eeb2-c642-4d15-9a0e-55417a8eb386" -->
## 📈 Benefits

<!-- section_id: "fd947cf6-eaff-45e1-9d07-a5d0b12ead90" -->
### For AI Agents
- **Consistent Tools**: Same tools available across all environments
- **Easy Management**: Simple commands to start/stop/configure
- **Reliability**: Health checks ensure servers are running
- **Flexibility**: Easy to add new MCP servers as needed

<!-- section_id: "3e3304fe-ed41-4e62-9e16-89f017f6dd14" -->
### For Development
- **Centralized Configuration**: All MCP configurations in one place
- **Environment Isolation**: Separate configs for different environments
- **Automated Deployment**: No manual configuration management
- **Comprehensive Documentation**: Complete setup and usage guides

<!-- section_id: "8a9ecbba-a837-4dfe-9585-d5c614866657" -->
## 🎯 Next Steps

1. **Review Documentation**: Read the complete setup guides
2. **Set Up MCP System**: Run the setup commands
3. **Configure Context7**: Set up documentation tools
4. **Integrate with Claude Code**: Add MCP servers to your AI agents
5. **Test and Validate**: Ensure everything is working correctly

<!-- section_id: "c0e9b1c4-0864-4ca9-9ee1-5aafece3a337" -->
## 📞 Support

- **Health Check**: `python3 scripts/mcp-cli.py health`
- **Context7 Status**: `python3 scripts/context7-setup.py status`
- **System Logs**: Check `backups/mcp/mcp.log`
- **Documentation**: Review the complete guides in this directory

---

**MCP tools provide a powerful foundation for AI agent capabilities. This documentation ensures consistent setup and usage across all environments and agents.**
