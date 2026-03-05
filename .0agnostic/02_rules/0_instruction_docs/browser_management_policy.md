---
resource_id: "840b9e98-c2e0-41d4-975d-23b722a0d858"
resource_type: "rule"
resource_name: "browser_management_policy"
---
# Browser Management Policy for AI Automation

<!-- section_id: "74054a27-10f6-4c37-bde5-707b33252414" -->
## Overview

This document establishes the default behavior for browser automation tasks performed by AI assistants working inside this universal context system (applies to every project unless a project-level override explicitly states otherwise).

<!-- section_id: "680ea8c0-1aa0-4a48-b3f9-a66d4892688d" -->
## Default Behavior: Keep Browsers Open and Persistent

**CRITICAL RULE**: When AI automates browser tasks, browser instances MUST remain open after completion.

**PERSISTENT SESSION RULE**: Browser sessions MUST persist across chat sessions. Never stop, delete, or close the browser instance unless explicitly requested by the user. The browser should remain running continuously so it can be reused across multiple AI sessions.

<!-- section_id: "22095f96-5e6e-449f-82f5-5b829fa0aa8f" -->
### Scope
- Applies to all browser automation: Chromium, Playwright, Chrome DevTools
- Browsers should stay open for user review and verification
- Only close browsers if explicitly requested by user

<!-- section_id: "2c8e3d78-9d16-43c1-b041-20ed06acbc59" -->
### Implementation
- General automation: Launch with `&` (background), leave running
- Use separate user data directories for multiple instances
- Preserve browser state for ongoing work

<!-- section_id: "9fa511a9-462b-4138-bea8-2e96de712b8d" -->
## Exception: Testing

**Testing Environment**: When running automated tests, browser instances SHOULD close after tests complete.

<!-- section_id: "c978f371-c7a6-4f89-a1ee-f228d1ee26db" -->
### Rationale
- Keeps the testing environment clean
- Prevents resource accumulation during test runs
- Maintains isolation between test sessions

<!-- section_id: "c8741b29-25f3-431c-aace-94ad6057efa9" -->
### Implementation
- Test scripts should include `driver.quit()` or equivalent cleanup
- Use explicit close/quit commands in test cleanup
- Ensure proper resource management

<!-- section_id: "b4a3c765-5488-44fc-9c98-882279b66e0b" -->
## Commands Reference

<!-- section_id: "93b13adf-69a5-4e88-8858-43f8ec4377d5" -->
### General Automation
```bash
# Launch browser and keep open
chromium --user-data-dir="/tmp/chromium-instance1" file.html &

# Multiple instances
chromium --user-data-dir="/tmp/chromium-instance2" &
```

<!-- section_id: "358f8133-1c45-4b3d-8b50-e91fc0e29d4c" -->
### Testing (with cleanup)
```python
# Include in test scripts
driver.quit()  # Close browser after tests
```

<!-- section_id: "8b6f2e15-c436-4cb0-8f4c-96f2ece25a70" -->
## Policy Enforcement

- ✅ Do NOT close any browser instances during task execution
- ✅ Do NOT close any browser instances after task completion  
- ✅ Do NOT close browser instances at the end of a chat session
- ✅ PERSIST browser sessions across multiple AI chat sessions
- ✅ Leave all browser windows open for user review and verification
- ✅ This is the DEFAULT BEHAVIOR for all future browser automation tasks
- ✅ EXCEPTION: Close browsers after automated testing is complete
- ✅ Only close browsers if explicitly requested by user

<!-- section_id: "4eabd6f2-db3f-48e6-a64b-744c73698ec4" -->
## Cross-Session Persistence

**Purpose**: Browser sessions should remain active and accessible across multiple AI chat sessions, allowing:
- Authenticated sessions to persist
- State to be maintained across conversations
- Efficient reuse of browser instances
- Continuous access to web applications

**Implementation**: 
- Use MCP browser servers that support persistent sessions
- Never call browser close/quit commands at session end
- Document the browser state for the next session
- Resume browser operations in new sessions without re-authentication

<!-- section_id: "5aaf1250-e7f1-48f2-af73-11fedd29719d" -->
## Examples

<!-- section_id: "1bd4a1b5-9f78-484f-a174-9b70687a1534" -->
### Correct Usage
- Opening templates for review → Keep browser open
- Canvas authentication → Keep browser open  
- Data extraction → Keep browser open
- Screenshot capture → Keep browser open

<!-- section_id: "8d7a2a62-1324-4e1a-a880-f1c65560d9fe" -->
### Testing Exception
- Unit tests → Close browser after completion
- Integration tests → Close browser after completion
- Performance tests → Close browser after completion

---

*This policy ensures optimal workflow for AI-assisted browser automation while maintaining clean testing environments.*
