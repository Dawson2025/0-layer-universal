---
resource_id: "e51bed35-6571-402d-94b7-8bcf8791f114"
resource_type: "document"
resource_name: "admin"
---
# Admin Guide

<!-- section_id: "dd4be56a-cf52-4940-89bb-b0d02e498169" -->
## Access
- Select "Admin Commands" from the main menu
- Enter password: `20251010`

<!-- section_id: "c3bd5ebd-7057-4acd-958a-51a63b82c4cf" -->
## Admin Features
1. Add new phoneme
2. Delete phoneme
3. Increase frequency
4. Decrease frequency
5. Reset database
6. Back to main menu

<!-- section_id: "69bbba21-1abe-4577-a34d-ba4c6b48e63d" -->
## Add/Delete Phonemes
- Add flow shows existing group/subgroup types with numeric selection
- Delete flow lists phonemes hierarchically with numeric selection
- Both use the app's fixed ordering and enforce database constraints

<!-- section_id: "1114a59e-6556-44b4-8c4e-1b315e6ec90a" -->
## Frequency Adjustments
- Increase/decrease frequency for selected phonemes
- Available to admins only

<!-- section_id: "e03bbdb4-8cd8-422f-8dfa-436210c08a4f" -->
## Reset Database (Safety)
- Dramatic warning + two-step confirmation
- Displays current counts of phonemes and words before final confirmation
- Must type exactly: `DELETE EVERYTHING`
- Recreates an empty database on success

For full rationale and UI examples:
- See `ENHANCED_RESET_SUMMARY.md`
- See `ADMIN_IMPLEMENTATION.md`
- See `MENU_RESTRUCTURE_FINAL.md`