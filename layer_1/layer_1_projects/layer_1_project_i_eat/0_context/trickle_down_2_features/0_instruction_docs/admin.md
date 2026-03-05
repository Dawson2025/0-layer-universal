---
resource_id: "a77d192d-9912-4959-8197-5e026d08e089"
resource_type: "document"
resource_name: "admin"
---
# Admin Guide

<!-- section_id: "80717eb7-f2cf-4908-a3c6-fad81c6b1613" -->
## Access
- Select "Admin Commands" from the main menu
- Enter password: `20251010`

<!-- section_id: "fffa5ed5-50d0-407e-8604-bb8d8ca87a59" -->
## Admin Features
1. Add new phoneme
2. Delete phoneme
3. Increase frequency
4. Decrease frequency
5. Reset database
6. Back to main menu

<!-- section_id: "bf2f82b1-b6df-448b-ba0b-0249a2fd9c92" -->
## Add/Delete Phonemes
- Add flow shows existing group/subgroup types with numeric selection
- Delete flow lists phonemes hierarchically with numeric selection
- Both use the app's fixed ordering and enforce database constraints

<!-- section_id: "355504a4-1187-4fd2-8138-4109de1d5b19" -->
## Frequency Adjustments
- Increase/decrease frequency for selected phonemes
- Available to admins only

<!-- section_id: "c6529d35-b207-447b-bf6c-d7499769de85" -->
## Reset Database (Safety)
- Dramatic warning + two-step confirmation
- Displays current counts of phonemes and words before final confirmation
- Must type exactly: `DELETE EVERYTHING`
- Recreates an empty database on success

For full rationale and UI examples:
- See `ENHANCED_RESET_SUMMARY.md`
- See `ADMIN_IMPLEMENTATION.md`
- See `MENU_RESTRUCTURE_FINAL.md`