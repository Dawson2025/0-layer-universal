---
resource_id: "c014f5fe-0092-4866-8e02-29c1ea40e178"
resource_type: "document"
resource_name: "quickstart"
---
# Quickstart

<!-- section_id: "88195e00-cda1-4f14-a14c-3d4c177c5a00" -->
## Prerequisites
- Python 3.9+

<!-- section_id: "858f31fe-bb9f-47d1-8b87-a36fae0a9d8e" -->
## Install
- No external dependencies are required beyond the standard library.
- Clone or open the repository.

<!-- section_id: "2f8c0c7b-f61b-4f6d-875b-4ec3e5b8e948" -->
## Run the App
```bash
python3 main.py
```

On first run, the SQLite database `phonemes.db` will be created automatically.

<!-- section_id: "4df76ac9-32d7-4d81-b6ad-c5276c0f060c" -->
## Common Tasks
- View phonemes: choose options 2–4 from the main menu
- Manage words: options 5–10
- Admin-only actions (password: `20251010`): choose option 1 → see admin menu

<!-- section_id: "4cd4d390-c527-469b-8d25-e4b552a7f3f2" -->
## Sample Data
- Insert default phonemes: when prompted by viewing functions, select to insert sample data
- Insert sample words:
```bash
python3 add_sample_words.py
```

<!-- section_id: "0247e85c-a329-4f7e-9fc8-11d136bfb27c" -->
## Reset Database
Accessible via Admin menu → Reset database. See `docs/admin.md` for safety details.