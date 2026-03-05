---
resource_id: "e6dad9dd-464e-4d39-aa26-35ff1a324582"
resource_type: "document"
resource_name: "MCP_SYSTEM_GUIDE"
---
# MCP Configuration Management System

<!-- section_id: "0dbf3329-4848-4f51-8f83-7d5edaa4bbbd" -->
## Overview

This project now includes a comprehensive **Model Context Protocol (MCP) Configuration Management System** that serves as a single source of truth for all AI agent configurations across different environments.

<!-- section_id: "a9b33ef4-7bc3-4ce4-aaac-f8f48c43f894" -->
## 🎯 Key Features

- **Centralized Configuration**: All MCP server configurations in one place
- **Environment Management**: Separate configurations for development, production, and testing
- **Automated Deployment**: Scripts to deploy and manage MCP configurations
- **Health Monitoring**: Built-in health checks and status monitoring
- **Backup & Recovery**: Automatic backup of configurations
- **Easy CLI Interface**: Simple command-line tools for management

<!-- section_id: "de745be7-f3db-475f-98c3-a19601aa3e71" -->
## 🚀 Quick Start

<!-- section_id: "3e913dc3-f315-46be-bba4-c38aeb6235c0" -->
### 1. Initial Setup
```bash
# Set up the complete MCP system
python3 automation/scripts/mcp_manager.py

# Verify setup
# (Health check script to be implemented)
```

<!-- section_id: "b80bd108-e92f-486a-9d36-471da43f7d65" -->
### 2. Deploy Configuration
```bash
# Deploy development environment (default)
python3 scripts/mcp-cli.py deploy development

# Deploy production environment
python3 scripts/mcp-cli.py deploy production

# Deploy testing environment
python3 scripts/mcp-cli.py deploy testing
```

<!-- section_id: "4d946e59-df9a-41ac-a95c-d39195b56685" -->
### 3. Check Status
```bash
# Show system status
python3 scripts/mcp-cli.py status

# Run health check
python3 scripts/mcp-cli.py health

# Generate report
python3 scripts/mcp-cli.py report
```

<!-- section_id: "37ccca38-fb5f-40f9-afe6-a495cf898424" -->
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

<!-- section_id: "c9638c41-72e2-4d04-b55e-c754e42d0fe6" -->
## 🔧 Available MCP Servers

<!-- section_id: "59c95fa3-b3f7-434c-ab76-4e5f6704524f" -->
### Browser Automation
- **chrome-devtools**: Chrome DevTools integration for debugging
- **playwright**: Cross-browser testing and automation
- **browser**: Simple browser automation

<!-- section_id: "70d4ac85-3c95-4bfa-97b6-7821e45b42a7" -->
### Search & Research
- **web-search**: Tavily web search integration
- **github-search**: GitHub repository search
- **context7**: Documentation and context management (local and remote options)

<!-- section_id: "1e3b4808-b3f8-4c5a-9bf4-a008e08e8349" -->
### System Integration
- **filesystem**: File system access and management
- **slack**: Slack integration for notifications
- **postgres**: PostgreSQL database integration

<!-- section_id: "08715e1f-272e-4e11-a251-096d57e5dbb8" -->
## 🌍 Environment Configurations

<!-- section_id: "6043d026-cacb-43bd-b029-fa242872b57e" -->
### Development Environment
**Purpose**: Full debugging and development tools
**Servers**: chrome-devtools, playwright, browser, web-search, github-search, filesystem, context7
**Features**:
- All browser automation tools
- Complete search capabilities
- Filesystem access
- Documentation tools
- Debug logging enabled

<!-- section_id: "2e7a880d-8cb3-4976-a8d5-c83f0b3abe3c" -->
### Production Environment
**Purpose**: Essential tools for production use
**Servers**: web-search, github-search, filesystem, slack, postgres
**Features**:
- Essential search tools only
- Slack notifications
- Database integration
- Optimized for performance
- Minimal resource usage

<!-- section_id: "5ff58054-f33e-423f-b0a2-542e99001d61" -->
### Testing Environment
**Purpose**: Automated testing and validation
**Servers**: playwright, browser, filesystem
**Features**:
- Browser automation for testing
- Filesystem access
- Minimal resource usage
- Fast startup times

