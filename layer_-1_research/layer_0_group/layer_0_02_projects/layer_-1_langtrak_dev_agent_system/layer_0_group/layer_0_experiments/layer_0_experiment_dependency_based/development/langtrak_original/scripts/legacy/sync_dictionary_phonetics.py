
#!/usr/bin/env python3
"""
Script to sync dictionary phonetics with IPA phonetics for all existing words.
"""

import sqlite3

DB_NAME = "data/phonemes.db"

def sync_dictionary_phonetics():
    """Update all existing words to have dictionary phonetics match IPA phonetics."""
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Get all words that need updating
    cursor.execute("""
        SELECT id, new_language_word, ipa_phonetics, dictionary_phonetics 
        FROM words 
        WHERE ipa_phonetics IS NOT NULL AND ipa_phonetics != ''
    """)
    
    words = cursor.fetchall()
    
    if not words:
        print("No words found to update.")
        conn.close()
        return
    
    print(f"Found {len(words)} words to update...")
    
    updated_count = 0
    for word_id, word_name, ipa, current_dict in words:
        if current_dict != ipa:
            cursor.execute("""
                UPDATE words SET dictionary_phonetics = ? WHERE id = ?
            """, (ipa, word_id))
            print(f"Updated '{word_name}': '{current_dict}' → '{ipa}'")
            updated_count += 1
        else:
            print(f"'{word_name}': Already synced")
    
    conn.commit()
    conn.close()
    
    print(f"\nCompleted! Updated {updated_count} out of {len(words)} words.")
    print("All dictionary phonetics now match their IPA phonetics.")

if __name__ == "__main__":
    sync_dictionary_phonetics()
