---
resource_id: "09bd240c-3a4d-4914-ab4c-cdf32f4d7200"
resource_type: "document"
resource_name: "browser_management_policy"
---
# Browser Management Policy for AI Automation

<!-- section_id: "4493f341-749c-4113-9ac2-3f030b1d5a56" -->
## Overview

This document establishes the default behavior for browser automation tasks performed by AI assistants working inside this universal context system (applies to every project unless a project-level override explicitly states otherwise).

<!-- section_id: "48ca94c7-16cd-4ded-9b95-239c150ee095" -->
## Default Behavior: Keep Browsers Open

**CRITICAL RULE**: When AI automates browser tasks, browser instances MUST remain open after completion.

<!-- section_id: "187e3d14-65af-4d1e-a536-4ab28dab2793" -->
### Scope
- Applies to all browser automation: Chromium, Playwright, Chrome DevTools
- Browsers should stay open for user review and verification
- Only close browsers if explicitly requested by user

<!-- section_id: "f2a7d868-80c4-45a7-ba87-b14bef82c48f" -->
### Implementation
- General automation: Launch with `&` (background), leave running
- Use separate user data directories for multiple instances
- Preserve browser state for ongoing work

<!-- section_id: "d9c576fd-e568-4ba9-bebf-16251f5d629f" -->
## Exception: Testing

**Testing Environment**: When running automated tests, browser instances SHOULD close after tests complete.

<!-- section_id: "221a778e-8998-42b0-9d65-b092f758d2c6" -->
### Rationale
- Keeps the testing environment clean
- Prevents resource accumulation during test runs
- Maintains isolation between test sessions

<!-- section_id: "fd0ff9ff-abf1-4579-acc0-b4941d7823b3" -->
### Implementation
- Test scripts should include `driver.quit()` or equivalent cleanup
- Use explicit close/quit commands in test cleanup
- Ensure proper resource management

<!-- section_id: "8bee5cc5-f8fb-4446-9cca-d4093c21441d" -->
## Commands Reference

<!-- section_id: "47cc8e59-f7e6-4940-9c4f-c6fbf79f72bf" -->
### General Automation
```bash
# Launch browser and keep open
chromium --user-data-dir="/tmp/chromium-instance1" file.html &

# Multiple instances
chromium --user-data-dir="/tmp/chromium-instance2" &
```

<!-- section_id: "3cf9516f-9c62-4dc0-9bc0-dcbce7a3cddf" -->
### Testing (with cleanup)
```python
# Include in test scripts
driver.quit()  # Close browser after tests
```

<!-- section_id: "47c89770-e2c5-4aaf-9976-190f4c724ff0" -->
## Policy Enforcement

- ✅ Do NOT close any Chromium instances during task execution
- ✅ Do NOT close any Chromium instances after task completion  
- ✅ Leave all browser windows open for user review and verification
- ✅ This is the DEFAULT BEHAVIOR for all future browser automation tasks
- ✅ EXCEPTION: Close browsers after automated testing is complete
- ✅ Only close browsers if explicitly requested by user

<!-- section_id: "443dc63f-b127-49ec-8495-b9c8e93db68b" -->
## Examples

<!-- section_id: "df49ef3a-79c0-4432-adb1-bb383c8ed577" -->
### Correct Usage
- Opening templates for review → Keep browser open
- Canvas authentication → Keep browser open  
- Data extraction → Keep browser open
- Screenshot capture → Keep browser open

<!-- section_id: "0d884fc2-da40-4f72-ba4a-c7f34a25e57b" -->
### Testing Exception
- Unit tests → Close browser after completion
- Integration tests → Close browser after completion
- Performance tests → Close browser after completion

---

*This policy ensures optimal workflow for AI-assisted browser automation while maintaining clean testing environments.*
