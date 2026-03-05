---
resource_id: "df3700c2-ca48-4f0d-85d5-e6ee5ab3788c"
resource_type: "document"
resource_name: "utilities"
---
# API Reference: Utilities

<!-- section_id: "a42656c9-4f64-4c3d-a686-3e13e7f60617" -->
## `flattened_dataset.py`
- Exports `flattened_dataset: list[dict]` with keys:
  - `syllable_type`, `position`, `length_type`, `group_type`, `subgroup_type`, `phoneme`, `frequency`
- Used by `insert_sample_data()` to seed the database

<!-- section_id: "9a254550-c593-4097-a1ba-c963a9c84268" -->
## `flatten_syllables.py`
- Utility script to convert hierarchical `syllable_making_dataset` (from `sample_data.py`) into a flat list
- Key function: `recurse(path: dict, data: Any)` populates an internal `grouped` structure
- Writes out `flattened_dataset.py` after user confirmation if overwriting

<!-- section_id: "0e6dd38d-2ffb-4f3e-bee8-aaaf1703b3d3" -->
## `add_sample_words.py`
- Function: `add_sample_words()` inserts example word rows into `words`
- Stores `english_words` as JSON string
- Can be invoked directly:
```bash
python3 add_sample_words.py
```



