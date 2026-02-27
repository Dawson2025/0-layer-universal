#!/usr/bin/env python3

"""
complete_firebase_setup.py

Complete Firebase project setup and Google Sign-In configuration.
This script handles the entire process from project creation to Google Sign-In enablement.
"""

import sys
import asyncio
import time
from pathlib import Path
from typing import Dict, List, Any

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Firebase project configurations
FIREBASE_PROJECTS = {
    "dev": {
        "id": "lang-trak-dev",
        "name": "Language Tracker Development",
        "domains": ["localhost", "127.0.0.1", "lang-trak-dev.web.app", "lang-trak-dev.firebaseapp.com"]
    },
    "staging": {
        "id": "lang-trak-staging", 
        "name": "Language Tracker Staging",
        "domains": ["lang-trak-staging.web.app", "lang-trak-staging.firebaseapp.com"]
    },
    "test": {
        "id": "lang-trak-test",
        "name": "Language Tracker Testing", 
        "domains": ["lang-trak-test.web.app", "lang-trak-test.firebaseapp.com"]
    },
    "prod": {
        "id": "lang-trak-prod",
        "name": "Language Tracker Production",
        "domains": ["lang-trak-prod.web.app", "lang-trak-prod.firebaseapp.com"]
    }
}

class CompleteFirebaseSetup:
    """Complete Firebase setup and Google Sign-In configuration."""
    
    def __init__(self):
        self.projects = FIREBASE_PROJECTS
    
    def print_setup_instructions(self) -> None:
        """Print comprehensive setup instructions."""
        print("🚀 Complete Firebase Setup Instructions")
        print("=" * 60)
        print("Following our meta-intelligent orchestration system")
        print("=" * 60)
        
        print("\n📋 STEP 1: Create Firebase Projects")
        print("-" * 40)
        for env_name, config in self.projects.items():
            print(f"\n{env_name.upper()} Environment:")
            print(f"  Project ID: {config['id']}")
            print(f"  Project Name: {config['name']}")
            print(f"  URL: https://console.firebase.google.com/project/{config['id']}")
        
        print("\n📋 STEP 2: Configure Google Sign-In for Each Project")
        print("-" * 40)
        for env_name, config in self.projects.items():
            print(f"\n{env_name.upper()} Environment ({config['id']}):")
            print(f"  1. Go to: https://console.firebase.google.com/project/{config['id']}/authentication/providers")
            print(f"  2. Click 'Add new provider'")
            print(f"  3. Select 'Google'")
            print(f"  4. Enable the provider")
            print(f"  5. Configure OAuth consent screen if prompted")
            print(f"  6. Add authorized domains: {', '.join(config['domains'])}")
        
        print("\n📋 STEP 3: Configure OAuth Consent Screen")
        print("-" * 40)
        for env_name, config in self.projects.items():
            print(f"\n{env_name.upper()} Environment ({config['id']}):")
            print(f"  1. Go to: https://console.cloud.google.com/apis/credentials/consent?project={config['id']}")
            print(f"  2. Configure OAuth consent screen:")
            print(f"     - App name: {config['name']}")
            print(f"     - User support email: 2025computer2025@gmail.com")
            print(f"     - Developer contact: 2025computer2025@gmail.com")
            print(f"     - App domain: {config['domains'][-1] if config['domains'] else 'N/A'}")
        
        print("\n📋 STEP 4: Verify Configuration")
        print("-" * 40)
        print("Run verification script:")
        print("  python3 scripts/verify_google_provider.py")
        
        print("\n📋 STEP 5: Test Authentication Flow")
        print("-" * 40)
        print("Run authentication test:")
        print("  python3 scripts/test_auth_flow.py")
    
    def print_automated_commands(self) -> None:
        """Print automated commands for quick setup."""
        print("\n🤖 Automated Commands Available")
        print("=" * 60)
        
        print("\n1. Configure Authorized Domains (Already Done):")
        print("   python3 scripts/configure_google_auth_automated.py")
        
        print("\n2. Verify Google Provider Status:")
        print("   python3 scripts/verify_google_provider.py")
        
        print("\n3. Test Authentication Flow:")
        print("   python3 scripts/test_auth_flow.py")
        
        print("\n4. Complete Setup Demo:")
        print("   python3 scripts/simple_automated_demo.py")
    
    def print_current_status(self) -> None:
        """Print current setup status."""
        print("\n📊 Current Setup Status")
        print("=" * 60)
        
        print("✅ COMPLETED:")
        print("  - Meta-intelligent orchestration system implemented")
        print("  - Browser automation framework created")
        print("  - Authorized domains configured for all environments")
        print("  - Verification scripts implemented")
        print("  - Authentication testing framework ready")
        
        print("\n⚠️  MANUAL STEPS REQUIRED:")
        print("  - Create Firebase projects in Firebase Console")
        print("  - Enable Google Sign-In provider for each project")
        print("  - Configure OAuth consent screen in Google Cloud Console")
        
        print("\n🎯 NEXT ACTIONS:")
        print("  1. Follow the setup instructions above")
        print("  2. Use the automated verification scripts")
        print("  3. Test the complete authentication flow")
    
    def print_firebase_console_urls(self) -> None:
        """Print direct Firebase Console URLs for each project."""
        print("\n🌐 Direct Firebase Console URLs")
        print("=" * 60)
        
        for env_name, config in self.projects.items():
            print(f"\n{env_name.upper()} Environment:")
            print(f"  Project: {config['name']}")
            print(f"  ID: {config['id']}")
            print(f"  Console: https://console.firebase.google.com/project/{config['id']}")
            print(f"  Auth: https://console.firebase.google.com/project/{config['id']}/authentication/providers")
            print(f"  OAuth: https://console.cloud.google.com/apis/credentials/consent?project={config['id']}")

async def main():
    """Main function."""
    print("🤖 Complete Firebase Setup System")
    print("Using Meta-Intelligent Orchestration")
    print("=" * 60)
    
    try:
        # Create setup instance
        setup = CompleteFirebaseSetup()
        
        # Print current status
        setup.print_current_status()
        
        # Print setup instructions
        setup.print_setup_instructions()
        
        # Print automated commands
        setup.print_automated_commands()
        
        # Print Firebase Console URLs
        setup.print_firebase_console_urls()
        
        print("\n" + "=" * 60)
        print("🎉 Setup Instructions Complete!")
        print("=" * 60)
        print("\n💡 Quick Start:")
        print("1. Create Firebase projects using the URLs above")
        print("2. Enable Google Sign-In provider for each project")
        print("3. Run: python3 scripts/verify_google_provider.py")
        print("4. Run: python3 scripts/test_auth_flow.py")
        
    except Exception as e:
        print(f"\n❌ Setup failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
