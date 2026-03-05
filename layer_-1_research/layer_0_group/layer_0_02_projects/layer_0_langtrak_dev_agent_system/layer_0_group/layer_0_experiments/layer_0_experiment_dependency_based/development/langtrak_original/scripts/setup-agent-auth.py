#!/usr/bin/env python3
# resource_id: "562b93d8-c6d8-40c3-9df6-c85e8524a700"
# resource_type: "document"
# resource_name: "setup-agent-auth"

"""
setup-agent-auth.py

Sets up authentication for agentic AI to manage Firebase projects.
This script creates service accounts and downloads credentials that can be used
by agentic AI systems to authenticate with Google Cloud and Firebase APIs.
"""

import subprocess
import json
import os
from typing import List, Dict, Optional

def run_command(cmd: str, project: str = None) -> Optional[str]:
    """Run a gcloud command and return stdout."""
    try:
        full_cmd = f"gcloud {cmd}"
        if project:
            full_cmd += f" --project={project}"
        
        result = subprocess.run(full_cmd.split(), capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {full_cmd}")
        print(f"Error: {e.stderr}")
        return None

def create_service_account(project: str, sa_name: str, display_name: str) -> bool:
    """Create a service account for the project."""
    print(f"Creating service account '{sa_name}' for project '{project}'...")
    
    cmd = f"iam service-accounts create {sa_name} --display-name={display_name}"
    result = run_command(cmd, project)
    
    if result is not None:
        print(f"✅ Service account '{sa_name}' created successfully")
        return True
    else:
        print(f"❌ Failed to create service account '{sa_name}'")
        return False

def grant_roles(project: str, sa_email: str, roles: List[str]) -> bool:
    """Grant roles to the service account."""
    print(f"Granting roles to service account '{sa_email}'...")
    
    for role in roles:
        print(f"  Granting role: {role}")
        cmd = f"projects add-iam-policy-binding {project} --member='serviceAccount:{sa_email}' --role='{role}'"
        result = run_command(cmd)
        
        if result is None:
            print(f"❌ Failed to grant role {role}")
            return False
    
    print("✅ All roles granted successfully")
    return True

def create_key(project: str, sa_email: str, key_file: str) -> bool:
    """Create and download a service account key."""
    print(f"Creating key for service account '{sa_email}'...")
    
    cmd = f"iam service-accounts keys create {key_file} --iam-account={sa_email}"
    result = run_command(cmd, project)
    
    if result is not None:
        print(f"✅ Key created and saved to '{key_file}'")
        return True
    else:
        print(f"❌ Failed to create key for service account")
        return False

def setup_agent_authentication(project: str) -> bool:
    """Set up complete authentication for agentic AI."""
    print(f"\n🚀 Setting up agent authentication for project: {project}")
    
    # Service account details
    sa_name = "firebase-admin-agent"
    sa_email = f"{sa_name}@{project}.iam.gserviceaccount.com"
    key_file = f"keys/{project}-agent-key.json"
    
    # Required roles for Firebase management
    roles = [
        "roles/firebase.admin",
        "roles/identitytoolkit.admin", 
        "roles/iam.serviceAccountUser",
        "roles/resourcemanager.projectIamAdmin"
    ]
    
    # Create keys directory
    os.makedirs("keys", exist_ok=True)
    
    # Step 1: Create service account
    if not create_service_account(project, sa_name, f"FirebaseAdminAgent"):
        return False
    
    # Step 2: Grant necessary roles
    if not grant_roles(project, sa_email, roles):
        return False
    
    # Step 3: Create and download key
    if not create_key(project, sa_email, key_file):
        return False
    
    # Step 4: Create authentication script
    auth_script = f"""#!/bin/bash
# Authentication setup for agentic AI - {project}
export GOOGLE_APPLICATION_CREDENTIALS="$(pwd)/{key_file}"
export GOOGLE_CLOUD_PROJECT="{project}"
echo "✅ Agent authentication configured for {project}"
echo "Service Account: {sa_email}"
echo "Key File: {key_file}"
"""
    
    with open(f"keys/{project}-auth.sh", "w") as f:
        f.write(auth_script)
    
    os.chmod(f"keys/{project}-auth.sh", 0o755)
    
    print(f"\n🎉 Agent authentication setup complete for {project}!")
    print(f"📁 Key file: {key_file}")
    print(f"🔑 Service account: {sa_email}")
    print(f"🚀 To use: source keys/{project}-auth.sh")
    
    return True

def main():
    projects = ["lang-trak-dev", "lang-trak-prod"]
    
    print("🤖 Setting up authentication for agentic AI")
    print("=" * 50)
    
    for project in projects:
        if setup_agent_authentication(project):
            print(f"✅ {project}: Authentication setup complete")
        else:
            print(f"❌ {project}: Authentication setup failed")
        print()
    
    print("🎯 Next steps:")
    print("1. Use the generated key files for programmatic authentication")
    print("2. Set GOOGLE_APPLICATION_CREDENTIALS environment variable")
    print("3. Agentic AI can now authenticate and manage Firebase projects")

if __name__ == "__main__":
    main()
