# Form Filling Automation Workflow (Playwright MCP)

## Overview

This protocol defines standard procedures for automating form completion using Playwright MCP. Form automation includes filling text inputs, selecting options, checking boxes, and submitting forms.

## Prerequisites

1. Playwright MCP server must be running and accessible
2. User must provide the data to fill (AI should never generate sensitive data)
3. Forms requiring authentication may need user to log in first

## Security Considerations

**IMPORTANT**: AI assistants should:
- Never enter sensitive financial data (credit cards, bank accounts)
- Never enter identity documents (SSN, passport numbers)
- Always confirm before submitting forms
- Never auto-fill forms opened from untrusted links

---

## Workflow 1: Basic Text Form Filling

### Use Case
Fill a simple contact form or registration form with text inputs.

### Steps

1. **Navigate to form page:**
   ```
   mcp__playwright__browser_navigate(url="https://example.com/contact")
   ```

2. **Get page snapshot to identify form fields:**
   ```
   mcp__playwright__browser_snapshot()
   ```

3. **Identify form field references:**
   From the snapshot, note the `ref` values for each input field.

4. **Fill each text field:**
   ```
   mcp__playwright__browser_type(
     element="Name input field",
     ref="ref_1",
     text="John Doe"
   )

   mcp__playwright__browser_type(
     element="Email input field",
     ref="ref_2",
     text="john@example.com"
   )

   mcp__playwright__browser_type(
     element="Message textarea",
     ref="ref_3",
     text="Hello, this is my message."
   )
   ```

5. **Verify filled values:**
   ```
   mcp__playwright__browser_snapshot()
   ```

6. **Submit form (with user confirmation):**
   ```
   mcp__playwright__browser_click(element="Submit button", ref="ref_submit")
   ```

---

## Workflow 2: Multi-Field Form (Using fill_form)

### Use Case
Fill multiple form fields efficiently in a single operation.

### Steps

1. **Navigate and get snapshot:**
   ```
   mcp__playwright__browser_navigate(url="https://example.com/register")
   mcp__playwright__browser_snapshot()
   ```

2. **Fill multiple fields at once:**
   ```
   mcp__playwright__browser_fill_form(
     fields=[
       {"name": "First Name", "type": "textbox", "ref": "ref_1", "value": "John"},
       {"name": "Last Name", "type": "textbox", "ref": "ref_2", "value": "Doe"},
       {"name": "Email", "type": "textbox", "ref": "ref_3", "value": "john@example.com"},
       {"name": "Phone", "type": "textbox", "ref": "ref_4", "value": "555-1234"}
     ]
   )
   ```

3. **Verify and submit:**
   ```
   mcp__playwright__browser_snapshot()
   # Confirm with user before submitting
   mcp__playwright__browser_click(element="Submit button", ref="ref_submit")
   ```

---

## Workflow 3: Dropdown Selection

### Use Case
Select options from dropdown menus (country, state, category, etc.).

### Steps

1. **Get snapshot to identify dropdown:**
   ```
   mcp__playwright__browser_snapshot()
   ```

2. **Select dropdown option:**
   ```
   mcp__playwright__browser_select_option(
     element="Country dropdown",
     ref="ref_country",
     values=["United States"]
   )
   ```

3. **For multi-select dropdowns:**
   ```
   mcp__playwright__browser_select_option(
     element="Interests multi-select",
     ref="ref_interests",
     values=["Technology", "Science", "Art"]
   )
   ```

4. **Alternative: Click-based selection**
   If standard select doesn't work (custom dropdowns):
   ```
   # Open dropdown
   mcp__playwright__browser_click(element="Country dropdown trigger", ref="ref_dropdown")
   mcp__playwright__browser_wait_for(time=0.5)

   # Click option
   mcp__playwright__browser_click(element="United States option", ref="ref_us_option")
   ```

---

## Workflow 4: Checkbox and Radio Button Handling

### Use Case
Toggle checkboxes and select radio button options.

### Steps

1. **Get snapshot to identify checkboxes/radios:**
   ```
   mcp__playwright__browser_snapshot()
   ```

2. **Check a checkbox:**
   ```
   mcp__playwright__browser_fill_form(
     fields=[
       {"name": "Terms checkbox", "type": "checkbox", "ref": "ref_terms", "value": "true"}
     ]
   )
   ```

3. **Select a radio option:**
   ```
   mcp__playwright__browser_fill_form(
     fields=[
       {"name": "Payment method", "type": "radio", "ref": "ref_credit_card", "value": "credit_card"}
     ]
   )
   ```

4. **Alternative: Click to toggle:**
   ```
   mcp__playwright__browser_click(element="Newsletter subscription checkbox", ref="ref_newsletter")
   ```

---

## Workflow 5: Date and Time Inputs

### Use Case
Fill date pickers, time selectors, and datetime fields.

### Steps

1. **For standard HTML date inputs:**
   ```
   mcp__playwright__browser_type(
     element="Birth date input",
     ref="ref_date",
     text="1990-01-15"
   )
   ```

2. **For custom date pickers:**
   ```
   # Open date picker
   mcp__playwright__browser_click(element="Date picker trigger", ref="ref_datepicker")
   mcp__playwright__browser_wait_for(time=0.5)

   # Navigate to correct month/year if needed
   mcp__playwright__browser_click(element="Previous month", ref="ref_prev_month")

   # Select day
   mcp__playwright__browser_click(element="Day 15", ref="ref_day_15")
   ```

3. **For time inputs:**
   ```
   mcp__playwright__browser_type(
     element="Appointment time",
     ref="ref_time",
     text="14:30"
   )
   ```

---

## Workflow 6: File Upload Fields

### Use Case
Upload files through file input fields.

