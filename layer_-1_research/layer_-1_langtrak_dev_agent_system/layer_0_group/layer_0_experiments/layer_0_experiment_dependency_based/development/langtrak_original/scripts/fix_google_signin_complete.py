#!/usr/bin/env python3
"""
Complete Google Sign-In Fix
This script handles OAuth consent screen setup and Google provider enablement
"""

import subprocess
import json
import time
import sys
from pathlib import Path

def run_command(command, timeout=30):
    """Run a command with timeout and return result."""
    try:
        result = subprocess.run(
            command, 
            shell=True, 
            capture_output=True, 
            text=True, 
            timeout=timeout
        )
        return result.returncode == 0, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return False, "", "Command timed out"
    except Exception as e:
        return False, "", str(e)

def get_access_token():
    """Get Google Cloud access token."""
    success, stdout, stderr = run_command("gcloud auth print-access-token")
    if not success:
        print(f"❌ Failed to get access token: {stderr}")
        return None
    return stdout.strip()

def check_oauth_consent_screen(project_id):
    """Check if OAuth consent screen is configured."""
    access_token = get_access_token()
    if not access_token:
        return False
    
    # Check OAuth consent screen using the correct API
    command = f'''curl -s -X GET "https://oauth2.googleapis.com/v1/projects/{project_id}/consentScreen" -H "Authorization: Bearer {access_token}"'''
    success, stdout, stderr = run_command(command)
    
    if success and "error" not in stdout:
        try:
            data = json.loads(stdout)
            return "displayName" in data
        except:
            return False
    return False

def configure_oauth_consent_screen(project_id):
    """Configure OAuth consent screen for the project."""
    access_token = get_access_token()
    if not access_token:
        return False
    
    print(f"🔧 Configuring OAuth consent screen for {project_id}...")
    
    # Configure OAuth consent screen using the correct API
    consent_data = {
        "displayName": f"Lang Trak {project_id.split('-')[-1].title()}",
        "supportEmail": "2025computer2025@gmail.com",
        "privacyPolicyUrl": "https://lang-trak.com/privacy",
        "termsOfServiceUrl": "https://lang-trak.com/terms",
        "authorizedDomains": [
            "localhost",
            "127.0.0.1",
            f"{project_id}.web.app",
            f"{project_id}.firebaseapp.com"
        ]
    }
    
    command = f'''curl -s -X PUT "https://oauth2.googleapis.com/v1/projects/{project_id}/consentScreen" -H "Authorization: Bearer {access_token}" -H "Content-Type: application/json" -d '{json.dumps(consent_data)}' '''
    success, stdout, stderr = run_command(command)
    
    if success and "error" not in stdout:
        print(f"✅ OAuth consent screen configured for {project_id}")
        return True
    else:
        print(f"❌ Failed to configure OAuth consent screen for {project_id}: {stdout}")
        return False

def enable_google_provider_firebase(project_id):
    """Enable Google Sign-In provider using Firebase Identity Toolkit API."""
    access_token = get_access_token()
    if not access_token:
        return False
    
    print(f"🔑 Enabling Google Sign-In provider for {project_id}...")
    
    # Get current config
    command = f'''curl -s -X GET "https://identitytoolkit.googleapis.com/admin/v2/projects/{project_id}/config" -H "Authorization: Bearer {access_token}" -H "X-Goog-User-Project: {project_id}"'''
    success, stdout, stderr = run_command(command)
    
    if not success:
        print(f"❌ Failed to get current config for {project_id}: {stderr}")
        return False
    
    try:
        config = json.loads(stdout)
        
        # Add Google provider to signIn configuration
        if "signIn" not in config:
            config["signIn"] = {}
        
        # Add Google provider configuration
        config["signIn"]["google"] = {
            "enabled": True
        }
        
        # Update the configuration
        update_command = f'''curl -s -X PATCH "https://identitytoolkit.googleapis.com/admin/v2/projects/{project_id}/config" -H "Authorization: Bearer {access_token}" -H "X-Goog-User-Project: {project_id}" -H "Content-Type: application/json" -d '{json.dumps(config)}' '''
        
        success, stdout, stderr = run_command(update_command)
        
        if success and "error" not in stdout:
            print(f"✅ Google Sign-In provider enabled for {project_id}")
            return True
        else:
            print(f"❌ Failed to enable Google provider for {project_id}: {stdout}")
            return False
            
    except Exception as e:
        print(f"❌ Error processing config for {project_id}: {e}")
        return False

def verify_google_provider(project_id):
    """Verify that Google Sign-In is enabled."""
    access_token = get_access_token()
    if not access_token:
        return False
    
    command = f'''curl -s -X GET "https://identitytoolkit.googleapis.com/admin/v2/projects/{project_id}/config" -H "Authorization: Bearer {access_token}" -H "X-Goog-User-Project: {project_id}" | jq -r '.signIn | "Google: " + (.google.enabled | tostring)' '''
    success, stdout, stderr = run_command(command)
    
    if success and "Google: true" in stdout:
        return True
    return False

def main():
    """Main function to fix Google Sign-In for all projects."""
    print("🚀 Complete Google Sign-In Fix")
    print("=" * 50)
    print()
    print("This script will:")
    print("1. Configure OAuth consent screen for each project")
    print("2. Enable Google Sign-In provider")
    print("3. Verify the setup")
    print()
    
    projects = {
        "dev": "lang-trak-dev",
        "staging": "lang-trak-staging", 
        "test": "lang-trak-test",
        "prod": "lang-trak-prod"
    }
    
    results = {}
    
    for env, project_id in projects.items():
        print(f"\n--- {env.upper()} Environment ({project_id}) ---")
        
        # Step 1: Check/Configure OAuth consent screen
        if not check_oauth_consent_screen(project_id):
            print(f"🔧 Setting up OAuth consent screen for {project_id}...")
            if not configure_oauth_consent_screen(project_id):
                print(f"❌ Failed to configure OAuth consent screen for {project_id}")
                results[env] = False
                continue
        else:
            print(f"✅ OAuth consent screen already configured for {project_id}")
        
        # Step 2: Enable Google provider
        if enable_google_provider_firebase(project_id):
            # Step 3: Verify it's working
            time.sleep(2)  # Give it a moment to propagate
            if verify_google_provider(project_id):
                print(f"✅ Google Sign-In successfully enabled for {project_id}")
                results[env] = True
            else:
                print(f"⚠️ Google provider enabled but verification failed for {project_id}")
                results[env] = False
        else:
            print(f"❌ Failed to enable Google provider for {project_id}")
            results[env] = False
    
    # Summary
    print("\n" + "=" * 50)
    print("🎯 GOOGLE SIGN-IN FIX SUMMARY")
    print("=" * 50)
    
    success_count = 0
    for env, project_id in projects.items():
        status = "✅ FIXED" if results.get(env, False) else "❌ FAILED"
        print(f"{status} {env.upper()} ({project_id})")
        if results.get(env, False):
            success_count += 1
    
    print(f"\n📊 Results: {success_count}/{len(projects)} environments fixed successfully")
    
    if success_count == len(projects):
        print("🎉 All Google Sign-In issues have been fixed!")
    else:
        print("⚠️ Some environments still need attention.")
        print("\n🔧 Manual fallback:")
        print("If API methods fail, use the browser setup guide:")
        print("python3 scripts/browser_google_signin_setup.py")
    
    print("\n🔧 Next steps:")
    print("1. Run verification: python3 scripts/quick_verify.py")
    print("2. Test authentication flow: python3 scripts/test_auth_flow.py")

if __name__ == "__main__":
    main()
