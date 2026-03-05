---
resource_id: "383d5086-7ed0-43a8-9341-685c6f546d15"
resource_type: "document"
resource_name: "MCP_SYSTEM_GUIDE"
---
# MCP Configuration Management System

<!-- section_id: "9d40238f-fdb9-4fe1-beff-64bc5dd018ac" -->
## Overview

This project now includes a comprehensive **Model Context Protocol (MCP) Configuration Management System** that serves as a single source of truth for all AI agent configurations across different environments.

<!-- section_id: "723c9fb5-c913-47d3-9a16-c16eddd178b6" -->
## 🎯 Key Features

- **Centralized Configuration**: All MCP server configurations in one place
- **Environment Management**: Separate configurations for development, production, and testing
- **Automated Deployment**: Scripts to deploy and manage MCP configurations
- **Health Monitoring**: Built-in health checks and status monitoring
- **Backup & Recovery**: Automatic backup of configurations
- **Easy CLI Interface**: Simple command-line tools for management

<!-- section_id: "bbd0a1f0-267d-4f6c-a879-49d098c2f3ab" -->
## 🚀 Quick Start

<!-- section_id: "77fd01e2-3304-4664-93d4-8fc5af6074fe" -->
### 1. Initial Setup
```bash
# Set up the complete MCP system
python3 automation/scripts/mcp_manager.py

# Verify setup
# (Health check script to be implemented)
```

<!-- section_id: "e235b672-cf1b-4100-83ee-fedf996db0a5" -->
### 2. Deploy Configuration
```bash
# Deploy development environment (default)
python3 scripts/mcp-cli.py deploy development

# Deploy production environment
python3 scripts/mcp-cli.py deploy production

# Deploy testing environment
python3 scripts/mcp-cli.py deploy testing
```

<!-- section_id: "2c8dca96-241c-47ef-99a9-4bda5c91caaf" -->
### 3. Check Status
```bash
# Show system status
python3 scripts/mcp-cli.py status

# Run health check
python3 scripts/mcp-cli.py health

# Generate report
python3 scripts/mcp-cli.py report
```

<!-- section_id: "6d99d90d-9732-4548-8036-b9b3d677a560" -->
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

<!-- section_id: "ce8784bb-38f2-4f53-8528-3c45ddb72641" -->
## 🔧 Available MCP Servers

<!-- section_id: "0053b6d2-3c31-42a0-8378-fc62cf909384" -->
### Browser Automation
- **chrome-devtools**: Chrome DevTools integration for debugging
- **playwright**: Cross-browser testing and automation
- **browser**: Simple browser automation

<!-- section_id: "fd97716b-6dd5-48c8-96eb-3e81b5809761" -->
### Search & Research
- **web-search**: Tavily web search integration
- **github-search**: GitHub repository search
- **context7**: Documentation and context management (local and remote options)

<!-- section_id: "327fe392-361d-4193-a48e-35abd2501d4c" -->
### System Integration
- **filesystem**: File system access and management
- **slack**: Slack integration for notifications
- **postgres**: PostgreSQL database integration

<!-- section_id: "11f7500d-5fb7-4ab4-a03e-d97d53a1c07d" -->
## 🌍 Environment Configurations

<!-- section_id: "c0799eb5-d832-45ac-ad85-b94fceaa62a1" -->
### Development Environment
**Purpose**: Full debugging and development tools
**Servers**: chrome-devtools, playwright, browser, web-search, github-search, filesystem, context7
**Features**:
- All browser automation tools
- Complete search capabilities
- Filesystem access
- Documentation tools
- Debug logging enabled

<!-- section_id: "bfa30844-0d1f-4330-a5f2-839dc9c40a68" -->
### Production Environment
**Purpose**: Essential tools for production use
**Servers**: web-search, github-search, filesystem, slack, postgres
**Features**:
- Essential search tools only
- Slack notifications
- Database integration
- Optimized for performance
- Minimal resource usage

<!-- section_id: "69f1497e-3e0f-477b-8855-6d53287af151" -->
### Testing Environment
**Purpose**: Automated testing and validation
**Servers**: playwright, browser, filesystem
**Features**:
- Browser automation for testing
- Filesystem access
- Minimal resource usage
- Fast startup times

