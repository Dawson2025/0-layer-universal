#!/usr/bin/env python3
# resource_id: "866f2a05-1f2d-46b1-a12f-af0e3743600b"
# resource_type: "document"
# resource_name: "final_google_signin_fix"
"""
Final Google Sign-In Fix Implementation
This script provides the complete solution for enabling Google Sign-In
by configuring OAuth consent screen and enabling the provider.
"""

import subprocess
import json
import sys
from pathlib import Path

def run_command(command, description):
    """Run a command using our robust terminal wrapper"""
    print(f"🔧 {description}...")
    try:
        # Use our robust terminal wrapper as per documentation
        wrapper_command = f"python3 scripts/terminal_wrapper.py \"{command}\""
        result = subprocess.run(wrapper_command, shell=True, capture_output=True, text=True, check=True)
        print(f"✅ {description} completed")
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e.stderr}")
        return None

def check_authentication():
    """Check current authentication status"""
    print("🔍 Checking authentication status...")
    
    # Check gcloud auth
    result = run_command("gcloud auth list --filter=status:ACTIVE --format='value(account)'", "Check active accounts")
    if result and "2025computer2025@gmail.com" in result:
        print(f"✅ Correct account authenticated: {result}")
        return True
    else:
        print(f"❌ Wrong account or not authenticated: {result}")
        print("   Please run: gcloud auth login")
        print("   Then select: 2025computer2025@gmail.com")
        return False

def verify_google_signin_status():
    """Verify current Google Sign-In status"""
    print("\n🔍 Verifying current Google Sign-In status...")
    
    projects = ["lang-trak-dev", "lang-trak-staging", "lang-trak-test", "lang-trak-prod"]
    
    for project in projects:
        print(f"\n📋 Checking {project}...")
        
        # Check Google Sign-In status via API
        command = f"""curl -s -X GET "https://identitytoolkit.googleapis.com/admin/v2/projects/{project}/config" \
            -H "Authorization: Bearer $(gcloud auth print-access-token)" \
            -H "X-Goog-User-Project: {project}" \
            -H "Content-Type: application/json" | jq -r '.signIn.enabledProviders[]?'"""
        
        result = run_command(command, f"Check Google Sign-In for {project}")
        
        if result and "GOOGLE" in result:
            print(f"✅ Google Sign-In is ENABLED for {project}")
        else:
            print(f"❌ Google Sign-In is DISABLED for {project}")

def provide_oauth_setup_instructions():
    """Provide comprehensive OAuth consent screen setup instructions"""
    print("\n📝 OAuth Consent Screen Setup Instructions")
    print("=" * 60)
    print("Google Sign-In requires OAuth consent screen configuration.")
    print("This must be done manually in the Google Cloud Console.")
    
    projects = {
        "lang-trak-dev": "Lang Trak Dev",
        "lang-trak-staging": "Lang Trak Staging", 
        "lang-trak-test": "Lang Trak Test",
        "lang-trak-prod": "Lang Trak Prod"
    }
    
    support_email = "2025computer2025@gmail.com"
    
    print(f"\n🔑 Make sure you're logged in as: {support_email}")
    print("   If not, go to: https://console.cloud.google.com/")
    print("   Click your profile picture → Switch account → Select 2025computer2025@gmail.com")
    
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

def provide_firebase_console_instructions():
    """Provide Firebase Console Google Sign-In enablement instructions"""
    print(f"\n🔥 Firebase Console Google Sign-In Setup")
    print("=" * 50)
    print("After OAuth consent screen is configured, enable Google Sign-In in Firebase Console:")
    
    projects = ["lang-trak-dev", "lang-trak-staging", "lang-trak-test", "lang-trak-prod"]
    
    for project in projects:
        print(f"\n🔗 {project.upper()}")
        print(f"   URL: https://console.firebase.google.com/u/1/project/{project}/authentication/providers")
        print(f"   Steps:")
        print(f"   1. Navigate to the URL above")
        print(f"   2. Find 'Google' in the providers table")
        print(f"   3. Click the 'Edit' button (pencil icon)")
        print(f"   4. Toggle 'Enable' to ON")
        print(f"   5. Enter support email: 2025computer2025@gmail.com")
        print(f"   6. Click 'Save'")

def main():
    """Main function"""
    print("🚀 Final Google Sign-In Fix Implementation")
    print("=" * 60)
    
    # Check authentication
    if not check_authentication():
        return False
    
    # Verify current status
    verify_google_signin_status()
    
    # Provide OAuth setup instructions
    provide_oauth_setup_instructions()
    
    # Provide Firebase Console instructions
    provide_firebase_console_instructions()
    
    print(f"\n🔧 After completing all setup steps:")
    print(f"   1. Run verification: python3 scripts/terminal_wrapper.py --script scripts/quick_verify.py")
    print(f"   2. Test authentication: python3 scripts/terminal_wrapper.py --script scripts/test_auth_flow.py")
    
    print(f"\n📋 Complete Setup Checklist:")
    print(f"   ☐ OAuth consent screen configured for all 4 projects")
    print(f"   ☐ Google Sign-In enabled in Firebase Console for all 4 projects")
    print(f"   ☐ Verification script shows: Google Sign-In: ✅")
    print(f"   ☐ Authentication flow test passes")
    
    print(f"\n🎯 Expected Result:")
    print(f"   Google Sign-In will be fully functional across all environments")
    print(f"   Users can sign in with their Google accounts")
    print(f"   API responses will show Google Sign-In as enabled")
    
    return True

if __name__ == "__main__":
    main()