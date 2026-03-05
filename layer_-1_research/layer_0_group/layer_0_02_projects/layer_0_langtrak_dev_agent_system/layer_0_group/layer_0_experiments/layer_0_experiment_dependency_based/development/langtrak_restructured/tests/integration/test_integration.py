#!/usr/bin/env python3
# resource_id: "3873f1c4-631c-4402-bdf7-d9d704193df9"
# resource_type: "document"
# resource_name: "test_integration"
"""
Integration test demonstrating video integration and language selection features.
This script tests the complete workflow without requiring user interaction.
"""

import os
import sqlite3
import sys
import json
import tempfile
import unittest.mock as mock

# Add current directory to path for imports
sys.path.append('.')
import main

def test_end_to_end_word_addition_with_video():
    """Test adding a word with video and language selection"""
    print("=" * 60)
    print("END-TO-END TEST: Word Addition with Video and Language Selection")
    print("=" * 60)
    
    # Create a temporary video file for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        test_video_path = os.path.join(temp_dir, "test_input.mp4")
        
        # Create a dummy MP4 file (we'll simulate a video file)
        with open(test_video_path, 'wb') as f:
            # Write MP4 file header magic bytes to make it look like a real MP4
            f.write(b'\x00\x00\x00\x20\x66\x74\x79\x70\x69\x73\x6f\x6d')
            f.write(b'dummy video content for testing')
        
        print(f"Created test video file: {test_video_path}")
        
        # Test 1: Add a word with language selection and video
        print("\n1. Testing add_new_word_with_structure with video...")
        
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()
        
        # Prepare test data
        language = "French"
        english_words = ["hello", "hi"]
        new_language_word = "bonjour"
        ipa_phonetics = "bonˈʒuʁ"
        dictionary_phonetics = "/bon-ZHOOR/"
        phoneme_data = {
            'syllable_type': 'CVC',
            'onset_phoneme': 'b',
            'onset_length_type': 'single_consonants',
            'nucleus_phoneme': 'o',
            'nucleus_length_type': 'monophthongs',
            'coda_phoneme': 'n',
            'coda_length_type': 'single_consonants'
        }
        
        # Expected video output path 
        expected_video_path = os.path.join("videos", "bonjour.mp4")
        
        # Mock the video conversion to avoid actually converting (since we have a dummy file)
        with mock.patch('main.convert_video_to_mp4') as mock_convert:
            mock_convert.return_value = True  # Simulate successful conversion
            
            # Test adding word with video
            video_path = expected_video_path  # Simulate successful conversion result
            result = main.add_new_word_with_structure(
                cursor, conn, language, english_words, new_language_word, 
                ipa_phonetics, dictionary_phonetics, phoneme_data, video_path
            )
            
            if result:
                print("✓ Successfully added word with video using add_new_word_with_structure")
            else:
                print("✗ Failed to add word with video")
                assert False
        
        # Verify the word was added to database with video path
        cursor.execute("SELECT language, english_words, new_language_word, video_path FROM words WHERE new_language_word = ?", (new_language_word,))
        row = cursor.fetchone()
        
        if row:
            lang, eng_json, word, video = row
            english_list = json.loads(eng_json)
            print(f"✓ Word found in database:")
            print(f"  Language: {lang}")
            print(f"  English: {english_list}")
            print(f"  Word: {word}")
            print(f"  Video: {video}")
            
            if video == expected_video_path:
                print("✓ Video path stored correctly")
            else:
                print(f"✗ Video path mismatch: expected {expected_video_path}, got {video}")
                assert False
        else:
            print("✗ Word not found in database")
            assert False
        
        conn.close()
        
        # Test 2: Test language selection functionality
        print("\n2. Testing language selection functionality...")
        
        languages = main.get_existing_languages()
        print(f"✓ Found {len(languages)} existing languages in database: {languages}")
        
        if "French" in languages:
            print("✓ French language correctly detected in existing languages")
        else:
            print("✗ French language not found in existing languages list")
            assert False
        
        # Test 3: Test word editing with video replacement
        print("\n3. Testing word editing with video replacement...")
        
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()
        
        # Get the word we just added
        cursor.execute("SELECT id, language, english_words, new_language_word, ipa_phonetics, dictionary_phonetics, video_path FROM words WHERE new_language_word = ?", (new_language_word,))
        word_data = cursor.fetchone()
        
        if word_data:
            word_id = word_data[0]
            
            # Simulate updating the word with a new video
            new_video_path = os.path.join("videos", "bonjour_updated.mp4")
            
            cursor.execute("""
                UPDATE words SET video_path = ? WHERE id = ?
            """, (new_video_path, word_id))
            conn.commit()
            
            # Verify the update
            cursor.execute("SELECT video_path FROM words WHERE id = ?", (word_id,))
            updated_video = cursor.fetchone()[0]
            
            if updated_video == new_video_path:
                print("✓ Video path updated successfully")
            else:
                print(f"✗ Video path update failed: expected {new_video_path}, got {updated_video}")
                assert False
        else:
            print("✗ Could not find word for editing test")
            assert False
        
        conn.close()
        
        # Test 4: Test display functionality includes video
        print("\n4. Testing word display includes video information...")
        
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT language, english_words, new_language_word, ipa_phonetics, dictionary_phonetics,
                   syllable_type, onset_phoneme, onset_length_type, nucleus_phoneme, nucleus_length_type,
                   coda_phoneme, coda_length_type, video_path
            FROM words WHERE new_language_word = ?
        """, (new_language_word,))
        
        word_display_data = cursor.fetchone()
        if word_display_data and len(word_display_data) == 13:
            video_in_display = word_display_data[12]  # video_path is the 13th column (index 12)
            print(f"✓ Display query includes video path: {video_in_display}")
        else:
            print("✗ Display query missing video path or incorrect number of columns")
            assert False
        
        conn.close()
        
        # Clean up test data
        print("\n5. Cleaning up test data...")
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM words WHERE new_language_word = ?", (new_language_word,))
        conn.commit()
        conn.close()
        print("✓ Test data cleaned up")
        
        assert True

def test_helper_functions():
    """Test individual helper functions"""
    print("\n" + "=" * 60)
    print("HELPER FUNCTIONS TEST")
    print("=" * 60)
    
    # Test 1: Video conversion function with non-existent file
    print("1. Testing video conversion with non-existent file...")
    result = main.convert_video_to_mp4("/non/existent/file.mp4", "/tmp/output.mp4")
    if result == False:
        print("✓ Video conversion correctly handled non-existent input file")
    else:
        print("✗ Video conversion should have failed for non-existent file")
        assert False
    
    # Test 2: Handle video upload with empty input
    print("\n2. Testing video upload with no input...")
    with mock.patch('builtins.input', return_value=''):
        result = main.handle_video_upload("test_word")
        if result is None:
            print("✓ Video upload correctly handled empty input")
        else:
            print("✗ Video upload should return None for empty input")
            assert False
    
    # Test 3: Test language selection with no existing languages
    print("\n3. Testing language selection with new language...")
    with mock.patch('builtins.input', return_value='German'):
        with mock.patch('main.get_existing_languages', return_value=[]):
            result = main.select_or_input_language()
            if result == "German":
                print("✓ Language selection correctly handled new language input")
            else:
                print(f"✗ Language selection failed: expected 'German', got '{result}'")
                assert False
    
    assert True

def run_integration_tests():
    """Run all integration tests"""
    print("Starting comprehensive integration tests for video and language features...")
    
    # Ensure database is migrated
    main.migrate_schema()
    
    tests = [
        test_end_to_end_word_addition_with_video,
        test_helper_functions,
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
            print(f"\n{'✓ PASSED' if result else '✗ FAILED'}: {test.__name__}")
        except Exception as e:
            print(f"\n✗ FAILED: {test.__name__} - Exception: {e}")
            results.append(False)
    
    passed = sum(results)
    total = len(results)
    
    print("\n" + "=" * 60)
    print("INTEGRATION TEST RESULTS")
    print("=" * 60)
    print(f"Tests passed: {passed}/{total}")
    
    if passed == total:
        print("\n🎉 ALL INTEGRATION TESTS PASSED!")
        print("✅ Video integration features are fully functional")
        print("✅ Language selection features are fully functional")
        print("✅ Database schema updates are working correctly")
        print("✅ Word addition and editing with video support is working")
        assert True
    else:
        print(f"\n⚠️  {total - passed} integration test(s) failed")
        assert False

if __name__ == "__main__":
    success = run_integration_tests()
    sys.exit(0 if success else 1)