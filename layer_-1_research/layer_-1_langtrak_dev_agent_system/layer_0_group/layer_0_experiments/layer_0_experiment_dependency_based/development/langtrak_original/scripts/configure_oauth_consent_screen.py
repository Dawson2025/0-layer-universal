#!/usr/bin/env python3
"""
Configure OAuth Consent Screen for Google Sign-In
This script sets up the OAuth consent screen which is required for Google Sign-In to work.
"""

import subprocess
import json
import sys
from pathlib import Path

def run_command(command, description):
    """Run a command and return the result"""
    print(f"🔧 {description}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        print(f"✅ {description} completed")
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e.stderr}")
        return None

def configure_oauth_consent_screen(project_id, app_name, support_email):
    """Configure OAuth consent screen for a project"""
    print(f"\n📋 Configuring OAuth consent screen for {project_id}...")
    
    # Step 1: Create OAuth consent screen configuration
    consent_config = {
        "displayName": app_name,
        "supportEmail": support_email,
        "userType": "EXTERNAL",
        "developerContactInformation": {
            "email": support_email
        }
    }
    
    # Step 2: Try to create the consent screen via API
    # Note: This might require different API endpoints or manual setup
    print(f"⚠️  OAuth consent screen configuration requires manual setup in Google Cloud Console")
    print(f"   Project: {project_id}")
    print(f"   App Name: {app_name}")
    print(f"   Support Email: {support_email}")
    
    return True

def enable_google_signin_after_consent(project_id):
    """Enable Google Sign-In after OAuth consent screen is configured"""
    print(f"\n🔧 Enabling Google Sign-In for {project_id}...")
    
    # Try to enable Google Sign-In via API
    command = f"""curl -s -X PATCH 'https://identitytoolkit.googleapis.com/admin/v2/projects/{project_id}/config' \
        -H 'Authorization: Bearer $(gcloud auth print-access-token)' \
        -H 'X-Goog-User-Project: {project_id}' \
        -H 'Content-Type: application/json' \
        -d '{{"signIn":{{"email":{{"enabled":true}},"google":{{"enabled":true}}}}}}'"""
    
    result = run_command(command, f"Enable Google Sign-In for {project_id}")
    
    if result and "error" not in result:
        print(f"✅ Google Sign-In enabled for {project_id}")
        return True
    else:
        print(f"❌ Failed to enable Google Sign-In for {project_id}")
        if result:
            print(f"   Error: {result}")
        return False

def main():
    """Main function"""
    print("🚀 OAuth Consent Screen Configuration for Google Sign-In")
    print("=" * 60)
    
    projects = {
        "lang-trak-dev": "Lang Trak Dev",
        "lang-trak-staging": "Lang Trak Staging", 
        "lang-trak-test": "Lang Trak Test",
        "lang-trak-prod": "Lang Trak Prod"
    }
    
    support_email = "2025computer2025@gmail.com"
    
    print(f"\n📝 Manual OAuth Consent Screen Setup Required")
    print("=" * 50)
    print("Google Sign-In requires OAuth consent screen configuration.")
    print("Please follow these steps for each project:")
    
    for project_id, app_name in projects.items():
        print(f"\n🔗 {project_id.upper()}")
        print(f"   URL: https://console.cloud.google.com/apis/credentials/consent?project={project_id}")
        print(f"   Steps:")
        print(f"   1. Click 'CONFIGURE CONSENT SCREEN'")
        print(f"   2. Choose 'External' user type")
        print(f"   3. Fill in required fields:")
        print(f"      - App name: {app_name}")
        print(f"      - User support email: {support_email}")
        print(f"      - Developer contact: {support_email}")
        print(f"   4. Save and continue")
        print(f"   5. Add scopes (if needed): email, profile, openid")
        print(f"   6. Add test users (if needed): {support_email}")
        print(f"   7. Save and continue")
    
    print(f"\n✅ After completing OAuth consent screen setup for all projects:")
    print(f"   Run: python3 scripts/quick_verify.py")
    
    return True

if __name__ == "__main__":
    main()
