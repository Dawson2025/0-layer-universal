---
resource_id: "26b32a27-dd68-4c58-b7ca-1e8caa287b7a"
resource_type: "document"
resource_name: "EFFICIENCY_TIPS"
---
# Browser Automation Efficiency Tips
*Learned Patterns and Best Practices for Efficient Browser Automation*

**Version**: 1.0  
**Last Updated**: 2025-01-27  
**Scope**: Universal (applies to all browser automation projects)

---

<!-- section_id: "b6ec47f5-d6be-4252-a461-fd4de1910252" -->
## Overview

This document captures efficiency tips, learned patterns, and best practices discovered during browser automation work. These patterns are broadly applicable across different projects and automation tools.

---

<!-- section_id: "c8a17aff-a926-4120-b656-e67916ea36f8" -->
## Element Reference Management

<!-- section_id: "f9a21430-a51e-49dd-b49f-2b2b132057f9" -->
### Problem: Stale Element References

**Issue**: Element references become invalid after:
- Page updates or DOM changes
- Dialog state changes (open/close)
- Dynamic content loading
- Tab switches

**Solution Pattern**:
```javascript
// ❌ BAD: Reusing stale references
await browser_click({ element: "button", ref: "e123" });
await browser_type({ element: "input", ref: "e456", text: "value" }); // May fail!

// ✅ GOOD: Fresh snapshot after state changes
await browser_click({ element: "button", ref: "e123" });
await browser_snapshot(); // Get fresh state
await browser_type({ element: "input", ref: "e789", text: "value" }); // Uses new ref
```

**When to Take Fresh Snapshots**:
- After opening/closing dialogs
- After page navigation
- After tab switches
- After any DOM-modifying action
- When element interactions fail unexpectedly

**Best Practice**: Take a snapshot before interacting with any element that might have changed state.

---

<!-- section_id: "7fb38af5-2b08-44b8-a5fe-1cea4835d12a" -->
## Negative Number Input in Equation Editors

<!-- section_id: "52c6629a-b682-49a1-beaf-feb5cc016671" -->
### Problem: Subtraction vs. Negative Number

**Issue**: Many equation editors (e.g., ALEKS, math input fields) interpret "-" as subtraction when there's existing content in the field.

**Example Problem**:
- Field contains "0"
- Typing "-2" results in "0 - 2" (subtraction) instead of "-2" (negative number)

**Solution Pattern**:
```javascript
// ❌ BAD: Typing negative number after existing content
await browser_type({ element: "input", ref: "e123", text: "0" });
await browser_press_key({ key: "ArrowRight" });
await browser_type({ element: "input", ref: "e123", text: "-2" }); // Results in "0 - 2"

// ✅ GOOD: Type negative sign first in empty field
await browser_type({ element: "input", ref: "e123", text: "0" });
await browser_press_key({ key: "ArrowRight" });
await browser_type({ element: "input", ref: "e123", text: "-" }); // Type "-" first
await browser_type({ element: "input", ref: "e123", text: "2" }); // Then number
```

**Workflow for Negative Numbers**:
1. Ensure field is completely empty (or clear it first)
2. Type "-" first (creates negative number context)
3. Then type the number

**When to Reset**:
- If you see "0 - 2" instead of "-2" in the field
- Close and reopen the dialog/form to get fresh state
- Use "Start over" or "Clear" button if available

---

<!-- section_id: "6ebcc698-311f-45f5-a5d6-42ef3413a25e" -->
## Dialog State Management

<!-- section_id: "d324056a-51d8-47d0-9a7f-f8879538df07" -->
### Pattern: Dialog Persistence

**Observation**: Some dialogs remain open between operations (e.g., point plotting dialogs that allow multiple entries).

**Efficient Workflow**:
```javascript
// ✅ GOOD: Keep dialog open for multiple operations
await browser_click({ element: "Plot point button", ref: "e123" });
// Dialog opens
await browser_snapshot(); // Get fresh refs
await browser_type({ element: "input", ref: "e456", text: "0" });
// ... enter first point ...
await browser_click({ element: "Submit button", ref: "e789" });
// Dialog stays open for next point
await browser_snapshot(); // Get fresh refs again
await browser_type({ element: "input", ref: "e101", text: "1" });
// ... enter second point ...
await browser_click({ element: "Close button", ref: "e112" });
// Now close dialog
```

**Key Points**:
- Don't close dialog between related operations
- Take fresh snapshot after each operation (refs may change)
- Only close dialog when all operations complete

---

<!-- section_id: "2dd43502-01a2-4387-9a31-ae7ca59e05a8" -->
## Concurrent Work Strategy

<!-- section_id: "b4bec6b3-a5f1-4a4d-a6dd-a7253cc7327f" -->
### Pattern: Working on Multiple Assignments

**Strategy**: When working on multiple related tasks (e.g., multiple prerequisites), work concurrently and switch when blocked.

**Workflow**:
1. Identify all related tasks/assignments
2. Open separate tabs for each
3. Work on one until blocked
4. Switch to another when blocked
5. Continue alternating

**Blocking Conditions**:
- Visual interpretation required (graphs, diagrams)
- User assistance needed for complex interactions
- Automation limitations reached
- Session expiration

**Benefits**:
- Maximizes progress across all tasks
- Reduces idle time when blocked
- Better overall completion rate

---

<!-- section_id: "03ba8c5c-5780-4b0f-9739-333f269e29d5" -->
## Session Management

