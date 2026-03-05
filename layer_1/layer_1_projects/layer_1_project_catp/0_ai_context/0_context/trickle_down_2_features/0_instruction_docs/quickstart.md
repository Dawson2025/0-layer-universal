---
resource_id: "758e87d2-e60c-4fe4-b816-214aaa531d4a"
resource_type: "document"
resource_name: "quickstart"
---
# Quickstart

<!-- section_id: "94947893-18c3-41e2-b7c7-2ba321f05b53" -->
## Prerequisites
- Python 3.9+

<!-- section_id: "63fd5aac-0007-4857-b558-6bf70af5e7cd" -->
## Install
- No external dependencies are required beyond the standard library.
- Clone or open the repository.

<!-- section_id: "4163df99-bdbd-4c4f-98a1-9a9ff30982a3" -->
## Run the App
```bash
python3 main.py
```

On first run, the SQLite database `phonemes.db` will be created automatically.

<!-- section_id: "f0cbcd2f-904f-4080-8a44-d23f3601d92b" -->
## Common Tasks
- View phonemes: choose options 2–4 from the main menu
- Manage words: options 5–10
- Admin-only actions (password: `20251010`): choose option 1 → see admin menu

<!-- section_id: "3c6f5b56-9ee8-4c7f-9834-c6ed6bb86de5" -->
## Sample Data
- Insert default phonemes: when prompted by viewing functions, select to insert sample data
- Insert sample words:
```bash
python3 add_sample_words.py
```

<!-- section_id: "1a3279e8-ee67-480d-99e6-4bdc4860a4d1" -->
## Reset Database
Accessible via Admin menu → Reset database. See `docs/admin.md` for safety details.