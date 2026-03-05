---
resource_id: "16bf03e8-c1a3-45a0-93c7-6819c4336948"
resource_type: "document"
resource_name: "quickstart"
---
# Quickstart

<!-- section_id: "5c58c6c4-9c43-4f19-9078-e9e2ee57ec73" -->
## Prerequisites
- Python 3.9+

<!-- section_id: "b8e33037-d204-49ae-a8dc-e793d3c37ab3" -->
## Install
- No external dependencies are required beyond the standard library.
- Clone or open the repository.

<!-- section_id: "5bb73636-a4cc-4601-bdab-473600ee334c" -->
## Run the App
```bash
python3 main.py
```

On first run, the SQLite database `phonemes.db` will be created automatically.

<!-- section_id: "6aacaa94-52ad-41a9-a9ae-aee86ea14e59" -->
## Common Tasks
- View phonemes: choose options 2–4 from the main menu
- Manage words: options 5–10
- Admin-only actions (password: `20251010`): choose option 1 → see admin menu

<!-- section_id: "7ffc175a-2869-4622-9cbb-82fb971c055b" -->
## Sample Data
- Insert default phonemes: when prompted by viewing functions, select to insert sample data
- Insert sample words:
```bash
python3 add_sample_words.py
```

<!-- section_id: "14421c54-32ba-4352-952b-62f79e364328" -->
## Reset Database
Accessible via Admin menu → Reset database. See `docs/admin.md` for safety details.