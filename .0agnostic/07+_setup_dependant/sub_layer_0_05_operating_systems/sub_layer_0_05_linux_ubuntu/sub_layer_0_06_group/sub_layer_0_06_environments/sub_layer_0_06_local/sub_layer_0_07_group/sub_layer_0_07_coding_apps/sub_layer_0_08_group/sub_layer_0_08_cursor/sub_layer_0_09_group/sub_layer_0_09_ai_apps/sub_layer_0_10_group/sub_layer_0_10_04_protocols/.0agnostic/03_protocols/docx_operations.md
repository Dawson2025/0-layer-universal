---
resource_id: "dce69976-efb6-4911-b725-6768f2833d6c"
resource_type: "protocol"
resource_name: "docx_operations"
---
# Protocol: DOCX Operations

<!-- section_id: "846ee6b8-7191-4249-8e57-2ef6d21fad81" -->
## Overview

This protocol defines how AI agents should work with Microsoft Word (.docx) files.

---

<!-- section_id: "9f2f41b8-7eb2-4766-8988-c07797d8fcb5" -->
## Method Selection

<!-- section_id: "0b248e39-1b5f-498b-bd6b-c88703ca7197" -->
### Use MCP Server When:
- Need full document manipulation capabilities
- Working with complex formatting
- Batch processing multiple documents
- Need tracked changes, comments
- Converting to PDF

<!-- section_id: "64941ed6-e848-40a2-a1b8-23976ddcba29" -->
### Use Claude Code /docx Skill When:
- Creating new documents from scratch
- Quick document generation
- Don't need MCP infrastructure

<!-- section_id: "087cdb51-2dbe-4eee-b1e4-90fb6db35b24" -->
### Use Python (python-docx) When:
- Simple text extraction
- Basic document creation
- Already in Python workflow

---

<!-- section_id: "e3c4bc61-5261-4f75-8bde-499b8a0258a6" -->
## Workflow: Create New Document

<!-- section_id: "9ff9bdd3-46c8-4aeb-ad6d-a49e56599fa9" -->
### Option A: Using /docx Skill
```
/docx Create a [document type] with [sections/content]
```

<!-- section_id: "df202c95-bbf0-4503-9a80-78993deac33a" -->
### Option B: Using MCP
```bash
# Ensure MCP server is running
claude mcp add office-word -- python -m office_word_mcp

# Then in conversation:
"Create a new Word document called report.docx with title page"
```

<!-- section_id: "a2c590db-81f6-45c5-a9a4-5593ec100a55" -->
### Option C: Using Python
```python
from docx import Document

doc = Document()
doc.add_heading('Title', 0)
doc.add_paragraph('Content here')
doc.save('output.docx')
```

---

<!-- section_id: "56dec3da-4c56-447c-9e87-1a3ec8e7d82d" -->
## Workflow: Read Existing Document

<!-- section_id: "acb84a2e-703b-4c03-97ad-9e61a5b0cf4d" -->
### Quick Text Extraction
```bash
source ~/.local/venvs/docx-tools/bin/activate
python -c "from docx import Document; d = Document('file.docx'); print('\n'.join(p.text for p in d.paragraphs))"
```

<!-- section_id: "5fa42929-6ada-4717-a8f5-4988e1c3bb8a" -->
### With Formatting (via pandoc)
```bash
pandoc file.docx -o output.md
```

<!-- section_id: "f2baaa32-75c9-4dfc-a531-be6d565c4e9d" -->
### Via MCP
"Read the contents of report.docx and summarize"

---

<!-- section_id: "29ca72d9-a4a0-40b4-a50d-b36e2337f65f" -->
## Workflow: Edit Existing Document

<!-- section_id: "5487e9a8-bece-4e23-8e02-fb659b72049c" -->
### Preserve Formatting
Use `docxedit` library or MCP server - both preserve formatting better than basic python-docx.

<!-- section_id: "c2fe3c72-2fbe-48cb-b1cd-32140133e78e" -->
### With Tracked Changes
Use MCP server or /docx skill - both support tracked changes.

---

<!-- section_id: "08f03c14-34b7-4f40-8bed-1916da09ec5f" -->
## Workflow: View Results

<!-- section_id: "085e004a-2882-4995-a695-3cfac498312a" -->
### On Linux
```bash
onlyoffice-desktopeditors /path/to/file.docx
```

<!-- section_id: "b1fb5d34-cb11-4dcf-b628-e549870d9668" -->
### Quick PDF Preview
```bash
libreoffice --headless --convert-to pdf document.docx
xdg-open document.pdf
```

---

<!-- section_id: "41a47c1c-cc3e-4a3f-9568-e513fe20cb8f" -->
## Best Practices

1. **Always preserve formatting** - Use tools that maintain original styling
2. **Verify output** - Open in OnlyOffice or Microsoft 365 Web to check formatting
3. **Use MCP for complex operations** - Direct tool calls are more reliable than prompting
4. **Keep backup** - Before editing, consider copying original file

---

<!-- section_id: "7cfa3125-95db-4213-a10a-0b865a413a74" -->
## Related Documentation

- Research: `sub_layer_0_10_office-word-mcp/sub_layer_0_10_99_stages/stage_0_02_research/outputs/docx_mcp_research.md`
- Setup: `sub_layer_0_10_office-word-mcp/sub_layer_0_10_99_stages/stage_0_10_current_product/outputs/office_word_mcp_setup.md`
