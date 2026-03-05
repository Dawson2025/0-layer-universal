---
resource_id: "b3554b49-f340-4edc-b0f1-d97dfbc93685"
resource_type: "document"
resource_name: "MCP_SYSTEM_GUIDE"
---
# MCP Configuration Management System

<!-- section_id: "f40a86bd-7b4f-48fb-97d1-06a623637723" -->
## Overview

This project now includes a comprehensive **Model Context Protocol (MCP) Configuration Management System** that serves as a single source of truth for all AI agent configurations across different environments.

<!-- section_id: "ff7873ba-bf4a-47ad-9bdd-864373d1950a" -->
## 🎯 Key Features

- **Centralized Configuration**: All MCP server configurations in one place
- **Environment Management**: Separate configurations for development, production, and testing
- **Automated Deployment**: Scripts to deploy and manage MCP configurations
- **Health Monitoring**: Built-in health checks and status monitoring
- **Backup & Recovery**: Automatic backup of configurations
- **Easy CLI Interface**: Simple command-line tools for management

<!-- section_id: "798d2955-21a4-4703-9629-e13c111895d8" -->
## 🚀 Quick Start

<!-- section_id: "3c352194-1e69-403a-9497-ce4b9f190758" -->
### 1. Initial Setup
```bash
# Set up the complete MCP system
python3 automation/scripts/mcp_manager.py

# Verify setup
# (Health check script to be implemented)
```

<!-- section_id: "459cefa0-7c60-4380-88e5-24715af79620" -->
### 2. Deploy Configuration
```bash
# Deploy development environment (default)
python3 scripts/mcp-cli.py deploy development

# Deploy production environment
python3 scripts/mcp-cli.py deploy production

# Deploy testing environment
python3 scripts/mcp-cli.py deploy testing
```

<!-- section_id: "be681c8e-fe01-41a4-adc0-d2f4f8339122" -->
### 3. Check Status
```bash
# Show system status
python3 scripts/mcp-cli.py status

# Run health check
python3 scripts/mcp-cli.py health

# Generate report
python3 scripts/mcp-cli.py report
```

<!-- section_id: "e2064855-f2f2-4bab-886b-4c2441669e63" -->
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

<!-- section_id: "5c2542ee-798a-4c62-a174-2aa945d233cb" -->
## 🔧 Available MCP Servers

<!-- section_id: "b4d6eca7-a888-405c-a64e-3414338411f3" -->
### Browser Automation
- **chrome-devtools**: Chrome DevTools integration for debugging
- **playwright**: Cross-browser testing and automation
- **browser**: Simple browser automation

<!-- section_id: "64fdc985-cef0-4f3e-a79e-715bd41a7b93" -->
### Search & Research
- **web-search**: Tavily web search integration
- **github-search**: GitHub repository search
- **context7**: Documentation and context management (local and remote options)

<!-- section_id: "0d48961a-7c78-4f51-8595-0ebc793a58ed" -->
### System Integration
- **filesystem**: File system access and management
- **slack**: Slack integration for notifications
- **postgres**: PostgreSQL database integration

<!-- section_id: "fef28421-24fa-4487-9ee5-941236de2ed7" -->
## 🌍 Environment Configurations

<!-- section_id: "7b065c1e-03eb-48c4-b8e0-99e4692dd91a" -->
### Development Environment
**Purpose**: Full debugging and development tools
**Servers**: chrome-devtools, playwright, browser, web-search, github-search, filesystem, context7
**Features**:
- All browser automation tools
- Complete search capabilities
- Filesystem access
- Documentation tools
- Debug logging enabled

<!-- section_id: "0d6bfdb3-5301-403d-b010-19f8ff015692" -->
### Production Environment
**Purpose**: Essential tools for production use
**Servers**: web-search, github-search, filesystem, slack, postgres
**Features**:
- Essential search tools only
- Slack notifications
- Database integration
- Optimized for performance
- Minimal resource usage

<!-- section_id: "ce711f1e-16a6-459c-a7e7-dd359125cf09" -->
### Testing Environment
**Purpose**: Automated testing and validation
**Servers**: playwright, browser, filesystem
**Features**:
- Browser automation for testing
- Filesystem access
- Minimal resource usage
- Fast startup times

