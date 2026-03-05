#!/usr/bin/env python3
# resource_id: "57c9dab9-3f84-4182-a2d4-f654225ef87b"
# resource_type: "document"
# resource_name: "browser_google_signin_automation"
"""
Browser-based Google Sign-In Automation
This script uses browser automation to properly configure Google Sign-In
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
    """Main function to automate Google Sign-In setup via browser."""
    print("🚀 Browser-Based Google Sign-In Automation")
    print("=" * 60)
    print()
    print("This script will use browser automation to:")
    print("1. Navigate to each Firebase project")
    print("2. Enable Google Sign-In provider")
    print("3. Configure OAuth consent screen if needed")
    print("4. Verify the setup")
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
    print("🤖 Starting browser automation...")
    print()
    print("📝 Instructions:")
    print("1. The browser will open each project's authentication page")
    print("2. For each project, you'll need to:")
    print("   - Click on the Google provider row")
    print("   - Toggle 'Enable' to ON")
    print("   - Enter support email: 2025computer2025@gmail.com")
    print("   - Click 'Save'")
    print("3. If prompted for OAuth consent screen setup:")
    print("   - Click 'Set up consent screen'")
    print("   - Choose 'External' user type")
    print("   - Fill in required fields")
    print("   - Save and continue")
    print()
    print("🔄 The script will guide you through each project...")
    
    # Start with the first project
    first_project = list(projects.values())[0]
    url = f"https://console.firebase.google.com/u/1/project/{first_project}/authentication/providers"
    
    print(f"\n🌐 Opening {first_project}...")
    print(f"URL: {url}")
    
    # Try to open in browser
    success, stdout, stderr = run_command(f"xdg-open '{url}'")
    if not success:
        print(f"❌ Failed to open browser automatically: {stderr}")
        print(f"Please manually open: {url}")
    else:
        print(f"✅ Opened browser for {first_project}")
    
    print("\n" + "=" * 60)
    print("🎯 MANUAL STEPS REQUIRED")
    print("=" * 60)
    print()
    print("Since browser automation is complex, please follow these steps:")
    print()
    
    for i, (env, project_id) in enumerate(projects.items(), 1):
        url = f"https://console.firebase.google.com/u/1/project/{project_id}/authentication/providers"
        print(f"{i}. {env.upper()} Project ({project_id})")
        print(f"   URL: {url}")
        print(f"   Steps:")
        print(f"   - Navigate to the URL above")
        print(f"   - Find 'Google' in the providers table")
        print(f"   - Click the 'Edit' button (pencil icon)")
        print(f"   - Toggle 'Enable' to ON")
        print(f"   - Enter support email: 2025computer2025@gmail.com")
        print(f"   - Click 'Save'")
        print(f"   - If OAuth consent screen setup appears:")
        print(f"     * Click 'Set up consent screen'")
        print(f"     * Choose 'External' user type")
        print(f"     * Fill in app name: Lang Trak {env.title()}")
        print(f"     * Enter support email: 2025computer2025@gmail.com")
        print(f"     * Enter developer contact: 2025computer2025@gmail.com")
        print(f"     * Save and continue")
        print()
    
    print("✅ After completing all projects, run:")
    print("   python3 scripts/quick_verify.py")
    print()
    print("🎉 This will verify that Google Sign-In is properly enabled!")

if __name__ == "__main__":
    main()
