---
resource_id: "7d9684ed-8d55-4aa8-ba05-7f905b4150a4"
resource_type: "document"
resource_name: "database_administration"
---
# Database Administration Tools

- **Source Prompt**: Existing implementation analysis (2025-10-15)
- **Related Implementation**: `app.py` routes 1768-2489, `templates/admin_phonemes.html`, `templates/admin_storage.html`

<!-- section_id: "b6d73dde-0eaa-4413-8f56-61926459189c" -->
## Goal
Provide administrative tools for maintaining database health, cleaning up orphaned data, managing phonemes, and recovering from data inconsistencies without requiring direct database access.

<!-- section_id: "8c1747e1-74af-4963-9dfd-d23061553c38" -->
## Functional Requirements
- Allow admins to add, update, and delete phonemes with validation of IPA symbols and categories.
- Display phoneme usage statistics showing which words use each phoneme.
- Provide bulk deletion of words matching specific criteria (e.g., language, date range).
- Enable deletion of unused phonemes (zero frequency) to keep the phoneme set lean.
- Offer full database reset functionality that clears all user data and restores default schema.
- Include utility to fix broken video paths resulting from file system changes or migrations.
- Show phoneme management interface with frequency tracking and usage details.
- Protect destructive operations with confirmation prompts and require admin authentication.

<!-- section_id: "299ddd82-44ce-41b0-959c-a7413bae5ef4" -->
## Acceptance Criteria
- Adding a phoneme via `/api/admin/add-phoneme` validates IPA symbol uniqueness and inserts into current project.
- Updating phoneme frequency via `/api/admin/update-phoneme-frequency` recalculates based on actual word usage.
- Phoneme usage endpoint (`/api/admin/phoneme-usage/<id>`) returns list of words using that phoneme.
- Deleting a phoneme via `/api/admin/delete-phoneme/<id>` succeeds only if frequency is zero; otherwise returns error.
- Bulk word deletion (`/api/admin/bulk-delete-words`) removes matching words and updates phoneme frequencies.
- Unused phoneme deletion (`/api/admin/delete-unused-phonemes`) clears all phonemes with frequency=0.
- Database reset (`/api/admin/reset-database`) drops and recreates all tables, preserving schema.
- Video path fixer (`/api/admin/fix-video-paths`) scans words and corrects file references to match actual storage.

<!-- section_id: "cd5f8c2b-32be-4637-9a12-fa71a88f2147" -->
## Notes
- Admin operations should be logged for audit trails and debugging.
- Database reset is irreversible; consider backup prompts or export-before-reset workflows.
- Phoneme deletion should cascade properly to avoid orphaned references in word phoneme mappings.
- Future work may include scheduled cleanup jobs, automated backups, and data export/import tools.
- Consider role-based access control to restrict admin endpoints to designated users only.
