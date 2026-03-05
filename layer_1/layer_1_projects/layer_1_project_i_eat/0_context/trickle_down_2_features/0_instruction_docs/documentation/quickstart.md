---
resource_id: "e64fe144-ab1b-4cb4-8909-c3285d1ac40d"
resource_type: "document"
resource_name: "quickstart"
---
# Quickstart

<!-- section_id: "1c8600f2-797b-4710-a5c1-21d1a677c484" -->
## Prerequisites
- Python 3.9+

<!-- section_id: "9cfb5322-6f84-4bee-8d7b-18d8e0768523" -->
## Install
- No external dependencies are required beyond the standard library.
- Clone or open the repository.

<!-- section_id: "ff840905-e0af-405c-badd-c01008786b57" -->
## Run the App
```bash
python3 main.py
```

On first run, the SQLite database `phonemes.db` will be created automatically.

<!-- section_id: "7f792136-55f8-4783-96dd-efebe2b0b5dd" -->
## Common Tasks
- View phonemes: choose options 2–4 from the main menu
- Manage words: options 5–10
- Admin-only actions (password: `20251010`): choose option 1 → see admin menu

<!-- section_id: "572a065b-dbd9-4db9-b90f-445e6c0b5802" -->
## Sample Data
- Insert default phonemes: when prompted by viewing functions, select to insert sample data
- Insert sample words:
```bash
python3 add_sample_words.py
```

<!-- section_id: "de5f79bc-aaee-4317-9b34-d2e719ab7313" -->
## Reset Database
Accessible via Admin menu → Reset database. See `docs/admin.md` for safety details.