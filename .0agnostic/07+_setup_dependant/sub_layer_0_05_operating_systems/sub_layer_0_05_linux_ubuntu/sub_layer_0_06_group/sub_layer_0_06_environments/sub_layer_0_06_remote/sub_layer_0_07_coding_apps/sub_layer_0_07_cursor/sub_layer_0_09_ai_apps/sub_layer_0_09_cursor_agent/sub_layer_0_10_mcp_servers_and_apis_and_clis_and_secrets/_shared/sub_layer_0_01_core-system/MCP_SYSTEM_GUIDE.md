---
resource_id: "be968aeb-93ea-4908-aaac-0f5d713a79d9"
resource_type: "document"
resource_name: "MCP_SYSTEM_GUIDE"
---
# MCP Configuration Management System

<!-- section_id: "8cdb268d-a133-4eb1-8e7c-cbd555854af5" -->
## Overview

This project now includes a comprehensive **Model Context Protocol (MCP) Configuration Management System** that serves as a single source of truth for all AI agent configurations across different environments.

<!-- section_id: "d9f3b8c9-53f3-40fc-b87a-3cb72c36cd58" -->
## 🎯 Key Features

- **Centralized Configuration**: All MCP server configurations in one place
- **Environment Management**: Separate configurations for development, production, and testing
- **Automated Deployment**: Scripts to deploy and manage MCP configurations
- **Health Monitoring**: Built-in health checks and status monitoring
- **Backup & Recovery**: Automatic backup of configurations
- **Easy CLI Interface**: Simple command-line tools for management

<!-- section_id: "1f2e16d8-0c11-4f85-abc6-3fed09e1aa06" -->
## 🚀 Quick Start

<!-- section_id: "88205bf3-4937-4bbe-8ca1-4466cd8fef1c" -->
### 1. Initial Setup
```bash
# Set up the complete MCP system
python3 automation/scripts/mcp_manager.py

# Verify setup
# (Health check script to be implemented)
```

<!-- section_id: "28480718-122b-4d9b-85d2-b1533e52f0ea" -->
### 2. Deploy Configuration
```bash
# Deploy development environment (default)
python3 scripts/mcp-cli.py deploy development

# Deploy production environment
python3 scripts/mcp-cli.py deploy production

# Deploy testing environment
python3 scripts/mcp-cli.py deploy testing
```

<!-- section_id: "1ba6cc92-6e5f-4540-989e-db9e46abc289" -->
### 3. Check Status
```bash
# Show system status
python3 scripts/mcp-cli.py status

# Run health check
python3 scripts/mcp-cli.py health

# Generate report
python3 scripts/mcp-cli.py report
```

<!-- section_id: "38a28ec8-e9d9-45ad-aa00-67b538816e94" -->
## 📁 Directory Structure

```
config/mcp/
├── mcp-system.json          # Main system configuration
├── development.json         # Development environment config
├── production.json          # Production environment config
├── testing.json            # Testing environment config
├── monitoring.json         # Monitoring configuration
└── README.md               # Detailed documentation

scripts/
├── mcp_config_manager.py   # Configuration management
├── mcp_deployer.py         # Deployment automation
├── mcp-cli.py             # Simple CLI interface
├── setup_mcp_system.py    # System setup script
├── mcp-manage.sh          # Management wrapper script
└── mcp-health-check.sh    # Health check script
```

<!-- section_id: "7a9445a8-5b62-4fad-ac71-1ddefe52f56b" -->
## 🔧 Available MCP Servers

<!-- section_id: "39357a6b-2a31-4849-b569-837aaccb2bec" -->
### Browser Automation
- **chrome-devtools**: Chrome DevTools integration for debugging
- **playwright**: Cross-browser testing and automation
- **browser**: Simple browser automation

<!-- section_id: "77184dcf-5799-41a7-8071-40f863539709" -->
### Search & Research
- **web-search**: Tavily web search integration
- **github-search**: GitHub repository search
- **context7**: Documentation and context management (local and remote options)

