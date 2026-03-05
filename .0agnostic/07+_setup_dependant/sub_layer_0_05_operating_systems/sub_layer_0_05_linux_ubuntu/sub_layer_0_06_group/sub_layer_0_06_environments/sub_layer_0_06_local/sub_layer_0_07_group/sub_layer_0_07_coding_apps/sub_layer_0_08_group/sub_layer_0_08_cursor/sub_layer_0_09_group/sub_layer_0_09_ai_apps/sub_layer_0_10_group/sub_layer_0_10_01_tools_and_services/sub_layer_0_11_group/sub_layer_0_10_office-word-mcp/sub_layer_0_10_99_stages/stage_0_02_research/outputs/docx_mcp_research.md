---
resource_id: "07f24ae1-ab7a-49f4-a9db-42dde8c78016"
resource_type: "output"
resource_name: "docx_mcp_research"
---
# Research: DOCX MCP Servers and AI Agent Integration

## Date
2026-01-28

## Research Summary

This document captures research findings on the best ways for AI agents to work with Microsoft Word (.docx) files as of 2025-2026.

---

## Key Finding: MCP is the Standard

**Model Context Protocol (MCP)** is the standardized way for AI agents to connect to external tools and data sources. Anthropic introduced MCP in November 2024, and it has become the de-facto standard for AI tool integration.

---

## MCP Servers for Word Documents

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

### Alternative MCP Servers

| Server | Language | Features | Best For |
|--------|----------|----------|----------|
| **docx-mcp** | Rust | Security features, readonly mode, sandbox | Enterprise with security needs |
| **word-mcp-server** | TypeScript | LibreOffice PDF conversion | PDF workflow |
| **Microsoft Word MCP** | Official | OneDrive/SharePoint integration | Microsoft 365 users |

---

## Claude Code Skills (Alternative to MCP)

Anthropic provides official skills for document manipulation:

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

### /doc-coauthoring Skill
- Collaborative document editing
- Iterative refinement workflow

### How Skills Work
- Uses **docx-js** (JavaScript) for creating new documents
- Uses **Python OOXML manipulation** for editing existing documents
- Uses **pandoc** for text extraction and format conversion

---

## Linux Viewing/Editing Tools

For viewing .docx files created by AI agents on Linux:

| Tool | Compatibility | Install | Notes |
|------|---------------|---------|-------|
| **OnlyOffice** | ~95% | `sudo snap install onlyoffice-desktopeditors` | Best native Linux option |
| **WPS Office** | ~95% | Download from wps.com | Very close to MS Office |
| **LibreOffice** | ~80% | Pre-installed | Good for basic editing |
| **Microsoft 365 Web** | 100% | Browser | Requires Microsoft account |

---

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

## Recommendations

### For Claude Code Users
1. **Primary**: Install `/docx` skill via `claude skill add anthropics/docx`
2. **Alternative**: Set up Office-Word-MCP-Server for more control

### For General AI Agent Integration
1. Use MCP servers - they're the standard
2. Office-Word-MCP-Server is the most mature option

### For Viewing Results on Linux
1. Install OnlyOffice for best compatibility
2. Use Microsoft 365 Web for 100% fidelity verification

---

## Sources

- Perplexity search: "MCP Model Context Protocol Word docx server AI agents 2025 2026"
- Perplexity search: "Claude Code skills slash commands docx Word document manipulation 2025"
- GitHub: GongRzhe/Office-Word-MCP-Server
- Anthropic: Model Context Protocol documentation
- Claude Code documentation: code.claude.com/docs
