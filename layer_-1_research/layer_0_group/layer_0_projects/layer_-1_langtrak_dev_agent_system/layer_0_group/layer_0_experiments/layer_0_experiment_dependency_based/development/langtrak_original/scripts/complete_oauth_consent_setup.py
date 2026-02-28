#!/usr/bin/env python3
"""
Complete OAuth Consent Screen Setup for Google Sign-In
This script provides comprehensive instructions for setting up OAuth consent screen
which is required for Google Sign-In to work properly.
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

def check_current_auth():
    """Check current authentication status"""
    print("🔍 Checking current authentication...")
    
    # Check if gcloud is authenticated
    result = run_command("gcloud auth list --filter=status:ACTIVE --format='value(account)'", "Check active accounts")
    if result:
        print(f"✅ Active account: {result}")
        return result
    else:
        print("❌ No active gcloud authentication found")
        return None

def main():
    """Main function"""
    print("🚀 Complete OAuth Consent Screen Setup for Google Sign-In")
    print("=" * 70)
    
    # Check authentication
    active_account = check_current_auth()
    if not active_account:
        print("❌ Please run 'gcloud auth login' first")
        return False
    
    projects = {
        "lang-trak-dev": "Lang Trak Dev",
        "lang-trak-staging": "Lang Trak Staging", 
        "lang-trak-test": "Lang Trak Test",
        "lang-trak-prod": "Lang Trak Prod"
    }
    
    support_email = "2025computer2025@gmail.com"
    
    print(f"\n📝 OAuth Consent Screen Setup Instructions")
    print("=" * 50)
    print("Google Sign-In requires OAuth consent screen configuration.")
    print("This must be done manually in the Google Cloud Console.")
    print(f"\n🔑 Current authenticated account: {active_account}")
    
    if "junk" in active_account.lower():
        print("⚠️  WARNING: You're using a junk account. Please switch to 2025computer2025@gmail.com")
        print("   Run: gcloud auth login")
        print("   Then select: 2025computer2025@gmail.com")
        return False
    
    print(f"\n✅ Account looks correct: {active_account}")
    
    for project_id, app_name in projects.items():
        print(f"\n🔗 {project_id.upper()}")
        print(f"   URL: https://console.cloud.google.com/apis/credentials/consent?project={project_id}")
        print(f"   Steps:")
        print(f"   1. Navigate to the URL above")
        print(f"   2. Click 'CONFIGURE CONSENT SCREEN'")
        print(f"   3. Choose 'External' user type")
        print(f"   4. Fill in required fields:")
        print(f"      - App name: {app_name}")
        print(f"      - User support email: {support_email}")
        print(f"      - Developer contact: {support_email}")
        print(f"   5. Save and continue")
        print(f"   6. Add scopes (if needed): email, profile, openid")
        print(f"   7. Add test users (if needed): {support_email}")
        print(f"   8. Save and continue")
        print(f"   9. Verify 'Publishing status' shows 'In production' or 'Testing'")
    
    print(f"\n🔧 After completing OAuth consent screen setup:")
    print(f"   1. Run verification: python3 scripts/quick_verify.py")
    print(f"   2. Test authentication: python3 scripts/test_auth_flow.py")
    
    print(f"\n📋 Quick Setup Checklist:")
    for project_id in projects.keys():
        print(f"   ☐ {project_id} - OAuth consent screen configured")
    
    print(f"\n🎯 Expected Result:")
    print(f"   After setup, Google Sign-In should show as 'Enabled' in API responses")
    print(f"   Verification script should show: Google Sign-In: ✅")
    
    return True

if __name__ == "__main__":
    main()
