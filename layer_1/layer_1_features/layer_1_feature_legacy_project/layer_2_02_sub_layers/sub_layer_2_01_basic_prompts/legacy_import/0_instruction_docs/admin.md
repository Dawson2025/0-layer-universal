---
resource_id: "27e9b1a6-10f9-4591-91bf-66795e0f6f44"
resource_type: "document"
resource_name: "admin"
---
# Admin Guide

<!-- section_id: "b90ef573-f086-477c-8f38-cc2a42257445" -->
## Access
- Select "Admin Commands" from the main menu
- Enter password: `20251010`

<!-- section_id: "6be59c9b-5ea2-43f7-a184-8932df391ed2" -->
## Admin Features
1. Add new phoneme
2. Delete phoneme
3. Increase frequency
4. Decrease frequency
5. Reset database
6. Back to main menu

<!-- section_id: "140ef712-3634-4456-b788-6abc09d62254" -->
## Add/Delete Phonemes
- Add flow shows existing group/subgroup types with numeric selection
- Delete flow lists phonemes hierarchically with numeric selection
- Both use the app's fixed ordering and enforce database constraints

<!-- section_id: "2b20026c-6e0c-409d-9374-5e69eeff5954" -->
## Frequency Adjustments
- Increase/decrease frequency for selected phonemes
- Available to admins only

<!-- section_id: "b0cf47e7-1223-4594-9c88-52c3107e7877" -->
## Reset Database (Safety)
- Dramatic warning + two-step confirmation
- Displays current counts of phonemes and words before final confirmation
- Must type exactly: `DELETE EVERYTHING`
- Recreates an empty database on success

For full rationale and UI examples:
- See `ENHANCED_RESET_SUMMARY.md`
- See `ADMIN_IMPLEMENTATION.md`
- See `MENU_RESTRUCTURE_FINAL.md`