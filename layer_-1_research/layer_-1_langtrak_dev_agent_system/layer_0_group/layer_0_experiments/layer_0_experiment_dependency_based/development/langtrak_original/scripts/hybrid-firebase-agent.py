#!/usr/bin/env python3

"""
hybrid-firebase-agent.py

Hybrid approach combining API calls and browser automation for maximum efficiency.
This script demonstrates how an agentic AI can:
1. Use APIs when possible (faster, more reliable)
2. Fall back to browser automation when APIs don't work
3. Handle authentication seamlessly
"""

import asyncio
import json
import subprocess
import os
from typing import List, Dict, Optional
from playwright.async_api import async_playwright

class HybridFirebaseAgent:
    def __init__(self):
        self.browser = None
        self.page = None
        self.access_token = None
    
    async def setup_authentication(self):
        """Set up both API and browser authentication."""
        print("🔐 Setting up hybrid authentication...")
        
        # Try to get API access token
        try:
            result = subprocess.run(
                ["gcloud", "auth", "print-access-token"], 
                capture_output=True, text=True, check=True
            )
            self.access_token = result.stdout.strip()
            print("✅ API authentication ready")
        except:
            print("⚠️ API authentication not available")
        
        # Setup browser authentication
        playwright = await async_playwright().start()
        self.browser = await playwright.chromium.launch_persistent_context(
            user_data_dir="./browser-data",
            headless=True,
            args=["--disable-blink-features=AutomationControlled"]
        )
        self.page = await self.browser.new_page()
        print("✅ Browser authentication ready")
    
    async def configure_authorized_domains(self, project_id: str, domains: List[str]):
        """Configure authorized domains using the best available method."""
        print(f"🌐 Configuring authorized domains for {project_id}...")
        
        # Try API first (fastest)
        if self.access_token and await self._configure_domains_via_api(project_id, domains):
            print("✅ Domains configured via API")
            return True
        
        # Fall back to browser automation
        print("🔄 Falling back to browser automation...")
        if await self._configure_domains_via_browser(project_id, domains):
            print("✅ Domains configured via browser")
            return True
        
        print("❌ Failed to configure domains")
        return False
    
    async def _configure_domains_via_api(self, project_id: str, domains: List[str]) -> bool:
        """Try to configure domains using the Identity Toolkit API."""
        if not self.access_token:
            return False
        
        try:
            # First, try to get current config
            import requests
            
            headers = {
                "Authorization": f"Bearer {self.access_token}",
                "X-Goog-User-Project": project_id,
                "Content-Type": "application/json"
            }
            
            # Get current configuration
            url = f"https://identitytoolkit.googleapis.com/admin/v2/projects/{project_id}/config"
            response = requests.get(url, headers=headers)
            
            if response.status_code == 404:
                print("⚠️ Auth configuration not found - needs browser setup")
                return False
            
            if response.status_code != 200:
                print(f"⚠️ API error: {response.status_code}")
                return False
            
            # Update configuration
            current_config = response.json()
            current_domains = current_config.get("authorizedDomains", [])
            
            # Merge domains
            new_domains = list(set(current_domains + domains))
            
            patch_data = {"authorizedDomains": new_domains}
            
            # Apply patch
            patch_url = f"{url}?updateMask=authorizedDomains"
            patch_response = requests.patch(patch_url, headers=headers, json=patch_data)
            
            if patch_response.status_code == 200:
                return True
            else:
                print(f"⚠️ Patch failed: {patch_response.status_code}")
                return False
                
        except Exception as e:
            print(f"⚠️ API method failed: {e}")
            return False
    
    async def _configure_domains_via_browser(self, project_id: str, domains: List[str]) -> bool:
        """Configure domains using browser automation."""
        try:
            # Navigate to Firebase Console
            await self.page.goto(f"https://console.firebase.google.com/project/{project_id}/authentication")
            
            # Check if auth is enabled, if not enable it
            try:
                await self.page.wait_for_selector('[data-testid="auth-providers"]', timeout=5000)
            except:
                # Try to enable auth
                try:
                    await self.page.click('button:has-text("Get started")')
                    await self.page.wait_for_selector('[data-testid="auth-providers"]', timeout=10000)
                except:
                    print("❌ Could not enable Firebase Auth via browser")
                    return False
            
            # Navigate to settings
            await self.page.goto(f"https://console.firebase.google.com/project/{project_id}/authentication/settings")
            
            # Add domains
            for domain in domains:
                try:
                    # Find the domain input field
                    await self.page.fill('input[placeholder*="domain"], input[name*="domain"]', domain)
                    await self.page.click('button:has-text("Add"), button[type="submit"]')
                    print(f"  ✅ Added domain: {domain}")
                except Exception as e:
                    print(f"  ⚠️ Could not add domain {domain}: {e}")
            
            # Save changes
            try:
                await self.page.click('button:has-text("Save")')
                await self.page.wait_for_timeout(2000)  # Wait for save
                return True
            except Exception as e:
                print(f"⚠️ Could not save changes: {e}")
                return False
                
        except Exception as e:
            print(f"❌ Browser method failed: {e}")
            return False
    
    async def close(self):
        """Clean up resources."""
        if self.browser:
            await self.browser.close()

async def main():
    """Main function demonstrating hybrid approach."""
    agent = HybridFirebaseAgent()
    
    try:
        # Setup authentication
        await agent.setup_authentication()
        
        # Configure domains for both projects
        projects = ["lang-trak-dev", "lang-trak-prod"]
        domains = ["localhost", "127.0.0.1"]
        
        for project in projects:
            print(f"\n🎯 Configuring {project}...")
            success = await agent.configure_authorized_domains(project, domains)
            if success:
                print(f"✅ {project} configured successfully")
            else:
                print(f"❌ {project} configuration failed")
    
    finally:
        await agent.close()

if __name__ == "__main__":
    asyncio.run(main())