<!-- section_id: "c9ce8590-8f75-439a-8788-7f880798e73f" -->
### System Integration
- **filesystem**: File system access and management
- **slack**: Slack integration for notifications
- **postgres**: PostgreSQL database integration

<!-- section_id: "31cbebf8-4a16-46c3-9b74-70c509a8bdf6" -->
## 🌍 Environment Configurations

<!-- section_id: "3df7cbe7-e035-41a8-b26a-8e9a57295739" -->
### Development Environment
**Purpose**: Full debugging and development tools
**Servers**: chrome-devtools, playwright, browser, web-search, github-search, filesystem, context7
**Features**:
- All browser automation tools
- Complete search capabilities
- Filesystem access
- Documentation tools
- Debug logging enabled

<!-- section_id: "73757463-de07-4d9b-96fb-55ec742dca99" -->
### Production Environment
**Purpose**: Essential tools for production use
**Servers**: web-search, github-search, filesystem, slack, postgres
**Features**:
- Essential search tools only
- Slack notifications
- Database integration
- Optimized for performance
- Minimal resource usage

<!-- section_id: "a0de8ae3-56ca-4da7-9765-0b9a55106d06" -->
### Testing Environment
**Purpose**: Automated testing and validation
**Servers**: playwright, browser, filesystem
**Features**:
- Browser automation for testing
- Filesystem access
- Minimal resource usage
- Fast startup times

<!-- section_id: "76795e41-febb-4924-9e9f-1440941e7206" -->
## 🛠️ Management Commands

<!-- section_id: "3dff3c6c-3399-4fd8-a0ca-ba29bc0d0703" -->
### CLI Interface
```bash
# Setup and initialization
python3 scripts/mcp-cli.py setup

# Environment management
python3 scripts/mcp-cli.py deploy <environment>
python3 scripts/mcp-cli.py start <environment>
python3 scripts/mcp-cli.py stop <environment>
python3 scripts/mcp-cli.py restart <environment>

# Status and monitoring
python3 scripts/mcp-cli.py status
python3 scripts/mcp-cli.py health
python3 scripts/mcp-cli.py report

# Configuration management
python3 scripts/mcp-cli.py validate <environment>
python3 scripts/mcp-cli.py list
```

<!-- section_id: "ad246d57-bc80-4a9d-b49b-d09ee2c10255" -->
### Advanced Management
```bash
# Direct configuration management
python3 scripts/mcp_config_manager.py generate --environment development
python3 scripts/mcp_config_manager.py validate --environment production
python3 scripts/mcp_config_manager.py list

# Direct deployment management
python3 scripts/mcp_deployer.py deploy --environment development
python3 scripts/mcp_deployer.py status
python3 scripts/mcp_deployer.py report
```

<!-- section_id: "4580d05a-8710-4729-884d-3ff16e95d147" -->
## 📊 Monitoring and Health Checks

<!-- section_id: "9c52b305-53fe-4c72-937c-8da2abd00baf" -->
### Automatic Monitoring
- **Health Checks**: Every 5 minutes
- **Server Status**: Real-time tracking
- **Configuration Validation**: Pre-deployment checks
- **Logging**: Comprehensive logging with rotation

<!-- section_id: "1817b002-0ff6-47df-a2c3-53ef5536320f" -->
### Health Check Features
```bash
# Run comprehensive health check
python3 scripts/mcp-cli.py health

# Check specific environment
python3 scripts/mcp-cli.py validate development
```

<!-- section_id: "34e7ea95-25a4-4e6c-830c-59875e5d20fc" -->
### Status Information
- Active server count
- Environment status
- Configuration validity
- Dependency checks
- Performance metrics

<!-- section_id: "e9147800-8406-48dd-9177-ec68c31d0244" -->
## 🔒 Security and Configuration

<!-- section_id: "1d31fc56-14b9-4912-a630-4e60bdd67c6f" -->
### API Key Management
- Environment-specific API keys
- Placeholder values for production setup
- Secure storage recommendations
- Key rotation support

