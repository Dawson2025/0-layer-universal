---
resource_id: "26e700e8-62ae-40fc-a00f-1ad9136a251b"
resource_type: "document"
resource_name: "MCP_CONFIGURATION_GUIDE"
---
# MCP Configuration Guide - Universal Tools

<!-- section_id: "e9a030a7-d8cc-449c-a43e-a6bdec8f9f11" -->
## Overview

This guide provides comprehensive instructions for configuring and managing MCP (Model Context Protocol) tools across all environments in the lang-trak-in-progress project.

<!-- section_id: "7e805d39-7b1a-46b9-b8d9-a6e7bd6212e5" -->
## 🎯 Configuration Philosophy

The MCP system follows these principles:
- **Single Source of Truth**: All configurations centralized
- **Environment Isolation**: Separate configs for dev/prod/testing
- **Automated Management**: Scripts handle deployment and updates
- **Easy Switching**: Simple commands to change configurations

<!-- section_id: "4a65e785-1a34-4c60-9a72-df846808c172" -->
## 📁 Configuration Structure

```
config/mcp/
├── mcp-system.json          # Main system configuration
├── development.json         # Development environment
├── production.json          # Production environment
├── testing.json            # Testing environment
├── monitoring.json         # Monitoring configuration
└── examples/               # Example configurations
    ├── context7-local.json
    ├── context7-remote.json
    └── context7-hybrid.json
```

<!-- section_id: "ef13b6b8-e6f0-4f06-b044-bb2a58707cbd" -->
## 🔧 Environment Configurations

<!-- section_id: "f042efae-6b84-42ec-bdf3-b4f868bb13c5" -->
### Development Environment
**Purpose**: Full debugging and development capabilities
**Servers**: All available MCP servers
**Configuration**: `config/mcp/development.json`

```json
{
  "environment": "development",
  "servers": [
    "chrome-devtools",    # Browser debugging
    "playwright",         # Cross-browser testing
    "browser",           # Simple automation
    "web-search",        # Web search
    "github-search",     # GitHub integration
    "filesystem",        # File access
    "context7-local"     # Documentation (local)
  ],
  "global_env": {
    "NODE_ENV": "development",
    "LOG_LEVEL": "debug"
  }
}
```

<!-- section_id: "67e07964-6dc9-4171-a703-0d0bdca804b8" -->
### Production Environment
**Purpose**: Essential tools for production use
**Servers**: Core functionality only
**Configuration**: `config/mcp/production.json`

```json
{
  "environment": "production",
  "servers": [
    "web-search",        # Web search
    "github-search",     # GitHub integration
    "filesystem",        # File access
    "slack",            # Notifications
    "postgres",         # Database
    "context7-remote"   # Documentation (remote)
  ],
  "global_env": {
    "NODE_ENV": "production",
    "LOG_LEVEL": "info"
  }
}
```

<!-- section_id: "c33e5280-ce40-44b8-b09e-37348f7b889a" -->
### Testing Environment
**Purpose**: Automated testing and validation
**Servers**: Testing-focused tools
**Configuration**: `config/mcp/testing.json`

```json
{
  "environment": "testing",
  "servers": [
    "playwright",        # Browser testing
    "browser",          # Simple automation
    "filesystem",       # File access
    "context7-local"    # Documentation (local)
  ],
  "global_env": {
    "NODE_ENV": "test",
    "LOG_LEVEL": "warn"
  }
}
```

<!-- section_id: "3b8b277d-4c73-4b58-b642-c87711cd1887" -->
## 🚀 Setup Commands

<!-- section_id: "7f4f9080-6777-47fd-a341-1bc7ef95419f" -->
### Initial Setup
```bash
# Set up complete MCP system
python3 scripts/mcp-cli.py setup

# Verify setup
python3 scripts/mcp-cli.py health
```

<!-- section_id: "3fa73ce5-b067-45af-97f8-65a1d392f69a" -->
### Environment Deployment
```bash
# Deploy development environment
python3 scripts/mcp-cli.py deploy development

# Deploy production environment
python3 scripts/mcp-cli.py deploy production

# Deploy testing environment
python3 scripts/mcp-cli.py deploy testing
```

<!-- section_id: "016c90e9-f6a6-4821-bb60-e6c012c1b500" -->
### Context7 Setup
```bash
# Set up local Context7 server
python3 scripts/context7-setup.py setup-local

# Set up remote Context7 server
python3 scripts/context7-setup.py setup-remote

# Set up both options
python3 scripts/context7-setup.py setup-hybrid
```

