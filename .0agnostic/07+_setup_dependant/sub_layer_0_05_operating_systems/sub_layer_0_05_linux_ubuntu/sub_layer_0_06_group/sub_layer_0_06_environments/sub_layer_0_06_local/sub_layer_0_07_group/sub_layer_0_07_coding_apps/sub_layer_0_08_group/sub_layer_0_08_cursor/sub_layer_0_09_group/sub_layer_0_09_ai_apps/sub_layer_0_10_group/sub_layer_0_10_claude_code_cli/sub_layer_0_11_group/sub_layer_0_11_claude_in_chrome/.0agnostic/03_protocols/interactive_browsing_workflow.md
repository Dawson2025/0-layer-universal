---
resource_id: "097062ba-9f3a-4e1a-a15f-07f608bdda24"
resource_type: "protocol"
resource_name: "interactive_browsing_workflow"
---
# Interactive Browsing Workflow

<!-- section_id: "8e5622a8-5580-49e1-a6a7-6b9d2e5f1a28" -->
## Overview

This workflow describes the standardized process for interactive browser automation using the Claude in Chrome MCP server. Interactive browsing involves navigating websites, clicking elements, filling forms, and performing complex multi-step browser interactions.

<!-- section_id: "41cb4b42-614d-4961-8815-9d8264ac7d38" -->
## Use Cases

- Form submission and data entry
- Multi-step navigation flows
- User interface testing
- Web application interaction
- Account management tasks
- Data entry automation

<!-- section_id: "e64c1c80-9863-4826-ab94-9fe7f783c189" -->
## Safety Guidelines

Before performing interactive actions, be aware of these safety requirements:

1. **User Approval Required** for:
   - Making purchases or financial transactions
   - Submitting forms with personal data
   - Sending messages (email, chat, social media)
   - Accepting terms and agreements
   - Publishing content publicly
   - Clicking irreversible action buttons

2. **Prohibited Actions**:
   - Entering banking or credit card information
   - Modifying security permissions
   - Creating accounts on user's behalf
   - Permanent deletions

3. **Always Verify**:
   - Current page state before actions
   - Element targets before clicking
   - Form data before submission

<!-- section_id: "a857cc70-4839-4d90-9647-36af14ab092c" -->
## Workflow Steps

<!-- section_id: "6b25616e-97cc-4a01-8f9b-a27410ecd6d7" -->
### Step 1: Initialize Session

Establish the browser session and tab context.

```python
# Get or create tab context
result = mcp__claude-in-chrome__tabs_context_mcp(createIfEmpty=True)
TAB_ID = result.tabs[0].id  # Extract tab ID

# Create a new tab if needed
new_tab = mcp__claude-in-chrome__tabs_create_mcp()
```

<!-- section_id: "7794f1f3-8551-480e-b1db-1c8539ad0700" -->
### Step 2: Navigate to Target

Navigate to the starting point of the interaction.

```python
# Navigate to URL
mcp__claude-in-chrome__navigate(
    url="https://example.com",
    tabId=TAB_ID
)

# Wait for page load
mcp__claude-in-chrome__computer(
    action="wait",
    duration=2,
    tabId=TAB_ID
)
```

**Navigation Options**:
```python
# Go back in history
navigate(url="back", tabId=TAB_ID)

# Go forward in history
navigate(url="forward", tabId=TAB_ID)
```

<!-- section_id: "8648875a-ac01-411a-a6b5-96d9a41d659c" -->
### Step 3: Analyze Page State

Before interacting, understand the current page state.

```python
# Take screenshot for visual context
mcp__claude-in-chrome__computer(
    action="screenshot",
    tabId=TAB_ID
)

# Get interactive elements
mcp__claude-in-chrome__read_page(
    tabId=TAB_ID,
    filter="interactive"
)

# Find specific target elements
mcp__claude-in-chrome__find(
    query="login form",
    tabId=TAB_ID
)
```

<!-- section_id: "bee489a3-2834-4ad2-95b2-f57acd1cd8d0" -->
### Step 4: Perform Interactions

Execute the required browser actions.

#### Click Actions

