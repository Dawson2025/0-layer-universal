---
resource_id: "b5429122-b02c-4197-8cb8-a8c20c488cbe"
resource_type: "readme_output"
resource_name: "README"
---
# Staleness Detection -- Requirements Index

**Need**: [Staleness Detection](../README.md)

<!-- section_id: "61a918e2-87c3-4169-afee-9a3e8fe705f0" -->
## Overview

These requirements define how the system detects when distilled knowledge files (Tier 2) have drifted from their source stage outputs (Tier 3). A stale knowledge file is worse than no knowledge file because it gives agents false confidence. The requirements cover the detection mechanism itself -- timestamp comparison, content drift analysis, and integration with chain-validate -- and the reporting format that tells a developer exactly which files are stale, by how much, and whether re-consolidation is needed.

<!-- section_id: "64a5cd2b-b2cb-4867-bacd-d62fdd481adf" -->
## Key Themes

- **Detection Mechanism**: Staleness is detected by comparing knowledge file timestamps against referenced source timestamps, with optional content drift analysis for distinguishing minor edits from substantial changes
- **Actionable Reporting**: The staleness report is human-readable, lists each stale file with its source and time delta, and suggests whether the drift warrants re-consolidation

---

| REQ # | Name | Description | File |
|-------|------|-------------|------|
| REQ-01 | Detection Mechanism | How staleness is detected via timestamps and content drift | [REQ-01_detection_mechanism.md](./REQ-01_detection_mechanism.md) |
| REQ-02 | Reporting | Human-readable staleness report format | [REQ-02_reporting.md](./REQ-02_reporting.md) |
