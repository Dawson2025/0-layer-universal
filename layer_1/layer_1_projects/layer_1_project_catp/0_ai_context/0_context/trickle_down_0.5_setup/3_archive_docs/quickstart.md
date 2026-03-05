---
resource_id: "2f1ed28c-d67c-4f4f-9ad2-051398e10b71"
resource_type: "document"
resource_name: "quickstart"
---
# Quickstart

<!-- section_id: "39cbe2f2-15d2-4c85-9b62-5117e5867069" -->
## Prerequisites
- Python 3.9+

<!-- section_id: "ec59d5e0-87fa-4a36-a885-737da882bc23" -->
## Install
- No external dependencies are required beyond the standard library.
- Clone or open the repository.

<!-- section_id: "e61e8df1-7c93-485c-8744-e99f77381d0b" -->
## Run the App
```bash
python3 main.py
```

On first run, the SQLite database `phonemes.db` will be created automatically.

<!-- section_id: "ca3898b1-8c84-40b6-8533-84fe38621bd2" -->
## Common Tasks
- View phonemes: choose options 2–4 from the main menu
- Manage words: options 5–10
- Admin-only actions (password: `20251010`): choose option 1 → see admin menu

<!-- section_id: "bcff26e4-73ed-438a-b51d-1eab4f9284da" -->
## Sample Data
- Insert default phonemes: when prompted by viewing functions, select to insert sample data
- Insert sample words:
```bash
python3 add_sample_words.py
```

<!-- section_id: "4c2379f2-1397-43cb-b4ad-8cadeb752c33" -->
## Reset Database
Accessible via Admin menu → Reset database. See `docs/admin.md` for safety details.