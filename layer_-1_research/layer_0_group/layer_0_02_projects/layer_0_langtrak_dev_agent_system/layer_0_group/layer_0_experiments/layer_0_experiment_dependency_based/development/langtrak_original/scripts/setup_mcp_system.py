#!/usr/bin/env python3
# resource_id: "56cf1957-daf6-4ffa-aaa2-7774ac3395c3"
# resource_type: "document"
# resource_name: "setup_mcp_system"
"""
MCP System Setup
Comprehensive setup and initialization script for the MCP configuration management system.
"""

import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class MCPSystemSetup:
    """Comprehensive MCP system setup and initialization."""
    
    def __init__(self, project_root: str = None):
        self.project_root = Path(project_root or "/home/dawson/code/lang-trak-in-progress")
        self.config_dir = self.project_root / "config" / "mcp"
        self.scripts_dir = self.project_root / "scripts"
        self.backup_dir = self.project_root / "backups" / "mcp"
        
        # Ensure directories exist
        self.config_dir.mkdir(parents=True, exist_ok=True)
        self.backup_dir.mkdir(parents=True, exist_ok=True)
    
    def setup_complete_system(self) -> bool:
        """Set up the complete MCP management system."""
        logger.info("🚀 Setting up MCP Configuration Management System")
        
        try:
            # Step 1: Install dependencies
            self._install_dependencies()
            
            # Step 2: Create configuration files
            self._create_configuration_files()
            
            # Step 3: Set up environment configurations
            self._setup_environment_configs()
            
            # Step 4: Create management scripts
            self._create_management_scripts()
            
            # Step 5: Set up monitoring and logging
            self._setup_monitoring()
            
            # Step 6: Create documentation
            self._create_documentation()
            
            # Step 7: Initialize default deployment
            self._initialize_default_deployment()
            
            logger.info("✅ MCP system setup completed successfully!")
            return True
            
        except Exception as e:
            logger.error(f"❌ Setup failed: {e}")
            return False
    
    def _install_dependencies(self):
        """Install required dependencies."""
        logger.info("📦 Installing dependencies...")
        
        # Install Python dependencies
        python_deps = [
            "pyyaml",
            "psutil",
            "requests"
        ]
        
        for dep in python_deps:
            try:
                subprocess.run([sys.executable, "-m", "pip", "install", dep], 
                             check=True, capture_output=True)
                logger.info(f"  ✅ Installed {dep}")
            except subprocess.CalledProcessError as e:
                logger.warning(f"  ⚠️  Failed to install {dep}: {e}")
        
        # Install Node.js dependencies for MCP servers
        node_deps = [
            "chrome-devtools-mcp@latest",
            "@playwright/mcp@latest",
            "@agent-infra/mcp-server-browser",
            "tavily-mcp",
            "github-mcp-server",
            "@modelcontextprotocol/server-filesystem",
            "@modelcontextprotocol/server-slack",
            "@modelcontextprotocol/server-postgres",
            "@context7/mcp-server"
        ]
        
        for dep in node_deps:
            try:
                subprocess.run(["npm", "install", "-g", dep], 
                             check=True, capture_output=True)
                logger.info(f"  ✅ Installed {dep}")
            except subprocess.CalledProcessError as e:
                logger.warning(f"  ⚠️  Failed to install {dep}: {e}")
    
    def _create_configuration_files(self):
        """Create base configuration files."""
        logger.info("📝 Creating configuration files...")
        
        # Create main configuration file
        main_config = {
            "version": "1.0.0",
            "project": "lang-trak-in-progress",
            "mcp_management": {
                "config_dir": str(self.config_dir),
                "backup_dir": str(self.backup_dir),
                "default_environment": "development",
                "auto_backup": True,
                "health_check_interval": 300
            },
            "environments": {
                "development": {
                    "description": "Development environment with full debugging tools",
                    "servers": ["chrome-devtools", "playwright", "browser", "web-search", "github-search", "filesystem", "context7"]
                },
                "production": {
                    "description": "Production environment with essential tools only",
                    "servers": ["web-search", "github-search", "filesystem", "slack", "postgres"]
                },
                "testing": {
                    "description": "Testing environment with automation tools",
                    "servers": ["playwright", "browser", "filesystem"]
                }
            }
        }
        
        config_file = self.config_dir / "mcp-system.json"
        with open(config_file, 'w') as f:
            json.dump(main_config, f, indent=2)
        
        logger.info(f"  ✅ Created main configuration: {config_file}")
    
    def _setup_environment_configs(self):
        """Set up environment-specific configurations."""
        logger.info("🌍 Setting up environment configurations...")
        
        # Environment configurations are already created in separate files
        # This method can be used to validate and enhance them
        
        environments = ["development", "production", "testing"]
        for env in environments:
            config_file = self.config_dir / f"{env}.json"
            if config_file.exists():
                logger.info(f"  ✅ {env} configuration exists")
            else:
                logger.warning(f"  ⚠️  {env} configuration missing")
    
    def _create_management_scripts(self):
        """Create management and utility scripts."""
        logger.info("🔧 Creating management scripts...")
        
        # Create MCP management wrapper script
        wrapper_script = f"""#!/bin/bash
# MCP Management Wrapper Script

PROJECT_ROOT="{self.project_root}"
CONFIG_DIR="$PROJECT_ROOT/config/mcp"
SCRIPTS_DIR="$PROJECT_ROOT/scripts"

# Change to project directory
cd "$PROJECT_ROOT"

# Run MCP management commands
case "$1" in
    "deploy")
        python3 "$SCRIPTS_DIR/mcp_deployer.py" "$@"
        ;;
    "config")
        python3 "$SCRIPTS_DIR/mcp_config_manager.py" "$@"
        ;;
    "status")
        python3 "$SCRIPTS_DIR/mcp_deployer.py" status
        ;;
    "start")
        python3 "$SCRIPTS_DIR/mcp_deployer.py" deploy --environment "${{2:-development}}"
        ;;
    "stop")
        python3 "$SCRIPTS_DIR/mcp_deployer.py" stop --environment "${{2:-development}}"
        ;;
    "restart")
        python3 "$SCRIPTS_DIR/mcp_deployer.py" restart --environment "${{2:-development}}"
        ;;
    "validate")
        python3 "$SCRIPTS_DIR/mcp_config_manager.py" validate --environment "${{2:-development}}"
        ;;
    "list")
        python3 "$SCRIPTS_DIR/mcp_config_manager.py" list
        ;;
    "report")
        python3 "$SCRIPTS_DIR/mcp_deployer.py" report
        ;;
    *)
        echo "MCP Management System"
        echo "Usage: $0 <command> [environment]"
        echo ""
        echo "Commands:"
        echo "  deploy [env]     - Deploy MCP configuration"
        echo "  config [env]     - Manage MCP configuration"
        echo "  status           - Show deployment status"
        echo "  start [env]      - Start MCP servers"
        echo "  stop [env]       - Stop MCP servers"
        echo "  restart [env]    - Restart MCP servers"
        echo "  validate [env]   - Validate configuration"
        echo "  list             - List available servers"
        echo "  report           - Generate deployment report"
        echo ""
        echo "Environments: development, production, testing"
        ;;
esac
"""
        
        wrapper_file = self.scripts_dir / "mcp-manage.sh"
        with open(wrapper_file, 'w') as f:
            f.write(wrapper_script)
        
        # Make executable
        os.chmod(wrapper_file, 0o755)
        logger.info(f"  ✅ Created management wrapper: {wrapper_file}")
        
        # Create health check script
        health_script = f"""#!/bin/bash
# MCP Health Check Script

PROJECT_ROOT="{self.project_root}"
SCRIPTS_DIR="$PROJECT_ROOT/scripts"

echo "🔍 MCP System Health Check"
echo "=========================="

# Check if MCP management scripts exist
if [ -f "$SCRIPTS_DIR/mcp_config_manager.py" ]; then
    echo "✅ MCP Config Manager: Available"
else
    echo "❌ MCP Config Manager: Missing"
fi

if [ -f "$SCRIPTS_DIR/mcp_deployer.py" ]; then
    echo "✅ MCP Deployer: Available"
else
    echo "❌ MCP Deployer: Missing"
fi

# Check configuration files
CONFIG_DIR="$PROJECT_ROOT/config/mcp"
for env in development production testing; do
    if [ -f "$CONFIG_DIR/$env.json" ]; then
        echo "✅ $env configuration: Available"
    else
        echo "❌ $env configuration: Missing"
    fi
done

# Check Node.js dependencies
echo ""
echo "📦 Node.js Dependencies:"
for dep in chrome-devtools-mcp @playwright/mcp @agent-infra/mcp-server-browser tavily-mcp github-mcp-server; do
    if npm list -g "$dep" >/dev/null 2>&1; then
        echo "✅ $dep: Installed"
    else
        echo "❌ $dep: Missing"
    fi
done

# Run validation
echo ""
echo "🔍 Configuration Validation:"
python3 "$SCRIPTS_DIR/mcp_config_manager.py" validate --environment development
"""
        
        health_file = self.scripts_dir / "mcp-health-check.sh"
        with open(health_file, 'w') as f:
            f.write(health_script)
        
        os.chmod(health_file, 0o755)
        logger.info(f"  ✅ Created health check script: {health_file}")
    
    def _setup_monitoring(self):
        """Set up monitoring and logging."""
        logger.info("📊 Setting up monitoring...")
        
        # Create monitoring configuration
        monitoring_config = {
            "health_check": {
                "interval_seconds": 300,
                "timeout_seconds": 30,
                "retry_count": 3
            },
            "logging": {
                "level": "INFO",
                "file": str(self.backup_dir / "mcp.log"),
                "max_size_mb": 10,
                "backup_count": 5
            },
            "alerts": {
                "enabled": True,
                "email": "admin@example.com",
                "slack_webhook": "https://hooks.slack.com/services/YOUR/SLACK/WEBHOOK"
            }
        }
        
        monitoring_file = self.config_dir / "monitoring.json"
        with open(monitoring_file, 'w') as f:
            json.dump(monitoring_config, f, indent=2)
        
        logger.info(f"  ✅ Created monitoring configuration: {monitoring_file}")
    
    def _create_documentation(self):
        """Create comprehensive documentation."""
        logger.info("📚 Creating documentation...")
        
        # Create README for MCP system
        readme_content = f"""# MCP Configuration Management System

This directory contains the centralized MCP (Model Context Protocol) configuration management system for the lang-trak-in-progress project.

## Overview

The MCP system provides a single source of truth for all AI agent configurations across different environments. It includes:

- **Centralized Configuration**: All MCP server configurations in one place
- **Environment Management**: Separate configurations for dev, staging, production, and testing
- **Automated Deployment**: Scripts to deploy and manage MCP configurations
- **Health Monitoring**: Built-in health checks and status monitoring
- **Backup & Recovery**: Automatic backup of configurations

## Quick Start

```bash
# Deploy development environment
./scripts/mcp-manage.sh start development

# Check system status
./scripts/mcp-manage.sh status

# Validate configuration
./scripts/mcp-manage.sh validate development

# Generate deployment report
./scripts/mcp-manage.sh report
```

## Directory Structure

```
config/mcp/
├── mcp-system.json          # Main system configuration
├── development.json         # Development environment config
├── production.json          # Production environment config
├── testing.json            # Testing environment config
└── monitoring.json         # Monitoring configuration

scripts/
├── mcp_config_manager.py   # Configuration management
├── mcp_deployer.py         # Deployment automation
├── mcp-manage.sh          # Management wrapper script
└── mcp-health-check.sh    # Health check script
```

## Available MCP Servers

### Browser Automation
- **chrome-devtools**: Chrome DevTools integration for debugging
- **playwright**: Cross-browser testing and automation
- **browser**: Simple browser automation

### Search & Research
- **web-search**: Tavily web search integration
- **github-search**: GitHub repository search
- **context7**: Documentation and context management

### System Integration
- **filesystem**: File system access and management
- **slack**: Slack integration for notifications
- **postgres**: PostgreSQL database integration

## Environment Configurations

### Development
- Full debugging tools (Chrome DevTools, Playwright)
- All search and research tools
- Filesystem access
- Context7 documentation

### Production
- Essential tools only (web-search, filesystem)
- Slack notifications
- PostgreSQL integration
- Optimized for performance

### Testing
- Browser automation tools (Playwright, browser)
- Filesystem access
- Minimal resource usage

## Management Commands

### Configuration Management
```bash
# List available servers
python3 scripts/mcp_config_manager.py list

# Validate configuration
python3 scripts/mcp_config_manager.py validate --environment development

# Generate MCP JSON
python3 scripts/mcp_config_manager.py generate --environment development
```

### Deployment Management
```bash
# Deploy to environment
python3 scripts/mcp_deployer.py deploy --environment development

# Start servers
python3 scripts/mcp_deployer.py start --environment development

# Stop servers
python3 scripts/mcp_deployer.py stop --environment development

# Restart servers
python3 scripts/mcp_deployer.py restart --environment development

# Check status
python3 scripts/mcp_deployer.py status

# Generate report
python3 scripts/mcp_deployer.py report
```

## Health Monitoring

The system includes built-in health monitoring:

- **Automatic Health Checks**: Every 5 minutes
- **Server Status Monitoring**: Real-time status tracking
- **Configuration Validation**: Pre-deployment validation
- **Logging**: Comprehensive logging with rotation

## Backup & Recovery

- **Automatic Backups**: Before each deployment
- **Configuration History**: Track changes over time
- **Easy Recovery**: Restore from any backup point

## Troubleshooting

### Common Issues

1. **Server Won't Start**
   ```bash
   # Check dependencies
   ./scripts/mcp-health-check.sh
   
   # Validate configuration
   ./scripts/mcp-manage.sh validate development
   ```

2. **Missing Dependencies**
   ```bash
   # Reinstall dependencies
   python3 scripts/setup_mcp_system.py
   ```

3. **Configuration Errors**
   ```bash
   # Check configuration syntax
   python3 scripts/mcp_config_manager.py validate --environment development
   ```

### Getting Help

- Check the health check script: `./scripts/mcp-health-check.sh`
- Review logs: `tail -f backups/mcp/mcp.log`
- Generate status report: `./scripts/mcp-manage.sh report`

## Security Notes

- API keys are stored in environment-specific configurations
- Production keys should be replaced with actual values
- Consider using environment variables for sensitive data
- Regular backup of configurations is recommended

## Contributing

When adding new MCP servers:

1. Add server configuration to `mcp_config_manager.py`
2. Update environment configurations as needed
3. Test with validation: `./scripts/mcp-manage.sh validate`
4. Update documentation

## Support

For issues or questions:
- Check the health check script
- Review configuration files
- Check system logs
- Validate configurations before deployment
"""
        
        readme_file = self.config_dir / "README.md"
        with open(readme_file, 'w') as f:
            f.write(readme_content)
        
        logger.info(f"  ✅ Created documentation: {readme_file}")
    
    def _initialize_default_deployment(self):
        """Initialize default deployment."""
        logger.info("🚀 Initializing default deployment...")
        
        try:
            # Deploy development environment by default
            from mcp_deployer import MCPDeployer
            from mcp_config_manager import MCPConfigManager, MCPEnvironment
            
            config_manager = MCPConfigManager(str(self.config_dir))
            deployer = MCPDeployer(config_manager)
            
            # Deploy development environment
            success = deployer.deploy_environment(
                MCPEnvironment.DEVELOPMENT,
                validate_first=True,
                start_servers=False  # Don't start servers during setup
            )
            
            if success:
                logger.info("  ✅ Default deployment initialized")
            else:
                logger.warning("  ⚠️  Default deployment failed")
                
        except Exception as e:
            logger.warning(f"  ⚠️  Could not initialize default deployment: {e}")
    
    def verify_setup(self) -> bool:
        """Verify that the setup was successful."""
        logger.info("🔍 Verifying MCP system setup...")
        
        checks = [
            ("Config directory", self.config_dir.exists()),
            ("Backup directory", self.backup_dir.exists()),
            ("Config manager script", (self.scripts_dir / "mcp_config_manager.py").exists()),
            ("Deployer script", (self.scripts_dir / "mcp_deployer.py").exists()),
            ("Management wrapper", (self.scripts_dir / "mcp-manage.sh").exists()),
            ("Health check script", (self.scripts_dir / "mcp-health-check.sh").exists()),
            ("Development config", (self.config_dir / "development.json").exists()),
            ("Production config", (self.config_dir / "production.json").exists()),
            ("Testing config", (self.config_dir / "testing.json").exists()),
            ("System config", (self.config_dir / "mcp-system.json").exists()),
            ("Monitoring config", (self.config_dir / "monitoring.json").exists()),
            ("Documentation", (self.config_dir / "README.md").exists())
        ]
        
        all_passed = True
        for check_name, passed in checks:
            if passed:
                logger.info(f"  ✅ {check_name}")
            else:
                logger.error(f"  ❌ {check_name}")
                all_passed = False
        
        if all_passed:
            logger.info("✅ All setup checks passed!")
        else:
            logger.error("❌ Some setup checks failed!")
        
        return all_passed

def main():
    """Main setup function."""
    import argparse
    
    parser = argparse.ArgumentParser(description="MCP System Setup")
    parser.add_argument("--project-root", help="Project root directory")
    parser.add_argument("--verify-only", action="store_true", help="Only verify setup")
    
    args = parser.parse_args()
    
    setup = MCPSystemSetup(args.project_root)
    
    if args.verify_only:
        success = setup.verify_setup()
        sys.exit(0 if success else 1)
    else:
        success = setup.setup_complete_system()
        if success:
            logger.info("🎉 MCP system setup completed successfully!")
            logger.info("Next steps:")
            logger.info("  1. Run health check: ./scripts/mcp-health-check.sh")
            logger.info("  2. Deploy development: ./scripts/mcp-manage.sh start development")
            logger.info("  3. Check status: ./scripts/mcp-manage.sh status")
        else:
            logger.error("❌ MCP system setup failed!")
        sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
