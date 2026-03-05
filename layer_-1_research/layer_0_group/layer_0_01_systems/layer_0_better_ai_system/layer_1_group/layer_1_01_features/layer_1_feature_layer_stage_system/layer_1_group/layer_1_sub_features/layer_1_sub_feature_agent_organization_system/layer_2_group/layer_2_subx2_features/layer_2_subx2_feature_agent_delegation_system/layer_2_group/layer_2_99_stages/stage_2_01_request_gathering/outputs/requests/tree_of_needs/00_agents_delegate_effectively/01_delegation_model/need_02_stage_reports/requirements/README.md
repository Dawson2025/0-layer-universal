---
resource_id: "c7a6f9bf-f7fc-40d1-b8e6-54f2a35bfc85"
resource_type: "readme
output"
resource_name: "README"
---
# Stage Reports -- Requirements Index

**Need**: [Stage Reports](../README.md)

<!-- section_id: "fa66974f-510b-4b49-8570-0b2ac4e7a5ae" -->
## Overview

These requirements define the stage report protocol — a concise, async status mechanism that lets managers understand what happened in a stage without loading its detailed outputs. Reports must live at a consistent location (`outputs/stage_report.md`), be written before every session exit, and contain status, summary, outputs, blockers, and next steps. The key constraint is that stage reports must be under 30 lines and sufficient for delegation decisions.

<!-- section_id: "20cbde9a-118c-4195-9784-d711657aea7c" -->
## Key Themes

- **Report Protocol**: Where reports live, when they're written, and what triggers an update — establishing a consistent, predictable mechanism across all stages
- **Content Requirements**: Reports must include status, work summary, key outputs, blockers, and actionable next steps — but never full methodology or detailed findings
- **Manager Consumption**: Reports are designed to be read by managers making delegation decisions; they must be concise enough to scan multiple stages quickly

---

| REQ# | Name | Description | File |
|------|------|-------------|------|
| REQ-01 | Report Protocol | Where reports live, when written, what they contain | [REQ-01_report_protocol.md](./REQ-01_report_protocol.md) |
| REQ-02 | Report Content | Required fields: status, summary, outputs, blockers, next steps | [REQ-02_report_content.md](./REQ-02_report_content.md) |
| REQ-03 | Report Consumption | Concise, enabling delegation decisions without stage details | [REQ-03_report_consumption.md](./REQ-03_report_consumption.md) |
