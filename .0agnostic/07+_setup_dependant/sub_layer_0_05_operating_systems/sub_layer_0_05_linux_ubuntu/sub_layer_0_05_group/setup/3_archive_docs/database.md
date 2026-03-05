---
resource_id: "3a9a68c4-4c23-413e-bfb9-308fbef8f6a9"
resource_type: "document"
resource_name: "database"
---
# Database Schema

SQLite database file: `phonemes.db`

<!-- section_id: "201ebda0-a57d-4ab3-8318-c60a2aee310a" -->
## Tables

<!-- section_id: "9729d610-6192-48aa-9c33-ef97d9aaf1a4" -->
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

<!-- section_id: "d5f4b3f5-3921-4dd7-b5c8-544d092181ea" -->
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

<!-- section_id: "1204e474-6d0c-4858-b06a-1925cf893bf3" -->
## Ordering Logic
Functions use `get_sorted_phonemes()` to impose a fixed logical ordering across classification levels, then sort by aggregated frequencies within groups/subgroups.

<!-- section_id: "57254e73-dc33-4239-8809-75f9c18d870b" -->
## Migrations
- `migrate_schema()` creates tables and index if missing
- `migrate_existing_words_to_structured()` prints guidance for manual migration to structured fields

<!-- section_id: "daa0bf3a-4708-4707-9639-514b67f9dab0" -->
## Sample Dataset
- See `flattened_dataset.py` for initial phoneme entries used by `insert_sample_data()`