<!-- section_id: "ddac5883-8f2e-4d73-bfce-f0f1bd13f185" -->
## 🔑 API Key Management

<!-- section_id: "d2c76ad3-4b05-476f-81cb-8e20f07e276b" -->
### API Key Configuration
```bash
# Context7
CONTEXT7_API_KEY=your_context7_api_key_here

# Tavily Web Search
TAVILY_API_KEY=your_tavily_api_key_here

# GitHub
GITHUB_TOKEN=your_github_token_here
```

<!-- section_id: "ec9e456d-52e3-4ee8-b652-050d2deea8c3" -->
### Security Best Practices
1. **Environment Variables**: Use env vars for sensitive data
2. **Key Rotation**: Regularly rotate API keys
3. **Access Control**: Limit key access to necessary environments
4. **Monitoring**: Monitor key usage and access

<!-- section_id: "e9c5b704-3378-484f-a5bd-0b17be23190f" -->
## 🛠️ Server Configurations

<!-- section_id: "f5ef7c16-0a25-4d0f-b649-5ae20a6126d3" -->
### Browser Automation Servers

#### Chrome DevTools
```json
{
  "name": "chrome-devtools",
  "command": "npx",
  "args": ["-y", "chrome-devtools-mcp@latest"],
  "category": "browser_automation",
  "dependencies": ["chrome", "node"]
}
```

#### Playwright
```json
{
  "name": "playwright",
  "command": "npx",
  "args": ["-y", "@playwright/mcp@latest", "--browser", "chromium"],
  "category": "browser_automation",
  "dependencies": ["node", "browsers"]
}
```

#### Browser
```json
{
  "name": "browser",
  "command": "npx",
  "args": ["@agent-infra/mcp-server-browser"],
  "category": "browser_automation",
  "dependencies": ["browser"]
}
```

<!-- section_id: "fb6ee9d7-5ec5-45e4-9ee3-89b5378c6305" -->
### Search & Research Servers

#### Web Search (Tavily)
```json
{
  "name": "web-search",
  "command": "npx",
  "args": ["tavily-mcp"],
  "env": {
    "TAVILY_API_KEY": "your_tavily_api_key_here"
  },
  "category": "search",
  "dependencies": ["node"]
}
```

#### GitHub Search
```json
{
  "name": "github-search",
  "command": "npx",
  "args": ["github-mcp-server"],
  "env": {
    "GITHUB_TOKEN": "your_github_token_here"
  },
  "category": "search",
  "dependencies": ["node"]
}
```

#### Context7 (Local)
```json
{
  "name": "context7-local",
  "command": "npx",
  "args": ["-y", "@upstash/context7-mcp", "--api-key", "your_context7_api_key_here"],
  "category": "documentation",
  "dependencies": ["node"]
}
```

#### Context7 (Remote)
```json
{
  "name": "context7-remote",
  "mcp_type": "remote",
  "mcp_url": "https://mcp.context7.com/mcp",
  "mcp_headers": {
    "CONTEXT7_API_KEY": "your_context7_api_key_here"
  },
  "category": "documentation",
  "dependencies": ["curl"]
}
```

<!-- section_id: "201c095f-bba8-4ce3-ab89-da4110f090fa" -->
### System Integration Servers

#### Filesystem
```json
{
  "name": "filesystem",
  "command": "npx",
  "args": ["@modelcontextprotocol/server-filesystem", "/home/dawson/dawson-workspace/code/lang-trak-in-progress"],
  "category": "filesystem",
  "dependencies": ["node"]
}
```

#### Slack
```json
{
  "name": "slack",
  "command": "npx",
  "args": ["@modelcontextprotocol/server-slack"],
  "env": {
    "SLACK_BOT_TOKEN": "xoxb-your-slack-bot-token"
  },
  "category": "communication",
  "dependencies": ["node"]
}
```

#### PostgreSQL
```json
{
  "name": "postgres",
  "command": "npx",
  "args": ["@modelcontextprotocol/server-postgres"],
  "env": {
    "POSTGRES_CONNECTION_STRING": "postgresql://user:password@localhost:5432/firebase_config"
  },
  "category": "database",
  "dependencies": ["node", "postgresql"]
}
```

<!-- section_id: "f31b1202-2c27-4ae5-ab15-a76d39c0ac2b" -->
## 🔄 Configuration Management

<!-- section_id: "382c003b-c0f4-43b2-ad40-60c70961de1a" -->
### Adding New Servers
```python
# Add custom server to environment
from mcp_config_manager import MCPConfigManager, MCPServerConfig, MCPEnvironment

custom_server = MCPServerConfig(
    name="my-custom-server",
    command="python3",
    args=["my_server.py"],
    env={"API_KEY": "my-key"},
    enabled=True,
    category="custom"
)

manager = MCPConfigManager()
manager.add_custom_server(custom_server, MCPEnvironment.DEVELOPMENT)
```

