---
resource_id: "b9375298-c961-4d21-bc9d-06393a125c68"
resource_type: "document"
resource_name: "quickstart"
---
# Quickstart

<!-- section_id: "e3ade3a3-ca91-469f-b915-23850c1e1c4b" -->
## Prerequisites
- Python 3.9+

<!-- section_id: "ecf9fe8e-8b5a-437d-9538-09582dcaf160" -->
## Install
- No external dependencies are required beyond the standard library.
- Clone or open the repository.

<!-- section_id: "c9ca8106-f95f-4f3e-b982-703bac949a57" -->
## Run the App
```bash
python3 main.py
```

On first run, the SQLite database `phonemes.db` will be created automatically.

<!-- section_id: "ce252080-7612-497a-96b4-0102bb0dd5ee" -->
## Common Tasks
- View phonemes: choose options 2–4 from the main menu
- Manage words: options 5–10
- Admin-only actions (password: `20251010`): choose option 1 → see admin menu

<!-- section_id: "01addeea-2d1c-42ef-a058-94e4d210d415" -->
## Sample Data
- Insert default phonemes: when prompted by viewing functions, select to insert sample data
- Insert sample words:
```bash
python3 add_sample_words.py
```

<!-- section_id: "44a856ed-1227-4901-88ea-4e287ef1069e" -->
## Reset Database
Accessible via Admin menu → Reset database. See `docs/admin.md` for safety details.