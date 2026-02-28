#!/usr/bin/env python3

"""
auto_firebase.py

Automated Firebase operations - no manual authentication required.
Just run this script and it handles everything automatically.
"""

import sys
import subprocess
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from scripts.auth_manager import AuthManager

def main():
    """Main automated Firebase operations."""
    print("🔥 Automated Firebase Operations")
    print("=" * 50)
    
    # Initialize auth manager
    auth_manager = AuthManager()
    
    # Check if authenticated
    if not auth_manager.is_authenticated():
        print("❌ Not authenticated. Please run setup first:")
        print("   python3 scripts/auth_manager.py")
        return False
    
    print("✅ Authentication verified")
    
    # Configure all Firebase projects with Google Sign-In
    print("\n🔧 Configuring Google Sign-In for all environments...")
    results = auth_manager.configure_all_firebase_projects()
    
    # Show results
    print(f"\n📊 Configuration Results:")
    successful = sum(1 for success in results.values() if success)
    total = len(results)
    
    for project_id, success in results.items():
        status = "✅" if success else "❌"
        print(f"  {status} {project_id}")
    
    if successful == total:
        print(f"\n🎉 All {total} environments configured successfully!")
        print("🔒 Google Sign-In is now ready across all environments")
        print("🚀 You can now use Google authentication in your app")
        return True
    else:
        print(f"\n⚠️ {total - successful} environments failed to configure")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
