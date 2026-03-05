---
resource_id: "57d7097d-00cc-4191-b567-0a583ff15980"
resource_type: "document"
resource_name: "quickstart"
---
# Quickstart

<!-- section_id: "95376aaf-5458-48bc-8ea4-2fff579181cf" -->
## Prerequisites
- Python 3.9+

<!-- section_id: "23edf73a-918c-4ba0-81e8-9299dc402737" -->
## Install
- No external dependencies are required beyond the standard library.
- Clone or open the repository.

<!-- section_id: "28a975f9-c262-429f-bd37-6977121eb8f1" -->
## Run the App
```bash
python3 main.py
```

On first run, the SQLite database `phonemes.db` will be created automatically.

<!-- section_id: "6cd3e987-1687-48e6-a2e0-ca3f07df786f" -->
## Common Tasks
- View phonemes: choose options 2–4 from the main menu
- Manage words: options 5–10
- Admin-only actions (password: `20251010`): choose option 1 → see admin menu

<!-- section_id: "b7fba514-5988-4ca4-9836-62b8c3c0de7c" -->
## Sample Data
- Insert default phonemes: when prompted by viewing functions, select to insert sample data
- Insert sample words:
```bash
python3 add_sample_words.py
```

<!-- section_id: "c23a683e-318a-4709-bf62-11371686ed93" -->
## Reset Database
Accessible via Admin menu → Reset database. See `docs/admin.md` for safety details.