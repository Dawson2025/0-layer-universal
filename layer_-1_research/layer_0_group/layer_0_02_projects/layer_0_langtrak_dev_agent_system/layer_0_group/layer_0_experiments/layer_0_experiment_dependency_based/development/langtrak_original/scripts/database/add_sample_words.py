#!/usr/bin/env python3
# resource_id: "28ac9092-55ba-4eb3-bb45-06ab8d2fde22"
# resource_type: "document"
# resource_name: "add_sample_words"
import sqlite3
import json

DB_NAME = "data/phonemes.db"

def add_sample_words():
    """Add sample words to test the JSON functionality"""
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Sample words with multiple English translations
    sample_words = [
        ("Spanish", ["hello", "hi", "greetings"], "hola", "/ˈola/", "OH-lah"),
        ("Spanish", ["goodbye", "bye", "farewell"], "adiós", "/aˈðjos/", "ah-DEES"),
        ("French", ["hello", "hi"], "bonjour", "/bɔ̃ˈʒur/", "bon-ZHOOR"),
        ("German", ["hello"], "hallo", "/ˈhalo/", "HAH-lo"),
        ("Italian", ["hello", "hi", "good morning"], "ciao", "/ˈtʃao/", "CHOW"),
    ]
    
    for lang, english_words, new_word, ipa, dict_ph in sample_words:
        cursor.execute("""
            INSERT INTO words (language, english_words, new_language_word, ipa_phonetics, dictionary_phonetics) 
            VALUES (?, ?, ?, ?, ?)
        """, (lang, json.dumps(english_words), new_word, ipa, dict_ph))
        print(f"Added {new_word} with English meanings: {', '.join(english_words)}")
    
    conn.commit()
    conn.close()
    print(f"\nSuccessfully added {len(sample_words)} sample words!")

if __name__ == "__main__":
    add_sample_words()
