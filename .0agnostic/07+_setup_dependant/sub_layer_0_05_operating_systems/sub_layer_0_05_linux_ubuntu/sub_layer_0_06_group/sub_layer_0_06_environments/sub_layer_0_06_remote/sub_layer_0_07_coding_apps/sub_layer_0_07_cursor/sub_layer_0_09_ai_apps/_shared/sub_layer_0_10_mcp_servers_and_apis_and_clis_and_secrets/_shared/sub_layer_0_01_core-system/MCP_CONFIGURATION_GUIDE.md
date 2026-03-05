---
resource_id: "ff419b3f-3b59-4951-89c3-d917be5b6780"
resource_type: "document"
resource_name: "MCP_CONFIGURATION_GUIDE"
---
# MCP Configuration Guide - Universal Tools

<!-- section_id: "46238a29-0425-43ff-ad42-e796f0c9ad28" -->
## Overview

This guide provides comprehensive instructions for configuring and managing MCP (Model Context Protocol) tools across all environments in the lang-trak-in-progress project.

<!-- section_id: "2f254ab3-c819-44c9-ae74-64bf8dd7b0fb" -->
## 🎯 Configuration Philosophy

The MCP system follows these principles:
- **Single Source of Truth**: All configurations centralized
- **Environment Isolation**: Separate configs for dev/prod/testing
- **Automated Management**: Scripts handle deployment and updates
- **Easy Switching**: Simple commands to change configurations

<!-- section_id: "d0f3eb96-7140-4f9c-92c1-e60a74aeeeb3" -->
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

<!-- section_id: "23223e0c-ce70-4d91-a52e-bd8ce90dc2df" -->
## 🔧 Environment Configurations

<!-- section_id: "199441e4-5d8a-4b9d-875e-45cc4ab7807f" -->
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

<!-- section_id: "82346524-6f5a-4c85-b2df-60cea1273c40" -->
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

<!-- section_id: "baa6bb8b-8269-449a-a57f-e1634fb5170c" -->
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

<!-- section_id: "335f9caf-da1c-42eb-be80-d95b2dba8486" -->
## 🚀 Setup Commands

<!-- section_id: "081638c5-2498-4f06-a158-7164877aa4b3" -->
### Initial Setup
```bash
# Set up complete MCP system
python3 scripts/mcp-cli.py setup

# Verify setup
python3 scripts/mcp-cli.py health
```

<!-- section_id: "b2923fcc-c96a-4686-b9f9-d5210a39e001" -->
### Environment Deployment
```bash
# Deploy development environment
python3 scripts/mcp-cli.py deploy development

# Deploy production environment
python3 scripts/mcp-cli.py deploy production

# Deploy testing environment
python3 scripts/mcp-cli.py deploy testing
```

<!-- section_id: "535e9131-8e91-4e4f-9cb5-a1c33548ba46" -->
### Context7 Setup
```bash
# Set up local Context7 server
python3 scripts/context7-setup.py setup-local

# Set up remote Context7 server
python3 scripts/context7-setup.py setup-remote

# Set up both options
python3 scripts/context7-setup.py setup-hybrid
```

<!-- section_id: "33f35fae-d031-455d-a933-7b1f9276a99f" -->
## 🔑 API Key Management

<!-- section_id: "af053383-64e2-4ef2-82ca-8464085cac4c" -->
### API Key Configuration
```bash
# Context7
CONTEXT7_API_KEY=your_context7_api_key_here

# Tavily Web Search
TAVILY_API_KEY=your_tavily_api_key_here

# GitHub
GITHUB_TOKEN=your_github_token_here
```

<!-- section_id: "f89e5e1b-9c8c-4b83-ad94-2d1626dca59e" -->
### Security Best Practices
1. **Environment Variables**: Use env vars for sensitive data
2. **Key Rotation**: Regularly rotate API keys
3. **Access Control**: Limit key access to necessary environments
4. **Monitoring**: Monitor key usage and access

