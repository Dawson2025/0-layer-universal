---
resource_id: "8e5afdcf-8c8f-44ba-924f-509cfa482ca9"
resource_type: "document"
resource_name: "admin"
---
# Admin Guide

<!-- section_id: "658cfef0-cd4e-4558-be7d-0567d909b16a" -->
## Access
- Select "Admin Commands" from the main menu
- Enter password: `20251010`

<!-- section_id: "c339a3b9-b352-4e5c-9e21-2847efad0616" -->
## Admin Features
1. Add new phoneme
2. Delete phoneme
3. Increase frequency
4. Decrease frequency
5. Reset database
6. Back to main menu

<!-- section_id: "757555bf-fbf8-41b7-aa51-ff716a3d3ee5" -->
## Add/Delete Phonemes
- Add flow shows existing group/subgroup types with numeric selection
- Delete flow lists phonemes hierarchically with numeric selection
- Both use the app's fixed ordering and enforce database constraints

<!-- section_id: "3a8223cf-27f8-4e87-8b08-a8fcf0dfd828" -->
## Frequency Adjustments
- Increase/decrease frequency for selected phonemes
- Available to admins only

<!-- section_id: "cfce976f-8dfb-4061-9781-77ce01f32388" -->
## Reset Database (Safety)
- Dramatic warning + two-step confirmation
- Displays current counts of phonemes and words before final confirmation
- Must type exactly: `DELETE EVERYTHING`
- Recreates an empty database on success

For full rationale and UI examples:
- See `ENHANCED_RESET_SUMMARY.md`
- See `ADMIN_IMPLEMENTATION.md`
- See `MENU_RESTRUCTURE_FINAL.md`