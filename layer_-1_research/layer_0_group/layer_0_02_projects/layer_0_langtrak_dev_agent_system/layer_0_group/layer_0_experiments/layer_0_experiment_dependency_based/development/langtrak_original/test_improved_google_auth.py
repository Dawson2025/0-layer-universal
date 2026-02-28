#!/usr/bin/env python3
"""
Test improved Google OAuth authentication with proper dev/prod handling
"""
import requests
import json
import os

def test_google_auth_improved():
    """Test the improved Google auth endpoint"""
    base_url = os.environ.get("APP_BASE_URL", "http://localhost:5000")
    url = f"{base_url}/auth/google"
    
    # Test data with unique user to avoid constraint errors
    test_data = {
        "idToken": "fake_id_token_for_testing_improved",
        "user": {
            "uid": "improved_test_user_456",
            "email": "improved@example.com",
            "displayName": "Improved Test User",
            "photoURL": "https://example.com/photo.jpg"
        }
    }
    
    print("🔍 Testing Improved Google auth endpoint...")
    print(f"URL: {url}")
    print(f"Data: {json.dumps(test_data, indent=2)}")
    
    try:
        response = requests.post(url, json=test_data, timeout=10)
        print(f"\n📊 Response Status: {response.status_code}")
        print(f"📊 Response Headers: {dict(response.headers)}")
        print(f"📊 Response Body: {response.text}")
        
        if response.status_code == 200:
            print("✅ Improved Google auth test PASSED!")
            return True
        else:
            print("❌ Improved Google auth test FAILED!")
            return False
            
    except Exception as e:
        print(f"❌ Error testing improved Google auth: {e}")
        return False

if __name__ == "__main__":
    test_google_auth_improved()
