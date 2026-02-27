"""
Create Phoneme Template for VC Syllables

This script generates a phoneme template file for VC (Vowel-Consonant) syllables
that can be imported into projects.
"""

import sqlite3
import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from core.database import DB_NAME
except ImportError:
    DB_NAME = "data/phonemes.db"


def create_vc_template():
    """Generate a phoneme template file for VC syllables."""

    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    print("Creating VC syllable phoneme template...")

    # Query all VC phonemes
    cursor.execute("""
        SELECT syllable_type, position, length_type, group_type, subgroup_type, phoneme, frequency
        FROM phonemes
        WHERE syllable_type = 'VC'
        ORDER BY position, length_type, group_type, subgroup_type, phoneme
    """)

    phonemes = cursor.fetchall()

    if not phonemes:
        print("Error: No VC phonemes found in database.")
        print("Please run the migration: python3 migrations/add_vc_syllables.py")
        conn.close()
        return

    print(f"Found {len(phonemes)} VC phonemes")

    # Build template file content
    template_name = "vc_syllables"
    template_content = f"""# Phoneme template: {template_name}
# VC (Vowel-Consonant) syllables
# Generated from CVC nucleus and coda phonemes
# Total phonemes: {len(phonemes)}

{template_name}_template = [
"""

    for phoneme in phonemes:
        # Handle None values for subgroup_type
        subgroup = phoneme['subgroup_type'] if phoneme['subgroup_type'] else 'none'

        template_content += f"    {{'syllable_type': '{phoneme['syllable_type']}', 'position': '{phoneme['position']}', 'length_type': '{phoneme['length_type']}', 'group_type': '{phoneme['group_type']}', 'subgroup_type': '{subgroup}', 'phoneme': '{phoneme['phoneme']}', 'frequency': 0}},\n"

    template_content += "]\n"

    # Write to file
    output_dir = "data/phoneme_templates"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"{template_name}.py")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(template_content)

    print(f"✓ Template created: {output_file}")
    print(f"✓ Total phonemes in template: {len(phonemes)}")

    # Print summary
    cursor.execute("""
        SELECT position, COUNT(*) as count
        FROM phonemes
        WHERE syllable_type = 'VC'
        GROUP BY position
        ORDER BY position
    """)

    print("\nPhoneme breakdown:")
    for row in cursor.fetchall():
        print(f"  {row['position']}: {row['count']} phonemes")

    conn.close()


if __name__ == '__main__':
    create_vc_template()
