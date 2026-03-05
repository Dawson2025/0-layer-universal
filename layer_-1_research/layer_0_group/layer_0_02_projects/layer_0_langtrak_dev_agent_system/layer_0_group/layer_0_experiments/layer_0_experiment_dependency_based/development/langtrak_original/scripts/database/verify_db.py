# resource_id: "5ff8cb8e-7e09-4900-960e-7bfa7ce44f21"
# resource_type: "document"
# resource_name: "verify_db"
import sqlite3
import json

# Connect to the database
conn = sqlite3.connect("data/phonemes.db")
cursor = conn.cursor()

print("=== DATABASE VERIFICATION ===")

# Check phonemes table
cursor.execute("SELECT COUNT(*) FROM phonemes")
phoneme_count = cursor.fetchone()[0]
print(f"Phonemes table: {phoneme_count} entries")

# Check words table structure
cursor.execute("PRAGMA table_info(words)")
columns = cursor.fetchall()
print(f"\nWords table columns ({len(columns)} total):")
for col in columns:
    print(f"  - {col[1]} ({col[2]})")

# Check if we have new structured fields
expected_new_fields = ['syllable_type', 'onset_phoneme', 'onset_length_type', 
                       'nucleus_phoneme', 'nucleus_length_type', 'coda_phoneme', 
                       'coda_length_type']

actual_columns = [col[1] for col in columns]
for field in expected_new_fields:
    status = "✓" if field in actual_columns else "✗"
    print(f"  {status} {field}")

# Check words table content
cursor.execute("SELECT COUNT(*) FROM words")
words_count = cursor.fetchone()[0]
print(f"\nWords table: {words_count} entries")

if words_count > 0:
    print("\nSample word entries:")
    cursor.execute("""
        SELECT language, english_words, new_language_word, 
               syllable_type, onset_phoneme, nucleus_phoneme, coda_phoneme 
        FROM words LIMIT 3
    """)
    for row in cursor.fetchall():
        lang, eng_json, new_word, syl_type, onset, nucleus, coda = row
        english_list = json.loads(eng_json) if eng_json else []
        print(f"  - {lang}: {', '.join(english_list)} -> {new_word}")
        print(f"    Structure: {syl_type} | Onset: {onset} | Nucleus: {nucleus} | Coda: {coda}")

conn.close()
print("\n=== VERIFICATION COMPLETE ===")
