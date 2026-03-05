---
resource_id: "e05b43b6-bbf9-41bb-8440-ef9f232668fc"
resource_type: "document"
resource_name: "admin"
---
# Admin Guide

<!-- section_id: "4a9c2217-3264-4ead-9067-15e38978350a" -->
## Access
- Select "Admin Commands" from the main menu
- Enter password: `20251010`

<!-- section_id: "1950a0b0-7c10-481c-a678-feaa79ee9fbb" -->
## Admin Features
1. Add new phoneme
2. Delete phoneme
3. Increase frequency
4. Decrease frequency
5. Reset database
6. Back to main menu

<!-- section_id: "357621a8-4a8d-4f06-9c51-be591ec9006b" -->
## Add/Delete Phonemes
- Add flow shows existing group/subgroup types with numeric selection
- Delete flow lists phonemes hierarchically with numeric selection
- Both use the app's fixed ordering and enforce database constraints

<!-- section_id: "02eb8885-fd09-46d0-9618-2656a9e73ba2" -->
## Frequency Adjustments
- Increase/decrease frequency for selected phonemes
- Available to admins only

<!-- section_id: "8f513854-f10b-403b-8c96-c5fe7bfce1f0" -->
## Reset Database (Safety)
- Dramatic warning + two-step confirmation
- Displays current counts of phonemes and words before final confirmation
- Must type exactly: `DELETE EVERYTHING`
- Recreates an empty database on success

For full rationale and UI examples:
- See `ENHANCED_RESET_SUMMARY.md`
- See `ADMIN_IMPLEMENTATION.md`
- See `MENU_RESTRUCTURE_FINAL.md`