```python
# Click using element reference
mcp__claude-in-chrome__computer(
    action="left_click",
    ref="ref_1",
    tabId=TAB_ID
)

# Click using coordinates
mcp__claude-in-chrome__computer(
    action="left_click",
    coordinate=[500, 300],
    tabId=TAB_ID
)

# Double click
mcp__claude-in-chrome__computer(
    action="double_click",
    ref="ref_1",
    tabId=TAB_ID
)

# Right click (context menu)
mcp__claude-in-chrome__computer(
    action="right_click",
    coordinate=[500, 300],
    tabId=TAB_ID
)

# Click with modifier keys
mcp__claude-in-chrome__computer(
    action="left_click",
    ref="ref_1",
    modifiers="ctrl",  # ctrl, shift, alt, cmd, or combinations like "ctrl+shift"
    tabId=TAB_ID
)
```

#### Form Input

```python
# Using form_input tool (preferred for form fields)
mcp__claude-in-chrome__form_input(
    ref="ref_2",
    value="user@example.com",
    tabId=TAB_ID
)

# Using type action for text input
mcp__claude-in-chrome__computer(
    action="type",
    text="Hello, World!",
    tabId=TAB_ID
)
```

#### Keyboard Actions

```python
# Press single key
mcp__claude-in-chrome__computer(
    action="key",
    text="Enter",
    tabId=TAB_ID
)

# Press multiple keys
mcp__claude-in-chrome__computer(
    action="key",
    text="Backspace Backspace Delete",  # Space-separated
    tabId=TAB_ID
)

# Keyboard shortcuts
mcp__claude-in-chrome__computer(
    action="key",
    text="ctrl+a",  # Select all (use "cmd+a" on Mac)
    tabId=TAB_ID
)

# Repeat key presses
mcp__claude-in-chrome__computer(
    action="key",
    text="ArrowDown",
    repeat=5,
    tabId=TAB_ID
)
```

#### Scrolling

```python
# Scroll down
mcp__claude-in-chrome__computer(
    action="scroll",
    scroll_direction="down",
    scroll_amount=3,  # Number of scroll ticks
    coordinate=[500, 400],  # Where to scroll
    tabId=TAB_ID
)

# Scroll element into view
mcp__claude-in-chrome__computer(
    action="scroll_to",
    ref="ref_10",
    tabId=TAB_ID
)
```

#### Hover Actions

```python
# Hover to reveal dropdown or tooltip
mcp__claude-in-chrome__computer(
    action="hover",
    ref="ref_3",
    tabId=TAB_ID
)

# Hover at coordinates
mcp__claude-in-chrome__computer(
    action="hover",
    coordinate=[300, 200],
    tabId=TAB_ID
)
```

#### Drag and Drop

```python
# Drag from one point to another
mcp__claude-in-chrome__computer(
    action="left_click_drag",
    start_coordinate=[100, 200],
    coordinate=[400, 200],  # End position
    tabId=TAB_ID
)
```

<!-- section_id: "6215ad18-3841-4646-a85c-4e62a9f059e7" -->
### Step 5: Verify Actions

After each significant action, verify the result.

```python
# Screenshot after action
mcp__claude-in-chrome__computer(
    action="screenshot",
    tabId=TAB_ID
)

# Wait for page update
mcp__claude-in-chrome__computer(
    action="wait",
    duration=1,
    tabId=TAB_ID
)

# Re-read page state
mcp__claude-in-chrome__read_page(
    tabId=TAB_ID,
    filter="interactive"
)
```

<!-- section_id: "56c7d1a5-fbbe-4089-a9e5-6dc7c074ac17" -->
### Step 6: Handle Dynamic Content

For pages with dynamic content, use appropriate waiting strategies.

```python
# Wait fixed time
mcp__claude-in-chrome__computer(
    action="wait",
    duration=3,
    tabId=TAB_ID
)

# Check for element existence
result = mcp__claude-in-chrome__find(
    query="success message",
    tabId=TAB_ID
)
# If not found, wait and retry
```

<!-- section_id: "383e3000-e588-43f2-9d8c-3c8031b77262" -->
## Interaction Patterns

<!-- section_id: "87d5c26a-b3da-4d27-a843-d06b7570ffc4" -->
### Pattern 1: Login Flow

