---
resource_id: "7ab3e2df-2c42-4bd0-a5d2-ef7f3cb25025"
resource_type: "document"
resource_name: "PHONEME_TEMPLATES_FEATURE"
---
# Phoneme Templates Feature

<!-- section_id: "51fb7535-1154-434a-af3e-49b0648967a8" -->
## Overview

The Phoneme Templates feature allows you to export your current phoneme collection as a reusable template and import templates later. This is useful for:

- Creating backup copies of your phoneme sets
- Sharing phoneme configurations between different databases
- Starting new projects with a predefined set of phonemes
- Creating standardized phoneme sets for specific languages or purposes

<!-- section_id: "97c5d547-6df6-4258-a0c3-5fdcde9937c7" -->
## Key Features

- **Export Templates**: Export all current phonemes with frequencies reset to 0
- **Import Templates**: Load phonemes from template files into your database
- **List Templates**: View all available template files
- **Automatic Frequency Reset**: All template phonemes have frequency set to 0
- **Duplicate Protection**: Import skips phonemes that already exist in the database

<!-- section_id: "8b60c807-4d4c-462a-a290-561e9fa92cda" -->
## How to Use

<!-- section_id: "82d9c2e8-26a4-45b8-9544-673ed1fdc9f4" -->
### Accessing Template Features

1. Run the main application: `python3 main.py`
2. Select "1. Admin Commands"
3. Enter admin password
4. Choose from template options:
   - **Option 6**: Export phonemes as template
   - **Option 7**: Import phonemes from template
   - **Option 8**: List available templates

<!-- section_id: "71119df5-0bc2-4574-8ca6-089a44425da3" -->
### Export Phonemes as Template

1. Select option 6 in the admin menu
2. Enter a template name (e.g., 'english_phonemes', 'my_language_set')
3. The system will:
   - Create a `phoneme_templates/` directory if it doesn't exist
   - Export all current phonemes with frequency set to 0
   - Save the template as a Python file

<!-- section_id: "d715d4e0-0e2b-4ede-9dad-5cc4466344a5" -->
### Import Phonemes from Template

1. Select option 7 in the admin menu
2. Choose from the list of available templates
3. Confirm the import
4. The system will:
   - Add all template phonemes to your database
   - Skip duplicates (phonemes that already exist)
   - Report import statistics

<!-- section_id: "479f4ba2-485d-48c7-8d33-7370e46cbc45" -->
### List Available Templates

1. Select option 8 in the admin menu
2. View all template files with phoneme counts

<!-- section_id: "502d78c3-c33d-4f8e-87cb-07e7d2f905f0" -->
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

<!-- section_id: "d59f06b2-f5c8-4eaa-a463-4fa2b6978396" -->
## Use Cases

1. **Language Learning Apps**: Create templates for specific languages
2. **Research Projects**: Share standardized phoneme sets
3. **Backup & Restore**: Create backups before making major changes
4. **Multi-Environment Setup**: Use the same phoneme set across different installations

<!-- section_id: "47c7ce04-edeb-4c6b-9fbd-f6c0da1d05a2" -->
## Notes

- Template files are human-readable Python files
- All frequencies in templates are set to 0
- Existing phonemes in the database are not overwritten during import
- Template names should be descriptive and follow Python variable naming conventions