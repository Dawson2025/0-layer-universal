# MCP (Model Context Protocol) Tools - Universal Documentation

## Overview

This directory contains comprehensive documentation for MCP (Model Context Protocol) tools and servers used across all AI agents in the lang-trak-in-progress project. MCP provides a standardized way for AI agents to interact with external tools and services.

## 🎯 Purpose

MCP tools enable AI agents to:
- Access external APIs and services
- Interact with databases and file systems
- Perform web searches and browser automation
- Manage documentation and context
- Integrate with communication platforms

## 📁 Documentation Structure

### Core MCP System
- **MCP Management System**: Centralized configuration management
- **Environment Configurations**: Development, production, and testing setups
- **Deployment Scripts**: Automated deployment and management tools

### Individual MCP Servers
- **Context7**: Documentation and context management
- **Browser Automation**: Chrome DevTools, Playwright, Browser tools
- **Search & Research**: Web search, GitHub search, filesystem access
- **Communication**: Slack integration
- **Database**: PostgreSQL integration

## 🚀 Quick Start

### 1. Set Up MCP Management System
```bash
# Initialize the complete MCP system
python3 scripts/mcp-cli.py setup

# Deploy development environment
python3 scripts/mcp-cli.py deploy development

# Check system status
python3 scripts/mcp-cli.py status
```

### 2. Set Up Context7 (Documentation Tool)
```bash
# Set up Context7 MCP server
python3 scripts/context7-setup.py setup-local

# Check Context7 status
python3 scripts/context7-setup.py status
```

### 3. Integrate with Claude Code
```bash
# Add Context7 to Claude Code (local)
claude mcp add context7 -- npx -y @upstash/context7-mcp --api-key ctx7sk-d20b6dec-5980-4ee1-9beb-0e635d626f46

# Add Context7 to Claude Code (remote)
claude mcp add --transport http context7 https://mcp.context7.com/mcp --header "CONTEXT7_API_KEY: ctx7sk-d20b6dec-5980-4ee1-9beb-0e635d626f46"
```

## 📚 Available Documentation

### Context7 MCP Server
- **[Complete Setup Guide](CONTEXT7_CLAUDE_SETUP.md)**: Detailed setup instructions for Context7
- **[Quick Reference](CONTEXT7_QUICK_REFERENCE.md)**: Quick commands and troubleshooting

### MCP Management System
- **[MCP System Guide](MCP_SYSTEM_GUIDE.md)**: Complete MCP management system documentation
- **[MCP Configuration Guide](MCP_CONFIGURATION_GUIDE.md)**: How to configure MCP servers
- **[MCP Server Setup](MCP_SERVER_SETUP.md)**: General MCP server setup guide
- **[MCP Work Log](MCP_WORK_LOG.md)**: Development work log for MCP server implementation

## 🔧 Available MCP Servers

### Browser Automation
- **chrome-devtools**: Chrome DevTools integration for debugging
- **playwright**: Cross-browser testing and automation
- **browser**: Simple browser automation
- **[Playwright MCP Cursor Setup](PLAYWRIGHT_MCP_CURSOR_SETUP.md)**: Complete setup guide for Playwright MCP in Cursor IDE (Linux/Ubuntu and WSL)
- **[Playwright MCP Usage](PLAYWRIGHT_MCP_USAGE.md)**: Usage guide for Playwright MCP server (all AI applications)
- **[Playwright MCP Testing](PLAYWRIGHT_MCP_TESTING.md)**: Testing documentation and troubleshooting
- **[Chrome DevTools MCP Setup](CHROME_DEVTOOLS_MCP_SETUP.md)**: Setup guide for Chrome DevTools MCP server
- **[Cursor Browser MCP Setup](CURSOR_BROWSER_MCP_SETUP.md)**: Browser automation setup for Cursor IDE (includes WSL notes)
- **[Browser MCP Setup Experience](BROWSER_MCP_SETUP_EXPERIENCE.md)**: Comprehensive documentation of setup experience, lessons learned, and troubleshooting for Linux/Ubuntu
- **[Testing MCP](TESTING_MCP.md)**: Testing guide for MCP servers

### Linux/Ubuntu-Specific Issues
- **[Linux/Ubuntu MCP Issues](LINUX_UBUNTU_MCP_ISSUES.md)**: OS-level MCP issues on Linux/Ubuntu
- **[Cursor IDE Linux MCP Issues](CURSOR_IDE_LINUX_MCP_ISSUES.md)**: Cursor IDE-specific MCP issues on Linux
- **[Linux/Ubuntu AI Apps MCP Issues](LINUX_UBUNTU_AI_APPS_MCP_ISSUES.md)**: AI apps and tools MCP issues on Linux

