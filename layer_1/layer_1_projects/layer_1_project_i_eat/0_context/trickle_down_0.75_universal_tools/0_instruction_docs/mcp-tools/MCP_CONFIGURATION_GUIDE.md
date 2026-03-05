---
resource_id: "0fd15fbb-2813-4fed-bd9b-787c4f10011a"
resource_type: "document"
resource_name: "MCP_CONFIGURATION_GUIDE"
---
# MCP Configuration Guide - Universal Tools

<!-- section_id: "e92b3aa2-9755-40ba-85d8-921bbbdd233f" -->
## Overview

This guide provides comprehensive instructions for configuring and managing MCP (Model Context Protocol) tools across all environments in the lang-trak-in-progress project.

<!-- section_id: "40447ea4-5b7e-4786-892b-06e6c5ec67b2" -->
## 🎯 Configuration Philosophy

The MCP system follows these principles:
- **Single Source of Truth**: All configurations centralized
- **Environment Isolation**: Separate configs for dev/prod/testing
- **Automated Management**: Scripts handle deployment and updates
- **Easy Switching**: Simple commands to change configurations

<!-- section_id: "3c208bfa-aef7-4e86-9374-01d809ebbfe6" -->
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

<!-- section_id: "8edc289d-6a90-42e9-a114-befea4e30e2f" -->
## 🔧 Environment Configurations

<!-- section_id: "813185ff-a6f3-4655-b680-3df0735d8c75" -->
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

<!-- section_id: "d2569aa4-4743-456e-bb18-33583b5785a5" -->
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

<!-- section_id: "462b8193-33f0-4d72-8e0d-e554e05a796b" -->
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

<!-- section_id: "0b1bc4d6-c9b3-4d8f-a328-2172844ee9dc" -->
## 🚀 Setup Commands

<!-- section_id: "f0281e4b-36a5-4e2d-a211-6dd57a6feec6" -->
### Initial Setup
```bash
# Set up complete MCP system
python3 scripts/mcp-cli.py setup

# Verify setup
python3 scripts/mcp-cli.py health
```

<!-- section_id: "f5d559e6-bb5f-4ce1-a36b-5bdec2dddc3f" -->
### Environment Deployment
```bash
# Deploy development environment
python3 scripts/mcp-cli.py deploy development

# Deploy production environment
python3 scripts/mcp-cli.py deploy production

# Deploy testing environment
python3 scripts/mcp-cli.py deploy testing
```

<!-- section_id: "a3c27c4c-fc3e-4308-be25-65768b5797c4" -->
### Context7 Setup
```bash
# Set up local Context7 server
python3 scripts/context7-setup.py setup-local

# Set up remote Context7 server
python3 scripts/context7-setup.py setup-remote

# Set up both options
python3 scripts/context7-setup.py setup-hybrid
```

<!-- section_id: "e39ce91f-f756-4b7e-8b0a-9f19e7c4472c" -->
## 🔑 API Key Management

<!-- section_id: "fa719621-f861-4c25-b78d-f768c9024abf" -->
### API Key Configuration
```bash
# Context7
CONTEXT7_API_KEY=your_context7_api_key_here

# Tavily Web Search
TAVILY_API_KEY=your_tavily_api_key_here

# GitHub
GITHUB_TOKEN=your_github_token_here
```

<!-- section_id: "6a081106-4319-4ada-90f6-bd5f51813117" -->
### Security Best Practices
1. **Environment Variables**: Use env vars for sensitive data
2. **Key Rotation**: Regularly rotate API keys
3. **Access Control**: Limit key access to necessary environments
4. **Monitoring**: Monitor key usage and access

<!-- section_id: "636c7d49-29c6-4a30-b455-4d27df99118d" -->
## 🛠️ Server Configurations

<!-- section_id: "1d938f22-2fc4-43f2-a988-a3d8cf7e504c" -->
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

<!-- section_id: "09f8e98b-4913-427d-b0e2-8520d9994f0a" -->
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

<!-- section_id: "90afad88-2ece-4344-8b01-942956fca920" -->
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

<!-- section_id: "d1b70e0c-d61e-4310-8b15-82cad1d3296e" -->
## 🔄 Configuration Management

<!-- section_id: "4c5c43ba-1c44-4ab2-aee4-3eb9888ae2f2" -->
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

<!-- section_id: "1666563a-fbe5-4b38-952a-5797bad43521" -->
### Updating Server Configuration
```bash
# Update server in specific environment
python3 scripts/mcp_config_manager.py update-server --environment development --server context7 --enabled true

# Update global environment variables
python3 scripts/mcp_config_manager.py update-global-env --environment production --key LOG_LEVEL --value info
```

<!-- section_id: "d9765198-d77f-47b1-8015-8c92b3a6aa9c" -->
### Switching Configurations
```bash
# Switch to different environment
python3 scripts/mcp-cli.py deploy production

# Switch Context7 to local
python3 scripts/context7-setup.py setup-local

# Switch Context7 to remote
python3 scripts/context7-setup.py setup-remote
```

<!-- section_id: "a768ab3f-334d-43fe-9e11-d56befeaaa8a" -->
## 📊 Monitoring and Health Checks

<!-- section_id: "5e7905d5-872e-48ab-933f-9eff22ed4dd0" -->
### Health Check Commands
```bash
# Overall MCP system health
python3 scripts/mcp-cli.py health

# Context7 specific status
python3 scripts/context7-setup.py status

# Validate configuration
python3 scripts/mcp-cli.py validate development
```

<!-- section_id: "c5cbdd5a-2a15-4d2e-8979-41b8aa025a89" -->
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

<!-- section_id: "48b555e4-5b18-4e2d-bdd7-2ddf20aa7f91" -->
## 🚨 Troubleshooting

<!-- section_id: "559f5967-bbae-4e68-a933-ebc124887d41" -->
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

<!-- section_id: "20fafe06-e220-4d61-b2d9-ad05582f32ba" -->
### Debug Information
```bash
# View logs
tail -f backups/mcp/mcp.log

# Check system status
python3 scripts/mcp-cli.py status

# Generate detailed report
python3 scripts/mcp-cli.py report
```

<!-- section_id: "23ff30ff-852c-444c-baf3-4314c96bcd84" -->
## 🎯 Best Practices

<!-- section_id: "d0a7f7bc-d40b-4d84-ad75-37c443e5c5a3" -->
### Development
- Use local servers for better performance
- Enable debug logging
- Test both local and remote configurations
- Keep configurations in version control

<!-- section_id: "ac27626d-5e18-41f0-984a-c6b5f27ada00" -->
### Production
- Use remote servers for simplicity
- Enable monitoring and alerting
- Regular configuration backups
- Secure API key management

<!-- section_id: "c81b2d71-8cc9-4f46-a863-e5a255ddbf04" -->
### Testing
- Use minimal server configurations
- Fast startup times
- Reliable test environments
- Automated health checks

<!-- section_id: "942083c8-e60f-4614-a4c9-8e9d95856b21" -->
## 📚 Additional Resources

- **Complete Setup Guide**: [CONTEXT7_CLAUDE_SETUP.md](CONTEXT7_CLAUDE_SETUP.md)
- **Quick Reference**: [CONTEXT7_QUICK_REFERENCE.md](CONTEXT7_QUICK_REFERENCE.md)
- **MCP System Guide**: [../../../../MCP_SYSTEM_GUIDE.md](../../../../MCP_SYSTEM_GUIDE.md)
- **Configuration Examples**: `config/mcp/examples/`

---

**This configuration guide ensures consistent MCP setup across all environments and provides comprehensive management capabilities for all AI agents.**
