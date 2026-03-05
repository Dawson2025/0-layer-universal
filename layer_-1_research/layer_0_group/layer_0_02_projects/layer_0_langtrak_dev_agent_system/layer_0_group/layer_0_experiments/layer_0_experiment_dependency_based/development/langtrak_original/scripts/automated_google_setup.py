#!/usr/bin/env python3
# resource_id: "c07678f5-a2d1-4056-b97f-e22208e7eead"
# resource_type: "document"
# resource_name: "automated_google_setup"

"""
automated_google_setup.py

Automated Google Sign-In provider setup and OAuth consent screen configuration.
Uses our meta-intelligent orchestration system and browser automation framework.
"""

import sys
import json
import time
import asyncio
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Import our meta-intelligent orchestration system
from features.meta_intelligent_orchestration.core.browser_automation_strategy import BrowserAutomationStrategy
from features.meta_intelligent_orchestration.core.project_analyzer import ProjectAnalyzer, ProjectProfile, ProjectType

@dataclass
class GoogleProviderConfig:
    """Configuration for Google Sign-In provider setup."""
    project_id: str
    project_name: str
    environment: str
    domains: List[str]
    oauth_consent_screen: Dict[str, Any]
    web_client_config: Dict[str, Any]

class AutomatedGoogleSetup:
    """Automated Google Sign-In provider setup using meta-intelligent orchestration."""
    
    def __init__(self):
        self.browser_strategy = BrowserAutomationStrategy()
        self.project_analyzer = ProjectAnalyzer()
        self.environments = self._load_environment_configs()
    
    def _load_environment_configs(self) -> Dict[str, GoogleProviderConfig]:
        """Load environment configurations."""
        return {
            "development": GoogleProviderConfig(
                project_id="lang-trak-dev",
                project_name="Language Tracker Development",
                environment="development",
                domains=["localhost", "127.0.0.1", "lang-trak-dev.web.app", "lang-trak-dev.firebaseapp.com"],
                oauth_consent_screen={
                    "app_name": "Language Tracker Development",
                    "user_support_email": "2025computer2025@gmail.com",
                    "developer_contact": "2025computer2025@gmail.com",
                    "app_domain": "lang-trak-dev.web.app",
                    "app_logo": None,
                    "scopes": ["openid", "email", "profile"]
                },
                web_client_config={
                    "client_type": "web",
                    "redirect_uris": [
                        "http://localhost:3000/auth/callback",
                        "http://127.0.0.1:3000/auth/callback",
                        "https://lang-trak-dev.web.app/auth/callback"
                    ]
                }
            ),
            "staging": GoogleProviderConfig(
                project_id="lang-trak-staging",
                project_name="Language Tracker Staging",
                environment="staging",
                domains=["lang-trak-staging.web.app", "lang-trak-staging.firebaseapp.com"],
                oauth_consent_screen={
                    "app_name": "Language Tracker Staging",
                    "user_support_email": "2025computer2025@gmail.com",
                    "developer_contact": "2025computer2025@gmail.com",
                    "app_domain": "lang-trak-staging.web.app",
                    "app_logo": None,
                    "scopes": ["openid", "email", "profile"]
                },
                web_client_config={
                    "client_type": "web",
                    "redirect_uris": [
                        "https://lang-trak-staging.web.app/auth/callback"
                    ]
                }
            ),
            "testing": GoogleProviderConfig(
                project_id="lang-trak-test",
                project_name="Language Tracker Testing",
                environment="testing",
                domains=["lang-trak-test.web.app", "lang-trak-test.firebaseapp.com"],
                oauth_consent_screen={
                    "app_name": "Language Tracker Testing",
                    "user_support_email": "2025computer2025@gmail.com",
                    "developer_contact": "2025computer2025@gmail.com",
                    "app_domain": "lang-trak-test.web.app",
                    "app_logo": None,
                    "scopes": ["openid", "email", "profile"]
                },
                web_client_config={
                    "client_type": "web",
                    "redirect_uris": [
                        "https://lang-trak-test.web.app/auth/callback"
                    ]
                }
            ),
            "production": GoogleProviderConfig(
                project_id="lang-trak-prod",
                project_name="Language Tracker Production",
                environment="production",
                domains=["lang-trak-prod.web.app", "lang-trak-prod.firebaseapp.com"],
                oauth_consent_screen={
                    "app_name": "Language Tracker",
                    "user_support_email": "2025computer2025@gmail.com",
                    "developer_contact": "2025computer2025@gmail.com",
                    "app_domain": "lang-trak-prod.web.app",
                    "app_logo": None,
                    "scopes": ["openid", "email", "profile"]
                },
                web_client_config={
                    "client_type": "web",
                    "redirect_uris": [
                        "https://lang-trak-prod.web.app/auth/callback"
                    ]
                }
            )
        }
    
    async def setup_google_provider_for_environment(self, env_name: str) -> Dict[str, Any]:
        """Setup Google Sign-In provider for a specific environment."""
        print(f"🚀 Setting up Google Sign-In for {env_name} environment...")
        
        config = self.environments[env_name]
        
        # Step 1: Configure OAuth Consent Screen
        oauth_result = await self._configure_oauth_consent_screen(config)
        
        # Step 2: Enable Google Sign-In Provider in Firebase
        firebase_result = await self._enable_firebase_google_provider(config)
        
        # Step 3: Configure Web Client
        web_client_result = await self._configure_web_client(config)
        
        # Step 4: Verify Setup
        verification_result = await self._verify_google_provider_setup(config)
        
        return {
            "environment": env_name,
            "project_id": config.project_id,
            "oauth_consent_screen": oauth_result,
            "firebase_provider": firebase_result,
            "web_client": web_client_result,
            "verification": verification_result,
            "overall_success": all([
                oauth_result.get("success", False),
                firebase_result.get("success", False),
                web_client_result.get("success", False),
                verification_result.get("success", False)
            ])
        }
    
    async def _configure_oauth_consent_screen(self, config: GoogleProviderConfig) -> Dict[str, Any]:
        """Configure OAuth consent screen in Google Cloud Console."""
        print(f"  🔧 Configuring OAuth consent screen for {config.project_id}...")
        
        try:
            # Use browser automation to configure OAuth consent screen
            task_requirements = {
                "complexity": "medium",
                "browser": "chrome",
                "performance": "balanced",
                "debugging": True
            }
            
            selected_tool = self.browser_strategy.select_tool(task_requirements)
            print(f"  📱 Using {selected_tool} for OAuth configuration")
            
            # Navigate to Google Cloud Console OAuth consent screen
            oauth_url = f"https://console.cloud.google.com/apis/credentials/consent?project={config.project_id}"
            
            # Execute OAuth consent screen configuration
            result = await self.browser_strategy.execute_task(
                tool=selected_tool,
                task="configure_oauth_consent_screen",
                parameters={
                    "url": oauth_url,
                    "app_name": config.oauth_consent_screen["app_name"],
                    "user_support_email": config.oauth_consent_screen["user_support_email"],
                    "developer_contact": config.oauth_consent_screen["developer_contact"],
                    "app_domain": config.oauth_consent_screen["app_domain"],
                    "scopes": config.oauth_consent_screen["scopes"]
                }
            )
            
            return {
                "success": True,
                "message": "OAuth consent screen configured successfully",
                "details": result
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "message": "Failed to configure OAuth consent screen"
            }
    
    async def _enable_firebase_google_provider(self, config: GoogleProviderConfig) -> Dict[str, Any]:
        """Enable Google Sign-In provider in Firebase Console."""
        print(f"  🔥 Enabling Google Sign-In provider in Firebase for {config.project_id}...")
        
        try:
            # Use browser automation to enable Google provider in Firebase
            task_requirements = {
                "complexity": "medium",
                "browser": "chrome",
                "performance": "balanced",
                "debugging": True
            }
            
            selected_tool = self.browser_strategy.select_tool(task_requirements)
            print(f"  📱 Using {selected_tool} for Firebase configuration")
            
            # Navigate to Firebase Console Authentication
            firebase_url = f"https://console.firebase.google.com/project/{config.project_id}/authentication/providers"
            
            # Execute Firebase Google provider enablement
            result = await self.browser_strategy.execute_task(
                tool=selected_tool,
                task="enable_firebase_google_provider",
                parameters={
                    "url": firebase_url,
                    "project_id": config.project_id,
                    "provider_id": "google.com",
                    "enable_provider": True
                }
            )
            
            return {
                "success": True,
                "message": "Google Sign-In provider enabled in Firebase",
                "details": result
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "message": "Failed to enable Google Sign-In provider in Firebase"
            }
    
    async def _configure_web_client(self, config: GoogleProviderConfig) -> Dict[str, Any]:
        """Configure web client for Google Sign-In."""
        print(f"  🌐 Configuring web client for {config.project_id}...")
        
        try:
            # Use browser automation to configure web client
            task_requirements = {
                "complexity": "medium",
                "browser": "chrome",
                "performance": "balanced",
                "debugging": True
            }
            
            selected_tool = self.browser_strategy.select_tool(task_requirements)
            print(f"  📱 Using {selected_tool} for web client configuration")
            
            # Navigate to Google Cloud Console Credentials
            credentials_url = f"https://console.cloud.google.com/apis/credentials?project={config.project_id}"
            
            # Execute web client configuration
            result = await self.browser_strategy.execute_task(
                tool=selected_tool,
                task="configure_web_client",
                parameters={
                    "url": credentials_url,
                    "project_id": config.project_id,
                    "client_type": config.web_client_config["client_type"],
                    "redirect_uris": config.web_client_config["redirect_uris"]
                }
            )
            
            return {
                "success": True,
                "message": "Web client configured successfully",
                "details": result
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "message": "Failed to configure web client"
            }
    
    async def _verify_google_provider_setup(self, config: GoogleProviderConfig) -> Dict[str, Any]:
        """Verify that Google Sign-In provider is properly configured."""
        print(f"  ✅ Verifying Google Sign-In setup for {config.project_id}...")
        
        try:
            # Use our existing verification script
            import subprocess
            
            result = subprocess.run([
                "python3", "scripts/verify_google_provider.py"
            ], capture_output=True, text=True, check=True)
            
            # Parse verification results
            verification_success = "Google Sign-In is ENABLED" in result.stdout
            
            return {
                "success": verification_success,
                "message": "Google Sign-In provider verification completed",
                "details": result.stdout
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "message": "Failed to verify Google Sign-In setup"
            }
    
    async def setup_all_environments(self) -> Dict[str, Any]:
        """Setup Google Sign-In provider for all environments."""
        print("🔥 Automated Google Sign-In Setup")
        print("=" * 60)
        print("Using Meta-Intelligent Orchestration System")
        print("=" * 60)
        
        results = {}
        
        for env_name in self.environments.keys():
            print(f"\n--- {env_name.upper()} Environment ---")
            results[env_name] = await self.setup_google_provider_for_environment(env_name)
            
            # Add delay between environments to avoid rate limiting
            await asyncio.sleep(2)
        
        return results
    
    def print_setup_summary(self, results: Dict[str, Any]) -> None:
        """Print setup summary."""
        print("\n" + "=" * 60)
        print("🎯 AUTOMATED GOOGLE SETUP SUMMARY")
        print("=" * 60)
        
        successful_envs = 0
        total_envs = len(results)
        
        for env_name, result in results.items():
            project_id = result["project_id"]
            overall_success = result["overall_success"]
            
            if overall_success:
                print(f"✅ {env_name.upper()} ({project_id}) - COMPLETE")
                successful_envs += 1
            else:
                print(f"❌ {env_name.upper()} ({project_id}) - FAILED")
                print(f"   OAuth Consent: {'✅' if result['oauth_consent_screen']['success'] else '❌'}")
                print(f"   Firebase Provider: {'✅' if result['firebase_provider']['success'] else '❌'}")
                print(f"   Web Client: {'✅' if result['web_client']['success'] else '❌'}")
                print(f"   Verification: {'✅' if result['verification']['success'] else '❌'}")
        
        print(f"\n📊 Results: {successful_envs}/{total_envs} environments configured successfully")
        
        if successful_envs == total_envs:
            print("🎉 All environments are ready for Google Sign-In!")
        else:
            print("⚠️  Some environments need manual intervention")
            print("\n🔧 Manual steps if needed:")
            print("1. Check Google Cloud Console for OAuth consent screen")
            print("2. Verify Firebase Console authentication settings")
            print("3. Check web client configuration")

async def main():
    """Main function."""
    print("🤖 Automated Google Sign-In Setup")
    print("Using Meta-Intelligent Orchestration System")
    print("=" * 60)
    
    try:
        # Create automated setup instance
        setup = AutomatedGoogleSetup()
        
        # Setup all environments
        results = await setup.setup_all_environments()
        
        # Print summary
        setup.print_setup_summary(results)
        
        # Check overall success
        all_successful = all(result["overall_success"] for result in results.values())
        
        sys.exit(0 if all_successful else 1)
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Setup interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Setup failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
