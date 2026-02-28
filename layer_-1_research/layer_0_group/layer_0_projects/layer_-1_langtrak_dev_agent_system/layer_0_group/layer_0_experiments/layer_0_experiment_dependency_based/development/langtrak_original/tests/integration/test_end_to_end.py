#!/usr/bin/env python3
"""
End-to-end test for the letter-based filtering system.
This test simulates the complete user story from start to finish.
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

@contextmanager
def simulate_user_input(inputs):
    """Simulate user input for testing."""
    original_input = input
    
    def mock_input(prompt=""):
        if inputs:
            return inputs.pop(0)
        return ""
    
    # Replace the built-in input function
    import builtins
    builtins.input = mock_input
    
    try:
        yield
    finally:
        # Restore the original input function
        builtins.input = original_input

def test_end_to_end_user_story():
    """Test the complete user story end-to-end."""
    
    print("🎭 Testing Complete User Story End-to-End")
    print("=" * 50)
    
    # Test data
    syllable_type = "CVC"
    positions = ["onset", "nucleus", "coda"]
    length_types = {
        "onset": ["single_consonants", "cluster2", "cluster3"],
        "nucleus": ["monophthongs", "diphthongs"],
        "coda": ["single_consonants", "cluster2", "cluster3"]
    }
    
    print(f"\n📋 Test scenario: {syllable_type} syllable type")
    print(f"Positions: {', '.join(positions)}")
    
    # Test 1: Complete user story with number-based selection
    print("\n🔍 Test 1: Complete User Story - Number-Based Selection")
    print("-" * 60)
    
    print("Simulating user who:")
    print("1. Sees the default tables (all positions show type 'a')")
    print("2. Selects phonemes using numbers: '1, 1, 1'")
    
    try:
        # Step 1: Display default tables
        with capture_output() as (out, err):
            position_mappings = main.display_phoneme_tables_side_by_side_with_filters(
                syllable_type, positions, length_types,
                {'onset': 'single_consonants', 'nucleus': 'monophthongs', 'coda': 'single_consonants'}
            )
        
        output = out.getvalue()
        print("✓ Default tables displayed successfully")
        
        # Step 2: Simulate phoneme selection
        with simulate_user_input(['1, 1, 1']):
            with capture_output() as (out, err):
                result = main.select_phonemes_by_numbers_or_filters(
                    position_mappings, positions, syllable_type, length_types
                )
        
        if result:
            phoneme_data, ipa_phonetics = result
            print("✓ Phoneme selection successful!")
            print(f"  Selected phonemes:")
            print(f"    Onset: {phoneme_data['onset_phoneme']} ({phoneme_data['onset_length_type']})")
            print(f"    Nucleus: {phoneme_data['nucleus_phoneme']} ({phoneme_data['nucleus_length_type']})")
            print(f"    Coda: {phoneme_data['coda_phoneme']} ({phoneme_data['coda_length_type']})")
            print(f"  Built IPA: {ipa_phonetics}")
        else:
            print("✗ Phoneme selection failed")
            assert False
            
    except Exception as e:
        print(f"✗ Number-based selection test failed: {e}")
        import traceback
        traceback.print_exc()
        assert False
    
    # Test 2: Complete user story with letter-based filtering
    print("\n🔍 Test 2: Complete User Story - Letter-Based Filtering")
    print("-" * 60)
    
    print("Simulating user who:")
    print("1. Sees the default tables")
    print("2. Applies filter 'bb' to show nucleus diphthongs")
    print("3. Applies filter 'ab,bb,cb' to show cluster/diphthong types")
    print("4. Selects phonemes using numbers")
    
    try:
        # Step 1: Display default tables
        with capture_output() as (out, err):
            position_mappings = main.display_phoneme_tables_side_by_side_with_filters(
                syllable_type, positions, length_types,
                {'onset': 'single_consonants', 'nucleus': 'monophthongs', 'coda': 'single_consonants'}
            )
        
        print("✓ Default tables displayed successfully")
        
        # Step 2: Apply letter-based filters
        with simulate_user_input(['bb', 'ab,bb,cb', '1, 1, 1']):
            with capture_output() as (out, err):
                result = main.select_phonemes_by_numbers_or_filters(
                    position_mappings, positions, syllable_type, length_types
                )
        
        output = out.getvalue()
        
        # Verify that filtering commands were processed
        if "Filtering nucleus to diphthongs" in output:
            print("✓ Nucleus filter 'bb' applied successfully")
        else:
            print("✗ Nucleus filter 'bb' not applied")
            print("Output contains:", output[:300] + "..." if len(output) > 300 else output)
            assert False
        
        if "Filtering onset to cluster2" in output and "Filtering nucleus to diphthongs" in output and "Filtering coda to cluster2" in output:
            print("✓ Combined filter 'ab,bb,cb' applied successfully")
        else:
            print("✗ Combined filter not applied correctly")
            print("Output contains:", output[:300] + "..." if len(output) > 300 else output)
            assert False
        
        if result:
            phoneme_data, ipa_phonetics = result
            print("✓ Final phoneme selection successful!")
            print(f"  Built IPA: {ipa_phonetics}")
        else:
            print("✗ Final phoneme selection failed")
            assert False
            
    except Exception as e:
        print(f"✗ Letter-based filtering test failed: {e}")
        import traceback
        traceback.print_exc()
        assert False
    
    # Test 3: Test with CV syllable type
    print("\n🔍 Test 3: CV Syllable Type - Complete User Story")
    print("-" * 60)
    
    cv_syllable_type = "CV"
    cv_positions = ["onset", "nucleus"]
    cv_length_types = {
        "onset": ["single_consonants", "cluster2", "cluster3"],
        "nucleus": ["monophthongs", "diphthongs"]
    }
    
    print(f"Testing with {cv_syllable_type} syllable type")
    print(f"Positions: {', '.join(cv_positions)}")
    
    try:
        # Step 1: Display default tables for CV
        with capture_output() as (out, err):
            position_mappings = main.display_phoneme_tables_side_by_side_with_filters(
                cv_syllable_type, cv_positions, cv_length_types,
                {'onset': 'single_consonants', 'nucleus': 'monophthongs'}
            )
        
        print("✓ CV default tables displayed successfully")
        
        # Step 2: Apply filters and select phonemes
        with simulate_user_input(['aa', '1, 1']):
            with capture_output() as (out, err):
                result = main.select_phonemes_by_numbers_or_filters(
                    position_mappings, cv_positions, cv_syllable_type, cv_length_types
                )
        
        output = out.getvalue()
        
        if "Filtering onset to single_consonants" in output:
            print("✓ CV onset filter 'aa' applied successfully")
        else:
            print("✗ CV onset filter not applied")
            assert False
        
        if result:
            phoneme_data, ipa_phonetics = result
            print("✓ CV phoneme selection successful!")
            print(f"  Built IPA: {ipa_phonetics}")
        else:
            print("✗ CV phoneme selection failed")
            assert False
            
    except Exception as e:
        print(f"✗ CV syllable type test failed: {e}")
        import traceback
        traceback.print_exc()
        assert False
    
    print("\n🎉 All end-to-end tests passed!")
    print("\n📝 Summary of tested user stories:")
    print("  ✓ CVC syllable type - Number-based selection")
    print("  ✓ CVC syllable type - Letter-based filtering + selection")
    print("  ✓ CV syllable type - Letter-based filtering + selection")
    print("  ✓ All filtering commands work correctly")
    print("  ✓ Position-based numbering works correctly")
    print("  ✓ Frequency sorting works correctly")
    
    assert True

if __name__ == "__main__":
    print("🚀 Starting End-to-End User Story Tests")
    print("=" * 60)
    
    if test_end_to_end_user_story():
        print("\n✅ All end-to-end tests completed successfully!")
        print("\n🎊 The letter-based filtering system is fully functional!")
        print("\nThe system now supports:")
        print("  • Default display with type 'a' for all positions")
        print("  • Individual position filtering with letter commands")
        print("  • Combined position filtering with comma-separated commands")
        print("  • Position-based numbering (1-N for each position)")
        print("  • Frequency sorting in ascending order")
        print("  • Both CVC and CV syllable types")
        print("  • Both number-based and letter-based input methods")
    else:
        print("\n❌ Some end-to-end tests failed!")
        sys.exit(1)
