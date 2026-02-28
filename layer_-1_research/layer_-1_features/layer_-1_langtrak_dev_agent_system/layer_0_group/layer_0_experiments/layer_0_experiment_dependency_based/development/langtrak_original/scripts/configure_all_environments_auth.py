#!/usr/bin/env python3

"""
configure_all_environments_auth.py

Configure Google Sign-In authentication for all project environments.
Uses the existing configure-auth-domains.py script for each environment.
"""

import subprocess
import sys
from datetime import datetime

def main():
    """Configure authentication for all environments."""
    print("🔥 Google Sign-In Authentication Configuration for All Environments")
    print("=" * 70)
    print(f"📅 Started: {datetime.now().isoformat()}")
    print()
    
    # Environment configurations
    environments = {
        "lang-trak-dev": {
            "domains": ["localhost", "127.0.0.1", "lang-trak-dev.web.app", "lang-trak-dev.firebaseapp.com"],
            "description": "Development Environment"
        },
        "lang-trak-staging": {
            "domains": ["lang-trak-staging.web.app", "lang-trak-staging.firebaseapp.com"],
            "description": "Staging Environment"
        },
        "lang-trak-test": {
            "domains": ["lang-trak-test.web.app", "lang-trak-test.firebaseapp.com"],
            "description": "Testing Environment"
        },
        "lang-trak-prod": {
            "domains": ["lang-trak-prod.web.app", "lang-trak-prod.firebaseapp.com"],
            "description": "Production Environment"
        }
    }
    
    results = {}
    
    # Configure each environment
    for project_id, config in environments.items():
        print(f"\n{'='*50}")
        print(f"🔧 Configuring {config['description']}")
        print(f"📋 Project: {project_id}")
        print(f"🌐 Domains: {', '.join(config['domains'])}")
        print('='*50)
        
        try:
            # Build command for configure-auth-domains.py
            cmd = [
                "python3", "scripts/configure-auth-domains.py",
                "--projects", project_id
            ]
            
            # Add domains
            for domain in config['domains']:
                cmd.extend(["--domains", domain])
            
            print(f"▶ Running: {' '.join(cmd)}")
            
            # Run the configuration
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                print("✅ Configuration successful!")
                results[project_id] = {
                    "success": True,
                    "output": result.stdout,
                    "error": None
                }
            else:
                print(f"❌ Configuration failed!")
                print(f"Error: {result.stderr}")
                results[project_id] = {
                    "success": False,
                    "output": result.stdout,
                    "error": result.stderr
                }
                
        except Exception as e:
            print(f"❌ Exception occurred: {e}")
            results[project_id] = {
                "success": False,
                "output": None,
                "error": str(e)
            }
    
    # Summary
    print(f"\n{'='*70}")
    print("🎯 CONFIGURATION SUMMARY")
    print('='*70)
    
    successful = sum(1 for r in results.values() if r["success"])
    total = len(results)
    
    print(f"📊 Total Environments: {total}")
    print(f"✅ Successful: {successful}")
    print(f"❌ Failed: {total - successful}")
    print(f"🎉 Overall Success: {'Yes' if successful == total else 'No'}")
    
    print("\n📋 Detailed Results:")
    for project_id, result in results.items():
        status = "✅" if result["success"] else "❌"
        print(f"  {status} {project_id}: {'Success' if result['success'] else 'Failed'}")
        if not result["success"] and result["error"]:
            print(f"      Error: {result['error'][:100]}...")
    
    if successful == total:
        print("\n🎉 All environments are now configured with Google Sign-In!")
        print("🔒 Authorized domains are properly set for all projects")
        print("📊 You can now use Google Sign-In across all environments")
    else:
        print(f"\n⚠️ {total - successful} environments failed to configure")
        print("🔧 Please check the error messages above and retry if needed")
    
    return successful == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
