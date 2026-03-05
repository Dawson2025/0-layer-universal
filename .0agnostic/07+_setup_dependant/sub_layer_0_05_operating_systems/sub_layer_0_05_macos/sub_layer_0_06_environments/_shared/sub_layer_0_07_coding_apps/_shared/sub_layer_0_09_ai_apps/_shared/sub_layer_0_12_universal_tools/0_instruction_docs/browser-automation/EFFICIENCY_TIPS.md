---
resource_id: "4dfde0b1-ded8-4fd8-a0f6-3b07c6100ff2"
resource_type: "document"
resource_name: "EFFICIENCY_TIPS"
---
# Browser Automation Efficiency Tips
*Learned Patterns and Best Practices for Efficient Browser Automation*

**Version**: 1.0  
**Last Updated**: 2025-01-27  
**Scope**: Universal (applies to all browser automation projects)

---

<!-- section_id: "808d0dd5-d0eb-439a-9696-6ca4691c0ddd" -->
## Overview

This document captures efficiency tips, learned patterns, and best practices discovered during browser automation work. These patterns are broadly applicable across different projects and automation tools.

---

<!-- section_id: "aa9bc0ba-837c-458d-b72e-a531e6b77b19" -->
## Element Reference Management

<!-- section_id: "9054910f-22be-40f8-a2c6-e5a69bbb7a1f" -->
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

<!-- section_id: "47ad05da-e571-4cf5-8de5-b57a63aa4c42" -->
## Negative Number Input in Equation Editors

<!-- section_id: "e9aac8b7-aa48-4349-90af-51c5c2111b95" -->
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

<!-- section_id: "4d738033-d55e-45d0-9156-21b63d6f9a82" -->
## Dialog State Management

<!-- section_id: "f318e066-9971-4150-812d-26a74be2ac83" -->
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

<!-- section_id: "75c71c28-bf1b-41cc-8046-d2de7e6db124" -->
## Concurrent Work Strategy

<!-- section_id: "43b833ee-7732-46b0-bc69-c98ac1d81b28" -->
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

<!-- section_id: "94c4a0bd-a27a-4de6-bb35-226493e11225" -->
## Session Management

<!-- section_id: "a3ba60bd-8ae5-4d23-9d3d-4d6a9115e2cc" -->
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

<!-- section_id: "eda62731-0858-4a6b-9242-ac32f5dba6b4" -->
## Input Field Navigation

<!-- section_id: "be53ef69-a0a6-4171-8678-33d57c564c8b" -->
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

<!-- section_id: "00638a8d-7c93-4d03-a8c9-36fcec5bd438" -->
## Error Recovery Patterns

<!-- section_id: "4cc8f14c-91db-421e-89c3-48a2083d6360" -->
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

<!-- section_id: "933f6e76-541a-4092-8bbb-ec26eeb221dd" -->
## Tab Management

<!-- section_id: "8f729740-c72e-495d-9349-a77d723261a5" -->
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

<!-- section_id: "c332774d-0f53-47c4-8030-9f8d626e79e4" -->
## Performance Optimization

<!-- section_id: "f5ee413f-391d-4b43-a509-c43d1d441254" -->
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

<!-- section_id: "1bcbc7bb-551c-4a12-a062-e205e166a6d2" -->
## Integration

- **Browser Management Policy**: See `browser_management_policy.md`
- **Browser Opening Rule**: See `browser_opening_rule.md`
- **Browser Automation Framework**: See `README.md` in this directory

---

**Status**: Active  
**Last Updated**: 2025-01-27  
**Purpose**: Capture learned patterns for efficient browser automation across all projects

