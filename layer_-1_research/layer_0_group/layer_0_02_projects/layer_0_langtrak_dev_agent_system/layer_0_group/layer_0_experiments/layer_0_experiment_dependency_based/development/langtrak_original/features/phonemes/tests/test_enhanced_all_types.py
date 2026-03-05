#!/usr/bin/env python3
# resource_id: "2de036eb-c109-41dd-a807-9b4f5266957f"
# resource_type: "document"
# resource_name: "test_enhanced_all_types"
"""
Comprehensive test for the enhanced "all types" display user story.
This tests the complete flow from default single phonemes to filtered all types display.
"""

import main
import os

# Ensure database is ready
if not os.path.exists("data/phonemes.db"):
    print("Initializing database...")
    main.migrate_schema()
    main.insert_sample_data()

def test_enhanced_all_types_user_story():
    """Test the complete enhanced user story for all types display."""
    
    print("🧪 TESTING ENHANCED ALL TYPES USER STORY")
    print("=" * 60)
    
    # Test parameters
    syllable_type = "CVC"
    positions = ["onset", "nucleus", "coda"]
    length_types = {
        "onset": ["single_consonants", "cluster2", "cluster3"],
        "nucleus": ["monophthongs", "diphthongs"],
        "coda": ["single_consonants", "cluster2", "cluster3"]
    }
    
    print("\n1️⃣ TESTING DEFAULT DISPLAY (Single Phonemes Only)")
    print("-" * 50)
    
    # Test default filters (should show single phonemes only)
    default_filters = {
        'onset': 'single_consonants',
        'nucleus': 'monophthongs',
        'coda': 'single_consonants'
    }
    
    print("Default filters applied:")
    for pos, filt in default_filters.items():
        print(f"  {pos}: {filt}")
    
    print("\nDisplaying default tables...")
    default_position_mappings = main.display_phoneme_tables_side_by_side_with_filters(
        syllable_type, positions, length_types, default_filters
    )
    
    # Verify default display shows only single phonemes
    print("\n✅ VERIFYING DEFAULT DISPLAY:")
    for position in positions:
        if position in default_position_mappings:
            count = len(default_position_mappings[position])
            print(f"  {position}: {count} phonemes")
            
            # Check first few phonemes to verify they're single types
            for i in range(1, min(4, count + 1)):
                if i in default_position_mappings[position]:
                    data = default_position_mappings[position][i]
                    print(f"    {i}: {data['phoneme']} ({data['length_type']})")
    
    print("\n2️⃣ TESTING FILTERED DISPLAY (All Types Mixed)")
    print("-" * 50)
    
    # Test 'all' filters (should show all length types mixed together)
    all_filters = {
        'onset': 'all',
        'nucleus': 'all',
        'coda': 'all'
    }
    
    print("All types filters applied:")
    for pos, filt in all_filters.items():
        print(f"  {pos}: {filt}")
    
    print("\nDisplaying all types tables...")
    all_position_mappings = main.display_phoneme_tables_side_by_side_with_filters(
        syllable_type, positions, length_types, all_filters
    )
    
    # Verify all types display shows mixed length types
    print("\n✅ VERIFYING ALL TYPES DISPLAY:")
    for position in positions:
        if position in all_position_mappings:
            count = len(all_position_mappings[position])
            print(f"  {position}: {count} total phonemes")
            
            # Check what length types are included
            length_types_found = set()
            for i in range(1, min(6, count + 1)):
                if i in all_position_mappings[position]:
                    data = all_position_mappings[position][i]
                    length_types_found.add(data['length_type'])
                    print(f"    {i}: {data['phoneme']} ({data['length_type']}) - freq: {data['row_data'][6]}")
            
            print(f"  Length types found: {length_types_found}")
            
            # Verify that all expected length types are present
            expected_types = length_types[position]
            missing_types = set(expected_types) - length_types_found
            if missing_types:
                print(f"  ⚠️  Missing length types: {missing_types}")
            else:
                print(f"  ✅ All expected length types present")
    
    print("\n3️⃣ TESTING FREQUENCY SORTING (Ascending Order)")
    print("-" * 50)
    
    # Verify that phonemes are sorted by frequency in ascending order
    print("Verifying frequency sorting (should be ascending - lowest first):")
    for position in positions:
        if position in all_position_mappings:
            print(f"\n  {position.upper()} frequency progression:")
            frequencies = []
            for i in range(1, min(6, count + 1)):
                if i in all_position_mappings[position]:
                    data = all_position_mappings[position][i]
                    freq = data['row_data'][6]
                    frequencies.append(freq)
                    print(f"    {i}: {data['phoneme']} - freq: {freq}")
            
            # Check if frequencies are in ascending order
            if frequencies == sorted(frequencies):
                print(f"  ✅ Frequencies are correctly sorted in ascending order")
            else:
                print(f"  ❌ Frequencies are NOT in ascending order")
                print(f"     Expected: {sorted(frequencies)}")
                print(f"     Got: {frequencies}")
    
    print("\n4️⃣ TESTING POSITION-BASED NUMBERING")
    print("-" * 50)
    
    # Verify that each position starts numbering from 1
    print("Verifying position-based numbering (each position starts from 1):")
    for position in positions:
        if position in all_position_mappings:
            position_numbers = list(all_position_mappings[position].keys())
            position_numbers.sort()
            
            if position_numbers[0] == 1:
                print(f"  ✅ {position}: numbering starts from 1")
            else:
                print(f"  ❌ {position}: numbering starts from {position_numbers[0]}, not 1")
            
            # Check for gaps in numbering
            expected_numbers = list(range(1, len(position_numbers) + 1))
            if position_numbers == expected_numbers:
                print(f"  ✅ {position}: no gaps in numbering")
            else:
                print(f"  ❌ {position}: gaps in numbering detected")
    
    print("\n🎉 ENHANCED ALL TYPES USER STORY TEST COMPLETED!")
    print("=" * 60)
    
    return True

if __name__ == "__main__":
    test_enhanced_all_types_user_story()
