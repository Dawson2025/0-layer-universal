---
resource_id: "3d41dd73-d764-4e5a-8c39-bda12400e041"
resource_type: "document"
resource_name: "utilities"
---
# API Reference: Utilities

<!-- section_id: "211adaee-fb51-4818-ac7e-48aa56ab019e" -->
## `flattened_dataset.py`
- Exports `flattened_dataset: list[dict]` with keys:
  - `syllable_type`, `position`, `length_type`, `group_type`, `subgroup_type`, `phoneme`, `frequency`
- Used by `insert_sample_data()` to seed the database

<!-- section_id: "1bbf0395-0961-4400-824e-0c723ac6dbfe" -->
## `flatten_syllables.py`
- Utility script to convert hierarchical `syllable_making_dataset` (from `sample_data.py`) into a flat list
- Key function: `recurse(path: dict, data: Any)` populates an internal `grouped` structure
- Writes out `flattened_dataset.py` after user confirmation if overwriting

<!-- section_id: "e32720e1-69c9-4a23-b104-62abf7087b7d" -->
## `add_sample_words.py`
- Function: `add_sample_words()` inserts example word rows into `words`
- Stores `english_words` as JSON string
- Can be invoked directly:
```bash
python3 add_sample_words.py
```



