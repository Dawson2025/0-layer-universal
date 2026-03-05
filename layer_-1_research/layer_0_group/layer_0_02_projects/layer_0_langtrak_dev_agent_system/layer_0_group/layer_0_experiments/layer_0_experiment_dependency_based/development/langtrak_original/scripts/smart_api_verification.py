#!/usr/bin/env python3
# resource_id: "811889ff-2658-4ff4-b318-412a5919927c"
# resource_type: "document"
# resource_name: "smart_api_verification"
"""
Smart API Verification System
Checks if enough time has passed since last check and verifies API sync status
"""

import subprocess
import json
import time
import sys
from datetime import datetime, timedelta
from pathlib import Path

def get_last_check_time():
    """Get the last check time from the API sync tracker"""
    tracker_path = (
        Path(__file__).parent.parent
        / "docs/0_context/layer_1_project/1.02_sub_layers/sub_layer_1.11_project_tools/api-sync-tracker.md"
    )
    
    try:
        with open(tracker_path, 'r') as f:
            content = f.read()
        
        # Extract last check time from the document
        date_str = None
        time_str = None
        
        for line in content.split('\n'):
            if 'Last Check Information' in line:
                continue
            if 'Date:' in line:
                date_str = line.split('Date:')[1].strip()
            elif 'Time:' in line:
                time_str = line.split('Time:')[1].strip()
                break
        
        if not date_str or not time_str:
            return None
        
        # Parse the datetime
        datetime_str = f"{date_str} {time_str}"
        last_check = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S UTC-6")
        return last_check
    except Exception as e:
        print(f"Error reading last check time: {e}")
        return None

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

def update_tracker_document(current_time, status, synced_projects, total_projects):
    """Update the API sync tracker document with new status"""
    tracker_path = (
        Path(__file__).parent.parent
        / "docs/0_context/layer_1_project/1.02_sub_layers/sub_layer_1.11_project_tools/api-sync-tracker.md"
    )
    
    try:
        with open(tracker_path, 'r') as f:
            content = f.read()
        
        # Update the last check information
        content = content.replace(
            "**Date**: 2025-01-19",
            f"**Date**: {current_time.strftime('%Y-%m-%d')}"
        )
        content = content.replace(
            "**Time**: 20:25:00 UTC-6",
            f"**Time**: {current_time.strftime('%H:%M:%S')} UTC-6"
        )
        
        # Update status
        if synced_projects == total_projects:
            content = content.replace(
                "**Status**: API discrepancy detected",
                "**Status**: API SYNC COMPLETE"
            )
            content = content.replace(
                "⏳ **Identity Toolkit API**: PENDING SYNC (discrepancy detected)",
                "✅ **Identity Toolkit API**: SYNCED (Google Sign-In ENABLED)"
            )
        else:
            content = content.replace(
                "**Status**: API discrepancy detected",
                f"**Status**: API discrepancy detected ({synced_projects}/{total_projects} synced)"
            )
        
        # Update last updated timestamp
        content = content.replace(
            "**Last Updated**: 2025-01-19 20:25:00 UTC-6",
            f"**Last Updated**: {current_time.strftime('%Y-%m-%d %H:%M:%S')} UTC-6"
        )
        
        # Calculate next check time (15 minutes from now)
        next_check = current_time + timedelta(minutes=15)
        content = content.replace(
            "**Next Check**: 2025-01-19 20:40:00 UTC-6 (15 minutes from last check)",
            f"**Next Check**: {next_check.strftime('%Y-%m-%d %H:%M:%S')} UTC-6 (15 minutes from last check)"
        )
        
        with open(tracker_path, 'w') as f:
            f.write(content)
        
        print(f"✅ Updated API sync tracker document")
        
    except Exception as e:
        print(f"Error updating tracker document: {e}")

def main():
    """Main function to check if it's time to verify and run verification"""
    print("🔍 Smart API Verification System")
    print("=" * 50)
    
    current_time = datetime.now()
    print(f"Current time: {current_time.strftime('%Y-%m-%d %H:%M:%S')} UTC-6")
    
    # Get last check time
    last_check = get_last_check_time()
    minutes_passed = 0  # Initialize variable
    
    if not last_check:
        print("❌ Could not determine last check time. Running verification anyway...")
    else:
        print(f"Last check time: {last_check.strftime('%Y-%m-%d %H:%M:%S')} UTC-6")
        
        # Calculate time difference
        time_diff = current_time - last_check
        minutes_passed = time_diff.total_seconds() / 60
        
        print(f"Time since last check: {minutes_passed:.1f} minutes")
        
        # Check if enough time has passed (15 minutes minimum)
        if minutes_passed < 15:
            print(f"⏳ Not enough time has passed. Expected 15+ minutes, got {minutes_passed:.1f}")
            print("💡 Recommendation: Wait and check again later")
            return
    
    print("\n🔍 Running API verification...")
    
    # Check all projects
    projects = {
        "dev": "lang-trak-dev",
        "staging": "lang-trak-staging",
        "test": "lang-trak-test",
        "prod": "lang-trak-prod"
    }
    
    synced_projects = 0
    total_projects = len(projects)
    
    for env, project_id in projects.items():
        status = check_google_provider_status(project_id)
        if status:
            print(f"✅ {env.upper()}: Google Sign-In ENABLED")
            synced_projects += 1
        else:
            print(f"❌ {env.upper()}: Google Sign-In DISABLED")
    
    print(f"\n📊 Results: {synced_projects}/{total_projects} projects synced")
    
    # Update tracker document
    update_tracker_document(current_time, "checked", synced_projects, total_projects)
    
    if synced_projects == total_projects:
        print("🎉 All projects are now synced! Google Sign-In is fully enabled.")
        print("\n✅ Next steps:")
        print("1. Test authentication flow: python3 scripts/test_auth_flow.py")
        print("2. Update project documentation")
    else:
        print("⚠️  Some projects still not synced. API may need more time.")
        print(f"\n💡 Recommendation: Check again in 15-30 minutes")
        
        if minutes_passed > 60:  # If more than 1 hour has passed
            print("\n🚨 ALERT: More than 1 hour has passed without sync!")
            print("🔧 Consider investigating and fixing manually:")
            print("1. Check Firebase Console for errors")
            print("2. Verify OAuth consent screen configuration")
            print("3. Check Google Cloud Console project status")

if __name__ == "__main__":
    main()
