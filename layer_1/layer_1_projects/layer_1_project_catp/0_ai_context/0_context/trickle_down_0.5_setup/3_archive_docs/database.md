---
resource_id: "9311caa0-ab77-4244-906d-158da3cfc4f0"
resource_type: "document"
resource_name: "database"
---
# Database Schema

SQLite database file: `phonemes.db`

<!-- section_id: "5d2fd8a4-9af3-4ef0-b9b7-1f6bb4f1d690" -->
## Tables

<!-- section_id: "46b28930-f706-4161-8657-35b82fb609c4" -->
### phonemes
```sql
CREATE TABLE IF NOT EXISTS phonemes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    syllable_type TEXT,
    position TEXT,
    length_type TEXT,
    group_type TEXT,
    subgroup_type TEXT,
    phoneme TEXT,
    frequency INTEGER DEFAULT 0
);

CREATE UNIQUE INDEX IF NOT EXISTS idx_unique_phoneme
ON phonemes (syllable_type, position, length_type, group_type, subgroup_type, phoneme);
```

- **syllable_type**: `CVC` or `CV`
- **position**: `onset`, `nucleus`, `coda` (no `coda` for `CV`)
- **length_type**:
  - For onset/coda: `single_consonants` | `cluster2` | `cluster3`
  - For nucleus: `monophthongs` | `diphthongs`
- **group_type**: E.g., `Stops`, `Fricatives`, `High`, `Low` (varies by position)
- **subgroup_type**: Optional; use `NULL` or `none`
- **phoneme**: Symbol (e.g., `p`, `a`, `aɪ`)
- **frequency**: Integer counter

<!-- section_id: "7696c3b3-23fc-4dc9-8d9c-ae70bb1dc115" -->
### words
```sql
CREATE TABLE IF NOT EXISTS words (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    language TEXT,
    english_words TEXT,           -- JSON list of strings
    new_language_word TEXT,
    ipa_phonetics TEXT,
    dictionary_phonetics TEXT,
    syllable_type TEXT,           -- optional structured data
    onset_phoneme TEXT,
    onset_length_type TEXT,
    nucleus_phoneme TEXT,
    nucleus_length_type TEXT,
    coda_phoneme TEXT,
    coda_length_type TEXT
);
```

- **english_words** is stored as JSON (list of translations)
- Structured phoneme fields are optional and populated by creation/edit flows

<!-- section_id: "7e68d317-e3b6-466d-8274-94e757ebf8a4" -->
## Ordering Logic
Functions use `get_sorted_phonemes()` to impose a fixed logical ordering across classification levels, then sort by aggregated frequencies within groups/subgroups.

<!-- section_id: "21a9366c-3d7b-4e3a-a51a-a16a16095eff" -->
## Migrations
- `migrate_schema()` creates tables and index if missing
- `migrate_existing_words_to_structured()` prints guidance for manual migration to structured fields

<!-- section_id: "7c585e64-bca1-4daa-a6a6-80ae3286929f" -->
## Sample Dataset
- See `flattened_dataset.py` for initial phoneme entries used by `insert_sample_data()`