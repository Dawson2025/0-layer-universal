#!/usr/bin/env python3
# resource_id: "3d44f784-141f-46a4-8f31-05a317579c36"
# resource_type: "document"
# resource_name: "mcp_config_manager"
"""
MCP Configuration Manager
Centralized management system for MCP (Model Context Protocol) configurations.
Provides a single source of truth for all AI agents and environments.
"""

import json
import os
import subprocess
import sys
import yaml
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, asdict
from enum import Enum
import shutil
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class MCPEnvironment(Enum):
    """Supported MCP environments."""
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"
    TESTING = "testing"

class MCPServerStatus(Enum):
    """MCP server status states."""
    RUNNING = "running"
    STOPPED = "stopped"
    ERROR = "error"
    UNKNOWN = "unknown"

@dataclass
class MCPServerConfig:
    """Configuration for a single MCP server."""
    name: str
    command: str
    args: List[str]
    env: Dict[str, str] = None
    enabled: bool = True
    priority: int = 1
    category: str = "general"
    description: str = ""
    dependencies: List[str] = None
    health_check_url: Optional[str] = None
    timeout: int = 30
    retry_count: int = 3
    
    def __post_init__(self):
        if self.env is None:
            self.env = {}
        if self.dependencies is None:
            self.dependencies = []

@dataclass
class MCPEnvironmentConfig:
    """Configuration for a specific environment."""
    environment: MCPEnvironment
    servers: List[MCPServerConfig]
    global_env: Dict[str, str] = None
    timeout: int = 30
    max_concurrent_servers: int = 10
    
    def __post_init__(self):
        if self.global_env is None:
            self.global_env = {}

