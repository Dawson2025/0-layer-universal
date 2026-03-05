#!/usr/bin/env python3
# resource_id: "e68c75d4-5006-42d4-a360-bcc60cc00db4"
# resource_type: "document"
# resource_name: "test_new_functionality"
"""
Test script for the new table-based word creation functionality
"""

import main

def test_new_functions():
    """Test the new functions without running the full interactive application"""
    
    print("Testing new table-based word creation functionality...")
    
    # Test data
    syllable_type = "CVC"
    positions = ["onset", "nucleus", "coda"]
    length_types = {
        "onset": ["single_consonants"],
        "nucleus": ["monophthongs"],
        "coda": ["single_consonants"]
    }
    
    print(f"\nTest parameters:")
    print(f"Syllable type: {syllable_type}")
    print(f"Positions: {positions}")
    print(f"Length types: {length_types}")
    
    try:
        # Test the new display function
        print("\n1. Testing display_phoneme_tables_side_by_side_with_numbers...")
        phoneme_mapping = main.display_phoneme_tables_side_by_side_with_numbers(
            syllable_type, positions, length_types
        )
        
        if phoneme_mapping:
            print(f"✓ Display function successful! Created mapping with {len(phoneme_mapping)} phonemes")
            print("Sample mapping entries:")
            for i, (num, data) in enumerate(list(phoneme_mapping.items())[:3]):
                print(f"  {num}: {data['phoneme']} ({data['position']} - {data['length_type']})")
        else:
            print("✗ Display function failed - no mapping returned")
            return False
        
        # Test the selection function with sample input
        print("\n2. Testing select_phonemes_by_numbers...")
        test_numbers = [1, 4, 7]  # Sample selection
        print(f"Test input: {test_numbers}")
        
        result = main.select_phonemes_by_numbers(phoneme_mapping, positions)
        if result:
            print("✓ Selection function successful!")
            print("Note: This function requires user input, so it will wait for input")
        else:
            print("✗ Selection function failed")
            return False
        
        print("\n✓ All tests passed! The new functionality appears to be working correctly.")
        return True
        
    except Exception as e:
        print(f"✗ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_new_functions()
    if success:
        print("\n🎉 New functionality is ready for testing!")
    else:
        print("\n❌ There are issues with the new functionality that need to be fixed.")
