---
resource_id: "8ac4906b-7319-45c5-8f73-113c2b75a266"
resource_type: "document"
resource_name: "utilities"
---
# API Reference: Utilities

<!-- section_id: "f09efe10-3a40-4807-b032-b0b386db2519" -->
## `flattened_dataset.py`
- Exports `flattened_dataset: list[dict]` with keys:
  - `syllable_type`, `position`, `length_type`, `group_type`, `subgroup_type`, `phoneme`, `frequency`
- Used by `insert_sample_data()` to seed the database

<!-- section_id: "30ebc0b9-f65e-4f15-9362-50042cd622a6" -->
## `flatten_syllables.py`
- Utility script to convert hierarchical `syllable_making_dataset` (from `sample_data.py`) into a flat list
- Key function: `recurse(path: dict, data: Any)` populates an internal `grouped` structure
- Writes out `flattened_dataset.py` after user confirmation if overwriting

<!-- section_id: "b4a37198-2eac-4c93-a76c-6c62a1b2d2fb" -->
## `add_sample_words.py`
- Function: `add_sample_words()` inserts example word rows into `words`
- Stores `english_words` as JSON string
- Can be invoked directly:
```bash
python3 add_sample_words.py
```