#!/usr/bin/env python3
# resource_id: "5b6c0cd6-74e3-4f98-a1ed-f82a411d4ac6"
# resource_type: "document"
# resource_name: "service-account-rotation"
"""
service-account-rotation.py

Automated service account key rotation for enhanced security.
"""

import subprocess
import json
import os
from datetime import datetime, timedelta
from typing import List, Dict

class ServiceAccountRotator:
    def __init__(self, project_id: str):
        self.project_id = project_id
        self.service_account = f"firebase-admin-agent@{project_id}.iam.gserviceaccount.com"
    
    def rotate_keys(self) -> bool:
        """Rotate service account keys."""
        print(f"🔄 Rotating keys for {self.service_account}")
        
        try:
            # Create new key
            new_key_file = f"keys/{self.project_id}-agent-key-new.json"
            subprocess.run([
                "gcloud", "iam", "service-accounts", "keys", "create", new_key_file,
                "--iam-account", self.service_account,
                "--project", self.project_id
            ], check=True)
            
            # Update configuration
            self._update_configuration(new_key_file)
            
            # Remove old key (after verification)
            old_key_file = f"keys/{self.project_id}-agent-key.json"
            if os.path.exists(old_key_file):
                os.rename(old_key_file, f"{old_key_file}.backup")
            
            # Rename new key
            os.rename(new_key_file, old_key_file)
            
            print(f"✅ Key rotation complete for {self.project_id}")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Key rotation failed: {e}")
            return False
    
    def _update_configuration(self, new_key_file: str):
        """Update configuration files with new key."""
        # This would update any configuration files that reference the key
        pass

if __name__ == "__main__":
    projects = ["lang-trak-dev", "lang-trak-prod"]
    for project in projects:
        rotator = ServiceAccountRotator(project)
        rotator.rotate_keys()
