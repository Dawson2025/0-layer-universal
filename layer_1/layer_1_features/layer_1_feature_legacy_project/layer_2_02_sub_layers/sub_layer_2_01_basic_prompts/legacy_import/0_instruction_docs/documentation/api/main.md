---
resource_id: "fa5b54ce-31e3-457f-9849-69f23b378ee3"
resource_type: "document"
resource_name: "main"
---
# API Reference: Main Application (`main.py`)

Importable constants/functions for advanced or scripted usage. Most functions are interactive and intended for TUI workflows.

<!-- section_id: "ad4684f8-e88f-441b-b3dc-dc3a26665d4b" -->
## Constants
- `DB_NAME`: str → SQLite filename (`phonemes.db`)

<!-- section_id: "788c2fde-f8f9-41a6-a058-9f4294570bec" -->
## Schema & Data
- `migrate_schema()` → Create tables and unique index if missing
- `migrate_existing_words_to_structured()` → Print migration guidance for legacy words
- `insert_sample_data()` → Insert entries from `flattened_dataset`

<!-- section_id: "1d445c8d-f0cb-4375-9a26-ed87ad60fc88" -->
## Ordering & Queries
- `get_sorted_phonemes() -> list[tuple]` → Returns rows:
  `(syllable_type, position, length_type, group_type, subgroup_type, phoneme, frequency, group_freq, subgroup_freq)`

<!-- section_id: "9f4b6149-f793-4bbc-af11-f47ae4d599b5" -->
## Displays (interactive)
- `display_flat()` → Flat list of all phonemes
- `display_nested_phonemes()` → Guided selection: type → position → length type, then nested view
- `display_full()` → Full nested hierarchy across all categories

<!-- section_id: "920f6b42-0607-4eb8-b55c-3b402fc04640" -->
## Utilities (interactive)
- `reset_database()` → Two-step confirmation and reset
- `select_and_modify_frequency(increment: int = 1)` → Helper used by frequency commands
- `increase_frequency()` / `decrease_frequency()` → Admin-only frequency adjustments

<!-- section_id: "86af9242-235f-4844-8716-168bfe911228" -->
## Word Management (interactive)
- `create_word_from_phonemes()` → Create a word and optionally populate structured fields
- `add_new_word(cursor, conn, language, english_words, new_language_word, ipa_phonetics, dictionary_phonetics)`
- `add_new_word_with_structure(cursor, conn, language, english_words, new_language_word, ...)`
- `display_words()` → List all words with structured detail if present
- `lookup_word()` → Search and display a word
- `update_phoneme_frequencies_for_deleted_word_structured(word_data)`
- `update_phoneme_frequencies_for_deleted_word(ipa_phonetics)`
- `delete_last_word()`
- `delete_word_by_lookup()`
- `edit_existing_word()`

<!-- section_id: "b3df95c1-adc0-4ce4-bfd6-584571dfc184" -->
## Phoneme Management (interactive)
- `add_new_phoneme()` → Guided add flow with existing group/subgroup selection
- `delete_phoneme()` → Hierarchical listing and safe deletion

<!-- section_id: "83436b18-9beb-4a7c-8e62-6342651869f4" -->
## Admin
- `admin_login() -> bool`
- `admin_menu()` → Protected submenu loop

<!-- section_id: "21a62e50-0dc3-46ab-aa95-5eebf6d58742" -->
## App Entrypoint
- `run()` → Main loop; also executed when running `python3 main.py`