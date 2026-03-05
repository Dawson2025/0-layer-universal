---
resource_id: "6f74f45a-51ec-4e2b-899a-3b96a7dae866"
resource_type: "output"
resource_name: "DOCX_SKILL_SETUP_GUIDE"
---
# Anthropic /docx Skill Setup & Usage Guide

**Date**: January 29, 2026
**Status**: Setup in progress
**Purpose**: Enable AI agents to work efficiently with Microsoft Word documents

---

<!-- section_id: "3e43f5f3-9da5-4230-8e7d-3ab6d9116a4b" -->
## Installation

<!-- section_id: "df2fcce9-f5a4-4cb6-9203-759e542ba765" -->
### Step 1: Add the Skill

```bash
claude skill add anthropics/docx
```

This installs Anthropic's officially maintained `/docx` skill into your Claude Code environment.

<!-- section_id: "355d101d-78b8-4664-800f-552f6d13827c" -->
### Step 2: Verify Installation

```bash
claude skill list | grep docx
```

You should see `/docx` in the available skills list.

---

<!-- section_id: "700683fc-0849-4379-9efb-281b06d33cec" -->
## Why Use /docx Skill?

<!-- section_id: "c1b7c2a9-818c-4455-9099-ddddce442633" -->
### Advantages Over Direct python-docx

| Aspect | /docx Skill | Direct python-docx |
|--------|------------|-------------------|
| **Design** | Built by Anthropic for Claude | General-purpose Python library |
| **Interface** | High-level abstractions | Low-level XML manipulation |
| **Context Awareness** | Understands document state | No state awareness |
| **Error Handling** | Optimized for AI use | Generic exception handling |
| **Efficiency** | Natural language commands | Manual code writing |
| **Maintenance** | Officially supported | Community library |

<!-- section_id: "f7f5444a-942e-4914-9aa1-b37607abc7fb" -->
### Use Cases

**Perfect for**:
- Creating professional documents programmatically
- Embedding text, tables, and images
- Formatting and styling with presets
- Working with document structure (sections, paragraphs)
- Converting to PDF
- Batch document operations

**Not ideal for**:
- Low-level format control
- Complex XML manipulation
- Proprietary .docx extensions

---

<!-- section_id: "84461af7-694a-46ad-b640-70b72823ca98" -->
## Basic Skill Usage

<!-- section_id: "81ede309-e46e-432a-b6b3-447a5f553e98" -->
### Creating a Document

The `/docx` skill provides high-level commands:

```
/docx create
  --title "Executive Summary - Module 02"
  --author "Your Team"
  --output "/home/dawson/Downloads/Executive_Summary.docx"
```

<!-- section_id: "d4ba42b5-5544-4586-aaf8-947f3ce74616" -->
### Adding Content

```
/docx add-heading "Section Title" --level 1
/docx add-paragraph "Your paragraph text here."
/docx add-table --rows 3 --cols 4
/docx add-image "/path/to/image.png"
/docx format-text bold italic underline
```

<!-- section_id: "f8341612-57e1-4b8b-8e0b-8e434194f3b2" -->
### Styling

```
/docx set-style "Heading 1"
/docx set-font-size 12
/docx set-color blue
```

<!-- section_id: "c5624821-6310-4ad0-9ac7-590a7d895e02" -->
### Saving & Converting

```
/docx save
/docx convert-to-pdf
```

---

<!-- section_id: "193bd1d5-1132-4760-b511-f4e5ca533c80" -->
## Implementation for Executive Summary

<!-- section_id: "6b48adf9-2c05-4000-b239-3a6ecb1b1f5b" -->
### Document Structure to Create

```
Executive Summary - Module 02 Case Study

1. Introduction/Overview
   - Context for the project
   - Problem being solved

2. Methodology & Implementation
   - Data preprocessing details
   - Models tested and why
   - Hyperparameter tuning approach
   - Evaluation methodology

3. Results & Findings
   - Key metrics table
   - Feature importance
   - Model comparison

4. Insights & Analysis
   - What the analysis revealed
   - Patterns discovered
   - Limitations and caveats

5. Evaluation & Reflection
   - Metrics discussion
   - Model strengths/weaknesses
   - What would you do differently

6. Conclusion & Recommendations
   - Key takeaways
   - Next steps

7. Discussion Questions
   - Response to Q1
   - Response to Q2
```

<!-- section_id: "0fd78eb2-9429-4bd0-b32f-2f2f0af916c9" -->
### Implementation Strategy

1. **Create base document** with title, author metadata
2. **Add each section** as heading + paragraphs
3. **Insert data tables** for metrics and results
4. **Embed visualizations** as high-quality images
5. **Format for professionalism** (consistent fonts, spacing, styles)
6. **Save and convert** to final .docx format

---

<!-- section_id: "f79d4d99-9403-4ff2-b471-73b230724ab6" -->
## Key Commands for This Project

<!-- section_id: "8d7ca9ae-b0e5-4b8e-8b6c-ca2c0b4d199c" -->
### For our Executive Summary, we'll use:

```bash
# Create document
/docx create --title "Executive Summary - Module 02 Deep Dive Case Study"

# Add sections
/docx add-heading "1. Introduction" --level 1
/docx add-paragraph "..."

# Add a table for metrics
/docx add-table \
  --data "Model,Accuracy,Precision,Recall,F1" \
  --data "Random Forest,0.87,0.72,0.65,0.68" \
  --data "Logistic Regression,0.85,0.69,0.61,0.65"

# Add visualization
/docx add-image "./outputs/feature_importance.png"

# Save final document
/docx save --output "/home/dawson/Downloads/Executive_Summary_Module02.docx"
```

