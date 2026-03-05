#!/usr/bin/env python3
# resource_id: "6dbcf9d5-29cd-4a39-9d57-2ba8a9d8fd66"
# resource_type: "document"
# resource_name: "test_json_schema"
import sqlite3
import json
import pytest

def test_json_schema(tmp_path):
    """Test the new JSON-based schema for English words"""
    
    # Create isolated database path
    db_path = tmp_path / "test_phonemes.db"
    
    # Create database with new schema
    conn = sqlite3.connect(str(db_path))
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE words (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            language TEXT,
            english_words TEXT,
            new_language_word TEXT,
            ipa_phonetics TEXT,
            dictionary_phonetics TEXT
        )
    """)
    
    # Test inserting a word with multiple English translations
    english_list = ["hello", "hi", "greetings"]
    cursor.execute("""
        INSERT INTO words (language, english_words, new_language_word, ipa_phonetics, dictionary_phonetics) 
        VALUES (?, ?, ?, ?, ?)
    """, ("TestLang", json.dumps(english_list), "hola", "/ˈhola/", "HO-la"))
    
    # Test retrieving and parsing JSON
    cursor.execute("SELECT language, english_words, new_language_word FROM words")
    row = cursor.fetchone()
    
    assert row is not None, "No data found"
    
    lang, eng_json, new_word = row
    parsed_english = json.loads(eng_json)
    
    assert lang == "TestLang"
    assert parsed_english == english_list
    assert new_word == "hola"
    assert isinstance(parsed_english, list)
    
    conn.close()