class MCPConfigManager:
    """Centralized MCP configuration manager."""
    
    def __init__(self, config_dir: str = None):
        self.config_dir = Path(config_dir or "/home/dawson/code/lang-trak-in-progress/config/mcp")
        self.config_dir.mkdir(parents=True, exist_ok=True)
        
        # Standard MCP server configurations
        self.standard_servers = self._get_standard_server_configs()
        
        # Environment-specific configurations
        self.environments = {}
        self._load_environment_configs()
    
    def _get_standard_server_configs(self) -> Dict[str, MCPServerConfig]:
        """Get standard MCP server configurations."""
        return {
            "chrome-devtools": MCPServerConfig(
                name="chrome-devtools",
                command="npx",
                args=["-y", "chrome-devtools-mcp@latest"],
                category="browser_automation",
                description="Chrome DevTools MCP server for debugging and performance analysis",
                dependencies=["chrome", "node"],
                priority=1
            ),
            "playwright": MCPServerConfig(
                name="playwright",
                command="npx",
                args=["-y", "@playwright/mcp@latest", "--browser", "chromium"],
                category="browser_automation",
                description="Playwright MCP server for cross-browser testing and automation",
                dependencies=["node", "browsers"],
                priority=2
            ),
            "browser": MCPServerConfig(
                name="browser",
                command="npx",
                args=["@agent-infra/mcp-server-browser"],
                category="browser_automation",
                description="Simple browser automation MCP server",
                dependencies=["browser"],
                priority=3
            ),
            "web-search": MCPServerConfig(
                name="web-search",
                command="npx",
                args=["tavily-mcp"],
                env={"TAVILY_API_KEY": "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"},
                category="search",
                description="Tavily web search MCP server",
                dependencies=["node"],
                priority=1
            ),
            "github-search": MCPServerConfig(
                name="github-search",
                command="npx",
                args=["github-mcp-server"],
                env={"GITHUB_TOKEN": "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"},
                category="search",
                description="GitHub search MCP server",
                dependencies=["node"],
                priority=2
            ),
            "filesystem": MCPServerConfig(
                name="filesystem",
                command="npx",
                args=["@modelcontextprotocol/server-filesystem", "/home/dawson/code/lang-trak-in-progress"],
                category="filesystem",
                description="Filesystem access MCP server",
                dependencies=["node"],
                priority=1
            ),
            "slack": MCPServerConfig(
                name="slack",
                command="npx",
                args=["@modelcontextprotocol/server-slack"],
                env={"SLACK_BOT_TOKEN": "xoxb-your-slack-bot-token"},
                category="communication",
                description="Slack integration MCP server",
                dependencies=["node"],
                priority=3
            ),
            "postgres": MCPServerConfig(
                name="postgres",
                command="npx",
                args=["@modelcontextprotocol/server-postgres"],
                env={"POSTGRES_CONNECTION_STRING": "postgresql://user:password@localhost:5432/firebase_config"},
                category="database",
                description="PostgreSQL MCP server",
                dependencies=["node", "postgresql"],
                priority=2
            ),
            "context7": MCPServerConfig(
                name="context7",
                command="npx",
                args=["@context7/mcp-server"],
                category="documentation",
                description="Context7 documentation MCP server",
                dependencies=["node"],
                priority=2
            )
        }
    
    def _load_environment_configs(self):
        """Load environment-specific configurations."""
        for env in MCPEnvironment:
            config_file = self.config_dir / f"{env.value}.json"
            if config_file.exists():
                try:
                    with open(config_file, 'r') as f:
                        data = json.load(f)
                    self.environments[env] = self._dict_to_environment_config(data)
                except Exception as e:
                    logger.warning(f"Failed to load {env.value} config: {e}")
                    self.environments[env] = self._create_default_environment_config(env)
            else:
                self.environments[env] = self._create_default_environment_config(env)
    
    def _create_default_environment_config(self, environment: MCPEnvironment) -> MCPEnvironmentConfig:
        """Create default configuration for an environment."""
        servers = []
        
        # Base servers for all environments
        base_servers = ["filesystem", "web-search", "github-search"]
        
        # Environment-specific server additions
        if environment == MCPEnvironment.DEVELOPMENT:
            base_servers.extend(["chrome-devtools", "playwright", "browser"])
        elif environment == MCPEnvironment.PRODUCTION:
            base_servers.extend(["slack", "postgres"])
        elif environment == MCPEnvironment.TESTING:
            base_servers.extend(["playwright", "browser"])
        
        for server_name in base_servers:
            if server_name in self.standard_servers:
                servers.append(self.standard_servers[server_name])
        
        return MCPEnvironmentConfig(
            environment=environment,
            servers=servers,
            global_env={},
            timeout=30,
            max_concurrent_servers=10
        )
    
    def _dict_to_environment_config(self, data: Dict) -> MCPEnvironmentConfig:
        """Convert dictionary to MCPEnvironmentConfig."""
        servers = []
        for server_data in data.get("servers", []):
            server = MCPServerConfig(**server_data)
            servers.append(server)
        
        return MCPEnvironmentConfig(
            environment=MCPEnvironment(data["environment"]),
            servers=servers,
            global_env=data.get("global_env", {}),
            timeout=data.get("timeout", 30),
            max_concurrent_servers=data.get("max_concurrent_servers", 10)
        )
    
    def get_environment_config(self, environment: MCPEnvironment) -> MCPEnvironmentConfig:
        """Get configuration for a specific environment."""
        return self.environments.get(environment, self._create_default_environment_config(environment))
    
    def update_environment_config(self, environment: MCPEnvironment, config: MCPEnvironmentConfig):
        """Update configuration for a specific environment."""
        self.environments[environment] = config
        self._save_environment_config(environment, config)
    
    def _save_environment_config(self, environment: MCPEnvironment, config: MCPEnvironmentConfig):
        """Save environment configuration to file."""
        config_file = self.config_dir / f"{environment.value}.json"
        
        # Convert to dictionary for JSON serialization
        data = {
            "environment": config.environment.value,
            "servers": [asdict(server) for server in config.servers],
            "global_env": config.global_env,
            "timeout": config.timeout,
            "max_concurrent_servers": config.max_concurrent_servers
        }
        
        with open(config_file, 'w') as f:
            json.dump(data, f, indent=2)
        
        logger.info(f"Saved {environment.value} configuration to {config_file}")
    
    def generate_mcp_json(self, environment: MCPEnvironment, output_path: str = None) -> str:
        """Generate mcp.json file for a specific environment."""
        config = self.get_environment_config(environment)
        
        mcp_config = {
            "mcpServers": {}
        }
        
        for server in config.servers:
            if server.enabled:
                server_config = {
                    "command": server.command,
                    "args": server.args
                }
                
                if server.env:
                    server_config["env"] = server.env
                
                mcp_config["mcpServers"][server.name] = server_config
        
        # Merge global environment variables
        for server_name, server_config in mcp_config["mcpServers"].items():
            if "env" not in server_config:
                server_config["env"] = {}
            server_config["env"].update(config.global_env)
        
        # Determine output path
        if output_path is None:
            output_path = f".mcp.{environment.value}.json"
        
        # Write to file
        with open(output_path, 'w') as f:
            json.dump(mcp_config, f, indent=2)
        
        logger.info(f"Generated MCP configuration for {environment.value} at {output_path}")
        return output_path
    
    def validate_configuration(self, environment: MCPEnvironment) -> Tuple[bool, List[str]]:
        """Validate MCP configuration for an environment."""
        config = self.get_environment_config(environment)
        errors = []
        
        # Check for duplicate server names
        server_names = [server.name for server in config.servers]
        if len(server_names) != len(set(server_names)):
            errors.append("Duplicate server names found")
        
        # Check for missing dependencies
        for server in config.servers:
            if server.enabled:
                for dep in server.dependencies:
                    if not self._check_dependency(dep):
                        errors.append(f"Missing dependency '{dep}' for server '{server.name}'")
        
        # Check for required environment variables
        for server in config.servers:
            if server.enabled and server.env:
                for key, value in server.env.items():
                    if value.startswith("your-") or value == "xoxb-your-slack-bot-token":
                        errors.append(f"Server '{server.name}' has placeholder value for {key}")
        
        return len(errors) == 0, errors
    
    def _check_dependency(self, dependency: str) -> bool:
        """Check if a dependency is available."""
        try:
            if dependency == "node":
                subprocess.run(["node", "--version"], capture_output=True, check=True)
            elif dependency == "chrome":
                subprocess.run(["google-chrome", "--version"], capture_output=True, check=True)
            elif dependency == "postgresql":
                subprocess.run(["psql", "--version"], capture_output=True, check=True)
            elif dependency == "browsers":
                # Check if Playwright browsers are installed
                subprocess.run(["npx", "playwright", "install", "--dry-run"], capture_output=True, check=True)
            else:
                # Generic check
                subprocess.run(["which", dependency], capture_output=True, check=True)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False
    
    def check_server_status(self, server_name: str) -> MCPServerStatus:
        """Check the status of a specific MCP server."""
        try:
            # Try to get server info
            result = subprocess.run(
                ["npx", "mcp-server-status", server_name],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result.returncode == 0:
                return MCPServerStatus.RUNNING
            else:
                return MCPServerStatus.STOPPED
        except (subprocess.TimeoutExpired, FileNotFoundError):
            return MCPServerStatus.UNKNOWN
    
    def start_server(self, server_name: str, environment: MCPEnvironment) -> bool:
        """Start a specific MCP server."""
        config = self.get_environment_config(environment)
        server = next((s for s in config.servers if s.name == server_name), None)
        
        if not server:
            logger.error(f"Server '{server_name}' not found in {environment.value} configuration")
            return False
        
        if not server.enabled:
            logger.warning(f"Server '{server_name}' is disabled")
            return False
        
        try:
            # Start server in background
            cmd = [server.command] + server.args
            env = os.environ.copy()
            env.update(server.env)
            env.update(config.global_env)
            
            process = subprocess.Popen(
                cmd,
                env=env,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            
            logger.info(f"Started server '{server_name}' with PID {process.pid}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to start server '{server_name}': {e}")
            return False
    
    def stop_server(self, server_name: str) -> bool:
        """Stop a specific MCP server."""
        try:
            # Find and kill the process
            result = subprocess.run(
                ["pkill", "-f", server_name],
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                logger.info(f"Stopped server '{server_name}'")
                return True
            else:
                logger.warning(f"Server '{server_name}' may not be running")
                return False
                
        except Exception as e:
            logger.error(f"Failed to stop server '{server_name}': {e}")
            return False
    
    def list_available_servers(self) -> List[str]:
        """List all available MCP servers."""
        return list(self.standard_servers.keys())
    
    def add_custom_server(self, server_config: MCPServerConfig, environment: MCPEnvironment):
        """Add a custom MCP server to an environment."""
        config = self.get_environment_config(environment)
        
        # Check if server already exists
        existing = next((s for s in config.servers if s.name == server_config.name), None)
        if existing:
            logger.warning(f"Server '{server_config.name}' already exists, updating...")
            config.servers = [s for s in config.servers if s.name != server_config.name]
        
        config.servers.append(server_config)
        self.update_environment_config(environment, config)
        logger.info(f"Added custom server '{server_config.name}' to {environment.value}")
    
    def remove_server(self, server_name: str, environment: MCPEnvironment):
        """Remove a server from an environment."""
        config = self.get_environment_config(environment)
        config.servers = [s for s in config.servers if s.name != server_name]
        self.update_environment_config(environment, config)
        logger.info(f"Removed server '{server_name}' from {environment.value}")
    
    def get_server_info(self, server_name: str) -> Optional[MCPServerConfig]:
        """Get information about a specific server."""
        return self.standard_servers.get(server_name)
    
    def export_configuration(self, environment: MCPEnvironment, format: str = "json") -> str:
        """Export configuration in specified format."""
        config = self.get_environment_config(environment)
        
        if format.lower() == "json":
            return json.dumps({
                "environment": config.environment.value,
                "servers": [asdict(server) for server in config.servers],
                "global_env": config.global_env,
                "timeout": config.timeout,
                "max_concurrent_servers": config.max_concurrent_servers
            }, indent=2)
        elif format.lower() == "yaml":
            return yaml.dump({
                "environment": config.environment.value,
                "servers": [asdict(server) for server in config.servers],
                "global_env": config.global_env,
                "timeout": config.timeout,
                "max_concurrent_servers": config.max_concurrent_servers
            }, default_flow_style=False)
        else:
            raise ValueError(f"Unsupported format: {format}")

def main():
    """Main CLI interface."""
    import argparse
    
    parser = argparse.ArgumentParser(description="MCP Configuration Manager")
    parser.add_argument("--config-dir", help="Configuration directory path")
    parser.add_argument("--environment", choices=[e.value for e in MCPEnvironment], 
                       default=MCPEnvironment.DEVELOPMENT.value, help="Target environment")
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Generate MCP JSON
    gen_parser = subparsers.add_parser("generate", help="Generate mcp.json file")
    gen_parser.add_argument("--output", help="Output file path")
    
    # Validate configuration
    val_parser = subparsers.add_parser("validate", help="Validate configuration")
    
    # List servers
    list_parser = subparsers.add_parser("list", help="List available servers")
    
    # Start/stop servers
    start_parser = subparsers.add_parser("start", help="Start a server")
    start_parser.add_argument("server", help="Server name to start")
    
    stop_parser = subparsers.add_parser("stop", help="Stop a server")
    stop_parser.add_argument("server", help="Server name to stop")
    
    # Status check
    status_parser = subparsers.add_parser("status", help="Check server status")
    status_parser.add_argument("server", help="Server name to check")
    
    args = parser.parse_args()
    
    manager = MCPConfigManager(args.config_dir)
    environment = MCPEnvironment(args.environment)
    
    if args.command == "generate":
        output_path = manager.generate_mcp_json(environment, args.output)
        print(f"Generated MCP configuration: {output_path}")
    
    elif args.command == "validate":
        is_valid, errors = manager.validate_configuration(environment)
        if is_valid:
            print("✅ Configuration is valid")
        else:
            print("❌ Configuration has errors:")
            for error in errors:
                print(f"  - {error}")
    
    elif args.command == "list":
        servers = manager.list_available_servers()
        print("Available MCP servers:")
        for server in servers:
            info = manager.get_server_info(server)
            print(f"  - {server}: {info.description}")
    
    elif args.command == "start":
        success = manager.start_server(args.server, environment)
        if success:
            print(f"✅ Started server '{args.server}'")
        else:
            print(f"❌ Failed to start server '{args.server}'")
    
    elif args.command == "stop":
        success = manager.stop_server(args.server)
        if success:
            print(f"✅ Stopped server '{args.server}'")
        else:
            print(f"❌ Failed to stop server '{args.server}'")
    
    elif args.command == "status":
        status = manager.check_server_status(args.server)
        print(f"Server '{args.server}' status: {status.value}")
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