```python
# 1. Navigate to login page
navigate(url="https://example.com/login", tabId=TAB_ID)
computer(action="wait", duration=2, tabId=TAB_ID)

# 2. Find form fields
find(query="username or email input", tabId=TAB_ID)
find(query="password input", tabId=TAB_ID)

# 3. Fill credentials (get user approval first!)
# NOTE: Ask user before entering credentials
form_input(ref="ref_1", value="user@example.com", tabId=TAB_ID)
form_input(ref="ref_2", value="********", tabId=TAB_ID)  # User enters password

# 4. Submit form (get user approval!)
find(query="login button", tabId=TAB_ID)
computer(action="left_click", ref="ref_3", tabId=TAB_ID)

# 5. Verify success
computer(action="wait", duration=3, tabId=TAB_ID)
computer(action="screenshot", tabId=TAB_ID)
```

<!-- section_id: "b854401a-4b92-44c4-a267-3872d49800ee" -->
### Pattern 2: Form Filling

```python
# 1. Analyze form structure
read_page(tabId=TAB_ID, filter="interactive")

# 2. Fill text fields
form_input(ref="ref_1", value="John Doe", tabId=TAB_ID)  # Name
form_input(ref="ref_2", value="john@example.com", tabId=TAB_ID)  # Email

# 3. Select dropdown option
find(query="country dropdown", tabId=TAB_ID)
computer(action="left_click", ref="ref_3", tabId=TAB_ID)
find(query="United States option", tabId=TAB_ID)
computer(action="left_click", ref="ref_4", tabId=TAB_ID)

# 4. Check checkboxes
find(query="agree to terms checkbox", tabId=TAB_ID)
form_input(ref="ref_5", value=True, tabId=TAB_ID)

# 5. Submit (get approval first!)
find(query="submit button", tabId=TAB_ID)
# Ask user: "Ready to submit the form. Proceed?"
computer(action="left_click", ref="ref_6", tabId=TAB_ID)
```

<!-- section_id: "925f75ff-da50-4f5b-bd22-488d43ba103d" -->
### Pattern 3: Multi-Page Navigation

```python
# 1. Start on homepage
navigate(url="https://example.com", tabId=TAB_ID)

# 2. Click navigation link
find(query="Products link", tabId=TAB_ID)
computer(action="left_click", ref="ref_1", tabId=TAB_ID)
computer(action="wait", duration=2, tabId=TAB_ID)

# 3. Click product
find(query="first product item", tabId=TAB_ID)
computer(action="left_click", ref="ref_2", tabId=TAB_ID)
computer(action="wait", duration=2, tabId=TAB_ID)

# 4. Add to cart
find(query="add to cart button", tabId=TAB_ID)
computer(action="left_click", ref="ref_3", tabId=TAB_ID)

# 5. Verify cart update
find(query="cart icon with count", tabId=TAB_ID)
computer(action="screenshot", tabId=TAB_ID)
```

<!-- section_id: "ce958431-49c5-4d39-831b-e9c9228d570e" -->
### Pattern 4: Table Interaction

```python
# 1. Find table
find(query="data table", tabId=TAB_ID)

# 2. Scroll to load more rows (if lazy-loaded)
for i in range(3):
    computer(action="scroll", scroll_direction="down", scroll_amount=5,
             coordinate=[500, 400], tabId=TAB_ID)
    computer(action="wait", duration=1, tabId=TAB_ID)

# 3. Click specific row
find(query="row containing 'Order #12345'", tabId=TAB_ID)
computer(action="left_click", ref="ref_5", tabId=TAB_ID)

# 4. Interact with row actions
find(query="view details button", tabId=TAB_ID)
computer(action="left_click", ref="ref_6", tabId=TAB_ID)
```

<!-- section_id: "12f5f63d-572c-40f2-a9e8-be7b3ee992e0" -->
### Pattern 5: Modal/Dialog Handling

```python
# 1. Trigger modal
find(query="open settings button", tabId=TAB_ID)
computer(action="left_click", ref="ref_1", tabId=TAB_ID)
computer(action="wait", duration=1, tabId=TAB_ID)

# 2. Interact with modal content
find(query="modal dialog", tabId=TAB_ID)
read_page(tabId=TAB_ID, ref_id="ref_2")  # Read only modal content

# 3. Fill modal form
find(query="input in modal", tabId=TAB_ID)
form_input(ref="ref_3", value="new value", tabId=TAB_ID)

# 4. Close modal
find(query="save button in modal", tabId=TAB_ID)
computer(action="left_click", ref="ref_4", tabId=TAB_ID)

# Or dismiss with Escape
computer(action="key", text="Escape", tabId=TAB_ID)
```

