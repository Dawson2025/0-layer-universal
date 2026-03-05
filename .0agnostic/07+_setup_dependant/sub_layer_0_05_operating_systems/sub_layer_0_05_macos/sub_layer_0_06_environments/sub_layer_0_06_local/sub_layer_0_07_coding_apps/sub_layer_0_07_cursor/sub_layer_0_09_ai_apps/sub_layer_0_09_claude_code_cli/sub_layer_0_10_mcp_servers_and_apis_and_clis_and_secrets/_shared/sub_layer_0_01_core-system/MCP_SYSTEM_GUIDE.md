---
resource_id: "34243259-11c8-4f28-a197-5e188d665b89"
resource_type: "document"
resource_name: "MCP_SYSTEM_GUIDE"
---
# MCP Configuration Management System

<!-- section_id: "32a89c63-2d1f-4afd-a4d4-7c417846528e" -->
## Overview

This project now includes a comprehensive **Model Context Protocol (MCP) Configuration Management System** that serves as a single source of truth for all AI agent configurations across different environments.

<!-- section_id: "e80ea1d7-f205-4793-96c9-67086c639af4" -->
## 🎯 Key Features

- **Centralized Configuration**: All MCP server configurations in one place
- **Environment Management**: Separate configurations for development, production, and testing
- **Automated Deployment**: Scripts to deploy and manage MCP configurations
- **Health Monitoring**: Built-in health checks and status monitoring
- **Backup & Recovery**: Automatic backup of configurations
- **Easy CLI Interface**: Simple command-line tools for management

<!-- section_id: "c7d9f70d-07f5-44ac-bf52-d8bb1c2ce9b7" -->
## 🚀 Quick Start

<!-- section_id: "968e599b-c5af-45b7-bd15-6de772f10d60" -->
### 1. Initial Setup
```bash
# Set up the complete MCP system
python3 automation/scripts/mcp_manager.py

# Verify setup
# (Health check script to be implemented)
```

<!-- section_id: "abd0a2d2-c16f-4a7e-96c3-e893927308d3" -->
### 2. Deploy Configuration
```bash
# Deploy development environment (default)
python3 scripts/mcp-cli.py deploy development

# Deploy production environment
python3 scripts/mcp-cli.py deploy production

# Deploy testing environment
python3 scripts/mcp-cli.py deploy testing
```

<!-- section_id: "f131be28-3946-4a79-9bbd-19bd7b64ea23" -->
### 3. Check Status
```bash
# Show system status
python3 scripts/mcp-cli.py status

# Run health check
python3 scripts/mcp-cli.py health

# Generate report
python3 scripts/mcp-cli.py report
```

<!-- section_id: "70d162be-5247-4259-955d-65bdb38a556c" -->
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

<!-- section_id: "8695664d-0b94-41f0-9b7f-9a9ceaf9d3ce" -->
## 🔧 Available MCP Servers

<!-- section_id: "d2e49996-240c-464a-82cb-3d82c804e17b" -->
### Browser Automation
- **chrome-devtools**: Chrome DevTools integration for debugging
- **playwright**: Cross-browser testing and automation
- **browser**: Simple browser automation

<!-- section_id: "441ce9d5-eaa7-4e6b-a444-79b710da0951" -->
### Search & Research
- **web-search**: Tavily web search integration
- **github-search**: GitHub repository search
- **context7**: Documentation and context management (local and remote options)

<!-- section_id: "19b873df-94b5-4e08-8119-52840079dcb1" -->
### System Integration
- **filesystem**: File system access and management
- **slack**: Slack integration for notifications
- **postgres**: PostgreSQL database integration

<!-- section_id: "6f17cc84-1024-45a0-bdaa-58fe9c24b732" -->
## 🌍 Environment Configurations

<!-- section_id: "0a13b818-3ba4-4e4b-be48-0a3abd34c370" -->
### Development Environment
**Purpose**: Full debugging and development tools
**Servers**: chrome-devtools, playwright, browser, web-search, github-search, filesystem, context7
**Features**:
- All browser automation tools
- Complete search capabilities
- Filesystem access
- Documentation tools
- Debug logging enabled

<!-- section_id: "d8ee8a3c-149f-4c09-b1fe-50c84c1bddc4" -->
### Production Environment
**Purpose**: Essential tools for production use
**Servers**: web-search, github-search, filesystem, slack, postgres
**Features**:
- Essential search tools only
- Slack notifications
- Database integration
- Optimized for performance
- Minimal resource usage

