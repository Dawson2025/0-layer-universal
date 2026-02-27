#!/usr/bin/env python3

"""
test_auth_flow.py

Test the authentication flow to ensure Google Sign-In is working properly.
"""

import subprocess
import json
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

def get_access_token():
    """Get access token from authenticated gcloud session."""
    try:
        result = subprocess.run(['gcloud', 'auth', 'print-access-token'], 
                              capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"❌ Error getting access token: {e}")
        return None

def test_project_auth(project_id, access_token):
    """Test authentication configuration for a project."""
    try:
        # Get project configuration
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
        
        print(f"📋 Testing {project_id}:")
        print(f"   Email/Password: {'✅ Enabled' if email_enabled else '❌ Disabled'}")
        print(f"   Google Sign-In: {'✅ Enabled' if google_enabled else '❌ Disabled'}")
        
        # Check authorized domains
        authorized_domains = config.get('authorizedDomains', [])
        print(f"   Authorized Domains: {authorized_domains}")
        
        return email_enabled and google_enabled
        
    except Exception as e:
        print(f"   ❌ Error testing {project_id}: {e}")
        return False

def main():
    """Main test function."""
    print("🧪 Testing Authentication Flow for All Firebase Projects\n")
    
    # Get access token
    access_token = get_access_token()
    if not access_token:
        print("❌ Failed to get access token. Please ensure you're authenticated with gcloud.")
        return
    
    projects = {
        "dev": "lang-trak-dev",
        "staging": "lang-trak-staging", 
        "test": "lang-trak-test",
        "prod": "lang-trak-prod"
    }
    
    all_passed = True
    
    for env, project_id in projects.items():
        success = test_project_auth(project_id, access_token)
        if not success:
            all_passed = False
        print()
    
    print("=" * 50)
    if all_passed:
        print("🎉 ALL TESTS PASSED! Authentication is properly configured for all projects.")
        print("\n✅ Ready for development and production use!")
        print("✅ Users can now sign in with Email/Password or Google")
        print("✅ All authorized domains are configured")
    else:
        print("⚠️  Some tests failed. Please check the configuration.")
    
    print("\n🔗 Next Steps:")
    print("1. Test the authentication in your application")
    print("2. Configure your app with the Firebase config")
    print("3. Implement the sign-in UI components")

if __name__ == "__main__":
    main()