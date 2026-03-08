---
resource_id: "8ba37699-f4f5-429c-9e73-6f1d22438fde"
resource_type: "readme_output"
resource_name: "README"
---
# Consolidation Process -- Requirements Index

**Need**: [Consolidation Process](../README.md)

<!-- section_id: "c81eb54f-c3dc-48fe-8276-7180a6afa9c2" -->
## Overview

These requirements define when and how raw stage outputs (Tier 3) are distilled into actionable knowledge files (Tier 2). Without a defined consolidation process, knowledge files never get created and agents are forced to read raw outputs every time. The requirements cover event-driven triggers (stage completion, major milestones), a step-by-step distillation protocol that enforces compression over duplication, and supporting tooling that measures compression ratios and generates consolidation reports.

<!-- section_id: "6d6f9d7f-0fc3-4f56-93f3-54446c46b528" -->
## Key Themes

- **Event-Driven Triggers**: Consolidation happens at natural stage boundaries (stage completion, major milestones), not continuously -- matching the brain's sleep consolidation pattern
- **Distillation Protocol**: A step-by-step process ensures knowledge files are shorter than their sources, include source references, and pass a quality checklist
- **Tooling Support**: Scripts and skills assist the distillation process, generating reports that track what was consolidated and the resulting compression ratio

---

| REQ # | Name | Description | File |
|-------|------|-------------|------|
| REQ-01 | Trigger Definition | When consolidation happens | [REQ-01_trigger_definition.md](./REQ-01_trigger_definition.md) |
| REQ-02 | Consolidation Protocol | Step-by-step distillation process | [REQ-02_consolidation_protocol.md](./REQ-02_consolidation_protocol.md) |
| REQ-03 | Tooling | Scripts and skills to assist distillation | [REQ-03_tooling.md](./REQ-03_tooling.md) |
