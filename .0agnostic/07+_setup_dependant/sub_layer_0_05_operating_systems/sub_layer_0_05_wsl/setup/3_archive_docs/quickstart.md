---
resource_id: "8447d2f2-5bda-4876-a5f3-aa2542c1e9f0"
resource_type: "document"
resource_name: "quickstart"
---
# Quickstart

<!-- section_id: "9fca2fe0-ae69-452b-a3d3-a2a4bc87508b" -->
## Prerequisites
- Python 3.9+

<!-- section_id: "e597b311-b57d-463d-ab83-69e4a41bb9e5" -->
## Install
- No external dependencies are required beyond the standard library.
- Clone or open the repository.

<!-- section_id: "d2069f55-58ce-4989-af4b-a203f21e212e" -->
## Run the App
```bash
python3 main.py
```

On first run, the SQLite database `phonemes.db` will be created automatically.

<!-- section_id: "5df11a3c-7950-433f-98ea-119218718377" -->
## Common Tasks
- View phonemes: choose options 2–4 from the main menu
- Manage words: options 5–10
- Admin-only actions (password: `20251010`): choose option 1 → see admin menu

<!-- section_id: "722d6be4-9654-452a-830b-876d52672bc4" -->
## Sample Data
- Insert default phonemes: when prompted by viewing functions, select to insert sample data
- Insert sample words:
```bash
python3 add_sample_words.py
```

<!-- section_id: "f43be4a5-52fd-4add-9c72-eb7b47008783" -->
## Reset Database
Accessible via Admin menu → Reset database. See `docs/admin.md` for safety details.