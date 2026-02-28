#!/usr/bin/env python3
"""
Context7 MCP Server Setup Script
Easy setup and switching between local and remote Context7 MCP server configurations.
"""

import json
import os
import sys
from pathlib import Path
from typing import Dict, Any
import subprocess
import argparse

class Context7Setup:
    """Context7 MCP server setup and management."""
    
    def __init__(self, project_root: str = None):
        self.project_root = Path(project_root or "/home/dawson/code/lang-trak-in-progress")
        self.config_dir = self.project_root / "config" / "mcp"
        self.api_key = "ctx7sk-d20b6dec-5980-4ee1-9beb-0e635d626f46"
        self.mcp_url = "https://mcp.context7.com/mcp"
    
    def create_local_config(self) -> Dict[str, Any]:
        """Create local Context7 MCP configuration."""
        return {
            "mcpServers": {
                "context7": {
                    "command": "npx",
                    "args": ["-y", "@upstash/context7-mcp", "--api-key", self.api_key]
                }
            }
        }
    
    def create_remote_config(self) -> Dict[str, Any]:
        """Create remote Context7 MCP configuration."""
        return {
            "mcpServers": {
                "context7": {
                    "url": self.mcp_url,
                    "headers": {
                        "CONTEXT7_API_KEY": self.api_key
                    }
                }
            }
        }
    
    def create_hybrid_config(self) -> Dict[str, Any]:
        """Create hybrid configuration with both local and remote options."""
        return {
            "mcpServers": {
                "context7-local": {
                    "command": "npx",
                    "args": ["-y", "@upstash/context7-mcp", "--api-key", self.api_key]
                },
                "context7-remote": {
                    "url": self.mcp_url,
                    "headers": {
                        "CONTEXT7_API_KEY": self.api_key
                    }
                }
            }
        }
    
    def setup_local(self, environment: str = "development"):
        """Set up local Context7 MCP server."""
        print(f"🔧 Setting up local Context7 MCP server for {environment}...")
        
        # Create local configuration
        config = self.create_local_config()
        
        # Write to .mcp.json
        mcp_file = self.project_root / ".mcp.json"
        with open(mcp_file, 'w') as f:
            json.dump(config, f, indent=2)
        
        print(f"✅ Created local Context7 configuration: {mcp_file}")
        
        # Test the setup
        self.test_local_setup()
    
    def setup_remote(self, environment: str = "development"):
        """Set up remote Context7 MCP server."""
        print(f"🌐 Setting up remote Context7 MCP server for {environment}...")
        
        # Create remote configuration
        config = self.create_remote_config()
        
        # Write to .mcp.json
        mcp_file = self.project_root / ".mcp.json"
        with open(mcp_file, 'w') as f:
            json.dump(config, f, indent=2)
        
        print(f"✅ Created remote Context7 configuration: {mcp_file}")
        
        # Test the setup
        self.test_remote_setup()
    
    def setup_hybrid(self, environment: str = "development"):
        """Set up hybrid Context7 MCP server configuration."""
        print(f"🔄 Setting up hybrid Context7 MCP server for {environment}...")
        
        # Create hybrid configuration
        config = self.create_hybrid_config()
        
        # Write to .mcp.json
        mcp_file = self.project_root / ".mcp.json"
        with open(mcp_file, 'w') as f:
            json.dump(config, f, indent=2)
        
        print(f"✅ Created hybrid Context7 configuration: {mcp_file}")
        print("   - context7-local: Local MCP server")
        print("   - context7-remote: Remote MCP server")
    
    def test_local_setup(self):
        """Test local Context7 MCP server setup."""
        print("🧪 Testing local Context7 setup...")
        
        try:
            # Test if the package can be installed
            result = subprocess.run([
                "npx", "-y", "@upstash/context7-mcp", "--help"
            ], capture_output=True, text=True, timeout=30)
            
            if result.returncode == 0:
                print("✅ Local Context7 MCP server package is accessible")
            else:
                print(f"⚠️  Local package test returned: {result.returncode}")
                print(f"   Error: {result.stderr}")
                
        except subprocess.TimeoutExpired:
            print("⚠️  Local package test timed out")
        except Exception as e:
            print(f"❌ Local setup test failed: {e}")
    
    def test_remote_setup(self):
        """Test remote Context7 MCP server setup."""
        print("🧪 Testing remote Context7 setup...")
        
        try:
            # Test if the remote endpoint is accessible
            result = subprocess.run([
                "curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", 
                self.mcp_url
            ], capture_output=True, text=True, timeout=10)
            
            if result.returncode == 0:
                http_code = result.stdout.strip()
                if http_code in ["200", "401", "403"]:  # 401/403 are expected for API endpoints
                    print(f"✅ Remote Context7 endpoint is accessible (HTTP {http_code})")
                else:
                    print(f"⚠️  Remote endpoint returned HTTP {http_code}")
            else:
                print(f"❌ Remote endpoint test failed: {result.stderr}")
                
        except subprocess.TimeoutExpired:
            print("⚠️  Remote endpoint test timed out")
        except Exception as e:
            print(f"❌ Remote setup test failed: {e}")
    
    def show_status(self):
        """Show current Context7 configuration status."""
        print("📊 Context7 MCP Server Status")
        print("=" * 50)
        
        # Check current .mcp.json
        mcp_file = self.project_root / ".mcp.json"
        if mcp_file.exists():
            try:
                with open(mcp_file, 'r') as f:
                    config = json.load(f)
                
                print(f"📁 Configuration file: {mcp_file}")
                
                if "mcpServers" in config:
                    for server_name, server_config in config["mcpServers"].items():
                        if "context7" in server_name.lower():
                            print(f"\n🔧 {server_name}:")
                            if "command" in server_config:
                                print(f"   Type: Local (command: {server_config['command']})")
                                print(f"   Args: {' '.join(server_config['args'])}")
                            elif "url" in server_config:
                                print(f"   Type: Remote (URL: {server_config['url']})")
                                if "headers" in server_config:
                                    print(f"   Headers: {server_config['headers']}")
                            else:
                                print(f"   Type: Unknown")
                else:
                    print("❌ No MCP servers configured")
            except Exception as e:
                print(f"❌ Error reading configuration: {e}")
        else:
            print("❌ No .mcp.json file found")
        
        # Test both setups
        print("\n🧪 Testing configurations...")
        self.test_local_setup()
        self.test_remote_setup()
    
    def install_dependencies(self):
        """Install required dependencies for Context7."""
        print("📦 Installing Context7 dependencies...")
        
        try:
            # Install the local MCP server package
            result = subprocess.run([
                "npm", "install", "-g", "@upstash/context7-mcp"
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                print("✅ Context7 MCP server package installed successfully")
            else:
                print(f"⚠️  Package installation returned: {result.returncode}")
                print(f"   Error: {result.stderr}")
                
        except Exception as e:
            print(f"❌ Dependency installation failed: {e}")
    
    def create_example_configs(self):
        """Create example configuration files."""
        print("📝 Creating example configuration files...")
        
        examples_dir = self.config_dir / "examples"
        examples_dir.mkdir(exist_ok=True)
        
        # Local configuration example
        local_config = self.create_local_config()
        with open(examples_dir / "context7-local.json", 'w') as f:
            json.dump(local_config, f, indent=2)
        
        # Remote configuration example
        remote_config = self.create_remote_config()
        with open(examples_dir / "context7-remote.json", 'w') as f:
            json.dump(remote_config, f, indent=2)
        
        # Hybrid configuration example
        hybrid_config = self.create_hybrid_config()
        with open(examples_dir / "context7-hybrid.json", 'w') as f:
            json.dump(hybrid_config, f, indent=2)
        
        print(f"✅ Example configurations created in: {examples_dir}")
        print("   - context7-local.json: Local server configuration")
        print("   - context7-remote.json: Remote server configuration")
        print("   - context7-hybrid.json: Hybrid configuration")

def main():
    """Main CLI interface."""
    parser = argparse.ArgumentParser(description="Context7 MCP Server Setup")
    parser.add_argument("--project-root", help="Project root directory")
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Setup commands
    local_parser = subparsers.add_parser("setup-local", help="Set up local Context7 MCP server")
    local_parser.add_argument("--environment", default="development", help="Target environment")
    
    remote_parser = subparsers.add_parser("setup-remote", help="Set up remote Context7 MCP server")
    remote_parser.add_argument("--environment", default="development", help="Target environment")
    
    hybrid_parser = subparsers.add_parser("setup-hybrid", help="Set up hybrid Context7 MCP server")
    hybrid_parser.add_argument("--environment", default="development", help="Target environment")
    
    # Other commands
    subparsers.add_parser("status", help="Show current Context7 configuration status")
    subparsers.add_parser("install", help="Install Context7 dependencies")
    subparsers.add_parser("examples", help="Create example configuration files")
    
    args = parser.parse_args()
    
    setup = Context7Setup(args.project_root)
    
    if args.command == "setup-local":
        setup.setup_local(args.environment)
    elif args.command == "setup-remote":
        setup.setup_remote(args.environment)
    elif args.command == "setup-hybrid":
        setup.setup_hybrid(args.environment)
    elif args.command == "status":
        setup.show_status()
    elif args.command == "install":
        setup.install_dependencies()
    elif args.command == "examples":
        setup.create_example_configs()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
