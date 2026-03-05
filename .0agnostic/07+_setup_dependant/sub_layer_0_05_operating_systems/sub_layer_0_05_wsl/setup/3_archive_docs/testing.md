---
resource_id: "288cea02-f3bf-4de8-8005-fb0ff28cc350"
resource_type: "document"
resource_name: "testing"
---
# Testing Guide

<!-- section_id: "d0c06179-4a31-48fc-8b85-f559e70ac99d" -->
## Overview
This repository includes multiple test scripts verifying menu structure, admin features, phoneme management, reset flow, and end-to-end workflows.

<!-- section_id: "6636d8c7-0bca-42fd-a0b6-5a4c5dea4dd6" -->
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

<!-- section_id: "cf626a21-8ce2-4868-af7b-5624fd757afc" -->
## Coverage Highlights
- Admin login and submenu flows
- Menu structure and numbering
- Add/delete phonemes with hierarchy and IDs
- Frequency adjustments and visibility
- Database reset safety flow
- Word CRUD and lookup flows
- JSON schema expectations for `english_words`

See `TESTING_RESULTS.md` for a summary of prior results.