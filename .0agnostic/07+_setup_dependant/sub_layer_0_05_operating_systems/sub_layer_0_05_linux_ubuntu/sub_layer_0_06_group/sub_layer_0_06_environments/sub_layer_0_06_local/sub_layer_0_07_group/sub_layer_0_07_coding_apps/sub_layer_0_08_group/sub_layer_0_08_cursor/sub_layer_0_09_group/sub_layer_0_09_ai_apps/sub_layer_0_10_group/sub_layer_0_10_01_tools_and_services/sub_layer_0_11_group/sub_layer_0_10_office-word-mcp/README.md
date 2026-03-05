---
resource_id: "60992295-730f-48aa-a576-e858ec46ecec"
resource_type: "readme
document"
resource_name: "README"
---
# Office Word MCP Server

## Overview

MCP (Model Context Protocol) server for creating, reading, and manipulating Microsoft Word documents (.docx files) via AI agents.

## Status

**Current Stage**: 02_research (completed) -> 10_current_product

## Primary Server

**Office-Word-MCP-Server** by GongRzhe
- GitHub: https://github.com/GongRzhe/Office-Word-MCP-Server
- Stars: 900+
- Language: Python
- License: MIT

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

## Installation

```bash
# Install via pip
pip install office-word-mcp

# Or clone and install
git clone https://github.com/GongRzhe/Office-Word-MCP-Server
cd Office-Word-MCP-Server
pip install -r requirements.txt
```

## Claude Code Integration

```bash
claude mcp add office-word -- python -m office_word_mcp
```

## Alternative: Claude Code Skills

Official Anthropic skills are also available:
- `/docx` - Create, edit, analyze Word documents
- `/doc-coauthoring` - Collaborative document editing

Install via:
```bash
claude skill add anthropics/docx
```

## Related Documentation

| Stage | Document |
|-------|----------|
| Request | `sub_layer_0_10_99_stages/stage_0_01_request_gathering/outputs/REQ_docx_ai_integration.md` |
| Research | `sub_layer_0_10_99_stages/stage_0_02_research/outputs/docx_mcp_research.md` |
| Current Setup | `sub_layer_0_10_99_stages/stage_0_10_current_product/outputs/office_word_mcp_setup.md` |

## Linux Viewing Tools

For viewing/editing .docx files on Linux Ubuntu:
- **OnlyOffice** (recommended) - Best .docx compatibility
- **LibreOffice Writer** - Pre-installed
- **Microsoft 365 Web** - 100% compatibility via browser
