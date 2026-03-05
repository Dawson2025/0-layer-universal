---
resource_id: "0a7bd3f2-b847-4c70-b789-9d4708246004"
resource_type: "document"
resource_name: "database"
---
# Database Schema

SQLite database file: `phonemes.db`

<!-- section_id: "41ba3b6a-62fb-45a6-b475-e41fb914c598" -->
## Tables

<!-- section_id: "7f8dd542-7c66-4c4a-9eb5-7acac306d5e4" -->
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

<!-- section_id: "ba08914c-815a-465e-8b87-44768c5feaa3" -->
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

<!-- section_id: "8302da8c-9232-4c8e-8d0a-c5b4bc7c35c0" -->
## Ordering Logic
Functions use `get_sorted_phonemes()` to impose a fixed logical ordering across classification levels, then sort by aggregated frequencies within groups/subgroups.

<!-- section_id: "1972d168-c933-4b30-9b9c-9ce2f963952d" -->
## Migrations
- `migrate_schema()` creates tables and index if missing
- `migrate_existing_words_to_structured()` prints guidance for manual migration to structured fields

<!-- section_id: "2c24e1a9-0860-4877-b869-506386a5a781" -->
## Sample Dataset
- See `flattened_dataset.py` for initial phoneme entries used by `insert_sample_data()`