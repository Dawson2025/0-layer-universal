#!/usr/bin/env python3
"""
MCP CLI Tool
Simple command-line interface for MCP configuration management.
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class MCPCLI:
    """Simple CLI for MCP management."""
    
    def __init__(self, config_dir: str = None):
        self.config_dir = Path(config_dir or "/home/dawson/code/lang-trak-in-progress/config/mcp")
        self.scripts_dir = Path("/home/dawson/code/lang-trak-in-progress/scripts")
    
    def run_command(self, command: str, args: List[str] = None):
        """Run a command with arguments."""
        try:
            if command == "setup":
                self._run_setup()
            elif command == "deploy":
                self._run_deploy(args)
            elif command == "status":
                self._run_status()
            elif command == "validate":
                self._run_validate(args)
            elif command == "list":
                self._run_list()
            elif command == "start":
                self._run_start(args)
            elif command == "stop":
                self._run_stop(args)
            elif command == "restart":
                self._run_restart(args)
            elif command == "health":
                self._run_health()
            elif command == "report":
                self._run_report()
            elif command == "help":
                self._show_help()
            else:
                print(f"Unknown command: {command}")
                self._show_help()
        except Exception as e:
            logger.error(f"Command failed: {e}")
            sys.exit(1)
    
    def _run_setup(self):
        """Run MCP system setup."""
        print("🚀 Setting up MCP system...")
        import subprocess
        result = subprocess.run([
            sys.executable, 
            str(self.scripts_dir / "setup_mcp_system.py")
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ MCP system setup completed!")
        else:
            print(f"❌ Setup failed: {result.stderr}")
            sys.exit(1)
    
    def _run_deploy(self, args: List[str]):
        """Deploy MCP configuration."""
        env = args[0] if args else "development"
        print(f"🚀 Deploying MCP configuration for {env}...")
        
        import subprocess
        result = subprocess.run([
            sys.executable,
            str(self.scripts_dir / "mcp_deployer.py"),
            "deploy",
            "--environment", env
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✅ Deployed {env} configuration!")
        else:
            print(f"❌ Deployment failed: {result.stderr}")
            sys.exit(1)
    
    def _run_status(self):
        """Show MCP system status."""
        print("📊 MCP System Status")
        print("=" * 50)
        
        import subprocess
        result = subprocess.run([
            sys.executable,
            str(self.scripts_dir / "mcp_deployer.py"),
            "status"
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            try:
                status = json.loads(result.stdout)
                print(f"Timestamp: {status['timestamp']}")
                print(f"Active Servers: {len(status['active_servers'])}")
                
                for env_name, env_status in status['environments'].items():
                    print(f"\n{env_name.title()}:")
                    print(f"  Total: {env_status['total_servers']}")
                    print(f"  Enabled: {env_status['enabled_servers']}")
                    print(f"  Running: {env_status['running_servers']}")
            except json.JSONDecodeError:
                print(result.stdout)
        else:
            print(f"❌ Status check failed: {result.stderr}")
    
    def _run_validate(self, args: List[str]):
        """Validate MCP configuration."""
        env = args[0] if args else "development"
        print(f"🔍 Validating {env} configuration...")
        
        import subprocess
        result = subprocess.run([
            sys.executable,
            str(self.scripts_dir / "mcp_config_manager.py"),
            "validate",
            "--environment", env
        ], capture_output=True, text=True)
        
        print(result.stdout)
        if result.returncode != 0:
            print(f"❌ Validation failed: {result.stderr}")
            sys.exit(1)
    
    def _run_list(self):
        """List available MCP servers."""
        print("📋 Available MCP Servers")
        print("=" * 50)
        
        import subprocess
        result = subprocess.run([
            sys.executable,
            str(self.scripts_dir / "mcp_config_manager.py"),
            "list"
        ], capture_output=True, text=True)
        
        print(result.stdout)
        if result.returncode != 0:
            print(f"❌ List failed: {result.stderr}")
            sys.exit(1)
    
    def _run_start(self, args: List[str]):
        """Start MCP servers."""
        env = args[0] if args else "development"
        print(f"🔄 Starting MCP servers for {env}...")
        
        import subprocess
        result = subprocess.run([
            sys.executable,
            str(self.scripts_dir / "mcp_deployer.py"),
            "deploy",
            "--environment", env
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✅ Started {env} servers!")
        else:
            print(f"❌ Start failed: {result.stderr}")
            sys.exit(1)
    
    def _run_stop(self, args: List[str]):
        """Stop MCP servers."""
        env = args[0] if args else "development"
        print(f"🛑 Stopping MCP servers for {env}...")
        
        import subprocess
        result = subprocess.run([
            sys.executable,
            str(self.scripts_dir / "mcp_deployer.py"),
            "stop",
            "--environment", env
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✅ Stopped {env} servers!")
        else:
            print(f"❌ Stop failed: {result.stderr}")
            sys.exit(1)
    
    def _run_restart(self, args: List[str]):
        """Restart MCP servers."""
        env = args[0] if args else "development"
        print(f"🔄 Restarting MCP servers for {env}...")
        
        import subprocess
        result = subprocess.run([
            sys.executable,
            str(self.scripts_dir / "mcp_deployer.py"),
            "restart",
            "--environment", env
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✅ Restarted {env} servers!")
        else:
            print(f"❌ Restart failed: {result.stderr}")
            sys.exit(1)
    
    def _run_health(self):
        """Run health check."""
        print("🏥 Running MCP health check...")
        
        import subprocess
        result = subprocess.run([
            "bash",
            str(self.scripts_dir / "mcp-health-check.sh")
        ], capture_output=True, text=True)
        
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
        
        if result.returncode != 0:
            sys.exit(1)
    
    def _run_report(self):
        """Generate deployment report."""
        print("📊 Generating deployment report...")
        
        import subprocess
        result = subprocess.run([
            sys.executable,
            str(self.scripts_dir / "mcp_deployer.py"),
            "report"
        ], capture_output=True, text=True)
        
        print(result.stdout)
        if result.returncode != 0:
            print(f"❌ Report failed: {result.stderr}")
            sys.exit(1)
    
    def _show_help(self):
        """Show help information."""
        help_text = """
