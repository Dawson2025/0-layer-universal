# resource_id: "01dc20a4-3685-4ddd-9c3b-4d8b62fc2839"
# resource_type: "document"
# resource_name: "add_vc_syllables"
"""
Database Migration: Add VC (Vowel-Consonant) syllables

This migration creates VC syllable phonemes by:
1. Copying nucleus (vowel) phonemes from CVC syllables to VC nucleus position
2. Copying coda (consonant) phonemes from CVC syllables to VC coda position
"""

import sqlite3
import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from core.database import DB_NAME
except ImportError:
    # Fallback if import doesn't work
    DB_NAME = "data/phonemes.db"


def migrate():
    """Add VC syllable phonemes based on CVC syllables."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    print("Starting migration: Adding VC syllables...")

    # Step 1: Get all unique projects that have phonemes
    cursor.execute("SELECT DISTINCT project_id FROM phonemes")
    projects = cursor.fetchall()

    if not projects:
        print("No projects found with phonemes. Using default project_id=NULL")
        projects = [(None,)]

    for project_row in projects:
        project_id = project_row[0] if isinstance(project_row, tuple) else project_row['project_id']
        print(f"\nProcessing project_id: {project_id}")

        # Handle NULL project_id in SQL queries
        project_id_clause = "project_id IS NULL" if project_id is None else f"project_id = {project_id}"

        # Step 2: Copy nucleus phonemes from CVC to VC
        print("  Copying nucleus phonemes from CVC to VC...")
        cursor.execute(f"""
            SELECT DISTINCT phoneme, length_type, group_type, subgroup_type, frequency
            FROM phonemes
            WHERE syllable_type = 'CVC'
            AND position = 'nucleus'
            AND {project_id_clause}
            ORDER BY phoneme
        """)

        nucleus_phonemes = cursor.fetchall()
        print(f"  Found {len(nucleus_phonemes)} nucleus phonemes to copy")

        for phoneme_row in nucleus_phonemes:
            phoneme = phoneme_row['phoneme']
            length_type = phoneme_row['length_type']
            group_type = phoneme_row['group_type']
            subgroup_type = phoneme_row['subgroup_type']

            # Check if this phoneme already exists in VC
            cursor.execute(f"""
                SELECT COUNT(*) FROM phonemes
                WHERE {project_id_clause}
                AND syllable_type = 'VC'
                AND position = 'nucleus'
                AND phoneme = ?
                AND length_type = ?
            """, (phoneme, length_type))

            if cursor.fetchone()[0] == 0:
                # Insert the nucleus phoneme for VC syllable
                cursor.execute("""
                    INSERT INTO phonemes (
                        project_id, syllable_type, position, length_type,
                        group_type, subgroup_type, phoneme, frequency
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (project_id, 'VC', 'nucleus', length_type,
                      group_type, subgroup_type, phoneme, 0))
                print(f"    Added nucleus: {phoneme} ({length_type})")

        # Step 3: Copy coda phonemes from CVC to VC
        print("  Copying coda phonemes from CVC to VC...")
        cursor.execute(f"""
            SELECT DISTINCT phoneme, length_type, group_type, subgroup_type, frequency
            FROM phonemes
            WHERE syllable_type = 'CVC'
            AND position = 'coda'
            AND {project_id_clause}
            ORDER BY phoneme
        """)

        coda_phonemes = cursor.fetchall()
        print(f"  Found {len(coda_phonemes)} coda phonemes to copy")

        for phoneme_row in coda_phonemes:
            phoneme = phoneme_row['phoneme']
            length_type = phoneme_row['length_type']
            group_type = phoneme_row['group_type']
            subgroup_type = phoneme_row['subgroup_type']

            # Check if this phoneme already exists in VC
            cursor.execute(f"""
                SELECT COUNT(*) FROM phonemes
                WHERE {project_id_clause}
                AND syllable_type = 'VC'
                AND position = 'coda'
                AND phoneme = ?
                AND length_type = ?
            """, (phoneme, length_type))

            if cursor.fetchone()[0] == 0:
                # Insert the coda phoneme for VC syllable
                cursor.execute("""
                    INSERT INTO phonemes (
                        project_id, syllable_type, position, length_type,
                        group_type, subgroup_type, phoneme, frequency
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (project_id, 'VC', 'coda', length_type,
                      group_type, subgroup_type, phoneme, 0))
                print(f"    Added coda: {phoneme} ({length_type})")

    conn.commit()

    # Summary
    cursor.execute("SELECT COUNT(*) FROM phonemes WHERE syllable_type = 'VC'")
    total_vc = cursor.fetchone()[0]
    print(f"\n✓ Migration completed successfully!")
    print(f"✓ Total VC phonemes created: {total_vc}")

    conn.close()


def rollback():
    """Remove all VC syllable phonemes."""
    print("Warning: Rollback will remove all VC syllable phonemes!")
    response = input("Are you sure? (yes/no): ")

    if response.lower() != 'yes':
        print("Rollback cancelled")
        return

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM phonemes WHERE syllable_type = 'VC'")
    deleted_count = cursor.rowcount

    conn.commit()
    conn.close()

    print(f"✓ Rollback completed. Deleted {deleted_count} VC phonemes.")


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == 'rollback':
        rollback()
    else:
        migrate()