<!-- section_id: "ddf14b22-7fda-4f7e-82e8-954d3aebf77a" -->
### Updating Server Configuration
```bash
# Update server in specific environment
python3 scripts/mcp_config_manager.py update-server --environment development --server context7 --enabled true

# Update global environment variables
python3 scripts/mcp_config_manager.py update-global-env --environment production --key LOG_LEVEL --value info
```

<!-- section_id: "da3fce30-3e46-49d3-953f-5fc37254ee0c" -->
### Switching Configurations
```bash
# Switch to different environment
python3 scripts/mcp-cli.py deploy production

# Switch Context7 to local
python3 scripts/context7-setup.py setup-local

# Switch Context7 to remote
python3 scripts/context7-setup.py setup-remote
```

<!-- section_id: "7358f4f3-9779-4a02-982b-bc6a3c83b69c" -->
## 📊 Monitoring and Health Checks

<!-- section_id: "4a2a6244-aa41-4cc2-90b0-0ebd30b2504b" -->
### Health Check Commands
```bash
# Overall MCP system health
python3 scripts/mcp-cli.py health

# Context7 specific status
python3 scripts/context7-setup.py status

# Validate configuration
python3 scripts/mcp-cli.py validate development
```

<!-- section_id: "2a322460-4c38-45d6-aa48-d072cd802c22" -->
### Monitoring Configuration
```json
{
  "health_check": {
    "interval_seconds": 300,
    "timeout_seconds": 30,
    "retry_count": 3
  },
  "logging": {
    "level": "INFO",
    "file": "backups/mcp/mcp.log",
    "max_size_mb": 10,
    "backup_count": 5
  }
}
```

<!-- section_id: "a1fe92c5-c723-4904-9ce8-0e0d22024fcb" -->
## 🚨 Troubleshooting

<!-- section_id: "e652a516-e070-4933-9cab-de42fc1456d6" -->
### Common Issues and Solutions

#### Server Won't Start
```bash
# Check dependencies
python3 scripts/mcp-cli.py health

# Check specific server
python3 scripts/context7-setup.py status

# Restart server
python3 scripts/mcp-cli.py restart development
```

#### Configuration Errors
```bash
# Validate configuration
python3 scripts/mcp-cli.py validate development

# Check configuration syntax
python3 -m json.tool config/mcp/development.json
```

#### API Key Issues
```bash
# Check API key configuration
grep -r "API_KEY" config/mcp/

# Test API connectivity
python3 scripts/context7-setup.py status
```

<!-- section_id: "718d85e2-34f7-43e5-958f-8d748081d67b" -->
### Debug Information
```bash
# View logs
tail -f backups/mcp/mcp.log

# Check system status
python3 scripts/mcp-cli.py status

# Generate detailed report
python3 scripts/mcp-cli.py report
```

<!-- section_id: "f0ada26e-d8d9-4ef5-b10c-ec1e422e40e0" -->
## 🎯 Best Practices

<!-- section_id: "8dd909a1-bcce-4630-9aba-0fa641cbe5f4" -->
### Development
- Use local servers for better performance
- Enable debug logging
- Test both local and remote configurations
- Keep configurations in version control

<!-- section_id: "03163e7a-aaa2-4344-8759-62d4fa6a90c6" -->
### Production
- Use remote servers for simplicity
- Enable monitoring and alerting
- Regular configuration backups
- Secure API key management

<!-- section_id: "3367507a-c5d3-41c7-84da-206feeb5ac36" -->
### Testing
- Use minimal server configurations
- Fast startup times
- Reliable test environments
- Automated health checks

<!-- section_id: "a940e857-747a-4527-a0d2-eaf407f1706d" -->
## 📚 Additional Resources

- **Complete Setup Guide**: [CONTEXT7_CLAUDE_SETUP.md](CONTEXT7_CLAUDE_SETUP.md)
- **Quick Reference**: [CONTEXT7_QUICK_REFERENCE.md](CONTEXT7_QUICK_REFERENCE.md)
- **MCP System Guide**: [../../../../MCP_SYSTEM_GUIDE.md](../../../../MCP_SYSTEM_GUIDE.md)
- **Configuration Examples**: `config/mcp/examples/`

---

**This configuration guide ensures consistent MCP setup across all environments and provides comprehensive management capabilities for all AI agents.**