<!-- section_id: "3fc737a5-6671-49da-9555-cb7d22233318" -->
## 🛠️ Server Configurations

<!-- section_id: "0d99e16e-b25d-4ba4-8fd4-569b3261c24f" -->
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
  "env": {
    "PLAYWRIGHT_BROWSERS_PATH": "/home/dawson/.cache/ms-playwright",
    "HOME": "/home/dawson"
  },
  "category": "browser_automation",
  "dependencies": ["node", "browsers"]
}
```

**Critical Configuration Note**: The `PLAYWRIGHT_BROWSERS_PATH` environment variable must be set to the directory where Playwright browsers are installed (typically `~/.cache/ms-playwright`). Without this, the MCP server running via `npx` in an isolated environment cannot find the browsers, even if they're installed. This is why browsers appear to need constant reinstallation - the MCP server process doesn't inherit your shell's environment variables.

**WSLg Browser Crash Fix**: On WSL (Windows Subsystem for Linux) with WSLg, headed Chromium can crash unless launched with Wayland/Ozone flags. See `0.02_mcp_config_options_0_file_tree_0/0.03_operating_systems/wsl/0.04_ai_apps/cursor_agent/0.05_mcp_servers/playwright-mcp/general_issues_and_fixes/WSLG_BROWSER_CRASH_FIX.md` for complete setup instructions including required `--ozone-platform=wayland` and `--enable-features=UseOzonePlatform` flags.

#### Browser
```json
{
  "name": "browser",
  "command": "npx",
  "args": ["@agent-infra/mcp-server-browser"],
  "env": {
    "PLAYWRIGHT_BROWSERS_PATH": "/home/dawson/.cache/ms-playwright",
    "HOME": "/home/dawson"
  },
  "category": "browser_automation",
  "dependencies": ["browser"]
}
```

**Critical Configuration Note**: The `@agent-infra/mcp-server-browser` server also needs `PLAYWRIGHT_BROWSERS_PATH` set to find browsers installed via Playwright. Additionally, set `HOME` to ensure the MCP server process can access user-specific paths and configurations.

<!-- section_id: "200bea4b-d535-4d75-a945-78dc35557309" -->
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

<!-- section_id: "88b4565e-72b2-449e-b655-c54d66092a50" -->
### System Integration Servers

#### Filesystem
```json
{
  "name": "filesystem",
  "command": "npx",
  "args": ["@modelcontextprotocol/server-filesystem", "/home/dawson/code/lang-trak-in-progress"],
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

<!-- section_id: "a41b4cd0-cf62-4275-b27b-ccec7b95782c" -->
## 🔄 Configuration Management

<!-- section_id: "94116a33-50af-4102-8321-ce28f441270e" -->
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

<!-- section_id: "a2b78808-1727-4537-aa26-77d56a723fc9" -->
### Updating Server Configuration
```bash
# Update server in specific environment
python3 scripts/mcp_config_manager.py update-server --environment development --server context7 --enabled true

# Update global environment variables
python3 scripts/mcp_config_manager.py update-global-env --environment production --key LOG_LEVEL --value info
```

<!-- section_id: "38316309-a581-4607-8725-61d2648c2cac" -->
### Switching Configurations
```bash
# Switch to different environment
python3 scripts/mcp-cli.py deploy production

# Switch Context7 to local
python3 scripts/context7-setup.py setup-local

# Switch Context7 to remote
python3 scripts/context7-setup.py setup-remote
```

<!-- section_id: "af27fe5e-488a-4b18-817e-19f1eaf67306" -->
## 📊 Monitoring and Health Checks

<!-- section_id: "84ba0f4a-0ee0-4758-91e7-d4b700f5bc1f" -->
### Health Check Commands
```bash
# Overall MCP system health
python3 scripts/mcp-cli.py health

# Context7 specific status
python3 scripts/context7-setup.py status

# Validate configuration
python3 scripts/mcp-cli.py validate development
```

<!-- section_id: "8b637f70-3bcf-4072-a0d2-3b2a79de36ff" -->
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

<!-- section_id: "a5d66ab9-bc42-4f4e-8339-a3031436f761" -->
## 🚨 Troubleshooting

<!-- section_id: "c72db763-96d2-46eb-b414-21d709f4b9fb" -->
### Common Issues and Solutions

#### Browser "Not Installed" Error (Most Common)

**Problem**: MCP browser servers report "Browser specified in your config is not installed" even when browsers are installed.

**Root Cause**: 
- MCP servers run via `npx` in isolated environments
- They don't inherit your shell's environment variables
- `PLAYWRIGHT_BROWSERS_PATH` isn't set, so servers can't find browsers in `~/.cache/ms-playwright/`
- This is why browsers appear to need constant reinstallation - they're installed, but the MCP server can't find them

**Solution**:
1. Add environment variables to your MCP server configuration:
   ```json
   {
     "playwright": {
       "command": "npx",
       "args": ["-y", "@playwright/mcp@latest", "--browser", "chromium"],
       "env": {
         "PLAYWRIGHT_BROWSERS_PATH": "/home/dawson/.cache/ms-playwright",
         "HOME": "/home/dawson"
       }
     },
     "browser": {
       "command": "npx",
       "args": ["@agent-infra/mcp-server-browser"],
       "env": {
         "PLAYWRIGHT_BROWSERS_PATH": "/home/dawson/.cache/ms-playwright",
         "HOME": "/home/dawson"
       }
     }
   }
   ```
2. Replace `/home/dawson` with your actual home directory path
3. Verify browsers are installed: `ls -la ~/.cache/ms-playwright/chromium-*/chrome-linux64/chrome`
4. Restart Cursor IDE after updating the configuration

**Why This Keeps Happening**:
- Each time Cursor restarts, it spawns new MCP server processes
- These processes run via `npx` which creates isolated execution environments
- Environment variables from your shell (like those in `.bashrc`) aren't automatically passed to MCP servers
- The MCP server needs explicit configuration to find user-installed browsers

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

<!-- section_id: "af9de05a-c2c0-4998-b763-fbbd70704848" -->
### Debug Information
```bash
# View logs
tail -f backups/mcp/mcp.log

# Check system status
python3 scripts/mcp-cli.py status

# Generate detailed report
python3 scripts/mcp-cli.py report
```

<!-- section_id: "ebc4b01f-9070-4703-8a33-8a723e95d199" -->
## 🎯 Best Practices

<!-- section_id: "8ea5cd88-10a5-4bbe-b6f3-7107111ee545" -->
### Development
- Use local servers for better performance
- Enable debug logging
- Test both local and remote configurations
- Keep configurations in version control

<!-- section_id: "ce39f748-e33a-4287-8be7-9f18c21af714" -->
### Production
- Use remote servers for simplicity
- Enable monitoring and alerting
- Regular configuration backups
- Secure API key management

<!-- section_id: "6a5e890a-8ae9-4295-bbe8-5c4fc52c579a" -->
### Testing
- Use minimal server configurations
- Fast startup times
- Reliable test environments
- Automated health checks

<!-- section_id: "61186d24-c577-45bf-afaf-89c8fadabe3f" -->
## 📚 Additional Resources

- **Complete Setup Guide**: [CONTEXT7_CLAUDE_SETUP.md](CONTEXT7_CLAUDE_SETUP.md)
- **Quick Reference**: [CONTEXT7_QUICK_REFERENCE.md](CONTEXT7_QUICK_REFERENCE.md)
- **MCP System Guide**: [../../../../MCP_SYSTEM_GUIDE.md](../../../../MCP_SYSTEM_GUIDE.md)
- **Configuration Examples**: `config/mcp/examples/`

---

**This configuration guide ensures consistent MCP setup across all environments and provides comprehensive management capabilities for all AI agents.**
