---
resource_id: "ea244a84-a662-4dfa-bc59-c13220c7a30a"
resource_type: "document"
resource_name: "PHONEME_TEMPLATES_FEATURE"
---
# Phoneme Templates Feature

<!-- section_id: "dfebb411-285e-402e-a803-79a638749d43" -->
## Overview

The Phoneme Templates feature allows you to export your current phoneme collection as a reusable template and import templates later. This is useful for:

- Creating backup copies of your phoneme sets
- Sharing phoneme configurations between different databases
- Starting new projects with a predefined set of phonemes
- Creating standardized phoneme sets for specific languages or purposes

<!-- section_id: "d538e779-8a13-45c8-af0f-5848cf448383" -->
## Key Features

- **Export Templates**: Export all current phonemes with frequencies reset to 0
- **Import Templates**: Load phonemes from template files into your database
- **List Templates**: View all available template files
- **Automatic Frequency Reset**: All template phonemes have frequency set to 0
- **Duplicate Protection**: Import skips phonemes that already exist in the database

<!-- section_id: "c6f8f19a-5e0c-4533-8467-7063049c8b2d" -->
## How to Use

<!-- section_id: "552c4112-11dc-4247-9b4a-f0f1ea297dce" -->
### Accessing Template Features

1. Run the main application: `python3 main.py`
2. Select "1. Admin Commands"
3. Enter admin password
4. Choose from template options:
   - **Option 6**: Export phonemes as template
   - **Option 7**: Import phonemes from template
   - **Option 8**: List available templates

<!-- section_id: "434a074c-c05f-4c7a-9554-d9c462d2cb63" -->
### Export Phonemes as Template

1. Select option 6 in the admin menu
2. Enter a template name (e.g., 'english_phonemes', 'my_language_set')
3. The system will:
   - Create a `phoneme_templates/` directory if it doesn't exist
   - Export all current phonemes with frequency set to 0
   - Save the template as a Python file

<!-- section_id: "ae565913-dcba-438e-89a2-32bf41225fd3" -->
### Import Phonemes from Template

1. Select option 7 in the admin menu
2. Choose from the list of available templates
3. Confirm the import
4. The system will:
   - Add all template phonemes to your database
   - Skip duplicates (phonemes that already exist)
   - Report import statistics

<!-- section_id: "f8b08f17-5d00-4a6e-ac73-2ac2de4c73ae" -->
### List Available Templates

1. Select option 8 in the admin menu
2. View all template files with phoneme counts

<!-- section_id: "41e543fe-a453-4256-a1a1-b782b6a76bf2" -->
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

<!-- section_id: "d8a504d6-9ae5-4bb0-b571-816a116347d4" -->
## Use Cases

1. **Language Learning Apps**: Create templates for specific languages
2. **Research Projects**: Share standardized phoneme sets
3. **Backup & Restore**: Create backups before making major changes
4. **Multi-Environment Setup**: Use the same phoneme set across different installations

<!-- section_id: "af69969c-2a9f-4c73-8f34-f6b142a7d772" -->
## Notes

- Template files are human-readable Python files
- All frequencies in templates are set to 0
- Existing phonemes in the database are not overwritten during import
- Template names should be descriptive and follow Python variable naming conventions