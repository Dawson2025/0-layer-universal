#!/usr/bin/env python3
"""
OAuth Consent Screen Automation Script
Automates the configuration of OAuth consent screen for Firebase projects
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

def create_oauth_consent_config():
    """Create OAuth consent screen configuration for all projects"""
    projects = {
        "dev": "lang-trak-dev",
        "staging": "lang-trak-staging", 
        "test": "lang-trak-test",
        "prod": "lang-trak-prod"
    }

    active_account = get_active_gcloud_account()
    if not active_account:
        print("❌ No active gcloud account found. Please run 'gcloud auth login'.")
        return False

    print(f"🔑 Current authenticated account: {active_account}")
    print("\n🚀 Starting OAuth Consent Screen Configuration")
    print("=" * 60)

    for env, project_id in projects.items():
        print(f"\n📋 Configuring {env.upper()} Project ({project_id})")
        print("-" * 40)
        
        # Step 1: Navigate to OAuth consent screen
        oauth_url = f"https://console.cloud.google.com/apis/credentials/consent?project={project_id}&authuser=1"
        print(f"🔗 OAuth Consent Screen URL: {oauth_url}")
        
        # Step 2: Open browser with the URL
        print("🌐 Opening browser...")
        try:
            subprocess.run(f"xdg-open '{oauth_url}'", shell=True, check=True)
            print("✅ Browser opened successfully")
        except Exception as e:
            print(f"⚠️ Could not open browser automatically: {e}")
            print(f"Please manually open: {oauth_url}")
        
        # Step 3: Wait for user to complete configuration
        print("\n📝 Manual Steps Required:")
        print("1. Click 'CONFIGURE CONSENT SCREEN' if not already configured")
        print("2. Choose 'External' user type")
        print("3. Fill in required fields:")
        print(f"   - App name: Lang Trak {env.capitalize()}")
        print(f"   - User support email: {active_account}")
        print(f"   - Developer contact: {active_account}")
        print("4. Save and continue")
        print("5. Add scopes (if needed): email, profile, openid")
        print("6. Add test users (if needed): {active_account}")
        print("7. Save and continue")
        print("8. Verify publishing status shows 'In production' or 'Testing'")
        
        # Step 4: Wait for user confirmation
        input(f"\n⏳ Press Enter when you've completed the OAuth consent screen setup for {project_id}...")
        
        # Step 5: Verify configuration
        print(f"🔍 Verifying configuration for {project_id}...")
        verify_command = f"curl -s -X GET \"https://identitytoolkit.googleapis.com/admin/v2/projects/{project_id}/config\" -H \"Authorization: Bearer $(gcloud auth print-access-token)\" -H \"X-Goog-User-Project: {project_id}\" -H \"Content-Type: application/json\""
        
        try:
            result = subprocess.run(verify_command, shell=True, capture_output=True, text=True, check=True)
            config = json.loads(result.stdout)
            
            if "signIn" in config and "enabledProviders" in config["signIn"]:
                if "GOOGLE" in config["signIn"]["enabledProviders"]:
                    print(f"✅ Google Sign-In is ENABLED for {project_id}")
                else:
                    print(f"⚠️ Google Sign-In is still DISABLED for {project_id}")
            else:
                print(f"⚠️ Could not verify Google Sign-In status for {project_id}")
                
        except Exception as e:
            print(f"⚠️ Error verifying {project_id}: {e}")
        
        print(f"✅ Completed configuration for {project_id}")
        print()

    print("🎉 OAuth Consent Screen Configuration Complete!")
    print("\n📋 Final Verification:")
    print("Run: python3 scripts/quick_verify.py")
    print("Expected Result: Google Sign-In should show as ✅ enabled for all projects")

def main():
    print("🚀 OAuth Consent Screen Automation")
    print("=" * 40)
    print("This script will guide you through configuring OAuth consent screen")
    print("for all Firebase projects with the correct Google account.")
    print()
    
    # Check authentication
    active_account = get_active_gcloud_account()
    if not active_account:
        print("❌ No active gcloud account found.")
        print("Please run: gcloud auth login")
        sys.exit(1)
    
    print(f"✅ Authenticated as: {active_account}")
    
    # Confirm account is correct
    if "2025computer2025@gmail.com" not in active_account:
        print("⚠️ Warning: Account doesn't match expected 2025computer2025@gmail.com")
        response = input("Continue anyway? (y/N): ")
        if response.lower() != 'y':
            print("Exiting...")
            sys.exit(1)
    
    # Start configuration
    create_oauth_consent_config()

if __name__ == "__main__":
    main()