### Steps

1. **Identify file input:**
   ```
   mcp__playwright__browser_snapshot()
   ```

2. **Upload file:**
   ```
   mcp__playwright__browser_file_upload(
     paths=["/path/to/document.pdf"]
   )
   ```

3. **For multiple files:**
   ```
   mcp__playwright__browser_file_upload(
     paths=[
       "/path/to/document1.pdf",
       "/path/to/document2.pdf"
     ]
   )
   ```

**Note**: File uploads require explicit user permission.

---

## Workflow 7: Multi-Step Forms (Wizards)

### Use Case
Complete forms that span multiple pages or steps.

### Steps

1. **Complete Step 1:**
   ```
   mcp__playwright__browser_navigate(url="https://example.com/wizard")
   mcp__playwright__browser_snapshot()

   # Fill step 1 fields
   mcp__playwright__browser_type(element="Name", ref="ref_1", text="John Doe")

   # Click Next
   mcp__playwright__browser_click(element="Next button", ref="ref_next")
   ```

2. **Wait for Step 2:**
   ```
   mcp__playwright__browser_wait_for(time=1)
   mcp__playwright__browser_snapshot()
   ```

3. **Complete Step 2:**
   ```
   # Fill step 2 fields
   mcp__playwright__browser_type(element="Address", ref="ref_2", text="123 Main St")

   # Click Next
   mcp__playwright__browser_click(element="Next button", ref="ref_next")
   ```

4. **Continue until final step:**
   ```
   # Review and submit
   mcp__playwright__browser_snapshot()
   # Confirm with user
   mcp__playwright__browser_click(element="Submit", ref="ref_submit")
   ```

---

## Workflow 8: Form Validation Handling

### Use Case
Handle validation errors and correct form entries.

### Steps

1. **Submit form:**
   ```
   mcp__playwright__browser_click(element="Submit", ref="ref_submit")
   ```

2. **Check for validation errors:**
   ```
   mcp__playwright__browser_snapshot()
   # Look for error messages in snapshot
   ```

3. **Correct invalid fields:**
   ```
   # Clear and re-enter field
   mcp__playwright__browser_click(element="Email field", ref="ref_email")
   mcp__playwright__browser_press_key(key="Control+a")
   mcp__playwright__browser_type(
     element="Email field",
     ref="ref_email",
     text="valid@email.com"
   )
   ```

4. **Re-submit:**
   ```
   mcp__playwright__browser_click(element="Submit", ref="ref_submit")
   ```

---

## Field Type Reference

| Field Type | Tool | Example |
|------------|------|---------|
| Text input | `browser_type` | Name, email, address |
| Password | `browser_type` | Password fields (user should enter) |
| Textarea | `browser_type` | Comments, descriptions |
| Select (dropdown) | `browser_select_option` | Country, category |
| Checkbox | `browser_fill_form` | Terms acceptance |
| Radio button | `browser_fill_form` | Payment method |
| Date | `browser_type` | Date of birth |
| Time | `browser_type` | Appointment time |
| File | `browser_file_upload` | Document upload |
| Slider | `browser_fill_form` | Price range |

---

## Best Practices

1. **Always get snapshot first**: Identify field references before filling
2. **Verify after filling**: Take snapshot to confirm values entered correctly
3. **Handle dynamic forms**: Some fields appear after others are filled
4. **Wait for validation**: Allow time for client-side validation to run
5. **Confirm before submit**: Always ask user before clicking submit/purchase buttons
6. **Handle CAPTCHA**: Inform user when CAPTCHA is present (cannot be automated)
7. **Save progress**: For long forms, verify each section before proceeding

---

## Error Handling

### Field Not Found
```
# Re-get snapshot
mcp__playwright__browser_snapshot()

# Try scrolling to field
mcp__playwright__browser_evaluate(
  function="() => document.querySelector('[name=\"fieldname\"]').scrollIntoView()"
)
```

### Value Not Accepted
```
# Clear field first
mcp__playwright__browser_click(element="Field", ref="ref_1")
mcp__playwright__browser_press_key(key="Control+a")
mcp__playwright__browser_press_key(key="Backspace")

# Re-enter value
mcp__playwright__browser_type(element="Field", ref="ref_1", text="new value")
```

### Form Timeout
```
# Check if page reloaded
mcp__playwright__browser_snapshot()

# May need to re-navigate
mcp__playwright__browser_navigate(url="https://example.com/form")
```

---

## Example: Complete Registration Form

```
# 1. Navigate to registration page
mcp__playwright__browser_navigate(url="https://example.com/register")

# 2. Get form structure
mcp__playwright__browser_snapshot()

# 3. Fill all fields
mcp__playwright__browser_fill_form(
  fields=[
    {"name": "First Name", "type": "textbox", "ref": "ref_fname", "value": "John"},
    {"name": "Last Name", "type": "textbox", "ref": "ref_lname", "value": "Doe"},
    {"name": "Email", "type": "textbox", "ref": "ref_email", "value": "john@example.com"},
    {"name": "Terms", "type": "checkbox", "ref": "ref_terms", "value": "true"}
  ]
)

# 4. Select country
mcp__playwright__browser_select_option(
  element="Country",
  ref="ref_country",
  values=["United States"]
)

# 5. Verify all fields
mcp__playwright__browser_snapshot()

# 6. Confirm with user: "Ready to submit registration form?"

# 7. Submit (after user confirmation)
mcp__playwright__browser_click(element="Register button", ref="ref_submit")

# 8. Verify success
mcp__playwright__browser_wait_for(text="Registration successful")
mcp__playwright__browser_snapshot()
```

---

**Last Updated**: 2026-01-13
**Applies To**: Playwright MCP Server for Claude Code CLI
