---
resource_id: "60992295-730f-48aa-a576-e858ec46ecec"
resource_type: "readme_document"
resource_name: "README"
---
# Office Word MCP Server

<!-- section_id: "771077ff-b642-40b2-af55-a90bdbeb5f7b" -->
## Overview

MCP (Model Context Protocol) server for creating, reading, and manipulating Microsoft Word documents (.docx files) via AI agents.

<!-- section_id: "91c444dc-153b-469f-b211-2e9d9a7f5898" -->
## Status

**Current Stage**: 02_research (completed) -> 10_current_product

<!-- section_id: "136f4549-ca41-48c4-8cfa-8da9f6076b67" -->
## Primary Server

**Office-Word-MCP-Server** by GongRzhe
- GitHub: https://github.com/GongRzhe/Office-Word-MCP-Server
- Stars: 900+
- Language: Python
- License: MIT

<!-- section_id: "13a4b8d4-a3ca-4538-a283-d61943794e8f" -->
## Capabilities

- Create new Word documents with metadata
- Extract text and analyze document structure
- Add headings, paragraphs, tables, images
- Format text (bold, italic, colors, fonts)
- Search and replace text
- Convert to PDF
- Add password protection
- Extract and manage comments
- Tracked changes support

<!-- section_id: "3afedc32-5544-4679-a6d6-ed1e867672d8" -->
## Installation

```bash
# Install via pip
pip install office-word-mcp

# Or clone and install
git clone https://github.com/GongRzhe/Office-Word-MCP-Server
cd Office-Word-MCP-Server
pip install -r requirements.txt
```

<!-- section_id: "010a5c98-ab5e-43a4-81e7-46925e769f36" -->
## Claude Code Integration

```bash
claude mcp add office-word -- python -m office_word_mcp
```

<!-- section_id: "b4674b70-f71e-4a6c-bb14-89a4fc6d1fb5" -->
## Alternative: Claude Code Skills

Official Anthropic skills are also available:
- `/docx` - Create, edit, analyze Word documents
- `/doc-coauthoring` - Collaborative document editing

Install via:
```bash
claude skill add anthropics/docx
```

<!-- section_id: "57ef6302-a479-4485-bec0-33458e7801d7" -->
## Related Documentation

| Stage | Document |
|-------|----------|
| Request | `sub_layer_0_10_99_stages/stage_0_01_request_gathering/outputs/REQ_docx_ai_integration.md` |
| Research | `sub_layer_0_10_99_stages/stage_0_02_research/outputs/docx_mcp_research.md` |
| Current Setup | `sub_layer_0_10_99_stages/stage_0_10_current_product/outputs/office_word_mcp_setup.md` |

<!-- section_id: "44a263fe-42a7-4b16-b292-b0685318568a" -->
## Linux Viewing Tools

For viewing/editing .docx files on Linux Ubuntu:
- **OnlyOffice** (recommended) - Best .docx compatibility
- **LibreOffice Writer** - Pre-installed
- **Microsoft 365 Web** - 100% compatibility via browser
