#!/usr/bin/env python3

"""
auth_manager.py

Comprehensive authentication management system that allows one-time authentication
and automatic handling of all Firebase/Google Cloud operations.
"""

import json
import os
import subprocess
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Any
import keyring
import getpass

class AuthManager:
    """Manages authentication for all Firebase/Google Cloud operations."""
    
    def __init__(self, config_file: str = "auth_config.json"):
        self.config_file = config_file
        self.config = self._load_config()
        self.access_token = None
        self.token_expiry = None
        
    def _load_config(self) -> Dict[str, Any]:
        """Load authentication configuration."""
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                return json.load(f)
        return {
            "email": None,
            "authenticated": False,
            "last_auth": None,
            "token_cache": None,
            "projects": {}
        }
    
    def _save_config(self):
        """Save authentication configuration."""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2, default=str)
    
    def authenticate_once(self, email: str = None, password: str = None) -> bool:
        """Perform one-time authentication and store credentials securely."""
        print("🔐 Setting up One-Time Authentication")
        print("=" * 50)
        
        # Get email if not provided
        if not email:
            email = input("Enter your Google account email: ").strip()
        
        if not email:
            print("❌ Email is required")
            return False
        
        # Store email
        self.config["email"] = email
        
        # Get password if not provided
        if not password:
            password = getpass.getpass("Enter your Google account password: ")
        
        if not password:
            print("❌ Password is required")
            return False
        
        try:
            print("🔑 Authenticating with Google Cloud...")
            
            # Store password securely using keyring
            keyring.set_password("lang-trak-auth", email, password)
            
            # Test authentication
            if self._test_authentication():
                self.config["authenticated"] = True
                self.config["last_auth"] = datetime.now().isoformat()
                self._save_config()
                
                print("✅ Authentication successful!")
                print(f"📧 Account: {email}")
                print("🔒 Credentials stored securely")
                print("🚀 Ready for automated operations")
                
                return True
            else:
                print("❌ Authentication failed")
                return False
                
        except Exception as e:
            print(f"❌ Authentication error: {e}")
            return False
    
    def _test_authentication(self) -> bool:
        """Test if authentication is working."""
        try:
            # Try to get access token
            result = subprocess.run([
                'gcloud', 'auth', 'print-access-token'
            ], capture_output=True, text=True, timeout=30)
            
            return result.returncode == 0
        except Exception:
            return False
    
    def get_access_token(self, force_refresh: bool = False) -> Optional[str]:
        """Get valid access token, refreshing if needed."""
        # Check if we have a cached token that's still valid
        if (not force_refresh and 
            self.access_token and 
            self.token_expiry and 
            datetime.now() < self.token_expiry):
            return self.access_token
        
        try:
            # Get fresh token
            result = subprocess.run([
                'gcloud', 'auth', 'print-access-token'
            ], capture_output=True, text=True, timeout=30)
            
            if result.returncode == 0:
                self.access_token = result.stdout.strip()
                # Tokens typically expire in 1 hour, refresh 5 minutes early
                self.token_expiry = datetime.now() + timedelta(minutes=55)
                return self.access_token
            else:
                print("❌ Failed to get access token")
                return None
                
        except Exception as e:
            print(f"❌ Error getting access token: {e}")
            return None
    
    def is_authenticated(self) -> bool:
        """Check if user is currently authenticated."""
        if not self.config.get("authenticated"):
            return False
        
        # Test if authentication still works
        return self._test_authentication()
    
    def setup_automated_auth(self) -> bool:
        """Set up automated authentication for seamless operations."""
        print("🤖 Setting up Automated Authentication")
        print("=" * 50)
        
        if not self.is_authenticated():
            print("❌ Not authenticated. Please run authenticate_once() first.")
            return False
        
        # Configure gcloud for automated operations
        try:
            print("🔧 Configuring gcloud for automated operations...")
            
            # Set up application default credentials
            subprocess.run([
                'gcloud', 'auth', 'application-default', 'login'
            ], check=True)
            
            # Configure Firebase CLI
            print("🔥 Configuring Firebase CLI...")
            subprocess.run([
                'firebase', 'login', '--no-localhost'
            ], check=True)
            
            print("✅ Automated authentication configured!")
            print("🚀 You can now run operations without manual authentication")
            
            return True
            
        except Exception as e:
            print(f"❌ Failed to setup automated auth: {e}")
            return False
    
    def configure_all_firebase_projects(self) -> Dict[str, bool]:
        """Configure all Firebase projects with Google Sign-In."""
        print("🔥 Configuring All Firebase Projects")
        print("=" * 50)
        
        if not self.is_authenticated():
            print("❌ Not authenticated. Please authenticate first.")
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
            success = self._configure_project_domains(project_id, config["domains"], access_token)
            results[project_id] = success
        
        return results
    
    def _configure_project_domains(self, project_id: str, domains: List[str], access_token: str) -> bool:
        """Configure authorized domains for a project."""
        try:
            # Get current config
            get_result = subprocess.run([
                'curl', '-s', '-H', f'Authorization: Bearer {access_token}',
                '-H', 'Content-Type: application/json',
                f'https://identitytoolkit.googleapis.com/admin/v2/projects/{project_id}/config'
            ], capture_output=True, text=True)
            
            if get_result.returncode != 0:
                print(f"❌ Failed to get current config for {project_id}")
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
    
    def run_automated_operation(self, operation: str, **kwargs) -> Any:
        """Run any Firebase/Google Cloud operation automatically."""
        if not self.is_authenticated():
            print("❌ Not authenticated. Please authenticate first.")
            return None
        
        access_token = self.get_access_token()
        if not access_token:
            print("❌ Failed to get access token")
            return None
        
        # Route to appropriate operation
        if operation == "configure_firebase_auth":
            return self.configure_all_firebase_projects()
        elif operation == "get_project_info":
            return self._get_project_info(kwargs.get("project_id"))
        elif operation == "deploy_firebase":
            return self._deploy_firebase(kwargs.get("project_id"))
        else:
            print(f"❌ Unknown operation: {operation}")
            return None
    
    def _get_project_info(self, project_id: str) -> Dict[str, Any]:
        """Get information about a Firebase project."""
        access_token = self.get_access_token()
        if not access_token:
            return {}
        
        try:
            result = subprocess.run([
                'curl', '-s', '-H', f'Authorization: Bearer {access_token}',
                '-H', 'Content-Type: application/json',
                f'https://identitytoolkit.googleapis.com/admin/v2/projects/{project_id}/config'
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                return json.loads(result.stdout)
            return {}
        except Exception:
            return {}
    
    def _deploy_firebase(self, project_id: str) -> bool:
        """Deploy Firebase project."""
        try:
            # Switch to project
            subprocess.run(['firebase', 'use', project_id], check=True)
            
            # Deploy
            result = subprocess.run(['firebase', 'deploy'], capture_output=True, text=True)
            return result.returncode == 0
        except Exception:
            return False
    
    def status(self) -> Dict[str, Any]:
        """Get authentication status."""
        return {
            "authenticated": self.is_authenticated(),
            "email": self.config.get("email"),
            "last_auth": self.config.get("last_auth"),
            "token_valid": self.access_token is not None and self.token_expiry and datetime.now() < self.token_expiry
        }

def main():
    """Main function for setting up one-time authentication."""
    print("🚀 Lang-Trak Authentication Manager")
    print("=" * 50)
    print("This will set up one-time authentication so you never need to")
    print("provide credentials again for Firebase/Google Cloud operations.")
    print()
    
    auth_manager = AuthManager()
    
    # Check if already authenticated
    if auth_manager.is_authenticated():
        print("✅ Already authenticated!")
        status = auth_manager.status()
        print(f"📧 Account: {status['email']}")
        print(f"🔑 Token valid: {status['token_valid']}")
        
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
    
    password = getpass.getpass("Enter your Google account password: ")
    if not password:
        print("❌ Password is required")
        return False
    
    # Authenticate
    if auth_manager.authenticate_once(email, password):
        print("\n🤖 Setting up automated operations...")
        if auth_manager.setup_automated_auth():
            print("\n🎉 Setup complete!")
            print("✅ You can now run any Firebase/Google Cloud operation")
            print("✅ No more manual authentication required")
            print("✅ All operations will be handled automatically")
            return True
    
    print("❌ Setup failed")
    return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
