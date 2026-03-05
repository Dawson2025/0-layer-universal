---
resource_id: "17fd7700-35e6-4b52-8375-f1f81ee118fb"
resource_type: "document"
resource_name: "utilities"
---
# API Reference: Utilities

<!-- section_id: "5631672d-6d22-43d1-a170-7345575fa71b" -->
## `flattened_dataset.py`
- Exports `flattened_dataset: list[dict]` with keys:
  - `syllable_type`, `position`, `length_type`, `group_type`, `subgroup_type`, `phoneme`, `frequency`
- Used by `insert_sample_data()` to seed the database

<!-- section_id: "112d72af-848f-4297-8122-fbf217c14130" -->
## `flatten_syllables.py`
- Utility script to convert hierarchical `syllable_making_dataset` (from `sample_data.py`) into a flat list
- Key function: `recurse(path: dict, data: Any)` populates an internal `grouped` structure
- Writes out `flattened_dataset.py` after user confirmation if overwriting

<!-- section_id: "64a6917d-33fe-4ed2-8c97-b66985681b90" -->
## `add_sample_words.py`
- Function: `add_sample_words()` inserts example word rows into `words`
- Stores `english_words` as JSON string
- Can be invoked directly:
```bash
python3 add_sample_words.py
```