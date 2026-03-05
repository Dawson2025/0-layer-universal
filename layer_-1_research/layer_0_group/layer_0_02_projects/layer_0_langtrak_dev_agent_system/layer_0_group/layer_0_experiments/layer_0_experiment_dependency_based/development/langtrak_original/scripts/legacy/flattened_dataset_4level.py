# resource_id: "ba1cd30e-d9a5-4df5-906d-be7badf5a56a"
# resource_type: "document"
# resource_name: "flattened_dataset_4level"
# 4-Level Hierarchical Consonant Classification System
# Based on research: Manner > Place > Voicing > Additional Features

flattened_dataset = [
    # SINGLE CONSONANTS - CVC ONSET
    # STOPS
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Stops', 'subgroup_type': 'Bilabial', 'sub_subgroup_type': 'Voiceless', 'sub_sub_subgroup_type': 'none', 'phoneme': 'p', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Stops', 'subgroup_type': 'Bilabial', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'none', 'phoneme': 'b', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Stops', 'subgroup_type': 'Alveolar', 'sub_subgroup_type': 'Voiceless', 'sub_sub_subgroup_type': 'none', 'phoneme': 't', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Stops', 'subgroup_type': 'Alveolar', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'none', 'phoneme': 'd', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Stops', 'subgroup_type': 'Velar', 'sub_subgroup_type': 'Voiceless', 'sub_sub_subgroup_type': 'none', 'phoneme': 'k', 'frequency': 1},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Stops', 'subgroup_type': 'Velar', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'none', 'phoneme': 'g', 'frequency': 0},
    
    # FRICATIVES
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Fricatives', 'subgroup_type': 'Labiodental', 'sub_subgroup_type': 'Voiceless', 'sub_sub_subgroup_type': 'none', 'phoneme': 'f', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Fricatives', 'subgroup_type': 'Labiodental', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'none', 'phoneme': 'v', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Fricatives', 'subgroup_type': 'Dental', 'sub_subgroup_type': 'Voiceless', 'sub_sub_subgroup_type': 'none', 'phoneme': 'θ', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Fricatives', 'subgroup_type': 'Dental', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'none', 'phoneme': 'ð', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Fricatives', 'subgroup_type': 'Alveolar', 'sub_subgroup_type': 'Voiceless', 'sub_sub_subgroup_type': 'none', 'phoneme': 's', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Fricatives', 'subgroup_type': 'Alveolar', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'none', 'phoneme': 'z', 'frequency': 1},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Fricatives', 'subgroup_type': 'Post-Alveolar', 'sub_subgroup_type': 'Voiceless', 'sub_sub_subgroup_type': 'none', 'phoneme': 'ʃ', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Fricatives', 'subgroup_type': 'Post-Alveolar', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'none', 'phoneme': 'ʒ', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Fricatives', 'subgroup_type': 'Glottal', 'sub_subgroup_type': 'Voiceless', 'sub_sub_subgroup_type': 'none', 'phoneme': 'h', 'frequency': 0},
    
    # AFFRICATES
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Affricates', 'subgroup_type': 'Post-Alveolar', 'sub_subgroup_type': 'Voiceless', 'sub_sub_subgroup_type': 'none', 'phoneme': 'tʃ', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Affricates', 'subgroup_type': 'Post-Alveolar', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'none', 'phoneme': 'dʒ', 'frequency': 0},
    
    # NASALS
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Nasals', 'subgroup_type': 'Bilabial', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'none', 'phoneme': 'm', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Nasals', 'subgroup_type': 'Alveolar', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'none', 'phoneme': 'n', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Nasals', 'subgroup_type': 'Velar', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'none', 'phoneme': 'ŋ', 'frequency': 0},
    
    # LIQUIDS/APPROXIMANTS
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Liquids', 'subgroup_type': 'Alveolar', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'Lateral', 'phoneme': 'l', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Liquids', 'subgroup_type': 'Post-Alveolar', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'Approximant', 'phoneme': 'ɹ', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Liquids', 'subgroup_type': 'Alveolar', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'Trill', 'phoneme': 'r', 'frequency': 0},
    
    # GLIDES
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Glides', 'subgroup_type': 'Palatal', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'none', 'phoneme': 'j', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Glides', 'subgroup_type': 'Bilabial', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'none', 'phoneme': 'w', 'frequency': 1},
    
    # CVC CODA CONSONANTS
    # STOPS
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Stops', 'subgroup_type': 'Bilabial', 'sub_subgroup_type': 'Voiceless', 'sub_sub_subgroup_type': 'none', 'phoneme': 'p', 'frequency': 1},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Stops', 'subgroup_type': 'Bilabial', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'none', 'phoneme': 'b', 'frequency': 1},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Stops', 'subgroup_type': 'Alveolar', 'sub_subgroup_type': 'Voiceless', 'sub_sub_subgroup_type': 'none', 'phoneme': 't', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Stops', 'subgroup_type': 'Alveolar', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'none', 'phoneme': 'd', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Stops', 'subgroup_type': 'Velar', 'sub_subgroup_type': 'Voiceless', 'sub_sub_subgroup_type': 'none', 'phoneme': 'k', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Stops', 'subgroup_type': 'Velar', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'none', 'phoneme': 'g', 'frequency': 0},
    
    # FRICATIVES
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Fricatives', 'subgroup_type': 'Labiodental', 'sub_subgroup_type': 'Voiceless', 'sub_sub_subgroup_type': 'none', 'phoneme': 'f', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Fricatives', 'subgroup_type': 'Labiodental', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'none', 'phoneme': 'v', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Fricatives', 'subgroup_type': 'Dental', 'sub_subgroup_type': 'Voiceless', 'sub_sub_subgroup_type': 'none', 'phoneme': 'θ', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Fricatives', 'subgroup_type': 'Dental', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'none', 'phoneme': 'ð', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Fricatives', 'subgroup_type': 'Alveolar', 'sub_subgroup_type': 'Voiceless', 'sub_sub_subgroup_type': 'none', 'phoneme': 's', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Fricatives', 'subgroup_type': 'Alveolar', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'none', 'phoneme': 'z', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Fricatives', 'subgroup_type': 'Post-Alveolar', 'sub_subgroup_type': 'Voiceless', 'sub_sub_subgroup_type': 'none', 'phoneme': 'ʃ', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Fricatives', 'subgroup_type': 'Post-Alveolar', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'none', 'phoneme': 'ʒ', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Fricatives', 'subgroup_type': 'Glottal', 'sub_subgroup_type': 'Voiceless', 'sub_sub_subgroup_type': 'none', 'phoneme': 'h', 'frequency': 0},
    
    # AFFRICATES
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Affricates', 'subgroup_type': 'Post-Alveolar', 'sub_subgroup_type': 'Voiceless', 'sub_sub_subgroup_type': 'none', 'phoneme': 'tʃ', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Affricates', 'subgroup_type': 'Post-Alveolar', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'none', 'phoneme': 'dʒ', 'frequency': 0},
    
    # NASALS
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Nasals', 'subgroup_type': 'Bilabial', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'none', 'phoneme': 'm', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Nasals', 'subgroup_type': 'Alveolar', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'none', 'phoneme': 'n', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Nasals', 'subgroup_type': 'Velar', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'none', 'phoneme': 'ŋ', 'frequency': 0},
    
    # LIQUIDS/APPROXIMANTS
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Liquids', 'subgroup_type': 'Alveolar', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'Lateral', 'phoneme': 'l', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Liquids', 'subgroup_type': 'Post-Alveolar', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'Approximant', 'phoneme': 'ɹ', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Liquids', 'subgroup_type': 'Alveolar', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'Trill', 'phoneme': 'r', 'frequency': 0},
    
    # GLIDES
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Glides', 'subgroup_type': 'Palatal', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'none', 'phoneme': 'j', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Glides', 'subgroup_type': 'Bilabial', 'sub_subgroup_type': 'Voiced', 'sub_sub_subgroup_type': 'none', 'phoneme': 'w', 'frequency': 0},
    
    # VOWELS - CVC NUCLEUS
    # MONOPHTHONGS
    {'syllable_type': 'CVC', 'position': 'nucleus', 'length_type': 'monophthongs', 'group_type': 'High', 'subgroup_type': 'Front', 'sub_subgroup_type': 'Tense', 'sub_sub_subgroup_type': 'none', 'phoneme': 'i', 'frequency': 1},
    {'syllable_type': 'CVC', 'position': 'nucleus', 'length_type': 'monophthongs', 'group_type': 'High', 'subgroup_type': 'Front', 'sub_subgroup_type': 'Lax', 'sub_sub_subgroup_type': 'none', 'phoneme': 'ɪ', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'nucleus', 'length_type': 'monophthongs', 'group_type': 'High', 'subgroup_type': 'Back', 'sub_subgroup_type': 'Tense', 'sub_sub_subgroup_type': 'none', 'phoneme': 'u', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'nucleus', 'length_type': 'monophthongs', 'group_type': 'High', 'subgroup_type': 'Back', 'sub_subgroup_type': 'Lax', 'sub_sub_subgroup_type': 'none', 'phoneme': 'ʊ', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'nucleus', 'length_type': 'monophthongs', 'group_type': 'Mid-High', 'subgroup_type': 'Front', 'sub_subgroup_type': 'Tense', 'sub_sub_subgroup_type': 'none', 'phoneme': 'e', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'nucleus', 'length_type': 'monophthongs', 'group_type': 'Mid-High', 'subgroup_type': 'Back', 'sub_subgroup_type': 'Tense', 'sub_sub_subgroup_type': 'none', 'phoneme': 'o', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'nucleus', 'length_type': 'monophthongs', 'group_type': 'Mid', 'subgroup_type': 'Front', 'sub_subgroup_type': 'Lax', 'sub_sub_subgroup_type': 'none', 'phoneme': 'ɛ', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'nucleus', 'length_type': 'monophthongs', 'group_type': 'Mid', 'subgroup_type': 'Central', 'sub_subgroup_type': 'Lax', 'sub_sub_subgroup_type': 'none', 'phoneme': 'ə', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'nucleus', 'length_type': 'monophthongs', 'group_type': 'Mid', 'subgroup_type': 'Back', 'sub_subgroup_type': 'Lax', 'sub_sub_subgroup_type': 'none', 'phoneme': 'ɔ', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'nucleus', 'length_type': 'monophthongs', 'group_type': 'Mid-Low', 'subgroup_type': 'Front', 'sub_subgroup_type': 'Lax', 'sub_sub_subgroup_type': 'none', 'phoneme': 'æ', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'nucleus', 'length_type': 'monophthongs', 'group_type': 'Mid-Low', 'subgroup_type': 'Central', 'sub_subgroup_type': 'Lax', 'sub_sub_subgroup_type': 'none', 'phoneme': 'ʌ', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'nucleus', 'length_type': 'monophthongs', 'group_type': 'Low', 'subgroup_type': 'Central', 'sub_subgroup_type': 'Lax', 'sub_sub_subgroup_type': 'none', 'phoneme': 'a', 'frequency': 1},
    {'syllable_type': 'CVC', 'position': 'nucleus', 'length_type': 'monophthongs', 'group_type': 'Low', 'subgroup_type': 'Back', 'sub_subgroup_type': 'Lax', 'sub_sub_subgroup_type': 'none', 'phoneme': 'ɑ', 'frequency': 0},
    
    # DIPHTHONGS
    {'syllable_type': 'CVC', 'position': 'nucleus', 'length_type': 'diphthongs', 'group_type': 'Closing', 'subgroup_type': 'Low-to-High', 'sub_subgroup_type': 'Fronting', 'sub_sub_subgroup_type': 'none', 'phoneme': 'aɪ', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'nucleus', 'length_type': 'diphthongs', 'group_type': 'Closing', 'subgroup_type': 'Mid-High-to-High', 'sub_subgroup_type': 'Fronting', 'sub_sub_subgroup_type': 'none', 'phoneme': 'eɪ', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'nucleus', 'length_type': 'diphthongs', 'group_type': 'Closing', 'subgroup_type': 'Low-to-High', 'sub_subgroup_type': 'Backing', 'sub_sub_subgroup_type': 'none', 'phoneme': 'aʊ', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'nucleus', 'length_type': 'diphthongs', 'group_type': 'Closing', 'subgroup_type': 'Mid-High-to-High', 'sub_subgroup_type': 'Backing', 'sub_sub_subgroup_type': 'none', 'phoneme': 'oʊ', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'nucleus', 'length_type': 'diphthongs', 'group_type': 'Closing', 'subgroup_type': 'Mid-to-High', 'sub_subgroup_type': 'Fronting', 'sub_sub_subgroup_type': 'none', 'phoneme': 'ɔɪ', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'nucleus', 'length_type': 'diphthongs', 'group_type': 'Opening', 'subgroup_type': 'High-to-Mid', 'sub_subgroup_type': 'Centering', 'sub_sub_subgroup_type': 'none', 'phoneme': 'ɪə', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'nucleus', 'length_type': 'diphthongs', 'group_type': 'Opening', 'subgroup_type': 'High-to-Mid', 'sub_subgroup_type': 'Centering', 'sub_sub_subgroup_type': 'none', 'phoneme': 'ʊə', 'frequency': 0},
    
    # CONSONANT CLUSTERS - CVC ONSET
    # 2-CONSONANT CLUSTERS
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'cluster2', 'group_type': 'Stop+', 'subgroup_type': 'Stop+Liquid', 'sub_subgroup_type': 'Bilabial+Lateral', 'sub_sub_subgroup_type': 'none', 'phoneme': 'pl', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'cluster2', 'group_type': 'Stop+', 'subgroup_type': 'Stop+Liquid', 'sub_subgroup_type': 'Bilabial+Lateral', 'sub_sub_subgroup_type': 'none', 'phoneme': 'bl', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'cluster2', 'group_type': 'Stop+', 'subgroup_type': 'Stop+Liquid', 'sub_subgroup_type': 'Velar+Lateral', 'sub_sub_subgroup_type': 'none', 'phoneme': 'kl', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'cluster2', 'group_type': 'Stop+', 'subgroup_type': 'Stop+Liquid', 'sub_subgroup_type': 'Velar+Lateral', 'sub_sub_subgroup_type': 'none', 'phoneme': 'gl', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'cluster2', 'group_type': 'Stop+', 'subgroup_type': 'Stop+Glide', 'sub_subgroup_type': 'Bilabial+Palatal', 'sub_sub_subgroup_type': 'none', 'phoneme': 'pj', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'cluster2', 'group_type': 'Stop+', 'subgroup_type': 'Stop+Glide', 'sub_subgroup_type': 'Velar+Palatal', 'sub_sub_subgroup_type': 'none', 'phoneme': 'kj', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'cluster2', 'group_type': 'Fricative+', 'subgroup_type': 'Fricative+Liquid', 'sub_subgroup_type': 'Labiodental+Lateral', 'sub_sub_subgroup_type': 'none', 'phoneme': 'fl', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'cluster2', 'group_type': 'S+', 'subgroup_type': 'S+Stop', 'sub_subgroup_type': 'Alveolar+Alveolar', 'sub_sub_subgroup_type': 'none', 'phoneme': 'st', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'cluster2', 'group_type': 'S+', 'subgroup_type': 'S+Stop', 'sub_subgroup_type': 'Alveolar+Bilabial', 'sub_sub_subgroup_type': 'none', 'phoneme': 'sp', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'cluster2', 'group_type': 'S+', 'subgroup_type': 'S+Stop', 'sub_subgroup_type': 'Alveolar+Velar', 'sub_sub_subgroup_type': 'none', 'phoneme': 'sk', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'cluster2', 'group_type': 'S+', 'subgroup_type': 'S+Nasal', 'sub_subgroup_type': 'Alveolar+Alveolar', 'sub_sub_subgroup_type': 'none', 'phoneme': 'sn', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'cluster2', 'group_type': 'S+', 'subgroup_type': 'S+Nasal', 'sub_subgroup_type': 'Alveolar+Bilabial', 'sub_sub_subgroup_type': 'none', 'phoneme': 'sm', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'cluster2', 'group_type': 'S+', 'subgroup_type': 'S+Liquid', 'sub_subgroup_type': 'Alveolar+Lateral', 'sub_sub_subgroup_type': 'none', 'phoneme': 'sl', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'cluster2', 'group_type': 'S+', 'subgroup_type': 'S+Glide', 'sub_subgroup_type': 'Alveolar+Bilabial', 'sub_sub_subgroup_type': 'none', 'phoneme': 'sw', 'frequency': 0},
    
    # 3-CONSONANT CLUSTERS
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'cluster3', 'group_type': 'S+Stop+', 'subgroup_type': 'S+Stop+Liquid', 'sub_subgroup_type': 'Alveolar+Bilabial+Lateral', 'sub_sub_subgroup_type': 'none', 'phoneme': 'spl', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'cluster3', 'group_type': 'S+Stop+', 'subgroup_type': 'S+Stop+Liquid', 'sub_subgroup_type': 'Alveolar+Alveolar+Post-Alveolar', 'sub_sub_subgroup_type': 'none', 'phoneme': 'str', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'cluster3', 'group_type': 'S+Stop+', 'subgroup_type': 'S+Stop+Liquid', 'sub_subgroup_type': 'Alveolar+Velar+Post-Alveolar', 'sub_sub_subgroup_type': 'none', 'phoneme': 'skr', 'frequency': 0},
    
    # CONSONANT CLUSTERS - CVC CODA
    # 2-CONSONANT CLUSTERS
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'cluster2', 'group_type': 'Nasal+', 'subgroup_type': 'Nasal+Stop', 'sub_subgroup_type': 'Alveolar+Alveolar', 'sub_sub_subgroup_type': 'none', 'phoneme': 'nt', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'cluster2', 'group_type': 'Nasal+', 'subgroup_type': 'Nasal+Stop', 'sub_subgroup_type': 'Bilabial+Bilabial', 'sub_sub_subgroup_type': 'none', 'phoneme': 'mp', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'cluster2', 'group_type': 'Nasal+', 'subgroup_type': 'Nasal+Stop', 'sub_subgroup_type': 'Velar+Velar', 'sub_sub_subgroup_type': 'none', 'phoneme': 'nk', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'cluster2', 'group_type': 'Stop+', 'subgroup_type': 'Stop+Liquid', 'sub_subgroup_type': 'Alveolar+Lateral', 'sub_sub_subgroup_type': 'none', 'phoneme': 'dl', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'cluster2', 'group_type': 'Liquid+', 'subgroup_type': 'Liquid+Stop', 'sub_subgroup_type': 'Lateral+Alveolar', 'sub_sub_subgroup_type': 'none', 'phoneme': 'lt', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'cluster2', 'group_type': 'Liquid+', 'subgroup_type': 'Liquid+Stop', 'sub_subgroup_type': 'Post-Alveolar+Alveolar', 'sub_sub_subgroup_type': 'none', 'phoneme': 'rd', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'cluster2', 'group_type': 'Fricative+', 'subgroup_type': 'Fricative+Stop', 'sub_subgroup_type': 'Labiodental+Alveolar', 'sub_sub_subgroup_type': 'none', 'phoneme': 'ft', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'cluster2', 'group_type': 'Fricative+', 'subgroup_type': 'Fricative+Stop', 'sub_subgroup_type': 'Alveolar+Bilabial', 'sub_sub_subgroup_type': 'none', 'phoneme': 'sp', 'frequency': 0},
]
