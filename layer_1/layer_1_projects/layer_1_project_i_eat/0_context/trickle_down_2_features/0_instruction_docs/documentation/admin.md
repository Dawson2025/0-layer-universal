---
resource_id: "2b825563-3f8c-4349-99e3-881a708de6c0"
resource_type: "document"
resource_name: "admin"
---
# Admin Guide

<!-- section_id: "70477f21-433d-402c-8b4b-87c39e123752" -->
## Access
- Select "Admin Commands" from the main menu
- Enter password: `20251010`

<!-- section_id: "0843bd5f-ddd8-4d65-bb0f-3878cbb622cf" -->
## Admin Features
1. Add new phoneme
2. Delete phoneme
3. Increase frequency
4. Decrease frequency
5. Reset database
6. Back to main menu

<!-- section_id: "1ee67f7c-7cb2-4f6c-81c4-123f1df5d0cd" -->
## Add/Delete Phonemes
- Add flow shows existing group/subgroup types with numeric selection
- Delete flow lists phonemes hierarchically with numeric selection
- Both use the app's fixed ordering and enforce database constraints

<!-- section_id: "790b9282-2c2d-485e-808c-40138c497863" -->
## Frequency Adjustments
- Increase/decrease frequency for selected phonemes
- Available to admins only

<!-- section_id: "5be8c615-f472-4d71-a24b-b9cb8a817aaa" -->
## Reset Database (Safety)
- Dramatic warning + two-step confirmation
- Displays current counts of phonemes and words before final confirmation
- Must type exactly: `DELETE EVERYTHING`
- Recreates an empty database on success

For full rationale and UI examples:
- See `ENHANCED_RESET_SUMMARY.md`
- See `ADMIN_IMPLEMENTATION.md`
- See `MENU_RESTRUCTURE_FINAL.md`