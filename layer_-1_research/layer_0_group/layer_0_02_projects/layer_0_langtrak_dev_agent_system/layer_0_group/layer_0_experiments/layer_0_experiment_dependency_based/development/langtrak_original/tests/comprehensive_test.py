#!/usr/bin/env python3
# resource_id: "22498dc8-edec-43a6-8ec5-7051819aa6ae"
# resource_type: "document"
# resource_name: "comprehensive_test"
"""Comprehensive test suite for enhanced phoneme management functions"""

import sqlite3
import os
import sys
import pytest
from collections import defaultdict

# Ensure root is in path
sys.path.append('.')
from main import get_sorted_phonemes

@pytest.fixture
def db_path(tmp_path):
    """Create a test database with sample data in a temp directory."""
    db_file = tmp_path / "test_phonemes.db"
    
    conn = sqlite3.connect(str(db_file))
    cursor = conn.cursor()
    
    # Create schema
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS phonemes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            syllable_type TEXT,
            position TEXT,
            length_type TEXT,
            group_type TEXT,
            subgroup_type TEXT,
            phoneme TEXT,
            frequency INTEGER DEFAULT 0
        )
    """)
    
    # Create unique index
    cursor.execute("""
        CREATE UNIQUE INDEX IF NOT EXISTS idx_unique_phoneme
        ON phonemes (syllable_type, position, length_type, group_type, subgroup_type, phoneme)
    """)
    
    # Add sample data for testing
    sample_data = [
        ("CVC", "onset", "single_consonants", "Plosives", "Voiced", "b", 5),
        ("CVC", "onset", "single_consonants", "Plosives", "Voiceless", "p", 3),
        ("CVC", "onset", "single_consonants", "Fricatives", "Sibilant", "s", 8),
        ("CVC", "onset", "single_consonants", "Fricatives", "Sibilant", "z", 4),
        ("CVC", "onset", "single_consonants", "Fricatives", None, "f", 2),
        ("CV", "nucleus", "monophthongs", "High", "Front", "i", 10),
        ("CV", "nucleus", "monophthongs", "High", "Back", "u", 7),
        ("CV", "nucleus", "diphthongs", "Closing", None, "aɪ", 6),
    ]
    
    for data in sample_data:
        cursor.execute("""
            INSERT INTO phonemes 
            (syllable_type, position, length_type, group_type, subgroup_type, phoneme, frequency)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, data)
    
    conn.commit()
    conn.close()
    return str(db_file)

def test_database_queries(db_path):
    """Test all database queries used in the enhanced functions"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # Test 1: Group query
        cursor.execute("""
            SELECT DISTINCT group_type FROM phonemes 
            WHERE syllable_type = ? AND position = ? AND length_type = ?
            ORDER BY group_type
        """, ("CVC", "onset", "single_consonants"))
        groups = cursor.fetchall()
        expected_groups = ["Fricatives", "Plosives"]
        actual_groups = [g[0] for g in groups]
        assert set(actual_groups) == set(expected_groups)
        
        # Test 2: Subgroup query
        cursor.execute("""
            SELECT DISTINCT subgroup_type FROM phonemes 
            WHERE syllable_type = ? AND position = ? AND length_type = ? AND group_type = ?
            AND subgroup_type IS NOT NULL
            ORDER BY subgroup_type
        """, ("CVC", "onset", "single_consonants", "Plosives"))
        subgroups = cursor.fetchall()
        expected_subgroups = ["Voiced", "Voiceless"]
        actual_subgroups = [s[0] for s in subgroups]
        assert set(actual_subgroups) == set(expected_subgroups)
        
        # Test 3: Complex deletion query
        cursor.execute("""
            SELECT id, frequency FROM phonemes 
            WHERE syllable_type=? AND position=? AND length_type=? 
            AND group_type=? AND (subgroup_type=? OR (subgroup_type IS NULL AND ? IS NULL)) AND phoneme=?
        """, ("CVC", "onset", "single_consonants", "Fricatives", None, None, "f"))
        result = cursor.fetchone()
        assert result and len(result) == 2
        
        # Test 4: Test with subgroup (not None)
        cursor.execute("""
            SELECT id, frequency FROM phonemes 
            WHERE syllable_type=? AND position=? AND length_type=? 
            AND group_type=? AND (subgroup_type=? OR (subgroup_type IS NULL AND ? IS NULL)) AND phoneme=?
        """, ("CVC", "onset", "single_consonants", "Plosives", "Voiced", "Voiced", "b"))
        result = cursor.fetchone()
        assert result and len(result) == 2
        
    finally:
        conn.close()

def test_get_sorted_phonemes(db_path, monkeypatch):
    """Test the get_sorted_phonemes function integration"""
    # Patch main.DB_NAME to use our test DB
    import main
    import core.database as core_db
    monkeypatch.setattr(main, 'DB_NAME', db_path)
    monkeypatch.setattr(core_db, 'DB_NAME', db_path)
    
    sorted_data = get_sorted_phonemes()
    assert sorted_data
    
    # Test filtering
    cvc_onset_single = [
        row for row in sorted_data
        if row[0] == "CVC" and row[1] == "onset" and row[2] == "single_consonants"
    ]
    assert len(cvc_onset_single) >= 5
    
    # Test hierarchical grouping
    grouped = defaultdict(list)
    for row in cvc_onset_single:
        s, p, l, g, sub, ph, f, gfreq, subfreq = row
        key = (g, sub, gfreq, subfreq)
        grouped[key].append((ph, f, row))
    
    assert len(grouped) >= 2

def test_function_imports():
    """Test that the enhanced functions can be imported without errors"""
    from main import add_new_phoneme, delete_phoneme
    assert callable(add_new_phoneme)
    assert callable(delete_phoneme)

def test_syntax_validation():
    """Test that there are no syntax errors in main.py"""
    import py_compile
    py_compile.compile("main.py", doraise=True)

def test_edge_cases(db_path):
    """Test edge cases and error conditions"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # Test 1: Empty database queries
        cursor.execute("DELETE FROM phonemes")
        conn.commit()
        
        cursor.execute("""
            SELECT DISTINCT group_type FROM phonemes 
            WHERE syllable_type = ? AND position = ? AND length_type = ?
            ORDER BY group_type
        """, ("CVC", "onset", "single_consonants"))
        empty_result = cursor.fetchall()
        assert len(empty_result) == 0
        
        # Test 2: NULL subgroup handling
        cursor.execute("""
            INSERT INTO phonemes 
            (syllable_type, position, length_type, group_type, subgroup_type, phoneme, frequency)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, ("CVC", "onset", "single_consonants", "TestGroup", None, "x", 1))
        conn.commit()
        
        cursor.execute("""
            SELECT id, frequency FROM phonemes 
            WHERE syllable_type=? AND position=? AND length_type=? 
            AND group_type=? AND (subgroup_type=? OR (subgroup_type IS NULL AND ? IS NULL)) AND phoneme=?
        """, ("CVC", "onset", "single_consonants", "TestGroup", None, None, "x"))
        
        null_result = cursor.fetchone()
        assert null_result
        
    finally:
        conn.close()
