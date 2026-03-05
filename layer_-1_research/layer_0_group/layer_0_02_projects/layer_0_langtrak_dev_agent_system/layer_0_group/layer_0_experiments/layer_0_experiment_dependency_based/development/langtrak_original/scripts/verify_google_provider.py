#!/usr/bin/env python3
# resource_id: "044e3504-b1fd-4de4-9dbc-6d55c878deb2"
# resource_type: "document"
# resource_name: "verify_google_provider"

"""
verify_google_provider.py

Verify that Google Sign-In provider is enabled for all Firebase environments.
This script checks the authentication configuration for each environment.
"""

import sys
import json
import subprocess
import shlex
from pathlib import Path
from typing import Dict, List, Any, Optional

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

def get_access_token() -> str:
    """Get Google Cloud access token."""
    try:
        result = subprocess.run(
            ["gcloud", "auth", "print-access-token"],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to get access token: {e}")
        sys.exit(1)

def fetch_auth_config(project_id: str, access_token: str) -> Optional[Dict[str, Any]]:
    """Fetch Firebase Auth configuration for a project."""
    url = f"https://identitytoolkit.googleapis.com/admin/v2/projects/{project_id}/config"
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "X-Goog-User-Project": project_id
    }
    
    try:
        result = subprocess.run([
            "curl", "-s", "-X", "GET", url,
            "-H", f"Authorization: Bearer {access_token}",
            "-H", "Content-Type: application/json",
            "-H", f"X-Goog-User-Project: {project_id}"
        ], capture_output=True, text=True, check=True)
        
        return json.loads(result.stdout)
    except (subprocess.CalledProcessError, json.JSONDecodeError) as e:
        print(f"⚠️  Failed to fetch config for {project_id}: {e}")
        return None

def check_google_provider(config: Dict[str, Any]) -> Dict[str, Any]:
    """Check if Google Sign-In provider is enabled."""
    if not config:
        return {
            "enabled": False,
            "error": "No configuration found"
        }
    
    # Check for signInProviders in the config
    sign_in_providers = config.get("signInProviders", [])
    
    google_provider = None
    for provider in sign_in_providers:
        if provider.get("providerId") == "google.com":
            google_provider = provider
            break
    
    if not google_provider:
        return {
            "enabled": False,
            "error": "Google provider not found in signInProviders"
        }
    
    return {
        "enabled": google_provider.get("enabled", False),
        "display_name": google_provider.get("displayName", "Google"),
        "client_id": google_provider.get("clientId", "Not configured"),
        "error": None
    }

def verify_all_environments() -> Dict[str, Any]:
    """Verify Google Sign-In provider for all environments."""
    print("🔍 Verifying Google Sign-In Provider Status")
    print("=" * 60)
    
    # Get access token
    print("🔑 Getting access token...")
    access_token = get_access_token()
    print("✅ Access token obtained")
    
    environments = {
        "Development": "lang-trak-dev",
        "Staging": "lang-trak-staging", 
        "Testing": "lang-trak-test",
        "Production": "lang-trak-prod"
    }
    
    results = {}
    
    for env_name, project_id in environments.items():
        print(f"\n--- {env_name} Environment ({project_id}) ---")
        
        # Fetch auth config
        config = fetch_auth_config(project_id, access_token)
        
        # Check Google provider
        provider_status = check_google_provider(config)
        
        results[env_name] = {
            "project_id": project_id,
            "provider_status": provider_status,
            "config_available": config is not None
        }
        
        if provider_status["enabled"]:
            print(f"✅ Google Sign-In is ENABLED")
            print(f"   Display Name: {provider_status['display_name']}")
            print(f"   Client ID: {provider_status['client_id']}")
        else:
            print(f"❌ Google Sign-In is DISABLED")
            if provider_status["error"]:
                print(f"   Error: {provider_status['error']}")
    
    return results

def print_summary(results: Dict[str, Any]) -> None:
    """Print verification summary."""
    print("\n" + "=" * 60)
    print("🎯 VERIFICATION SUMMARY")
    print("=" * 60)
    
    enabled_count = 0
    total_count = len(results)
    
    for env_name, result in results.items():
        project_id = result["project_id"]
        provider_status = result["provider_status"]
        
        if provider_status["enabled"]:
            print(f"✅ {env_name} ({project_id}) - Google Sign-In ENABLED")
            enabled_count += 1
        else:
            print(f"❌ {env_name} ({project_id}) - Google Sign-In DISABLED")
            if provider_status["error"]:
                print(f"   Error: {provider_status['error']}")
    
    print(f"\n📊 Results: {enabled_count}/{total_count} environments have Google Sign-In enabled")
    
    if enabled_count == total_count:
        print("🎉 All environments are ready for Google Sign-In!")
    else:
        print("⚠️  Some environments need Google Sign-In to be enabled")
        print("\n🔧 To enable Google Sign-In:")
        print("1. Go to Firebase Console for each project")
        print("2. Navigate to Authentication > Sign-in method")
        print("3. Enable Google provider")
        print("4. Configure OAuth consent screen if needed")

def main():
    """Main function."""
    print("🔥 Google Sign-In Provider Verification")
    print("=" * 60)
    print(f"📅 Started: {subprocess.run(['date', '-Iseconds'], capture_output=True, text=True).stdout.strip()}")
    
    try:
        results = verify_all_environments()
        print_summary(results)
        
        # Check if all are enabled
        all_enabled = all(
            result["provider_status"]["enabled"] 
            for result in results.values()
        )
        
        sys.exit(0 if all_enabled else 1)
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Verification interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Verification failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
