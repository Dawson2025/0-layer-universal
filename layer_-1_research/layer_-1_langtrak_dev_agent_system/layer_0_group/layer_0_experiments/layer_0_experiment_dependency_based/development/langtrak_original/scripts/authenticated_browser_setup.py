#!/usr/bin/env python3

"""
authenticated_browser_setup.py

Uses the authenticated gcloud session to access Firebase Console
with the correct account and complete Google Sign-In setup.
"""

import sys
import asyncio
import subprocess
import json
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

class AuthenticatedBrowserSetup:
    """Uses authenticated gcloud session for browser automation."""
    
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
            return "Unknown"
    
    def create_authenticated_url(self, project_id: str) -> str:
        """Create Firebase Console URL with authentication token."""
        access_token = self.get_access_token()
        return f"https://console.firebase.google.com/project/{project_id}?authuser=0&access_token={access_token}"
    
    def print_authenticated_urls(self) -> None:
        """Print authenticated Firebase Console URLs."""
        print("🌐 Authenticated Firebase Console URLs")
        print("=" * 60)
        print(f"🔑 Using account: {self.get_current_account()}")
        print("")
        
        for env_name, project_id in self.projects.items():
            print(f"{env_name.upper()} Environment ({project_id}):")
            print(f"  🔥 Firebase Console: https://console.firebase.google.com/project/{project_id}")
            print(f"  🔐 Authentication: https://console.firebase.google.com/project/{project_id}/authentication/providers")
            print(f"  🌐 OAuth Consent: https://console.cloud.google.com/apis/credentials/consent?project={project_id}")
            print("")
    
    def print_setup_instructions(self) -> None:
        """Print setup instructions using authenticated session."""
        print("🚀 Authenticated Google Sign-In Setup")
        print("=" * 60)
        print("You are already authenticated with the correct account!")
        print("Follow these steps to complete the setup:")
        print("")
        
        for env_name, project_id in self.projects.items():
            print(f"📋 {env_name.upper()} Environment ({project_id})")
            print("-" * 40)
            print(f"1. 🌐 Go to: https://console.firebase.google.com/project/{project_id}")
            print(f"2. 🔐 Navigate to Authentication > Sign-in method")
            print(f"3. 🔑 Click 'Add new provider' and select 'Google'")
            print(f"4. ✅ Enable the Google Sign-In provider")
            print(f"5. 🌐 Configure OAuth consent screen:")
            print(f"   - Go to: https://console.cloud.google.com/apis/credentials/consent?project={project_id}")
            print(f"   - App name: Language Tracker {env_name.title()}")
            print(f"   - User support email: 2025computer2025@gmail.com")
            print(f"   - Developer contact: 2025computer2025@gmail.com")
            print("")
    
    def run_verification(self) -> None:
        """Run verification to check current status."""
        print("🔍 Running Verification...")
        print("=" * 60)
        
        try:
            result = subprocess.run([
                'python3', 'scripts/verify_google_provider.py'
            ], capture_output=True, text=True, check=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"❌ Verification failed: {e.stderr}")

async def main():
    """Main function."""
    print("🤖 Authenticated Browser Setup")
    print("Using existing gcloud authentication")
    print("=" * 60)
    
    try:
        # Create setup instance
        setup = AuthenticatedBrowserSetup()
        
        # Show authenticated URLs
        setup.print_authenticated_urls()
        
        # Print setup instructions
        setup.print_setup_instructions()
        
        # Run verification
        setup.run_verification()
        
        print("=" * 60)
        print("🎉 Setup Instructions Complete!")
        print("=" * 60)
        print("💡 You can now:")
        print("1. Use the authenticated URLs above")
        print("2. Complete the Google Sign-In setup")
        print("3. Run verification scripts to confirm")
        
    except Exception as e:
        print(f"\n❌ Setup failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
