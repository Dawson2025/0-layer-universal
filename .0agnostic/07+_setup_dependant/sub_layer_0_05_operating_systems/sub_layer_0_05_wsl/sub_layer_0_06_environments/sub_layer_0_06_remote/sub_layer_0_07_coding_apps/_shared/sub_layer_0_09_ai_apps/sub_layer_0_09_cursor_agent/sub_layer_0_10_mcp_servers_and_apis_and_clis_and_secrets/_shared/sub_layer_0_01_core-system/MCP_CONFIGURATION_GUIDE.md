---
resource_id: "b8752675-f925-46ad-b2a4-ab59f93888ca"
resource_type: "document"
resource_name: "MCP_CONFIGURATION_GUIDE"
---
# MCP Configuration Guide - Universal Tools

<!-- section_id: "8e23eb78-1231-4b62-ac77-7b35a07ff88a" -->
## Overview

This guide provides comprehensive instructions for configuring and managing MCP (Model Context Protocol) tools across all environments in the lang-trak-in-progress project.

<!-- section_id: "0a896bb6-886e-4836-b1bf-aaeb2e7fd065" -->
## 🎯 Configuration Philosophy

The MCP system follows these principles:
- **Single Source of Truth**: All configurations centralized
- **Environment Isolation**: Separate configs for dev/prod/testing
- **Automated Management**: Scripts handle deployment and updates
- **Easy Switching**: Simple commands to change configurations

<!-- section_id: "f437e206-69d0-4a51-9684-ff329a059dee" -->
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

<!-- section_id: "531015d6-469a-4636-bd63-1cefd5d5f966" -->
## 🔧 Environment Configurations

<!-- section_id: "c68da9c4-1605-4f56-97f6-9c4189f4ed9a" -->
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

<!-- section_id: "5b6824c1-e083-4778-aea7-8a23beb73d2f" -->
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

<!-- section_id: "a1d50957-a3cf-4812-9c86-948bccae80cb" -->
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

<!-- section_id: "70319d02-5c4c-4115-b417-a6640e93f3e2" -->
## 🚀 Setup Commands

<!-- section_id: "fcc83cf7-be9c-4c61-b82d-7c8d9a26257f" -->
### Initial Setup
```bash
# Set up complete MCP system
python3 scripts/mcp-cli.py setup

# Verify setup
python3 scripts/mcp-cli.py health
```

<!-- section_id: "46dbe0b2-56a0-4c1e-8fa0-2194850f5a24" -->
### Environment Deployment
```bash
# Deploy development environment
python3 scripts/mcp-cli.py deploy development

# Deploy production environment
python3 scripts/mcp-cli.py deploy production

# Deploy testing environment
python3 scripts/mcp-cli.py deploy testing
```

<!-- section_id: "c861dbd5-5b93-48eb-a5bb-6ed6d90effc4" -->
### Context7 Setup
```bash
# Set up local Context7 server
python3 scripts/context7-setup.py setup-local

# Set up remote Context7 server
python3 scripts/context7-setup.py setup-remote

# Set up both options
python3 scripts/context7-setup.py setup-hybrid
```

<!-- section_id: "e2410389-47c9-4a26-b10c-42147aad7d3e" -->
## 🔑 API Key Management

<!-- section_id: "976113e0-08dc-40be-ae02-7580c5b97031" -->
### API Key Configuration
```bash
# Context7
CONTEXT7_API_KEY=your_context7_api_key_here

# Tavily Web Search
TAVILY_API_KEY=your_tavily_api_key_here

# GitHub
GITHUB_TOKEN=your_github_token_here
```

<!-- section_id: "6d631eb1-3ea5-4264-833f-de3f5deb6e6b" -->
### Security Best Practices
1. **Environment Variables**: Use env vars for sensitive data
2. **Key Rotation**: Regularly rotate API keys
3. **Access Control**: Limit key access to necessary environments
4. **Monitoring**: Monitor key usage and access

