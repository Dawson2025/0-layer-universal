---
resource_id: "d347939b-bcd7-4e94-a516-fd1a9a80f014"
resource_type: "output"
resource_name: "office_word_mcp_setup"
---
# Current Setup: Office Word MCP and DOCX Tools

<!-- section_id: "5672424e-e493-44c6-9858-79d4bde8453f" -->
## Date
2026-01-28

<!-- section_id: "152e5ef5-13d0-4611-a639-9ae3db437b3f" -->
## Status
OPERATIONAL

---

<!-- section_id: "6e3f233b-47e8-4cd9-a545-3317d053b593" -->
## Installed Tools

<!-- section_id: "18e04528-c8f7-4a3e-8bd8-cce30746b414" -->
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

<!-- section_id: "e0866d6c-729f-4fc5-a1df-4b8fd26d33ca" -->
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

<!-- section_id: "4b92eda6-b065-4d4c-922f-b1bb91cf5481" -->
## Available But Not Installed

<!-- section_id: "19ec04ee-cdb3-43c8-b8dc-bdb2a5d7f453" -->
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

<!-- section_id: "8e69d5f2-d152-49e1-aca1-8e0e06871a91" -->
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

<!-- section_id: "3f841b0f-1a54-4544-9685-4e81ee451438" -->
## Quick Reference

<!-- section_id: "7fb68e6b-09a4-4384-9366-ff62fddfc33b" -->
### View .docx on Linux
```bash
onlyoffice-desktopeditors /path/to/file.docx
```

<!-- section_id: "3129e0ef-af49-4262-9cdf-dc9c7a94f598" -->
### Convert .docx to text (quick check)
```bash
source ~/.local/venvs/docx-tools/bin/activate
python -c "from docx import Document; d = Document('file.docx'); print('\n'.join(p.text for p in d.paragraphs))"
```

<!-- section_id: "357020f7-5e23-4892-977e-7583b675d03b" -->
### Convert .docx to PDF
```bash
libreoffice --headless --convert-to pdf document.docx
```

---

<!-- section_id: "9b6ee8f8-05f4-47bd-b90a-ea223c194931" -->
## Related Documentation

| Document | Location |
|----------|----------|
| Request | `stage_0_01_request_gathering/outputs/REQ_docx_ai_integration.md` |
| Research | `stage_0_02_research/outputs/docx_mcp_research.md` |

---

<!-- section_id: "148090e8-59e6-4fb4-bfb7-7c808f795cd0" -->
## Next Steps (Optional)

1. Install Office-Word-MCP-Server if full MCP integration needed
2. Install `/docx` skill if using Claude Code document generation features
3. Consider docx-mcp (Rust) if security/sandbox features needed
