#!/usr/bin/env python3

"""
optimal-firebase-agent.py

The optimal setup for agentic AI Firebase management combining:
- API calls (fastest)
- Playwright automation (most reliable)
- Chrome DevTools (best debugging)
- Intelligent fallback strategies
"""

import asyncio
import json
import subprocess
import time
from typing import List, Dict, Optional, Tuple
from playwright.async_api import async_playwright

class OptimalFirebaseAgent:
    """Optimal Firebase management agent combining multiple approaches."""
    
    def __init__(self, project_id: str):
        self.project_id = project_id
        self.access_token = None
        self.browser = None
        self.page = None
        self.method_preferences = ["api", "playwright", "chrome_devtools"]
    
    async def setup_authentication(self) -> bool:
        """Set up authentication for all methods."""
        print(f"🔐 Setting up authentication for {self.project_id}...")
        
        # Setup API authentication
        try:
            result = subprocess.run(
                ["gcloud", "auth", "print-access-token"],
                check=True, capture_output=True, text=True
            )
            self.access_token = result.stdout.strip()
            print("✅ API authentication ready")
        except:
            print("⚠️ API authentication not available")
        
        # Setup browser authentication
        try:
            playwright = await async_playwright().start()
            self.browser = await playwright.chromium.launch_persistent_context(
                user_data_dir=f"./browser-data-{self.project_id}",
                headless=True,
                args=["--disable-blink-features=AutomationControlled"]
            )
            self.page = await self.browser.new_page()
            print("✅ Browser authentication ready")
        except Exception as e:
            print(f"⚠️ Browser authentication failed: {e}")
        
        return True
    
    async def configure_authorized_domains(self, domains: List[str]) -> bool:
        """Configure authorized domains using the best available method."""
        print(f"🌐 Configuring authorized domains: {', '.join(domains)}")
        
        # Try each method in order of preference
        for method in self.method_preferences:
            print(f"🔄 Trying {method} approach...")
            
            if method == "api" and await self._configure_domains_via_api(domains):
                print(f"✅ Success with {method}")
                return True
            
            elif method == "playwright" and await self._configure_domains_via_playwright(domains):
                print(f"✅ Success with {method}")
                return True
            
            elif method == "chrome_devtools" and await self._configure_domains_via_devtools(domains):
                print(f"✅ Success with {method}")
                return True
            
            print(f"⚠️ {method} approach failed, trying next...")
        
        print("❌ All methods failed")
        return False
    
    async def _configure_domains_via_api(self, domains: List[str]) -> bool:
        """Configure domains using Identity Toolkit API."""
        if not self.access_token:
            return False
        
        try:
            import requests
            
            headers = {
                "Authorization": f"Bearer {self.access_token}",
                "X-Goog-User-Project": self.project_id,
                "Content-Type": "application/json"
            }
            
            # Get current config
            url = f"https://identitytoolkit.googleapis.com/admin/v2/projects/{self.project_id}/config"
            response = requests.get(url, headers=headers)
            
            if response.status_code == 404:
                print("⚠️ Auth not initialized - API cannot configure")
                return False
            
            if response.status_code != 200:
                return False
            
            # Update config
            current_config = response.json()
            current_domains = current_config.get("authorizedDomains", [])
            new_domains = list(set(current_domains + domains))
            
            update_data = {"authorizedDomains": new_domains}
            patch_url = f"{url}?updateMask=authorizedDomains"
            
            patch_response = requests.patch(patch_url, headers=headers, json=update_data)
            return patch_response.status_code == 200
            
        except Exception as e:
            print(f"API error: {e}")
            return False
    
    async def _configure_domains_via_playwright(self, domains: List[str]) -> bool:
        """Configure domains using Playwright browser automation."""
        if not self.page:
            return False
        
        try:
            # Navigate to Firebase Console
            await self.page.goto(f"https://console.firebase.google.com/project/{self.project_id}/authentication")
            await self.page.wait_for_timeout(3000)
            
            # Check if auth is enabled, if not enable it
            try:
                await self.page.wait_for_selector('[data-testid="auth-providers"]', timeout=5000)
            except:
                # Try to enable auth
                try:
                    await self.page.click('button:has-text("Get started")')
                    await self.page.wait_for_selector('[data-testid="auth-providers"]', timeout=10000)
                except:
                    return False
            
            # Navigate to settings
            await self.page.goto(f"https://console.firebase.google.com/project/{self.project_id}/authentication/settings")
            await self.page.wait_for_timeout(2000)
            
            # Add domains
            for domain in domains:
                try:
                    # Find domain input and add button
                    await self.page.fill('input[placeholder*="domain"], input[name*="domain"]', domain)
                    await self.page.click('button:has-text("Add"), button[type="submit"]')
                    await self.page.wait_for_timeout(1000)
                except:
                    pass
            
            # Save changes
            try:
                await self.page.click('button:has-text("Save")')
                await self.page.wait_for_timeout(2000)
                return True
            except:
                return False
                
        except Exception as e:
            print(f"Playwright error: {e}")
            return False
    
    async def _configure_domains_via_devtools(self, domains: List[str]) -> bool:
        """Configure domains using Chrome DevTools (placeholder for MCP integration)."""
        # This would integrate with Chrome DevTools MCP
        # For now, return False to indicate it's not implemented
        print("Chrome DevTools approach not implemented in this demo")
        return False
    
    async def enable_firebase_auth(self) -> bool:
        """Enable Firebase Authentication using the best available method."""
        print(f"🔐 Enabling Firebase Auth for {self.project_id}...")
        
        # Try Playwright first (most reliable for initialization)
        if self.page and await self._enable_auth_via_playwright():
            return True
        
        # Try API (if already initialized)
        if self.access_token and await self._enable_auth_via_api():
            return True
        
        return False
    
    async def _enable_auth_via_playwright(self) -> bool:
        """Enable Firebase Auth using Playwright."""
        try:
            await self.page.goto(f"https://console.firebase.google.com/project/{self.project_id}/authentication")
            await self.page.wait_for_timeout(3000)
            
            # Check if already enabled
            try:
                await self.page.wait_for_selector('[data-testid="auth-providers"]', timeout=5000)
                print("✅ Firebase Auth already enabled")
                return True
            except:
                pass
            
            # Try to enable
            try:
                await self.page.click('button:has-text("Get started")')
                await self.page.wait_for_selector('[data-testid="auth-providers"]', timeout=10000)
                print("✅ Firebase Auth enabled successfully")
                return True
            except:
                return False
                
        except Exception as e:
            print(f"Playwright auth enable error: {e}")
            return False
    
    async def _enable_auth_via_api(self) -> bool:
        """Enable Firebase Auth using API (if possible)."""
        # API cannot initialize auth - this is a placeholder
        return False
    
    async def get_project_status(self) -> Dict:
        """Get comprehensive project status."""
        status = {
            "project_id": self.project_id,
            "auth_initialized": False,
            "auth_providers": [],
            "authorized_domains": [],
            "api_available": bool(self.access_token),
            "browser_available": bool(self.page)
        }
        
        # Check via API
        if self.access_token:
            try:
                import requests
                headers = {
                    "Authorization": f"Bearer {self.access_token}",
                    "X-Goog-User-Project": self.project_id
                }
                url = f"https://identitytoolkit.googleapis.com/admin/v2/projects/{self.project_id}/config"
                response = requests.get(url, headers=headers)
                
                if response.status_code == 200:
                    config = response.json()
                    status["auth_initialized"] = True
                    status["authorized_domains"] = config.get("authorizedDomains", [])
                    status["auth_providers"] = config.get("signIn", {}).get("providers", [])
                elif response.status_code == 404:
                    status["auth_initialized"] = False
            except:
                pass
        
        return status
    
    async def close(self):
        """Clean up resources."""
        if self.browser:
            await self.browser.close()

