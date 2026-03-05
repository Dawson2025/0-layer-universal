#!/usr/bin/env python3
# resource_id: "f1f7a3c5-2edf-49ac-a52e-47d5a68963ad"
# resource_type: "document"
# resource_name: "enable_google_providers_api"

"""
enable_google_providers_api.py

Enable Google Sign-In providers for all Firebase projects using the API.
"""

import sys
import subprocess
import json
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

class GoogleProviderEnabler:
    """Enable Google Sign-In providers using Firebase Admin API."""
    
    def __init__(self):
        self.projects = {
            "dev": "lang-trak-dev",
            "staging": "lang-trak-staging", 
            "test": "lang-trak-test",
            "prod": "lang-trak-prod"
        }
    
    def get_access_token(self) -> str:
        """Get access token from authenticated gcloud session."""
        try:
            result = subprocess.run([
                'gcloud', 'auth', 'print-access-token'
            ], capture_output=True, text=True, check=True)
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            print(f"❌ Error getting access token: {e.stderr}")
            sys.exit(1)
    
    def enable_google_provider(self, project_id: str) -> dict:
        """Enable Google Sign-In provider for a project."""
        print(f"🔑 Enabling Google Sign-In for {project_id}...")
        
        access_token = self.get_access_token()
        
        # Get current config
        get_url = f"https://identitytoolkit.googleapis.com/admin/v2/projects/{project_id}/config"
        get_command = [
            'curl', '-s', '-X', 'GET', get_url,
            '-H', f'Authorization: Bearer {access_token}',
            '-H', 'X-Goog-User-Project: ' + project_id,
            '-H', 'Content-Type: application/json'
        ]
        
        try:
            result = subprocess.run(get_command, capture_output=True, text=True, check=True)
            config = json.loads(result.stdout)
            
            # Check if Google provider is already enabled
            if 'signIn' in config and 'google' in config['signIn']:
                if config['signIn']['google'].get('enabled', False):
                    print(f"  ✅ Google Sign-In already enabled for {project_id}")
                    return {"success": True, "message": "Already enabled"}
            
            # Enable Google provider
            if 'signIn' not in config:
                config['signIn'] = {}
            
            config['signIn']['google'] = {
                "enabled": True
            }
            
            # Update config
            update_command = [
                'curl', '-s', '-X', 'PATCH', get_url,
                '-H', f'Authorization: Bearer {access_token}',
                '-H', 'X-Goog-User-Project: ' + project_id,
                '-H', 'Content-Type: application/json',
                '-d', json.dumps(config)
            ]
            
            result = subprocess.run(update_command, capture_output=True, text=True, check=True)
            print(f"  ✅ Google Sign-In enabled for {project_id}")
            return {"success": True, "message": "Successfully enabled"}
            
        except subprocess.CalledProcessError as e:
            print(f"  ❌ Failed to enable Google provider for {project_id}: {e.stderr}")
            return {"success": False, "error": str(e)}
        except json.JSONDecodeError as e:
            print(f"  ❌ Failed to parse config for {project_id}: {e}")
            return {"success": False, "error": str(e)}
    
    def enable_all_providers(self) -> dict:
        """Enable Google Sign-In for all projects."""
        print("🚀 Enabling Google Sign-In Providers")
        print("Using authenticated gcloud session")
        print("=" * 60)
        
        # Show current account
        try:
            result = subprocess.run([
                'gcloud', 'config', 'get-value', 'account'
            ], capture_output=True, text=True, check=True)
            print(f"🔑 Authenticated as: {result.stdout.strip()}")
        except:
            print("🔑 Using authenticated gcloud session")
        
        print("")
        
        results = {}
        
        for env_name, project_id in self.projects.items():
            print(f"--- {env_name.upper()} Environment ({project_id}) ---")
            result = self.enable_google_provider(project_id)
            results[env_name] = result
            print("")
        
        return results
    
    def print_summary(self, results: dict) -> None:
        """Print setup summary."""
        print("=" * 60)
        print("🎯 GOOGLE SIGN-IN PROVIDER ENABLEMENT SUMMARY")
        print("=" * 60)
        
        successful_envs = 0
        total_envs = len(results)
        
        for env_name, result in results.items():
            project_id = self.projects[env_name]
            success = result["success"]
            
            if success:
                print(f"✅ {env_name.upper()} ({project_id}) - ENABLED")
                print(f"   Status: {result.get('message', 'Success')}")
                successful_envs += 1
            else:
                print(f"❌ {env_name.upper()} ({project_id}) - FAILED")
                print(f"   Error: {result.get('error', 'Unknown error')}")
        
        print(f"\n📊 Results: {successful_envs}/{total_envs} environments enabled successfully")
        
        if successful_envs == total_envs:
            print("🎉 All environments have Google Sign-In enabled!")
            print("\n🔧 Next steps:")
            print("1. Run verification: python3 scripts/verify_google_provider.py")
            print("2. Test authentication flow: python3 scripts/test_auth_flow.py")
        else:
            print("⚠️  Some environments need manual intervention")
            print("\n🔧 Manual steps if needed:")
            print("1. Go to Firebase Console for each project")
            print("2. Navigate to Authentication > Sign-in method")
            print("3. Enable Google provider manually")

def main():
    """Main function."""
    print("🤖 Google Sign-In Provider Enabler")
    print("Using authenticated gcloud session")
    print("=" * 60)
    
    try:
        # Create enabler instance
        enabler = GoogleProviderEnabler()
        
        # Enable all providers
        results = enabler.enable_all_providers()
        
        # Print summary
        enabler.print_summary(results)
        
        # Check overall success
        all_successful = all(result["success"] for result in results.values())
        
        if all_successful:
            print("\n🎉 Google Sign-In providers enabled successfully!")
        else:
            print("\n⚠️  Some projects need manual intervention")
        
        sys.exit(0 if all_successful else 1)
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Setup interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Setup failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
