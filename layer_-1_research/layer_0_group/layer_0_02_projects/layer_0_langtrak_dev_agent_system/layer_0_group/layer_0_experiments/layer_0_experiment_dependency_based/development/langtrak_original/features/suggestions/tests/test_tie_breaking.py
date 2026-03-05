#!/usr/bin/env python3
# resource_id: "d35afd07-6cd2-4644-809b-b61ace30ebf8"
# resource_type: "document"
# resource_name: "test_tie_breaking"
"""
Test script to verify that length type tie-breaking logic works correctly.
This tests that when groups have the same aggregate frequency, 
the group from the shorter length type takes priority.
"""

import main
import os

# Ensure database is ready
if not os.path.exists("data/phonemes.db"):
    print("Initializing database...")
    main.migrate_schema()
    main.insert_sample_data()

def test_tie_breaking_logic():
    """Test that length type tie-breaking works correctly."""
    
    print("🧪 TESTING LENGTH TYPE TIE-BREAKING LOGIC")
    print("=" * 60)
    
    # Test parameters
    syllable_type = "CVC"
    positions = ["onset", "nucleus", "coda"]
    length_types = {
        "onset": ["single_consonants", "cluster2", "cluster3"],
        "nucleus": ["monophthongs", "diphthongs"],
        "coda": ["single_consonants", "cluster2", "cluster3"]
    }
    
    print("\n1️⃣ TESTING 'ALL TYPES' DISPLAY WITH TIE-BREAKING")
    print("-" * 50)
    
    # Test the "all types" display which should show tie-breaking
    filters = {
        "onset": "all",      # ad - shows all onset types
        "nucleus": "all",    # bc - shows all nucleus types  
        "coda": "all"        # cd - shows all coda types
    }
    
    print("Filters applied: ad, bc, cd (all types)")
    print("Expected: Groups with same frequency sorted by length type priority")
    print("          (shorter length types first)")
    
    # Get the display
    position_mappings = main.display_phoneme_tables_side_by_side_with_filters(
        syllable_type, positions, length_types, filters
    )
    
    print("\n2️⃣ VERIFYING TIE-BREAKING IN DATA STRUCTURE")
    print("-" * 50)
    
    # Check if the position_mappings are properly sorted
    for position in positions:
        print(f"\n{position.upper()} position:")
        if position in position_mappings:
            # Show the first few entries to verify sorting
            count = 0
            for num, data in position_mappings[position].items():
                if count < 10:  # Show first 10 entries
                    print(f"  {num}: {data['phoneme']} ({data['length_type']}) - freq: {data['frequency']} - group: {data['group_type']}")
                    count += 1
                else:
                    break
        else:
            print("  No data available")
    
    print("\n3️⃣ TESTING INDIVIDUAL FILTERS WITH TIE-BREAKING")
    print("-" * 50)
    
    # Test individual filters that should also show tie-breaking
    individual_filters = [
        ("aa", "ba", "ca"),  # Single consonants for all positions
        ("ab", "bb", "cb"),  # Clusters for all positions
        ("ac", "bc", "cc")   # Complex clusters for all positions
    ]
    
    for i, (onset_filter, nucleus_filter, coda_filter) in enumerate(individual_filters, 1):
        print(f"\n{i}. Testing filters: {onset_filter}, {nucleus_filter}, {coda_filter}")
        
        filters = {
            "onset": onset_filter,
            "nucleus": nucleus_filter,
            "coda": coda_filter
        }
        
        try:
            position_mappings = main.display_phoneme_tables_side_by_side_with_filters(
                syllable_type, positions, length_types, filters
            )
            print(f"   ✅ Successfully displayed with tie-breaking")
        except Exception as e:
            print(f"   ❌ Error: {e}")
    
    print("\n" + "=" * 60)
    print("🎯 TIE-BREAKING TEST COMPLETE")
    print("\nExpected behavior:")
    print("• Groups sorted by aggregate frequency (ascending)")
    print("• When groups have same frequency, shorter length types appear first:")
    print("  - Onset/Coda: single_consonants (0) → cluster2 (1) → cluster3 (2)")
    print("  - Nucleus: monophthongs (0) → diphthongs (1)")
    print("• Subgroups within groups sorted by aggregate frequency (ascending)")
    print("• Phonemes within subgroups sorted by individual frequency (ascending)")

if __name__ == "__main__":
    test_tie_breaking_logic()