<!-- section_id: "c30a9555-9144-4a3a-8907-ace8da510218" -->
## 🛠️ Management Commands

<!-- section_id: "74f99850-ab25-4244-806a-a56da04e35fe" -->
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

<!-- section_id: "b0bb13a2-7588-4683-a282-ffe0e3c20bd9" -->
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

<!-- section_id: "3cecdca9-849f-4511-babe-01c2e9b5c185" -->
## 📊 Monitoring and Health Checks

<!-- section_id: "61455a56-e2bd-4ab2-84bd-fd214eeba121" -->
### Automatic Monitoring
- **Health Checks**: Every 5 minutes
- **Server Status**: Real-time tracking
- **Configuration Validation**: Pre-deployment checks
- **Logging**: Comprehensive logging with rotation

<!-- section_id: "d922d146-722b-4389-96cb-556765e09419" -->
### Health Check Features
```bash
# Run comprehensive health check
python3 scripts/mcp-cli.py health

# Check specific environment
python3 scripts/mcp-cli.py validate development
```

<!-- section_id: "343f1cee-9669-4c80-b0f5-31080c008a55" -->
### Status Information
- Active server count
- Environment status
- Configuration validity
- Dependency checks
- Performance metrics

<!-- section_id: "f31d9464-9fd7-4ab4-a955-dc4f5cb25ecc" -->
## 🔒 Security and Configuration

<!-- section_id: "d35a851c-146a-4c8e-a9b9-fefe4bd68e10" -->
### API Key Management
- Environment-specific API keys
- Placeholder values for production setup
- Secure storage recommendations
- Key rotation support

<!-- section_id: "c120494f-ec1a-40f5-964c-107596187c61" -->
### Configuration Security
- Separate configurations per environment
- No hardcoded production keys
- Environment variable support
- Backup and recovery

<!-- section_id: "df09549e-60d6-4ad2-94aa-c9629b431627" -->
## 📈 Backup and Recovery

<!-- section_id: "cadbf941-bcca-46d0-ac57-067c43aaa634" -->
### Automatic Backups
- Configuration backups before each deployment
- Timestamped backup files
- Easy restoration process
- Configuration history tracking

<!-- section_id: "3df56572-d7c4-4015-897e-a258771770bf" -->
### Manual Backup
```bash
# Backup current configuration
cp .mcp.json backups/mcp/manual_backup_$(date +%Y%m%d_%H%M%S).json

# Restore from backup
cp backups/mcp/backup_file.json .mcp.json
```

<!-- section_id: "92ecc89f-1958-4a51-b10f-78f1c77f4fdb" -->
## 🚨 Troubleshooting

<!-- section_id: "387a9c9d-eec9-4c71-80db-3c2ce60fc514" -->
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

<!-- section_id: "e7360ce4-52ca-4b6b-9bc9-917198d1a267" -->
### Debug Information
- Check logs: `tail -f backups/mcp/mcp.log`
- Run health check: `python3 scripts/mcp-cli.py health`
- Generate report: `python3 scripts/mcp-cli.py report`

<!-- section_id: "20e77da9-67de-4bbf-aaff-60e9970006a3" -->
## 🔄 Workflow Integration

<!-- section_id: "48dea4ac-82e4-4f40-9c61-9070d4d3b13e" -->
### Development Workflow
1. **Setup**: `python3 scripts/mcp-cli.py setup`
2. **Deploy Dev**: `python3 scripts/mcp-cli.py deploy development`
3. **Develop**: Use MCP tools for development
4. **Test**: `python3 scripts/mcp-cli.py deploy testing`
5. **Deploy Prod**: `python3 scripts/mcp-cli.py deploy production`

<!-- section_id: "bc54c66e-6933-477f-bb0c-df1a5fa5722f" -->
### CI/CD Integration
```bash
# In your CI/CD pipeline
python3 scripts/mcp-cli.py validate production
python3 scripts/mcp-cli.py deploy production
python3 scripts/mcp-cli.py health
```

<!-- section_id: "5ecb929c-4cac-48a2-b9cb-f9538fc7b8ed" -->
## 📚 Advanced Usage

