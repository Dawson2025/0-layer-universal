#!/usr/bin/env python3

"""
configure_google_auth_automated.py

Automated Google Sign-In configuration for all environments.
Uses your existing gcloud authentication.
"""

import json
import subprocess
import sys
from datetime import datetime

def get_access_token():
    """Get access token from gcloud."""
    try:
        result = subprocess.run(['gcloud', 'auth', 'print-access-token'], 
                              capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None

def configure_project_domains(project_id, domains, access_token):
    """Configure authorized domains for a project."""
    print(f"🔧 Configuring {project_id}...")
    
    try:
        # Get current config
        get_result = subprocess.run([
            'curl', '-s', '-H', f'Authorization: Bearer {access_token}',
            '-H', 'Content-Type: application/json',
            f'https://identitytoolkit.googleapis.com/admin/v2/projects/{project_id}/config'
        ], capture_output=True, text=True)
        
        if get_result.returncode != 0:
            print(f"❌ Failed to get current config for {project_id}")
            return False
        
        current_config = json.loads(get_result.stdout) if get_result.stdout else {}
        current_domains = set(current_config.get('authorizedDomains', []))
        new_domains = set(domains)
        all_domains = list(current_domains.union(new_domains))
        
        print(f"  Current domains: {sorted(current_domains)}")
        print(f"  Adding domains: {sorted(new_domains)}")
        
        # Update configuration
        updated_config = {
            **current_config,
            'authorizedDomains': all_domains
        }
        
        # Apply update
        update_result = subprocess.run([
            'curl', '-s', '-X', 'PATCH',
            '-H', f'Authorization: Bearer {access_token}',
            '-H', 'Content-Type: application/json',
            '-H', f'X-Goog-User-Project: {project_id}',
            '-d', json.dumps(updated_config),
            f'https://identitytoolkit.googleapis.com/admin/v2/projects/{project_id}/config'
        ], capture_output=True, text=True)
        
        if update_result.returncode == 0:
            print(f"✅ Successfully configured {project_id}")
            return True
        else:
            print(f"❌ Failed to update {project_id}")
            return False
            
    except Exception as e:
        print(f"❌ Error configuring {project_id}: {e}")
        return False

def main():
    """Main configuration function."""
    print("🔥 Automated Google Sign-In Configuration")
    print("=" * 60)
    print(f"📅 Started: {datetime.now().isoformat()}")
    print()
    
    # Get access token
    print("🔑 Getting access token...")
    access_token = get_access_token()
    if not access_token:
        print("❌ Failed to get access token")
        print("💡 Please run 'gcloud auth login' first")
        return False
    
    print("✅ Access token obtained")
    
    # Environment configurations
    environments = {
        "lang-trak-dev": {
            "domains": ["localhost", "127.0.0.1", "lang-trak-dev.web.app", "lang-trak-dev.firebaseapp.com"],
            "description": "Development"
        },
        "lang-trak-staging": {
            "domains": ["lang-trak-staging.web.app", "lang-trak-staging.firebaseapp.com"],
            "description": "Staging"
        },
        "lang-trak-test": {
            "domains": ["lang-trak-test.web.app", "lang-trak-test.firebaseapp.com"],
            "description": "Testing"
        },
        "lang-trak-prod": {
            "domains": ["lang-trak-prod.web.app", "lang-trak-prod.firebaseapp.com"],
            "description": "Production"
        }
    }
    
    results = {}
    
    # Configure each environment
    for project_id, config in environments.items():
        print(f"\n--- {config['description']} Environment ({project_id}) ---")
        success = configure_project_domains(project_id, config["domains"], access_token)
        results[project_id] = success
    
    # Summary
    print(f"\n{'='*60}")
    print("🎯 CONFIGURATION SUMMARY")
    print('='*60)
    
    successful = sum(1 for success in results.values() if success)
    total = len(results)
    
    for project_id, success in results.items():
        status = "✅" if success else "❌"
        env_name = environments[project_id]["description"]
        print(f"{status} {env_name} ({project_id})")
    
    print(f"\n📊 Results: {successful}/{total} environments configured successfully")
    
    if successful == total:
        print("🎉 All environments are now ready for Google Sign-In!")
        print("\n🔒 Next steps:")
        print("1. Verify Google Sign-In provider is enabled in Firebase Console")
        print("2. Test authentication flow in your application")
        print("3. Monitor authentication metrics")
        return True
    else:
        print("⚠️ Some environments failed to configure")
        print("🔧 Check the error messages above and retry if needed")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
