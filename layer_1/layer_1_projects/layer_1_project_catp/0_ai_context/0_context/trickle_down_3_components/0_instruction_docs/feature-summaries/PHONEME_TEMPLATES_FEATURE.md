---
resource_id: "e87f5512-1004-40e6-a693-92970f9e9b13"
resource_type: "document"
resource_name: "PHONEME_TEMPLATES_FEATURE"
---
# Phoneme Templates Feature

<!-- section_id: "fd42ad79-13a2-41a5-aea4-32db3bb1e42c" -->
## Overview

The Phoneme Templates feature allows you to export your current phoneme collection as a reusable template and import templates later. This is useful for:

- Creating backup copies of your phoneme sets
- Sharing phoneme configurations between different databases
- Starting new projects with a predefined set of phonemes
- Creating standardized phoneme sets for specific languages or purposes

<!-- section_id: "2542b2de-35e8-4c10-baf6-9e0f94cf0506" -->
## Key Features

- **Export Templates**: Export all current phonemes with frequencies reset to 0
- **Import Templates**: Load phonemes from template files into your database
- **List Templates**: View all available template files
- **Automatic Frequency Reset**: All template phonemes have frequency set to 0
- **Duplicate Protection**: Import skips phonemes that already exist in the database

<!-- section_id: "eef4d5bf-6741-4c18-a5ed-51cf9cd637f0" -->
## How to Use

<!-- section_id: "66afb22d-5e92-4f5a-83ad-a9e4cedde405" -->
### Accessing Template Features

1. Run the main application: `python3 main.py`
2. Select "1. Admin Commands"
3. Enter admin password
4. Choose from template options:
   - **Option 6**: Export phonemes as template
   - **Option 7**: Import phonemes from template
   - **Option 8**: List available templates

<!-- section_id: "d356c2c8-fdf9-4d64-9f3e-86c70b38ede8" -->
### Export Phonemes as Template

1. Select option 6 in the admin menu
2. Enter a template name (e.g., 'english_phonemes', 'my_language_set')
3. The system will:
   - Create a `phoneme_templates/` directory if it doesn't exist
   - Export all current phonemes with frequency set to 0
   - Save the template as a Python file

<!-- section_id: "d7acee32-c4f6-4d15-a2e1-4e6788ce4ef1" -->
### Import Phonemes from Template

1. Select option 7 in the admin menu
2. Choose from the list of available templates
3. Confirm the import
4. The system will:
   - Add all template phonemes to your database
   - Skip duplicates (phonemes that already exist)
   - Report import statistics

<!-- section_id: "126d98b1-ee92-4cae-941f-41c513450933" -->
### List Available Templates

1. Select option 8 in the admin menu
2. View all template files with phoneme counts

<!-- section_id: "e29b7d8b-a790-41e5-8e99-fdba7c52b1c0" -->
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

<!-- section_id: "974cf15f-8376-42b1-b0e4-a41b402b62d1" -->
## Use Cases

1. **Language Learning Apps**: Create templates for specific languages
2. **Research Projects**: Share standardized phoneme sets
3. **Backup & Restore**: Create backups before making major changes
4. **Multi-Environment Setup**: Use the same phoneme set across different installations

<!-- section_id: "883f4e46-f5b6-48c9-bcf3-cd58e9e16dce" -->
## Notes

- Template files are human-readable Python files
- All frequencies in templates are set to 0
- Existing phonemes in the database are not overwritten during import
- Template names should be descriptive and follow Python variable naming conventions