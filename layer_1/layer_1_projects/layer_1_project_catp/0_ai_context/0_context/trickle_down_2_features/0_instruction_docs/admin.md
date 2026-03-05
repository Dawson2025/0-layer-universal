---
resource_id: "2a7cbc60-f7c1-41a0-84be-8b59ff79a75a"
resource_type: "document"
resource_name: "admin"
---
# Admin Guide

<!-- section_id: "db7e729a-1e7b-4f3e-bc40-eff03a1ec7b4" -->
## Access
- Select "Admin Commands" from the main menu
- Enter password: `20251010`

<!-- section_id: "ad6dde70-d6b2-4544-9e27-e13c397ba7c7" -->
## Admin Features
1. Add new phoneme
2. Delete phoneme
3. Increase frequency
4. Decrease frequency
5. Reset database
6. Back to main menu

<!-- section_id: "c461f76c-0e70-40b5-aa42-d953f9920005" -->
## Add/Delete Phonemes
- Add flow shows existing group/subgroup types with numeric selection
- Delete flow lists phonemes hierarchically with numeric selection
- Both use the app's fixed ordering and enforce database constraints

<!-- section_id: "1270cf3e-0b68-4d62-92c1-af44a0d3c07d" -->
## Frequency Adjustments
- Increase/decrease frequency for selected phonemes
- Available to admins only

<!-- section_id: "3550893c-c050-4e46-8fbd-b092d3dd8e32" -->
## Reset Database (Safety)
- Dramatic warning + two-step confirmation
- Displays current counts of phonemes and words before final confirmation
- Must type exactly: `DELETE EVERYTHING`
- Recreates an empty database on success

For full rationale and UI examples:
- See `ENHANCED_RESET_SUMMARY.md`
- See `ADMIN_IMPLEMENTATION.md`
- See `MENU_RESTRUCTURE_FINAL.md`