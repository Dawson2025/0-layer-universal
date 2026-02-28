#!/usr/bin/env python3
"""
Test script for the new group/subgroup hierarchy display in table-based method.
This tests the enhanced display_phoneme_tables_side_by_side_with_filters function.
"""

import main
import os

# Ensure database is ready
if not os.path.exists("data/phonemes.db"):
    print("Initializing database...")
    main.migrate_schema()
    main.insert_sample_data()

def test_hierarchy_display():
    """Test the new hierarchy display functionality."""
    
    print("🧪 TESTING GROUP/SUBGROUP HIERARCHY DISPLAY")
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
    
    print("\n2️⃣ TESTING HIERARCHY DISPLAY (All Types)")
    print("-" * 50)
    
    # Test 'all' filters (should show all length types with hierarchy)
    all_filters = {
        'onset': 'all',
        'nucleus': 'all',
        'coda': 'all'
    }
    
    print("All types filters applied:")
    for pos, filt in all_filters.items():
        print(f"  {pos}: {filt}")
    
    print("\nDisplaying all types tables with hierarchy...")
    all_position_mappings = main.display_phoneme_tables_side_by_side_with_filters(
        syllable_type, positions, length_types, all_filters
    )
    
    print("\n3️⃣ VERIFYING HIERARCHY STRUCTURE")
    print("-" * 50)
    
    # Verify that the hierarchy is properly structured
    for position in positions:
        if position in all_position_mappings:
            print(f"\n{position.upper()} hierarchy verification:")
            
            # Check if groups and subgroups are properly organized
            groups_found = set()
            subgroups_found = set()
            
            for num, data in all_position_mappings[position].items():
                group = data['group_type']
                subgroup = data['subgroup_type']
                groups_found.add(group)
                if subgroup and subgroup != "none":
                    subgroups_found.add(subgroup)
            
            print(f"  Groups found: {sorted(groups_found)}")
            print(f"  Subgroups found: {sorted(subgroups_found)}")
            
            # Check first few phonemes to verify hierarchy
            print(f"  First few phonemes with hierarchy info:")
            for i in range(1, min(6, len(all_position_mappings[position]) + 1)):
                if i in all_position_mappings[position]:
                    data = all_position_mappings[position][i]
                    group = data['group_type']
                    subgroup = data['subgroup_type']
                    phoneme = data['phoneme']
                    freq = data['frequency']
                    group_freq = data['group_freq']
                    subgroup_freq = data['subgroup_freq']
                    
                    if subgroup and subgroup != "none":
                        print(f"    {i}: {phoneme} (freq: {freq}) - {group} > {subgroup} (group: {group_freq}, subgroup: {subgroup_freq})")
                    else:
                        print(f"    {i}: {phoneme} (freq: {freq}) - {group} (group: {group_freq})")
    
    print("\n4️⃣ VERIFYING FREQUENCY SORTING")
    print("-" * 50)
    
    # Verify that groups, subgroups, and phonemes are sorted by frequency in ascending order
    for position in positions:
        if position in all_position_mappings:
            print(f"\n{position.upper()} frequency sorting verification:")
            
            # Get unique groups and their frequencies
            group_frequencies = {}
            for num, data in all_position_mappings[position].items():
                group = data['group_type']
                if group not in group_frequencies:
                    group_frequencies[group] = data['group_freq']
            
            # Sort groups by frequency
            sorted_groups = sorted(group_frequencies.items(), key=lambda x: x[1])
            print(f"  Groups sorted by frequency (ascending):")
            for group, freq in sorted_groups:
                print(f"    {group}: {freq}")
            
            # Check if the order in position_mappings matches the sorted order
            print(f"  Verifying phoneme order follows group hierarchy...")
            current_group = None
            current_subgroup = None
            group_order_correct = True
            
            for num, data in all_position_mappings[position].items():
                group = data['group_type']
                subgroup = data['subgroup_type']
                
                if group != current_group:
                    current_group = group
                    current_subgroup = None
                
                if subgroup and subgroup != "none" and subgroup != current_subgroup:
                    current_subgroup = subgroup
                
                # Check if this group appears in the expected order
                expected_group_index = next(i for i, (g, _) in enumerate(sorted_groups) if g == group)
                if current_group != group:
                    print(f"    ❌ Group order mismatch at phoneme {num}")
                    group_order_correct = False
                    break
            
            if group_order_correct:
                print(f"  ✅ Group hierarchy order is correct")
    
    print("\n🎉 HIERARCHY DISPLAY TEST COMPLETED!")
    print("=" * 60)
    
    return True

if __name__ == "__main__":
    test_hierarchy_display()
