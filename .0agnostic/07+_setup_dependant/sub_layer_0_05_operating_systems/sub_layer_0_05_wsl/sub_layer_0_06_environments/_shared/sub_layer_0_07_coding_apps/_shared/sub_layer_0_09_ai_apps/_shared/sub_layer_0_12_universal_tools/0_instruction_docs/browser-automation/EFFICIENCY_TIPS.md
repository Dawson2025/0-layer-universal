---
resource_id: "08738ec0-bdca-4147-bbbc-38f486388e1b"
resource_type: "document"
resource_name: "EFFICIENCY_TIPS"
---
# Browser Automation Efficiency Tips
*Learned Patterns and Best Practices for Efficient Browser Automation*

**Version**: 1.0  
**Last Updated**: 2025-01-27  
**Scope**: Universal (applies to all browser automation projects)

---

<!-- section_id: "088108e6-cba9-4839-8477-2ab2ce8a8da0" -->
## Overview

This document captures efficiency tips, learned patterns, and best practices discovered during browser automation work. These patterns are broadly applicable across different projects and automation tools.

---

<!-- section_id: "73a78268-84e6-4d8f-a188-5b9999e6588f" -->
## Element Reference Management

<!-- section_id: "a7446d29-de24-4c51-9a2f-96b5126e423b" -->
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

<!-- section_id: "ba1339c4-90fe-474d-877e-3fb9b83bd10e" -->
## Negative Number Input in Equation Editors

<!-- section_id: "1fbac293-0aa7-468c-8a00-cc47da98baeb" -->
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

<!-- section_id: "ba2279d4-b284-4405-9ad6-559b9bd2e1d5" -->
## Dialog State Management

<!-- section_id: "b83532dc-5ef7-4519-9f33-b05725029a12" -->
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

<!-- section_id: "c8517c83-b2a6-4c0e-910c-f0c468b53d27" -->
## Concurrent Work Strategy

<!-- section_id: "1a12afe2-cd4e-491f-8924-fa7eaeefa3f1" -->
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

<!-- section_id: "7ec06861-64f1-40b9-87c8-ce16a205befa" -->
## Session Management

<!-- section_id: "e7a151bd-42c3-48f8-9399-95ba93dd5f3f" -->
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

<!-- section_id: "d74bcd2a-e6b7-4fa5-8bbd-62ab37f567f1" -->
## Input Field Navigation

<!-- section_id: "41db45fb-89d5-41ee-b33e-f9516745d0aa" -->
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

<!-- section_id: "e168776e-9935-4260-b2b8-7ca6d30e312d" -->
## Error Recovery Patterns

<!-- section_id: "52aba210-6ecb-4199-a5ba-096cf6e4a0e4" -->
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

<!-- section_id: "d3308bdd-0a8f-4a46-bc00-e5b44c39546a" -->
## Tab Management

<!-- section_id: "38e595f9-793b-4936-96a6-53fffd1693c1" -->
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

<!-- section_id: "48501a5f-378b-4546-9315-247d542ae964" -->
## Performance Optimization

<!-- section_id: "cc933580-85b8-4046-9f50-fb5ae532866b" -->
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

<!-- section_id: "835a7c5b-924a-4a1f-b3e3-b8faaf842bc3" -->
## Integration

- **Browser Management Policy**: See `browser_management_policy.md`
- **Browser Opening Rule**: See `browser_opening_rule.md`
- **Browser Automation Framework**: See `README.md` in this directory

---

**Status**: Active  
**Last Updated**: 2025-01-27  
**Purpose**: Capture learned patterns for efficient browser automation across all projects

