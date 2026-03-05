---
resource_id: "89984062-be54-4b95-9dad-1416b943ec27"
resource_type: "document"
resource_name: "admin"
---
# Admin Guide

<!-- section_id: "8267e699-365c-4493-a597-70c1694d6309" -->
## Access
- Select "Admin Commands" from the main menu
- Enter password: `20251010`

<!-- section_id: "64b0dd53-51f4-4784-8547-109ae2063296" -->
## Admin Features
1. Add new phoneme
2. Delete phoneme
3. Increase frequency
4. Decrease frequency
5. Reset database
6. Back to main menu

<!-- section_id: "a3732ea6-3949-47f1-bbe3-7880459f0295" -->
## Add/Delete Phonemes
- Add flow shows existing group/subgroup types with numeric selection
- Delete flow lists phonemes hierarchically with numeric selection
- Both use the app's fixed ordering and enforce database constraints

<!-- section_id: "594cf562-6e11-43a0-b6e5-d7059045aac3" -->
## Frequency Adjustments
- Increase/decrease frequency for selected phonemes
- Available to admins only

<!-- section_id: "082b81e7-b58d-4092-9c30-844400c78b9e" -->
## Reset Database (Safety)
- Dramatic warning + two-step confirmation
- Displays current counts of phonemes and words before final confirmation
- Must type exactly: `DELETE EVERYTHING`
- Recreates an empty database on success

For full rationale and UI examples:
- See `ENHANCED_RESET_SUMMARY.md`
- See `ADMIN_IMPLEMENTATION.md`
- See `MENU_RESTRUCTURE_FINAL.md`