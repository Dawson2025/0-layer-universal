#!/usr/bin/env python3
# resource_id: "555cc298-56f1-463b-bdbf-919adf1f21d9"
# resource_type: "document"
# resource_name: "add_cv_to_4level"
"""
Script to add CV phonemes to the 4-level hierarchy dataset
"""

import sys
sys.path.append('.')
from flattened_dataset import flattened_dataset

def convert_cv_to_4level():
    """Convert CV phonemes from original dataset to 4-level hierarchy format"""
    
    # Extract CV phonemes from original dataset
    cv_phonemes = [p for p in flattened_dataset if p['syllable_type'] == 'CV']
    
    # Mapping for single consonants from old 2-level to new 4-level hierarchy
    consonant_mapping = {
        # Stops
        'p': {'group_type': 'Stops', 'subgroup_type': 'Bilabial', 'sub_subgroup_type': 'Voiceless', 'sub_sub_subgroup_type': 'none'},
        'b': {'group_type': 'Stops', 'subgroup_type': 'Bilabial', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'none'},
        't': {'group_type': 'Stops', 'subgroup_type': 'Alveolar', 'sub_subgroup_type': 'Voiceless', 'sub_sub_subgroup_type': 'none'},
        'd': {'group_type': 'Stops', 'subgroup_type': 'Alveolar', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'none'},
        'k': {'group_type': 'Stops', 'subgroup_type': 'Velar', 'sub_subgroup_type': 'Voiceless', 'sub_sub_subgroup_type': 'none'},
        'g': {'group_type': 'Stops', 'subgroup_type': 'Velar', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'none'},
        
        # Fricatives
        'f': {'group_type': 'Fricatives', 'subgroup_type': 'Labiodental', 'sub_subgroup_type': 'Voiceless', 'sub_sub_subgroup_type': 'none'},
        'v': {'group_type': 'Fricatives', 'subgroup_type': 'Labiodental', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'none'},
        'θ': {'group_type': 'Fricatives', 'subgroup_type': 'Dental', 'sub_subgroup_type': 'Voiceless', 'sub_sub_subgroup_type': 'none'},
        'ð': {'group_type': 'Fricatives', 'subgroup_type': 'Dental', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'none'},
        's': {'group_type': 'Fricatives', 'subgroup_type': 'Alveolar', 'sub_subgroup_type': 'Voiceless', 'sub_sub_subgroup_type': 'none'},
        'z': {'group_type': 'Fricatives', 'subgroup_type': 'Alveolar', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'none'},
        'ʃ': {'group_type': 'Fricatives', 'subgroup_type': 'Post-Alveolar', 'sub_subgroup_type': 'Voiceless', 'sub_sub_subgroup_type': 'none'},
        'ʒ': {'group_type': 'Fricatives', 'subgroup_type': 'Post-Alveolar', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'none'},
        'h': {'group_type': 'Fricatives', 'subgroup_type': 'Glottal', 'sub_subgroup_type': 'Voiceless', 'sub_sub_subgroup_type': 'none'},
        
        # Affricates
        'tʃ': {'group_type': 'Affricates', 'subgroup_type': 'Post-Alveolar', 'sub_subgroup_type': 'Voiceless', 'sub_sub_subgroup_type': 'none'},
        'dʒ': {'group_type': 'Affricates', 'subgroup_type': 'Post-Alveolar', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'none'},
        
        # Nasals
        'm': {'group_type': 'Nasals', 'subgroup_type': 'Bilabial', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'none'},
        'n': {'group_type': 'Nasals', 'subgroup_type': 'Alveolar', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'none'},
        'ŋ': {'group_type': 'Nasals', 'subgroup_type': 'Velar', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'none'},
        
        # Liquids
        'l': {'group_type': 'Liquids', 'subgroup_type': 'Alveolar', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'Lateral'},
        'ɹ': {'group_type': 'Liquids', 'subgroup_type': 'Post-Alveolar', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'Approximant'},
        'r': {'group_type': 'Liquids', 'subgroup_type': 'Alveolar', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'Trill'},
        
        # Glides
        'j': {'group_type': 'Glides', 'subgroup_type': 'Palatal', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'none'},
        'w': {'group_type': 'Glides', 'subgroup_type': 'Bilabial', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'none'},
    }
    
    # Mapping for vowels from old 2-level to new 3-level hierarchy
    vowel_mapping = {
        'i': {'group_type': 'High', 'subgroup_type': 'Front', 'sub_subgroup_type': 'Tense', 'sub_sub_subgroup_type': 'none'},
        'ɪ': {'group_type': 'High', 'subgroup_type': 'Front', 'sub_subgroup_type': 'Lax', 'sub_sub_subgroup_type': 'none'},
        'e': {'group_type': 'Mid-High', 'subgroup_type': 'Front', 'sub_subgroup_type': 'Tense', 'sub_sub_subgroup_type': 'none'},
        'ɛ': {'group_type': 'Mid', 'subgroup_type': 'Front', 'sub_subgroup_type': 'Lax', 'sub_sub_subgroup_type': 'none'},
        'æ': {'group_type': 'Mid-Low', 'subgroup_type': 'Front', 'sub_subgroup_type': 'Lax', 'sub_sub_subgroup_type': 'none'},
        'ɑ': {'group_type': 'Low', 'subgroup_type': 'Back', 'sub_subgroup_type': 'Tense', 'sub_sub_subgroup_type': 'none'},
        'ɒ': {'group_type': 'Low', 'subgroup_type': 'Back', 'sub_subgroup_type': 'Lax', 'sub_sub_subgroup_type': 'none'},
        'ɔ': {'group_type': 'Mid-Low', 'subgroup_type': 'Back', 'sub_subgroup_type': 'Tense', 'sub_sub_subgroup_type': 'none'},
        'o': {'group_type': 'Mid-High', 'subgroup_type': 'Back', 'sub_subgroup_type': 'Tense', 'sub_sub_subgroup_type': 'none'},
        'u': {'group_type': 'High', 'subgroup_type': 'Back', 'sub_subgroup_type': 'Tense', 'sub_sub_subgroup_type': 'none'},
        'ʊ': {'group_type': 'High', 'subgroup_type': 'Back', 'sub_subgroup_type': 'Lax', 'sub_sub_subgroup_type': 'none'},
        'ʌ': {'group_type': 'Mid-Low', 'subgroup_type': 'Central', 'sub_subgroup_type': 'Lax', 'sub_sub_subgroup_type': 'none'},
        'ə': {'group_type': 'Mid', 'subgroup_type': 'Central', 'sub_subgroup_type': 'Lax', 'sub_sub_subgroup_type': 'none'},
        'ɜ': {'group_type': 'Mid', 'subgroup_type': 'Central', 'sub_subgroup_type': 'Tense', 'sub_sub_subgroup_type': 'none'},
    }
    
    # Mapping for diphthongs
    diphthong_mapping = {
        'aɪ': {'group_type': 'Closing', 'subgroup_type': 'Low-to-High', 'sub_subgroup_type': 'Fronting', 'sub_sub_subgroup_type': 'none'},
        'eɪ': {'group_type': 'Closing', 'subgroup_type': 'Mid-High-to-High', 'sub_subgroup_type': 'Fronting', 'sub_sub_subgroup_type': 'none'},
        'ɔɪ': {'group_type': 'Closing', 'subgroup_type': 'Mid-to-High', 'sub_subgroup_type': 'Fronting', 'sub_sub_subgroup_type': 'none'},
        'aʊ': {'group_type': 'Closing', 'subgroup_type': 'Low-to-High', 'sub_subgroup_type': 'Backing', 'sub_sub_subgroup_type': 'none'},
        'oʊ': {'group_type': 'Closing', 'subgroup_type': 'Mid-High-to-High', 'sub_subgroup_type': 'Backing', 'sub_sub_subgroup_type': 'none'},
        'ɪə': {'group_type': 'Opening', 'subgroup_type': 'High-to-Mid', 'sub_subgroup_type': 'Centering', 'sub_sub_subgroup_type': 'none'},
        'ʊə': {'group_type': 'Opening', 'subgroup_type': 'High-to-Mid', 'sub_subgroup_type': 'Centering', 'sub_sub_subgroup_type': 'none'},
    }
    
    cv_4level = []
    
    for p in cv_phonemes:
        # Start with the base structure
        new_p = {
            'syllable_type': p['syllable_type'],
            'position': p['position'],
            'length_type': p['length_type'],
            'phoneme': p['phoneme'],
            'frequency': p['frequency']
        }
        
        # Convert based on position and length_type
        if p['position'] == 'onset':
            if p['length_type'] == 'single_consonants':
                # Use consonant mapping
                mapping = consonant_mapping.get(p['phoneme'], {
                    'group_type': p['group_type'],
                    'subgroup_type': 'Bilabial',
                    'sub_subgroup_type': p['subgroup_type'],
                    'sub_sub_subgroup_type': 'none'
                })
                new_p.update(mapping)
            else:
                # For clusters, use similar structure as CVC
                new_p.update({
                    'group_type': p['group_type'],
                    'subgroup_type': p['subgroup_type'],
                    'sub_subgroup_type': 'none',
                    'sub_sub_subgroup_type': 'none'
                })
        elif p['position'] == 'nucleus':
            if p['length_type'] == 'monophthongs':
                # Use vowel mapping
                mapping = vowel_mapping.get(p['phoneme'], {
                    'group_type': p['group_type'],
                    'subgroup_type': p['subgroup_type'],
                    'sub_subgroup_type': 'Tense',
                    'sub_sub_subgroup_type': 'none'
                })
                new_p.update(mapping)
            elif p['length_type'] == 'diphthongs':
                # Use diphthong mapping
                mapping = diphthong_mapping.get(p['phoneme'], {
                    'group_type': 'Closing',
                    'subgroup_type': 'Mid-to-High',
                    'sub_subgroup_type': 'Fronting',
                    'sub_sub_subgroup_type': 'none'
                })
                new_p.update(mapping)
        
        cv_4level.append(new_p)
    
    return cv_4level

if __name__ == '__main__':
    cv_4level = convert_cv_to_4level()
    print(f'Converted {len(cv_4level)} CV phonemes to 4-level format')
    
    # Show sample converted CV phonemes
    print('\nSample converted CV phonemes:')
    for i, p in enumerate(cv_4level[:10]):
        print(f'{i+1}. {p["syllable_type"]} {p["position"]}: {p["phoneme"]} - {p["group_type"]} - {p["subgroup_type"]} - {p["sub_subgroup_type"]} - {p["sub_sub_subgroup_type"]}')
    
    # Show breakdown by position and length_type
    print('\nBreakdown by position and length_type:')
    from collections import Counter
    breakdown = Counter((p['position'], p['length_type']) for p in cv_4level)
    for (pos, length), count in breakdown.items():
        print(f'  {pos} {length}: {count} phonemes')
