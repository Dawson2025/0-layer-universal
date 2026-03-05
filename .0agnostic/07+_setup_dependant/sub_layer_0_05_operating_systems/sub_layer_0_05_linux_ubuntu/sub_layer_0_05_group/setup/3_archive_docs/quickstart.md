---
resource_id: "84138feb-6e4f-4bd0-8b68-15efd4dbb779"
resource_type: "document"
resource_name: "quickstart"
---
# Quickstart

<!-- section_id: "6b9fa515-fd82-4e8d-8721-72e29cd444d1" -->
## Prerequisites
- Python 3.9+

<!-- section_id: "2e9d8c3f-94a3-4d10-8273-0dae8c16178a" -->
## Install
- No external dependencies are required beyond the standard library.
- Clone or open the repository.

<!-- section_id: "e2ac4bea-7608-4d4b-831e-9b54bddf9270" -->
## Run the App
```bash
python3 main.py
```

On first run, the SQLite database `phonemes.db` will be created automatically.

<!-- section_id: "f3cc38a4-4fab-41b6-b9bf-fe65d6deed75" -->
## Common Tasks
- View phonemes: choose options 2–4 from the main menu
- Manage words: options 5–10
- Admin-only actions (password: `20251010`): choose option 1 → see admin menu

<!-- section_id: "dc7737c7-7144-495b-87d1-f38ad3112793" -->
## Sample Data
- Insert default phonemes: when prompted by viewing functions, select to insert sample data
- Insert sample words:
```bash
python3 add_sample_words.py
```

<!-- section_id: "b8a7dcb1-709f-4c97-836a-e2b107b59a1b" -->
## Reset Database
Accessible via Admin menu → Reset database. See `docs/admin.md` for safety details.