<!-- section_id: "41f6a2bd-9d48-431c-9a15-fa4b01e6eeb3" -->
## 🛠️ Server Configurations

<!-- section_id: "04161e98-8443-4a68-8048-29a4b13f690a" -->
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

<!-- section_id: "880c6dae-b962-47bb-af37-e76f661e2085" -->
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

<!-- section_id: "310a211e-69ee-4c81-87a0-a06726b2509c" -->
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

<!-- section_id: "31073833-3843-4ce5-96c6-09cc3d3c9140" -->
## 🔄 Configuration Management

<!-- section_id: "c9533537-d87b-400d-a3e5-66134f772d9c" -->
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

<!-- section_id: "94fa7edb-6b89-438c-aba5-457f6cf99e34" -->
### Updating Server Configuration
```bash
# Update server in specific environment
python3 scripts/mcp_config_manager.py update-server --environment development --server context7 --enabled true

# Update global environment variables
python3 scripts/mcp_config_manager.py update-global-env --environment production --key LOG_LEVEL --value info
```

<!-- section_id: "de5cbfb0-9089-416d-89e3-3001b9174242" -->
### Switching Configurations
```bash
# Switch to different environment
python3 scripts/mcp-cli.py deploy production

# Switch Context7 to local
python3 scripts/context7-setup.py setup-local

# Switch Context7 to remote
python3 scripts/context7-setup.py setup-remote
```

<!-- section_id: "068fe922-7f97-445a-b7f7-c1025bd0c6dc" -->
## 📊 Monitoring and Health Checks

<!-- section_id: "fdccbc16-e585-47b2-be1e-8354c7e7ca73" -->
### Health Check Commands
```bash
# Overall MCP system health
python3 scripts/mcp-cli.py health

# Context7 specific status
python3 scripts/context7-setup.py status

# Validate configuration
python3 scripts/mcp-cli.py validate development
```

<!-- section_id: "7f5d0b05-7457-4bb8-9704-7d85e86de506" -->
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

<!-- section_id: "e013dd97-ff70-45f8-8bb1-733f9a4e21e4" -->
## 🚨 Troubleshooting

<!-- section_id: "1a0250a4-5e18-485f-86de-ec8eb534f520" -->
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

<!-- section_id: "030edbf6-3c42-43cd-95aa-c90a506a3c98" -->
### Debug Information
```bash
# View logs
tail -f backups/mcp/mcp.log

# Check system status
python3 scripts/mcp-cli.py status

# Generate detailed report
python3 scripts/mcp-cli.py report
```

<!-- section_id: "8378bbcc-ff63-4503-8c5c-a3be185e73b5" -->
## 🎯 Best Practices

<!-- section_id: "a98f3897-39a8-473f-ae7d-9eefa63aa329" -->
### Development
- Use local servers for better performance
- Enable debug logging
- Test both local and remote configurations
- Keep configurations in version control

<!-- section_id: "9757b9b6-fc36-41fa-b990-ca5394d1fa59" -->
### Production
- Use remote servers for simplicity
- Enable monitoring and alerting
- Regular configuration backups
- Secure API key management

<!-- section_id: "86edeb04-35aa-4a0f-9c00-fc6c8e995db3" -->
### Testing
- Use minimal server configurations
- Fast startup times
- Reliable test environments
- Automated health checks

<!-- section_id: "60207af3-8cc4-4896-bf05-7b90da13d598" -->
## 📚 Additional Resources

- **Complete Setup Guide**: [CONTEXT7_CLAUDE_SETUP.md](CONTEXT7_CLAUDE_SETUP.md)
- **Quick Reference**: [CONTEXT7_QUICK_REFERENCE.md](CONTEXT7_QUICK_REFERENCE.md)
- **MCP System Guide**: [../../../../MCP_SYSTEM_GUIDE.md](../../../../MCP_SYSTEM_GUIDE.md)
- **Configuration Examples**: `config/mcp/examples/`

---

**This configuration guide ensures consistent MCP setup across all environments and provides comprehensive management capabilities for all AI agents.**
