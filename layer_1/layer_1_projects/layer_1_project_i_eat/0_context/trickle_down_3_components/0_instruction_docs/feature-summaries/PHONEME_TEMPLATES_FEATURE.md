---
resource_id: "411bba31-8a58-4c65-a892-ca31cf0c2339"
resource_type: "document"
resource_name: "PHONEME_TEMPLATES_FEATURE"
---
# Phoneme Templates Feature

<!-- section_id: "708c5d25-c26b-4579-ad2f-15b8d1d83276" -->
## Overview

The Phoneme Templates feature allows you to export your current phoneme collection as a reusable template and import templates later. This is useful for:

- Creating backup copies of your phoneme sets
- Sharing phoneme configurations between different databases
- Starting new projects with a predefined set of phonemes
- Creating standardized phoneme sets for specific languages or purposes

<!-- section_id: "11b97e2b-ef26-4fc6-a576-79f2f1bf2a7c" -->
## Key Features

- **Export Templates**: Export all current phonemes with frequencies reset to 0
- **Import Templates**: Load phonemes from template files into your database
- **List Templates**: View all available template files
- **Automatic Frequency Reset**: All template phonemes have frequency set to 0
- **Duplicate Protection**: Import skips phonemes that already exist in the database

<!-- section_id: "a1e8495b-6369-4367-8d18-d81a47c9b46f" -->
## How to Use

<!-- section_id: "51ba62a2-a3d3-4e86-9ef9-606712dd8dc6" -->
### Accessing Template Features

1. Run the main application: `python3 main.py`
2. Select "1. Admin Commands"
3. Enter admin password
4. Choose from template options:
   - **Option 6**: Export phonemes as template
   - **Option 7**: Import phonemes from template
   - **Option 8**: List available templates

<!-- section_id: "c3473db6-43f4-462b-906a-35fc57790dc9" -->
### Export Phonemes as Template

1. Select option 6 in the admin menu
2. Enter a template name (e.g., 'english_phonemes', 'my_language_set')
3. The system will:
   - Create a `phoneme_templates/` directory if it doesn't exist
   - Export all current phonemes with frequency set to 0
   - Save the template as a Python file

<!-- section_id: "961893f0-49ba-4925-90ba-db5088bef4ab" -->
### Import Phonemes from Template

1. Select option 7 in the admin menu
2. Choose from the list of available templates
3. Confirm the import
4. The system will:
   - Add all template phonemes to your database
   - Skip duplicates (phonemes that already exist)
   - Report import statistics

<!-- section_id: "99c8ca3a-c12d-4e46-867d-bcba7f4221cb" -->
### List Available Templates

1. Select option 8 in the admin menu
2. View all template files with phoneme counts

<!-- section_id: "5b35beda-99f3-4550-8eaf-ddc8964d6f8e" -->
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

<!-- section_id: "fe5d7be3-ceed-43c8-8b20-b540e9676e72" -->
## Use Cases

1. **Language Learning Apps**: Create templates for specific languages
2. **Research Projects**: Share standardized phoneme sets
3. **Backup & Restore**: Create backups before making major changes
4. **Multi-Environment Setup**: Use the same phoneme set across different installations

<!-- section_id: "52b48c39-53a0-4b8c-847f-0dae679ee177" -->
## Notes

- Template files are human-readable Python files
- All frequencies in templates are set to 0
- Existing phonemes in the database are not overwritten during import
- Template names should be descriptive and follow Python variable naming conventions