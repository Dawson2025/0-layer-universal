---
resource_id: "07f24ae1-ab7a-49f4-a9db-42dde8c78016"
resource_type: "output"
resource_name: "docx_mcp_research"
---
# Research: DOCX MCP Servers and AI Agent Integration

<!-- section_id: "4e47c703-ce87-4836-a46f-03f02397deae" -->
## Date
2026-01-28

<!-- section_id: "7cdec1bc-2bcb-45f2-a51f-fa28d2191165" -->
## Research Summary

This document captures research findings on the best ways for AI agents to work with Microsoft Word (.docx) files as of 2025-2026.

---

<!-- section_id: "c5b13824-e15f-4d56-a0fc-a357a7b1288c" -->
## Key Finding: MCP is the Standard

**Model Context Protocol (MCP)** is the standardized way for AI agents to connect to external tools and data sources. Anthropic introduced MCP in November 2024, and it has become the de-facto standard for AI tool integration.

---

<!-- section_id: "f43c7320-b933-414c-803a-846623cd4176" -->
## MCP Servers for Word Documents

<!-- section_id: "f48d3dcc-e68e-4ff9-a87e-dd7914d2293b" -->
### Top Recommendation: Office-Word-MCP-Server

| Attribute | Value |
|-----------|-------|
| **Repository** | https://github.com/GongRzhe/Office-Word-MCP-Server |
| **Stars** | 900+ |
| **Language** | Python |
| **License** | MIT |
| **Maintainer** | GongRzhe |

**Capabilities:**
- Create new Word documents with metadata
- Extract text and analyze document structure
- View document properties and statistics
- List available documents in a directory
- Create copies of existing documents
- Merge multiple documents
- Convert Word documents to PDF format
- Add headings with different levels and formatting
- Insert paragraphs with optional styling
- Create tables with custom data
- Add images with proportional scaling
- Insert page breaks, bulleted/numbered lists
- Format text (bold, italic, underline, color, font)
- Search and replace text
- Add password protection
- Extract and manage comments

<!-- section_id: "0fa8b3ef-d380-4c69-a2ee-2d0103f89c41" -->
### Alternative MCP Servers

| Server | Language | Features | Best For |
|--------|----------|----------|----------|
| **docx-mcp** | Rust | Security features, readonly mode, sandbox | Enterprise with security needs |
| **word-mcp-server** | TypeScript | LibreOffice PDF conversion | PDF workflow |
| **Microsoft Word MCP** | Official | OneDrive/SharePoint integration | Microsoft 365 users |

---

<!-- section_id: "134290d1-acfe-428a-a033-a1ee64dd19cb" -->
## Claude Code Skills (Alternative to MCP)

Anthropic provides official skills for document manipulation:

<!-- section_id: "966e8d40-433b-483a-bb37-1c3f1c67a457" -->
### /docx Skill
- Create, edit, analyze Word documents
- Tracked changes support
- Comments
- Formatting preservation
- Text extraction

**Installation:**
```bash
claude skill add anthropics/docx
```

<!-- section_id: "ce61f241-6180-4cc9-9dd0-bbea12798f2b" -->
### /doc-coauthoring Skill
- Collaborative document editing
- Iterative refinement workflow

<!-- section_id: "b1ebfa2f-6169-457a-8fb5-3f2d2a34dcc5" -->
### How Skills Work
- Uses **docx-js** (JavaScript) for creating new documents
- Uses **Python OOXML manipulation** for editing existing documents
- Uses **pandoc** for text extraction and format conversion

---

<!-- section_id: "b83b00f0-6640-40c1-907e-fb5ffc7d341f" -->
## Linux Viewing/Editing Tools

For viewing .docx files created by AI agents on Linux:

| Tool | Compatibility | Install | Notes |
|------|---------------|---------|-------|
| **OnlyOffice** | ~95% | `sudo snap install onlyoffice-desktopeditors` | Best native Linux option |
| **WPS Office** | ~95% | Download from wps.com | Very close to MS Office |
| **LibreOffice** | ~80% | Pre-installed | Good for basic editing |
| **Microsoft 365 Web** | 100% | Browser | Requires Microsoft account |

---

<!-- section_id: "89b348d0-5f59-4519-99fd-15f787297b35" -->
## Python Libraries

For programmatic manipulation without MCP:

| Library | Purpose | Install |
|---------|---------|---------|
| **python-docx** | Read/write .docx files | `pip install python-docx` |
| **docxedit** | Better formatting preservation | `pip install docxedit` |

Virtual environment setup:
```bash
python3 -m venv ~/.local/venvs/docx-tools
source ~/.local/venvs/docx-tools/bin/activate
pip install python-docx docxedit
```

---

<!-- section_id: "2a760e0e-009a-44cb-926d-b8e168ff8dda" -->
## Recommendations

<!-- section_id: "cf21b6c4-d174-404f-a744-f7f510c15330" -->
### For Claude Code Users
1. **Primary**: Install `/docx` skill via `claude skill add anthropics/docx`
2. **Alternative**: Set up Office-Word-MCP-Server for more control

<!-- section_id: "81d3b727-2c33-4596-b158-ceba390a33b9" -->
### For General AI Agent Integration
1. Use MCP servers - they're the standard
2. Office-Word-MCP-Server is the most mature option

<!-- section_id: "9187e658-e65b-4364-a6a0-3c850ea93543" -->
### For Viewing Results on Linux
1. Install OnlyOffice for best compatibility
2. Use Microsoft 365 Web for 100% fidelity verification

---

<!-- section_id: "83c4e634-3599-41cb-a64e-b92f27e4cf13" -->
## Sources

- Perplexity search: "MCP Model Context Protocol Word docx server AI agents 2025 2026"
- Perplexity search: "Claude Code skills slash commands docx Word document manipulation 2025"
- GitHub: GongRzhe/Office-Word-MCP-Server
- Anthropic: Model Context Protocol documentation
- Claude Code documentation: code.claude.com/docs
