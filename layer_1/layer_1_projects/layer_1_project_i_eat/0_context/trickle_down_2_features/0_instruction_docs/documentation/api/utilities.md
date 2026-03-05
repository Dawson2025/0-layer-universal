---
resource_id: "febc1fc9-a971-4f7e-88a9-da79dd543e37"
resource_type: "document"
resource_name: "utilities"
---
# API Reference: Utilities

<!-- section_id: "8ca6a307-e022-4881-845b-2e411af63a0b" -->
## `flattened_dataset.py`
- Exports `flattened_dataset: list[dict]` with keys:
  - `syllable_type`, `position`, `length_type`, `group_type`, `subgroup_type`, `phoneme`, `frequency`
- Used by `insert_sample_data()` to seed the database

<!-- section_id: "bd2ce2a2-fd82-4da5-87a5-19b81e2e2a6e" -->
## `flatten_syllables.py`
- Utility script to convert hierarchical `syllable_making_dataset` (from `sample_data.py`) into a flat list
- Key function: `recurse(path: dict, data: Any)` populates an internal `grouped` structure
- Writes out `flattened_dataset.py` after user confirmation if overwriting

<!-- section_id: "1fb6d5de-4461-4e1a-b814-e085e40b96a2" -->
## `add_sample_words.py`
- Function: `add_sample_words()` inserts example word rows into `words`
- Stores `english_words` as JSON string
- Can be invoked directly:
```bash
python3 add_sample_words.py
```