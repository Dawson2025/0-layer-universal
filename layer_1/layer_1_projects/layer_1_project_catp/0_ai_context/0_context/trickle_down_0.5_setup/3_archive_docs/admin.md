---
resource_id: "7efed79b-9f0e-4511-971d-31216519e870"
resource_type: "document"
resource_name: "admin"
---
# Admin Guide

<!-- section_id: "50fabd4c-0479-46af-ad0e-512717c40a4e" -->
## Access
- Select "Admin Commands" from the main menu
- Enter password: `20251010`

<!-- section_id: "524dbdc5-07aa-47a7-9bea-0a6147d85ff6" -->
## Admin Features
1. Add new phoneme
2. Delete phoneme
3. Increase frequency
4. Decrease frequency
5. Reset database
6. Back to main menu

<!-- section_id: "047594d8-c9a0-46a1-b9f1-55c24b9fcca6" -->
## Add/Delete Phonemes
- Add flow shows existing group/subgroup types with numeric selection
- Delete flow lists phonemes hierarchically with numeric selection
- Both use the app's fixed ordering and enforce database constraints

<!-- section_id: "fda0a325-ab9b-4aef-909c-caefd0c5687e" -->
## Frequency Adjustments
- Increase/decrease frequency for selected phonemes
- Available to admins only

<!-- section_id: "44ef6587-02e8-4862-8ca5-1e26c0b278a9" -->
## Reset Database (Safety)
- Dramatic warning + two-step confirmation
- Displays current counts of phonemes and words before final confirmation
- Must type exactly: `DELETE EVERYTHING`
- Recreates an empty database on success

For full rationale and UI examples:
- See `ENHANCED_RESET_SUMMARY.md`
- See `ADMIN_IMPLEMENTATION.md`
- See `MENU_RESTRUCTURE_FINAL.md`