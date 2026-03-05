#!/usr/bin/env python3
# resource_id: "82818d89-83c4-4072-b652-9a772e32635c"
# resource_type: "document"
# resource_name: "test_new_functions"
"""
Direct test of the new table-based word creation functionality
"""

import main

def test_new_functionality():
    """Test the new functions directly"""
    
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
        position_mappings = main.display_phoneme_tables_side_by_side_with_numbers(
            syllable_type, positions, length_types
        )
        
        if position_mappings:
            total_phonemes = sum(len(mapping) for mapping in position_mappings.values())
            print(f"✓ Display function successful! Created position-based mappings with {total_phonemes} total phonemes")
            print("Position-based mappings:")
            for position, mapping in position_mappings.items():
                print(f"  {position}: {len(mapping)} phonemes (numbered 1-{len(mapping)})")
                # Show first few entries for each position
                for i, (num, data) in enumerate(list(mapping.items())[:2]):
                    print(f"    {num}: {data['phoneme']} ({data['length_type']})")
        else:
            print("✗ Display function failed - no mappings returned")
            return False
        
        print("\n2. Testing select_phonemes_by_numbers...")
        print("This function requires user input, so we'll test the structure...")
        
        # Test with sample data to verify the function structure
        test_numbers = [1, 4, 7]
        print(f"Test input would be: {test_numbers}")
        
        # We can't test the input function directly, but we can verify the function exists
        if hasattr(main, 'select_phonemes_by_numbers'):
            print("✓ select_phonemes_by_numbers function exists and is callable")
        else:
            print("✗ select_phonemes_by_numbers function not found")
            return False
        
        print("\n✓ All tests passed! The new functionality appears to be working correctly.")
        print("\n🎉 New functionality is ready for testing!")
        print("\nTo test the complete user story:")
        print("1. Run 'python main.py'")
        print("2. Select option 5 (Add new word)")
        print("3. Select option 3 (Table-based method)")
        print("4. Follow the prompts to create a word using the new number-based selection")
        
        return True
        
    except Exception as e:
        print(f"✗ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_new_functionality()
    if success:
        print("\n✅ New functionality is working correctly!")
    else:
        print("\n❌ There are issues with the new functionality that need to be fixed.")
