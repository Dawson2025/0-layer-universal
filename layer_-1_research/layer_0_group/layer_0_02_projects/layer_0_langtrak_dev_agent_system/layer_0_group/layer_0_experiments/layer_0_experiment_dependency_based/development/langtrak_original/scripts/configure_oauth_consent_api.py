#!/usr/bin/env python3
# resource_id: "a2754826-ad50-4c70-9763-f736ae91b370"
# resource_type: "document"
# resource_name: "configure_oauth_consent_api"
"""
OAuth Consent Screen Configuration via API
Configures OAuth consent screen for Firebase projects using Google Cloud APIs
"""

import subprocess
import json
import time
import sys
from pathlib import Path

def get_active_gcloud_account():
    """Get the currently active gcloud account"""
    try:
        result = subprocess.run(
            "gcloud auth list --filter=status:ACTIVE --format='value(account)'",
            shell=True,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except Exception as e:
        print(f"Error getting active gcloud account: {e}")
        return None

def get_access_token():
    """Get access token for API calls"""
    try:
        result = subprocess.run(
            "gcloud auth print-access-token",
            shell=True,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except Exception as e:
        print(f"Error getting access token: {e}")
        return None

def configure_oauth_consent_screen(project_id, app_name, support_email):
    """Configure OAuth consent screen for a project"""
    try:
        access_token = get_access_token()
        if not access_token:
            print(f"❌ Failed to get access token for {project_id}")
            return False

        # OAuth consent screen configuration
        consent_config = {
            "displayName": app_name,
            "supportEmail": support_email,
            "userType": "EXTERNAL",
            "consentScreen": {
                "displayName": app_name,
                "supportEmail": support_email,
                "privacyPolicyUrl": f"https://{project_id}.web.app/privacy",
                "termsOfServiceUrl": f"https://{project_id}.web.app/terms"
            }
        }

        # Make API call to configure OAuth consent screen
        url = f"https://oauth2.googleapis.com/v1/projects/{project_id}/consentScreen"
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }

        command = f'curl -s -X PATCH "{url}" -H "Authorization: Bearer {access_token}" -H "Content-Type: application/json" -d \'{json.dumps(consent_config)}\''
        
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        
        if result.returncode == 0:
            print(f"✅ OAuth consent screen configured for {project_id}")
            return True
        else:
            print(f"❌ Failed to configure OAuth consent screen for {project_id}: {result.stderr}")
            return False

    except Exception as e:
        print(f"❌ Error configuring OAuth consent screen for {project_id}: {e}")
        return False

def main():
    """Main function to configure OAuth consent screen for all projects"""
    print("🚀 OAuth Consent Screen Configuration via API")
    print("=" * 50)
    
    # Check authentication
    active_account = get_active_gcloud_account()
    if not active_account:
        print("❌ No active gcloud account found. Please run 'gcloud auth login'.")
        return
    
    print(f"🔑 Current authenticated account: {active_account}")
    
    # Project configurations
    projects = {
        "dev": "lang-trak-dev",
        "staging": "lang-trak-staging",
        "test": "lang-trak-test",
        "prod": "lang-trak-prod"
    }
    
    success_count = 0
    total_projects = len(projects)
    
    for env, project_id in projects.items():
        app_name = f"Lang Trak {env.capitalize()}"
        support_email = active_account
        
        print(f"\n📋 Configuring {env.upper()} project ({project_id})...")
        
        if configure_oauth_consent_screen(project_id, app_name, support_email):
            success_count += 1
        else:
            print(f"⚠️  Failed to configure OAuth consent screen for {project_id}")
    
    print(f"\n📊 Results: {success_count}/{total_projects} projects configured successfully")
    
    if success_count == total_projects:
        print("🎉 All OAuth consent screens configured successfully!")
        print("\n🔧 Next steps:")
        print("1. Run verification: python3 scripts/quick_verify.py")
        print("2. Test authentication: python3 scripts/test_auth_flow.py")
    else:
        print("⚠️  Some projects may need manual configuration")
        print("\n🔧 Manual steps:")
        for env, project_id in projects.items():
            print(f"   - {project_id}: https://console.cloud.google.com/apis/credentials/consent?project={project_id}")

if __name__ == "__main__":
    main()