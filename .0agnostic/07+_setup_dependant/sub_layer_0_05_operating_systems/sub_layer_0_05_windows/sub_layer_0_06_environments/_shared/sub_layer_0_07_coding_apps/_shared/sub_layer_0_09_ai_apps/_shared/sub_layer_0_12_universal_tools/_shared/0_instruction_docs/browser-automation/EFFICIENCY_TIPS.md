---
resource_id: "fbb4a205-63c3-4032-8f78-9c6e9892d2ad"
resource_type: "document"
resource_name: "EFFICIENCY_TIPS"
---
# Browser Automation Efficiency Tips
*Learned Patterns and Best Practices for Efficient Browser Automation*

**Version**: 1.0  
**Last Updated**: 2025-01-27  
**Scope**: Universal (applies to all browser automation projects)

---

<!-- section_id: "ff8d7239-000b-47ae-9c5d-afc421f20998" -->
## Overview

This document captures efficiency tips, learned patterns, and best practices discovered during browser automation work. These patterns are broadly applicable across different projects and automation tools.

---

<!-- section_id: "b23d9cb4-9dc3-465f-84ca-42c1e5e0067a" -->
## Element Reference Management

<!-- section_id: "b9079d0a-9684-407b-b0a0-444e631e0d0c" -->
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

<!-- section_id: "f8f9b222-0fdf-4f30-8b1a-f208e61e5678" -->
## Negative Number Input in Equation Editors

<!-- section_id: "7ababec2-8512-4730-961c-2fcef60215a5" -->
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

<!-- section_id: "39d39271-d3c5-4024-955d-809a85b78810" -->
## Dialog State Management

<!-- section_id: "3bc83830-c63d-47a6-b06e-7e1d4825adda" -->
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

<!-- section_id: "a99df391-c221-49d1-b2f9-18bd243d3808" -->
## Concurrent Work Strategy

<!-- section_id: "83b25901-2ec9-4630-a74b-2e62dec5ddf2" -->
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

<!-- section_id: "eec834e3-a0b5-4d02-a878-86c2e9c4b9e9" -->
## Session Management

<!-- section_id: "cfc6ec29-4c5d-4b38-a3c4-eda394170c50" -->
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

<!-- section_id: "090934a0-789e-48ee-8e82-56dc551a5494" -->
## Input Field Navigation

<!-- section_id: "094232fa-fc96-42cf-9d20-7679fdb42ab4" -->
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

<!-- section_id: "9c881194-cd02-4b77-9967-311361506b2e" -->
## Error Recovery Patterns

<!-- section_id: "35d463d1-ec90-4473-9e5b-e6848eeb2a85" -->
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

<!-- section_id: "6f470213-5f69-47fe-b083-023690e6fc5b" -->
## Tab Management

<!-- section_id: "cd25a106-e2e3-405e-9a38-f741f201147d" -->
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

<!-- section_id: "ca4a258e-b9b3-453c-93eb-293a28ec5d21" -->
## Performance Optimization

<!-- section_id: "33f18037-093c-4778-a147-fbfc8d0b2cbe" -->
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

<!-- section_id: "a31918ac-8d4e-456c-acca-0908a74da585" -->
## Integration

- **Browser Management Policy**: See `browser_management_policy.md`
- **Browser Opening Rule**: See `browser_opening_rule.md`
- **Browser Automation Framework**: See `README.md` in this directory

---

**Status**: Active  
**Last Updated**: 2025-01-27  
**Purpose**: Capture learned patterns for efficient browser automation across all projects

