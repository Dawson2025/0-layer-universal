---
resource_id: "f2cef497-4a6c-4556-a774-f02112f65eb3"
resource_type: "document"
resource_name: "testing"
---
# Testing Guide

<!-- section_id: "69b0ff53-06c0-4392-af8a-2577b985a891" -->
## Overview
This repository includes multiple test scripts verifying menu structure, admin features, phoneme management, reset flow, and end-to-end workflows.

<!-- section_id: "cef20629-e5f2-4a16-96d1-0c918c56d06b" -->
## How to Run
- These tests are simple Python scripts using assertions; run directly:
```bash
python3 test_app.py | cat
python3 test_admin.py | cat
python3 test_menu.py | cat
python3 test_updated_menu.py | cat
python3 test_phoneme_management.py | cat
python3 test_enhanced_phonemes.py | cat
python3 test_reset_database.py | cat
python3 test_json_schema.py | cat
python3 verify_db.py | cat
python3 verify_menu.py | cat
python3 comprehensive_test.py | cat
python3 workflow_test.py | cat
```

- Use `| cat` to avoid pagers and ensure all output is printed.

<!-- section_id: "1c0c2974-5258-4681-b1ac-26a2e0cba67d" -->
## Coverage Highlights
- Admin login and submenu flows
- Menu structure and numbering
- Add/delete phonemes with hierarchy and IDs
- Frequency adjustments and visibility
- Database reset safety flow
- Word CRUD and lookup flows
- JSON schema expectations for `english_words`

See `TESTING_RESULTS.md` for a summary of prior results.