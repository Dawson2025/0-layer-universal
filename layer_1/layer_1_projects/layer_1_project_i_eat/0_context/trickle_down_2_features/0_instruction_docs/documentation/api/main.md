---
resource_id: "044b03db-7373-477c-96f1-eaa98e750d2c"
resource_type: "document"
resource_name: "main"
---
# API Reference: Main Application (`main.py`)

Importable constants/functions for advanced or scripted usage. Most functions are interactive and intended for TUI workflows.

<!-- section_id: "a703ca95-e8a7-4c8b-b3fb-7665b160070e" -->
## Constants
- `DB_NAME`: str → SQLite filename (`phonemes.db`)

<!-- section_id: "800bb7c1-2942-46f9-b5a7-d829a2d71df3" -->
## Schema & Data
- `migrate_schema()` → Create tables and unique index if missing
- `migrate_existing_words_to_structured()` → Print migration guidance for legacy words
- `insert_sample_data()` → Insert entries from `flattened_dataset`

<!-- section_id: "facfb938-4faa-46ce-9f4e-1ffb24422406" -->
## Ordering & Queries
- `get_sorted_phonemes() -> list[tuple]` → Returns rows:
  `(syllable_type, position, length_type, group_type, subgroup_type, phoneme, frequency, group_freq, subgroup_freq)`

<!-- section_id: "21509a45-1a31-4a84-9b40-cd587c5a4efb" -->
## Displays (interactive)
- `display_flat()` → Flat list of all phonemes
- `display_nested_phonemes()` → Guided selection: type → position → length type, then nested view
- `display_full()` → Full nested hierarchy across all categories

<!-- section_id: "0f596dd1-322f-446f-be08-670fb3023ba9" -->
## Utilities (interactive)
- `reset_database()` → Two-step confirmation and reset
- `select_and_modify_frequency(increment: int = 1)` → Helper used by frequency commands
- `increase_frequency()` / `decrease_frequency()` → Admin-only frequency adjustments

<!-- section_id: "c2b1f655-0ea9-4e0a-815e-d65fa721f4b2" -->
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

<!-- section_id: "5d8d65d2-1d76-48e7-8bef-d5294bb69c38" -->
## Phoneme Management (interactive)
- `add_new_phoneme()` → Guided add flow with existing group/subgroup selection
- `delete_phoneme()` → Hierarchical listing and safe deletion

<!-- section_id: "87aaf091-9f07-40d4-83d9-7274b75219dc" -->
## Admin
- `admin_login() -> bool`
- `admin_menu()` → Protected submenu loop

<!-- section_id: "6961d60b-62b5-4a1b-a68a-b56ef5163f04" -->
## App Entrypoint
- `run()` → Main loop; also executed when running `python3 main.py`