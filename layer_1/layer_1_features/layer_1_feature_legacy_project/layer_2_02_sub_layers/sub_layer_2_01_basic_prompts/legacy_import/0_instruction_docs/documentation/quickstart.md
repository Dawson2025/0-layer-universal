---
resource_id: "81f34123-8b01-403c-a2e0-d2238f4857b4"
resource_type: "document"
resource_name: "quickstart"
---
# Quickstart

<!-- section_id: "bb4c53d6-5372-4b08-ba71-f2d633d60cb4" -->
## Prerequisites
- Python 3.9+

<!-- section_id: "c645b92f-00ec-43e1-b51d-a9c9a5f573c0" -->
## Install
- No external dependencies are required beyond the standard library.
- Clone or open the repository.

<!-- section_id: "827de1b4-9625-47c8-9a4a-9ceda7b34b87" -->
## Run the App
```bash
python3 main.py
```

On first run, the SQLite database `phonemes.db` will be created automatically.

<!-- section_id: "1098b4e1-21b6-44af-add3-8c811af6d705" -->
## Common Tasks
- View phonemes: choose options 2–4 from the main menu
- Manage words: options 5–10
- Admin-only actions (password: `20251010`): choose option 1 → see admin menu

<!-- section_id: "18c9ca56-6fe4-4a0b-8786-3b2719611b9d" -->
## Sample Data
- Insert default phonemes: when prompted by viewing functions, select to insert sample data
- Insert sample words:
```bash
python3 add_sample_words.py
```

<!-- section_id: "a89db63b-6710-45dc-a844-7b2932518af0" -->
## Reset Database
Accessible via Admin menu → Reset database. See `docs/admin.md` for safety details.