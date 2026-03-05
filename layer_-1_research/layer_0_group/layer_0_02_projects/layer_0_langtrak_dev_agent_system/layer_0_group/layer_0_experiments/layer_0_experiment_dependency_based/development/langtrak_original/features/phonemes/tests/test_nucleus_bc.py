#!/usr/bin/env python3
# resource_id: "30d0d8db-19d5-41de-a941-1e12b3782c4d"
# resource_type: "document"
# resource_name: "test_nucleus_bc"
"""
Quick test to verify nucleus 'bc' command shows all phoneme types.
"""

import main

def test_nucleus_bc():
    """Test that nucleus 'bc' shows all phoneme types."""
    
    print("🧪 Testing Nucleus 'bc' Command")
    print("=" * 40)
    
    syllable_type = "CVC"
    positions = ["onset", "nucleus", "coda"]
    length_types = {
        "onset": ["single_consonants", "cluster2", "cluster3"],
        "nucleus": ["monophthongs", "diphthongs"],
        "coda": ["single_consonants", "cluster2", "cluster3"]
    }
    
    # Test nucleus with 'all' filter (which is what 'bc' should do)
    filters = {
        'onset': 'single_consonants',
        'nucleus': 'all',  # This is what 'bc' should set
        'coda': 'single_consonants'
    }
    
    print("Testing nucleus with 'all' filter...")
    print("This should show both monophthongs and diphthongs combined and sorted by frequency.")
    
    position_mappings = main.display_phoneme_tables_side_by_side_with_filters(
        syllable_type, positions, length_types, filters
    )
    
    # Verify the nucleus has all phoneme types
    if 'nucleus' in position_mappings:
        nucleus_count = len(position_mappings['nucleus'])
        print(f"\n✓ Nucleus has {nucleus_count} total phonemes")
        
        # Check what types are included
        nucleus_types = set()
        for num, data in position_mappings['nucleus'].items():
            nucleus_types.add(data['length_type'])
        
        print(f"✓ Nucleus includes these length types: {nucleus_types}")
        
        if 'monophthongs' in nucleus_types and 'diphthongs' in nucleus_types:
            print("✓ Nucleus correctly shows both monophthongs and diphthongs")
        else:
            print("✗ Nucleus missing some phoneme types")
            return False
            
        # Show first few phonemes to verify sorting
        print("\nFirst few nucleus phonemes (should be sorted by frequency):")
        for i in range(1, min(6, nucleus_count + 1)):
            if i in position_mappings['nucleus']:
                data = position_mappings['nucleus'][i]
                print(f"  {i}: {data['phoneme']} ({data['length_type']}) - freq: {data['row_data'][6]}")
                
    else:
        print("✗ Nucleus not found in position mappings")
        return False
    
    print("\n🎉 Nucleus 'bc' test completed successfully!")
    return True

if __name__ == "__main__":
    test_nucleus_bc()