<!-- section_id: "40424441-8dfa-472f-8a21-1afcdfb3ba63" -->
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

<!-- section_id: "a84c053a-efe2-41d0-8562-7fedeeca5b44" -->
### Environment Synchronization
```python
from mcp_deployer import MCPDeployer, MCPEnvironment

deployer = MCPDeployer(config_manager)
deployer.sync_across_environments([
    MCPEnvironment.DEVELOPMENT,
    MCPEnvironment.PRODUCTION
])
```

<!-- section_id: "bc459593-8773-4ae0-8cd0-ac9b4234d487" -->
## 🎉 Benefits

<!-- section_id: "42ca44df-4dd5-4857-971d-edd9f25c63ec" -->
### For Developers
- **Single Source of Truth**: All MCP configurations in one place
- **Easy Management**: Simple CLI commands for all operations
- **Environment Isolation**: Separate configs for different environments
- **Automated Deployment**: No manual configuration management

<!-- section_id: "4ce9bcc8-a8bd-4252-9025-30ee5a99f069" -->
### For Operations
- **Health Monitoring**: Built-in monitoring and alerting
- **Backup & Recovery**: Automatic backup and easy restoration
- **Scalability**: Easy to add new servers and environments
- **Documentation**: Comprehensive documentation and examples

<!-- section_id: "d8cdf114-9221-4700-a759-bee54dc96866" -->
### For AI Agents
- **Consistent Configuration**: Same tools available across environments
- **Easy Access**: Simple commands to start/stop/configure
- **Reliability**: Health checks ensure servers are running
- **Flexibility**: Easy to add new MCP servers as needed

<!-- section_id: "2b7b6c48-d9a1-4215-9a96-5e468b78c7af" -->
## 🔧 Context7 MCP Server Setup

Context7 provides documentation and context management capabilities. You have two connection options:

<!-- section_id: "bbd26b3d-547f-4345-8d98-b268986bd764" -->
### Local Server (Recommended for Development)
```bash
# Set up local Context7 MCP server
python3 scripts/context7-setup.py setup-local

# Check status
python3 scripts/context7-setup.py status
```

<!-- section_id: "9c3c65bd-dd3d-4c79-ad9c-beb36f4e5d85" -->
### Remote Server (Recommended for Production)
```bash
# Set up remote Context7 MCP server
python3 scripts/context7-setup.py setup-remote

# Check status
python3 scripts/context7-setup.py status
```

<!-- section_id: "34fbe984-9619-43ab-a302-20291f12a673" -->
### Hybrid Setup (Both Options)
```bash
# Set up both local and remote options
python3 scripts/context7-setup.py setup-hybrid
```

<!-- section_id: "78f2094d-ca4d-43f7-8a4c-f4b087ae343f" -->
### Context7 Configuration Files
- **Local**: `config/mcp/examples/context7-local.json`
- **Remote**: `config/mcp/examples/context7-remote.json`
- **Hybrid**: `config/mcp/examples/context7-hybrid.json`

<!-- section_id: "d19e6e4a-7af8-4553-8676-1b9f0c67c67f" -->
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

<!-- section_id: "6da116e5-69d6-41b4-9bd0-a2156602ffca" -->
## 🚀 Next Steps

1. **Run Setup**: `python3 scripts/mcp-cli.py setup`
2. **Deploy Development**: `python3 scripts/mcp-cli.py deploy development`
3. **Set up Context7**: `python3 scripts/context7-setup.py setup-local`
4. **Check Status**: `python3 scripts/mcp-cli.py status`
5. **Explore Tools**: Use the MCP servers for your AI agent tasks
6. **Customize**: Add your own MCP servers as needed

<!-- section_id: "f629401c-fd91-486a-8638-0deac8bd0963" -->
## 📞 Support

- **Health Check**: `python3 scripts/mcp-cli.py health`
- **Documentation**: Check `config/mcp/README.md`
- **Logs**: Review `backups/mcp/mcp.log`
- **Status**: `python3 scripts/mcp-cli.py status`

This MCP system provides a robust, scalable, and easy-to-use foundation for managing AI agent configurations across all your environments!
