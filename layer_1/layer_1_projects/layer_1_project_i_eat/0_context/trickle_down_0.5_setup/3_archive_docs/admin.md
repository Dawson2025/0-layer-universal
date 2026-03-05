---
resource_id: "b00a4628-b75b-4ff3-b099-aec45037db77"
resource_type: "document"
resource_name: "admin"
---
# Admin Guide

<!-- section_id: "1b6fba1f-360a-471e-8aca-3c6d92c0fb7b" -->
## Access
- Select "Admin Commands" from the main menu
- Enter password: `20251010`

<!-- section_id: "81dab388-f1e6-4338-80eb-705b4b81b84e" -->
## Admin Features
1. Add new phoneme
2. Delete phoneme
3. Increase frequency
4. Decrease frequency
5. Reset database
6. Back to main menu

<!-- section_id: "b0202675-792f-4fda-84e3-cb8d38557822" -->
## Add/Delete Phonemes
- Add flow shows existing group/subgroup types with numeric selection
- Delete flow lists phonemes hierarchically with numeric selection
- Both use the app's fixed ordering and enforce database constraints

<!-- section_id: "6267649d-bda4-4e7c-842e-ecb4f45571af" -->
## Frequency Adjustments
- Increase/decrease frequency for selected phonemes
- Available to admins only

<!-- section_id: "5498012c-e97b-4e86-89cc-2bd8e6357352" -->
## Reset Database (Safety)
- Dramatic warning + two-step confirmation
- Displays current counts of phonemes and words before final confirmation
- Must type exactly: `DELETE EVERYTHING`
- Recreates an empty database on success

For full rationale and UI examples:
- See `ENHANCED_RESET_SUMMARY.md`
- See `ADMIN_IMPLEMENTATION.md`
- See `MENU_RESTRUCTURE_FINAL.md`