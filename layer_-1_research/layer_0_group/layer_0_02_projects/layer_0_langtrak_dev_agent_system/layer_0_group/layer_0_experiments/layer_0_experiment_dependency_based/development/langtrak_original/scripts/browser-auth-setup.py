#!/usr/bin/env python3
# resource_id: "1edc670a-1ba3-46a4-9fba-4ac30ad1099a"
# resource_type: "document"
# resource_name: "browser-auth-setup"

"""
browser-auth-setup.py

Sets up browser authentication for agentic AI using Playwright.
This approach allows the AI to authenticate with Google accounts and maintain
sessions for Firebase Console automation.
"""

import asyncio
import json
import os
from playwright.async_api import async_playwright

async def setup_browser_authentication():
    """Set up browser authentication for agentic AI."""
    
    async with async_playwright() as p:
        # Launch browser with persistent context
        browser = await p.chromium.launch_persistent_context(
            user_data_dir="./browser-data",
            headless=False,  # Set to True for headless operation
            args=[
                "--disable-blink-features=AutomationControlled",
                "--disable-web-security",
                "--disable-features=VizDisplayCompositor"
            ]
        )
        
        page = await browser.new_page()
        
        print("🌐 Setting up browser authentication...")
        
        # Navigate to Google login
        await page.goto("https://accounts.google.com/signin")
        
        print("📝 Please complete the Google authentication in the browser window")
        print("   - Sign in with your Google account that has access to Firebase projects")
        print("   - Complete any 2FA if required")
        print("   - Press Enter here when done...")
        
        # Wait for user to complete authentication
        input("Press Enter when authentication is complete...")
        
        # Test authentication by navigating to Firebase Console
        print("🧪 Testing authentication...")
        await page.goto("https://console.firebase.google.com/")
        
        # Check if we can see projects
        try:
            await page.wait_for_selector('[data-testid="project-card"]', timeout=10000)
            print("✅ Authentication successful! Can access Firebase Console")
        except:
            print("❌ Authentication failed or incomplete")
            return False
        
        # Save authentication state
        auth_state = {
            "authenticated": True,
            "user_data_dir": "./browser-data",
            "timestamp": str(asyncio.get_event_loop().time())
        }
        
        with open("browser-auth-state.json", "w") as f:
            json.dump(auth_state, f, indent=2)
        
        print("💾 Authentication state saved to browser-auth-state.json")
        print("🎉 Browser authentication setup complete!")
        
        await browser.close()
        return True

def create_browser_automation_script():
    """Create a script for agentic AI to use browser authentication."""
    
    script_content = '''#!/usr/bin/env python3

"""
firebase-browser-automation.py

Browser automation script for agentic AI to manage Firebase Console.
Uses pre-authenticated browser session.
"""

import asyncio
import json
from playwright.async_api import async_playwright

class FirebaseBrowserAutomation:
    def __init__(self):
        self.browser = None
        self.page = None
    
    async def start(self):
        """Start browser with authenticated session."""
        playwright = await async_playwright().start()
        
        self.browser = await playwright.chromium.launch_persistent_context(
            user_data_dir="./browser-data",
            headless=True,  # Run headless for automation
            args=["--disable-blink-features=AutomationControlled"]
        )
        
        self.page = await self.browser.new_page()
    
    async def enable_firebase_auth(self, project_id: str):
        """Enable Firebase Authentication for a project."""
        print(f"🔐 Enabling Firebase Auth for project: {project_id}")
        
        # Navigate to project
        await self.page.goto(f"https://console.firebase.google.com/project/{project_id}")
        
        # Navigate to Authentication
        await self.page.goto(f"https://console.firebase.google.com/project/{project_id}/authentication")
        
        # Check if auth is already enabled
        try:
            await self.page.wait_for_selector('[data-testid="auth-providers"]', timeout=5000)
            print("✅ Firebase Auth is already enabled")
            return True
        except:
            pass
        
        # Try to enable auth
        try:
            await self.page.click('button:has-text("Get started")')
            await self.page.wait_for_selector('[data-testid="auth-providers"]', timeout=10000)
            print("✅ Firebase Auth enabled successfully")
            return True
        except Exception as e:
            print(f"❌ Failed to enable Firebase Auth: {e}")
            return False
    
    async def configure_authorized_domains(self, project_id: str, domains: list):
        """Configure authorized domains for Firebase Auth."""
        print(f"🌐 Configuring authorized domains for project: {project_id}")
        
        # Navigate to auth settings
        await self.page.goto(f"https://console.firebase.google.com/project/{project_id}/authentication/settings")
        
        # Add domains
        for domain in domains:
            try:
                # Find the add domain input
                await self.page.fill('input[placeholder*="domain"]', domain)
                await self.page.click('button:has-text("Add")')
                print(f"  ✅ Added domain: {domain}")
            except Exception as e:
                print(f"  ❌ Failed to add domain {domain}: {e}")
        
        # Save changes
        try:
            await self.page.click('button:has-text("Save")')
            print("✅ Authorized domains saved")
            return True
        except Exception as e:
            print(f"❌ Failed to save domains: {e}")
            return False
    
    async def close(self):
        """Close browser."""
        if self.browser:
            await self.browser.close()

# Example usage
async def main():
    automation = FirebaseBrowserAutomation()
    
    try:
        await automation.start()
        
        # Enable auth for production project
        await automation.enable_firebase_auth("lang-trak-prod")
        
        # Configure authorized domains
        domains = ["localhost", "127.0.0.1"]
        await automation.configure_authorized_domains("lang-trak-prod", domains)
        
    finally:
        await automation.close()

if __name__ == "__main__":
    asyncio.run(main())
'''
    
    with open("firebase-browser-automation.py", "w") as f:
        f.write(script_content)
    
    print("📝 Created firebase-browser-automation.py for agentic AI")

async def main():
    print("🤖 Setting up browser authentication for agentic AI")
    print("=" * 50)
    
    # Setup browser authentication
    success = await setup_browser_authentication()
    
    if success:
        # Create automation script
        create_browser_automation_script()
        print("\n🎉 Browser authentication setup complete!")
        print("📝 Use firebase-browser-automation.py for Firebase Console automation")
    else:
        print("\n❌ Browser authentication setup failed")

if __name__ == "__main__":
    asyncio.run(main())

