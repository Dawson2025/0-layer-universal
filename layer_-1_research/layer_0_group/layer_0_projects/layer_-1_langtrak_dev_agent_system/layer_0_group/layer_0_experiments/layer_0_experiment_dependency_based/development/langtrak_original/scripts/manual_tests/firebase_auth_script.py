#!/usr/bin/env python3
"""
Test Firebase Admin SDK authentication
"""
import sys
import os

# Add the project root to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from firebase_admin import auth as firebase_auth
    print("✅ Firebase Admin SDK imported successfully")
    
    # Test if Firebase is initialized
    try:
        # This will raise an exception if Firebase is not initialized
        firebase_auth.list_users(max_results=1)
        print("✅ Firebase Admin SDK is properly initialized")
    except Exception as e:
        print(f"❌ Firebase Admin SDK not initialized: {e}")
        
except ImportError as e:
    print(f"❌ Failed to import Firebase Admin SDK: {e}")

# Test the Google auth endpoint
import requests

print("\n🔍 Testing Google auth endpoint...")
response = requests.post(f'{os.environ.get("APP_BASE_URL", "http://localhost:5000")}/auth/google',
                        json={
                            'idToken': 'fake_token',
                            'user': {
                                'uid': 'test123',
                                'email': 'test@example.com',
                                'displayName': 'Test User'
                            }
                        })

print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")
