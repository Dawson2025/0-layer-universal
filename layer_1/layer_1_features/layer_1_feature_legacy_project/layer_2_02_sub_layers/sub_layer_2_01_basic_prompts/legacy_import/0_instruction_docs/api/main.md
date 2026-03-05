---
resource_id: "8040de1e-1751-4b96-b1d8-8bc790f9c500"
resource_type: "document"
resource_name: "main"
---
# API Reference: Main Application (`main.py`)

Importable constants/functions for advanced or scripted usage. Most functions are interactive and intended for TUI workflows.

<!-- section_id: "d3db2d35-c4d7-4a5d-81c9-d23d47f95ccd" -->
## Constants
- `DB_NAME`: str → SQLite filename (`phonemes.db`)

<!-- section_id: "a5f61d20-cf28-49e4-bfb7-53f437cb6d14" -->
## Schema & Data
- `migrate_schema()` → Create tables and unique index if missing
- `migrate_existing_words_to_structured()` → Print migration guidance for legacy words
- `insert_sample_data()` → Insert entries from `flattened_dataset`

<!-- section_id: "0b2d1c62-8e57-42d9-b419-39e5072a6799" -->
## Ordering & Queries
- `get_sorted_phonemes() -> list[tuple]` → Returns rows:
  `(syllable_type, position, length_type, group_type, subgroup_type, phoneme, frequency, group_freq, subgroup_freq)`

<!-- section_id: "24e7bb16-2f80-4925-8d38-8f11e25c6957" -->
## Displays (interactive)
- `display_flat()` → Flat list of all phonemes
- `display_nested_phonemes()` → Guided selection: type → position → length type, then nested view
- `display_full()` → Full nested hierarchy across all categories

<!-- section_id: "fe18e6b8-8759-4bcd-8d4a-d734a82a5149" -->
## Utilities (interactive)
- `reset_database()` → Two-step confirmation and reset
- `select_and_modify_frequency(increment: int = 1)` → Helper used by frequency commands
- `increase_frequency()` / `decrease_frequency()` → Admin-only frequency adjustments

<!-- section_id: "7a21ff31-79fc-48fe-9e52-d57063faef6d" -->
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

<!-- section_id: "c0562b75-e247-4e8c-b6b9-afe62c70b1b1" -->
## Phoneme Management (interactive)
- `add_new_phoneme()` → Guided add flow with existing group/subgroup selection
- `delete_phoneme()` → Hierarchical listing and safe deletion

<!-- section_id: "e6e7be08-357b-46b6-a12e-06b1bda90244" -->
## Admin
- `admin_login() -> bool`
- `admin_menu()` → Protected submenu loop

<!-- section_id: "e6f6d26f-92bc-40a1-970c-8cd51cb6b1bb" -->
## App Entrypoint
- `run()` → Main loop; also executed when running `python3 main.py`