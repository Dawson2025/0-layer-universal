---
resource_id: "660f9a14-c329-42dd-b5a8-d26878c86308"
resource_type: "document"
resource_name: "database"
---
# Database Schema

SQLite database file: `phonemes.db`

<!-- section_id: "98bf784b-a24e-4caf-b858-4ec74d1aaea7" -->
## Tables

<!-- section_id: "afd5bb0a-8e9e-4cf4-ae20-fb3e99428bb1" -->
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

<!-- section_id: "95b0c621-f471-4f61-b252-62eec061de34" -->
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

<!-- section_id: "95d985a8-67ba-440e-9795-c3890f6e37d9" -->
## Ordering Logic
Functions use `get_sorted_phonemes()` to impose a fixed logical ordering across classification levels, then sort by aggregated frequencies within groups/subgroups.

<!-- section_id: "c1c74e27-d07b-47e3-8f0b-678d8c0bf04c" -->
## Migrations
- `migrate_schema()` creates tables and index if missing
- `migrate_existing_words_to_structured()` prints guidance for manual migration to structured fields

<!-- section_id: "e6414ac5-138e-43da-b79c-c929f9cd74a3" -->
## Sample Dataset
- See `flattened_dataset.py` for initial phoneme entries used by `insert_sample_data()`