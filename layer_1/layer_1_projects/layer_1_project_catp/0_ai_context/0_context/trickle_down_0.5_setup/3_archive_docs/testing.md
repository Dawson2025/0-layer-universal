---
resource_id: "5b3ee8d5-85ef-428a-bc79-dde53e4902c0"
resource_type: "document"
resource_name: "testing"
---
# Testing Guide

<!-- section_id: "c82aedfe-ec57-428c-9755-f8b86672876f" -->
## Overview
This repository includes multiple test scripts verifying menu structure, admin features, phoneme management, reset flow, and end-to-end workflows.

<!-- section_id: "7b10609a-d02c-44a1-a725-c31d203658a4" -->
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

<!-- section_id: "e2ebdd0d-1d20-492c-b7fa-00658dfe649f" -->
## Coverage Highlights
- Admin login and submenu flows
- Menu structure and numbering
- Add/delete phonemes with hierarchy and IDs
- Frequency adjustments and visibility
- Database reset safety flow
- Word CRUD and lookup flows
- JSON schema expectations for `english_words`

See `TESTING_RESULTS.md` for a summary of prior results.