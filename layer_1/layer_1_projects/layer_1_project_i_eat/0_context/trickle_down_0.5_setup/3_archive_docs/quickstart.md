---
resource_id: "923b8c55-464e-46f1-af1f-4d3b60dc96c7"
resource_type: "document"
resource_name: "quickstart"
---
# Quickstart

<!-- section_id: "01815aa4-5615-4f4a-8a52-82dcab6b5217" -->
## Prerequisites
- Python 3.9+

<!-- section_id: "9eed196f-ab7c-48ea-a27a-cca891d6e9eb" -->
## Install
- No external dependencies are required beyond the standard library.
- Clone or open the repository.

<!-- section_id: "82ccf180-ac19-47c0-a632-57eef51dc021" -->
## Run the App
```bash
python3 main.py
```

On first run, the SQLite database `phonemes.db` will be created automatically.

<!-- section_id: "12a53f24-a81c-4b22-a8b8-3811f5e5b842" -->
## Common Tasks
- View phonemes: choose options 2–4 from the main menu
- Manage words: options 5–10
- Admin-only actions (password: `20251010`): choose option 1 → see admin menu

<!-- section_id: "d25b0919-c391-4f37-bc79-fcdff7cea66a" -->
## Sample Data
- Insert default phonemes: when prompted by viewing functions, select to insert sample data
- Insert sample words:
```bash
python3 add_sample_words.py
```

<!-- section_id: "5f978fcf-d27f-4d9f-b0d9-9499803d89a9" -->
## Reset Database
Accessible via Admin menu → Reset database. See `docs/admin.md` for safety details.