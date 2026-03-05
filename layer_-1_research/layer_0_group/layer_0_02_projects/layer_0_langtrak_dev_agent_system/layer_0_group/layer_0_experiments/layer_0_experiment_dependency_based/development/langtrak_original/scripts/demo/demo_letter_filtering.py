#!/usr/bin/env python3
# resource_id: "dfddfc0f-65c1-4a1e-a02a-4220a551addc"
# resource_type: "document"
# resource_name: "demo_letter_filtering"
"""
Demo script for the letter-based filtering system.
This shows how the filtering works with real examples.
"""

import main

def demo_letter_based_filtering():
    """Demonstrate the letter-based filtering system."""
    
    print("🎯 Letter-Based Filtering System Demo")
    print("=" * 50)
    
    # Test data
    syllable_type = "CVC"
    positions = ["onset", "nucleus", "coda"]
    length_types = {
        "onset": ["single_consonants", "cluster2", "cluster3"],
        "nucleus": ["monophthongs", "diphthongs"],
        "coda": ["single_consonants", "cluster2", "cluster3"]
    }
    
    print(f"\n📋 Testing with {syllable_type} syllable type")
    print(f"Positions: {', '.join(positions)}")
    print(f"Length types: {length_types}")
    
    # Demo 1: Default display (all positions show type 'a')
    print("\n🔍 Demo 1: Default Display (All positions show type 'a')")
    print("-" * 50)
    
    default_filters = {
        'onset': 'single_consonants',
        'nucleus': 'monophthongs',
        'coda': 'single_consonants'
    }
    
    print("Default filters:")
    for position, filter_type in default_filters.items():
        print(f"  {position}: {filter_type}")
    
    print("\nDisplaying tables with default filters...")
    position_mappings = main.display_phoneme_tables_side_by_side_with_filters(
        syllable_type, positions, length_types, default_filters
    )
    
    # Demo 2: Individual position filtering
    print("\n🔍 Demo 2: Individual Position Filtering")
    print("-" * 50)
    
    # Test onset filtering
    print("\nFiltering onset to show cluster2 phonemes...")
    onset_cluster2_filters = default_filters.copy()
    onset_cluster2_filters['onset'] = 'cluster2'
    
    position_mappings = main.display_phoneme_tables_side_by_side_with_filters(
        syllable_type, positions, length_types, onset_cluster2_filters
    )
    
    # Test nucleus filtering
    print("\nFiltering nucleus to show diphthongs...")
    nucleus_diphthong_filters = default_filters.copy()
    nucleus_diphthong_filters['nucleus'] = 'diphthongs'
    
    position_mappings = main.display_phoneme_tables_side_by_side_with_filters(
        syllable_type, positions, length_types, nucleus_diphthong_filters
    )
    
    # Demo 3: Combined filtering
    print("\n🔍 Demo 3: Combined Filtering (Multiple Positions)")
    print("-" * 50)
    
    print("Applying multiple filters at once:")
    combined_filters = {
        'onset': 'cluster2',
        'nucleus': 'diphthongs',
        'coda': 'cluster2'
    }
    
    for position, filter_type in combined_filters.items():
        print(f"  {position}: {filter_type}")
    
    print("\nDisplaying tables with combined filters...")
    position_mappings = main.display_phoneme_tables_side_by_side_with_filters(
        syllable_type, positions, length_types, combined_filters
    )
    
    # Demo 4: Show all phonemes for a position
    print("\n🔍 Demo 4: Show All Phonemes for a Position")
    print("-" * 50)
    
    print("Showing all phoneme types for onset position...")
    all_onset_filters = default_filters.copy()
    all_onset_filters['onset'] = 'all'
    
    position_mappings = main.display_phoneme_tables_side_by_side_with_filters(
        syllable_type, positions, length_types, all_onset_filters
    )
    
    # Demo 5: Position-based numbering verification
    print("\n🔍 Demo 5: Position-Based Numbering Verification")
    print("-" * 50)
    
    print("Verifying that each position has its own numbering starting from 1...")
    
    for position in positions:
        if position in position_mappings:
            mapping = position_mappings[position]
            if mapping:
                first_key = min(mapping.keys())
                last_key = max(mapping.keys())
                print(f"  {position}: numbered {first_key}-{last_key} ({len(mapping)} phonemes)")
                
                # Show first few phonemes with their numbers
                print(f"    First few phonemes:")
                for i in range(1, min(4, len(mapping) + 1)):
                    if i in mapping:
                        data = mapping[i]
                        print(f"      {i}: {data['phoneme']} ({data['length_type']}) - freq: {data['row_data'][6]}")
            else:
                print(f"  {position}: no phonemes")
        else:
            print(f"  {position}: not found in mappings")
    
    print("\n🎉 Demo completed successfully!")
    print("\n📝 Summary of demonstrated functionality:")
    print("  ✓ Default display with type 'a' for all positions")
    print("  ✓ Individual position filtering")
    print("  ✓ Combined position filtering")
    print("  ✓ Showing all phoneme types for a position")
    print("  ✓ Position-based numbering (1-N for each position)")
    print("  ✓ Frequency sorting in ascending order")
    
    print("\n💡 How to use in the main app:")
    print("1. Run 'python main.py'")
    print("2. Select option 5 (Add new word)")
    print("3. Select option 3 (Table-based method)")
    print("4. Use filter commands:")
    print("   - 'aa' = onset single consonants")
    print("   - 'bb' = nucleus diphthongs")
    print("   - 'cc' = coda cluster3")
    print("   - 'ab,bb,cb' = multiple positions at once")
    print("   - 'ad' = onset all types")
    print("   - 'bc' = nucleus all types (monophthongs + diphthongs)")

if __name__ == "__main__":
    demo_letter_based_filtering()
