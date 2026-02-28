#!/usr/bin/env python3
"""Quick menu verification"""

import sys
sys.path.append('.')

# Import and show just the menu structure without running the full app
try:
    # Read first few lines of main.py to verify imports work
    import sqlite3
    import os
    import json
    from collections import defaultdict
    
    print("✓ All imports successful")
    
    # Test the menu structure by reading the menu print statements
    with open("main.py", "r", encoding='utf-8') as f:
        lines = f.readlines()
    
    menu_lines = []
    in_menu = False
    for line in lines:
        if 'print("--- Phoneme Frequency Tracker ---")' in line:
            in_menu = True
        elif in_menu and line.strip().startswith('print("'):
            menu_lines.append(line.strip())
        elif in_menu and 'choice = input(' in line:
            break
    
    print("\n✓ Current Menu Structure:")
    for line in menu_lines:
        # Extract just the menu text
        if 'print("' in line:
            text = line.split('print("')[1].split('")')[0]
            if text.strip() and not text.startswith('-'):
                print(f"  {text}")
    
except Exception as e:
    print(f"✗ Error: {e}")
