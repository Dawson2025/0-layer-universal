---
resource_id: "e46299ef-089e-4004-92a1-142f16213a81"
resource_type: "document"
resource_name: "testing"
---
# Testing Guide

<!-- section_id: "bcbaf3aa-594e-4b24-ac63-1d6ac47874cb" -->
## Overview
This repository includes multiple test scripts verifying menu structure, admin features, phoneme management, reset flow, and end-to-end workflows.

<!-- section_id: "26235db1-8155-4cdc-a3f6-a8fc9d761dfe" -->
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

<!-- section_id: "465344c5-07a5-48c2-9943-10a8398c2550" -->
## Coverage Highlights
- Admin login and submenu flows
- Menu structure and numbering
- Add/delete phonemes with hierarchy and IDs
- Frequency adjustments and visibility
- Database reset safety flow
- Word CRUD and lookup flows
- JSON schema expectations for `english_words`

See `TESTING_RESULTS.md` for a summary of prior results.