<!-- section_id: "f53a3498-91ad-4ca3-b7c4-8947dfc58d95" -->
### Testing Environment
**Purpose**: Automated testing and validation
**Servers**: playwright, browser, filesystem
**Features**:
- Browser automation for testing
- Filesystem access
- Minimal resource usage
- Fast startup times

<!-- section_id: "0495eeac-da61-4124-bcd7-98a98399294c" -->
## 🛠️ Management Commands

<!-- section_id: "316892b5-9302-4c23-812a-32f792064081" -->
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

<!-- section_id: "21aa95ad-60c6-476c-a1be-8720717591fb" -->
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

<!-- section_id: "f0646dd5-a295-4450-97c1-c257084fd902" -->
## 📊 Monitoring and Health Checks

<!-- section_id: "5075e47f-52c2-4f61-91d3-7b10b338221c" -->
### Automatic Monitoring
- **Health Checks**: Every 5 minutes
- **Server Status**: Real-time tracking
- **Configuration Validation**: Pre-deployment checks
- **Logging**: Comprehensive logging with rotation

<!-- section_id: "f2b35a07-2f21-4c57-bc31-54c2c3e6cc91" -->
### Health Check Features
```bash
# Run comprehensive health check
python3 scripts/mcp-cli.py health

# Check specific environment
python3 scripts/mcp-cli.py validate development
```

<!-- section_id: "6240acf6-a6ec-491d-b81b-4ee2b0ef0412" -->
### Status Information
- Active server count
- Environment status
- Configuration validity
- Dependency checks
- Performance metrics

<!-- section_id: "ba9a9043-0a00-4b19-842e-5fcdf65a7bff" -->
## 🔒 Security and Configuration

<!-- section_id: "0cc86661-8309-4c1d-a41a-b1f288e85572" -->
### API Key Management
- Environment-specific API keys
- Placeholder values for production setup
- Secure storage recommendations
- Key rotation support

<!-- section_id: "43f1632c-9b64-45c3-9afa-b371471a9283" -->
### Configuration Security
- Separate configurations per environment
- No hardcoded production keys
- Environment variable support
- Backup and recovery

<!-- section_id: "21f34daf-9e3c-43f3-adba-1ef057ee1f60" -->
## 📈 Backup and Recovery

<!-- section_id: "a836c957-7b0f-4c44-9616-4d139e3c3762" -->
### Automatic Backups
- Configuration backups before each deployment
- Timestamped backup files
- Easy restoration process
- Configuration history tracking

<!-- section_id: "ba83ff6f-0291-4f74-bd7e-341fd923b0ce" -->
### Manual Backup
```bash
# Backup current configuration
cp .mcp.json backups/mcp/manual_backup_$(date +%Y%m%d_%H%M%S).json

# Restore from backup
cp backups/mcp/backup_file.json .mcp.json
```

<!-- section_id: "90092a46-0a48-4d8f-bf0e-a4cdcba4c530" -->
## 🚨 Troubleshooting

<!-- section_id: "b1796a0e-dade-4390-ac91-16d8a3e290e5" -->
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

<!-- section_id: "ea81e64a-bc87-4439-8fb0-d605a84e7616" -->
### Debug Information
- Check logs: `tail -f backups/mcp/mcp.log`
- Run health check: `python3 scripts/mcp-cli.py health`
- Generate report: `python3 scripts/mcp-cli.py report`

<!-- section_id: "93de5a99-fc3f-409f-b756-d2af4fe4408e" -->
## 🔄 Workflow Integration

<!-- section_id: "e237f67a-ad61-4411-95c9-4707d97276ca" -->
### Development Workflow
1. **Setup**: `python3 scripts/mcp-cli.py setup`
2. **Deploy Dev**: `python3 scripts/mcp-cli.py deploy development`
3. **Develop**: Use MCP tools for development
4. **Test**: `python3 scripts/mcp-cli.py deploy testing`
5. **Deploy Prod**: `python3 scripts/mcp-cli.py deploy production`

<!-- section_id: "735a265a-7329-4a76-9297-173fb8acfc9e" -->
### CI/CD Integration
```bash
# In your CI/CD pipeline
python3 scripts/mcp-cli.py validate production
python3 scripts/mcp-cli.py deploy production
python3 scripts/mcp-cli.py health
```