MCP CLI Tool - Model Context Protocol Management

USAGE:
    python3 scripts/mcp-cli.py <command> [arguments]

COMMANDS:
    setup                    Set up the complete MCP system
    deploy <env>             Deploy MCP configuration for environment
    status                   Show current system status
    validate <env>           Validate configuration for environment
    list                     List available MCP servers
    start <env>              Start MCP servers for environment
    stop <env>               Stop MCP servers for environment
    restart <env>            Restart MCP servers for environment
    health                   Run comprehensive health check
    report                   Generate deployment report
    help                     Show this help message

ENVIRONMENTS:
    development              Development environment (default)
    production               Production environment
    testing                  Testing environment

EXAMPLES:
    # Initial setup
    python3 scripts/mcp-cli.py setup
    
    # Deploy development environment
    python3 scripts/mcp-cli.py deploy development
    
    # Check system status
    python3 scripts/mcp-cli.py status
    
    # Validate production configuration
    python3 scripts/mcp-cli.py validate production
    
    # Start testing servers
    python3 scripts/mcp-cli.py start testing
    
    # Run health check
    python3 scripts/mcp-cli.py health
    
    # Generate report
    python3 scripts/mcp-cli.py report

QUICK START:
    1. python3 scripts/mcp-cli.py setup
    2. python3 scripts/mcp-cli.py deploy development
    3. python3 scripts/mcp-cli.py status
"""
        print(help_text)

def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(description="MCP CLI Tool")
    parser.add_argument("command", help="Command to execute")
    parser.add_argument("args", nargs="*", help="Command arguments")
    parser.add_argument("--config-dir", help="Configuration directory")
    
    args = parser.parse_args()
    
    cli = MCPCLI(args.config_dir)
    cli.run_command(args.command, args.args)

if __name__ == "__main__":
    main()
