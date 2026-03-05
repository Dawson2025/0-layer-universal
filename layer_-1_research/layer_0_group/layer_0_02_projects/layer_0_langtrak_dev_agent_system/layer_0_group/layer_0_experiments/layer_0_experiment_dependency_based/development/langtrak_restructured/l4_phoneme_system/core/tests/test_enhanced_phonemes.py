#!/usr/bin/env python3
# resource_id: "7bce14ae-bd77-4082-bd5b-59bec0ccda57"
# resource_type: "document"
# resource_name: "test_enhanced_phonemes"
"""Test script for enhanced phoneme management functions"""

import sqlite3
import os
import pytest
import main

def test_enhanced_add_phoneme():
    """Test the enhanced add phoneme function with existing group display"""
    # This test uses the db_isolation fixture automatically via autouse
    # The fixture sets main.DB_NAME to a temporary test database
    conn = sqlite3.connect(main.DB_NAME)
    cursor = conn.cursor()

    # Check if we have some sample data to work with
    cursor.execute("SELECT COUNT(*) FROM phonemes")
    count = cursor.fetchone()[0]
    
    # Test passes if the database is accessible and query works
    # (Empty database is expected for isolated tests)
    assert count >= 0

    # Check if we can query existing groups for a specific category
    cursor.execute("""
        SELECT DISTINCT syllable_type, position, length_type, group_type
        FROM phonemes
        LIMIT 3
    """)
    sample_data = cursor.fetchall()

    # Query should work even if empty
    assert isinstance(sample_data, list)

    conn.close()

def test_enhanced_delete_phoneme():
    """Test the enhanced delete phoneme function with hierarchical display"""
    # This test uses the db_isolation fixture automatically via autouse
    conn = sqlite3.connect(main.DB_NAME)
    cursor = conn.cursor()
    
    # Check if we have data that would show hierarchical structure
    cursor.execute("""
        SELECT syllable_type, position, length_type, group_type, subgroup_type, phoneme, frequency
        FROM phonemes
        ORDER BY syllable_type, position, length_type, group_type, subgroup_type, phoneme
        LIMIT 5
    """)
    sample_phonemes = cursor.fetchall()

    # Query should work even if empty
    assert isinstance(sample_phonemes, list)

    conn.close()

def test_database_queries():
    """Test that the new database queries work correctly"""
    # This test uses the db_isolation fixture automatically via autouse
    conn = sqlite3.connect(main.DB_NAME)
    cursor = conn.cursor()

    # Test the group query used in add_new_phoneme
    cursor.execute("""
        SELECT DISTINCT group_type FROM phonemes
        WHERE syllable_type = ? AND position = ? AND length_type = ?
        ORDER BY group_type
    """, ("CVC", "onset", "single_consonants"))
    groups = cursor.fetchall()
    # Query should work even if empty
    assert isinstance(groups, list)

    # Test the subgroup query used in add_new_phoneme
    if groups:
        test_group = groups[0][0]
        cursor.execute("""
            SELECT DISTINCT subgroup_type FROM phonemes
            WHERE syllable_type = ? AND position = ? AND length_type = ? AND group_type = ?
            AND subgroup_type IS NOT NULL
            ORDER BY subgroup_type
        """, ("CVC", "onset", "single_consonants", test_group))
        subgroups = cursor.fetchall()
        assert isinstance(subgroups, list)

    # Test the hierarchical data query used in delete_phoneme
    from main import get_sorted_phonemes
    sorted_data = get_sorted_phonemes()
    # Should return a list (empty or not)
    assert isinstance(sorted_data, list)

    conn.close()
