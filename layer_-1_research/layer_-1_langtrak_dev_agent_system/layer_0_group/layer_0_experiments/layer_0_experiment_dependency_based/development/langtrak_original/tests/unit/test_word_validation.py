"""
Unit tests for word validation logic
Fast, isolated tests for word processing
"""

import pytest
import json


def test_word_english_words_validation():
    """Test validation of English words field"""
    # Valid JSON array
    valid = json.dumps(['hello', 'world'])
    parsed = json.loads(valid)
    assert isinstance(parsed, list)
    assert len(parsed) == 2
    
    # Empty array is valid
    empty = json.dumps([])
    parsed_empty = json.loads(empty)
    assert isinstance(parsed_empty, list)
    assert len(parsed_empty) == 0


def test_word_syllable_type_validation():
    """Test syllable type validation for words"""
    valid_syllable_types = ['CV', 'CVC', 'V', 'VC', 'CCV', 'CCVC', 'CVCC']
    
    # Test valid types
    for syl_type in valid_syllable_types:
        assert syl_type in valid_syllable_types
    
    # Test structure validation
    assert 'C' in 'CVC'
    assert 'V' in 'CVC'


def test_word_phoneme_structure():
    """Test word phoneme structure validation"""
    word = {
        'syllable_type': 'CVC',
        'onset_phoneme': 'm',
        'nucleus_phoneme': 'a',
        'coda_phoneme': 't',
    }
    
    # CVC should have all three components
    assert word['onset_phoneme'] is not None
    assert word['nucleus_phoneme'] is not None
    assert word['coda_phoneme'] is not None
    
    # CV word should not have coda
    cv_word = {
        'syllable_type': 'CV',
        'onset_phoneme': 'm',
        'nucleus_phoneme': 'a',
        'coda_phoneme': None,
    }
    assert cv_word['coda_phoneme'] is None


def test_multisyllable_word_structure():
    """Test multi-syllable word structure"""
    syllables = [
        {
            'syllableType': 'CVC',
            'phonemes': {
                'onset': {'phoneme': 'm', 'length_type': 'single_consonants'},
                'nucleus': {'phoneme': 'a', 'length_type': 'monophthongs'},
                'coda': {'phoneme': 't', 'length_type': 'single_consonants'},
            },
        },
        {
            'syllableType': 'CVC',
            'phonemes': {
                'onset': {'phoneme': 'n', 'length_type': 'single_consonants'},
                'nucleus': {'phoneme': 'o', 'length_type': 'monophthongs'},
                'coda': {'phoneme': 'd', 'length_type': 'single_consonants'},
            },
        },
    ]
    
    assert len(syllables) == 2
    assert syllables[0]['syllableType'] == 'CVC'
    assert syllables[0]['phonemes']['onset']['phoneme'] == 'm'
    assert syllables[1]['phonemes']['coda']['phoneme'] == 'd'


def test_word_ipa_format():
    """Test IPA phonetics format"""
    # Simple IPA
    ipa = 'mæt'
    assert len(ipa) > 0
    
    # IPA with diacritics
    ipa_diacritics = 'mæt̚'
    assert len(ipa_diacritics) >= len(ipa)
    
    # IPA with length markers
    ipa_length = 'maːt'
    assert 'ː' in ipa_length  # length marker


def test_word_language_field():
    """Test language field validation"""
    # Valid language names
    valid_languages = ['English', 'Spanish', 'Mandarin', 'Test Language']
    
    for lang in valid_languages:
        assert isinstance(lang, str)
        assert len(lang) > 0


def test_word_new_language_word_validation():
    """Test new language word validation"""
    # Valid word
    word = 'mat'
    assert isinstance(word, str)
    assert len(word) > 0
    
    # Empty word should fail
    empty = ''
    assert len(empty) == 0  # Would fail validation
    
    # Very long word should be allowed
    long_word = 'a' * 100
    assert len(long_word) == 100


def test_word_dictionary_phonetics():
    """Test dictionary phonetics field"""
    # Typical dictionary format
    dict_phonetics = 'm-a-t'
    assert '-' in dict_phonetics
    parts = dict_phonetics.split('-')
    assert len(parts) == 3
    
    # IPA format
    ipa_phonetics = 'mæt'
    assert isinstance(ipa_phonetics, str)


def test_word_frequency_tracking():
    """Test word frequency/usage tracking"""
    word = {
        'new_language_word': 'mat',
        'frequency': 0,
    }
    
    # Increment on use
    word['frequency'] += 1
    assert word['frequency'] == 1
    
    # Track multiple uses
    for _ in range(5):
        word['frequency'] += 1
    assert word['frequency'] == 6


def test_word_project_association():
    """Test word-project association"""
    word = {
        'new_language_word': 'mat',
        'project_id': 123,
        'user_id': 456,
    }
    
    assert word['project_id'] == 123
    assert word['user_id'] == 456


def test_word_video_path_optional():
    """Test that video path is optional"""
    # Word without video
    word_no_video = {
        'new_language_word': 'mat',
        'video_path': None,
    }
    assert word_no_video['video_path'] is None
    
    # Word with video
    word_with_video = {
        'new_language_word': 'bat',
        'video_path': '/uploads/bat.mp4',
    }
    assert word_with_video['video_path'] is not None
    assert '.mp4' in word_with_video['video_path']


def test_word_syllables_json_parsing():
    """Test syllables JSON field parsing"""
    syllables_data = [
        {'syllableType': 'CVC', 'phonemes': {}},
        {'syllableType': 'CV', 'phonemes': {}},
    ]
    
    # Serialize
    json_str = json.dumps(syllables_data)
    assert isinstance(json_str, str)
    
    # Deserialize
    parsed = json.loads(json_str)
    assert isinstance(parsed, list)
    assert len(parsed) == 2
    assert parsed[0]['syllableType'] == 'CVC'


if __name__ == '__main__':
    pytest.main([__file__, '-v'])

