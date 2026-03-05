---
resource_id: "55a4b4ca-2d22-4bff-b3c0-eacbee272477"
resource_type: "document"
resource_name: "PHONEME_TEMPLATES_FEATURE"
---
# Phoneme Templates Feature

<!-- section_id: "b4ae59ab-9990-43bf-9a18-976db1194654" -->
## Overview

The Phoneme Templates feature allows you to export your current phoneme collection as a reusable template and import templates later. This is useful for:

- Creating backup copies of your phoneme sets
- Sharing phoneme configurations between different databases
- Starting new projects with a predefined set of phonemes
- Creating standardized phoneme sets for specific languages or purposes

<!-- section_id: "93d06c2f-e021-4114-9b22-4cb36f0694f3" -->
## Key Features

- **Export Templates**: Export all current phonemes with frequencies reset to 0
- **Import Templates**: Load phonemes from template files into your database
- **List Templates**: View all available template files
- **Automatic Frequency Reset**: All template phonemes have frequency set to 0
- **Duplicate Protection**: Import skips phonemes that already exist in the database

<!-- section_id: "5762e0d0-b1d2-4816-9eaa-d6f5038ce87d" -->
## How to Use

<!-- section_id: "4b76957a-051a-4d62-8f90-5c776b7e7735" -->
### Accessing Template Features

1. Run the main application: `python3 main.py`
2. Select "1. Admin Commands"
3. Enter admin password
4. Choose from template options:
   - **Option 6**: Export phonemes as template
   - **Option 7**: Import phonemes from template
   - **Option 8**: List available templates

<!-- section_id: "dc0ba6ff-74dc-4808-9e00-1775287f79c1" -->
### Export Phonemes as Template

1. Select option 6 in the admin menu
2. Enter a template name (e.g., 'english_phonemes', 'my_language_set')
3. The system will:
   - Create a `phoneme_templates/` directory if it doesn't exist
   - Export all current phonemes with frequency set to 0
   - Save the template as a Python file

<!-- section_id: "733189f9-7185-46c9-a12c-8ab4640b6797" -->
### Import Phonemes from Template

1. Select option 7 in the admin menu
2. Choose from the list of available templates
3. Confirm the import
4. The system will:
   - Add all template phonemes to your database
   - Skip duplicates (phonemes that already exist)
   - Report import statistics

<!-- section_id: "d9e1bdf6-b2cb-4a9c-83cf-96cdd5346cba" -->
### List Available Templates

1. Select option 8 in the admin menu
2. View all template files with phoneme counts

<!-- section_id: "2e56cdd1-2878-41ac-8a68-562d9eadbf96" -->
## Template File Structure

Templates are stored in the `phoneme_templates/` directory as Python files. Each template contains:

```python
# Phoneme template: template_name
# Generated from existing phonemes with frequency set to 0
# Total phonemes: X

template_name_template = [
    {'syllable_type': 'CVC', 'position': 'onset', 'length_type': 'single_consonants', 'group_type': 'Stops', 'subgroup_type': 'none', 'phoneme': 'p', 'frequency': 0},
    # ... more phonemes
]
```

<!-- section_id: "0c31eb94-2072-4882-b8e7-55afa50687fa" -->
## Use Cases

1. **Language Learning Apps**: Create templates for specific languages
2. **Research Projects**: Share standardized phoneme sets
3. **Backup & Restore**: Create backups before making major changes
4. **Multi-Environment Setup**: Use the same phoneme set across different installations

<!-- section_id: "c41ca52f-dfc0-4e45-883f-89c6752dd3a7" -->
## Notes

- Template files are human-readable Python files
- All frequencies in templates are set to 0
- Existing phonemes in the database are not overwritten during import
- Template names should be descriptive and follow Python variable naming conventions