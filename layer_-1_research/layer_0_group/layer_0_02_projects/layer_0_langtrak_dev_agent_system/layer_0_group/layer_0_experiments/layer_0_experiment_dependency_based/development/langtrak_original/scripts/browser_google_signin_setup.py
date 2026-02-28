#!/usr/bin/env python3
"""
Browser-based Google Sign-In setup for Firebase projects
This uses browser automation to properly configure Google Sign-In
"""

import subprocess
import time
import sys
from pathlib import Path

def run_command(command, timeout=30):
    """Run a command with timeout and return result."""
    try:
        result = subprocess.run(
            command, 
            shell=True, 
            capture_output=True, 
            text=True, 
            timeout=timeout
        )
        return result.returncode == 0, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return False, "", "Command timed out"
    except Exception as e:
        return False, "", str(e)

def main():
    """Main function to set up Google Sign-In via browser automation."""
    print("🚀 Browser-Based Google Sign-In Setup")
    print("=" * 50)
    print()
    print("This script will open the Firebase Console in your browser")
    print("and guide you through the Google Sign-In setup process.")
    print()
    print("📋 Manual Steps Required:")
    print("1. The script will open Firebase Console for each project")
    print("2. Navigate to Authentication > Sign-in method")
    print("3. Enable Google provider")
    print("4. Configure OAuth consent screen if prompted")
    print("5. Save the configuration")
    print()
    
    projects = {
        "dev": "lang-trak-dev",
        "staging": "lang-trak-staging", 
        "test": "lang-trak-test",
        "prod": "lang-trak-prod"
    }
    
    print("🔗 Firebase Console URLs:")
    for env, project_id in projects.items():
        url = f"https://console.firebase.google.com/u/1/project/{project_id}/authentication/providers"
        print(f"  {env.upper()}: {url}")
    
    print()
    print("🌐 Opening Firebase Console...")
    
    # Open Firebase Console for the first project
    first_project = list(projects.values())[0]
    url = f"https://console.firebase.google.com/u/1/project/{first_project}/authentication/providers"
    
    # Try to open in browser
    success, stdout, stderr = run_command(f"xdg-open '{url}'")
    if not success:
        print(f"❌ Failed to open browser automatically: {stderr}")
        print(f"Please manually open: {url}")
    else:
        print(f"✅ Opened Firebase Console for {first_project}")
    
    print()
    print("📝 Instructions for Google Sign-In Setup:")
    print("=" * 50)
    print()
    print("For EACH project, follow these steps:")
    print()
    print("1. 🔍 Navigate to Authentication > Sign-in method")
    print("2. 🔑 Find 'Google' in the providers list")
    print("3. ⚙️  Click the 'Edit' button (pencil icon)")
    print("4. ✅ Toggle 'Enable' to ON")
    print("5. 📧 Enter support email: 2025computer2025@gmail.com")
    print("6. 💾 Click 'Save'")
    print()
    print("If you see an OAuth consent screen setup prompt:")
    print("1. 🎯 Click 'Set up consent screen'")
    print("2. 👤 Choose 'External' user type")
    print("3. 📝 Fill in required fields:")
    print("   - App name: Lang Trak [Environment]")
    print("   - User support email: 2025computer2025@gmail.com")
    print("   - Developer contact: 2025computer2025@gmail.com")
    print("4. 💾 Save and continue")
    print()
    print("🔄 Repeat for all 4 projects:")
    for env, project_id in projects.items():
        url = f"https://console.firebase.google.com/u/1/project/{project_id}/authentication/providers"
        print(f"   {env.upper()}: {url}")
    
    print()
    print("✅ After completing all projects, run:")
    print("   python3 scripts/quick_verify.py")
    print()
    print("🎉 This will verify that Google Sign-In is properly enabled!")

if __name__ == "__main__":
    main()
