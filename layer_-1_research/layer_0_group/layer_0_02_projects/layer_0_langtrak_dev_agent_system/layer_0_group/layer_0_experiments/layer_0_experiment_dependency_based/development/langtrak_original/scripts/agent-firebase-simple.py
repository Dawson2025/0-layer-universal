#!/usr/bin/env python3
# resource_id: "e6cacaf1-1bdb-4d7d-85c4-be32d902482f"
# resource_type: "document"
# resource_name: "agent-firebase-simple"

"""
agent-firebase-simple.py

Simple agentic Firebase manager using gcloud authentication.
This demonstrates the most reliable approach for agentic AI.
"""

import json
import subprocess
import sys
from typing import List, Dict, Optional

class SimpleAgentFirebaseManager:
    def __init__(self, project_id: str):
        """Initialize with project ID."""
        self.project_id = project_id
        self.access_token = None
    
    def get_access_token(self) -> bool:
        """Get access token using gcloud."""
        print(f"🔐 Getting access token for {self.project_id}...")
        
        try:
            # Set the project
            subprocess.run(
                ["gcloud", "config", "set", "project", self.project_id],
                check=True, capture_output=True
            )
            
            # Get access token
            result = subprocess.run(
                ["gcloud", "auth", "print-access-token"],
                check=True, capture_output=True, text=True
            )
            
            self.access_token = result.stdout.strip()
            print("✅ Access token obtained")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to get access token: {e}")
            return False
    
    def get_auth_config(self) -> Optional[Dict]:
        """Get current Firebase Auth configuration."""
        if not self.access_token:
            print("❌ No access token available")
            return None
        
        print(f"📋 Fetching auth configuration for {self.project_id}...")
        
        import requests
        
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
                print(f"❌ Failed to get config: {response.status_code}")
                print(f"Response: {response.text}")
                return None
                
        except Exception as e:
            print(f"❌ Error fetching config: {e}")
            return None
    
    def configure_authorized_domains(self, domains: List[str]) -> bool:
        """Configure authorized domains for Firebase Auth."""
        if not self.access_token:
            print("❌ No access token available")
            return False
        
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
        print(f"📝 Adding domains: {', '.join(domains)}")
        print(f"📝 Final domains: {', '.join(new_domains)}")
        
        # Prepare update
        update_data = {"authorizedDomains": new_domains}
        
        import requests
        
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
                print(f"❌ Failed to update domains: {response.status_code}")
                print(f"Response: {response.text}")
                return False
                
        except Exception as e:
            print(f"❌ Error updating domains: {e}")
            return False

def main():
    """Demonstrate simple agentic Firebase management."""
    print("🤖 Simple Agentic Firebase Manager")
    print("=" * 50)
    
    # Configuration
    projects = ["lang-trak-dev", "lang-trak-prod"]
    domains_to_add = ["localhost", "127.0.0.1"]
    
    for project_id in projects:
        print(f"\n🎯 Managing project: {project_id}")
        
        try:
            # Initialize manager
            manager = SimpleAgentFirebaseManager(project_id)
            
            # Get access token
            if not manager.get_access_token():
                print(f"❌ Cannot authenticate to {project_id}")
                continue
            
            # Get current configuration
            config = manager.get_auth_config()
            if config:
                print("✅ Firebase Auth is configured")
                
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
    
    print("\n🎉 Simple agentic Firebase management complete!")

if __name__ == "__main__":
    main()

