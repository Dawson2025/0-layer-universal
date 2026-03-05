---
resource_id: "ddf2668b-44a1-486f-ac10-395eb677aebc"
resource_type: "output"
resource_name: "US-03_ci_catches_chain_breakage"
---
# US-03: CI/hook catches chain breakage on commit

**Need**: [Chain Validation Enhancement](../README.md)

---

**As a** user who commits structural changes (moving files, renaming entities),
**I want** chain validation to run automatically as a git hook or CI check,
**So that** broken references are caught at commit time, not discovered later when the AI fails.

### What Happens

1. User makes structural changes (moves files, renames directories, updates references)
2. User commits the changes
3. Git hook or CI pipeline triggers chain validation automatically
4. If any references are broken, the commit is flagged (or blocked) with a clear error message
5. User fixes the broken references before the changes reach the main branch

### Acceptance Criteria

- Chain validation runs automatically on structural changes (git hook or CI)
- Broken references block or flag the commit with actionable error messages
- Validation completes fast enough to not disrupt the commit workflow