<!-- section_id: "cde1829f-178a-4e44-9ecc-a3136a2e5540" -->
## 🛠️ Management Commands

<!-- section_id: "b5b16ff3-17c2-451b-8357-216ebd870ef1" -->
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

<!-- section_id: "fa04e393-5cfb-4e9b-92b0-93b4f78bf92d" -->
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

<!-- section_id: "ce5ada66-03ae-44ff-ba1b-1ba70b7d5165" -->
## 📊 Monitoring and Health Checks

<!-- section_id: "9243a12c-ee41-4e35-bdd9-eab73d81bdad" -->
### Automatic Monitoring
- **Health Checks**: Every 5 minutes
- **Server Status**: Real-time tracking
- **Configuration Validation**: Pre-deployment checks
- **Logging**: Comprehensive logging with rotation

<!-- section_id: "c5c893c4-52cc-4831-ab0e-ab56cca2d235" -->
### Health Check Features
```bash
# Run comprehensive health check
python3 scripts/mcp-cli.py health

# Check specific environment
python3 scripts/mcp-cli.py validate development
```

<!-- section_id: "64ab1d5c-789f-45ae-893c-eb2831380cbd" -->
### Status Information
- Active server count
- Environment status
- Configuration validity
- Dependency checks
- Performance metrics

<!-- section_id: "e8445d0e-2249-415d-901d-67bd2ceb23e3" -->
## 🔒 Security and Configuration

<!-- section_id: "63525267-523a-497e-b82b-7f20ab277120" -->
### API Key Management
- Environment-specific API keys
- Placeholder values for production setup
- Secure storage recommendations
- Key rotation support

<!-- section_id: "f6aaf300-d2d8-45a4-9af1-7d9494c94d2f" -->
### Configuration Security
- Separate configurations per environment
- No hardcoded production keys
- Environment variable support
- Backup and recovery

<!-- section_id: "433ad019-cd65-4f62-82b4-5331c40898c3" -->
## 📈 Backup and Recovery

<!-- section_id: "fd09b669-b552-4179-af62-fdaf15a33ca0" -->
### Automatic Backups
- Configuration backups before each deployment
- Timestamped backup files
- Easy restoration process
- Configuration history tracking

<!-- section_id: "da703233-32b4-4800-8970-45d0ecae2e15" -->
### Manual Backup
```bash
# Backup current configuration
cp .mcp.json backups/mcp/manual_backup_$(date +%Y%m%d_%H%M%S).json

# Restore from backup
cp backups/mcp/backup_file.json .mcp.json
```

<!-- section_id: "db39d3f3-50ac-4f5f-9ac0-d50a45682790" -->
## 🚨 Troubleshooting

<!-- section_id: "dd7eed33-96e4-473f-bb49-9b9cd6aabef5" -->
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

<!-- section_id: "82ead57d-f2d3-4314-91a8-83f2623d2cd7" -->
### Debug Information
- Check logs: `tail -f backups/mcp/mcp.log`
- Run health check: `python3 scripts/mcp-cli.py health`
- Generate report: `python3 scripts/mcp-cli.py report`

<!-- section_id: "c794fc19-9288-42fa-9c16-dd482c9322bb" -->
## 🔄 Workflow Integration

<!-- section_id: "f1c9a39d-5304-492a-ba79-7027749abe13" -->
### Development Workflow
1. **Setup**: `python3 scripts/mcp-cli.py setup`
2. **Deploy Dev**: `python3 scripts/mcp-cli.py deploy development`
3. **Develop**: Use MCP tools for development
4. **Test**: `python3 scripts/mcp-cli.py deploy testing`
5. **Deploy Prod**: `python3 scripts/mcp-cli.py deploy production`

<!-- section_id: "e74f2779-afc3-4c77-a57a-a19f23327527" -->
### CI/CD Integration
```bash
# In your CI/CD pipeline
python3 scripts/mcp-cli.py validate production
python3 scripts/mcp-cli.py deploy production
python3 scripts/mcp-cli.py health
```

<!-- section_id: "d768e513-a9b7-4a24-bbdb-bc7a766a6bb5" -->
## 📚 Advanced Usage

