---
resource_id: "67419147-9426-4332-b0af-a8384431e27d"
resource_type: "document"
resource_name: "admin"
---
# Admin Guide

<!-- section_id: "7625a37f-a20a-426e-8a31-060249f1d5cc" -->
## Access
- Select "Admin Commands" from the main menu
- Enter password: `20251010`

<!-- section_id: "4075986e-ad7b-43fc-8aa2-190d246ac3ad" -->
## Admin Features
1. Add new phoneme
2. Delete phoneme
3. Increase frequency
4. Decrease frequency
5. Reset database
6. Back to main menu

<!-- section_id: "6ecb1a6a-3434-41d3-8eb3-a46fa74709a3" -->
## Add/Delete Phonemes
- Add flow shows existing group/subgroup types with numeric selection
- Delete flow lists phonemes hierarchically with numeric selection
- Both use the app's fixed ordering and enforce database constraints

<!-- section_id: "99789596-60cb-4a41-b700-f3d42435d8cb" -->
## Frequency Adjustments
- Increase/decrease frequency for selected phonemes
- Available to admins only

<!-- section_id: "03e3db2d-9519-4b28-8cf4-9d0c537b6024" -->
## Reset Database (Safety)
- Dramatic warning + two-step confirmation
- Displays current counts of phonemes and words before final confirmation
- Must type exactly: `DELETE EVERYTHING`
- Recreates an empty database on success

For full rationale and UI examples:
- See `ENHANCED_RESET_SUMMARY.md`
- See `ADMIN_IMPLEMENTATION.md`
- See `MENU_RESTRUCTURE_FINAL.md`