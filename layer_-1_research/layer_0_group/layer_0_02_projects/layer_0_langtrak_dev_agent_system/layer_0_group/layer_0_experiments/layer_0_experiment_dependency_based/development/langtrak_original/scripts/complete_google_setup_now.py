#!/usr/bin/env python3
# resource_id: "232ca733-7209-4f3f-9202-6a80175f5aa1"
# resource_type: "document"
# resource_name: "complete_google_setup_now"

"""
complete_google_setup_now.py

Complete Google Sign-In setup using authenticated gcloud session.
This script uses the existing authentication to complete the setup.
"""

import sys
import asyncio
import subprocess
import json
import time
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

class CompleteGoogleSetup:
    """Complete Google Sign-In setup using authenticated session."""
    
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
    
    def enable_google_provider_api(self, project_id: str) -> bool:
        """Enable Google Sign-In provider using Firebase Admin API."""
        print(f"  🔑 Enabling Google Sign-In provider for {project_id}...")
        
        access_token = self.get_access_token()
        
        # Enable Google Sign-In provider using Firebase Admin API
        url = f"https://identitytoolkit.googleapis.com/admin/v2/projects/{project_id}/config"
        
        # Get current config
        get_command = [
            'curl', '-s', '-X', 'GET', url,
            '-H', f'Authorization: Bearer {access_token}',
            '-H', 'X-Goog-User-Project: ' + project_id,
            '-H', 'Content-Type: application/json'
        ]
        
        try:
            result = subprocess.run(get_command, capture_output=True, text=True, check=True)
            config = json.loads(result.stdout)
            
            # Enable Google provider
            if 'signIn' not in config:
                config['signIn'] = {}
            
            if 'enabledProviders' not in config['signIn']:
                config['signIn']['enabledProviders'] = []
            
            if 'GOOGLE' not in config['signIn']['enabledProviders']:
                config['signIn']['enabledProviders'].append('GOOGLE')
            
            # Update config
            update_command = [
                'curl', '-s', '-X', 'PATCH', url,
                '-H', f'Authorization: Bearer {access_token}',
                '-H', 'X-Goog-User-Project: ' + project_id,
                '-H', 'Content-Type: application/json',
                '-d', json.dumps(config)
            ]
            
            result = subprocess.run(update_command, capture_output=True, text=True, check=True)
            print(f"    ✅ Google Sign-In provider enabled for {project_id}")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"    ❌ Failed to enable Google provider for {project_id}: {e.stderr}")
            return False
        except json.JSONDecodeError as e:
            print(f"    ❌ Failed to parse config for {project_id}: {e}")
            return False
    
    def setup_project(self, project_id: str, env_name: str) -> dict:
        """Setup Google Sign-In for a project."""
        print(f"🔥 Setting up {env_name} environment ({project_id})...")
        
        # Enable Google provider
        success = self.enable_google_provider_api(project_id)
        
        if success:
            print(f"  ✅ {env_name.upper()} Google Sign-In enabled")
            return {
                "success": True,
                "project_id": project_id,
                "environment": env_name,
                "message": "Google Sign-In provider enabled successfully"
            }
        else:
            print(f"  ❌ {env_name.upper()} Google Sign-In failed")
            return {
                "success": False,
                "project_id": project_id,
                "environment": env_name,
                "message": "Failed to enable Google Sign-In provider"
            }
    
    def setup_all_projects(self) -> dict:
        """Setup Google Sign-In for all projects."""
        print("🚀 Complete Google Sign-In Setup")
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
            result = self.setup_project(project_id, env_name)
            results[env_name] = result
            print("")
            
            # Add delay between projects
            time.sleep(1)
        
        return results
    
    def print_summary(self, results: dict) -> None:
        """Print setup summary."""
        print("=" * 60)
        print("🎯 GOOGLE SIGN-IN SETUP SUMMARY")
        print("=" * 60)
        
        successful_envs = 0
        total_envs = len(results)
        
        for env_name, result in results.items():
            project_id = result["project_id"]
            success = result["success"]
            
            if success:
                print(f"✅ {env_name.upper()} ({project_id}) - ENABLED")
                successful_envs += 1
            else:
                print(f"❌ {env_name.upper()} ({project_id}) - FAILED")
                print(f"   Error: {result.get('message', 'Unknown error')}")
        
        print(f"\n📊 Results: {successful_envs}/{total_envs} environments enabled successfully")
        
        if successful_envs == total_envs:
            print("🎉 All environments have Google Sign-In enabled!")
            print("\n🔧 Next steps:")
            print("1. Configure OAuth consent screen in Google Cloud Console")
            print("2. Run verification: python3 scripts/verify_google_provider.py")
            print("3. Test authentication flow: python3 scripts/test_auth_flow.py")
        else:
            print("⚠️  Some environments need manual intervention")
            print("\n🔧 Manual steps if needed:")
            print("1. Go to Firebase Console for each project")
            print("2. Navigate to Authentication > Sign-in method")
            print("3. Enable Google provider manually")

async def main():
    """Main function."""
    print("🤖 Complete Google Sign-In Setup")
    print("Using authenticated gcloud session")
    print("=" * 60)
    
    try:
        # Create setup instance
        setup = CompleteGoogleSetup()
        
        # Setup all projects
        results = setup.setup_all_projects()
        
        # Print summary
        setup.print_summary(results)
        
        # Check overall success
        all_successful = all(result["success"] for result in results.values())
        
        if all_successful:
            print("\n🎉 Google Sign-In setup completed successfully!")
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
    asyncio.run(main())
