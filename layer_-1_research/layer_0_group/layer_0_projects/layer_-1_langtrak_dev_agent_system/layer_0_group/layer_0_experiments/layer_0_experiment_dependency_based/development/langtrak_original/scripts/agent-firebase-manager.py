#!/usr/bin/env python3

"""
agent-firebase-manager.py

Demonstrates how an agentic AI can manage Firebase projects using service account authentication.
This script shows the complete workflow for programmatic Firebase management.
"""

import json
import os
import requests
from typing import List, Dict, Optional

class AgentFirebaseManager:
    def __init__(self, project_id: str, key_file: str):
        """Initialize the Firebase manager with service account authentication."""
        self.project_id = project_id
        self.key_file = key_file
        self.access_token = None
        self._load_credentials()
    
    def _load_credentials(self):
        """Load service account credentials and get access token."""
        print(f"🔐 Loading credentials for project: {self.project_id}")
        
        # Set environment variable for Google Auth
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = self.key_file
        
        try:
            from google.auth import default
            from google.auth.transport.requests import Request
            
            # Get default credentials (service account)
            credentials, project = default()
            
            # Refresh to get access token
            credentials.refresh(Request())
            self.access_token = credentials.token
            
            print(f"✅ Authentication successful for {self.project_id}")
            
        except Exception as e:
            print(f"❌ Authentication failed: {e}")
            raise
    
    def get_auth_config(self) -> Optional[Dict]:
        """Get current Firebase Auth configuration."""
        print(f"📋 Fetching auth configuration for {self.project_id}...")
        
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "X-Goog-User-Project": self.project_id,
            "Content-Type": "application/json"
        }
        
        url = f"https://identitytoolkit.googleapis.com/admin/v2/projects/{self.project_id}/config"
        
        try:
            response = requests.get(url, headers=headers)
            
            if response.status_code == 200:
                config = response.json()
                print("✅ Auth configuration retrieved")
                return config
            elif response.status_code == 404:
                print("⚠️ Auth configuration not found - needs initialization")
                return None
            else:
                print(f"❌ Failed to get config: {response.status_code} - {response.text}")
                return None
                
        except Exception as e:
            print(f"❌ Error fetching config: {e}")
            return None
    
    def configure_authorized_domains(self, domains: List[str]) -> bool:
        """Configure authorized domains for Firebase Auth."""
        print(f"🌐 Configuring authorized domains: {', '.join(domains)}")
        
        # Get current config first
        current_config = self.get_auth_config()
        if current_config is None:
            print("❌ Cannot configure domains - auth not initialized")
            return False
        
        # Merge with existing domains
        current_domains = current_config.get("authorizedDomains", [])
        new_domains = list(set(current_domains + domains))
        
        print(f"📝 Current domains: {', '.join(current_domains) if current_domains else '(none)'}")
        print(f"📝 New domains: {', '.join(domains)}")
        print(f"📝 Final domains: {', '.join(new_domains)}")
        
        # Prepare update
        update_data = {"authorizedDomains": new_domains}
        
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "X-Goog-User-Project": self.project_id,
            "Content-Type": "application/json"
        }
        
        url = f"https://identitytoolkit.googleapis.com/admin/v2/projects/{self.project_id}/config?updateMask=authorizedDomains"
        
        try:
            response = requests.patch(url, headers=headers, json=update_data)
            
            if response.status_code == 200:
                print("✅ Authorized domains updated successfully")
                return True
            else:
                print(f"❌ Failed to update domains: {response.status_code} - {response.text}")
                return False
                
        except Exception as e:
            print(f"❌ Error updating domains: {e}")
            return False
    
    def list_auth_providers(self) -> Optional[List[Dict]]:
        """List configured authentication providers."""
        print(f"🔍 Listing auth providers for {self.project_id}...")
        
        config = self.get_auth_config()
        if config:
            providers = config.get("signIn", {}).get("providers", [])
            print(f"📋 Found {len(providers)} auth providers")
            for provider in providers:
                print(f"  - {provider.get('providerId', 'unknown')}")
            return providers
        return None

def main():
    """Demonstrate agentic Firebase management."""
    print("🤖 Agentic Firebase Manager Demo")
    print("=" * 50)
    
    # Configuration
    projects = [
        {
            "id": "lang-trak-dev",
            "key_file": "keys/lang-trak-dev-agent-key.json"
        }
    ]
    
    domains_to_add = ["localhost", "127.0.0.1"]
    
    for project_config in projects:
        project_id = project_config["id"]
        key_file = project_config["key_file"]
        
        print(f"\n🎯 Managing project: {project_id}")
        
        try:
            # Initialize manager
            manager = AgentFirebaseManager(project_id, key_file)
            
            # Get current configuration
            config = manager.get_auth_config()
            if config:
                print("✅ Firebase Auth is configured")
                
                # List current providers
                manager.list_auth_providers()
                
                # Configure authorized domains
                success = manager.configure_authorized_domains(domains_to_add)
                if success:
                    print(f"✅ {project_id} domain configuration complete")
                else:
                    print(f"❌ {project_id} domain configuration failed")
            else:
                print(f"⚠️ {project_id} Firebase Auth needs initialization")
                
        except Exception as e:
            print(f"❌ Error managing {project_id}: {e}")
    
    print("\n🎉 Agentic Firebase management complete!")

if __name__ == "__main__":
    main()