<!-- section_id: "9c4c0bff-7ae2-4296-b205-418ca79aa698" -->
## 📚 Advanced Usage

<!-- section_id: "d7f852bc-849a-4246-ba28-2c4d8f5d7443" -->
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

<!-- section_id: "32d32498-90a3-4c0b-804e-ec9c2c461640" -->
### Environment Synchronization
```python
from mcp_deployer import MCPDeployer, MCPEnvironment

deployer = MCPDeployer(config_manager)
deployer.sync_across_environments([
    MCPEnvironment.DEVELOPMENT,
    MCPEnvironment.PRODUCTION
])
```

<!-- section_id: "f480dae8-62b7-4435-a838-1addd238fae9" -->
## 🎉 Benefits

<!-- section_id: "e98acef4-2043-43ae-95f3-04d730941c43" -->
### For Developers
- **Single Source of Truth**: All MCP configurations in one place
- **Easy Management**: Simple CLI commands for all operations
- **Environment Isolation**: Separate configs for different environments
- **Automated Deployment**: No manual configuration management

<!-- section_id: "28eb08b7-8bdd-4744-a735-06a1d7919e81" -->
### For Operations
- **Health Monitoring**: Built-in monitoring and alerting
- **Backup & Recovery**: Automatic backup and easy restoration
- **Scalability**: Easy to add new servers and environments
- **Documentation**: Comprehensive documentation and examples

<!-- section_id: "812b58dc-62ca-48f9-ae3f-77f88a196a91" -->
### For AI Agents
- **Consistent Configuration**: Same tools available across environments
- **Easy Access**: Simple commands to start/stop/configure
- **Reliability**: Health checks ensure servers are running
- **Flexibility**: Easy to add new MCP servers as needed

<!-- section_id: "0d4a9efe-bd77-40cb-8352-2eebab9af4e5" -->
## 🔧 Context7 MCP Server Setup

Context7 provides documentation and context management capabilities. You have two connection options:

<!-- section_id: "29961daf-c611-439e-b043-c5b453b9261b" -->
### Local Server (Recommended for Development)
```bash
# Set up local Context7 MCP server
python3 scripts/context7-setup.py setup-local

# Check status
python3 scripts/context7-setup.py status
```

<!-- section_id: "375ab706-85ae-4810-a0e4-6c32c9f50068" -->
### Remote Server (Recommended for Production)
```bash
# Set up remote Context7 MCP server
python3 scripts/context7-setup.py setup-remote

# Check status
python3 scripts/context7-setup.py status
```

<!-- section_id: "139c28cb-611f-4137-8976-222d6d7e06b7" -->
### Hybrid Setup (Both Options)
```bash
# Set up both local and remote options
python3 scripts/context7-setup.py setup-hybrid
```

<!-- section_id: "93b7b23b-eb70-42e0-9f17-c2c5808a9440" -->
### Context7 Configuration Files
- **Local**: `config/mcp/examples/context7-local.json`
- **Remote**: `config/mcp/examples/context7-remote.json`
- **Hybrid**: `config/mcp/examples/context7-hybrid.json`

<!-- section_id: "53775b7f-1b88-4b68-b04b-cfb7add9310b" -->
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

<!-- section_id: "a85fec5b-596b-4c5c-baa3-74261e837d0d" -->
## 🚀 Next Steps

1. **Run Setup**: `python3 scripts/mcp-cli.py setup`
2. **Deploy Development**: `python3 scripts/mcp-cli.py deploy development`
3. **Set up Context7**: `python3 scripts/context7-setup.py setup-local`
4. **Check Status**: `python3 scripts/mcp-cli.py status`
5. **Explore Tools**: Use the MCP servers for your AI agent tasks
6. **Customize**: Add your own MCP servers as needed

<!-- section_id: "8df20bb5-054c-48ca-804c-9f89fb8a9295" -->
## 📞 Support

- **Health Check**: `python3 scripts/mcp-cli.py health`
- **Documentation**: Check `config/mcp/README.md`
- **Logs**: Review `backups/mcp/mcp.log`
- **Status**: `python3 scripts/mcp-cli.py status`

This MCP system provides a robust, scalable, and easy-to-use foundation for managing AI agent configurations across all your environments!
