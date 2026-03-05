---
resource_id: "dce69976-efb6-4911-b725-6768f2833d6c"
resource_type: "protocol"
resource_name: "docx_operations"
---
# Protocol: DOCX Operations

## Overview

This protocol defines how AI agents should work with Microsoft Word (.docx) files.

---

## Method Selection

### Use MCP Server When:
- Need full document manipulation capabilities
- Working with complex formatting
- Batch processing multiple documents
- Need tracked changes, comments
- Converting to PDF

### Use Claude Code /docx Skill When:
- Creating new documents from scratch
- Quick document generation
- Don't need MCP infrastructure

### Use Python (python-docx) When:
- Simple text extraction
- Basic document creation
- Already in Python workflow

---

## Workflow: Create New Document

### Option A: Using /docx Skill
```
/docx Create a [document type] with [sections/content]
```

### Option B: Using MCP
```bash
# Ensure MCP server is running
claude mcp add office-word -- python -m office_word_mcp

# Then in conversation:
"Create a new Word document called report.docx with title page"
```

### Option C: Using Python
```python
from docx import Document

doc = Document()
doc.add_heading('Title', 0)
doc.add_paragraph('Content here')
doc.save('output.docx')
```

---

## Workflow: Read Existing Document

### Quick Text Extraction
```bash
source ~/.local/venvs/docx-tools/bin/activate
python -c "from docx import Document; d = Document('file.docx'); print('\n'.join(p.text for p in d.paragraphs))"
```

### With Formatting (via pandoc)
```bash
pandoc file.docx -o output.md
```

### Via MCP
"Read the contents of report.docx and summarize"

---

## Workflow: Edit Existing Document

### Preserve Formatting
Use `docxedit` library or MCP server - both preserve formatting better than basic python-docx.

### With Tracked Changes
Use MCP server or /docx skill - both support tracked changes.

---

## Workflow: View Results

### On Linux
```bash
onlyoffice-desktopeditors /path/to/file.docx
```

### Quick PDF Preview
```bash
libreoffice --headless --convert-to pdf document.docx
xdg-open document.pdf
```

---

## Best Practices

1. **Always preserve formatting** - Use tools that maintain original styling
2. **Verify output** - Open in OnlyOffice or Microsoft 365 Web to check formatting
3. **Use MCP for complex operations** - Direct tool calls are more reliable than prompting
4. **Keep backup** - Before editing, consider copying original file

---

## Related Documentation

- Research: `sub_layer_0_10_office-word-mcp/sub_layer_0_10_99_stages/stage_0_02_research/outputs/docx_mcp_research.md`
- Setup: `sub_layer_0_10_office-word-mcp/sub_layer_0_10_99_stages/stage_0_10_current_product/outputs/office_word_mcp_setup.md`
