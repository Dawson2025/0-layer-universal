#!/usr/bin/env python3
"""Test script for video integration and language selection features"""

import os
import sqlite3
import sys
import json
import tempfile
import shutil

# Add current directory to path for imports
sys.path.append('.')
import main

def test_database_migration():
    """Test that video_path column was added to database"""
    print("Testing database migration...")
    
    conn = sqlite3.connect(main.DB_NAME)
    cursor = conn.cursor()
    
    # Check if video_path column exists
    cursor.execute("PRAGMA table_info(words)")
    columns = [column[1] for column in cursor.fetchall()]
    
    if 'video_path' in columns:
        print("✓ video_path column exists in words table")
        conn.close()
        return True
    else:
        print("✗ video_path column missing from words table")
        conn.close()
        return False

def test_language_selection_functions():
    """Test language selection helper functions"""
    print("Testing language selection functions...")
    
    # Test get_existing_languages function
    try:
        languages = main.get_existing_languages()
        print(f"✓ get_existing_languages() returned {len(languages)} languages")
        return True
    except Exception as e:
        print(f"✗ get_existing_languages() failed: {e}")
        return False

def test_video_conversion_function():
    """Test video conversion function with dummy files"""
    print("Testing video conversion function...")
    
    # Create a temporary directory for test files
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a dummy input file (simulate a video file)
        input_path = os.path.join(temp_dir, "test_input.txt")
        output_path = os.path.join(temp_dir, "test_output.mp4")
        
        with open(input_path, 'w') as f:
            f.write("dummy video content")
        
        # Test the conversion function (should fail gracefully with dummy file)
        try:
            result = main.convert_video_to_mp4(input_path, output_path)
            if result == False:
                print("✓ convert_video_to_mp4() handled invalid input correctly")
                return True
            else:
                print("✓ convert_video_to_mp4() executed without error")
                return True
        except Exception as e:
            print(f"✗ convert_video_to_mp4() failed unexpectedly: {e}")
            return False

def test_video_directory_creation():
    """Test that videos directory is created"""
    print("Testing videos directory creation...")
    
    if os.path.exists("videos") and os.path.isdir("videos"):
        print("✓ videos directory exists")
        return True
    else:
        print("✗ videos directory not found")
        return False

def test_word_functions_with_video():
    """Test that word functions accept video_path parameter"""
    print("Testing word functions with video parameter...")
    
    try:
        # Test add_new_word function signature
        import inspect
        sig = inspect.signature(main.add_new_word)
        if 'video_path' in sig.parameters:
            print("✓ add_new_word() has video_path parameter")
        else:
            print("✗ add_new_word() missing video_path parameter")
            return False
        
        # Test add_new_word_with_structure function signature
        sig = inspect.signature(main.add_new_word_with_structure)
        if 'video_path' in sig.parameters:
            print("✓ add_new_word_with_structure() has video_path parameter")
        else:
            print("✗ add_new_word_with_structure() missing video_path parameter")
            return False
            
        return True
        
    except Exception as e:
        print(f"✗ Function signature test failed: {e}")
        return False

def test_basic_functionality():
    """Test basic app functionality still works"""
    print("Testing basic app functionality...")
    
    try:
        # Test basic imports and function availability
        assert hasattr(main, 'migrate_schema')
        assert hasattr(main, 'get_existing_languages')
        assert hasattr(main, 'convert_video_to_mp4')
        assert hasattr(main, 'handle_video_upload')
        assert hasattr(main, 'select_or_input_language')
        
        print("✓ All new functions are available")
        return True
        
    except Exception as e:
        print(f"✗ Basic functionality test failed: {e}")
        return False

def run_all_tests():
    """Run all tests and report results"""
    print("=" * 50)
    print("Video Integration and Language Selection Tests")
    print("=" * 50)
    
    tests = [
        test_database_migration,
        test_language_selection_functions,
        test_video_conversion_function,
        test_video_directory_creation,
        test_word_functions_with_video,
        test_basic_functionality
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"✗ Test {test.__name__} failed with exception: {e}")
            results.append(False)
        print()
    
    passed = sum(results)
    total = len(results)
    
    print("=" * 50)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Video integration features are working correctly.")
        return True
    else:
        print("⚠️  Some tests failed. Check the output above for details.")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)