<!-- section_id: "e919ecda-720a-4fc7-83d9-30a0b8633c88" -->
### Configuration Security
- Separate configurations per environment
- No hardcoded production keys
- Environment variable support
- Backup and recovery

<!-- section_id: "bc136937-a1d3-4d27-b0fe-71e37cc212f8" -->
## 📈 Backup and Recovery

<!-- section_id: "047f0ab4-edd8-4d9a-a12a-6b8573bf58b2" -->
### Automatic Backups
- Configuration backups before each deployment
- Timestamped backup files
- Easy restoration process
- Configuration history tracking

<!-- section_id: "e285ba7b-f422-4f28-b7ac-126248b9b769" -->
### Manual Backup
```bash
# Backup current configuration
cp .mcp.json backups/mcp/manual_backup_$(date +%Y%m%d_%H%M%S).json

# Restore from backup
cp backups/mcp/backup_file.json .mcp.json
```

<!-- section_id: "e792c0f2-4f84-4117-88f8-eaaeded5f64e" -->
## 🚨 Troubleshooting

<!-- section_id: "145153bc-b532-4df6-bb3a-3937f9030ea5" -->
### Common Issues

1. **Server Won't Start**
   ```bash
   # Check health
   python3 scripts/mcp-cli.py health
   
   # Validate configuration
   python3 scripts/mcp-cli.py validate development
   ```

2. **Missing Dependencies**
   ```bash
   # Reinstall dependencies
   python3 scripts/setup_mcp_system.py
   ```

3. **Configuration Errors**
   ```bash
   # Check configuration syntax
   python3 scripts/mcp-cli.py validate development
   ```

<!-- section_id: "c66933c2-5db0-424d-acc9-8b2817f2627f" -->
### Debug Information
- Check logs: `tail -f backups/mcp/mcp.log`
- Run health check: `python3 scripts/mcp-cli.py health`
- Generate report: `python3 scripts/mcp-cli.py report`

<!-- section_id: "8a2c2fb4-ef5c-4930-ba09-9b78e6a75749" -->
## 🔄 Workflow Integration

<!-- section_id: "3699b0cd-1f4b-46d8-8d33-49afcc886352" -->
### Development Workflow
1. **Setup**: `python3 scripts/mcp-cli.py setup`
2. **Deploy Dev**: `python3 scripts/mcp-cli.py deploy development`
3. **Develop**: Use MCP tools for development
4. **Test**: `python3 scripts/mcp-cli.py deploy testing`
5. **Deploy Prod**: `python3 scripts/mcp-cli.py deploy production`

<!-- section_id: "ae9d9642-1402-4f54-b3fa-da36e9e05d69" -->
### CI/CD Integration
```bash
# In your CI/CD pipeline
python3 scripts/mcp-cli.py validate production
python3 scripts/mcp-cli.py deploy production
python3 scripts/mcp-cli.py health
```

<!-- section_id: "f82863b0-0441-4fef-97df-5c57ebce3847" -->
## 📚 Advanced Usage

<!-- section_id: "f05c928b-8e6c-46ed-a589-49a38c758f46" -->
### Custom Server Configuration
```python
from mcp_config_manager import MCPConfigManager, MCPServerConfig, MCPEnvironment

# Add custom server
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

<!-- section_id: "aaaa3e6f-ca81-4599-9461-986d89b93380" -->
### Environment Synchronization
```python
from mcp_deployer import MCPDeployer, MCPEnvironment