---

<!-- section_id: "4ce78e49-b4fc-442a-9dfb-9101e37e5101" -->
## Integration with Layer Structure

<!-- section_id: "7e5e4831-2da8-4c97-afe3-b0bafc0c30bd" -->
### Where This Lives

**Location**:
```
layer_0/layer_0_04_sub_layers/sub_layer_0_05+_setup_dependant/
  └── sub_layer_0_12_universal_tools/
      └── sub_layer_0_12_universal_tool_docx_ai_tool/
          └── sub_layer_0_14_agent_setup/outputs/
              └── DOCX_SKILL_SETUP_GUIDE.md (this file)
```

<!-- section_id: "e548bfc4-57c1-40e9-960e-83ee7955d4c3" -->
### Related Files

| File | Purpose |
|------|---------|
| `README.md` | Tool overview |
| `sub_layer_0_13_protocols/outputs/` | Operation protocols |
| `sub_layer_0_12_99_stages/` | Tool development lifecycle |

---

<!-- section_id: "79281ab2-6e70-4a28-a49e-c808658e6663" -->
## Workflow for Executive Summary Creation

<!-- section_id: "789fda34-e885-4160-8fb4-0b3bf74c8c01" -->
### 1. Preparation Phase
- [ ] Gather all data from Colab notebook
- [ ] Create visualization files (PNG/JPG)
- [ ] Prepare text content for each section

<!-- section_id: "76b7b40e-d4a7-4fed-8de2-32725ebfb58b" -->
### 2. Document Creation Phase
- [ ] Initialize .docx document with metadata
- [ ] Add each major section with headings
- [ ] Add detailed content for Implementation section (40 pts weight)
- [ ] Add Insights section with data-backed statements (20 pts weight)

<!-- section_id: "a475debf-46b4-47c4-97fb-bd1fbea232d7" -->
### 3. Visualization Phase
- [ ] Insert feature importance chart
- [ ] Insert model comparison chart
- [ ] Insert confusion matrix
- [ ] Insert ROC/AUC visualization
- [ ] Insert performance metrics chart
- [ ] Insert optional 6th visualization

<!-- section_id: "dac73a0c-008f-477b-b481-2dd6dc24b2bd" -->
### 4. Formatting Phase
- [ ] Apply consistent styling
- [ ] Verify all tables are formatted
- [ ] Ensure images are properly sized/labeled
- [ ] Check document layout

<!-- section_id: "bdbdccfc-148d-4c2f-953d-b310e195d338" -->
### 5. Finalization Phase
- [ ] Add discussion question responses
- [ ] Final spell/grammar check
- [ ] Save to .docx format
- [ ] Upload to Canvas

---

<!-- section_id: "53eeb56f-bdcd-41b3-80c6-807116fd84f0" -->
## Best Practices

<!-- section_id: "2191c087-c1fd-462f-884e-de258727ded2" -->
### Document Quality

1. **Professional Appearance**
   - Use consistent fonts (Calibri or Arial)
   - Proper heading hierarchy
   - Good whitespace/margins

2. **Content Organization**
   - Clear section breaks
   - Logical flow
   - Data-backed statements

3. **Visualization Quality**
   - High-resolution images
   - Proper labeling and captions
   - Supports main points

4. **Writing Standards**
   - Natural, conversational tone
   - Zero grammar/spelling errors
   - Professional but not overly formal

<!-- section_id: "9f45e1f8-05ce-4b0b-a885-4c65757ef63c" -->
### Technical Considerations

- All paths should be absolute paths
- Images should be high-quality (300+ DPI recommended)
- Tables should use consistent formatting
- Metadata (title, author) should be accurate

---

<!-- section_id: "757b9534-d636-4094-8ea6-acc69e79595a" -->
## Troubleshooting

<!-- section_id: "062acfd7-f976-4e82-9800-31093e29019b" -->
### If /docx skill isn't available

```bash
# Re-add the skill
claude skill add anthropics/docx --force

# Check for installation issues
claude skill list --debug

# Fall back to python-docx if needed
python3 -c "import docx; print('python-docx available')"
```

<!-- section_id: "40bea7e6-ab7d-4503-a657-05074797467e" -->
### If document creation fails

1. Verify all file paths are absolute
2. Check image file formats (PNG/JPG preferred)
3. Ensure proper permissions on output directory
4. Try creating with simple content first, then add complexity

---

<!-- section_id: "ae03ae67-df70-4f40-9499-9db8325c4f03" -->
## Next Steps

1. Verify `/docx` skill is installed
2. Gather Executive Summary data from Colab
3. Create visualization files
4. Initialize document and add sections
5. Format and finalize
6. Upload to Canvas

---

<!-- section_id: "ab2eb6b4-3a9d-4be1-9eb1-93ed654ba3c0" -->
## Version

**Created**: January 29, 2026
**Status**: Ready for implementation
**Last Updated**: 2026-01-29

---

<!-- section_id: "df4ef317-1846-430d-a8c1-7b4fe1e8bf4e" -->
## Related Documentation

- **Anthropic /docx Skill**: Official documentation (part of Claude Code)
- **python-docx**: Fallback library documentation
- **Office-Word-MCP-Server**: Alternative MCP approach
