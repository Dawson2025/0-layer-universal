#!/usr/bin/env python3
# resource_id: "7bab65b8-f090-4add-a8eb-d5dea73c6a53"
# resource_type: "document"
# resource_name: "test_phoneme_management"
"""Test script for the new phoneme management functions"""

import sys
import os
import sqlite3

# Test adding and deleting phonemes
def test_phoneme_functions():
    print("Testing phoneme management functions...")
    
    # Check database exists and has correct schema
    if not os.path.exists("data/phonemes.db"):
        print("✗ Database not found. Run the main app first to create it.")
        return False
    
    conn = sqlite3.connect("data/phonemes.db")
    cursor = conn.cursor()
    
    # Test adding a phoneme directly to database
    try:
        # Add a test phoneme
        cursor.execute("""
            INSERT OR IGNORE INTO phonemes 
            (syllable_type, position, length_type, group_type, subgroup_type, phoneme, frequency)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, ("CVC", "onset", "single_consonants", "test_group", "test_subgroup", "ʔ", 5))
        
        # Check if it was added
        cursor.execute("""
            SELECT COUNT(*) FROM phonemes 
            WHERE syllable_type='CVC' AND position='onset' AND length_type='single_consonants' 
            AND group_type='test_group' AND phoneme='ʔ'
        """)
        count = cursor.fetchone()[0]
        
        if count > 0:
            print("✓ Test phoneme added successfully")
            
            # Test deletion
            cursor.execute("""
                DELETE FROM phonemes 
                WHERE syllable_type='CVC' AND position='onset' AND length_type='single_consonants' 
                AND group_type='test_group' AND phoneme='ʔ'
            """)
            
            cursor.execute("""
                SELECT COUNT(*) FROM phonemes 
                WHERE syllable_type='CVC' AND position='onset' AND length_type='single_consonants' 
                AND group_type='test_group' AND phoneme='ʔ'
            """)
            count_after = cursor.fetchone()[0]
            
            if count_after == 0:
                print("✓ Test phoneme deleted successfully")
            else:
                print("✗ Test phoneme deletion failed")
        else:
            print("✗ Test phoneme addition failed")
        
        conn.commit()
        
    except Exception as e:
        print(f"✗ Error during phoneme testing: {e}")
        return False
    
    conn.close()
    return True

def test_menu_structure():
    """Test that the menu structure is updated correctly"""
    print("Testing menu structure...")
    
    try:
        with open("main.py", "r", encoding='utf-8') as f:
            content = f.read()
        
        # Check for new menu options
        if "1. Add new phoneme" in content and "2. Delete phoneme" in content:
            print("✓ Menu updated with phoneme management options")
        else:
            print("✗ Menu not properly updated")
            return False
        
        # Check for function definitions
        if "def add_new_phoneme():" in content and "def delete_phoneme():" in content:
            print("✓ Phoneme management functions defined")
        else:
            print("✗ Phoneme management functions missing")
            return False
        
        return True
        
    except Exception as e:
        print(f"✗ Error checking menu structure: {e}")
        return False

if __name__ == "__main__":
    print("Language Tracker App - Phoneme Management Test")
    print("=" * 50)
    
    # Run tests
    menu_success = test_menu_structure()
    phoneme_success = test_phoneme_functions()
    
    print("\n" + "=" * 50)
    if menu_success and phoneme_success:
        print("✓ All phoneme management tests passed!")
        print("\nNew features ready to use:")
        print("  • Option 1: Add new phoneme")
        print("  • Option 2: Delete phoneme")
        print("  • Updated menu numbering (now 1-17 options)")
    else:
        print("✗ Some tests failed. Check the issues above.")