deployer = MCPDeployer(config_manager)
deployer.sync_across_environments([
    MCPEnvironment.DEVELOPMENT,
    MCPEnvironment.PRODUCTION
])
```

<!-- section_id: "32f34a48-2cae-46a3-9379-9326bc28f4f1" -->
## 🎉 Benefits

<!-- section_id: "1fc0534e-fc58-434f-b42c-63ea99cffc75" -->
### For Developers
- **Single Source of Truth**: All MCP configurations in one place
- **Easy Management**: Simple CLI commands for all operations
- **Environment Isolation**: Separate configs for different environments
- **Automated Deployment**: No manual configuration management

<!-- section_id: "8abb2ce8-6bbb-4ed0-840f-4f52f1e7ba16" -->
### For Operations
- **Health Monitoring**: Built-in monitoring and alerting
- **Backup & Recovery**: Automatic backup and easy restoration
- **Scalability**: Easy to add new servers and environments
- **Documentation**: Comprehensive documentation and examples

<!-- section_id: "42de1a41-d504-462b-978c-516444954daa" -->
### For AI Agents
- **Consistent Configuration**: Same tools available across environments
- **Easy Access**: Simple commands to start/stop/configure
- **Reliability**: Health checks ensure servers are running
- **Flexibility**: Easy to add new MCP servers as needed

<!-- section_id: "c6b8bccb-f188-4b52-8c28-288950ef1875" -->
## 🔧 Context7 MCP Server Setup

Context7 provides documentation and context management capabilities. You have two connection options:

<!-- section_id: "6d99e535-9273-44c1-a2e3-f71270d40be1" -->
### Local Server (Recommended for Development)
```bash
# Set up local Context7 MCP server
python3 scripts/context7-setup.py setup-local

# Check status
python3 scripts/context7-setup.py status
```

<!-- section_id: "f4cb92c6-7cbc-4707-b94b-5d88f9e67006" -->
### Remote Server (Recommended for Production)
```bash
# Set up remote Context7 MCP server
python3 scripts/context7-setup.py setup-remote

# Check status
python3 scripts/context7-setup.py status
```

<!-- section_id: "03a52a73-88ce-41b9-a0ee-bc92876d9af8" -->
### Hybrid Setup (Both Options)
```bash
# Set up both local and remote options
python3 scripts/context7-setup.py setup-hybrid
```

<!-- section_id: "51fc82c5-93f6-4d9b-a7d8-b31cc2673e6d" -->
### Context7 Configuration Files
- **Local**: `config/mcp/examples/context7-local.json`
- **Remote**: `config/mcp/examples/context7-remote.json`
- **Hybrid**: `config/mcp/examples/context7-hybrid.json`

<!-- section_id: "2f55867c-a8e9-4cef-a4ab-8e0d81709e31" -->
### Claude Code Integration
For direct integration with Claude Code:

**Remote Server (Production):**
```bash
claude mcp add --transport http context7 https://mcp.context7.com/mcp --header "CONTEXT7_API_KEY: YOUR_CONTEXT7_API_KEY"
```

**Local Server (Development):**
```bash
claude mcp add context7 -- npx -y @upstash/context7-mcp --api-key YOUR_CONTEXT7_API_KEY
```

📚 **Complete Setup Guide**: See `docs/CONTEXT7_CLAUDE_SETUP.md` for detailed instructions.

<!-- section_id: "87b5dd80-1168-41d0-be3c-ccd01ca58273" -->
## 🚀 Next Steps

1. **Run Setup**: `python3 scripts/mcp-cli.py setup`
2. **Deploy Development**: `python3 scripts/mcp-cli.py deploy development`
3. **Set up Context7**: `python3 scripts/context7-setup.py setup-local`
4. **Check Status**: `python3 scripts/mcp-cli.py status`
5. **Explore Tools**: Use the MCP servers for your AI agent tasks
6. **Customize**: Add your own MCP servers as needed

<!-- section_id: "3ef9545d-80a6-43e2-afac-d913ff72089e" -->
## 📞 Support

- **Health Check**: `python3 scripts/mcp-cli.py health`
- **Documentation**: Check `config/mcp/README.md`
- **Logs**: Review `backups/mcp/mcp.log`
- **Status**: `python3 scripts/mcp-cli.py status`

This MCP system provides a robust, scalable, and easy-to-use foundation for managing AI agent configurations across all your environments!
