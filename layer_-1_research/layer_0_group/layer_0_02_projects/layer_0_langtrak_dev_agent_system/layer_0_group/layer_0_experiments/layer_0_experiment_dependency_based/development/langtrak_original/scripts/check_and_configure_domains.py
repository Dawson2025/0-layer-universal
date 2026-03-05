#!/usr/bin/env python3
# resource_id: "77958849-70bc-417b-92ca-4a762a74c0eb"
# resource_type: "document"
# resource_name: "check_and_configure_domains"

"""
check_and_configure_domains.py

Check current authorized domains and configure them for all environments.
"""

import json
import subprocess
import sys

def get_access_token():
    """Get access token from gcloud."""
    try:
        result = subprocess.run(['gcloud', 'auth', 'print-access-token'], 
                              capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None

def get_current_domains(project_id, access_token):
    """Get current authorized domains for a project."""
    try:
        curl_result = subprocess.run([
            'curl', '-s', '-H', f'Authorization: Bearer {access_token}',
            '-H', 'Content-Type: application/json',
            f'https://identitytoolkit.googleapis.com/admin/v2/projects/{project_id}/config'
        ], capture_output=True, text=True)
        
        if curl_result.returncode == 0 and curl_result.stdout:
            config = json.loads(curl_result.stdout)
            return config.get('authorizedDomains', [])
        return []
    except Exception:
        return []

def configure_domains(project_id, domains, access_token):
    """Configure authorized domains for a project."""
    try:
        # Get current config first
        get_result = subprocess.run([
            'curl', '-s', '-H', f'Authorization: Bearer {access_token}',
            '-H', 'Content-Type: application/json',
            f'https://identitytoolkit.googleapis.com/admin/v2/projects/{project_id}/config'
        ], capture_output=True, text=True)
        
        if get_result.returncode != 0:
            return False
        
        current_config = json.loads(get_result.stdout) if get_result.stdout else {}
        
        # Update authorized domains
        current_domains = set(current_config.get('authorizedDomains', []))
        new_domains = set(domains)
        all_domains = list(current_domains.union(new_domains))
        
        updated_config = {
            **current_config,
            'authorizedDomains': all_domains
        }
        
        # Update configuration
        curl_result = subprocess.run([
            'curl', '-s', '-X', 'PATCH',
            '-H', f'Authorization: Bearer {access_token}',
            '-H', 'Content-Type: application/json',
            '-H', f'X-Goog-User-Project: {project_id}',
            '-d', json.dumps(updated_config),
            f'https://identitytoolkit.googleapis.com/admin/v2/projects/{project_id}/config'
        ], capture_output=True, text=True)
        
        return curl_result.returncode == 0
    except Exception as e:
        print(f"Error configuring domains: {e}")
        return False

def main():
    """Main function."""
    print("🔥 Checking and Configuring Authorized Domains")
    print("=" * 50)
    
    # Get access token
    access_token = get_access_token()
    if not access_token:
        print("❌ Failed to get access token")
        return False
    
    print("✅ Got access token")
    
    # Environment configurations
    environments = {
        "lang-trak-dev": ["localhost", "127.0.0.1", "lang-trak-dev.web.app", "lang-trak-dev.firebaseapp.com"],
        "lang-trak-staging": ["lang-trak-staging.web.app", "lang-trak-staging.firebaseapp.com"],
        "lang-trak-test": ["lang-trak-test.web.app", "lang-trak-test.firebaseapp.com"],
        "lang-trak-prod": ["lang-trak-prod.web.app", "lang-trak-prod.firebaseapp.com"]
    }
    
    results = {}
    
    for project_id, required_domains in environments.items():
        print(f"\n--- {project_id} ---")
        
        # Get current domains
        current_domains = get_current_domains(project_id, access_token)
        print(f"Current domains: {current_domains}")
        print(f"Required domains: {required_domains}")
        
        # Check if all required domains are present
        missing_domains = [d for d in required_domains if d not in current_domains]
        
        if not missing_domains:
            print("✅ All required domains already authorized")
            results[project_id] = {"success": True, "action": "no_change_needed"}
        else:
            print(f"⚠️ Missing domains: {missing_domains}")
            print("🔧 Configuring domains...")
            
            if configure_domains(project_id, required_domains, access_token):
                print("✅ Domains configured successfully")
                results[project_id] = {"success": True, "action": "configured"}
            else:
                print("❌ Failed to configure domains")
                results[project_id] = {"success": False, "action": "failed"}
    
    # Summary
    print(f"\n{'='*50}")
    print("SUMMARY")
    print('='*50)
    
    successful = sum(1 for r in results.values() if r["success"])
    total = len(results)
    
    for project_id, result in results.items():
        status = "✅" if result["success"] else "❌"
        print(f"{status} {project_id}: {result['action']}")
    
    print(f"\n📊 {successful}/{total} projects configured successfully")
    
    if successful == total:
        print("🎉 All environments are ready for Google Sign-In!")
        return True
    else:
        print("⚠️ Some environments need manual configuration")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
