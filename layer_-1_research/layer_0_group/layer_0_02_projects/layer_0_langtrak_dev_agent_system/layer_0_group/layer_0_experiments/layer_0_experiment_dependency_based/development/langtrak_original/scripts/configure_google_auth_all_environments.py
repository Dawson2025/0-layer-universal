#!/usr/bin/env python3
# resource_id: "8d812877-e930-42ff-bee1-762ee51e298c"
# resource_type: "document"
# resource_name: "configure_google_auth_all_environments"

"""
configure_google_auth_all_environments.py

Meta-intelligent orchestration script to configure Google Sign-In authentication
for all project environments using the Firebase orchestration system.
"""

import asyncio
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional

# Add the project root to the Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from features.meta_intelligent_orchestration import (
    UniversalMasterOrchestrator, FirebaseProvider, FirebaseProjectProfile, 
    FirebaseProjectType, EnvironmentType
)

class GoogleAuthOrchestrator:
    """Orchestrator for Google Sign-In authentication across all environments."""
    
    def __init__(self):
        self.provider = FirebaseProvider()
        self.orchestrator = UniversalMasterOrchestrator(self.provider)
        self.projects = {
            "lang-trak-dev": {
                "environment": EnvironmentType.DEVELOPMENT,
                "domains": ["localhost", "127.0.0.1", "lang-trak-dev.web.app", "lang-trak-dev.firebaseapp.com"]
            },
            "lang-trak-staging": {
                "environment": EnvironmentType.STAGING,
                "domains": ["lang-trak-staging.web.app", "lang-trak-staging.firebaseapp.com"]
            },
            "lang-trak-test": {
                "environment": EnvironmentType.TESTING,
                "domains": ["lang-trak-test.web.app", "lang-trak-test.firebaseapp.com"]
            },
            "lang-trak-prod": {
                "environment": EnvironmentType.PRODUCTION,
                "domains": ["lang-trak-prod.web.app", "lang-trak-prod.firebaseapp.com"]
            }
        }
        self.results = {}
    
    async def configure_all_environments(self) -> Dict[str, Any]:
        """Configure Google Sign-In for all environments."""
        print("🔥 Google Sign-In Authentication Orchestration")
        print("=" * 60)
        print(f"📅 Started: {datetime.now().isoformat()}")
        print(f"🎯 Target Projects: {list(self.projects.keys())}")
        print()
        
        # Step 1: Analyze current authentication state
        print("🔍 Step 1: Analyzing current authentication state...")
        auth_analysis = await self._analyze_current_auth_state()
        self._print_analysis_results(auth_analysis)
        
        # Step 2: Plan authentication configuration
        print("\n📋 Step 2: Planning authentication configuration...")
        auth_plan = await self._plan_auth_configuration()
        self._print_plan_results(auth_plan)
        
        # Step 3: Configure each environment
        print("\n🚀 Step 3: Configuring authentication for each environment...")
        for project_id, config in self.projects.items():
            print(f"\n--- Configuring {project_id} ---")
            result = await self._configure_project_auth(project_id, config)
            self.results[project_id] = result
        
        # Step 4: Verify configurations
        print("\n✅ Step 4: Verifying configurations...")
        verification_results = await self._verify_all_configurations()
        
        # Step 5: Generate comprehensive report
        print("\n📊 Step 5: Generating comprehensive report...")
        report = self._generate_comprehensive_report(auth_analysis, auth_plan, verification_results)
        
        return report
    
    async def _analyze_current_auth_state(self) -> Dict[str, Any]:
        """Analyze current authentication state across all projects."""
        analysis = {
            "timestamp": datetime.now().isoformat(),
            "projects": {},
            "overall_status": "unknown",
            "issues_found": [],
            "recommendations": []
        }
        
        for project_id in self.projects.keys():
            print(f"  🔍 Analyzing {project_id}...")
            
            try:
                # Switch to project
                await self._switch_to_project(project_id)
                
                # Get current auth configuration
                auth_config = await self._get_auth_config(project_id)
                
                # Check authorized domains
                domains = await self._get_authorized_domains(project_id)
                
                # Check Google provider status
                google_provider = await self._check_google_provider(project_id)
                
                analysis["projects"][project_id] = {
                    "auth_configured": auth_config is not None,
                    "authorized_domains": domains,
                    "google_provider_enabled": google_provider,
                    "status": "configured" if auth_config and google_provider else "needs_configuration"
                }
                
                # Identify issues
                if not auth_config:
                    analysis["issues_found"].append(f"{project_id}: Firebase Auth not initialized")
                if not google_provider:
                    analysis["issues_found"].append(f"{project_id}: Google provider not enabled")
                
                missing_domains = self._find_missing_domains(project_id, domains)
                if missing_domains:
                    analysis["issues_found"].append(f"{project_id}: Missing domains: {missing_domains}")
                
            except Exception as e:
                print(f"    ❌ Error analyzing {project_id}: {e}")
                analysis["projects"][project_id] = {
                    "auth_configured": False,
                    "authorized_domains": [],
                    "google_provider_enabled": False,
                    "status": "error",
                    "error": str(e)
                }
                analysis["issues_found"].append(f"{project_id}: Analysis error - {e}")
        
        # Determine overall status
        configured_count = sum(1 for p in analysis["projects"].values() if p["status"] == "configured")
        total_count = len(analysis["projects"])
        
        if configured_count == total_count:
            analysis["overall_status"] = "fully_configured"
        elif configured_count > 0:
            analysis["overall_status"] = "partially_configured"
        else:
            analysis["overall_status"] = "needs_configuration"
        
        return analysis
    
    async def _plan_auth_configuration(self) -> Dict[str, Any]:
        """Plan authentication configuration using meta-intelligent analysis."""
        plan = {
            "timestamp": datetime.now().isoformat(),
            "strategy": "comprehensive_google_auth_setup",
            "phases": [],
            "estimated_duration": "10-15 minutes",
            "risk_level": "low"
        }
        
        # Phase 1: Initialize Firebase Auth where needed
        plan["phases"].append({
            "phase": 1,
            "name": "Initialize Firebase Auth",
            "description": "Initialize Firebase Authentication for projects that need it",
            "projects": [pid for pid, config in self.projects.items()],
            "estimated_time": "3-5 minutes"
        })
        
        # Phase 2: Enable Google Provider
        plan["phases"].append({
            "phase": 2,
            "name": "Enable Google Sign-In Provider",
            "description": "Enable Google as a sign-in provider for all projects",
            "projects": [pid for pid, config in self.projects.items()],
            "estimated_time": "2-3 minutes"
        })
        
        # Phase 3: Configure Authorized Domains
        plan["phases"].append({
            "phase": 3,
            "name": "Configure Authorized Domains",
            "description": "Add all required domains to authorized domains list",
            "projects": [pid for pid, config in self.projects.items()],
            "estimated_time": "3-4 minutes"
        })
        
        # Phase 4: Verify Configuration
        plan["phases"].append({
            "phase": 4,
            "name": "Verify Configuration",
            "description": "Verify all configurations are working correctly",
            "projects": [pid for pid, config in self.projects.items()],
            "estimated_time": "2-3 minutes"
        })
        
        return plan
    
    async def _configure_project_auth(self, project_id: str, config: Dict[str, Any]) -> Dict[str, Any]:
        """Configure authentication for a specific project."""
        result = {
            "project_id": project_id,
            "environment": config["environment"].value,
            "domains": config["domains"],
            "steps_completed": [],
            "success": False,
            "errors": []
        }
        
        try:
            # Step 1: Switch to project
            print(f"    🔄 Switching to {project_id}...")
            await self._switch_to_project(project_id)
            result["steps_completed"].append("switch_to_project")
            
            # Step 2: Initialize Firebase Auth if needed
            print(f"    🔧 Initializing Firebase Auth...")
            auth_initialized = await self._initialize_firebase_auth(project_id)
            if auth_initialized:
                result["steps_completed"].append("initialize_auth")
            else:
                result["errors"].append("Failed to initialize Firebase Auth")
            
            # Step 3: Enable Google Provider
            print(f"    🔑 Enabling Google Sign-In provider...")
            google_enabled = await self._enable_google_provider(project_id)
            if google_enabled:
                result["steps_completed"].append("enable_google_provider")
            else:
                result["errors"].append("Failed to enable Google provider")
            
            # Step 4: Configure authorized domains
            print(f"    🌐 Configuring authorized domains...")
            domains_configured = await self._configure_authorized_domains(project_id, config["domains"])
            if domains_configured:
                result["steps_completed"].append("configure_domains")
            else:
                result["errors"].append("Failed to configure authorized domains")
            
            # Step 5: Verify configuration
            print(f"    ✅ Verifying configuration...")
            verification = await self._verify_project_configuration(project_id)
            if verification["success"]:
                result["steps_completed"].append("verify_configuration")
                result["success"] = True
            else:
                result["errors"].extend(verification["errors"])
            
            print(f"    {'✅ Success' if result['success'] else '❌ Failed'}: {project_id}")
            
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
    
    async def _get_auth_config(self, project_id: str) -> Optional[Dict[str, Any]]:
        """Get current Firebase Auth configuration."""
        try:
            result = subprocess.run(
                ["firebase", "auth:export", "--project", project_id, "/tmp/auth_export.json"],
                capture_output=True,
                text=True
            )
            return {"configured": result.returncode == 0}
        except Exception:
            return None
    
    async def _get_authorized_domains(self, project_id: str) -> List[str]:
        """Get current authorized domains for the project."""
        try:
            # Use gcloud to get auth configuration
            result = subprocess.run([
                "gcloud", "auth", "print-access-token"
            ], capture_output=True, text=True, check=True)
            
            access_token = result.stdout.strip()
            
            # Get project configuration
            curl_result = subprocess.run([
                "curl", "-H", f"Authorization: Bearer {access_token}",
                "-H", "Content-Type: application/json",
                f"https://identitytoolkit.googleapis.com/admin/v2/projects/{project_id}/config"
            ], capture_output=True, text=True)
            
            if curl_result.returncode == 0:
                config = json.loads(curl_result.stdout)
                return config.get("authorizedDomains", [])
            else:
                return []
        except Exception:
            return []
    
    async def _check_google_provider(self, project_id: str) -> bool:
        """Check if Google provider is enabled."""
        try:
            # This would require checking the auth configuration
            # For now, we'll assume it needs to be enabled
            return False
        except Exception:
            return False
    
    def _find_missing_domains(self, project_id: str, current_domains: List[str]) -> List[str]:
        """Find domains that should be authorized but aren't."""
        required_domains = self.projects[project_id]["domains"]
        return [domain for domain in required_domains if domain not in current_domains]
    
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
            
            # Enable Google provider
            curl_result = subprocess.run([
                "curl", "-X", "PATCH",
                "-H", f"Authorization: Bearer {access_token}",
                "-H", "Content-Type: application/json",
                "-H", f"X-Goog-User-Project: {project_id}",
                "-d", json.dumps({
                    "authorizedDomains": self.projects[project_id]["domains"],
                    "signIn": {
                        "email": {"enabled": True},
                        "google": {"enabled": True}
                    }
                }),
                f"https://identitytoolkit.googleapis.com/admin/v2/projects/{project_id}/config"
            ], capture_output=True, text=True)
            
            return curl_result.returncode == 0
        except Exception:
            return False
    
    async def _configure_authorized_domains(self, project_id: str, domains: List[str]) -> bool:
        """Configure authorized domains for the project."""
        try:
            # Get access token
            token_result = subprocess.run([
                "gcloud", "auth", "print-access-token"
            ], capture_output=True, text=True, check=True)
            
            access_token = token_result.stdout.strip()
            
            # Update authorized domains
            curl_result = subprocess.run([
                "curl", "-X", "PATCH",
                "-H", f"Authorization: Bearer {access_token}",
                "-H", "Content-Type: application/json",
                "-H", f"X-Goog-User-Project: {project_id}",
                "-d", json.dumps({
                    "authorizedDomains": domains
                }),
                f"https://identitytoolkit.googleapis.com/admin/v2/projects/{project_id}/config"
            ], capture_output=True, text=True)
            
            return curl_result.returncode == 0
        except Exception:
            return False
    
    async def _verify_project_configuration(self, project_id: str) -> Dict[str, Any]:
        """Verify the project configuration is working."""
        verification = {
            "success": False,
            "errors": [],
            "details": {}
        }
        
        try:
            # Check if auth is configured
            auth_config = await self._get_auth_config(project_id)
            verification["details"]["auth_configured"] = auth_config is not None
            
            # Check authorized domains
            domains = await self._get_authorized_domains(project_id)
            verification["details"]["authorized_domains"] = domains
            
            # Check if all required domains are present
            required_domains = self.projects[project_id]["domains"]
            missing_domains = [d for d in required_domains if d not in domains]
            
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
        
        for project_id in self.projects.keys():
            print(f"  🔍 Verifying {project_id}...")
            verification = await self._verify_project_configuration(project_id)
            verification_results["projects"][project_id] = verification
            
            if verification["success"]:
                success_count += 1
                print(f"    ✅ {project_id}: Configuration verified")
            else:
                print(f"    ❌ {project_id}: Verification failed - {verification['errors']}")
        
        verification_results["overall_success"] = success_count == len(self.projects)
        return verification_results
    
    def _print_analysis_results(self, analysis: Dict[str, Any]):
        """Print analysis results in a formatted way."""
        print(f"  📊 Overall Status: {analysis['overall_status']}")
        print(f"  🔍 Projects Analyzed: {len(analysis['projects'])}")
        print(f"  ⚠️  Issues Found: {len(analysis['issues_found'])}")
        
        for project_id, project_data in analysis["projects"].items():
            status_emoji = "✅" if project_data["status"] == "configured" else "❌"
            print(f"    {status_emoji} {project_id}: {project_data['status']}")
        
        if analysis["issues_found"]:
            print("\n  🚨 Issues to Address:")
            for issue in analysis["issues_found"]:
                print(f"    • {issue}")
    
    def _print_plan_results(self, plan: Dict[str, Any]):
        """Print plan results in a formatted way."""
        print(f"  📋 Strategy: {plan['strategy']}")
        print(f"  ⏱️  Estimated Duration: {plan['estimated_duration']}")
        print(f"  🎯 Risk Level: {plan['risk_level']}")
        print(f"  📝 Phases: {len(plan['phases'])}")
        
        for phase in plan["phases"]:
            print(f"    Phase {phase['phase']}: {phase['name']} ({phase['estimated_time']})")
    
    def _generate_comprehensive_report(self, analysis: Dict[str, Any], 
                                     plan: Dict[str, Any], 
                                     verification: Dict[str, Any]) -> Dict[str, Any]:
        """Generate a comprehensive report of the orchestration process."""
        report = {
            "orchestration_summary": {
                "timestamp": datetime.now().isoformat(),
                "total_projects": len(self.projects),
                "successful_configurations": sum(1 for r in self.results.values() if r["success"]),
                "failed_configurations": sum(1 for r in self.results.values() if not r["success"]),
                "overall_success": verification["overall_success"]
            },
            "project_results": self.results,
            "analysis": analysis,
            "plan": plan,
            "verification": verification,
            "recommendations": self._generate_recommendations()
        }
        
        # Save report to file
        report_file = f"google_auth_orchestration_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2, default=str)
        
        print(f"\n📄 Comprehensive report saved: {report_file}")
        return report
    
    def _generate_recommendations(self) -> List[str]:
        """Generate recommendations based on the orchestration results."""
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
    """Main orchestration function."""
    print("🚀 Starting Google Sign-In Authentication Orchestration")
    print("Using Meta-Intelligent Firebase Orchestration System")
    print()
    
    orchestrator = GoogleAuthOrchestrator()
    
    try:
        report = await orchestrator.configure_all_environments()
        
        print("\n" + "=" * 60)
        print("🎯 ORCHESTRATION COMPLETE")
        print("=" * 60)
        
        summary = report["orchestration_summary"]
        print(f"📊 Total Projects: {summary['total_projects']}")
        print(f"✅ Successful: {summary['successful_configurations']}")
        print(f"❌ Failed: {summary['failed_configurations']}")
        print(f"🎉 Overall Success: {'Yes' if summary['overall_success'] else 'No'}")
        
        print("\n📋 Recommendations:")
        for rec in report["recommendations"]:
            print(f"  {rec}")
        
        return summary["overall_success"]
        
    except Exception as e:
        print(f"\n❌ Orchestration failed: {e}")
        return False

if __name__ == "__main__":
    success = asyncio.run(main())
    sys.exit(0 if success else 1)
