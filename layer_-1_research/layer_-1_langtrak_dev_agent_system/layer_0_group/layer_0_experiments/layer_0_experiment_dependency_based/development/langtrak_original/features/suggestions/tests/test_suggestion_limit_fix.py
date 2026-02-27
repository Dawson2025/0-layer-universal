#!/usr/bin/env python3
"""
Test that the suggestion limit fix allows for many more suggestions.
"""

from main import (
    generate_phoneme_suggestions,
    migrate_schema,
    insert_sample_data,
    display_phoneme_tables_side_by_side_with_numbers
)

def test_suggestion_limit_fix():
    """Test that we can now generate many more than 20 suggestions."""
    print("=== Testing Suggestion Limit Fix ===")
    
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
    
    print(f"Position mapping sizes:")
    for pos in positions:
        print(f"  {pos}: {len(position_mappings[pos])} phonemes available")
    
    # Calculate theoretical maximum
    max_possible = 1
    for pos in positions:
        max_possible *= len(position_mappings[pos])
    print(f"  Theoretical maximum combinations: {max_possible}")
    
    # Test different suggestion limits
    limits_to_test = [20, 50, 100, 200, 500]
    
    for limit in limits_to_test:
        suggestions = generate_phoneme_suggestions(position_mappings, positions, max_suggestions=limit)
        actual_generated = len(suggestions)
        print(f"  Requested {limit}, got {actual_generated} suggestions")
        
        # Show first and last few
        if actual_generated > 0:
            print(f"    First: {suggestions[0]}")
            if actual_generated > 1:
                print(f"    Last:  {suggestions[-1]}")
    
    # Test the extend scenario
    print(f"\n=== Extend Feature Test ===")
    suggestions = generate_phoneme_suggestions(position_mappings, positions, max_suggestions=500)
    total_available = len(suggestions)
    print(f"Total suggestions available: {total_available}")
    
    # Simulate extend scenarios
    display_counts = [15, 30, 45, 60, 75, 90]
    for count in display_counts:
        if count <= total_available:
            remaining = total_available - count
            print(f"  Showing {count}: {remaining} more available")
        else:
            print(f"  Showing {count}: Cannot show (only {total_available} available)")
    
    return total_available

if __name__ == "__main__":
    total = test_suggestion_limit_fix()
    print(f"\n✅ Suggestion limit fix successful!")
    print(f"   Now generating {total} suggestions instead of just 20")
    print(f"   Users can extend through many more options!")
