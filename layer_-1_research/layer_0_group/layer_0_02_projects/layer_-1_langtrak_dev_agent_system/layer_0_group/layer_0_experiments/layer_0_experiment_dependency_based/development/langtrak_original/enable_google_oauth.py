#!/usr/bin/env python3
"""
Enable Google OAuth for Firebase project using Firebase Admin API
"""
import json
import subprocess
import sys

def get_access_token():
    """Get access token for Firebase Admin API"""
    try:
        result = subprocess.run([
            'gcloud', 'auth', 'print-access-token'
        ], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"❌ Error getting access token: {e.stderr}")
        return None

def enable_google_oauth(project_id):
    """Enable Google OAuth for Firebase project"""
    access_token = get_access_token()
    if not access_token:
        return False
    
    print(f"🔑 Enabling Google OAuth for {project_id}...")
    
    # Get current config
    get_url = f"https://identitytoolkit.googleapis.com/admin/v2/projects/{project_id}/config"
    get_command = [
        'curl', '-s', '-X', 'GET', get_url,
        '-H', f'Authorization: Bearer {access_token}',
        '-H', 'X-Goog-User-Project: ' + project_id
    ]
    
    try:
        result = subprocess.run(get_command, capture_output=True, text=True, check=True)
        config = json.loads(result.stdout)
        
        # Enable Google provider
        if 'signIn' not in config:
            config['signIn'] = {}
        
        config['signIn']['google'] = {
            'enabled': True
        }
        
        # Update config
        update_url = f"https://identitytoolkit.googleapis.com/admin/v2/projects/{project_id}/config"
        update_command = [
            'curl', '-s', '-X', 'PATCH', update_url,
            '-H', f'Authorization: Bearer {access_token}',
            '-H', 'X-Goog-User-Project: ' + project_id,
            '-H', 'Content-Type: application/json',
            '-d', json.dumps(config)
        ]
        
        result = subprocess.run(update_command, capture_output=True, text=True, check=True)
        
        if 'error' not in result.stdout:
            print(f"✅ Google OAuth enabled for {project_id}")
            return True
        else:
            print(f"❌ Failed to enable Google OAuth: {result.stdout}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def add_authorized_domains(project_id):
    """Add localhost to authorized domains"""
    access_token = get_access_token()
    if not access_token:
        return False
    
    print(f"🌐 Adding authorized domains for {project_id}...")
    
    # Get current config
    get_url = f"https://identitytoolkit.googleapis.com/admin/v2/projects/{project_id}/config"
    get_command = [
        'curl', '-s', '-X', 'GET', get_url,
        '-H', f'Authorization: Bearer {access_token}',
        '-H', 'X-Goog-User-Project: ' + project_id
    ]
    
    try:
        result = subprocess.run(get_command, capture_output=True, text=True, check=True)
        config = json.loads(result.stdout)
        
        # Add authorized domains
        if 'authorizedDomains' not in config:
            config['authorizedDomains'] = []
        
        domains_to_add = ['localhost', '127.0.0.1', '172.23.194.12']
        for domain in domains_to_add:
            if domain not in config['authorizedDomains']:
                config['authorizedDomains'].append(domain)
                print(f"  ➕ Added domain: {domain}")
        
        # Update config
        update_url = f"https://identitytoolkit.googleapis.com/admin/v2/projects/{project_id}/config"
        update_command = [
            'curl', '-s', '-X', 'PATCH', update_url,
            '-H', f'Authorization: Bearer {access_token}',
            '-H', 'X-Goog-User-Project: ' + project_id,
            '-H', 'Content-Type: application/json',
            '-d', json.dumps(config)
        ]
        
        result = subprocess.run(update_command, capture_output=True, text=True, check=True)
        
        if 'error' not in result.stdout:
            print(f"✅ Authorized domains updated for {project_id}")
            return True
        else:
            print(f"❌ Failed to update domains: {result.stdout}")
            return False
            
    except Exception as e:
        print(f"❌ Error updating domains: {e}")
        return False

def main():
    project_id = "lang-trak-dev"
    
    print("🚀 Enabling Google OAuth for Firebase")
    print("=" * 50)
    
    # Step 1: Enable Google OAuth
    if enable_google_oauth(project_id):
        print("✅ Google OAuth enabled successfully")
    else:
        print("❌ Failed to enable Google OAuth")
        return False
    
    # Step 2: Add authorized domains
    if add_authorized_domains(project_id):
        print("✅ Authorized domains updated successfully")
    else:
        print("❌ Failed to update authorized domains")
        return False
    
    print("\n🎉 Google OAuth setup complete!")
    print("You can now test Google sign-in in your app.")
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
