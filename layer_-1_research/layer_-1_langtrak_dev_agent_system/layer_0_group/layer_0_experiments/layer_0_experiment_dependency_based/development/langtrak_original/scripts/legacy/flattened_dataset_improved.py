flattened_dataset = [
    # CVC Onset Single Consonants - Stops with Voicing and Place of Articulation
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Stops', 'subgroup_type': 'Voiceless', 'phoneme': 'p', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Stops', 'subgroup_type': 'Voiceless', 'phoneme': 't', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Stops', 'subgroup_type': 'Voiceless', 'phoneme': 'k', 'frequency': 1},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Stops', 'subgroup_type': 'Voiced', 'phoneme': 'b', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Stops', 'subgroup_type': 'Voiced', 'phoneme': 'd', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Stops', 'subgroup_type': 'Voiced', 'phoneme': 'g', 'frequency': 0},
    
    # CVC Onset Single Consonants - Fricatives with Voicing
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Fricatives', 'subgroup_type': 'Voiceless', 'phoneme': 'f', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Fricatives', 'subgroup_type': 'Voiced', 'phoneme': 'v', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Fricatives', 'subgroup_type': 'Voiceless', 'phoneme': 's', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Fricatives', 'subgroup_type': 'Voiced', 'phoneme': 'z', 'frequency': 1},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Fricatives', 'subgroup_type': 'Voiceless', 'phoneme': 'ʃ', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Fricatives', 'subgroup_type': 'Voiced', 'phoneme': 'ʒ', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Fricatives', 'subgroup_type': 'Voiceless', 'phoneme': 'θ', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Fricatives', 'subgroup_type': 'Voiced', 'phoneme': 'ð', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Fricatives', 'subgroup_type': 'Voiceless', 'phoneme': 'h', 'frequency': 0},
    
    # CVC Onset Single Consonants - Affricates with Voicing
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Affricates', 'subgroup_type': 'Voiceless', 'phoneme': 'tʃ', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Affricates', 'subgroup_type': 'Voiced', 'phoneme': 'dʒ', 'frequency': 0},
    
    # CVC Onset Single Consonants - Nasals
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Nasals', 'subgroup_type': 'none', 'phoneme': 'm', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Nasals', 'subgroup_type': 'none', 'phoneme': 'n', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Nasals', 'subgroup_type': 'none', 'phoneme': 'ŋ', 'frequency': 0},
    
    # CVC Onset Single Consonants - Liquids
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Liquids', 'subgroup_type': 'none', 'phoneme': 'l', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Liquids', 'subgroup_type': 'none', 'phoneme': 'ɹ', 'frequency': 0},
    
    # CVC Onset Single Consonants - Glides
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Glides', 'subgroup_type': 'none', 'phoneme': 'j', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Glides', 'subgroup_type': 'none', 'phoneme': 'w', 'frequency': 1},
    
    # CVC Onset Clusters (keeping existing structure)
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'cluster2', 'group_type': 'Stop+', 'subgroup_type': 'Stop+Liquid', 'phoneme': 'pl', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'cluster2', 'group_type': 'Stop+', 'subgroup_type': 'Stop+Liquid', 'phoneme': 'bl', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'cluster2', 'group_type': 'Stop+', 'subgroup_type': 'Stop+Liquid', 'phoneme': 'kl', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'cluster2', 'group_type': 'Stop+', 'subgroup_type': 'Stop+Liquid', 'phoneme': 'gl', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'cluster2', 'group_type': 'Stop+', 'subgroup_type': 'Stop+Glide', 'phoneme': 'pj', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'cluster2', 'group_type': 'Stop+', 'subgroup_type': 'Stop+Glide', 'phoneme': 'kj', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'cluster2', 'group_type': 'Fricative+', 'subgroup_type': 'Fricative+Liquid', 'phoneme': 'fl', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'cluster2', 'group_type': 'S+', 'subgroup_type': 'S+Stop', 'phoneme': 'st', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'cluster2', 'group_type': 'S+', 'subgroup_type': 'S+Stop', 'phoneme': 'sp', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'cluster2', 'group_type': 'S+', 'subgroup_type': 'S+Stop', 'phoneme': 'sk', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'cluster2', 'group_type': 'S+', 'subgroup_type': 'S+Nasal', 'phoneme': 'sn', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'cluster2', 'group_type': 'S+', 'subgroup_type': 'S+Nasal', 'phoneme': 'sm', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'cluster2', 'group_type': 'S+', 'subgroup_type': 'S+Liquid', 'phoneme': 'sl', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'cluster2', 'group_type': 'S+', 'subgroup_type': 'S+Glide', 'phoneme': 'sw', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'cluster3', 'group_type': 'S+Stop+', 'subgroup_type': 'S+Stop+Liquid', 'phoneme': 'spl', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'cluster3', 'group_type': 'S+Stop+', 'subgroup_type': 'S+Stop+Liquid', 'phoneme': 'str', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'cluster3', 'group_type': 'S+Stop+', 'subgroup_type': 'S+Stop+Liquid', 'phoneme': 'skr', 'frequency': 0},
    
    # CVC Nucleus Monophthongs - Enhanced classification
    {'syllable_type': 'CVC', 'position': 'nucleus', 'length_type': 'monophthongs', 'group_type': 'High', 'subgroup_type': 'Front', 'phoneme': 'i', 'frequency': 1},
    {'syllable_type': 'CVC', 'position': 'nucleus', 'length_type': 'monophthongs', 'group_type': 'High', 'subgroup_type': 'Front', 'phoneme': 'ɪ', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'nucleus', 'length_type': 'monophthongs', 'group_type': 'High', 'subgroup_type': 'Back', 'phoneme': 'u', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'nucleus', 'length_type': 'monophthongs', 'group_type': 'High', 'subgroup_type': 'Back', 'phoneme': 'ʊ', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'nucleus', 'length_type': 'monophthongs', 'group_type': 'Mid-High', 'subgroup_type': 'Front', 'phoneme': 'e', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'nucleus', 'length_type': 'monophthongs', 'group_type': 'Mid-High', 'subgroup_type': 'Back', 'phoneme': 'o', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'nucleus', 'length_type': 'monophthongs', 'group_type': 'Mid', 'subgroup_type': 'Front', 'phoneme': 'ɛ', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'nucleus', 'length_type': 'monophthongs', 'group_type': 'Mid', 'subgroup_type': 'Central', 'phoneme': 'ə', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'nucleus', 'length_type': 'monophthongs', 'group_type': 'Mid', 'subgroup_type': 'Back', 'phoneme': 'ɔ', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'nucleus', 'length_type': 'monophthongs', 'group_type': 'Mid-Low', 'subgroup_type': 'Front', 'phoneme': 'æ', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'nucleus', 'length_type': 'monophthongs', 'group_type': 'Low', 'subgroup_type': 'Central', 'phoneme': 'a', 'frequency': 1},
    {'syllable_type': 'CVC', 'position': 'nucleus', 'length_type': 'monophthongs', 'group_type': 'Low', 'subgroup_type': 'Back', 'phoneme': 'ɑ', 'frequency': 0},
    
    # CVC Nucleus Diphthongs - Enhanced classification
    {'syllable_type': 'CVC', 'position': 'nucleus', 'length_type': 'diphthongs', 'group_type': 'Closing', 'subgroup_type': 'High-to-Mid Fronting', 'phoneme': 'aɪ', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'nucleus', 'length_type': 'diphthongs', 'group_type': 'Closing', 'subgroup_type': 'High-to-Mid Fronting', 'phoneme': 'eɪ', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'nucleus', 'length_type': 'diphthongs', 'group_type': 'Closing', 'subgroup_type': 'Mid-to-High Fronting', 'phoneme': 'ɔɪ', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'nucleus', 'length_type': 'diphthongs', 'group_type': 'Closing', 'subgroup_type': 'High-to-Mid Backing', 'phoneme': 'aʊ', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'nucleus', 'length_type': 'diphthongs', 'group_type': 'Closing', 'subgroup_type': 'High-to-Mid Backing', 'phoneme': 'oʊ', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'nucleus', 'length_type': 'diphthongs', 'group_type': 'Centering', 'subgroup_type': 'High-to-Central', 'phoneme': 'ɪə', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'nucleus', 'length_type': 'diphthongs', 'group_type': 'Centering', 'subgroup_type': 'High-to-Central', 'phoneme': 'ʊə', 'frequency': 0},
    
    # CVC Coda Single Consonants - Stops with Voicing
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Stops', 'subgroup_type': 'Voiceless', 'phoneme': 'p', 'frequency': 1},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Stops', 'subgroup_type': 'Voiceless', 'phoneme': 't', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Stops', 'subgroup_type': 'Voiceless', 'phoneme': 'k', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Stops', 'subgroup_type': 'Voiced', 'phoneme': 'b', 'frequency': 1},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Stops', 'subgroup_type': 'Voiced', 'phoneme': 'd', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Stops', 'subgroup_type': 'Voiced', 'phoneme': 'g', 'frequency': 0},
    
    # CVC Coda Single Consonants - Fricatives with Voicing
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Fricatives', 'subgroup_type': 'Voiceless', 'phoneme': 'f', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Fricatives', 'subgroup_type': 'Voiced', 'phoneme': 'v', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Fricatives', 'subgroup_type': 'Voiceless', 'phoneme': 's', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Fricatives', 'subgroup_type': 'Voiced', 'phoneme': 'z', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Fricatives', 'subgroup_type': 'Voiceless', 'phoneme': 'ʃ', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Fricatives', 'subgroup_type': 'Voiced', 'phoneme': 'ʒ', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Fricatives', 'subgroup_type': 'Voiceless', 'phoneme': 'θ', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Fricatives', 'subgroup_type': 'Voiced', 'phoneme': 'ð', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Fricatives', 'subgroup_type': 'Voiceless', 'phoneme': 'h', 'frequency': 0},
    
    # CVC Coda Single Consonants - Affricates with Voicing
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Affricates', 'subgroup_type': 'Voiceless', 'phoneme': 'tʃ', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Affricates', 'subgroup_type': 'Voiced', 'phoneme': 'dʒ', 'frequency': 0},
    
    # CVC Coda Single Consonants - Nasals
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Nasals', 'subgroup_type': 'none', 'phoneme': 'm', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Nasals', 'subgroup_type': 'none', 'phoneme': 'n', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Nasals', 'subgroup_type': 'none', 'phoneme': 'ŋ', 'frequency': 0},
    
    # CVC Coda Single Consonants - Liquids
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Liquids', 'subgroup_type': 'none', 'phoneme': 'l', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Liquids', 'subgroup_type': 'none', 'phoneme': 'ɹ', 'frequency': 0},
    
    # CVC Coda Single Consonants - Glides
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Glides', 'subgroup_type': 'none', 'phoneme': 'j', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'single_consonants', 'group_type': 'Glides', 'subgroup_type': 'none', 'phoneme': 'w', 'frequency': 0},
    
    # CVC Coda Clusters (fixing terminology)
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'cluster2', 'group_type': 'Nasal+', 'subgroup_type': 'Nasal+Stop', 'phoneme': 'nt', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'cluster2', 'group_type': 'Nasal+', 'subgroup_type': 'Nasal+Stop', 'phoneme': 'mp', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'cluster2', 'group_type': 'Nasal+', 'subgroup_type': 'Nasal+Stop', 'phoneme': 'nk', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'cluster2', 'group_type': 'Stop+', 'subgroup_type': 'Stop+Liquid', 'phoneme': 'dl', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'cluster2', 'group_type': 'Liquid+', 'subgroup_type': 'Liquid+Stop', 'phoneme': 'lt', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'cluster2', 'group_type': 'Liquid+', 'subgroup_type': 'Liquid+Stop', 'phoneme': 'rd', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'cluster2', 'group_type': 'Fricative+', 'subgroup_type': 'Fricative+Stop', 'phoneme': 'ft', 'frequency': 0},
    {'syllable_type': 'CVC', 'position': 'coda', 'length_type': 'cluster2', 'group_type': 'Fricative+', 'subgroup_type': 'Fricative+Stop', 'phoneme': 'sp', 'frequency': 0},
    
    # CV Onset Single Consonants - Stops with Voicing
    {'syllable_type': 'CV', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Stops', 'subgroup_type': 'Voiceless', 'phoneme': 'p', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Stops', 'subgroup_type': 'Voiceless', 'phoneme': 't', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Stops', 'subgroup_type': 'Voiceless', 'phoneme': 'k', 'frequency': 1},
    {'syllable_type': 'CV', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Stops', 'subgroup_type': 'Voiced', 'phoneme': 'b', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Stops', 'subgroup_type': 'Voiced', 'phoneme': 'd', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Stops', 'subgroup_type': 'Voiced', 'phoneme': 'g', 'frequency': 0},
    
    # CV Onset Single Consonants - Fricatives with Voicing
    {'syllable_type': 'CV', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Fricatives', 'subgroup_type': 'Voiceless', 'phoneme': 'f', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Fricatives', 'subgroup_type': 'Voiced', 'phoneme': 'v', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Fricatives', 'subgroup_type': 'Voiceless', 'phoneme': 's', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Fricatives', 'subgroup_type': 'Voiced', 'phoneme': 'z', 'frequency': 1},
    {'syllable_type': 'CV', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Fricatives', 'subgroup_type': 'Voiceless', 'phoneme': 'ʃ', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Fricatives', 'subgroup_type': 'Voiced', 'phoneme': 'ʒ', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Fricatives', 'subgroup_type': 'Voiceless', 'phoneme': 'θ', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Fricatives', 'subgroup_type': 'Voiced', 'phoneme': 'ð', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Fricatives', 'subgroup_type': 'Voiceless', 'phoneme': 'h', 'frequency': 0},
    
    # CV Onset Single Consonants - Affricates with Voicing
    {'syllable_type': 'CV', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Affricates', 'subgroup_type': 'Voiceless', 'phoneme': 'tʃ', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Affricates', 'subgroup_type': 'Voiced', 'phoneme': 'dʒ', 'frequency': 0},
    
    # CV Onset Single Consonants - Nasals
    {'syllable_type': 'CV', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Nasals', 'subgroup_type': 'none', 'phoneme': 'm', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Nasals', 'subgroup_type': 'none', 'phoneme': 'n', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Nasals', 'subgroup_type': 'none', 'phoneme': 'ŋ', 'frequency': 0},
    
    # CV Onset Single Consonants - Liquids
    {'syllable_type': 'CV', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Liquids', 'subgroup_type': 'none', 'phoneme': 'l', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Liquids', 'subgroup_type': 'none', 'phoneme': 'ɹ', 'frequency': 0},
    
    # CV Onset Single Consonants - Glides
    {'syllable_type': 'CV', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Glides', 'subgroup_type': 'none', 'phoneme': 'j', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Glides', 'subgroup_type': 'none', 'phoneme': 'w', 'frequency': 1},
    
    # CV Onset Clusters (keeping existing structure)
    {'syllable_type': 'CV', 'position': 'onset', 'length_type': 'cluster2', 'group_type': 'Stop+', 'subgroup_type': 'Stop+Liquid', 'phoneme': 'pl', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'onset', 'length_type': 'cluster2', 'group_type': 'Stop+', 'subgroup_type': 'Stop+Liquid', 'phoneme': 'bl', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'onset', 'length_type': 'cluster2', 'group_type': 'Stop+', 'subgroup_type': 'Stop+Liquid', 'phoneme': 'kl', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'onset', 'length_type': 'cluster2', 'group_type': 'Stop+', 'subgroup_type': 'Stop+Liquid', 'phoneme': 'gl', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'onset', 'length_type': 'cluster2', 'group_type': 'Stop+', 'subgroup_type': 'Stop+Glide', 'phoneme': 'pj', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'onset', 'length_type': 'cluster2', 'group_type': 'Stop+', 'subgroup_type': 'Stop+Glide', 'phoneme': 'kj', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'onset', 'length_type': 'cluster2', 'group_type': 'Fricative+', 'subgroup_type': 'Fricative+Liquid', 'phoneme': 'fl', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'onset', 'length_type': 'cluster2', 'group_type': 'S+', 'subgroup_type': 'S+Stop', 'phoneme': 'st', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'onset', 'length_type': 'cluster2', 'group_type': 'S+', 'subgroup_type': 'S+Stop', 'phoneme': 'sp', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'onset', 'length_type': 'cluster2', 'group_type': 'S+', 'subgroup_type': 'S+Stop', 'phoneme': 'sk', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'onset', 'length_type': 'cluster2', 'group_type': 'S+', 'subgroup_type': 'S+Nasal', 'phoneme': 'sn', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'onset', 'length_type': 'cluster2', 'group_type': 'S+', 'subgroup_type': 'S+Nasal', 'phoneme': 'sm', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'onset', 'length_type': 'cluster2', 'group_type': 'S+', 'subgroup_type': 'S+Liquid', 'phoneme': 'sl', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'onset', 'length_type': 'cluster2', 'group_type': 'S+', 'subgroup_type': 'S+Glide', 'phoneme': 'sw', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'onset', 'length_type': 'cluster3', 'group_type': 'S+Stop+', 'subgroup_type': 'S+Stop+Liquid', 'phoneme': 'spl', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'onset', 'length_type': 'cluster3', 'group_type': 'S+Stop+', 'subgroup_type': 'S+Stop+Liquid', 'phoneme': 'str', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'onset', 'length_type': 'cluster3', 'group_type': 'S+Stop+', 'subgroup_type': 'S+Stop+Liquid', 'phoneme': 'skr', 'frequency': 0},
    
    # CV Nucleus Monophthongs - Enhanced classification
    {'syllable_type': 'CV', 'position': 'nucleus', 'length_type': 'monophthongs', 'group_type': 'High', 'subgroup_type': 'Front', 'phoneme': 'i', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'nucleus', 'length_type': 'monophthongs', 'group_type': 'High', 'subgroup_type': 'Front', 'phoneme': 'ɪ', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'nucleus', 'length_type': 'monophthongs', 'group_type': 'High', 'subgroup_type': 'Back', 'phoneme': 'u', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'nucleus', 'length_type': 'monophthongs', 'group_type': 'High', 'subgroup_type': 'Back', 'phoneme': 'ʊ', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'nucleus', 'length_type': 'monophthongs', 'group_type': 'Mid-High', 'subgroup_type': 'Front', 'phoneme': 'e', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'nucleus', 'length_type': 'monophthongs', 'group_type': 'Mid-High', 'subgroup_type': 'Back', 'phoneme': 'o', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'nucleus', 'length_type': 'monophthongs', 'group_type': 'Mid', 'subgroup_type': 'Front', 'phoneme': 'ɛ', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'nucleus', 'length_type': 'monophthongs', 'group_type': 'Mid', 'subgroup_type': 'Central', 'phoneme': 'ə', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'nucleus', 'length_type': 'monophthongs', 'group_type': 'Mid', 'subgroup_type': 'Back', 'phoneme': 'ɔ', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'nucleus', 'length_type': 'monophthongs', 'group_type': 'Mid-Low', 'subgroup_type': 'Front', 'phoneme': 'æ', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'nucleus', 'length_type': 'monophthongs', 'group_type': 'Low', 'subgroup_type': 'Central', 'phoneme': 'a', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'nucleus', 'length_type': 'monophthongs', 'group_type': 'Low', 'subgroup_type': 'Back', 'phoneme': 'ɑ', 'frequency': 0},
    
    # CV Nucleus Diphthongs - Enhanced classification
    {'syllable_type': 'CV', 'position': 'nucleus', 'length_type': 'diphthongs', 'group_type': 'Closing', 'subgroup_type': 'High-to-Mid Fronting', 'phoneme': 'aɪ', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'nucleus', 'length_type': 'diphthongs', 'group_type': 'Closing', 'subgroup_type': 'High-to-Mid Fronting', 'phoneme': 'eɪ', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'nucleus', 'length_type': 'diphthongs', 'group_type': 'Closing', 'subgroup_type': 'Mid-to-High Fronting', 'phoneme': 'ɔɪ', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'nucleus', 'length_type': 'diphthongs', 'group_type': 'Closing', 'subgroup_type': 'High-to-Mid Backing', 'phoneme': 'aʊ', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'nucleus', 'length_type': 'diphthongs', 'group_type': 'Closing', 'subgroup_type': 'High-to-Mid Backing', 'phoneme': 'oʊ', 'frequency': 0},
    {'syllable_type': 'CV', 'position': 'nucleus', 'length_type': 'diphthongs', 'group_type': 'Centering', 'subgroup_type': 'High-to-Central', 'phoneme': 'ɪə', 'frequency': 0},
]
