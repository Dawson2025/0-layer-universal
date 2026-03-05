#!/usr/bin/env python3
# resource_id: "adab5996-3eb4-4ef1-ba19-c1793d39aafc"
# resource_type: "document"
# resource_name: "test_google_auth"
"""
Test Google OAuth authentication flow
"""
import requests
import json
import os

def test_google_auth():
    """Test the Google auth endpoint"""
    base_url = os.environ.get("APP_BASE_URL", "http://localhost:5000")
    url = f"{base_url}/auth/google"
    
    # Test data that simulates what Firebase would send
    test_data = {
        "idToken": "fake_id_token_for_testing",
        "user": {
            "uid": "test_user_123",
            "email": "test@example.com",
            "displayName": "Test User",
            "photoURL": "https://example.com/photo.jpg"
        }
    }
    
    print("🔍 Testing Google auth endpoint...")
    print(f"URL: {url}")
    print(f"Data: {json.dumps(test_data, indent=2)}")
    
    try:
        response = requests.post(url, json=test_data, timeout=10)
        print(f"\n📊 Response Status: {response.status_code}")
        print(f"📊 Response Headers: {dict(response.headers)}")
        print(f"📊 Response Body: {response.text}")
        
        if response.status_code == 200:
            print("✅ Google auth test PASSED!")
            return True
        else:
            print("❌ Google auth test FAILED!")
            return False
            
    except Exception as e:
        print(f"❌ Error testing Google auth: {e}")
        return False

if __name__ == "__main__":
    test_google_auth()
