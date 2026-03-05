---
resource_id: "840b9e98-c2e0-41d4-975d-23b722a0d858"
resource_type: "rule"
resource_name: "browser_management_policy"
---
# Browser Management Policy for AI Automation

## Overview

This document establishes the default behavior for browser automation tasks performed by AI assistants working inside this universal context system (applies to every project unless a project-level override explicitly states otherwise).

## Default Behavior: Keep Browsers Open and Persistent

**CRITICAL RULE**: When AI automates browser tasks, browser instances MUST remain open after completion.

**PERSISTENT SESSION RULE**: Browser sessions MUST persist across chat sessions. Never stop, delete, or close the browser instance unless explicitly requested by the user. The browser should remain running continuously so it can be reused across multiple AI sessions.

### Scope
- Applies to all browser automation: Chromium, Playwright, Chrome DevTools
- Browsers should stay open for user review and verification
- Only close browsers if explicitly requested by user

### Implementation
- General automation: Launch with `&` (background), leave running
- Use separate user data directories for multiple instances
- Preserve browser state for ongoing work

## Exception: Testing

**Testing Environment**: When running automated tests, browser instances SHOULD close after tests complete.

### Rationale
- Keeps the testing environment clean
- Prevents resource accumulation during test runs
- Maintains isolation between test sessions

### Implementation
- Test scripts should include `driver.quit()` or equivalent cleanup
- Use explicit close/quit commands in test cleanup
- Ensure proper resource management

## Commands Reference

### General Automation
```bash
# Launch browser and keep open
chromium --user-data-dir="/tmp/chromium-instance1" file.html &

# Multiple instances
chromium --user-data-dir="/tmp/chromium-instance2" &
```

### Testing (with cleanup)
```python
# Include in test scripts
driver.quit()  # Close browser after tests
```

## Policy Enforcement

- ✅ Do NOT close any browser instances during task execution
- ✅ Do NOT close any browser instances after task completion  
- ✅ Do NOT close browser instances at the end of a chat session
- ✅ PERSIST browser sessions across multiple AI chat sessions
- ✅ Leave all browser windows open for user review and verification
- ✅ This is the DEFAULT BEHAVIOR for all future browser automation tasks
- ✅ EXCEPTION: Close browsers after automated testing is complete
- ✅ Only close browsers if explicitly requested by user

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

## Examples

### Correct Usage
- Opening templates for review → Keep browser open
- Canvas authentication → Keep browser open  
- Data extraction → Keep browser open
- Screenshot capture → Keep browser open

### Testing Exception
- Unit tests → Close browser after completion
- Integration tests → Close browser after completion
- Performance tests → Close browser after completion

---

*This policy ensures optimal workflow for AI-assisted browser automation while maintaining clean testing environments.*
