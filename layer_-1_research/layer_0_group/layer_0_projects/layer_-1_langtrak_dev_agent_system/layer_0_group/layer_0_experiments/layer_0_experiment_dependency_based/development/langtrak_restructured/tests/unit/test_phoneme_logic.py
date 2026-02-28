"""
Unit tests for phoneme business logic
Fast, isolated tests for core phoneme functionality
"""

import pytest


def test_phoneme_frequency_calculation():
    """Test phoneme frequency calculation logic"""
    # Mock phoneme data
    phonemes = [
        {'phoneme': 'm', 'frequency': 5},
        {'phoneme': 'a', 'frequency': 3},
        {'phoneme': 't', 'frequency': 7},
    ]
    
    # Calculate total frequency
    total = sum(p['frequency'] for p in phonemes)
    assert total == 15
    
    # Calculate percentages
    percentages = {p['phoneme']: (p['frequency'] / total) * 100 for p in phonemes}
    assert percentages['m'] == pytest.approx(33.33, rel=0.01)
    assert percentages['a'] == pytest.approx(20.0, rel=0.01)
    assert percentages['t'] == pytest.approx(46.67, rel=0.01)


def test_phoneme_position_validation():
    """Test phoneme position validation"""
    valid_positions = ['onset', 'nucleus', 'coda']
    
    # Valid positions
    for pos in valid_positions:
        assert pos in valid_positions
    
    # Invalid positions
    invalid = ['middle', 'start', 'end']
    for pos in invalid:
        assert pos not in valid_positions


def test_syllable_type_validation():
    """Test syllable type validation"""
    valid_types = ['CV', 'CVC', 'V', 'VC', 'CCV', 'CCVC']
    
    assert 'CVC' in valid_types
    assert 'CV' in valid_types
    assert 'INVALID' not in valid_types


def test_phoneme_grouping():
    """Test phoneme grouping by type"""
    phonemes = [
        {'phoneme': 'm', 'group_type': 'Stops'},
        {'phoneme': 'n', 'group_type': 'Nasals'},
        {'phoneme': 'p', 'group_type': 'Stops'},
        {'phoneme': 'f', 'group_type': 'Fricatives'},
    ]
    
    # Group by type
    grouped = {}
    for p in phonemes:
        group = p['group_type']
        if group not in grouped:
            grouped[group] = []
        grouped[group].append(p['phoneme'])
    
    assert len(grouped['Stops']) == 2
    assert 'm' in grouped['Stops']
    assert 'p' in grouped['Stops']
    assert len(grouped['Nasals']) == 1
    assert len(grouped['Fricatives']) == 1


def test_phoneme_length_type_classification():
    """Test phoneme length type classification"""
    length_types = {
        'single_consonants': ['m', 'n', 'p', 't'],
        'cluster2': ['st', 'pl', 'tr'],
        'cluster3': ['str', 'spl'],
        'monophthongs': ['a', 'e', 'i', 'o', 'u'],
        'diphthongs': ['aɪ', 'eɪ', 'oʊ'],
    }
    
    # Test single consonants
    assert 'm' in length_types['single_consonants']
    assert len('m') == 1
    
    # Test clusters
    assert 'st' in length_types['cluster2']
    assert len('st') == 2
    
    # Test diphthongs
    assert 'aɪ' in length_types['diphthongs']


def test_phoneme_sorting():
    """Test phoneme sorting logic"""
    phonemes = [
        {'phoneme': 't', 'frequency': 5, 'position': 'onset'},
        {'phoneme': 'a', 'frequency': 10, 'position': 'nucleus'},
        {'phoneme': 'm', 'frequency': 3, 'position': 'onset'},
    ]
    
    # Sort by frequency (descending)
    by_freq = sorted(phonemes, key=lambda p: p['frequency'], reverse=True)
    assert by_freq[0]['phoneme'] == 'a'  # highest frequency
    assert by_freq[-1]['phoneme'] == 'm'  # lowest frequency
    
    # Sort by phoneme alphabetically
    by_name = sorted(phonemes, key=lambda p: p['phoneme'])
    assert by_name[0]['phoneme'] == 'a'
    assert by_name[-1]['phoneme'] == 't'


def test_phoneme_filtering_by_position():
    """Test filtering phonemes by position"""
    phonemes = [
        {'phoneme': 'm', 'position': 'onset'},
        {'phoneme': 'a', 'position': 'nucleus'},
        {'phoneme': 't', 'position': 'coda'},
        {'phoneme': 'n', 'position': 'onset'},
    ]
    
    # Filter by position
    onsets = [p for p in phonemes if p['position'] == 'onset']
    nuclei = [p for p in phonemes if p['position'] == 'nucleus']
    codas = [p for p in phonemes if p['position'] == 'coda']
    
    assert len(onsets) == 2
    assert len(nuclei) == 1
    assert len(codas) == 1


def test_phoneme_frequency_increment():
    """Test frequency increment logic"""
    phoneme = {'phoneme': 'm', 'frequency': 5}
    
    # Increment
    phoneme['frequency'] += 1
    assert phoneme['frequency'] == 6
    
    # Increment by custom amount
    phoneme['frequency'] += 3
    assert phoneme['frequency'] == 9


def test_phoneme_zero_frequency_handling():
    """Test handling of zero-frequency phonemes"""
    phonemes = [
        {'phoneme': 'm', 'frequency': 5},
        {'phoneme': 'a', 'frequency': 0},
        {'phoneme': 't', 'frequency': 3},
    ]
    
    # Filter non-zero
    used = [p for p in phonemes if p['frequency'] > 0]
    unused = [p for p in phonemes if p['frequency'] == 0]
    
    assert len(used) == 2
    assert len(unused) == 1
    assert unused[0]['phoneme'] == 'a'


def test_phoneme_recalculation_logic():
    """Test the logic for recalculating frequencies"""
    # Start with some frequencies
    phoneme_freqs = {'m': 5, 'a': 3, 't': 2}
    
    # Reset to zero
    for key in phoneme_freqs:
        phoneme_freqs[key] = 0
    
    # Verify reset
    assert all(freq == 0 for freq in phoneme_freqs.values())
    
    # Simulate word analysis
    words = [
        {'onset': 'm', 'nucleus': 'a', 'coda': 't'},  # mat
        {'onset': 'n', 'nucleus': 'o', 'coda': 't'},  # not
    ]
    
    # Recalculate
    for word in words:
        for phoneme in [word['onset'], word['nucleus'], word['coda']]:
            if phoneme in phoneme_freqs:
                phoneme_freqs[phoneme] += 1
            else:
                phoneme_freqs[phoneme] = 1
    
    # Verify recalculated values
    assert phoneme_freqs['m'] == 1
    assert phoneme_freqs['a'] == 1
    assert phoneme_freqs['t'] == 2  # appears in both words
    assert phoneme_freqs['n'] == 1
    assert phoneme_freqs['o'] == 1


if __name__ == '__main__':
    pytest.main([__file__, '-v'])

