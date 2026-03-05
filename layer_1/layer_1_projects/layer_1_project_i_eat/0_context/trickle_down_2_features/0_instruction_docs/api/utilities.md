---
resource_id: "1461c831-11ee-4b3f-a8c9-680192e09664"
resource_type: "document"
resource_name: "utilities"
---
# API Reference: Utilities

<!-- section_id: "fac45056-bd7c-4606-b0e4-327b1c257252" -->
## `flattened_dataset.py`
- Exports `flattened_dataset: list[dict]` with keys:
  - `syllable_type`, `position`, `length_type`, `group_type`, `subgroup_type`, `phoneme`, `frequency`
- Used by `insert_sample_data()` to seed the database

<!-- section_id: "23b3a3d7-47a1-4e1c-af72-0275b4e88a89" -->
## `flatten_syllables.py`
- Utility script to convert hierarchical `syllable_making_dataset` (from `sample_data.py`) into a flat list
- Key function: `recurse(path: dict, data: Any)` populates an internal `grouped` structure
- Writes out `flattened_dataset.py` after user confirmation if overwriting

<!-- section_id: "936f516e-6a36-43f0-a32a-7d40b47860c9" -->
## `add_sample_words.py`
- Function: `add_sample_words()` inserts example word rows into `words`
- Stores `english_words` as JSON string
- Can be invoked directly:
```bash
python3 add_sample_words.py
```



