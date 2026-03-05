---
resource_id: "43cde1a0-b186-40ba-8d5c-a75eb1f852e9"
resource_type: "document"
resource_name: "EFFICIENCY_TIPS"
---
# Browser Automation Efficiency Tips
*Learned Patterns and Best Practices for Efficient Browser Automation*

**Version**: 1.0  
**Last Updated**: 2025-01-27  
**Scope**: Universal (applies to all browser automation projects)

---

<!-- section_id: "67825142-c89f-48b3-ab84-f655f9076afb" -->
## Overview

This document captures efficiency tips, learned patterns, and best practices discovered during browser automation work. These patterns are broadly applicable across different projects and automation tools.

---

<!-- section_id: "14919de9-d5fa-4de6-8b88-fbfb4b82b4c6" -->
## Element Reference Management

<!-- section_id: "a0d2846f-bdaa-4adc-81af-375b165fa22d" -->
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

<!-- section_id: "4958baf4-4c96-459b-a889-9cc046e6e2d8" -->
## Negative Number Input in Equation Editors

<!-- section_id: "95bfd723-8285-4391-9926-1ef848dd2c78" -->
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

<!-- section_id: "931392ce-acac-4ce4-95b5-862df9667b9a" -->
## Dialog State Management

<!-- section_id: "17de78bf-bddd-4e8a-b932-5de7220cf361" -->
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

<!-- section_id: "deb7fac9-ae39-4386-a988-3283381b6aa7" -->
## Concurrent Work Strategy

<!-- section_id: "acc69201-9255-4f7c-a85e-0280389d648c" -->
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

<!-- section_id: "ff986f08-bc5a-4ec7-9be5-92f1bc7bcf32" -->
## Session Management

<!-- section_id: "c0687045-646d-48b7-ba84-6fcb801490c8" -->
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

<!-- section_id: "0eb56ac0-1c3a-4be7-9aae-fef5afe4b62c" -->
## Input Field Navigation

<!-- section_id: "4e105af5-cd8f-459a-944c-086c39b238f0" -->
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

<!-- section_id: "ba0762da-0dd7-4f97-9c0f-1d5c7abb5172" -->
## Error Recovery Patterns

<!-- section_id: "941ec4f5-27a5-4781-bfc6-8764394587a8" -->
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

<!-- section_id: "ad7f732d-e469-41fc-a5ec-a93066279d13" -->
## Tab Management

<!-- section_id: "5f809513-c096-4e6f-b79f-38090354310f" -->
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

<!-- section_id: "20201718-e386-4f62-adbc-b293ec8416c6" -->
## Performance Optimization

<!-- section_id: "4ca0e0d8-384c-4c83-bab5-e16cf6cd823d" -->
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

<!-- section_id: "e1ad05c1-2d02-45cc-a452-a09127af6227" -->
## Integration

- **Browser Management Policy**: See `browser_management_policy.md`
- **Browser Opening Rule**: See `browser_opening_rule.md`
- **Browser Automation Framework**: See `README.md` in this directory

---

**Status**: Active  
**Last Updated**: 2025-01-27  
**Purpose**: Capture learned patterns for efficient browser automation across all projects

