
"""
Phonotactic rules for validating and improving word generation.
These rules determine which sound combinations are natural and pronounceable.
"""

class PhonotacticRules:
    def __init__(self):
        # Sonority hierarchy (lower number = lower sonority)
        self.sonority_scale = {
            # Stops
            'p': 1, 'b': 1, 't': 1, 'd': 1, 'k': 1, 'g': 1,
            # Fricatives
            'f': 2, 'v': 2, 's': 2, 'z': 2, 'θ': 2, 'ð': 2, 'ʃ': 2, 'ʒ': 2, 'h': 2,
            # Affricates
            'tʃ': 2, 'dʒ': 2,
            # Nasals
            'm': 3, 'n': 3, 'ŋ': 3,
            # Liquids
            'l': 4, 'ɹ': 4,
            # Glides
            'w': 5, 'j': 5,
            # Vowels
            'i': 6, 'ɪ': 6, 'e': 6, 'ɛ': 6, 'æ': 6, 'a': 6, 'ɑ': 6,
            'ɔ': 6, 'o': 6, 'ʊ': 6, 'u': 6, 'ə': 6
        }
        
        # Voicing pairs
        self.voicing_pairs = {
            'p': 'b', 'b': 'p', 't': 'd', 'd': 't', 'k': 'g', 'g': 'k',
            'f': 'v', 'v': 'f', 's': 'z', 'z': 's', 'θ': 'ð', 'ð': 'θ',
            'ʃ': 'ʒ', 'ʒ': 'ʃ', 'tʃ': 'dʒ', 'dʒ': 'tʃ'
        }
        
        # Problematic consonant clusters to avoid
        self.forbidden_clusters = {
            'pb', 'bp', 'td', 'dt', 'kg', 'gk',  # Hard to pronounce
            'nm', 'mn',  # Nasal clusters
            'lr', 'rl',  # Liquid clusters can be difficult
        }
        
        # Preferred consonant clusters
        self.preferred_clusters = {
            'onset': ['pl', 'bl', 'kl', 'gl', 'fl', 'sl', 'pr', 'br', 'kr', 'gr', 'fr', 'tr', 'dr', 'st', 'sp', 'sk', 'sw'],
            'coda': ['st', 'nt', 'nd', 'mp', 'nk', 'lt', 'rt']
        }

    def validate_syllable(self, onset, nucleus, coda):
        """Validate a complete syllable for phonotactic compliance."""
        issues = []
        
        # Check onset clusters
        if len(onset) > 1:
            if not self._validate_onset_cluster(onset):
                issues.append(f"Problematic onset cluster: {onset}")
        
        # Check coda clusters
        if len(coda) > 1:
            if not self._validate_coda_cluster(coda):
                issues.append(f"Problematic coda cluster: {coda}")
        
        # Check overall sonority
        if not self._validate_sonority_sequence(onset, nucleus, coda):
            issues.append("Sonority sequencing violation")
        
        return len(issues) == 0, issues

    def _validate_onset_cluster(self, cluster):
        """Validate consonant cluster in onset position."""
        if cluster in self.forbidden_clusters:
            return False
        
        # Check sonority rise in onset
        if len(cluster) == 2:
            c1, c2 = cluster[0], cluster[1]
            son1 = self.sonority_scale.get(c1, 0)
            son2 = self.sonority_scale.get(c2, 0)
            return son1 < son2  # Should rise in sonority
        
        return True

    def _validate_coda_cluster(self, cluster):
        """Validate consonant cluster in coda position."""
        if cluster in self.forbidden_clusters:
            return False
        
        # Check sonority fall in coda
        if len(cluster) == 2:
            c1, c2 = cluster[0], cluster[1]
            son1 = self.sonority_scale.get(c1, 0)
            son2 = self.sonority_scale.get(c2, 0)
            return son1 >= son2  # Should fall or stay level
        
        return True

    def _validate_sonority_sequence(self, onset, nucleus, coda):
        """Check overall sonority profile of syllable."""
        # Simple check: nucleus should have highest sonority
        nucleus_sonority = self.sonority_scale.get(nucleus, 0)
        
        # Check onset doesn't exceed nucleus
        if onset:
            onset_max = max(self.sonority_scale.get(c, 0) for c in onset)
            if onset_max >= nucleus_sonority:
                return False
        
        # Check coda doesn't exceed nucleus
        if coda:
            coda_max = max(self.sonority_scale.get(c, 0) for c in coda)
            if coda_max >= nucleus_sonority:
                return False
        
        return True

    def score_syllable(self, onset, nucleus, coda):
        """Score syllable naturalness (higher = more natural)."""
        score = 100  # Start with perfect score
        
        # Penalty for forbidden clusters
        full_onset = ''.join(onset) if isinstance(onset, list) else onset
        full_coda = ''.join(coda) if isinstance(coda, list) else coda
        
        if full_onset in self.forbidden_clusters:
            score -= 50
        if full_coda in self.forbidden_clusters:
            score -= 50
        
        # Bonus for preferred clusters
        if full_onset in self.preferred_clusters.get('onset', []):
            score += 20
        if full_coda in self.preferred_clusters.get('coda', []):
            score += 20
        
        # Sonority bonus
        is_valid, _ = self.validate_syllable(onset, nucleus, coda)
        if is_valid:
            score += 30
        
        return max(0, score)

    def suggest_improvements(self, onset, nucleus, coda):
        """Suggest alternative phonemes to improve phonotactics."""
        suggestions = []
        
        is_valid, issues = self.validate_syllable(onset, nucleus, coda)
        if is_valid:
            return suggestions
        
        for issue in issues:
            if "onset cluster" in issue:
                # Suggest removing one consonant or replacing with preferred cluster
                preferred = self.preferred_clusters.get('onset', [])
                matching = [p for p in preferred if p[0] == onset[0] or p[-1] == onset[-1]]
                if matching:
                    suggestions.append(f"Try onset cluster: {matching[0]}")
            
            elif "coda cluster" in issue:
                preferred = self.preferred_clusters.get('coda', [])
                matching = [p for p in preferred if p[0] == coda[0] or p[-1] == coda[-1]]
                if matching:
                    suggestions.append(f"Try coda cluster: {matching[0]}")
        
        return suggestions
