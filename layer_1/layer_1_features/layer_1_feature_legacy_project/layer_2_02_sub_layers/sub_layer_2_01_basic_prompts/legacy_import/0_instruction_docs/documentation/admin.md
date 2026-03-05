---
resource_id: "9b0c2444-2c84-48e0-bf80-d1e378b593f4"
resource_type: "document"
resource_name: "admin"
---
# Admin Guide

<!-- section_id: "0343b713-49c4-4e0c-aeae-5ad52ae4af38" -->
## Access
- Select "Admin Commands" from the main menu
- Enter password: `20251010`

<!-- section_id: "68c153b0-e0e5-4ca7-82b4-93fec139d93d" -->
## Admin Features
1. Add new phoneme
2. Delete phoneme
3. Increase frequency
4. Decrease frequency
5. Reset database
6. Back to main menu

<!-- section_id: "f2b38166-815e-41e9-8627-0caff68b32b5" -->
## Add/Delete Phonemes
- Add flow shows existing group/subgroup types with numeric selection
- Delete flow lists phonemes hierarchically with numeric selection
- Both use the app's fixed ordering and enforce database constraints

<!-- section_id: "994b8353-be4d-48f7-a3fb-166ad6b19cb2" -->
## Frequency Adjustments
- Increase/decrease frequency for selected phonemes
- Available to admins only

<!-- section_id: "9c690237-cfb7-4b76-b420-bd05ea3697c8" -->
## Reset Database (Safety)
- Dramatic warning + two-step confirmation
- Displays current counts of phonemes and words before final confirmation
- Must type exactly: `DELETE EVERYTHING`
- Recreates an empty database on success

For full rationale and UI examples:
- See `ENHANCED_RESET_SUMMARY.md`
- See `ADMIN_IMPLEMENTATION.md`
- See `MENU_RESTRUCTURE_FINAL.md`