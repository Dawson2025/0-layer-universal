---
resource_id: "2ee609d6-2baf-400d-94c4-4e4ca34903fb"
resource_type: "document"
resource_name: "main"
---
# API Reference: Main Application (`main.py`)

Importable constants/functions for advanced or scripted usage. Most functions are interactive and intended for TUI workflows.

<!-- section_id: "24418cc5-a6df-4795-acb8-48958a11219f" -->
## Constants
- `DB_NAME`: str → SQLite filename (`phonemes.db`)

<!-- section_id: "7fe6dbe2-751b-4782-a71c-0e8b39a28f5c" -->
## Schema & Data
- `migrate_schema()` → Create tables and unique index if missing
- `migrate_existing_words_to_structured()` → Print migration guidance for legacy words
- `insert_sample_data()` → Insert entries from `flattened_dataset`

<!-- section_id: "8a858ef5-8018-4bdf-a029-44ba08980691" -->
## Ordering & Queries
- `get_sorted_phonemes() -> list[tuple]` → Returns rows:
  `(syllable_type, position, length_type, group_type, subgroup_type, phoneme, frequency, group_freq, subgroup_freq)`

<!-- section_id: "52655876-c1b5-4bca-84c2-64d07f59895d" -->
## Displays (interactive)
- `display_flat()` → Flat list of all phonemes
- `display_nested_phonemes()` → Guided selection: type → position → length type, then nested view
- `display_full()` → Full nested hierarchy across all categories

<!-- section_id: "407cb747-d180-482e-915c-40f4545eafb1" -->
## Utilities (interactive)
- `reset_database()` → Two-step confirmation and reset
- `select_and_modify_frequency(increment: int = 1)` → Helper used by frequency commands
- `increase_frequency()` / `decrease_frequency()` → Admin-only frequency adjustments

<!-- section_id: "12a6f0a6-21f4-4806-a61f-c5df4bcd4edb" -->
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

<!-- section_id: "c47efe57-0719-4eb9-9db5-7f09ab9819c8" -->
## Phoneme Management (interactive)
- `add_new_phoneme()` → Guided add flow with existing group/subgroup selection
- `delete_phoneme()` → Hierarchical listing and safe deletion

<!-- section_id: "a260ece9-11cd-49db-9c54-9efafbe01865" -->
## Admin
- `admin_login() -> bool`
- `admin_menu()` → Protected submenu loop

<!-- section_id: "5b973809-1669-4e4f-aaf0-2645ff6e126c" -->
## App Entrypoint
- `run()` → Main loop; also executed when running `python3 main.py`