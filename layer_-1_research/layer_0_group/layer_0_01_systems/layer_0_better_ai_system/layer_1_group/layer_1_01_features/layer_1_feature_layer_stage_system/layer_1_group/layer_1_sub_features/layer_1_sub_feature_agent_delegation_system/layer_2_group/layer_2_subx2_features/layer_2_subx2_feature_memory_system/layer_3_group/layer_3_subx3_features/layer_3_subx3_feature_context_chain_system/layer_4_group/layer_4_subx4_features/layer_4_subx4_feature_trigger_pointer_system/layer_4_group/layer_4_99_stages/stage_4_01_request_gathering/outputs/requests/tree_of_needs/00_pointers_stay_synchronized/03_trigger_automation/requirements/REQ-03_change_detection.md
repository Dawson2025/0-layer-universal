# REQ-03: Change Detection Scope

**Need**: [Trigger Automation](../README.md)

## Requirements

- **MUST** detect when a canonical target directory has been renamed or moved
- **MUST** identify which pointer files are affected by a given structural change
- **SHOULD** support incremental detection (only resync affected pointers, not all)
- **MUST** fall back to full rescan when incremental detection is uncertain
- **SHOULD** log which pointers were detected as stale and what triggered the detection
- **MUST NOT** miss broken pointers after a directory rename (zero false negatives for structural changes)
