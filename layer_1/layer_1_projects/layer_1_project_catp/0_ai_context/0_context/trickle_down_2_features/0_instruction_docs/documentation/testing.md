---
resource_id: "ca09f93d-a37e-44cb-b0a5-72cfc6cfb20d"
resource_type: "document"
resource_name: "testing"
---
# Testing Guide

<!-- section_id: "811bc07f-c410-4d27-9996-464e6e50f845" -->
## Overview
This repository includes multiple test scripts verifying menu structure, admin features, phoneme management, reset flow, and end-to-end workflows.

<!-- section_id: "6efb6993-2e4f-4ea1-9c67-884931df6c15" -->
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

<!-- section_id: "821d8817-34cc-416e-8c24-ad01e31dd790" -->
## Coverage Highlights
- Admin login and submenu flows
- Menu structure and numbering
- Add/delete phonemes with hierarchy and IDs
- Frequency adjustments and visibility
- Database reset safety flow
- Word CRUD and lookup flows
- JSON schema expectations for `english_words`

See `TESTING_RESULTS.md` for a summary of prior results.