<!-- section_id: "05c6b4d8-1b8e-4bae-91cd-82b1dbdb825f" -->
### Pattern: Session Expiration Handling

**Issue**: Web application sessions can expire, causing automation to fail.

**Symptoms**:
- "Session Closed" dialogs
- Authentication errors
- Element not found errors after period of inactivity

**Solution Pattern**:
```javascript
// Check for session expiration
const snapshot = await browser_snapshot();
if (snapshot.includes("Session Closed") || snapshot.includes("Session expired")) {
    // Navigate to active tab
    const tabs = await browser_tabs({ action: "list" });
    const activeTab = tabs.find(tab => tab.url.includes("application-url"));
    await browser_tabs({ action: "select", index: activeTab.index });
    
    // Resume session
    await browser_click({ element: "Start button", ref: "e123" });
    await browser_snapshot(); // Verify session resumed
}
```

**Prevention**:
- Keep browser open across sessions (per browser management policy)
- Check tab state before interactions
- Monitor for session expiration indicators

---

<!-- section_id: "1a603365-254f-44e5-8cd4-14b42e10b907" -->
## Input Field Navigation

<!-- section_id: "38487ffd-e420-4fe7-ad70-933b1aba8dc2" -->
### Pattern: Keyboard Navigation in Multi-Field Forms

**Issue**: Some forms require keyboard navigation between fields rather than direct clicking.

**Solution Pattern**:
```javascript
// ✅ GOOD: Use ArrowRight/ArrowLeft for field navigation
await browser_type({ element: "input", ref: "e123", text: "value1" });
await browser_press_key({ key: "ArrowRight" }); // Move to next field
await browser_type({ element: "input", ref: "e123", text: "value2" }); // Types in new field

// ❌ BAD: Trying to click next field (may not work in equation editors)
await browser_type({ element: "input", ref: "e123", text: "value1" });
await browser_click({ element: "next input", ref: "e456" }); // May not work
```

**When to Use**:
- Equation editor fields (x, y coordinates)
- Multi-part input fields
- Fields that don't respond to direct clicks

---

<!-- section_id: "d853b2af-4de4-4389-b39a-1bdd1d4ffb8a" -->
## Error Recovery Patterns

<!-- section_id: "e628559d-40ba-4bd7-9753-0e7e3b2b2e0a" -->
### Pattern: Dialog Reset on Input Errors

**Issue**: When input errors occur (e.g., "Fill in all empty boxes"), the dialog state may be corrupted.

**Solution Pattern**:
```javascript
// If error occurs, reset dialog state
try {
    await browser_click({ element: "Submit button", ref: "e123" });
} catch (error) {
    if (error.message.includes("Fill in all") || error.message.includes("empty boxes")) {
        // Close dialog to reset state
        await browser_click({ element: "Close button", ref: "e124" });
        await browser_snapshot(); // Fresh state
        // Reopen and try again
        await browser_click({ element: "Open dialog button", ref: "e125" });
        await browser_snapshot(); // Fresh refs
        // Retry with correct input
    }
}
```

**Key Points**:
- Close dialog on input errors
- Reopen to get fresh state
- Take fresh snapshot after reopen
- Retry with corrected input

---

<!-- section_id: "8077ce77-b55f-4b37-81c8-84b4ac8b6c47" -->
## Tab Management

<!-- section_id: "6896a53e-6cd9-4605-9348-791b50eeb05b" -->
### Pattern: Tab State Verification

**Issue**: Working in wrong tab or tab state not as expected.

**Solution Pattern**:
```javascript
// Always verify tab state before operations
const tabs = await browser_tabs({ action: "list" });
const targetTab = tabs.find(tab => 
    tab.url.includes("target-url") || 
    tab.title.includes("Target Title")
);

if (!targetTab) {
    // Navigate to correct URL or open new tab
    await browser_navigate({ url: "target-url" });
} else {
    // Switch to target tab
    await browser_tabs({ action: "select", index: targetTab.index });
    await browser_snapshot(); // Verify correct page
}
```

**Best Practice**: Always verify tab state before starting work, especially after session breaks.

---

<!-- section_id: "ade9e09b-7ca8-4a30-b1fb-e257674de16e" -->
## Performance Optimization

<!-- section_id: "c0a5db73-5b57-42a0-991a-8ca151fee604" -->
### Pattern: Batch Operations

**Observation**: Some operations can be batched for efficiency.

**Example**: Plotting multiple points
```javascript
// ✅ GOOD: Batch point plotting (keep dialog open)
for (const point of points) {
    await browser_type({ element: "input", ref: currentRef, text: point.x });
    await browser_press_key({ key: "ArrowRight" });
    await browser_type({ element: "input", ref: currentRef, text: point.y });
    await browser_click({ element: "Plot button", ref: plotRef });
    // Dialog stays open - no need to reopen
    await browser_snapshot(); // Get fresh refs for next iteration
}
```

**Benefits**:
- Reduces dialog open/close overhead
- Faster overall execution
- Less state management complexity

---

<!-- section_id: "189ae99d-4706-45e8-acb5-2eea9c6c7af7" -->
## Integration

- **Browser Management Policy**: See `browser_management_policy.md`
- **Browser Opening Rule**: See `browser_opening_rule.md`
- **Browser Automation Framework**: See `README.md` in this directory

---

**Status**: Active  
**Last Updated**: 2025-01-27  
**Purpose**: Capture learned patterns for efficient browser automation across all projects