<!-- section_id: "80b69c64-a59c-44fd-ab8e-d40bf502a100" -->
## 🛠️ Management Commands

<!-- section_id: "2246f8c6-f028-47f9-afc7-3574c79211b4" -->
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

<!-- section_id: "22352c1b-2864-49bd-b4cd-8e7043238036" -->
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

<!-- section_id: "5e70802f-e369-4c67-a68f-8eaf63dfd29c" -->
## 📊 Monitoring and Health Checks

<!-- section_id: "dd31e2ce-9760-44fe-9fad-9e8dd938d777" -->
### Automatic Monitoring
- **Health Checks**: Every 5 minutes
- **Server Status**: Real-time tracking
- **Configuration Validation**: Pre-deployment checks
- **Logging**: Comprehensive logging with rotation

<!-- section_id: "ee9951ce-35d8-4851-8e57-f54373e299a6" -->
### Health Check Features
```bash
# Run comprehensive health check
python3 scripts/mcp-cli.py health

# Check specific environment
python3 scripts/mcp-cli.py validate development
```

<!-- section_id: "10eab3c6-c415-42e1-aa3a-525762c6dff2" -->
### Status Information
- Active server count
- Environment status
- Configuration validity
- Dependency checks
- Performance metrics

<!-- section_id: "235b95f6-6a25-42c1-b4f8-4f3711784237" -->
## 🔒 Security and Configuration

<!-- section_id: "e26329c1-38ca-4f2e-8bc0-55d53775ae6e" -->
### API Key Management
- Environment-specific API keys
- Placeholder values for production setup
- Secure storage recommendations
- Key rotation support

<!-- section_id: "0a25d532-b08e-4564-89fd-1b7a570f06d4" -->
### Configuration Security
- Separate configurations per environment
- No hardcoded production keys
- Environment variable support
- Backup and recovery

<!-- section_id: "f2a9a8ce-6037-4eea-a277-65acce1a6e33" -->
## 📈 Backup and Recovery

<!-- section_id: "4d2f92ab-383f-4b3e-9819-1f2a9060195e" -->
### Automatic Backups
- Configuration backups before each deployment
- Timestamped backup files
- Easy restoration process
- Configuration history tracking

<!-- section_id: "55a8720d-c9a8-4d05-880b-b5508f36fd5d" -->
### Manual Backup
```bash
# Backup current configuration
cp .mcp.json backups/mcp/manual_backup_$(date +%Y%m%d_%H%M%S).json

# Restore from backup
cp backups/mcp/backup_file.json .mcp.json
```

<!-- section_id: "61f99562-d51e-4d05-8158-0672d3054769" -->
## 🚨 Troubleshooting

<!-- section_id: "db315b67-feb8-452d-ab43-c233d377d15d" -->
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

<!-- section_id: "556b184b-152a-46af-a375-84b2f939ede8" -->
### Debug Information
- Check logs: `tail -f backups/mcp/mcp.log`
- Run health check: `python3 scripts/mcp-cli.py health`
- Generate report: `python3 scripts/mcp-cli.py report`

<!-- section_id: "780f6443-d5ab-441f-a27b-5e1ee6ab9fec" -->
## 🔄 Workflow Integration

<!-- section_id: "80ce45d6-7314-4731-a9f8-e1ddb3b7f095" -->
### Development Workflow
1. **Setup**: `python3 scripts/mcp-cli.py setup`
2. **Deploy Dev**: `python3 scripts/mcp-cli.py deploy development`
3. **Develop**: Use MCP tools for development
4. **Test**: `python3 scripts/mcp-cli.py deploy testing`
5. **Deploy Prod**: `python3 scripts/mcp-cli.py deploy production`

<!-- section_id: "8f4c4c0d-76fb-494e-a7ce-ca960eec0de5" -->
### CI/CD Integration
```bash
# In your CI/CD pipeline
python3 scripts/mcp-cli.py validate production
python3 scripts/mcp-cli.py deploy production
python3 scripts/mcp-cli.py health
```

<!-- section_id: "04ebaa58-6479-4a52-b986-75f9923e4223" -->
## 📚 Advanced Usage

