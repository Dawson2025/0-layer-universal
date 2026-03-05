#!/usr/bin/env python3
# resource_id: "61318d38-bdd7-432a-8546-5c13907aeef3"
# resource_type: "document"
# resource_name: "test_side_by_side"
"""
Simple test to verify side-by-side display works correctly.
"""

import main
import os

# Ensure database is ready
if not os.path.exists("data/phonemes.db"):
    print("Initializing database...")
    main.migrate_schema()
    main.insert_sample_data()

def test_side_by_side():
    """Test the side-by-side display with hierarchy."""
    
    print("🧪 TESTING SIDE-BY-SIDE HIERARCHY DISPLAY")
    print("=" * 60)
    
    # Test parameters
    syllable_type = "CVC"
    positions = ["onset", "nucleus", "coda"]
    length_types = {
        "onset": ["single_consonants", "cluster2", "cluster3"],
        "nucleus": ["monophthongs", "diphthongs"],
        "coda": ["single_consonants", "cluster2", "cluster3"]
    }
    
    print("\n1️⃣ TESTING DEFAULT DISPLAY (should be side-by-side)")
    print("-" * 50)
    
    # Test default filters (should show single phonemes side by side)
    default_filters = {
        'onset': 'single_consonants',
        'nucleus': 'monophthongs',
        'coda': 'single_consonants'
    }
    
    main.display_phoneme_tables_side_by_side_with_filters(
        syllable_type, positions, length_types, default_filters
    )
    
    print("\n2️⃣ TESTING 'ALL TYPES' DISPLAY (should be side-by-side with hierarchy)")
    print("-" * 50)
    
    # Test 'all' filters (should show hierarchy side by side)
    all_filters = {
        'onset': 'all',
        'nucleus': 'all',
        'coda': 'all'
    }
    
    main.display_phoneme_tables_side_by_side_with_filters(
        syllable_type, positions, length_types, all_filters
    )
    
    print("\n🎉 SIDE-BY-SIDE DISPLAY TEST COMPLETED!")
    
    return True

if __name__ == "__main__":
    test_side_by_side()
