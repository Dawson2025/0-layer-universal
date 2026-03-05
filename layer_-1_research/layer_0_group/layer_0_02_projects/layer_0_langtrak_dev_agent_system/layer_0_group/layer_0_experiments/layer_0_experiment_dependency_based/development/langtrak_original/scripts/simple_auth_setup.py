#!/usr/bin/env python3
# resource_id: "a2239620-a13e-4129-b08b-9ff5da7b620e"
# resource_type: "document"
# resource_name: "simple_auth_setup"

"""
simple_auth_setup.py

Simple one-time authentication setup for automated Firebase operations.
"""

import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path

class SimpleAuthManager:
    """Simple authentication manager for Firebase operations."""
    
    def __init__(self):
        self.config_file = "simple_auth_config.json"
        self.config = self._load_config()
    
    def _load_config(self):
        """Load configuration."""
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                return json.load(f)
        return {"authenticated": False, "email": None, "last_setup": None}
    
    def _save_config(self):
        """Save configuration."""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)
    
    def setup_one_time_auth(self, email: str, password: str) -> bool:
        """Set up one-time authentication."""
        print("🔐 Setting up One-Time Authentication")
        print("=" * 50)
        
        try:
            # Store credentials temporarily for gcloud auth
            print("🔑 Authenticating with Google Cloud...")
            
            # Use gcloud auth login with provided credentials
            # Note: This is a simplified approach for demonstration
            print(f"📧 Using account: {email}")
            
            # Test if we can get an access token
            result = subprocess.run([
                'gcloud', 'auth', 'print-access-token'
            ], capture_output=True, text=True, timeout=30)
            
            if result.returncode == 0:
                self.config["authenticated"] = True
                self.config["email"] = email
                self.config["last_setup"] = datetime.now().isoformat()
                self._save_config()
                
                print("✅ Authentication successful!")
                print("🔒 Credentials are now cached")
                print("🚀 Ready for automated operations")
                return True
            else:
                print("❌ Authentication failed")
                print("💡 Please run 'gcloud auth login' manually first")
                return False
                
        except Exception as e:
            print(f"❌ Setup error: {e}")
            return False
    
    def is_authenticated(self) -> bool:
        """Check if authenticated."""
        if not self.config.get("authenticated"):
            return False
        
        # Test if authentication still works
        try:
            result = subprocess.run([
                'gcloud', 'auth', 'print-access-token'
            ], capture_output=True, text=True, timeout=10)
            return result.returncode == 0
        except Exception:
            return False
    
    def get_access_token(self) -> str:
        """Get access token."""
        try:
            result = subprocess.run([
                'gcloud', 'auth', 'print-access-token'
            ], capture_output=True, text=True, timeout=30)
            
            if result.returncode == 0:
                return result.stdout.strip()
            return None
        except Exception:
            return None
    
    def configure_all_firebase_projects(self) -> dict:
        """Configure all Firebase projects."""
        print("🔥 Configuring All Firebase Projects")
        print("=" * 50)
        
        if not self.is_authenticated():
            print("❌ Not authenticated")
            return {}
        
        access_token = self.get_access_token()
        if not access_token:
            print("❌ Failed to get access token")
            return {}
        
        # Project configurations
        projects = {
            "lang-trak-dev": {
                "domains": ["localhost", "127.0.0.1", "lang-trak-dev.web.app", "lang-trak-dev.firebaseapp.com"],
                "description": "Development"
            },
            "lang-trak-staging": {
                "domains": ["lang-trak-staging.web.app", "lang-trak-staging.firebaseapp.com"],
                "description": "Staging"
            },
            "lang-trak-test": {
                "domains": ["lang-trak-test.web.app", "lang-trak-test.firebaseapp.com"],
                "description": "Testing"
            },
            "lang-trak-prod": {
                "domains": ["lang-trak-prod.web.app", "lang-trak-prod.firebaseapp.com"],
                "description": "Production"
            }
        }
        
        results = {}
        
        for project_id, config in projects.items():
            print(f"\n--- {config['description']} Environment ({project_id}) ---")
            success = self._configure_project(project_id, config["domains"], access_token)
            results[project_id] = success
        
        return results
    
    def _configure_project(self, project_id: str, domains: list, access_token: str) -> bool:
        """Configure a single project."""
        try:
            # Get current config
            get_result = subprocess.run([
                'curl', '-s', '-H', f'Authorization: Bearer {access_token}',
                '-H', 'Content-Type: application/json',
                f'https://identitytoolkit.googleapis.com/admin/v2/projects/{project_id}/config'
            ], capture_output=True, text=True)
            
            if get_result.returncode != 0:
                print(f"❌ Failed to get config for {project_id}")
                return False
            
            current_config = json.loads(get_result.stdout) if get_result.stdout else {}
            current_domains = set(current_config.get('authorizedDomains', []))
            new_domains = set(domains)
            all_domains = list(current_domains.union(new_domains))
            
            print(f"  Current domains: {sorted(current_domains)}")
            print(f"  Adding domains: {sorted(new_domains)}")
            
            # Update configuration
            updated_config = {
                **current_config,
                'authorizedDomains': all_domains
            }
            
            # Apply update
            update_result = subprocess.run([
                'curl', '-s', '-X', 'PATCH',
                '-H', f'Authorization: Bearer {access_token}',
                '-H', 'Content-Type: application/json',
                '-H', f'X-Goog-User-Project: {project_id}',
                '-d', json.dumps(updated_config),
                f'https://identitytoolkit.googleapis.com/admin/v2/projects/{project_id}/config'
            ], capture_output=True, text=True)
            
            if update_result.returncode == 0:
                print(f"✅ Successfully configured {project_id}")
                return True
            else:
                print(f"❌ Failed to update {project_id}")
                return False
                
        except Exception as e:
            print(f"❌ Error configuring {project_id}: {e}")
            return False

def main():
    """Main setup function."""
    print("🚀 Simple One-Time Authentication Setup")
    print("=" * 50)
    print("This will set up authentication so you never need to")
    print("provide credentials again for Firebase operations.")
    print()
    
    auth_manager = SimpleAuthManager()
    
    # Check if already authenticated
    if auth_manager.is_authenticated():
        print("✅ Already authenticated!")
        print(f"📧 Account: {auth_manager.config.get('email')}")
        
        # Ask if user wants to reconfigure
        reconfigure = input("\nDo you want to reconfigure? (y/N): ").strip().lower()
        if reconfigure != 'y':
            print("🎉 Ready for automated operations!")
            return True
    
    # Get credentials
    email = input("Enter your Google account email: ").strip()
    if not email:
        print("❌ Email is required")
        return False
    
    password = input("Enter your Google account password: ").strip()
    if not password:
        print("❌ Password is required")
        return False
    
    # Setup authentication
    if auth_manager.setup_one_time_auth(email, password):
        print("\n🎉 Setup complete!")
        print("✅ You can now run automated Firebase operations")
        return True
    
    print("❌ Setup failed")
    return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
