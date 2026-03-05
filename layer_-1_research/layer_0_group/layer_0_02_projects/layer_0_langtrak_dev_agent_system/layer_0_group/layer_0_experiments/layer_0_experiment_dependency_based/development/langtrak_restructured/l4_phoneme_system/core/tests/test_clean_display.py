#!/usr/bin/env python3
# resource_id: "d836e5ea-12d7-4f6d-936f-660044b2b49d"
# resource_type: "document"
# resource_name: "test_clean_display"
"""
Test script to verify the cleaner hierarchy display format.
"""

import main
import os

# Ensure database is ready
if not os.path.exists("data/phonemes.db"):
    print("Initializing database...")
    main.migrate_schema()
    main.insert_sample_data()

def test_clean_display():
    """Test the cleaner hierarchy display format."""
    
    print("🧪 TESTING CLEANER HIERARCHY DISPLAY")
    print("=" * 60)
    
    # Test parameters
    syllable_type = "CVC"
    positions = ["onset", "nucleus", "coda"]
    length_types = {
        "onset": ["single_consonants", "cluster2", "cluster3"],
        "nucleus": ["monophthongs", "diphthongs"],
        "coda": ["single_consonants", "cluster2", "cluster3"]
    }
    
    print("\n🎯 TESTING 'ALL TYPES' DISPLAY WITH CLEAN FORMAT")
    print("-" * 50)
    
    # Test 'all' filters (should show clean hierarchy side by side)
    all_filters = {
        'onset': 'all',
        'nucleus': 'all',
        'coda': 'all'
    }
    
    print("Applying 'all types' filters (ad,bc,cd):")
    for pos, filt in all_filters.items():
        print(f"  {pos}: {filt}")
    
    print("\nDisplaying all types tables with clean hierarchy...")
    all_position_mappings = main.display_phoneme_tables_side_by_side_with_filters(
        syllable_type, positions, length_types, all_filters
    )
    
    print("\n🎉 CLEAN DISPLAY TEST COMPLETED!")
    print("=" * 60)
    
    return True

if __name__ == "__main__":
    test_clean_display()
