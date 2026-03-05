---
resource_id: "c369fa43-98ca-481f-9490-b0b4a7e86c53"
resource_type: "document"
resource_name: "form_filling_workflow"
---
# Form Filling Automation Workflow (Playwright MCP)

<!-- section_id: "94432df3-2ef2-4aa8-8199-a5b06e5d111d" -->
## Overview

This protocol defines standard procedures for automating form completion using Playwright MCP. Form automation includes filling text inputs, selecting options, checking boxes, and submitting forms.

<!-- section_id: "0bd7923f-9be1-4f31-bd6c-58ef77594d7e" -->
## Prerequisites

1. Playwright MCP server must be running and accessible
2. User must provide the data to fill (AI should never generate sensitive data)
3. Forms requiring authentication may need user to log in first

<!-- section_id: "9d3c173a-e94c-457e-a92b-b385c883a8ab" -->
## Security Considerations

**IMPORTANT**: AI assistants should:
- Never enter sensitive financial data (credit cards, bank accounts)
- Never enter identity documents (SSN, passport numbers)
- Always confirm before submitting forms
- Never auto-fill forms opened from untrusted links

---

<!-- section_id: "a466e8d6-ebbd-4613-b2c8-5a71a77b2f26" -->
## Workflow 1: Basic Text Form Filling

<!-- section_id: "073a615d-a108-4bb5-86e2-321dfbd2dc30" -->
### Use Case
Fill a simple contact form or registration form with text inputs.

<!-- section_id: "4512251d-eb83-4d8c-81c5-09dfbdac0c13" -->
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

<!-- section_id: "ec7d2d0c-13f4-4339-b351-a0d2212597aa" -->
## Workflow 2: Multi-Field Form (Using fill_form)

<!-- section_id: "b4b905bf-848e-4e3a-9e41-e6065cc14635" -->
### Use Case
Fill multiple form fields efficiently in a single operation.

<!-- section_id: "78622518-7888-49c9-bf5c-711dee0a80c1" -->
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

<!-- section_id: "b0690dff-b36d-4cac-97ae-5a7ddf3ce03f" -->
## Workflow 3: Dropdown Selection

<!-- section_id: "816cb32e-2444-4296-aba9-66b1ce734033" -->
### Use Case
Select options from dropdown menus (country, state, category, etc.).

<!-- section_id: "776c9594-a420-4f00-826a-8d28b8728d42" -->
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

<!-- section_id: "4325bfc5-6e0a-4b8e-8c22-a8a61e290f2c" -->
## Workflow 4: Checkbox and Radio Button Handling

<!-- section_id: "e7952d2d-ff2c-4985-bbde-22281149319d" -->
### Use Case
Toggle checkboxes and select radio button options.

<!-- section_id: "a2921707-b86f-4fb5-9086-3ff7bf494e53" -->
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

<!-- section_id: "0729ad07-ff11-4dc7-84ff-f9925a497009" -->
## Workflow 5: Date and Time Inputs

<!-- section_id: "d9373c46-566f-46d9-af59-0bc5c44d32fb" -->
### Use Case
Fill date pickers, time selectors, and datetime fields.

<!-- section_id: "3dbf097e-dbb8-4348-a81e-d7f323e8b527" -->
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

<!-- section_id: "ac387f73-8505-4e5a-b11f-4c39c4e4afc7" -->
## Workflow 6: File Upload Fields

<!-- section_id: "c2109d72-1b6f-4f87-b64a-882a5e49d93f" -->
### Use Case
Upload files through file input fields.

<!-- section_id: "706d8200-6d28-44f9-b7a4-3aa9bbcdbe7f" -->
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

<!-- section_id: "e1275460-74c2-4fb0-a17e-c5e5e3d1f1be" -->
## Workflow 7: Multi-Step Forms (Wizards)

<!-- section_id: "41434bec-8065-4e8a-bb6f-dee07f9c9e4c" -->
### Use Case
Complete forms that span multiple pages or steps.

<!-- section_id: "2b83f93e-ee1e-4dc1-8836-5e161f29f374" -->
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

<!-- section_id: "5adb5181-a43e-465f-abdd-da6670ddde58" -->
## Workflow 8: Form Validation Handling

<!-- section_id: "99677f83-d1a9-49c0-8c5b-0e512fa6c7de" -->
### Use Case
Handle validation errors and correct form entries.

<!-- section_id: "8e3c5b77-3959-4d67-8e50-2306f9eba8cf" -->
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

<!-- section_id: "aa21a2d2-9ced-4c5f-b9ff-8e7fccb71449" -->
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

<!-- section_id: "5a986dcf-ec15-440b-952b-2719999e964c" -->
## Best Practices

1. **Always get snapshot first**: Identify field references before filling
2. **Verify after filling**: Take snapshot to confirm values entered correctly
3. **Handle dynamic forms**: Some fields appear after others are filled
4. **Wait for validation**: Allow time for client-side validation to run
5. **Confirm before submit**: Always ask user before clicking submit/purchase buttons
6. **Handle CAPTCHA**: Inform user when CAPTCHA is present (cannot be automated)
7. **Save progress**: For long forms, verify each section before proceeding

---

<!-- section_id: "6b5c38ea-e9e7-4c79-9296-611489558c49" -->
## Error Handling

<!-- section_id: "dfa87399-dac0-4d9d-b54a-737aed44a4f3" -->
### Field Not Found
```
# Re-get snapshot
mcp__playwright__browser_snapshot()

# Try scrolling to field
mcp__playwright__browser_evaluate(
  function="() => document.querySelector('[name=\"fieldname\"]').scrollIntoView()"
)
```

<!-- section_id: "701a3a3f-0796-48ae-a082-1202541f6619" -->
### Value Not Accepted
```
# Clear field first
mcp__playwright__browser_click(element="Field", ref="ref_1")
mcp__playwright__browser_press_key(key="Control+a")
mcp__playwright__browser_press_key(key="Backspace")

# Re-enter value
mcp__playwright__browser_type(element="Field", ref="ref_1", text="new value")
```

<!-- section_id: "453e5765-0082-40a6-9f1d-a591c447ce49" -->
### Form Timeout
```
# Check if page reloaded
mcp__playwright__browser_snapshot()

# May need to re-navigate
mcp__playwright__browser_navigate(url="https://example.com/form")
```

---

<!-- section_id: "7215917e-e30c-4d93-af16-3df0a28ca4fe" -->
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
