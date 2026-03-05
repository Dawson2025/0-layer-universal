#!/usr/bin/env python3
# resource_id: "876abc6a-7e75-4258-b314-d66f4b87019d"
# resource_type: "document"
# resource_name: "monitor_api_sync"
"""
API Synchronization Monitor
Monitors the API synchronization status for Google Sign-In providers
"""

import subprocess
import json
import time
import sys
from datetime import datetime

def check_google_provider_status(project_id):
    """Check Google Sign-In provider status for a project"""
    try:
        command = f"curl -s -X GET \"https://identitytoolkit.googleapis.com/admin/v2/projects/{project_id}/config\" -H \"Authorization: Bearer $(gcloud auth print-access-token)\" -H \"X-Goog-User-Project: {project_id}\" -H \"Content-Type: application/json\""
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        config = json.loads(result.stdout)
        
        if "signIn" in config and "enabledProviders" in config["signIn"]:
            if "GOOGLE" in config["signIn"]["enabledProviders"]:
                return True
        return False
    except Exception as e:
        print(f"Error checking {project_id}: {e}")
        return False

def monitor_api_sync():
    """Monitor API synchronization status"""
    projects = {
        "dev": "lang-trak-dev",
        "staging": "lang-trak-staging",
        "test": "lang-trak-test",
        "prod": "lang-trak-prod"
    }
    
    print("🔍 Monitoring API Synchronization Status")
    print("=" * 50)
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("Press Ctrl+C to stop monitoring")
    print()
    
    check_count = 0
    all_synced = False
    
    while not all_synced:
        check_count += 1
        timestamp = datetime.now().strftime('%H:%M:%S')
        
        print(f"[{timestamp}] Check #{check_count}")
        
        synced_projects = 0
        total_projects = len(projects)
        
        for env, project_id in projects.items():
            status = check_google_provider_status(project_id)
            if status:
                print(f"  ✅ {env.upper()}: Google Sign-In ENABLED")
                synced_projects += 1
            else:
                print(f"  ❌ {env.upper()}: Google Sign-In DISABLED")
        
        print(f"  📊 Status: {synced_projects}/{total_projects} projects synced")
        
        if synced_projects == total_projects:
            all_synced = True
            print(f"\n🎉 All projects synced! Total checks: {check_count}")
            break
        
        print(f"  ⏳ Waiting 30 seconds before next check...")
        print()
        time.sleep(30)
    
    return check_count

if __name__ == "__main__":
    try:
        total_checks = monitor_api_sync()
        print(f"\n✅ Monitoring completed after {total_checks} checks")
    except KeyboardInterrupt:
        print(f"\n⏹️  Monitoring stopped by user")
    except Exception as e:
        print(f"\n❌ Error during monitoring: {e}")
