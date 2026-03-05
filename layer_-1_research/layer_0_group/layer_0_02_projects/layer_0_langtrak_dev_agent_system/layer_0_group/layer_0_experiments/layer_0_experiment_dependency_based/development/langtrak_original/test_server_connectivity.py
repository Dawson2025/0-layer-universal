#!/usr/bin/env python3
# resource_id: "522e578e-544b-4b72-8b86-4e8e54c65e03"
# resource_type: "document"
# resource_name: "test_server_connectivity"
"""
Test script to verify server connectivity check functionality.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts', 'automation'))

from run_user_stories_with_server_check import check_server_connectivity, wait_for_server

def test_server_connectivity():
    print("🧪 Testing server connectivity check...")
    
    # Test 1: Check current server
    print("\n1. Testing current server connectivity...")
    if check_server_connectivity():
        print("✅ Server is accessible")
    else:
        print("❌ Server is not accessible")
    
    # Test 2: Test with invalid URL
    print("\n2. Testing with invalid URL...")
    if check_server_connectivity("http://127.0.0.1:9999"):
        print("❌ Should not be accessible")
    else:
        print("✅ Correctly identified as not accessible")
    
    # Test 3: Test wait functionality (with short timeout)
    print("\n3. Testing wait functionality...")
    if wait_for_server(max_attempts=2, delay=1):
        print("✅ Server became available")
    else:
        print("❌ Server did not become available")

if __name__ == "__main__":
    test_server_connectivity()
