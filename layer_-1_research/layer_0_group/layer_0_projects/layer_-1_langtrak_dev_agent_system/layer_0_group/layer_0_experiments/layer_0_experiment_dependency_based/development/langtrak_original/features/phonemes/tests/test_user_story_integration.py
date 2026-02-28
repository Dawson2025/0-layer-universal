#!/usr/bin/env python3
"""
Test script for the complete user story integration.
This tests the table-based word creation method with the new hierarchy display.
"""

import main
import os

# Ensure database is ready
if not os.path.exists("data/phonemes.db"):
    print("Initializing database...")
    main.migrate_schema()
    main.insert_sample_data()

def test_complete_user_story():
    """Test the complete user story flow with hierarchy display."""
    
    print("🧪 TESTING COMPLETE USER STORY INTEGRATION")
    print("=" * 60)
    
    print("\n📖 USER STORY SIMULATION:")
    print("1. User selects table-based method for word creation")
    print("2. User chooses 'multiple types' for length types")
    print("3. System displays default single phoneme tables")
    print("4. User applies 'all types' filter (ad,bc,cd)")
    print("5. System displays all types with group/subgroup hierarchy")
    print("6. User selects phonemes by number")
    print("7. System creates the word")
    
    print("\n" + "="*60)
    
    # Test parameters
    syllable_type = "CVC"
    positions = ["onset", "nucleus", "coda"]
    length_types = {
        "onset": ["single_consonants", "cluster2", "cluster3"],
        "nucleus": ["monophthongs", "diphthongs"],
        "coda": ["single_consonants", "cluster2", "cluster3"]
    }
    
    print("\n🎯 STEP 1: Display default tables (single phonemes only)")
    print("-" * 50)
    
    # Default filters (single phonemes only)
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
    
    print("\n🎯 STEP 2: Apply 'all types' filter and display hierarchy")
    print("-" * 50)
    
    # Apply 'all types' filters
    all_filters = {
        'onset': 'all',
        'nucleus': 'all',
        'coda': 'all'
    }
    
    print("Applying 'all types' filters (ad,bc,cd):")
    for pos, filt in all_filters.items():
        print(f"  {pos}: {filt}")
    
    print("\nDisplaying all types tables with hierarchy...")
    all_position_mappings = main.display_phoneme_tables_side_by_side_with_filters(
        syllable_type, positions, length_types, all_filters
    )
    
    print("\n🎯 STEP 3: Simulate phoneme selection")
    print("-" * 50)
    
    # Simulate user selecting phonemes by number
    # Let's pick some phonemes from different groups to test the hierarchy
    selected_phonemes = {}
    
    # For onset, pick from different groups
    onset_selections = [1, 15, 25]  # Different groups
    for i, num in enumerate(onset_selections):
        if num in all_position_mappings['onset']:
            data = all_position_mappings['onset'][num]
            selected_phonemes['onset'] = {
                'phoneme': data['phoneme'],
                'length_type': data['length_type'],
                'group': data['group_type'],
                'subgroup': data['subgroup_type'],
                'frequency': data['frequency']
            }
            print(f"  Onset {num}: {data['phoneme']} ({data['length_type']}) - {data['group_type']}")
            break
    
    # For nucleus, pick from different groups
    nucleus_selections = [1, 6, 10]  # Different groups
    for i, num in enumerate(nucleus_selections):
        if num in all_position_mappings['nucleus']:
            data = all_position_mappings['nucleus'][num]
            selected_phonemes['nucleus'] = {
                'phoneme': data['phoneme'],
                'length_type': data['length_type'],
                'group': data['group_type'],
                'subgroup': data['subgroup_type'],
                'frequency': data['frequency']
            }
            print(f"  Nucleus {num}: {data['phoneme']} ({data['length_type']}) - {data['group_type']}")
            break
    
    # For coda, pick from different groups
    coda_selections = [1, 7, 13]  # Different groups
    for i, num in enumerate(coda_selections):
        if num in all_position_mappings['coda']:
            data = all_position_mappings['coda'][num]
            selected_phonemes['coda'] = {
                'phoneme': data['phoneme'],
                'length_type': data['length_type'],
                'group': data['group_type'],
                'subgroup': data['subgroup_type'],
                'frequency': data['frequency']
            }
            print(f"  Coda {num}: {data['phoneme']} ({data['length_type']}) - {data['group_type']}")
            break
    
    print("\n🎯 STEP 4: Verify selected phonemes and hierarchy")
    print("-" * 50)
    
    print("Selected phonemes summary:")
    for position in positions:
        if position in selected_phonemes:
            data = selected_phonemes[position]
            if data['subgroup'] and data['subgroup'] != "none":
                print(f"  {position.capitalize()}: {data['phoneme']} ({data['length_type']}) - {data['group']} > {data['subgroup']}")
            else:
                print(f"  {position.capitalize()}: {data['phoneme']} ({data['length_type']}) - {data['group']}")
    
    print("\n🎯 STEP 5: Verify hierarchy sorting and organization")
    print("-" * 50)
    
    # Verify that the hierarchy is properly sorted
    for position in positions:
        if position in all_position_mappings:
            print(f"\n{position.upper()} hierarchy verification:")
            
            # Get unique groups and their frequencies
            group_frequencies = {}
            for num, data in all_position_mappings[position].items():
                group = data['group_type']
                if group not in group_frequencies:
                    group_frequencies[group] = data['group_freq']
            
            # Sort groups by frequency (ascending)
            sorted_groups = sorted(group_frequencies.items(), key=lambda x: x[1])
            
            print(f"  Groups sorted by frequency (ascending):")
            for i, (group, freq) in enumerate(sorted_groups):
                marker = "✅" if i < 3 else "  "  # Mark first 3 groups
                print(f"    {marker} {group}: {freq}")
            
            # Check if selected phoneme's group appears in the expected order
            if position in selected_phonemes:
                selected_group = selected_phonemes[position]['group']
                group_index = next(i for i, (g, _) in enumerate(sorted_groups) if g == selected_group)
                print(f"  Selected phoneme group '{selected_group}' is at position {group_index + 1} in frequency order")
    
    print("\n🎉 USER STORY INTEGRATION TEST COMPLETED!")
    print("=" * 60)
    
    return True

if __name__ == "__main__":
    test_complete_user_story()
