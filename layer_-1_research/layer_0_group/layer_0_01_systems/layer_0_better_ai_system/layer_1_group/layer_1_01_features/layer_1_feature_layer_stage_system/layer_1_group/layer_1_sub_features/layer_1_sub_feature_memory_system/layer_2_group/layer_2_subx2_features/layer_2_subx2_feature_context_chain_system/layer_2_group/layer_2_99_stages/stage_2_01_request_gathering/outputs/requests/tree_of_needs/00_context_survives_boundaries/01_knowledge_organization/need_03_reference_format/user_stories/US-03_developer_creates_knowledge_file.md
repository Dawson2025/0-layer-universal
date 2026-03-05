---
resource_id: "6eb866a4-52bd-47e4-8207-dcc3f544c938"
resource_type: "output"
resource_name: "US-03_developer_creates_knowledge_file"
---
# US-03: Developer creates new knowledge file

**Need**: [Reference Format Standard](../README.md)

---

**As a** user writing or asking the AI to write a new knowledge file,
**I want** a clear, documented reference format with copy-pasteable examples,
**So that** every reference in the file is consistent with all other knowledge files and can be validated automatically.

### What Happens

1. User creates a new knowledge file (or tells the AI to create one)
2. User or AI consults the documented reference format for the correct syntax
3. References are written using the standard format with copy-pasteable examples as a guide
4. The new file's references pass automated validation on the first try

### Acceptance Criteria

- Reference format is documented with copy-pasteable examples
- Format covers all reference types (file path, section, cross-entity)
- New knowledge files using the format pass the validation script without errors
