# resource_id: "3edb58ec-7ad2-4047-8890-80d471e13ec5"
# resource_type: "document"
# resource_name: "test_conflict_detection"

#!/usr/bin/env python3
"""Test conflict detection for the specific case of 'wɪð'"""

import main

def test_with_conflict():
    """Test that 'wɪð' correctly maps to 'with'"""
    print("Testing conflict detection for 'wɪð'...")
    
    # Get the English words set
    english_words = main.get_common_english_words_ipa()
    print(f"Total English words: {len(english_words)}")
    print(f"'wɪð' in English words: {'wɪð' in english_words}")
    
    # Test the conflict word info function
    existing_ipa = set()
    conflict_info = main.get_conflict_word_info('wɪð', existing_ipa, english_words)
    print(f"Conflict info for 'wɪð': {conflict_info}")
    
    # Test the filter function
    positions = ['onset', 'nucleus', 'coda']
    length_types = {
        "onset": ["single_consonants"],
        "nucleus": ["monophthongs"], 
        "coda": ["single_consonants"]
    }
    filters = {
        'onset': 'single_consonants',
        'nucleus': 'monophthongs',
        'coda': 'single_consonants'
    }
    
    position_mappings = main.display_phoneme_tables_side_by_side_with_filters(
        'CVC', positions, length_types, filters
    )
    
    # Create a test suggestion that would produce 'wɪð'
    # This requires finding the right phoneme numbers
    test_suggestion = [2, 2, 1]  # This might produce 'wɪð' depending on the mapping
    
    filtered, conflicting = main.filter_suggestions_for_conflicts(
        [test_suggestion], positions, position_mappings
    )
    
    print(f"Conflicting suggestions: {conflicting}")
    if conflicting:
        for conflict in conflicting:
            print(f"  IPA: {conflict['ipa']}")
            print(f"  Conflict info: {conflict['conflict_word']}")

if __name__ == "__main__":
    test_with_conflict()
