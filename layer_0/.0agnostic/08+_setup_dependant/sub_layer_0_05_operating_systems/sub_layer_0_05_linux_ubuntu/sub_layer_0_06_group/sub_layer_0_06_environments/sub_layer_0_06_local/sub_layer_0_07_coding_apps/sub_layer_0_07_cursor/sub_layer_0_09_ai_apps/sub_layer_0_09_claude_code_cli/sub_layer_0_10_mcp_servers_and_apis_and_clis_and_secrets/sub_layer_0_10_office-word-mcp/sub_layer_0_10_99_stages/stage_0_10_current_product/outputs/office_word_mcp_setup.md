# Current Setup: Office Word MCP and DOCX Tools

## Date
2026-01-28

## Status
OPERATIONAL

---

## Installed Tools

### 1. OnlyOffice Desktop Editors

**Purpose**: View and edit .docx files with high fidelity on Linux

**Installation**:
```bash
sudo snap install onlyoffice-desktopeditors
```

**Version**: 9.2.1

**Usage**:
```bash
onlyoffice-desktopeditors /path/to/file.docx
```

### 2. Python DOCX Virtual Environment

**Purpose**: Programmatic .docx manipulation

**Location**: `~/.local/venvs/docx-tools`

**Packages**:
- python-docx
- docxedit

**Usage**:
```bash
source ~/.local/venvs/docx-tools/bin/activate
python -c "from docx import Document; d = Document('file.docx'); print('\n'.join(p.text for p in d.paragraphs))"
```

---

## Available But Not Installed

### Office-Word-MCP-Server

**Install when needed**:
```bash
pip install office-word-mcp
# or
git clone https://github.com/GongRzhe/Office-Word-MCP-Server
cd Office-Word-MCP-Server
pip install -r requirements.txt
```

**Add to Claude Code**:
```bash
claude mcp add office-word -- python -m office_word_mcp
```

### Claude Code /docx Skill

**Install when needed**:
```bash
claude skill add anthropics/docx
```

**Usage**:
```
/docx Create a project proposal with executive summary
```

---

## Quick Reference

### View .docx on Linux
```bash
onlyoffice-desktopeditors /path/to/file.docx
```

### Convert .docx to text (quick check)
```bash
source ~/.local/venvs/docx-tools/bin/activate
python -c "from docx import Document; d = Document('file.docx'); print('\n'.join(p.text for p in d.paragraphs))"
```

### Convert .docx to PDF
```bash
libreoffice --headless --convert-to pdf document.docx
```

---

## Related Documentation

| Document | Location |
|----------|----------|
| Request | `stage_0_01_request_gathering/outputs/REQ_docx_ai_integration.md` |
| Research | `stage_0_02_research/outputs/docx_mcp_research.md` |

---

## Next Steps (Optional)

1. Install Office-Word-MCP-Server if full MCP integration needed
2. Install `/docx` skill if using Claude Code document generation features
3. Consider docx-mcp (Rust) if security/sandbox features needed
