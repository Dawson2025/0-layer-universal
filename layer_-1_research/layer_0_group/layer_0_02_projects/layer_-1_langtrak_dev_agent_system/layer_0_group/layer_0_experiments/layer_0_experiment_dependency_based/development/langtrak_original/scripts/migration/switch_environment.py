#!/usr/bin/env python3
"""
Firebase Environment Switcher
"""
import os
import sys

def switch_environment(env):
    """Switch Firebase environment"""
    if env not in ['development', 'production']:
        print("Error: Environment must be 'development' or 'production'")
        return False
    
    # Set environment variable
    os.environ['FIREBASE_ENV'] = env
    
    # Clear module cache to force reload
    modules_to_clear = [
        'services.firebase.config',
        'services.firebase.firestore',
        'services.firebase',
        'storage_manager',
    ]
    for mod in modules_to_clear:
        if mod in sys.modules:
            del sys.modules[mod]
    
    print(f"✅ Switched to {env} environment")
    
    # Test the connection
    try:
        from services.firebase import clean_firebase_service, firebase_config

        print(f"Project ID: {firebase_config.project_id}")
        
        if clean_firebase_service.is_available():
            print(f"✅ {env.title()} Firebase is ready!")
            return True
        else:
            print(f"❌ {env.title()} Firebase connection failed")
            return False
    except Exception as e:
        print(f"Error testing {env}: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 switch_environment.py [development|production]")
        sys.exit(1)
    
    env = sys.argv[1].lower()
    switch_environment(env)