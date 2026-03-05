---
resource_id: "bf455f6d-00ed-4994-9226-f93e4d2a09c9"
resource_type: "output"
resource_name: "US-02_script_validates_references"
---
# US-02: Script validates all references

**Need**: [Reference Format Standard](../README.md)

---

**As a** user who wants to check that all knowledge file references are still valid,
**I want** to run a validation script that finds and checks every reference,
**So that** I catch broken links (moved files, renamed sections) before the AI hits a dead end.

<!-- section_id: "4f029149-27fc-4ceb-8c06-28b8b56e266a" -->
### What Happens

1. User runs the reference validation script
2. Script parses all references in all knowledge files using the standard format
3. Script checks each referenced path exists and the section is present
4. Script produces a report listing any broken references with their location and target

<!-- section_id: "d0bc8d6f-b422-4cf7-9427-96d324c80460" -->
### Acceptance Criteria

- Script finds and validates every reference in every knowledge file
- Broken references are reported with file location and what they point to
- Script exits with non-zero status if any references are broken
