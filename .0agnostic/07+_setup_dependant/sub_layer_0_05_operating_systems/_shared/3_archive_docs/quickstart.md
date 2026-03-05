---
resource_id: "b6671180-d90f-4ab8-9566-ca0412ec5c99"
resource_type: "document"
resource_name: "quickstart"
---
# Quickstart

<!-- section_id: "07c4f3ef-03cb-4f7b-98ad-898d24a99456" -->
## Prerequisites
- Python 3.9+

<!-- section_id: "92d5d3aa-ac35-4543-ae44-bd01aaf47231" -->
## Install
- No external dependencies are required beyond the standard library.
- Clone or open the repository.

<!-- section_id: "274fde1d-fd7f-41ad-8f7d-a7c92085aebc" -->
## Run the App
```bash
python3 main.py
```

On first run, the SQLite database `phonemes.db` will be created automatically.

<!-- section_id: "cf965e97-2f57-4a56-90d5-96beaad92f17" -->
## Common Tasks
- View phonemes: choose options 2–4 from the main menu
- Manage words: options 5–10
- Admin-only actions (password: `20251010`): choose option 1 → see admin menu

<!-- section_id: "8cfb09f2-a737-4ca5-94be-e6e0b8430aff" -->
## Sample Data
- Insert default phonemes: when prompted by viewing functions, select to insert sample data
- Insert sample words:
```bash
python3 add_sample_words.py
```

<!-- section_id: "cd8571ee-c16d-4b2b-8710-9858ed545995" -->
## Reset Database
Accessible via Admin menu → Reset database. See `docs/admin.md` for safety details.