#### Recent lessons (Linux, Chrome/Playwright MCP)
- Playwright MCP can report “Browser specified in your config is not installed” and drop the transport even when `playwright install chromium` is done and `--executable-path` points to `~/.cache/ms-playwright/.../chrome`. Adding `PLAYWRIGHT_BROWSERS_PATH` and `--no-sandbox` did not resolve; the server exited before tools were usable.
- chrome-devtools MCP may also close transport immediately even with a running Chrome on `--remote-debugging-port=9222`.
- Reliable workaround: launch Chrome manually with remote debugging (`google-chrome --remote-debugging-port=9222 --user-data-dir ~/.config/mcp/playwright-profile`) and connect via Playwright CDP directly:
  ```bash
  node -e "const { chromium } = require('playwright'); (async() => { const b = await chromium.connectOverCDP('http://127.0.0.1:9222'); const ctx = b.contexts()[0]; const page = await ctx.newPage(); await page.goto('https://www.aleks.com'); console.log('Opened page via CDP.'); })();"
  ```
- If MCP servers remain unstable, prefer direct CDP scripts (above) or the `browser` server as fallback to interact with the already-open Chrome.

### Search & Research
- **web-search**: Tavily web search integration
- **github-search**: GitHub repository search
- **context7**: Documentation and context management
- **filesystem**: File system access and management

### Communication & Database
- **slack**: Slack integration for notifications
- **postgres**: PostgreSQL database integration

## 🌍 Environment Configurations

### Development Environment
- **Purpose**: Full debugging and development tools
- **Servers**: All browser automation, search, and development tools
- **Configuration**: `config/mcp/development.json`

### Production Environment
- **Purpose**: Essential tools for production use
- **Servers**: Web search, filesystem, communication, database tools
- **Configuration**: `config/mcp/production.json`

### Testing Environment
- **Purpose**: Automated testing and validation
- **Servers**: Browser automation and filesystem tools
- **Configuration**: `config/mcp/testing.json`

## 🛠️ Management Commands

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

## 📝 Gemini CLI `settings.json` Configuration

For the Gemini CLI to correctly detect and use MCP servers, the `settings.json` file must be located at `~/.gemini/settings.json`.

**Crucially, this file should contain *all* your Gemini CLI settings, including API keys, IDE integration settings, and the `mcpServers` configuration.** Do not create separate `settings.json` files for different configurations; merge them into a single file.

**Example `settings.json` structure:**

```json
{
  "ide": {
    "enabled": true
  },
  "auth": {
    "method": "apiKey",
    "apiKey": "YOUR_GEMINI_API_KEY_HERE"
  },
  "security": {
    "auth": {
      "selectedType": "gemini-api-key"
    }
  },
  "hasSeenIdeIntegrationNudge": true,
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "@playwright/mcp@latest",
        "--browser", "chromium",
        "--headless"
      ]
    }
    // Add other MCP server configurations here if needed
  }
}
```

**After updating `~/.gemini/settings.json`, you *must* restart the Gemini CLI for the changes to take effect.**

### Environment Configurations
- **`config/mcp/development.json`**: Development environment
- **`config/mcp/production.json`**: Production environment
- **`config/mcp/testing.json`**: Testing environment

### Example Configurations
- **`config/mcp/examples/`**: Example configurations for all MCP servers

## 🔒 Security & API Keys

### API Key Configuration
- **Context7**: `your_context7_api_key_here`
- **Tavily**: `your_tavily_api_key_here`
- **GitHub**: `your_github_token_here`

### Security Notes
- API keys are stored in environment-specific configurations
- Production keys should be replaced with actual values
- Consider using environment variables for sensitive data
- Regular backup of configurations is recommended

## 🚨 Troubleshooting

### Common Issues
1. **Server Won't Start**: Check dependencies and configuration
2. **Missing Dependencies**: Run setup scripts to install required packages
3. **Configuration Errors**: Validate configuration with health checks
4. **API Key Issues**: Verify API keys are correct and active

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

## 📈 Benefits

### For AI Agents
- **Consistent Tools**: Same tools available across all environments
- **Easy Management**: Simple commands to start/stop/configure
- **Reliability**: Health checks ensure servers are running
- **Flexibility**: Easy to add new MCP servers as needed

### For Development
- **Centralized Configuration**: All MCP configurations in one place
- **Environment Isolation**: Separate configs for different environments
- **Automated Deployment**: No manual configuration management
- **Comprehensive Documentation**: Complete setup and usage guides

## 🎯 Next Steps

1. **Review Documentation**: Read the complete setup guides
2. **Set Up MCP System**: Run the setup commands
3. **Configure Context7**: Set up documentation tools
4. **Integrate with Claude Code**: Add MCP servers to your AI agents
5. **Test and Validate**: Ensure everything is working correctly

## 📞 Support

- **Health Check**: `python3 scripts/mcp-cli.py health`
- **Context7 Status**: `python3 scripts/context7-setup.py status`
- **System Logs**: Check `backups/mcp/mcp.log`
- **Documentation**: Review the complete guides in this directory

---

**MCP tools provide a powerful foundation for AI agent capabilities. This documentation ensures consistent setup and usage across all environments and agents.**
