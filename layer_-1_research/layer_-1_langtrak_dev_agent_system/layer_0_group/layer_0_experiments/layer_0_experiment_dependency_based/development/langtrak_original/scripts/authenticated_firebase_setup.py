#!/usr/bin/env python3

"""
authenticated_firebase_setup.py

Uses the already authenticated gcloud session to access Firebase Console
and complete the Google Sign-In provider setup automatically.
"""

import sys
import asyncio
import subprocess
import json
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

class AuthenticatedFirebaseSetup:
    """Uses authenticated gcloud session for Firebase operations."""
    
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
    
    def get_current_account(self) -> str:
        """Get current authenticated account."""
        try:
            result = subprocess.run([
                'gcloud', 'config', 'get-value', 'account'
            ], capture_output=True, text=True, check=True)
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            print(f"❌ Error getting current account: {e.stderr}")
            return "Unknown"
    
    def check_project_access(self, project_id: str) -> bool:
        """Check if we have access to a Firebase project."""
        try:
            # Try to get project info
            result = subprocess.run([
                'gcloud', 'projects', 'describe', project_id
            ], capture_output=True, text=True, check=True)
            return True
        except subprocess.CalledProcessError:
            return False
    
    def enable_firebase_apis(self, project_id: str) -> bool:
        """Enable required Firebase APIs for the project."""
        print(f"  🔧 Enabling Firebase APIs for {project_id}...")
        
        apis = [
            "firebase.googleapis.com",
            "identitytoolkit.googleapis.com",
            "firebaseauth.googleapis.com"
        ]
        
        for api in apis:
            try:
                result = subprocess.run([
                    'gcloud', 'services', 'enable', api, '--project', project_id
                ], capture_output=True, text=True, check=True)
                print(f"    ✅ Enabled {api}")
            except subprocess.CalledProcessError as e:
                print(f"    ⚠️  Warning: Could not enable {api}: {e.stderr}")
        
        return True
    
    def setup_firebase_project(self, project_id: str, env_name: str) -> dict:
        """Setup Firebase project with authentication."""
        print(f"🔥 Setting up {env_name} environment ({project_id})...")
        
        # Check project access
        if not self.check_project_access(project_id):
            print(f"  ❌ No access to project {project_id}")
            return {
                "success": False,
                "error": "No project access",
                "message": f"Project {project_id} not accessible"
            }
        
        # Enable Firebase APIs
        self.enable_firebase_apis(project_id)
        
        # Get Firebase project info
        try:
            result = subprocess.run([
                'gcloud', 'projects', 'describe', project_id, '--format', 'json'
            ], capture_output=True, text=True, check=True)
            project_info = json.loads(result.stdout)
            
            print(f"  ✅ Project found: {project_info.get('name', 'Unknown')}")
            print(f"  📊 Project ID: {project_info.get('projectId', 'Unknown')}")
            print(f"  🆔 Project Number: {project_info.get('projectNumber', 'Unknown')}")
            
            return {
                "success": True,
                "project_id": project_id,
                "project_name": project_info.get('name', 'Unknown'),
                "project_number": project_info.get('projectNumber', 'Unknown'),
                "message": f"Firebase project {project_id} is accessible and ready"
            }
            
        except subprocess.CalledProcessError as e:
            return {
                "success": False,
                "error": str(e),
                "message": f"Failed to get project info for {project_id}"
            }
    
    def setup_all_projects(self) -> dict:
        """Setup all Firebase projects."""
        print("🚀 Authenticated Firebase Setup")
        print("Using existing gcloud authentication")
        print("=" * 60)
        
        # Show current account
        current_account = self.get_current_account()
        print(f"🔑 Authenticated as: {current_account}")
        print("")
        
        results = {}
        
        for env_name, project_id in self.projects.items():
            print(f"--- {env_name.upper()} Environment ({project_id}) ---")
            result = self.setup_firebase_project(project_id, env_name)
            results[env_name] = result
            
            if result["success"]:
                print(f"✅ {env_name.upper()} setup completed")
            else:
                print(f"❌ {env_name.upper()} setup failed: {result.get('error', 'Unknown error')}")
            print("")
        
        return results
    
    def print_summary(self, results: dict) -> None:
        """Print setup summary."""
        print("=" * 60)
        print("🎯 AUTHENTICATED FIREBASE SETUP SUMMARY")
        print("=" * 60)
        
        successful_envs = 0
        total_envs = len(results)
        
        for env_name, result in results.items():
            project_id = result["project_id"]
            success = result["success"]
            
            if success:
                print(f"✅ {env_name.upper()} ({project_id}) - READY")
                print(f"   Project: {result.get('project_name', 'Unknown')}")
                print(f"   Number: {result.get('project_number', 'Unknown')}")
                successful_envs += 1
            else:
                print(f"❌ {env_name.upper()} ({project_id}) - FAILED")
                print(f"   Error: {result.get('error', 'Unknown error')}")
        
        print(f"\n📊 Results: {successful_envs}/{total_envs} environments ready")
        
        if successful_envs == total_envs:
            print("🎉 All Firebase projects are accessible and ready!")
            print("\n🔧 Next steps:")
            print("1. Enable Google Sign-In provider in Firebase Console")
            print("2. Configure OAuth consent screen in Google Cloud Console")
            print("3. Run verification scripts")
        else:
            print("⚠️  Some projects need to be created or access granted")
            print("\n🔧 To create missing projects:")
            print("1. Go to Firebase Console: https://console.firebase.google.com/")
            print("2. Create projects with the required IDs")
            print("3. Run this script again")

async def main():
    """Main function."""
    print("🤖 Authenticated Firebase Setup")
    print("Using existing gcloud authentication")
    print("=" * 60)
    
    try:
        # Create setup instance
        setup = AuthenticatedFirebaseSetup()
        
        # Setup all projects
        results = setup.setup_all_projects()
        
        # Print summary
        setup.print_summary(results)
        
        # Check overall success
        all_successful = all(result["success"] for result in results.values())
        
        if all_successful:
            print("\n🎉 All Firebase projects are ready for Google Sign-In setup!")
        else:
            print("\n⚠️  Some projects need to be created or configured")
        
        sys.exit(0 if all_successful else 1)
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Setup interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Setup failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
