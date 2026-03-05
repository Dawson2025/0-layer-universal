---
resource_id: "9a3f299a-ac68-48d7-8099-a465bcb22db2"
resource_type: "output"
resource_name: "REQ-03_change_detection"
---
# REQ-03: Change Detection Scope

**Need**: [Trigger Automation](../README.md)

<!-- section_id: "94791cd7-f22e-4bc3-9cbf-79663fd7da08" -->
## Requirements

- **MUST** detect when a canonical target directory has been renamed or moved
- **MUST** identify which pointer files are affected by a given structural change
- **SHOULD** support incremental detection (only resync affected pointers, not all)
- **MUST** fall back to full rescan when incremental detection is uncertain
- **SHOULD** log which pointers were detected as stale and what triggered the detection
- **MUST NOT** miss broken pointers after a directory rename (zero false negatives for structural changes)
