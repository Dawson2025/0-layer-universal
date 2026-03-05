---
resource_id: "fd1f8010-f4be-4834-b52b-9037736ff458"
resource_type: "document"
resource_name: "database"
---
# Database Schema

SQLite database file: `phonemes.db`

<!-- section_id: "fe076b83-ab6d-411b-859b-5247a225c7ba" -->
## Tables

<!-- section_id: "bef1e367-1cf3-4b79-a778-28de507eaf6f" -->
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

<!-- section_id: "a82a0269-d257-44f6-9594-29b156e6c93a" -->
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

<!-- section_id: "b9a5d885-a43f-4577-a7dc-72c9613079df" -->
## Ordering Logic
Functions use `get_sorted_phonemes()` to impose a fixed logical ordering across classification levels, then sort by aggregated frequencies within groups/subgroups.

<!-- section_id: "d3191745-3d94-4ca3-bda8-4e9e0ee88c45" -->
## Migrations
- `migrate_schema()` creates tables and index if missing
- `migrate_existing_words_to_structured()` prints guidance for manual migration to structured fields

<!-- section_id: "ae2c001b-6fa8-403c-be5c-dd11bc334764" -->
## Sample Dataset
- See `flattened_dataset.py` for initial phoneme entries used by `insert_sample_data()`