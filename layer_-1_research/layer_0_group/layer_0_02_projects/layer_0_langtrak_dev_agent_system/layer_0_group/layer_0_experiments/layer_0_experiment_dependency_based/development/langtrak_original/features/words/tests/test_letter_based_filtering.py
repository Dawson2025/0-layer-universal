#!/usr/bin/env python3
# resource_id: "d6e936ac-2174-4394-804b-153cc822106e"
# resource_type: "document"
# resource_name: "test_letter_based_filtering"
"""
Comprehensive test script for the letter-based filtering system.
This script simulates real user interactions with the app to test the new filtering functionality.
"""

import main
import sys
from io import StringIO
from contextlib import contextmanager

@contextmanager
def capture_output():
    """Capture stdout and stderr for testing."""
    old_out, old_err = sys.stdout, sys.stderr
    try:
        out = StringIO()
        err = StringIO()
        sys.stdout = out
        sys.stderr = err
        yield out, err
    finally:
        sys.stdout = old_out
        sys.stderr = old_err

def test_letter_based_filtering():
    """Test the letter-based filtering system comprehensively."""
    
    print("🧪 Testing Letter-Based Filtering System")
    print("=" * 50)
    
    # Test data
    syllable_type = "CVC"
    positions = ["onset", "nucleus", "coda"]
    length_types = {
        "onset": ["single_consonants", "cluster2", "cluster3"],
        "nucleus": ["monophthongs", "diphthongs"],
        "coda": ["single_consonants", "cluster2", "cluster3"]
    }
    
    # Test 1: Default display (all positions show type 'a')
    print("\n📋 Test 1: Default Display (All positions show type 'a')")
    print("-" * 40)
    
    default_filters = {
        'onset': 'single_consonants',
        'nucleus': 'monophthongs',
        'coda': 'single_consonants'
    }
    
    try:
        with capture_output() as (out, err):
            position_mappings = main.display_phoneme_tables_side_by_side_with_filters(
                syllable_type, positions, length_types, default_filters
            )
        
        output = out.getvalue()
        print("✓ Default display function executed successfully")
        
        # Verify default filters are applied
        if "ONSET (single_consonants)" in output and "NUCLEUS (monophthongs)" in output and "CODA (single_consonants)" in output:
            print("✓ Default filters correctly applied")
        else:
            print("✗ Default filters not correctly applied")
            print("Output contains:", output[:200] + "..." if len(output) > 200 else output)
            return False
            
    except Exception as e:
        print(f"✗ Default display test failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    # Test 2: Individual position filtering
    print("\n📋 Test 2: Individual Position Filtering")
    print("-" * 40)
    
    test_filters = [
        # Onset filtering
        {'onset': 'cluster2', 'nucleus': 'monophthongs', 'coda': 'single_consonants'},
        {'onset': 'cluster3', 'nucleus': 'monophthongs', 'coda': 'single_consonants'},
        {'onset': 'all', 'nucleus': 'monophthongs', 'coda': 'single_consonants'},
        
        # Nucleus filtering
        {'onset': 'single_consonants', 'nucleus': 'diphthongs', 'coda': 'single_consonants'},
        {'onset': 'single_consonants', 'nucleus': 'all', 'coda': 'single_consonants'},
        
        # Coda filtering
        {'onset': 'single_consonants', 'nucleus': 'monophthongs', 'coda': 'cluster2'},
        {'onset': 'single_consonants', 'nucleus': 'monophthongs', 'coda': 'cluster3'},
        {'onset': 'single_consonants', 'nucleus': 'monophthongs', 'coda': 'all'},
    ]
    
    for i, test_filter in enumerate(test_filters, 1):
        try:
            with capture_output() as (out, err):
                position_mappings = main.display_phoneme_tables_side_by_side_with_filters(
                    syllable_type, positions, length_types, test_filter
                )
            
            output = out.getvalue()
            
            # Check if the filter is correctly applied
            position_names = {'onset': 'ONSET', 'nucleus': 'NUCLEUS', 'coda': 'CODA'}
            expected_header = ""
            
            for position, filter_type in test_filter.items():
                if filter_type == 'all':
                    expected_header = f"{position_names[position]} (All Types)"
                else:
                    expected_header = f"{position_names[position]} ({filter_type})"
                
                if expected_header in output:
                    print(f"✓ Test {i}.{position}: {filter_type} filter applied correctly")
                else:
                    print(f"✗ Test {i}.{position}: {filter_type} filter not applied correctly")
                    print(f"Expected: {expected_header}")
                    print(f"Output contains: {output[:200]}...")
                    return False
                    
        except Exception as e:
            print(f"✗ Test {i} failed: {e}")
            return False
    
    # Test 3: Combined filtering (multiple positions at once)
    print("\n📋 Test 3: Combined Filtering (Multiple Positions)")
    print("-" * 40)
    
    combined_filters = [
        {'onset': 'cluster2', 'nucleus': 'diphthongs', 'coda': 'cluster2'},
        {'onset': 'all', 'nucleus': 'all', 'coda': 'all'},
        {'onset': 'single_consonants', 'nucleus': 'diphthongs', 'coda': 'cluster3'},
    ]
    
    for i, test_filter in enumerate(combined_filters, 1):
        try:
            with capture_output() as (out, err):
                position_mappings = main.display_phoneme_tables_side_by_side_with_filters(
                    syllable_type, positions, length_types, test_filter
                )
            
            output = out.getvalue()
            print(f"✓ Combined filter test {i} executed successfully")
            
            # Verify all filters are applied
            for position, filter_type in test_filter.items():
                position_name = position.upper()
                if filter_type == 'all':
                    expected = f"{position_name} (All Types)"
                else:
                    expected = f"{position_name} ({filter_type})"
                
                if expected in output:
                    print(f"  ✓ {position}: {filter_type}")
                else:
                    print(f"  ✗ {position}: {filter_type} not found")
                    return False
                    
        except Exception as e:
            print(f"✗ Combined filter test {i} failed: {e}")
            return False
    
    # Test 4: Position-based numbering verification
    print("\n📋 Test 4: Position-Based Numbering Verification")
    print("-" * 40)
    
    try:
        with capture_output() as (out, err):
            position_mappings = main.display_phoneme_tables_side_by_side_with_filters(
                syllable_type, positions, length_types, default_filters
            )
        
        # Verify that each position has its own numbering starting from 1
        for position in positions:
            if position in position_mappings:
                mapping = position_mappings[position]
                if mapping:
                    first_key = min(mapping.keys())
                    last_key = max(mapping.keys())
                    if first_key == 1:
                        print(f"✓ {position}: numbering starts from 1")
                    else:
                        print(f"✗ {position}: numbering doesn't start from 1 (starts from {first_key})")
                        return False
                    
                    # Check if numbering is sequential
                    expected_keys = set(range(1, len(mapping) + 1))
                    actual_keys = set(mapping.keys())
                    if expected_keys == actual_keys:
                        print(f"✓ {position}: numbering is sequential 1-{len(mapping)}")
                    else:
                        print(f"✗ {position}: numbering is not sequential")
                        print(f"Expected: {expected_keys}")
                        print(f"Actual: {actual_keys}")
                        return False
                else:
                    print(f"✗ {position}: no mapping data")
                    return False
            else:
                print(f"✗ {position}: not found in position mappings")
                return False
                
    except Exception as e:
        print(f"✗ Position-based numbering test failed: {e}")
        return False
    
    # Test 5: Frequency sorting verification (ascending order)
    print("\n📋 Test 5: Frequency Sorting Verification (Ascending Order)")
    print("-" * 40)
    
    try:
        with capture_output() as (out, err):
            position_mappings = main.display_phoneme_tables_side_by_side_with_filters(
                syllable_type, positions, length_types, default_filters
            )
        
        # Check the actual sorted data from the position mappings
        for position in positions:
            if position in position_mappings:
                # Get the phoneme data for this position from the mappings
                position_phonemes = []
                for num, data in position_mappings[position].items():
                    position_phonemes.append(data['row_data'])
                
                # Group by length type and check sorting
                for length_type in length_types[position]:
                    type_phonemes = [p for p in position_phonemes if p[2] == length_type]
                    if type_phonemes:
                        # Check if sorted by frequency in ascending order
                        frequencies = [p[6] for p in type_phonemes]
                        if frequencies == sorted(frequencies):
                            print(f"✓ {position} {length_type}: correctly sorted by frequency (ascending)")
                        else:
                            print(f"✗ {position} {length_type}: not correctly sorted by frequency")
                            print(f"Frequencies: {frequencies}")
                            print(f"Expected sorted: {sorted(frequencies)}")
                            return False
                            
    except Exception as e:
        print(f"✗ Frequency sorting test failed: {e}")
        return False
    
    # Test 6: Function existence and callability
    print("\n📋 Test 6: Function Existence and Callability")
    print("-" * 40)
    
    required_functions = [
        'display_phoneme_tables_side_by_side_with_filters',
        'select_phonemes_by_numbers_or_filters',
        'display_phoneme_tables_side_by_side_with_numbers'
    ]
    
    for func_name in required_functions:
        if hasattr(main, func_name) and callable(getattr(main, func_name)):
            print(f"✓ {func_name} exists and is callable")
        else:
            print(f"✗ {func_name} not found or not callable")
            return False
    
    print("\n🎉 All tests passed! The letter-based filtering system is working correctly.")
    print("\n📝 Summary of tested functionality:")
    print("  ✓ Default display with type 'a' for all positions")
    print("  ✓ Individual position filtering")
    print("  ✓ Combined position filtering")
    print("  ✓ Position-based numbering (1-N for each position)")
    print("  ✓ Frequency sorting in ascending order")
    print("  ✓ All required functions exist and are callable")
    
    return True

def test_cv_syllable_type():
    """Test the filtering system with CV syllable type."""
    
    print("\n🧪 Testing CV Syllable Type")
    print("=" * 30)
    
    syllable_type = "CV"
    positions = ["onset", "nucleus"]
    length_types = {
        "onset": ["single_consonants", "cluster2", "cluster3"],
        "nucleus": ["monophthongs", "diphthongs"]
    }
    
    default_filters = {
        'onset': 'single_consonants',
        'nucleus': 'monophthongs'
    }
    
    try:
        with capture_output() as (out, err):
            position_mappings = main.display_phoneme_tables_side_by_side_with_filters(
                syllable_type, positions, length_types, default_filters
            )
        
        output = out.getvalue()
        
        # Verify CV-specific behavior
        if "ONSET (single_consonants)" in output and "NUCLEUS (monophthongs)" in output:
            print("✓ CV syllable type filtering works correctly")
        else:
            print("✗ CV syllable type filtering not working correctly")
            return False
            
        # Verify position-based numbering for CV
        if position_mappings and 'onset' in position_mappings and 'nucleus' in position_mappings:
            onset_count = len(position_mappings['onset'])
            nucleus_count = len(position_mappings['nucleus'])
            print(f"✓ CV positions: onset has {onset_count} phonemes, nucleus has {nucleus_count} phonemes")
        else:
            print("✗ CV position mappings not created correctly")
            return False
            
    except Exception as e:
        print(f"✗ CV syllable type test failed: {e}")
        return False
    
    return True

if __name__ == "__main__":
    print("🚀 Starting Comprehensive Letter-Based Filtering Tests")
    print("=" * 60)
    
    # Test CVC syllable type
    if test_letter_based_filtering():
        print("\n✅ CVC syllable type tests passed!")
    else:
        print("\n❌ CVC syllable type tests failed!")
        sys.exit(1)
    
    # Test CV syllable type
    if test_cv_syllable_type():
        print("\n✅ CV syllable type tests passed!")
    else:
        print("\n❌ CV syllable type tests failed!")
        sys.exit(1)
    
    print("\n🎊 All tests completed successfully!")
    print("\nThe letter-based filtering system is ready for use!")
    print("\nTo test manually:")
    print("1. Run 'python main.py'")
    print("2. Select option 5 (Add new word)")
    print("3. Select option 3 (Table-based method)")
    print("4. Use filter commands like 'aa', 'bb', 'cc', 'ab,bb,cb', etc.")
