---
resource_id: "dccac442-41fd-4331-b761-c8ff75b5887e"
resource_type: "document"
resource_name: "cloud_variant_actions"
---
# Cloud Variant Controls Parity

- **Source Prompt**: `docs/for_ai/prompts.txt/cloud/cloud_variant_actions.md`

<!-- section_id: "e4a4f6e1-59de-4b19-9e16-04e285b94e3f" -->
## Goal
Ensure cloud-based project variants expose the same management actions as local variants in the Projects interface so owners can administer cloud-only workflows without switching to a local copy.

<!-- section_id: "b2f94727-3bf7-4e35-8cb1-e52eea29b1e2" -->
## Functional Requirements
- Display `Edit`, `Delete`, and `Share` actions for cloud variants when the viewing user owns the cloud project.
- Keep the existing `Fork to Local` option available for cloud variants and retain the current controls for local variants.
- Enable the `Share` flow to work with cloud project identifiers using the same modal and API endpoints as local projects.
- Encode project identifiers in modal operations so both numeric (local) and string (cloud) IDs are handled safely in browser interactions.

<!-- section_id: "b274f28e-c0a2-4692-93ad-6e92d1dbe13c" -->
## Acceptance Criteria
- Owners see `Edit`, `Delete`, `Share`, and `Fork to Local` buttons when a project’s active variant is in the cloud; non-owners only see the actions they have permission to use.
- Editing a cloud project name persists the change in Firestore and updates the language attribute for its words.
- Deleting a cloud project removes the Firestore document, associated words/phonemes, and clears any `project_shares` entries referencing it.
- Sharing or unsharing a cloud project via the modal succeeds without client-side or server-side identifier errors, and the dashboard’s shared-projects list includes cloud projects with accurate metadata.

<!-- section_id: "1dc9b0f3-62f5-4ab6-a59d-c68fb5da3491" -->
## Notes
- Consolidate identifier handling in the API layer so future project routes work transparently with both local and cloud IDs.
- Keep share listings and group detail pages aware of cloud projects to avoid dropping entries that lack a local SQLite counterpart.
