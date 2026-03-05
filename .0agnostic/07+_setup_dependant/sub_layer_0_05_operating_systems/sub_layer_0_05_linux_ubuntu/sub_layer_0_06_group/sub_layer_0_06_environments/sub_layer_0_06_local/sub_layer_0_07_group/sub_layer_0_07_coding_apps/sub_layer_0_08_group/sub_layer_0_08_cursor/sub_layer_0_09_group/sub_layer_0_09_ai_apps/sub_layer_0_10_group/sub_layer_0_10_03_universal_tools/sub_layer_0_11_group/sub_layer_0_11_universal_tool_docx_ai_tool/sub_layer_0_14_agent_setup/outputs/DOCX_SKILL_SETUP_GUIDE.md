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

## Installation

### Step 1: Add the Skill

```bash
claude skill add anthropics/docx
```

This installs Anthropic's officially maintained `/docx` skill into your Claude Code environment.

### Step 2: Verify Installation

```bash
claude skill list | grep docx
```

You should see `/docx` in the available skills list.

---

## Why Use /docx Skill?

### Advantages Over Direct python-docx

| Aspect | /docx Skill | Direct python-docx |
|--------|------------|-------------------|
| **Design** | Built by Anthropic for Claude | General-purpose Python library |
| **Interface** | High-level abstractions | Low-level XML manipulation |
| **Context Awareness** | Understands document state | No state awareness |
| **Error Handling** | Optimized for AI use | Generic exception handling |
| **Efficiency** | Natural language commands | Manual code writing |
| **Maintenance** | Officially supported | Community library |

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

## Basic Skill Usage

### Creating a Document

The `/docx` skill provides high-level commands:

```
/docx create
  --title "Executive Summary - Module 02"
  --author "Your Team"
  --output "/home/dawson/Downloads/Executive_Summary.docx"
```

### Adding Content

```
/docx add-heading "Section Title" --level 1
/docx add-paragraph "Your paragraph text here."
/docx add-table --rows 3 --cols 4
/docx add-image "/path/to/image.png"
/docx format-text bold italic underline
```

### Styling

```
/docx set-style "Heading 1"
/docx set-font-size 12
/docx set-color blue
```

### Saving & Converting

```
/docx save
/docx convert-to-pdf
```

---

## Implementation for Executive Summary

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

### Implementation Strategy

1. **Create base document** with title, author metadata
2. **Add each section** as heading + paragraphs
3. **Insert data tables** for metrics and results
4. **Embed visualizations** as high-quality images
5. **Format for professionalism** (consistent fonts, spacing, styles)
6. **Save and convert** to final .docx format

---

## Key Commands for This Project

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

## Integration with Layer Structure

### Where This Lives

**Location**:
```
layer_0/layer_0_04_sub_layers/sub_layer_0_05+_setup_dependant/
  └── sub_layer_0_12_universal_tools/
      └── sub_layer_0_12_universal_tool_docx_ai_tool/
          └── sub_layer_0_14_agent_setup/outputs/
              └── DOCX_SKILL_SETUP_GUIDE.md (this file)
```

### Related Files

| File | Purpose |
|------|---------|
| `README.md` | Tool overview |
| `sub_layer_0_13_protocols/outputs/` | Operation protocols |
| `sub_layer_0_12_99_stages/` | Tool development lifecycle |

---

## Workflow for Executive Summary Creation

### 1. Preparation Phase
- [ ] Gather all data from Colab notebook
- [ ] Create visualization files (PNG/JPG)
- [ ] Prepare text content for each section

### 2. Document Creation Phase
- [ ] Initialize .docx document with metadata
- [ ] Add each major section with headings
- [ ] Add detailed content for Implementation section (40 pts weight)
- [ ] Add Insights section with data-backed statements (20 pts weight)

### 3. Visualization Phase
- [ ] Insert feature importance chart
- [ ] Insert model comparison chart
- [ ] Insert confusion matrix
- [ ] Insert ROC/AUC visualization
- [ ] Insert performance metrics chart
- [ ] Insert optional 6th visualization

### 4. Formatting Phase
- [ ] Apply consistent styling
- [ ] Verify all tables are formatted
- [ ] Ensure images are properly sized/labeled
- [ ] Check document layout

### 5. Finalization Phase
- [ ] Add discussion question responses
- [ ] Final spell/grammar check
- [ ] Save to .docx format
- [ ] Upload to Canvas

---

## Best Practices

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

### Technical Considerations

- All paths should be absolute paths
- Images should be high-quality (300+ DPI recommended)
- Tables should use consistent formatting
- Metadata (title, author) should be accurate

---

## Troubleshooting

### If /docx skill isn't available

```bash
# Re-add the skill
claude skill add anthropics/docx --force

# Check for installation issues
claude skill list --debug

# Fall back to python-docx if needed
python3 -c "import docx; print('python-docx available')"
```

### If document creation fails

1. Verify all file paths are absolute
2. Check image file formats (PNG/JPG preferred)
3. Ensure proper permissions on output directory
4. Try creating with simple content first, then add complexity

---

## Next Steps

1. Verify `/docx` skill is installed
2. Gather Executive Summary data from Colab
3. Create visualization files
4. Initialize document and add sections
5. Format and finalize
6. Upload to Canvas

---

## Version

**Created**: January 29, 2026
**Status**: Ready for implementation
**Last Updated**: 2026-01-29

---

## Related Documentation

- **Anthropic /docx Skill**: Official documentation (part of Claude Code)
- **python-docx**: Fallback library documentation
- **Office-Word-MCP-Server**: Alternative MCP approach
