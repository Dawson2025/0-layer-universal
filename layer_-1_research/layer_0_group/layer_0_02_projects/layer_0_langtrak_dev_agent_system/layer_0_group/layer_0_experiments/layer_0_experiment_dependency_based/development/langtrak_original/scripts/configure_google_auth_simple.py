#!/usr/bin/env python3
# resource_id: "3ef3b495-2a3a-4109-85ef-4487a5dbf581"
# resource_type: "document"
# resource_name: "configure_google_auth_simple"

"""
configure_google_auth_simple.py

Simple script to configure Google Sign-In authentication for all project environments.
Uses Firebase CLI and Google Cloud APIs directly.
"""

import asyncio
import json
import subprocess
import sys
from datetime import datetime
from typing import Dict, List, Any, Optional

class GoogleAuthConfigurator:
    """Simple Google Sign-In authentication configurator."""
    
    def __init__(self):
        self.projects = {
            "lang-trak-dev": {
                "domains": ["localhost", "127.0.0.1", "lang-trak-dev.web.app", "lang-trak-dev.firebaseapp.com"],
                "environment": "development"
            },
            "lang-trak-staging": {
                "domains": ["lang-trak-staging.web.app", "lang-trak-staging.firebaseapp.com"],
                "environment": "staging"
            },
            "lang-trak-test": {
                "domains": ["lang-trak-test.web.app", "lang-trak-test.firebaseapp.com"],
                "environment": "testing"
            },
            "lang-trak-prod": {
                "domains": ["lang-trak-prod.web.app", "lang-trak-prod.firebaseapp.com"],
                "environment": "production"
            }
        }
        self.results = {}
    
    async def configure_all_environments(self) -> Dict[str, Any]:
        """Configure Google Sign-In for all environments."""
        print("🔥 Google Sign-In Authentication Configuration")
        print("=" * 60)
        print(f"📅 Started: {datetime.now().isoformat()}")
        print(f"🎯 Target Projects: {list(self.projects.keys())}")
        print()
        
        # Step 1: Check current state
        print("🔍 Step 1: Checking current authentication state...")
        current_state = await self._check_current_state()
        self._print_current_state(current_state)
        
        # Step 2: Configure each project
        print("\n🚀 Step 2: Configuring authentication for each project...")
        for project_id, config in self.projects.items():
            print(f"\n--- Configuring {project_id} ({config['environment']}) ---")
            result = await self._configure_project(project_id, config)
            self.results[project_id] = result
        
        # Step 3: Verify configurations
        print("\n✅ Step 3: Verifying configurations...")
        verification = await self._verify_all_configurations()
        
        # Step 4: Generate report
        print("\n📊 Step 4: Generating report...")
        report = self._generate_report(current_state, verification)
        
        return report
    
    async def _check_current_state(self) -> Dict[str, Any]:
        """Check current authentication state for all projects."""
        state = {
            "timestamp": datetime.now().isoformat(),
            "projects": {}
        }
        
        for project_id in self.projects.keys():
            print(f"  🔍 Checking {project_id}...")
            
            try:
                # Switch to project
                await self._switch_to_project(project_id)
                
                # Check if auth is initialized
                auth_initialized = await self._check_auth_initialized(project_id)
                
                # Get current authorized domains
                current_domains = await self._get_current_domains(project_id)
                
                # Check Google provider status
                google_enabled = await self._check_google_provider(project_id)
                
                state["projects"][project_id] = {
                    "auth_initialized": auth_initialized,
                    "current_domains": current_domains,
                    "google_provider_enabled": google_enabled,
                    "status": "configured" if auth_initialized and google_enabled else "needs_configuration"
                }
                
            except Exception as e:
                print(f"    ❌ Error checking {project_id}: {e}")
                state["projects"][project_id] = {
                    "auth_initialized": False,
                    "current_domains": [],
                    "google_provider_enabled": False,
                    "status": "error",
                    "error": str(e)
                }
        
        return state
    
    async def _configure_project(self, project_id: str, config: Dict[str, Any]) -> Dict[str, Any]:
        """Configure authentication for a specific project."""
        result = {
            "project_id": project_id,
            "environment": config["environment"],
            "domains": config["domains"],
            "steps_completed": [],
            "success": False,
            "errors": []
        }
        
        try:
            # Step 1: Switch to project
            print(f"    🔄 Switching to {project_id}...")
            if await self._switch_to_project(project_id):
                result["steps_completed"].append("switch_to_project")
            else:
                result["errors"].append("Failed to switch to project")
                return result
            
            # Step 2: Initialize Firebase Auth if needed
            print(f"    🔧 Initializing Firebase Auth...")
            if await self._initialize_firebase_auth(project_id):
                result["steps_completed"].append("initialize_auth")
            else:
                result["errors"].append("Failed to initialize Firebase Auth")
            
            # Step 3: Enable Google provider
            print(f"    🔑 Enabling Google Sign-In provider...")
            if await self._enable_google_provider(project_id):
                result["steps_completed"].append("enable_google_provider")
            else:
                result["errors"].append("Failed to enable Google provider")
            
            # Step 4: Configure authorized domains
            print(f"    🌐 Configuring authorized domains...")
            if await self._configure_authorized_domains(project_id, config["domains"]):
                result["steps_completed"].append("configure_domains")
            else:
                result["errors"].append("Failed to configure authorized domains")
            
            # Step 5: Verify configuration
            print(f"    ✅ Verifying configuration...")
            verification = await self._verify_project_configuration(project_id, config["domains"])
            if verification["success"]:
                result["steps_completed"].append("verify_configuration")
                result["success"] = True
                print(f"    ✅ Success: {project_id}")
            else:
                result["errors"].extend(verification["errors"])
                print(f"    ❌ Failed: {project_id}")
            
        except Exception as e:
            print(f"    ❌ Error configuring {project_id}: {e}")
            result["errors"].append(f"Configuration error: {e}")
        
        return result
    
    async def _switch_to_project(self, project_id: str) -> bool:
        """Switch Firebase CLI to the specified project."""
        try:
            result = subprocess.run(
                ["firebase", "use", project_id],
                capture_output=True,
                text=True,
                check=True
            )
            return True
        except subprocess.CalledProcessError as e:
            print(f"    ❌ Failed to switch to {project_id}: {e.stderr}")
            return False
    
    async def _check_auth_initialized(self, project_id: str) -> bool:
        """Check if Firebase Auth is initialized for the project."""
        try:
            # Try to get auth configuration
            result = subprocess.run([
                "firebase", "auth:export", "--project", project_id, "/tmp/auth_export.json"
            ], capture_output=True, text=True)
            
            return result.returncode == 0
        except Exception:
            return False
    
    async def _get_current_domains(self, project_id: str) -> List[str]:
        """Get current authorized domains for the project."""
        try:
            # Get access token
            token_result = subprocess.run([
                "gcloud", "auth", "print-access-token"
            ], capture_output=True, text=True, check=True)
            
            access_token = token_result.stdout.strip()
            
            # Get project configuration
            curl_result = subprocess.run([
                "curl", "-s", "-H", f"Authorization: Bearer {access_token}",
                "-H", "Content-Type: application/json",
                f"https://identitytoolkit.googleapis.com/admin/v2/projects/{project_id}/config"
            ], capture_output=True, text=True)
            
            if curl_result.returncode == 0 and curl_result.stdout:
                config = json.loads(curl_result.stdout)
                return config.get("authorizedDomains", [])
            else:
                return []
        except Exception:
            return []
    
    async def _check_google_provider(self, project_id: str) -> bool:
        """Check if Google provider is enabled."""
        try:
            # Get access token
            token_result = subprocess.run([
                "gcloud", "auth", "print-access-token"
            ], capture_output=True, text=True, check=True)
            
            access_token = token_result.stdout.strip()
            
            # Get project configuration
            curl_result = subprocess.run([
                "curl", "-s", "-H", f"Authorization: Bearer {access_token}",
                "-H", "Content-Type: application/json",
                f"https://identitytoolkit.googleapis.com/admin/v2/projects/{project_id}/config"
            ], capture_output=True, text=True)
            
            if curl_result.returncode == 0 and curl_result.stdout:
                config = json.loads(curl_result.stdout)
                sign_in = config.get("signIn", {})
                return sign_in.get("google", {}).get("enabled", False)
            else:
                return False
        except Exception:
            return False
    
    async def _initialize_firebase_auth(self, project_id: str) -> bool:
        """Initialize Firebase Auth for the project."""
        try:
            # Enable Firebase Auth API
            result = subprocess.run([
                "gcloud", "services", "enable", "identitytoolkit.googleapis.com",
                "--project", project_id
            ], capture_output=True, text=True)
            
            return result.returncode == 0
        except Exception:
            return False
    
    async def _enable_google_provider(self, project_id: str) -> bool:
        """Enable Google Sign-In provider."""
        try:
            # Get access token
            token_result = subprocess.run([
                "gcloud", "auth", "print-access-token"
            ], capture_output=True, text=True, check=True)
            
            access_token = token_result.stdout.strip()
            
            # Get current configuration first
            get_result = subprocess.run([
                "curl", "-s", "-H", f"Authorization: Bearer {access_token}",
                "-H", "Content-Type: application/json",
                f"https://identitytoolkit.googleapis.com/admin/v2/projects/{project_id}/config"
            ], capture_output=True, text=True)
            
            if get_result.returncode != 0:
                return False
            
            # Parse current config
            current_config = json.loads(get_result.stdout) if get_result.stdout else {}
            
            # Update configuration to enable Google provider
            updated_config = {
                "authorizedDomains": self.projects[project_id]["domains"],
                "signIn": {
                    "email": {"enabled": True},
                    "google": {"enabled": True}
                }
            }
            
            # Merge with existing config
            if "signIn" in current_config:
                updated_config["signIn"].update(current_config["signIn"])
                updated_config["signIn"]["google"]["enabled"] = True
            
            # Update configuration
            curl_result = subprocess.run([
                "curl", "-s", "-X", "PATCH",
                "-H", f"Authorization: Bearer {access_token}",
                "-H", "Content-Type: application/json",
                "-H", f"X-Goog-User-Project: {project_id}",
                "-d", json.dumps(updated_config),
                f"https://identitytoolkit.googleapis.com/admin/v2/projects/{project_id}/config"
            ], capture_output=True, text=True)
            
            return curl_result.returncode == 0
        except Exception as e:
            print(f"    ❌ Error enabling Google provider: {e}")
            return False
    
    async def _configure_authorized_domains(self, project_id: str, domains: List[str]) -> bool:
        """Configure authorized domains for the project."""
        try:
            # Get access token
            token_result = subprocess.run([
                "gcloud", "auth", "print-access-token"
            ], capture_output=True, text=True, check=True)
            
            access_token = token_result.stdout.strip()
            
            # Get current configuration first
            get_result = subprocess.run([
                "curl", "-s", "-H", f"Authorization: Bearer {access_token}",
                "-H", "Content-Type: application/json",
                f"https://identitytoolkit.googleapis.com/admin/v2/projects/{project_id}/config"
            ], capture_output=True, text=True)
            
            if get_result.returncode != 0:
                return False
            
            # Parse current config
            current_config = json.loads(get_result.stdout) if get_result.stdout else {}
            
            # Update authorized domains
            current_domains = set(current_config.get("authorizedDomains", []))
            new_domains = set(domains)
            all_domains = list(current_domains.union(new_domains))
            
            updated_config = {
                **current_config,
                "authorizedDomains": all_domains
            }
            
            # Update configuration
            curl_result = subprocess.run([
                "curl", "-s", "-X", "PATCH",
                "-H", f"Authorization: Bearer {access_token}",
                "-H", "Content-Type: application/json",
                "-H", f"X-Goog-User-Project: {project_id}",
                "-d", json.dumps(updated_config),
                f"https://identitytoolkit.googleapis.com/admin/v2/projects/{project_id}/config"
            ], capture_output=True, text=True)
            
            return curl_result.returncode == 0
        except Exception as e:
            print(f"    ❌ Error configuring domains: {e}")
            return False
    
    async def _verify_project_configuration(self, project_id: str, expected_domains: List[str]) -> Dict[str, Any]:
        """Verify the project configuration is working."""
        verification = {
            "success": False,
            "errors": [],
            "details": {}
        }
        
        try:
            # Check authorized domains
            current_domains = await self._get_current_domains(project_id)
            verification["details"]["current_domains"] = current_domains
            verification["details"]["expected_domains"] = expected_domains
            
            # Check if all expected domains are present
            missing_domains = [d for d in expected_domains if d not in current_domains]
            
            if missing_domains:
                verification["errors"].append(f"Missing domains: {missing_domains}")
            else:
                verification["success"] = True
                
        except Exception as e:
            verification["errors"].append(f"Verification error: {e}")
        
        return verification
    
    async def _verify_all_configurations(self) -> Dict[str, Any]:
        """Verify all project configurations."""
        verification_results = {
            "timestamp": datetime.now().isoformat(),
            "projects": {},
            "overall_success": False
        }
        
        success_count = 0
        
        for project_id, config in self.projects.items():
            print(f"  🔍 Verifying {project_id}...")
            verification = await self._verify_project_configuration(project_id, config["domains"])
            verification_results["projects"][project_id] = verification
            
            if verification["success"]:
                success_count += 1
                print(f"    ✅ {project_id}: Configuration verified")
            else:
                print(f"    ❌ {project_id}: Verification failed - {verification['errors']}")
        
        verification_results["overall_success"] = success_count == len(self.projects)
        return verification_results
    
    def _print_current_state(self, state: Dict[str, Any]):
        """Print current state in a formatted way."""
        print(f"  📊 Projects Checked: {len(state['projects'])}")
        
        for project_id, project_data in state["projects"].items():
            status_emoji = "✅" if project_data["status"] == "configured" else "❌"
            print(f"    {status_emoji} {project_id}: {project_data['status']}")
            if project_data["current_domains"]:
                print(f"      🌐 Domains: {', '.join(project_data['current_domains'])}")
    
    def _generate_report(self, current_state: Dict[str, Any], verification: Dict[str, Any]) -> Dict[str, Any]:
        """Generate a comprehensive report."""
        report = {
            "configuration_summary": {
                "timestamp": datetime.now().isoformat(),
                "total_projects": len(self.projects),
                "successful_configurations": sum(1 for r in self.results.values() if r["success"]),
                "failed_configurations": sum(1 for r in self.results.values() if not r["success"]),
                "overall_success": verification["overall_success"]
            },
            "project_results": self.results,
            "current_state": current_state,
            "verification": verification,
            "recommendations": self._generate_recommendations()
        }
        
        # Save report to file
        report_file = f"google_auth_configuration_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2, default=str)
        
        print(f"\n📄 Configuration report saved: {report_file}")
        return report
    
    def _generate_recommendations(self) -> List[str]:
        """Generate recommendations based on the configuration results."""
        recommendations = []
        
        successful_count = sum(1 for r in self.results.values() if r["success"])
        total_count = len(self.results)
        
        if successful_count == total_count:
            recommendations.append("🎉 All environments successfully configured with Google Sign-In")
            recommendations.append("✅ All authorized domains properly set")
            recommendations.append("🔒 Google provider enabled across all projects")
            recommendations.append("📊 Consider setting up monitoring for authentication metrics")
        elif successful_count > 0:
            recommendations.append(f"⚠️ {successful_count}/{total_count} environments configured successfully")
            recommendations.append("🔧 Review failed configurations and retry")
            recommendations.append("📋 Check error logs for specific issues")
        else:
            recommendations.append("❌ No environments configured successfully")
            recommendations.append("🔍 Review authentication setup and permissions")
            recommendations.append("🛠️ Consider manual configuration for critical environments")
        
        recommendations.append("📚 Document any custom configurations for team reference")
        recommendations.append("🔄 Set up automated testing for authentication flows")
        
        return recommendations

async def main():
    """Main configuration function."""
    print("🚀 Starting Google Sign-In Authentication Configuration")
    print("Using Direct Firebase CLI and Google Cloud APIs")
    print()
    
    configurator = GoogleAuthConfigurator()
    
    try:
        report = await configurator.configure_all_environments()
        
        print("\n" + "=" * 60)
        print("🎯 CONFIGURATION COMPLETE")
        print("=" * 60)
        
        summary = report["configuration_summary"]
        print(f"📊 Total Projects: {summary['total_projects']}")
        print(f"✅ Successful: {summary['successful_configurations']}")
        print(f"❌ Failed: {summary['failed_configurations']}")
        print(f"🎉 Overall Success: {'Yes' if summary['overall_success'] else 'No'}")
        
        print("\n📋 Recommendations:")
        for rec in report["recommendations"]:
            print(f"  {rec}")
        
        return summary["overall_success"]
        
    except Exception as e:
        print(f"\n❌ Configuration failed: {e}")
        return False

if __name__ == "__main__":
    success = asyncio.run(main())
    sys.exit(0 if success else 1)
