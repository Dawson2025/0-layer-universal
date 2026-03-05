---
resource_id: "119e7ec2-4cec-4aac-8374-c7d481bc75e3"
resource_type: "document"
resource_name: "phoneme_template_system"
---
# Phoneme Template System

- **Source Prompt**: Existing implementation analysis (2025-10-15)
- **Related Implementation**: `app.py` routes 1910-2526, `templates/admin_templates.html`

<!-- section_id: "8391d189-2bdc-4413-9d1b-59755cafcfb5" -->
## Goal
Streamline project setup and enable sharing of phoneme configurations by providing a template system that captures, exports, imports, and applies phoneme sets across projects.

<!-- section_id: "b11d8b30-c7f2-447f-b328-47eff2b9348d" -->
## Functional Requirements
- Allow admins to export the current project's phoneme set as a reusable template with a descriptive name.
- Store templates with metadata including creation timestamp, phoneme count, and associated user/project.
- Provide a templates management page (`/admin/templates`) listing all available templates.
- Enable importing templates from JSON files uploaded by users.
- Support applying templates to the current project, replacing existing phonemes with template contents.
- Offer template download functionality to share phoneme configurations across installations.
- Include a "reset to default" option that restores a predefined set of phonemes.
- Allow deletion of custom templates while preserving the default template.

<!-- section_id: "d8b5ba82-965d-409a-9cd1-25919948f3d3" -->
## Acceptance Criteria
- Exporting a template via `/api/admin/export-template` creates a JSON file containing all phonemes with their IPA symbols, categories, frequencies, and example words.
- Templates are stored in the `phoneme_templates` table with unique IDs and descriptive names.
- The templates page displays template name, phoneme count, creation date, and action buttons (Apply, Download, Delete).
- Applying a template via `/api/templates/<id>/apply` clears current phonemes and populates the project with template phonemes.
- Importing a template from JSON validates structure and creates new template entry.
- Downloading a template via `/api/admin/download-template/<id>` returns a properly-formatted JSON file.
- Reset to default loads a built-in starter template with common IPA phonemes.
- Template operations update the current project's phoneme data and refresh frequency statistics.

<!-- section_id: "24e4e988-5a9f-4c42-93ca-5c8ddb417847" -->
## Notes
- Templates include phoneme categories (vowel, consonant, etc.) to maintain organization across projects.
- Export format should be version-tagged to support future schema migrations.
- Consider adding template preview functionality before applying to prevent accidental data loss.
- Future enhancements may include template sharing marketplace or community-contributed phoneme sets.