async def main():
    """Demonstrate the optimal Firebase agent."""
    print("🚀 Optimal Firebase Agent Demo")
    print("=" * 50)
    
    projects = ["lang-trak-dev", "lang-trak-prod"]
    domains_to_add = ["localhost", "127.0.0.1"]
    
    for project_id in projects:
        print(f"\n🎯 Managing project: {project_id}")
        
        agent = OptimalFirebaseAgent(project_id)
        
        try:
            # Setup authentication
            await agent.setup_authentication()
            
            # Get project status
            status = await agent.get_project_status()
            print(f"📊 Project Status:")
            print(f"  Auth Initialized: {status['auth_initialized']}")
            print(f"  API Available: {status['api_available']}")
            print(f"  Browser Available: {status['browser_available']}")
            print(f"  Current Domains: {', '.join(status['authorized_domains']) if status['authorized_domains'] else '(none)'}")
            
            # Enable auth if needed
            if not status['auth_initialized']:
                print("🔐 Firebase Auth not initialized, enabling...")
                if await agent.enable_firebase_auth():
                    print("✅ Firebase Auth enabled")
                else:
                    print("❌ Failed to enable Firebase Auth")
                    continue
            
            # Configure domains
            success = await agent.configure_authorized_domains(domains_to_add)
            if success:
                print(f"✅ {project_id} configuration complete")
            else:
                print(f"❌ {project_id} configuration failed")
        
        finally:
            await agent.close()
    
    print("\n🎉 Optimal Firebase Agent demo complete!")

if __name__ == "__main__":
    asyncio.run(main())

