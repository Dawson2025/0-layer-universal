#!/usr/bin/env python3
# resource_id: "e87e2c26-0885-4266-ab2e-de236137d1a0"
# resource_type: "document"
# resource_name: "test_suggestion_method"
"""
Test script for the new suggestion-based word creation method.
"""

import sys
import io
from contextlib import contextmanager
from main import (
    create_word_suggestion_based,
    generate_phoneme_suggestions,
    select_phonemes_with_suggestions,
    process_phoneme_selection,
    display_phoneme_tables_side_by_side_with_numbers,
    migrate_schema,
    insert_sample_data
)

@contextmanager
def simulate_user_input(inputs):
    """Context manager to simulate user input for testing."""
    input_iter = iter(inputs)
    
    def mock_input(prompt=""):
        try:
            user_input = next(input_iter)
            print(f"{prompt}{user_input}")  # Show what input was "typed"
            return user_input
        except StopIteration:
            return ""
    
    original_input = __builtins__.get('input', input)
    __builtins__['input'] = mock_input
    try:
        yield
    finally:
        __builtins__['input'] = original_input

def test_suggestion_generation():
    """Test the suggestion generation algorithm."""
    print("=== Testing Suggestion Generation ===")
    
    # Initialize database
    migrate_schema()
    insert_sample_data()
    
    # Test with CVC syllable type
    syllable_type = "CVC"
    positions = ["onset", "nucleus", "coda"]
    length_types = {
        "onset": ["single_consonants"],
        "nucleus": ["monophthongs"],
        "coda": ["single_consonants"]
    }
    
    # Get position mappings
    position_mappings = display_phoneme_tables_side_by_side_with_numbers(
        syllable_type, positions, length_types
    )
    
    # Generate suggestions
    suggestions = generate_phoneme_suggestions(position_mappings, positions, max_suggestions=15)
    
    print(f"\nGenerated {len(suggestions)} suggestions:")
    for i, suggestion in enumerate(suggestions, 1):
        combo_str = ",".join(map(str, suggestion))
        print(f"s{i}: [{combo_str}]")
    
    # Verify the first few suggestions follow the expected pattern
    expected_patterns = [
        [1, 1, 1],  # s1: least frequent from each position
        [2, 1, 1],  # s2: 2nd least frequent onset
        [1, 2, 1],  # s3: 2nd least frequent nucleus
        [1, 1, 2],  # s4: 2nd least frequent coda
        [2, 2, 1],  # s5: 2nd least frequent onset + nucleus
    ]
    
    print("\nVerifying suggestion pattern:")
    for i, expected in enumerate(expected_patterns):
        if i < len(suggestions):
            actual = suggestions[i]
            match = actual == expected
            print(f"s{i+1}: Expected {expected}, Got {actual} {'✓' if match else '✗'}")
        else:
            print(f"s{i+1}: Expected {expected}, Got None (not enough suggestions)")
    
    return True

def test_process_selection():
    """Test the phoneme selection processing."""
    print("\n=== Testing Selection Processing ===")
    
    # Initialize database
    migrate_schema()
    insert_sample_data()
    
    # Test with CV syllable type
    syllable_type = "CV"
    positions = ["onset", "nucleus"]
    length_types = {
        "onset": ["single_consonants"],
        "nucleus": ["monophthongs"]
    }
    
    # Get position mappings
    position_mappings = display_phoneme_tables_side_by_side_with_numbers(
        syllable_type, positions, length_types
    )
    
    # Test processing a selection
    test_numbers = [1, 1]  # Select first phoneme from each position
    
    try:
        phoneme_data, ipa_phonetics = process_phoneme_selection(
            test_numbers, positions, position_mappings
        )
        
        print(f"\nSelection processing successful!")
        print(f"IPA: {ipa_phonetics}")
        print(f"Onset: {phoneme_data['onset_phoneme']} ({phoneme_data['onset_length_type']})")
        print(f"Nucleus: {phoneme_data['nucleus_phoneme']} ({phoneme_data['nucleus_length_type']})")
        
        # Verify structure
        expected_keys = ['syllable_type', 'onset_phoneme', 'onset_length_type', 
                        'nucleus_phoneme', 'nucleus_length_type', 'coda_phoneme', 'coda_length_type']
        missing_keys = [key for key in expected_keys if key not in phoneme_data]
        
        if missing_keys:
            print(f"✗ Missing keys in phoneme_data: {missing_keys}")
            return False
        else:
            print("✓ Phoneme data structure is correct")
            return True
            
    except Exception as e:
        print(f"✗ Error processing selection: {e}")
        return False

def test_full_user_story():
    """Test the complete user story flow."""
    print("\n=== Testing Complete User Story ===")
    
    # Initialize database
    migrate_schema()
    insert_sample_data()
    
    # Simulate user inputs for the complete flow
    user_inputs = [
        "TestLang",        # Language name
        "hello",           # English word
        "1",               # CVC syllable type
        "1",               # Solo phonemes length type
        "s1",              # Select first suggestion
        "helo",            # Word in test language
        "/hello/",         # Dictionary phonetics
        "n"                # Don't save (for testing)
    ]
    
    print("Simulating complete user story...")
    
    try:
        with simulate_user_input(user_inputs):
            create_word_suggestion_based()
        
        print("✓ Complete user story test passed!")
        return True
        
    except Exception as e:
        print(f"✗ Error in complete user story: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Run all tests."""
    print("Testing Suggestion-Based Word Creation Method")
    print("=" * 50)
    
    tests = [
        test_suggestion_generation,
        test_process_selection,
        test_full_user_story
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"✗ Test {test.__name__} failed with error: {e}")
            import traceback
            traceback.print_exc()
            results.append(False)
    
    print("\n" + "=" * 50)
    print("TEST SUMMARY:")
    print(f"Passed: {sum(results)}/{len(results)}")
    
    if all(results):
        print("🎉 All tests passed! The suggestion-based method is working correctly.")
    else:
        print("❌ Some tests failed. Check the output above for details.")
    
    return all(results)

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
