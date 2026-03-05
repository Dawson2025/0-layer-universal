# resource_id: "9d493a60-a7ec-477c-a623-33e5b2eaa87f"
# resource_type: "document"
# resource_name: "add_syllables_data"
"""
Database Migration: Add syllables_data column to words table

This migration adds support for multi-syllable words by adding a JSON column
to store an array of syllables, while maintaining backward compatibility with
existing single-syllable data.
"""

import sqlite3
import json
from core.database import DB_NAME


def migrate():
    """Add syllables_data column to words table and migrate existing data."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    print("Starting migration: Adding syllables_data column...")

    # Step 1: Add syllables_data column if it doesn't exist
    try:
        cursor.execute("""
            ALTER TABLE words ADD COLUMN syllables_data TEXT
        """)
        print("✓ Added syllables_data column")
    except sqlite3.OperationalError as e:
        if "duplicate column name" in str(e).lower():
            print("✓ syllables_data column already exists")
        else:
            raise

    # Step 2: Migrate existing single-syllable words to new format
    cursor.execute("""
        SELECT id, syllable_type,
               onset_phoneme, onset_length_type,
               nucleus_phoneme, nucleus_length_type,
               coda_phoneme, coda_length_type
        FROM words
        WHERE syllables_data IS NULL
    """)

    words_to_migrate = cursor.fetchall()
    print(f"Found {len(words_to_migrate)} words to migrate")

    migrated_count = 0
    for word in words_to_migrate:
        word_id = word['id']
        syllable_type = word['syllable_type'] or 'CVC'

        # Build syllable data structure
        syllable = {
            'syllable_type': syllable_type,
            'phonemes': {}
        }

        # Add onset if present
        if word['onset_phoneme']:
            syllable['phonemes']['onset'] = {
                'phoneme': word['onset_phoneme'],
                'length_type': word['onset_length_type'] or ''
            }

        # Add nucleus if present
        if word['nucleus_phoneme']:
            syllable['phonemes']['nucleus'] = {
                'phoneme': word['nucleus_phoneme'],
                'length_type': word['nucleus_length_type'] or ''
            }

        # Add coda if present
        if word['coda_phoneme']:
            syllable['phonemes']['coda'] = {
                'phoneme': word['coda_phoneme'],
                'length_type': word['coda_length_type'] or ''
            }

        # Create syllables array (single syllable for existing words)
        syllables_data = [syllable]

        # Update word with new syllables_data
        cursor.execute("""
            UPDATE words
            SET syllables_data = ?
            WHERE id = ?
        """, (json.dumps(syllables_data), word_id))

        migrated_count += 1

    conn.commit()
    print(f"✓ Migrated {migrated_count} words to multi-syllable format")
    print("Migration completed successfully!")

    conn.close()


def rollback():
    """Remove syllables_data column (not recommended if data has been added)."""
    print("Warning: Rollback will remove syllables_data column and all multi-syllable data!")
    response = input("Are you sure? (yes/no): ")

    if response.lower() != 'yes':
        print("Rollback cancelled")
        return

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # SQLite doesn't support DROP COLUMN directly, need to recreate table
    print("Note: SQLite rollback requires table recreation. Skipping rollback.")
    print("To rollback, restore from backup.")

    conn.close()


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == 'rollback':
        rollback()
    else:
        migrate()
