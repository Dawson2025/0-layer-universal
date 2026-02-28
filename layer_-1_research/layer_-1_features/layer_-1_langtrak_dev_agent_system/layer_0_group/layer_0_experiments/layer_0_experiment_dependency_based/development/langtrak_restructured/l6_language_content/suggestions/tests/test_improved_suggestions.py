#!/usr/bin/env python3
"""
Test the improved suggestion generation algorithm.
"""

from main import generate_phoneme_suggestions, migrate_schema, insert_sample_data, display_phoneme_tables_side_by_side_with_numbers

def test_cvc_suggestions():
    """Test CVC suggestion generation with the improved algorithm."""
    print("=== Testing CVC Suggestions (Improved Algorithm) ===")
    
    # Initialize database
    migrate_schema()
    insert_sample_data()
    
    # Test with CVC syllable type
    syllable_type = "CVC"
    positions = ["onset", "nucleus", "coda"]
    length_types = {
        "onset": ["single_consonants"],
        "nucleus": ["monophthongs"],
        "coda": ["single_consonants"]
    }
    
    # Get position mappings
    position_mappings = display_phoneme_tables_side_by_side_with_numbers(
        syllable_type, positions, length_types
    )
    
    # Generate suggestions with improved algorithm
    suggestions = generate_phoneme_suggestions(position_mappings, positions, max_suggestions=27)
    
    print(f"\nGenerated {len(suggestions)} suggestions (showing first 20):")
    for i, suggestion in enumerate(suggestions[:20], 1):
        combo_str = ",".join(map(str, suggestion))
        freq_sum = sum(suggestion)
        print(f"s{i:2d}: [{combo_str}] (frequency sum: {freq_sum})")
    
    print(f"\nComplete sequence for 1-3 range:")
    expected_optimal_sequence = [
        [1,1,1],  # sum: 3
        [1,1,2], [1,2,1], [2,1,1],  # sum: 4
        [1,1,3], [1,2,2], [1,3,1], [2,1,2], [2,2,1], [3,1,1],  # sum: 5
        [1,2,3], [1,3,2], [2,1,3], [2,2,2], [2,3,1], [3,1,2], [3,2,1],  # sum: 6
        [1,3,3], [2,2,3], [2,3,2], [3,1,3], [3,2,2], [3,3,1],  # sum: 7
        [2,3,3], [3,2,3], [3,3,2],  # sum: 8
        [3,3,3]  # sum: 9
    ]
    
    print("\nExpected optimal sequence (if all combinations 1-3 are available):")
    for i, combo in enumerate(expected_optimal_sequence, 1):
        combo_str = ",".join(map(str, combo))
        freq_sum = sum(combo)
        print(f"s{i:2d}: [{combo_str}] (frequency sum: {freq_sum})")
    
    # Verify the algorithm produces expected results for combinations that exist
    print(f"\n=== Verification ===")
    matches = 0
    for i, (actual, expected) in enumerate(zip(suggestions, expected_optimal_sequence)):
        if actual == expected:
            matches += 1
            print(f"✓ s{i+1}: {actual} matches expected")
        else:
            print(f"✗ s{i+1}: {actual} differs from expected {expected}")
    
    print(f"\nMatches: {matches}/{min(len(suggestions), len(expected_optimal_sequence))}")
    
    return suggestions

def test_cv_suggestions():
    """Test CV suggestion generation."""
    print("\n=== Testing CV Suggestions ===")
    
    # Initialize database
    migrate_schema()
    insert_sample_data()
    
    # Test with CV syllable type
    syllable_type = "CV"
    positions = ["onset", "nucleus"]
    length_types = {
        "onset": ["single_consonants"],
        "nucleus": ["monophthongs"]
    }
    
    # Get position mappings
    position_mappings = display_phoneme_tables_side_by_side_with_numbers(
        syllable_type, positions, length_types
    )
    
    # Generate suggestions
    suggestions = generate_phoneme_suggestions(position_mappings, positions, max_suggestions=15)
    
    print(f"\nGenerated {len(suggestions)} CV suggestions:")
    for i, suggestion in enumerate(suggestions, 1):
        combo_str = ",".join(map(str, suggestion))
        freq_sum = sum(suggestion)
        print(f"s{i:2d}: [{combo_str}] (frequency sum: {freq_sum})")
    
    # Expected CV sequence
    expected_cv_sequence = [
        [1,1],  # sum: 2
        [1,2], [2,1],  # sum: 3
        [1,3], [2,2], [3,1],  # sum: 4
        [2,3], [3,2],  # sum: 5
        [3,3]  # sum: 6
    ]
    
    print(f"\nExpected CV sequence:")
    for i, combo in enumerate(expected_cv_sequence, 1):
        combo_str = ",".join(map(str, combo))
        freq_sum = sum(combo)
        print(f"s{i:2d}: [{combo_str}] (frequency sum: {freq_sum})")
    
    return suggestions

def analyze_optimization():
    """Analyze how well the algorithm optimizes for frequency usage."""
    print("\n=== Optimization Analysis ===")
    
    # Test the CVC case
    suggestions = test_cvc_suggestions()
    
    # Analyze frequency distribution
    frequency_sums = [sum(combo) for combo in suggestions[:15]]
    
    print(f"\nFrequency sum analysis (first 15 suggestions):")
    print(f"Sums: {frequency_sums}")
    print(f"Average: {sum(frequency_sums) / len(frequency_sums):.1f}")
    print(f"Range: {min(frequency_sums)} - {max(frequency_sums)}")
    
    # Check if suggestions are properly sorted by sum
    is_sorted = all(frequency_sums[i] <= frequency_sums[i+1] for i in range(len(frequency_sums)-1))
    print(f"Properly sorted by frequency sum: {'✓' if is_sorted else '✗'}")
    
    # Count suggestions by frequency sum
    from collections import Counter
    sum_counts = Counter(frequency_sums)
    print(f"\nDistribution by frequency sum:")
    for freq_sum in sorted(sum_counts.keys()):
        print(f"  Sum {freq_sum}: {sum_counts[freq_sum]} suggestions")

if __name__ == "__main__":
    test_cvc_suggestions()
    test_cv_suggestions() 
    analyze_optimization()