<!-- section_id: "f049631e-1e5f-4b65-9b9d-62e5011ba6d5" -->
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

<!-- section_id: "6949d7e1-fcad-440f-82d4-4c240469b18b" -->
### Environment Synchronization
```python
from mcp_deployer import MCPDeployer, MCPEnvironment

deployer = MCPDeployer(config_manager)
deployer.sync_across_environments([
    MCPEnvironment.DEVELOPMENT,
    MCPEnvironment.PRODUCTION
])
```

<!-- section_id: "e346d354-b004-43ef-85f4-8a83068c0d06" -->
## 🎉 Benefits

<!-- section_id: "2fb42849-ce72-4876-b42d-7690f47524ad" -->
### For Developers
- **Single Source of Truth**: All MCP configurations in one place
- **Easy Management**: Simple CLI commands for all operations
- **Environment Isolation**: Separate configs for different environments
- **Automated Deployment**: No manual configuration management

<!-- section_id: "5c8753c7-066e-41ef-a03a-24943968d032" -->
### For Operations
- **Health Monitoring**: Built-in monitoring and alerting
- **Backup & Recovery**: Automatic backup and easy restoration
- **Scalability**: Easy to add new servers and environments
- **Documentation**: Comprehensive documentation and examples

<!-- section_id: "300c3f2a-90b4-4d88-8cf7-2ff8b60bc062" -->
### For AI Agents
- **Consistent Configuration**: Same tools available across environments
- **Easy Access**: Simple commands to start/stop/configure
- **Reliability**: Health checks ensure servers are running
- **Flexibility**: Easy to add new MCP servers as needed

<!-- section_id: "4d8311f1-d9d8-433a-ac14-908d5e8052cc" -->
## 🔧 Context7 MCP Server Setup

Context7 provides documentation and context management capabilities. You have two connection options:

<!-- section_id: "0ccc8f83-c047-4efc-b02e-0bcd100f7dc5" -->
### Local Server (Recommended for Development)
```bash
# Set up local Context7 MCP server
python3 scripts/context7-setup.py setup-local

# Check status
python3 scripts/context7-setup.py status
```

<!-- section_id: "27654ff8-d30c-4845-8700-bf5e70ebe8ed" -->
### Remote Server (Recommended for Production)
```bash
# Set up remote Context7 MCP server
python3 scripts/context7-setup.py setup-remote

# Check status
python3 scripts/context7-setup.py status
```

<!-- section_id: "b927beb7-3321-4b39-9d39-28d6b311eb18" -->
### Hybrid Setup (Both Options)
```bash
# Set up both local and remote options
python3 scripts/context7-setup.py setup-hybrid
```

<!-- section_id: "c39964ca-178d-4d11-9fa4-9cf167a70238" -->
### Context7 Configuration Files
- **Local**: `config/mcp/examples/context7-local.json`
- **Remote**: `config/mcp/examples/context7-remote.json`
- **Hybrid**: `config/mcp/examples/context7-hybrid.json`

<!-- section_id: "857caf77-fda1-4f58-af40-0005df8ddb54" -->
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

<!-- section_id: "f84ade6f-d12a-4f2f-b6f3-e315abe6ce75" -->
## 🚀 Next Steps

1. **Run Setup**: `python3 scripts/mcp-cli.py setup`
2. **Deploy Development**: `python3 scripts/mcp-cli.py deploy development`
3. **Set up Context7**: `python3 scripts/context7-setup.py setup-local`
4. **Check Status**: `python3 scripts/mcp-cli.py status`
5. **Explore Tools**: Use the MCP servers for your AI agent tasks
6. **Customize**: Add your own MCP servers as needed

<!-- section_id: "8e143cf4-af29-4cfb-95ae-de19438f903f" -->
## 📞 Support

- **Health Check**: `python3 scripts/mcp-cli.py health`
- **Documentation**: Check `config/mcp/README.md`
- **Logs**: Review `backups/mcp/mcp.log`
- **Status**: `python3 scripts/mcp-cli.py status`

This MCP system provides a robust, scalable, and easy-to-use foundation for managing AI agent configurations across all your environments!
