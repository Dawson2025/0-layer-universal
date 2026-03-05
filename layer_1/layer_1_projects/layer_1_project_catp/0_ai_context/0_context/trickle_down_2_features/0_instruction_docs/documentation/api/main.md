---
resource_id: "303f0444-1a4f-4aad-9889-503fbfa6e6e4"
resource_type: "document"
resource_name: "main"
---
# API Reference: Main Application (`main.py`)

Importable constants/functions for advanced or scripted usage. Most functions are interactive and intended for TUI workflows.

<!-- section_id: "92a6f76d-3d78-4c6b-a4ec-37f28c24b218" -->
## Constants
- `DB_NAME`: str → SQLite filename (`phonemes.db`)

<!-- section_id: "555c30a5-988c-4c19-b410-566665c90ba6" -->
## Schema & Data
- `migrate_schema()` → Create tables and unique index if missing
- `migrate_existing_words_to_structured()` → Print migration guidance for legacy words
- `insert_sample_data()` → Insert entries from `flattened_dataset`

<!-- section_id: "865cb18d-411a-48ea-ac41-1428091d01c3" -->
## Ordering & Queries
- `get_sorted_phonemes() -> list[tuple]` → Returns rows:
  `(syllable_type, position, length_type, group_type, subgroup_type, phoneme, frequency, group_freq, subgroup_freq)`

<!-- section_id: "39cab4c3-41fe-4810-85ce-d591f2cbaa7c" -->
## Displays (interactive)
- `display_flat()` → Flat list of all phonemes
- `display_nested_phonemes()` → Guided selection: type → position → length type, then nested view
- `display_full()` → Full nested hierarchy across all categories

<!-- section_id: "f6a8a694-a5db-488b-a9f2-3aac4717dd9e" -->
## Utilities (interactive)
- `reset_database()` → Two-step confirmation and reset
- `select_and_modify_frequency(increment: int = 1)` → Helper used by frequency commands
- `increase_frequency()` / `decrease_frequency()` → Admin-only frequency adjustments

<!-- section_id: "03926c4c-cbdb-4097-904c-19c757ef637b" -->
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

<!-- section_id: "721792bd-803a-4735-9ce7-3969fd619256" -->
## Phoneme Management (interactive)
- `add_new_phoneme()` → Guided add flow with existing group/subgroup selection
- `delete_phoneme()` → Hierarchical listing and safe deletion

<!-- section_id: "6306e2de-6720-475f-892c-b6f5f8587a68" -->
## Admin
- `admin_login() -> bool`
- `admin_menu()` → Protected submenu loop

<!-- section_id: "74eafc65-1089-45d3-80c4-dfc39a0bff28" -->
## App Entrypoint
- `run()` → Main loop; also executed when running `python3 main.py`