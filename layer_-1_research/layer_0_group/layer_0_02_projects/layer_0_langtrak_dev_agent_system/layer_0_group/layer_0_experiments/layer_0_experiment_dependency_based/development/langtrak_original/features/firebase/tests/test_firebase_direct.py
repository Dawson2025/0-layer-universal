#!/usr/bin/env python3
# resource_id: "725b9175-e041-4cd6-93bb-ec8f90112023"
# resource_type: "document"
# resource_name: "test_firebase_direct"
"""
Direct Firebase test with nam7 region
"""
import os
import json
from google.cloud import firestore

# Set up authentication
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/runner/workspace/firebase-service-account.json'

try:
    print("Testing direct Firestore connection for nam7 region...")
    
    # Create Firestore client with explicit project
    client = firestore.Client(project='lang-trak')
    
    print("✅ Client created successfully")
    
    # Test write operation
    doc_ref = client.collection('test_nam7').document('test_doc')
    doc_ref.set({
        'region': 'nam7',
        'test': True,
        'message': 'Direct connection test',
        'timestamp': firestore.SERVER_TIMESTAMP
    })
    
    print("✅ Write operation successful!")
    
    # Test read operation
    doc = doc_ref.get()
    if doc.exists:
        print(f"✅ Read operation successful: {doc.to_dict()}")
        
        # Clean up
        doc_ref.delete()
        print("✅ Cleanup completed")
        
        print("🎉 Firebase connection is working!")
    else:
        print("❌ Document was not found after write")
        
except Exception as e:
    print(f"❌ Error: {e}")
    print("The error suggests there might still be an issue with database setup")