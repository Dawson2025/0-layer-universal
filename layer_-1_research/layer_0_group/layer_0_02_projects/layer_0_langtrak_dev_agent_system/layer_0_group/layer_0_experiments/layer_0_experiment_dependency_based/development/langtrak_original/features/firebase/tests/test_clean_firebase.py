#!/usr/bin/env python3
"""
Test the clean Firebase setup
"""

def test_firebase_setup():
    print("Testing clean Firebase setup...")
    
    from services.firebase import clean_firebase_service
    
    if clean_firebase_service.is_available():
        print("✅ Firebase service is available")
        
        # Test document creation
        test_id = clean_firebase_service.add_document('test_projects', {
            'name': 'Clean Firebase Test',
            'user_id': 1,
            'test': True
        })
        
        if test_id:
            print(f"✅ Document created successfully: {test_id}")
            print("🎉 Firebase setup is working!")
            return True
        else:
            print("❌ Document creation failed")
            return False
    else:
        print("❌ Firebase service is not available")
        print("Make sure you've placed the service account file in the project directory")
        return False

if __name__ == "__main__":
    test_firebase_setup()