<!-- section_id: "47057dec-5773-407d-bed7-d1611db851ca" -->
## GIF Recording for Documentation

Record browser sessions for documentation or debugging.

```python
# 1. Start recording
mcp__claude-in-chrome__gif_creator(
    action="start_recording",
    tabId=TAB_ID
)

# 2. Take initial screenshot
computer(action="screenshot", tabId=TAB_ID)

# 3. Perform interactions...
# [your automation steps here]

# 4. Take final screenshot
computer(action="screenshot", tabId=TAB_ID)

# 5. Stop recording
mcp__claude-in-chrome__gif_creator(
    action="stop_recording",
    tabId=TAB_ID
)

# 6. Export GIF
mcp__claude-in-chrome__gif_creator(
    action="export",
    download=True,
    filename="my-recording.gif",
    options={
        "showClickIndicators": True,
        "showActionLabels": True,
        "showProgressBar": True
    },
    tabId=TAB_ID
)
```

<!-- section_id: "7550d68d-ecae-4a87-83ac-47734a47c53f" -->
## Window Management

```python
# Resize window for specific viewport
mcp__claude-in-chrome__resize_window(
    width=1920,
    height=1080,
    tabId=TAB_ID
)

# Common viewport sizes
# Mobile: 375 x 667
# Tablet: 768 x 1024
# Desktop: 1920 x 1080
# HD: 1280 x 720
```

<!-- section_id: "c6d14d71-9eff-4a6b-a9c1-9dfbd050e989" -->
## Error Handling

<!-- section_id: "abc649fa-95ff-4d2a-b01e-ebc265e689ee" -->
### Element Not Found
```python
result = find(query="button that may not exist", tabId=TAB_ID)
if not result.elements:
    # Element not found - try alternative approach
    # Or scroll to reveal hidden elements
    computer(action="scroll", scroll_direction="down",
             scroll_amount=3, coordinate=[500, 400], tabId=TAB_ID)
```

<!-- section_id: "09901722-190f-470d-be17-c5c662d44137" -->
### Click Misses Target
```python
# Use element reference instead of coordinates when possible
# References are more reliable than coordinates

# If coordinate-based click fails, use zoom to verify position
computer(action="zoom", region=[400, 200, 600, 400], tabId=TAB_ID)
```

<!-- section_id: "7ec4f8d2-a3bb-406e-8d3a-97d1743b9d64" -->
### Page Not Responding
```python
# Refresh the page
navigate(url="https://current-url.com", tabId=TAB_ID)  # Reload

# Or use JavaScript
javascript_tool(
    action="javascript_exec",
    text="location.reload()",
    tabId=TAB_ID
)
```

<!-- section_id: "5d4200a1-b914-47ab-96b4-559f94b9c51d" -->
### Stale Element Reference
```python
# Re-read page to get fresh references
read_page(tabId=TAB_ID, filter="interactive")
# Then re-find the element
find(query="target element", tabId=TAB_ID)
```

<!-- section_id: "12efd70d-c15b-4860-b7f1-079efaffc0fc" -->
## Best Practices

1. **Always screenshot before complex interactions** - Provides context and documentation
2. **Use element references over coordinates** - More reliable across different screen sizes
3. **Add waits after navigation** - Pages need time to load
4. **Verify state after actions** - Confirm the action had the expected effect
5. **Get user approval before irreversible actions** - Submissions, purchases, deletions
6. **Handle errors gracefully** - Elements may not exist or be interactable
7. **Use find for dynamic content** - Natural language queries adapt to page changes
8. **Test in headed mode first** - Visual feedback helps debug issues
9. **Keep tab IDs fresh** - Call tabs_context_mcp if unsure of validity
10. **Document the flow** - Use GIF recording for complex workflows

---

**Related Workflows**:
- [Page Analysis Workflow](./page_analysis_workflow.md)
- [Content Extraction Workflow](./content_extraction_workflow.md)

**Last Updated**: 2026-01-13
