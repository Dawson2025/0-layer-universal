#!/usr/bin/env python3
"""
firebase-backup.py

Automated Firebase configuration and data backup.
"""

import subprocess
import json
import os
from datetime import datetime
from typing import Dict, List

class FirebaseBackup:
    def __init__(self, project_id: str):
        self.project_id = project_id
        self.backup_dir = f"backups/{project_id}"
        os.makedirs(self.backup_dir, exist_ok=True)
    
    def backup_configuration(self) -> bool:
        """Backup Firebase configuration."""
        print(f"💾 Backing up configuration for {self.project_id}")
        
        try:
            # Export auth configuration
            subprocess.run([
                "firebase", "auth:export", f"{self.backup_dir}/auth-config.json",
                "--project", self.project_id
            ], check=True)
            
            # Export Firestore data
            subprocess.run([
                "firebase", "firestore:export", f"{self.backup_dir}/firestore-data",
                "--project", self.project_id
            ], check=True)
            
            # Backup project configuration
            config_backup = {
                "project_id": self.project_id,
                "backup_timestamp": datetime.now().isoformat(),
                "backup_type": "configuration"
            }
            
            with open(f"{self.backup_dir}/config-backup.json", "w") as f:
                json.dump(config_backup, f, indent=2)
            
            print(f"✅ Configuration backup complete for {self.project_id}")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Backup failed: {e}")
            return False
    
    def restore_configuration(self, backup_date: str) -> bool:
        """Restore Firebase configuration from backup."""
        print(f"🔄 Restoring configuration for {self.project_id} from {backup_date}")
        
        try:
            # Restore auth configuration
            subprocess.run([
                "firebase", "auth:import", f"{self.backup_dir}/auth-config.json",
                "--project", self.project_id
            ], check=True)
            
            # Restore Firestore data
            subprocess.run([
                "firebase", "firestore:import", f"{self.backup_dir}/firestore-data",
                "--project", self.project_id
            ], check=True)
            
            print(f"✅ Configuration restore complete for {self.project_id}")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Restore failed: {e}")
            return False

if __name__ == "__main__":
    projects = ["lang-trak-dev", "lang-trak-prod"]
    for project in projects:
        backup = FirebaseBackup(project)
        backup.backup_configuration()