<!-- section_id: "bfd02563-e349-46cd-a303-aa7cc079b0f6" -->
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

<!-- section_id: "01309c42-371d-41c1-93e4-fcc7710d9384" -->
### Environment Synchronization
```python
from mcp_deployer import MCPDeployer, MCPEnvironment

deployer = MCPDeployer(config_manager)
deployer.sync_across_environments([
    MCPEnvironment.DEVELOPMENT,
    MCPEnvironment.PRODUCTION
])
```

<!-- section_id: "a882c346-9931-406d-86b1-58e1014757b4" -->
## 🎉 Benefits

<!-- section_id: "789d5ae0-bebc-4b43-9fba-a0599a32afbf" -->
### For Developers
- **Single Source of Truth**: All MCP configurations in one place
- **Easy Management**: Simple CLI commands for all operations
- **Environment Isolation**: Separate configs for different environments
- **Automated Deployment**: No manual configuration management

<!-- section_id: "1022aece-107e-429a-9fcd-c13700b1a593" -->
### For Operations
- **Health Monitoring**: Built-in monitoring and alerting
- **Backup & Recovery**: Automatic backup and easy restoration
- **Scalability**: Easy to add new servers and environments
- **Documentation**: Comprehensive documentation and examples

<!-- section_id: "2d601d2b-d5fa-42a7-89a6-e0153237084b" -->
### For AI Agents
- **Consistent Configuration**: Same tools available across environments
- **Easy Access**: Simple commands to start/stop/configure
- **Reliability**: Health checks ensure servers are running
- **Flexibility**: Easy to add new MCP servers as needed

<!-- section_id: "74688183-3d84-44b0-9cb9-991393b67e9e" -->
## 🔧 Context7 MCP Server Setup

Context7 provides documentation and context management capabilities. You have two connection options:

<!-- section_id: "8daee3bd-3bd4-4ca8-b49e-8eca912c0c19" -->
### Local Server (Recommended for Development)
```bash
# Set up local Context7 MCP server
python3 scripts/context7-setup.py setup-local

# Check status
python3 scripts/context7-setup.py status
```

<!-- section_id: "00e82356-7cdc-4e4f-9504-f52b3c8df3f5" -->
### Remote Server (Recommended for Production)
```bash
# Set up remote Context7 MCP server
python3 scripts/context7-setup.py setup-remote

# Check status
python3 scripts/context7-setup.py status
```

<!-- section_id: "fa9b94d3-39b4-465e-a3b4-244ef3da1122" -->
### Hybrid Setup (Both Options)
```bash
# Set up both local and remote options
python3 scripts/context7-setup.py setup-hybrid
```

<!-- section_id: "ab894ec3-da55-47a3-bfe4-55a96ab40f5c" -->
### Context7 Configuration Files
- **Local**: `config/mcp/examples/context7-local.json`
- **Remote**: `config/mcp/examples/context7-remote.json`
- **Hybrid**: `config/mcp/examples/context7-hybrid.json`

<!-- section_id: "8c496b5b-af88-4f8f-8d2b-adb447a4d24e" -->
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

<!-- section_id: "14b64d04-6260-46c9-b0d1-bd7509c3d5c0" -->
## 🚀 Next Steps

1. **Run Setup**: `python3 scripts/mcp-cli.py setup`
2. **Deploy Development**: `python3 scripts/mcp-cli.py deploy development`
3. **Set up Context7**: `python3 scripts/context7-setup.py setup-local`
4. **Check Status**: `python3 scripts/mcp-cli.py status`
5. **Explore Tools**: Use the MCP servers for your AI agent tasks
6. **Customize**: Add your own MCP servers as needed

<!-- section_id: "0f59d00e-af96-4c4f-823e-1df27d33d461" -->
## 📞 Support

- **Health Check**: `python3 scripts/mcp-cli.py health`
- **Documentation**: Check `config/mcp/README.md`
- **Logs**: Review `backups/mcp/mcp.log`
- **Status**: `python3 scripts/mcp-cli.py status`

This MCP system provides a robust, scalable, and easy-to-use foundation for managing AI agent configurations across all your environments!
