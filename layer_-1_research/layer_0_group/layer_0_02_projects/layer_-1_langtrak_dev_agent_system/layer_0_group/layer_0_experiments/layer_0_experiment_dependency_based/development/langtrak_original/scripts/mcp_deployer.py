#!/usr/bin/env python3
"""
MCP Deployer
Automated deployment and management system for MCP configurations across environments.
"""

import json
import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any
import logging
from mcp_config_manager import MCPConfigManager, MCPEnvironment

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class MCPDeployer:
    """Automated MCP deployment and management system."""
    
    def __init__(self, config_manager: MCPConfigManager):
        self.config_manager = config_manager
        self.deployment_log = []
        self.active_servers = {}
    
    def deploy_environment(self, environment: MCPEnvironment, 
                          validate_first: bool = True,
                          start_servers: bool = True) -> bool:
        """Deploy MCP configuration to a specific environment."""
        logger.info(f"🚀 Deploying MCP configuration for {environment.value}")
        
        try:
            # Step 1: Validate configuration
            if validate_first:
                logger.info("🔍 Validating configuration...")
                is_valid, errors = self.config_manager.validate_configuration(environment)
                if not is_valid:
                    logger.error("❌ Configuration validation failed:")
                    for error in errors:
                        logger.error(f"  - {error}")
                    return False
                logger.info("✅ Configuration validation passed")
            
            # Step 2: Generate MCP JSON file
            logger.info("📝 Generating MCP configuration file...")
            mcp_file = self.config_manager.generate_mcp_json(environment)
            logger.info(f"✅ Generated MCP configuration: {mcp_file}")
            
            # Step 3: Backup existing configuration
            self._backup_existing_config(environment)
            
            # Step 4: Deploy configuration
            self._deploy_configuration(environment, mcp_file)
            
            # Step 5: Start servers if requested
            if start_servers:
                self._start_environment_servers(environment)
            
            # Step 6: Verify deployment
            self._verify_deployment(environment)
            
            logger.info(f"✅ Successfully deployed MCP configuration for {environment.value}")
            return True
            
        except Exception as e:
            logger.error(f"❌ Deployment failed: {e}")
            return False
    
    def _backup_existing_config(self, environment: MCPEnvironment):
        """Backup existing MCP configuration."""
        backup_dir = Path("backups/mcp") / environment.value
        backup_dir.mkdir(parents=True, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = backup_dir / f"mcp_config_{timestamp}.json"
        
        # Look for existing .mcp.json files
        existing_files = [
            ".mcp.json",
            f".mcp.{environment.value}.json",
            f"mcp.{environment.value}.json"
        ]
        
        for file_path in existing_files:
            if Path(file_path).exists():
                shutil.copy2(file_path, backup_file)
                logger.info(f"📦 Backed up existing config: {file_path} -> {backup_file}")
                break
    
    def _deploy_configuration(self, environment: MCPEnvironment, mcp_file: str):
        """Deploy MCP configuration to target locations."""
        config = self.config_manager.get_environment_config(environment)
        
        # Copy to standard locations
        target_locations = [
            ".mcp.json",  # Default location
            f".mcp.{environment.value}.json",  # Environment-specific
            f"config/mcp.{environment.value}.json"  # Config directory
        ]
        
        for target in target_locations:
            target_path = Path(target)
            target_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(mcp_file, target_path)
            logger.info(f"📋 Deployed to: {target_path}")
        
        # Create symlink for easy access
        symlink_path = f".mcp.{environment.value}.json"
        if not Path(symlink_path).exists():
            os.symlink(mcp_file, symlink_path)
            logger.info(f"🔗 Created symlink: {symlink_path}")
    
    def _start_environment_servers(self, environment: MCPEnvironment):
        """Start all enabled servers for an environment."""
        config = self.config_manager.get_environment_config(environment)
        
        logger.info(f"🔄 Starting servers for {environment.value}...")
        
        for server in config.servers:
            if server.enabled:
                logger.info(f"  Starting {server.name}...")
                success = self.config_manager.start_server(server.name, environment)
                if success:
                    self.active_servers[server.name] = {
                        "environment": environment.value,
                        "started_at": datetime.now(),
                        "status": "running"
                    }
                    logger.info(f"  ✅ {server.name} started")
                else:
                    logger.error(f"  ❌ Failed to start {server.name}")
            else:
                logger.info(f"  ⏸️  {server.name} is disabled")
    
    def _verify_deployment(self, environment: MCPEnvironment):
        """Verify that deployment was successful."""
        logger.info("🔍 Verifying deployment...")
        
        config = self.config_manager.get_environment_config(environment)
        running_servers = 0
        total_servers = len([s for s in config.servers if s.enabled])
        
        for server in config.servers:
            if server.enabled:
                status = self.config_manager.check_server_status(server.name)
                if status.value == "running":
                    running_servers += 1
                    logger.info(f"  ✅ {server.name}: {status.value}")
                else:
                    logger.warning(f"  ⚠️  {server.name}: {status.value}")
        
        logger.info(f"📊 Deployment summary: {running_servers}/{total_servers} servers running")
        
        if running_servers == total_servers:
            logger.info("✅ All servers are running successfully")
        elif running_servers > 0:
            logger.warning("⚠️  Some servers failed to start")
        else:
            logger.error("❌ No servers are running")
    
    def stop_environment(self, environment: MCPEnvironment):
        """Stop all servers for an environment."""
        logger.info(f"🛑 Stopping servers for {environment.value}...")
        
        config = self.config_manager.get_environment_config(environment)
        stopped_count = 0
        
        for server in config.servers:
            if server.enabled:
                success = self.config_manager.stop_server(server.name)
                if success:
                    stopped_count += 1
                    if server.name in self.active_servers:
                        del self.active_servers[server.name]
                    logger.info(f"  ✅ Stopped {server.name}")
                else:
                    logger.warning(f"  ⚠️  {server.name} may not be running")
        
        logger.info(f"📊 Stopped {stopped_count} servers")
    
    def restart_environment(self, environment: MCPEnvironment):
        """Restart all servers for an environment."""
        logger.info(f"🔄 Restarting {environment.value} environment...")
        
        self.stop_environment(environment)
        time.sleep(2)  # Brief pause between stop and start
        self._start_environment_servers(environment)
    
    def get_deployment_status(self) -> Dict[str, Any]:
        """Get current deployment status."""
        status = {
            "timestamp": datetime.now().isoformat(),
            "active_servers": self.active_servers,
            "environments": {}
        }
        
        for env in MCPEnvironment:
            config = self.config_manager.get_environment_config(env)
            env_status = {
                "total_servers": len(config.servers),
                "enabled_servers": len([s for s in config.servers if s.enabled]),
                "running_servers": 0
            }
            
            for server in config.servers:
                if server.enabled:
                    server_status = self.config_manager.check_server_status(server.name)
                    if server_status.value == "running":
                        env_status["running_servers"] += 1
            
            status["environments"][env.value] = env_status
        
        return status
    
    def create_environment_from_template(self, source_env: MCPEnvironment, 
                                       target_env: MCPEnvironment,
                                       modifications: Dict[str, Any] = None):
        """Create a new environment configuration from an existing one."""
        logger.info(f"📋 Creating {target_env.value} from {source_env.value} template...")
        
        source_config = self.config_manager.get_environment_config(source_env)
        
        # Create new configuration
        new_config = MCPEnvironmentConfig(
            environment=target_env,
            servers=source_config.servers.copy(),
            global_env=source_config.global_env.copy(),
            timeout=source_config.timeout,
            max_concurrent_servers=source_config.max_concurrent_servers
        )
        
        # Apply modifications if provided
        if modifications:
            if "servers" in modifications:
                for server_mod in modifications["servers"]:
                    server_name = server_mod.get("name")
                    if server_name:
                        server = next((s for s in new_config.servers if s.name == server_name), None)
                        if server:
                            for key, value in server_mod.items():
                                if key != "name" and hasattr(server, key):
                                    setattr(server, key, value)
            
            if "global_env" in modifications:
                new_config.global_env.update(modifications["global_env"])
        
        # Save new configuration
        self.config_manager.update_environment_config(target_env, new_config)
        logger.info(f"✅ Created {target_env.value} environment configuration")
    
    def sync_across_environments(self, environments: List[MCPEnvironment]):
        """Sync MCP configuration across multiple environments."""
        logger.info(f"🔄 Syncing configuration across {len(environments)} environments...")
        
        # Use the first environment as the source
        source_env = environments[0]
        source_config = self.config_manager.get_environment_config(source_env)
        
        for target_env in environments[1:]:
            logger.info(f"  Syncing to {target_env.value}...")
            self.config_manager.update_environment_config(target_env, source_config)
        
        logger.info("✅ Configuration sync completed")
    
    def generate_deployment_report(self) -> str:
        """Generate a comprehensive deployment report."""
        status = self.get_deployment_status()
        
        report = f"""
# MCP Deployment Report
Generated: {status['timestamp']}

## Active Servers
"""
        
        if status['active_servers']:
            for server_name, info in status['active_servers'].items():
                report += f"- **{server_name}**: {info['status']} (started: {info['started_at']})\n"
        else:
            report += "- No active servers\n"
        
        report += "\n## Environment Status\n"
        
        for env_name, env_status in status['environments'].items():
            report += f"""
### {env_name.title()}
- Total servers: {env_status['total_servers']}
- Enabled servers: {env_status['enabled_servers']}
- Running servers: {env_status['running_servers']}
- Health: {'✅ Healthy' if env_status['running_servers'] == env_status['enabled_servers'] else '⚠️ Issues'}
"""
        
        return report

def main():
    """Main CLI interface for MCP Deployer."""
    import argparse
    
    parser = argparse.ArgumentParser(description="MCP Deployer")
    parser.add_argument("--config-dir", help="Configuration directory path")
    parser.add_argument("--environment", choices=[e.value for e in MCPEnvironment], 
                       default=MCPEnvironment.DEVELOPMENT.value, help="Target environment")
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Deploy command
    deploy_parser = subparsers.add_parser("deploy", help="Deploy MCP configuration")
    deploy_parser.add_argument("--no-validate", action="store_true", help="Skip validation")
    deploy_parser.add_argument("--no-start", action="store_true", help="Don't start servers")
    
    # Stop command
    stop_parser = subparsers.add_parser("stop", help="Stop environment servers")
    
    # Restart command
    restart_parser = subparsers.add_parser("restart", help="Restart environment servers")
    
    # Status command
    status_parser = subparsers.add_parser("status", help="Show deployment status")
    
    # Create environment command
    create_parser = subparsers.add_parser("create-env", help="Create new environment")
    create_parser.add_argument("--from", dest="source_env", 
                              choices=[e.value for e in MCPEnvironment],
                              help="Source environment to copy from")
    create_parser.add_argument("target_env", help="Target environment name")
    
    # Sync command
    sync_parser = subparsers.add_parser("sync", help="Sync configuration across environments")
    sync_parser.add_argument("environments", nargs="+", 
                            choices=[e.value for e in MCPEnvironment],
                            help="Environments to sync")
    
    # Report command
    report_parser = subparsers.add_parser("report", help="Generate deployment report")
    report_parser.add_argument("--output", help="Output file path")
    
    args = parser.parse_args()
    
    # Initialize components
    config_manager = MCPConfigManager(args.config_dir)
    deployer = MCPDeployer(config_manager)
    environment = MCPEnvironment(args.environment)
    
    if args.command == "deploy":
        success = deployer.deploy_environment(
            environment,
            validate_first=not args.no_validate,
            start_servers=not args.no_start
        )
        sys.exit(0 if success else 1)
    
    elif args.command == "stop":
        deployer.stop_environment(environment)
    
    elif args.command == "restart":
        deployer.restart_environment(environment)
    
    elif args.command == "status":
        status = deployer.get_deployment_status()
        print(json.dumps(status, indent=2))
    
    elif args.command == "create-env":
        if not args.source_env:
            print("Error: --from is required for create-env command")
            sys.exit(1)
        
        source_env = MCPEnvironment(args.source_env)
        target_env = MCPEnvironment(args.target_env)
        deployer.create_environment_from_template(source_env, target_env)
    
    elif args.command == "sync":
        environments = [MCPEnvironment(env) for env in args.environments]
        deployer.sync_across_environments(environments)
    
    elif args.command == "report":
        report = deployer.generate_deployment_report()
        if args.output:
            with open(args.output, 'w') as f:
                f.write(report)
            print(f"Report saved to {args.output}")
        else:
            print(report)
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
