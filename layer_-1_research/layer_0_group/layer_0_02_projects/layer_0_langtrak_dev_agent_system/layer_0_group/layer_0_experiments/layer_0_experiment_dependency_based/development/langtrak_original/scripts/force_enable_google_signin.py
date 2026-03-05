#!/usr/bin/env python3
# resource_id: "b2cc555b-53c7-4bc0-967b-c3a802702d2f"
# resource_type: "document"
# resource_name: "force_enable_google_signin"
"""
Force Enable Google Sign-In via API
Directly enables Google Sign-In provider for all Firebase projects using the Identity Toolkit Admin API
"""

import subprocess
import json
import time
import sys
from pathlib import Path

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

def get_current_config(project_id, access_token):
    """Get current Firebase Auth configuration"""
    try:
        command = f"curl -s -X GET \"https://identitytoolkit.googleapis.com/admin/v2/projects/{project_id}/config\" -H \"Authorization: Bearer {access_token}\" -H \"X-Goog-User-Project: {project_id}\" -H \"Content-Type: application/json\""
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return json.loads(result.stdout)
    except Exception as e:
        print(f"Error getting current config for {project_id}: {e}")
        return None

def enable_google_provider_api(project_id, access_token):
    """Enable Google Sign-In provider via API"""
    try:
        # First, get the current configuration
        current_config = get_current_config(project_id, access_token)
        if not current_config:
            print(f"❌ Could not get current config for {project_id}")
            return False
        
        print(f"📋 Current config for {project_id}:")
        print(f"   - signIn: {current_config.get('signIn', 'Not found')}")
        
        # Prepare the update payload
        # The API expects the configuration in a specific format
        update_payload = {
            "signIn": {
                "enabledProviders": ["GOOGLE"]
            }
        }
        
        # If there's already a signIn config, merge it
        if "signIn" in current_config:
            existing_signin = current_config["signIn"]
            if "enabledProviders" in existing_signin:
                # Add GOOGLE to existing providers if not already present
                existing_providers = existing_signin["enabledProviders"]
                if "GOOGLE" not in existing_providers:
                    existing_providers.append("GOOGLE")
                update_payload["signIn"]["enabledProviders"] = existing_providers
            else:
                # If no enabledProviders, just set GOOGLE
                update_payload["signIn"]["enabledProviders"] = ["GOOGLE"]
        else:
            # No existing signIn config, create new one
            update_payload["signIn"]["enabledProviders"] = ["GOOGLE"]
        
        print(f"📝 Update payload for {project_id}:")
        print(f"   - signIn.enabledProviders: {update_payload['signIn']['enabledProviders']}")
        
        # Make the API call to update the configuration
        payload_json = json.dumps(update_payload)
        command = f"curl -s -X PATCH \"https://identitytoolkit.googleapis.com/admin/v2/projects/{project_id}/config\" -H \"Authorization: Bearer {access_token}\" -H \"X-Goog-User-Project: {project_id}\" -H \"Content-Type: application/json\" -d '{payload_json}'"
        
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        response = json.loads(result.stdout)
        
        print(f"✅ API response for {project_id}:")
        print(f"   - Response: {response}")
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ API call failed for {project_id}: {e}")
        print(f"   - Stderr: {e.stderr}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error for {project_id}: {e}")
        return False

def verify_google_provider(project_id, access_token):
    """Verify Google Sign-In provider status"""
    try:
        current_config = get_current_config(project_id, access_token)
        if not current_config:
            return False
        
        if "signIn" in current_config and "enabledProviders" in current_config["signIn"]:
            return "GOOGLE" in current_config["signIn"]["enabledProviders"]
        return False
    except Exception as e:
        print(f"Error verifying Google provider for {project_id}: {e}")
        return False

def main():
    """Main function to force enable Google Sign-In for all projects"""
    projects = {
        "dev": "lang-trak-dev",
        "staging": "lang-trak-staging",
        "test": "lang-trak-test",
        "prod": "lang-trak-prod"
    }
    
    print("🚀 Force Enable Google Sign-In via API")
    print("=" * 50)
    
    # Get access token
    access_token = get_access_token()
    if not access_token:
        print("❌ Failed to get access token. Please run 'gcloud auth login' first.")
        sys.exit(1)
    
    print(f"🔑 Access token obtained successfully")
    print()
    
    # Enable Google Sign-In for each project
    enabled_count = 0
    for env, project_id in projects.items():
        print(f"📋 Processing {env.upper()} project ({project_id})...")
        
        # Check current status
        current_status = verify_google_provider(project_id, access_token)
        print(f"   - Current status: {'ENABLED' if current_status else 'DISABLED'}")
        
        if current_status:
            print(f"   - Google Sign-In already enabled for {project_id}")
            enabled_count += 1
        else:
            # Enable Google Sign-In
            if enable_google_provider_api(project_id, access_token):
                print(f"   - ✅ Google Sign-In enabled for {project_id}")
                enabled_count += 1
            else:
                print(f"   - ❌ Failed to enable Google Sign-In for {project_id}")
        
        print()
    
    # Final verification
    print("🔍 Final verification...")
    all_enabled = True
    for env, project_id in projects.items():
        status = verify_google_provider(project_id, access_token)
        if status:
            print(f"✅ {env.upper()}: Google Sign-In ENABLED")
        else:
            print(f"❌ {env.upper()}: Google Sign-In DISABLED")
            all_enabled = False
    
    print(f"\n📊 Results: {enabled_count}/{len(projects)} projects enabled")
    if all_enabled:
        print("🎉 All Google Sign-In providers are now ENABLED!")
    else:
        print("⚠️ Some Google Sign-In providers are still DISABLED.")
        print("💡 This might be due to API limitations or project configuration issues.")

if __name__ == "__main__":
    main()
