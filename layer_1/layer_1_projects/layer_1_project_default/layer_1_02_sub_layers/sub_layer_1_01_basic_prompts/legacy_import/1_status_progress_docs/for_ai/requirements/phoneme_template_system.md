---
resource_id: "fcbb748d-9845-4391-81ca-c568e9d55612"
resource_type: "document"
resource_name: "phoneme_template_system"
---
# Phoneme Template System

- **Source Prompt**: Existing implementation analysis (2025-10-15)
- **Related Implementation**: `app.py` routes 1910-2526, `templates/admin_templates.html`

<!-- section_id: "d7cdf98b-5d0b-4215-9f6b-d075a83045e5" -->
## Goal
Streamline project setup and enable sharing of phoneme configurations by providing a template system that captures, exports, imports, and applies phoneme sets across projects.

<!-- section_id: "dc02eb86-4039-4462-97e0-3ecd51a885dc" -->
## Functional Requirements
- Allow admins to export the current project's phoneme set as a reusable template with a descriptive name.
- Store templates with metadata including creation timestamp, phoneme count, and associated user/project.
- Provide a templates management page (`/admin/templates`) listing all available templates.
- Enable importing templates from JSON files uploaded by users.
- Support applying templates to the current project, replacing existing phonemes with template contents.
- Offer template download functionality to share phoneme configurations across installations.
- Include a "reset to default" option that restores a predefined set of phonemes.
- Allow deletion of custom templates while preserving the default template.

<!-- section_id: "be420402-483a-4ff0-9d5c-04f05c6efd95" -->
## Acceptance Criteria
- Exporting a template via `/api/admin/export-template` creates a JSON file containing all phonemes with their IPA symbols, categories, frequencies, and example words.
- Templates are stored in the `phoneme_templates` table with unique IDs and descriptive names.
- The templates page displays template name, phoneme count, creation date, and action buttons (Apply, Download, Delete).
- Applying a template via `/api/templates/<id>/apply` clears current phonemes and populates the project with template phonemes.
- Importing a template from JSON validates structure and creates new template entry.
- Downloading a template via `/api/admin/download-template/<id>` returns a properly-formatted JSON file.
- Reset to default loads a built-in starter template with common IPA phonemes.
- Template operations update the current project's phoneme data and refresh frequency statistics.

<!-- section_id: "d1bf6839-3a6f-4db9-a467-78583421001d" -->
## Notes
- Templates include phoneme categories (vowel, consonant, etc.) to maintain organization across projects.
- Export format should be version-tagged to support future schema migrations.
- Consider adding template preview functionality before applying to prevent accidental data loss.
- Future enhancements may include template sharing marketplace or community-contributed phoneme sets.
