---
resource_id: "9e6dde43-b212-473e-bdfe-3ac32ae5d9fa"
resource_type: "document"
resource_name: "admin"
---
# Admin Guide

<!-- section_id: "8838b167-fc37-42b6-8746-43880f1c8486" -->
## Access
- Select "Admin Commands" from the main menu
- Enter password: `20251010`

<!-- section_id: "4282c78f-057f-4805-8e1a-2eda6f53b6a2" -->
## Admin Features
1. Add new phoneme
2. Delete phoneme
3. Increase frequency
4. Decrease frequency
5. Reset database
6. Back to main menu

<!-- section_id: "2bbb64a3-c29f-4b21-9dca-15e273288170" -->
## Add/Delete Phonemes
- Add flow shows existing group/subgroup types with numeric selection
- Delete flow lists phonemes hierarchically with numeric selection
- Both use the app's fixed ordering and enforce database constraints

<!-- section_id: "3c5dcbb8-8aa3-4e77-9c9b-0eb3db7fea13" -->
## Frequency Adjustments
- Increase/decrease frequency for selected phonemes
- Available to admins only

<!-- section_id: "6e2f45a5-b5fc-4676-95c6-976f135ee4d3" -->
## Reset Database (Safety)
- Dramatic warning + two-step confirmation
- Displays current counts of phonemes and words before final confirmation
- Must type exactly: `DELETE EVERYTHING`
- Recreates an empty database on success

For full rationale and UI examples:
- See `ENHANCED_RESET_SUMMARY.md`
- See `ADMIN_IMPLEMENTATION.md`
- See `MENU_RESTRUCTURE_FINAL.md`