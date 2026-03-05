---
resource_id: "e752a365-5ae5-4c77-8cff-d53f6137485e"
resource_type: "document"
resource_name: "MCP_CONFIGURATION_GUIDE"
---
# MCP Configuration Guide - Universal Tools

<!-- section_id: "8e7e4f8b-0b73-4ec2-984b-6a2746a87499" -->
## Overview

This guide provides comprehensive instructions for configuring and managing MCP (Model Context Protocol) tools across all environments in the lang-trak-in-progress project.

<!-- section_id: "5f643d06-aeed-4116-83ac-de467465115d" -->
## 🎯 Configuration Philosophy

The MCP system follows these principles:
- **Single Source of Truth**: All configurations centralized
- **Environment Isolation**: Separate configs for dev/prod/testing
- **Automated Management**: Scripts handle deployment and updates
- **Easy Switching**: Simple commands to change configurations

<!-- section_id: "90e98e63-3239-4527-98b3-674c70b163e1" -->
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

<!-- section_id: "042dfadc-3fe3-4f91-b2a5-d295553d1862" -->
## 🔧 Environment Configurations

<!-- section_id: "7c1e9c18-244e-44c1-b206-4a8300d27650" -->
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

<!-- section_id: "f817797b-b178-4fd1-892f-0d9d57411b70" -->
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

<!-- section_id: "8f68943e-d477-4fa0-9f97-be26df93b0d8" -->
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

<!-- section_id: "81a031ae-c5e3-4838-946d-68666433b470" -->
## 🚀 Setup Commands

<!-- section_id: "2747ac63-fa72-4876-944a-d6cdf2e4207e" -->
### Initial Setup
```bash
# Set up complete MCP system
python3 scripts/mcp-cli.py setup

# Verify setup
python3 scripts/mcp-cli.py health
```

<!-- section_id: "daba0c57-4a1f-49f5-aaf4-6aafaed65634" -->
### Environment Deployment
```bash
# Deploy development environment
python3 scripts/mcp-cli.py deploy development

# Deploy production environment
python3 scripts/mcp-cli.py deploy production

# Deploy testing environment
python3 scripts/mcp-cli.py deploy testing
```

<!-- section_id: "e1d44a8d-fc5c-4b6b-9e0f-5fd862683c98" -->
### Context7 Setup
```bash
# Set up local Context7 server
python3 scripts/context7-setup.py setup-local

# Set up remote Context7 server
python3 scripts/context7-setup.py setup-remote

# Set up both options
python3 scripts/context7-setup.py setup-hybrid
```

<!-- section_id: "4d394a6a-8205-46c4-87e7-d648ef3d23d1" -->
## 🔑 API Key Management

<!-- section_id: "b563c01d-4255-4c39-81d2-978077ba4870" -->
### API Key Configuration
```bash
# Context7
CONTEXT7_API_KEY=your_context7_api_key_here

# Tavily Web Search
TAVILY_API_KEY=your_tavily_api_key_here

# GitHub
GITHUB_TOKEN=your_github_token_here
```

<!-- section_id: "bbcdc5ac-484d-40c9-bd31-513ee002137a" -->
### Security Best Practices
1. **Environment Variables**: Use env vars for sensitive data
2. **Key Rotation**: Regularly rotate API keys
3. **Access Control**: Limit key access to necessary environments
4. **Monitoring**: Monitor key usage and access

<!-- section_id: "c475b0eb-0e02-4d9c-973c-9e99287cad8a" -->
## 🛠️ Server Configurations

<!-- section_id: "5790fab1-a077-46e5-90cc-b68a5fda2c9d" -->
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

<!-- section_id: "d6f84c82-7009-4eac-87fd-a9a7aa4f17e9" -->
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

<!-- section_id: "4bf02ece-0d3b-45f6-9591-41b63a487f52" -->
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

<!-- section_id: "2155bf77-24a8-47c7-af90-dda0a8832118" -->
## 🔄 Configuration Management

<!-- section_id: "2ff5cb0f-239f-4d20-b27d-a9d95f455ddb" -->
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

<!-- section_id: "8d3f4c59-80b2-4614-ac2d-862300ebe16a" -->
### Updating Server Configuration
```bash
# Update server in specific environment
python3 scripts/mcp_config_manager.py update-server --environment development --server context7 --enabled true

# Update global environment variables
python3 scripts/mcp_config_manager.py update-global-env --environment production --key LOG_LEVEL --value info
```

<!-- section_id: "ee22cbb8-1277-41bc-823b-e196d1b41610" -->
### Switching Configurations
```bash
# Switch to different environment
python3 scripts/mcp-cli.py deploy production

# Switch Context7 to local
python3 scripts/context7-setup.py setup-local

# Switch Context7 to remote
python3 scripts/context7-setup.py setup-remote
```

<!-- section_id: "60d3cf4a-2b79-43fa-8015-87a1a9b7f65d" -->
## 📊 Monitoring and Health Checks

<!-- section_id: "6873265e-bc2d-4fef-9d03-61e383374d78" -->
### Health Check Commands
```bash
# Overall MCP system health
python3 scripts/mcp-cli.py health

# Context7 specific status
python3 scripts/context7-setup.py status

# Validate configuration
python3 scripts/mcp-cli.py validate development
```

<!-- section_id: "40648965-d4d1-43fa-b054-7b894e23b180" -->
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

<!-- section_id: "e076bb0f-4f53-4534-9f02-e2b74f8ba371" -->
## 🚨 Troubleshooting

<!-- section_id: "f243e05b-7c8a-494e-a042-da4c189d9251" -->
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

<!-- section_id: "3daf9a7e-f52e-4423-b3c9-7b37584f9fbd" -->
### Debug Information
```bash
# View logs
tail -f backups/mcp/mcp.log

# Check system status
python3 scripts/mcp-cli.py status

# Generate detailed report
python3 scripts/mcp-cli.py report
```

<!-- section_id: "65da4870-7432-4f38-9e7e-52de718d42c5" -->
## 🎯 Best Practices

<!-- section_id: "956d3b29-57ce-48d9-b89e-638446612ec3" -->
### Development
- Use local servers for better performance
- Enable debug logging
- Test both local and remote configurations
- Keep configurations in version control

<!-- section_id: "8d4298f9-41e2-4bd9-b68f-9392681a424d" -->
### Production
- Use remote servers for simplicity
- Enable monitoring and alerting
- Regular configuration backups
- Secure API key management

<!-- section_id: "b0fed47a-9e8a-45d0-87ff-96fe98f7a805" -->
### Testing
- Use minimal server configurations
- Fast startup times
- Reliable test environments
- Automated health checks

<!-- section_id: "0717ef53-ae36-44fc-9dd7-d24794d9e0db" -->
## 📚 Additional Resources

- **Complete Setup Guide**: [CONTEXT7_CLAUDE_SETUP.md](CONTEXT7_CLAUDE_SETUP.md)
- **Quick Reference**: [CONTEXT7_QUICK_REFERENCE.md](CONTEXT7_QUICK_REFERENCE.md)
- **MCP System Guide**: [../../../../MCP_SYSTEM_GUIDE.md](../../../../MCP_SYSTEM_GUIDE.md)
- **Configuration Examples**: `config/mcp/examples/`

---

**This configuration guide ensures consistent MCP setup across all environments and provides comprehensive management capabilities for all AI agents.**
