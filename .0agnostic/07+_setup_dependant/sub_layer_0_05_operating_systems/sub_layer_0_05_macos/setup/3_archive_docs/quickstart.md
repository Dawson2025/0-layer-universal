---
resource_id: "52b01323-3a90-4fe3-9867-23f45ae78d86"
resource_type: "document"
resource_name: "quickstart"
---
# Quickstart

<!-- section_id: "e91f95ba-595b-4393-94d4-806809b40f0a" -->
## Prerequisites
- Python 3.9+

<!-- section_id: "68946e33-e26c-4f33-a568-368bbced0da8" -->
## Install
- No external dependencies are required beyond the standard library.
- Clone or open the repository.

<!-- section_id: "73833abe-99fe-482a-80f4-1313cd3ca48a" -->
## Run the App
```bash
python3 main.py
```

On first run, the SQLite database `phonemes.db` will be created automatically.

<!-- section_id: "5e3ec08d-d97e-48a3-a601-7d0d8060ea5d" -->
## Common Tasks
- View phonemes: choose options 2–4 from the main menu
- Manage words: options 5–10
- Admin-only actions (password: `20251010`): choose option 1 → see admin menu

<!-- section_id: "ac273e29-c0ca-47f0-b8c7-ef3f910778d6" -->
## Sample Data
- Insert default phonemes: when prompted by viewing functions, select to insert sample data
- Insert sample words:
```bash
python3 add_sample_words.py
```

<!-- section_id: "712266b2-75ba-4137-9bf1-c1036a12e193" -->
## Reset Database
Accessible via Admin menu → Reset database. See `docs/admin.md` for safety details.