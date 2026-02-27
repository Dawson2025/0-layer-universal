#!/usr/bin/env python3

"""
quick_verify.py

Quick verification of Google Sign-In setup for all Firebase projects.
"""

import subprocess
import json

def get_access_token():
    """Get access token from authenticated gcloud session."""
    try:
        result = subprocess.run(['gcloud', 'auth', 'print-access-token'], 
                              capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error getting access token: {e}")
        return None

def check_project_config(project_id, access_token):
    """Check Firebase configuration for a project."""
    try:
        cmd = [
            'curl', '-s', '-X', 'GET',
            f'https://identitytoolkit.googleapis.com/admin/v2/projects/{project_id}/config',
            '-H', f'Authorization: Bearer {access_token}',
            '-H', f'X-Goog-User-Project: {project_id}',
            '-H', 'Content-Type: application/json'
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        config = json.loads(result.stdout)
        
        sign_in = config.get('signIn', {})
        email_enabled = sign_in.get('email', {}).get('enabled', False)
        google_enabled = sign_in.get('google', {}).get('enabled', False)
        
        return {
            'email_enabled': email_enabled,
            'google_enabled': google_enabled,
            'enabled_providers': sign_in.get('enabledProviders', [])
        }
    except Exception as e:
        print(f"Error checking {project_id}: {e}")
        return None

def main():
    """Main verification function."""
    print("🔍 Verifying Google Sign-In setup for all Firebase projects...\n")
    
    # Get access token
    access_token = get_access_token()
    if not access_token:
        print("❌ Failed to get access token")
        return
    
    projects = {
        "dev": "lang-trak-dev",
        "staging": "lang-trak-staging", 
        "test": "lang-trak-test",
        "prod": "lang-trak-prod"
    }
    
    all_good = True
    
    for env, project_id in projects.items():
        print(f"📋 Checking {env} ({project_id})...")
        
        config = check_project_config(project_id, access_token)
        if config:
            email_status = "✅" if config['email_enabled'] else "❌"
            google_status = "✅" if config['google_enabled'] else "❌"
            
            print(f"   Email/Password: {email_status}")
            print(f"   Google Sign-In: {google_status}")
            print(f"   Enabled Providers: {config['enabled_providers']}")
            
            if not config['email_enabled'] or not config['google_enabled']:
                all_good = False
        else:
            print(f"   ❌ Failed to check configuration")
            all_good = False
        
        print()
    
    if all_good:
        print("🎉 All projects are properly configured!")
    else:
        print("⚠️  Some projects may need attention.")

if __name__ == "__main__":
    main()
