---
resource_id: "a5c5ad32-96db-42be-827e-ff9f6ac4ef03"
resource_type: "document"
resource_name: "screenshot_capture_workflow"
---
# Screenshot Capture Workflow (Playwright MCP)

<!-- section_id: "cd702237-44b1-4fbe-93dc-50c2c06bcb76" -->
## Overview

This protocol defines standard procedures for capturing screenshots using Playwright MCP. Screenshots are useful for documentation, visual verification, debugging, and analyzing page layouts.

<!-- section_id: "2e0045f6-9b84-4141-a286-750375e635dd" -->
## Prerequisites

1. Playwright MCP server must be running and accessible
2. Page must be loaded before taking screenshots
3. For headed mode, ensure DISPLAY environment is set

---

<!-- section_id: "c42a2068-54b1-4081-8f17-bed92b95f0a9" -->
## Workflow 1: Basic Viewport Screenshot

<!-- section_id: "ddf36ba4-7493-4624-955b-cb25ba97f1b9" -->
### Use Case
Capture the currently visible portion of the page.

<!-- section_id: "d73d4ceb-bb88-4735-aa04-d154af4e7d9b" -->
### Steps

1. **Navigate to page:**
   ```
   mcp__playwright__browser_navigate(url="https://example.com")
   ```

2. **Wait for page to fully load:**
   ```
   mcp__playwright__browser_wait_for(time=2)
   ```

3. **Capture viewport screenshot:**
   ```
   mcp__playwright__browser_take_screenshot()
   ```

4. **With custom filename:**
   ```
   mcp__playwright__browser_take_screenshot(filename="homepage.png")
   ```

<!-- section_id: "1af4dba3-b015-4b79-b8e6-f13c0ea01d74" -->
### Output
- PNG image of current viewport
- Default filename: `page-{timestamp}.png`

---

<!-- section_id: "24a538c8-36b8-454a-9fea-5159e1b9dd9a" -->
## Workflow 2: Full Page Screenshot

<!-- section_id: "e1ce9d33-bdf4-4378-9ba0-176df8a00874" -->
### Use Case
Capture the entire scrollable page, not just the visible viewport.

<!-- section_id: "ee521313-f849-492e-8f52-371c6f11bac6" -->
### Steps

1. **Navigate and wait:**
   ```
   mcp__playwright__browser_navigate(url="https://example.com/long-article")
   mcp__playwright__browser_wait_for(time=2)
   ```

2. **Capture full page:**
   ```
   mcp__playwright__browser_take_screenshot(fullPage=true, filename="full-article.png")
   ```

<!-- section_id: "3ebc99e6-d3e5-40ae-9c9a-72e35a98e4b3" -->
### Notes
- Full page screenshots can be very tall
- May take longer for pages with many images
- Cannot be combined with element screenshots

---

<!-- section_id: "9a1769f6-bebf-4666-8c23-d67b54adfa75" -->
## Workflow 3: Element-Specific Screenshot

<!-- section_id: "f7eaaceb-5440-4ef9-abd2-5feb7a6fafe0" -->
### Use Case
Capture a specific element (form, chart, component) rather than full page.

<!-- section_id: "ba6836b2-51fc-4b76-b2a7-0e648b3fb159" -->
### Steps

1. **Navigate and get snapshot:**
   ```
   mcp__playwright__browser_navigate(url="https://example.com/dashboard")
   mcp__playwright__browser_snapshot()
   ```

2. **Identify target element reference:**
   From snapshot, find the `ref` for the desired element.

3. **Capture element screenshot:**
   ```
   mcp__playwright__browser_take_screenshot(
     element="Dashboard chart widget",
     ref="ref_chart",
     filename="chart.png"
   )
   ```

<!-- section_id: "a96fc2bb-5460-4b17-9113-6a865393bd5a" -->
### Best Practices
- Ensure element is visible (scroll into view if needed)
- Wait for dynamic content within element to load
- Use descriptive element names for clarity

---

<!-- section_id: "02c8a0a7-1f29-412c-93c6-65c3250ef538" -->
## Workflow 4: Screenshot with Specific Dimensions

<!-- section_id: "1a5db947-1bc4-423e-a1b7-2780b04200dc" -->
### Use Case
Capture screenshot at specific viewport dimensions (responsive testing).

<!-- section_id: "f3babd6e-02e8-4888-be22-f3a481295f65" -->
### Steps

1. **Resize browser window:**
   ```
   mcp__playwright__browser_resize(width=375, height=812)
   ```

2. **Navigate to page:**
   ```
   mcp__playwright__browser_navigate(url="https://example.com")
   mcp__playwright__browser_wait_for(time=2)
   ```

3. **Capture mobile view:**
   ```
   mcp__playwright__browser_take_screenshot(filename="mobile-view.png")
   ```

4. **Capture tablet view:**
   ```
   mcp__playwright__browser_resize(width=768, height=1024)
   mcp__playwright__browser_wait_for(time=1)
   mcp__playwright__browser_take_screenshot(filename="tablet-view.png")
   ```

5. **Capture desktop view:**
   ```
   mcp__playwright__browser_resize(width=1920, height=1080)
   mcp__playwright__browser_wait_for(time=1)
   mcp__playwright__browser_take_screenshot(filename="desktop-view.png")
   ```

<!-- section_id: "9690237a-83ea-4dab-8d03-7387e8bb0430" -->
### Common Device Dimensions

| Device | Width | Height |
|--------|-------|--------|
| iPhone SE | 375 | 667 |
| iPhone 12/13 | 390 | 844 |
| iPhone 14 Pro Max | 430 | 932 |
| iPad | 768 | 1024 |
| iPad Pro | 1024 | 1366 |
| Laptop | 1366 | 768 |
| Desktop | 1920 | 1080 |
| 4K Monitor | 3840 | 2160 |

---

<!-- section_id: "af6a36b7-f219-4f71-89b1-1e3f7b0b520e" -->
## Workflow 5: Screenshot for Visual Comparison

<!-- section_id: "366cf122-844b-4399-8bee-c571af3d8b08" -->
### Use Case
Capture screenshots for before/after comparison or regression testing.

<!-- section_id: "74009006-c137-4690-8cbe-f2db90b0f213" -->
### Steps

1. **Capture "before" state:**
   ```
   mcp__playwright__browser_navigate(url="https://example.com/page")
   mcp__playwright__browser_wait_for(time=2)
   mcp__playwright__browser_take_screenshot(filename="page-before.png")
   ```

2. **Perform action that changes page:**
   ```
   mcp__playwright__browser_click(element="Toggle theme", ref="ref_theme")
   mcp__playwright__browser_wait_for(time=1)
   ```

3. **Capture "after" state:**
   ```
   mcp__playwright__browser_take_screenshot(filename="page-after.png")
   ```

<!-- section_id: "dfa465ab-0d92-4685-a3ff-f2b7cd000e74" -->
### Comparison Notes
- Use consistent viewport sizes for comparisons
- Ensure same wait times for dynamic content
- Consider caching/CDN differences between captures

---

<!-- section_id: "27290166-8623-4702-a3fa-dc93071a62f0" -->
## Workflow 6: Screenshot with Hidden Elements

<!-- section_id: "b89b6eeb-4176-479f-bd1f-1256ea6dd867" -->
### Use Case
Hide certain elements (modals, overlays, ads) before capturing.

<!-- section_id: "e72be305-5c01-4868-9cfd-97a599a10ece" -->
### Steps

1. **Navigate to page:**
   ```
   mcp__playwright__browser_navigate(url="https://example.com")
   ```

2. **Hide unwanted elements via JavaScript:**
   ```
   mcp__playwright__browser_evaluate(
     function="() => {
       // Hide cookie banner
       const banner = document.querySelector('.cookie-banner');
       if (banner) banner.style.display = 'none';

       // Hide chat widget
       const chat = document.querySelector('.chat-widget');
       if (chat) chat.style.display = 'none';

       // Hide floating elements
       document.querySelectorAll('.floating, .popup').forEach(el => el.style.display = 'none');
     }"
   )
   ```

3. **Wait briefly for reflow:**
   ```
   mcp__playwright__browser_wait_for(time=0.5)
   ```

4. **Capture clean screenshot:**
   ```
   mcp__playwright__browser_take_screenshot(filename="clean-page.png")
   ```

---

<!-- section_id: "f3587e5d-96d7-4964-9052-852abe5e7b96" -->
## Workflow 7: Screenshot of Dynamic Content

<!-- section_id: "83be266e-31ce-456e-8b6a-2ca3a7a603fb" -->
### Use Case
Capture content that loads dynamically (charts, animations, lazy-loaded images).

<!-- section_id: "8ec59967-39aa-4861-b6d7-cae5b841834c" -->
### Steps

1. **Navigate to page:**
   ```
   mcp__playwright__browser_navigate(url="https://example.com/dashboard")
   ```

2. **Wait for specific content to appear:**
   ```
   mcp__playwright__browser_wait_for(text="Data loaded")
   ```

3. **Or wait for network idle:**
   ```
   mcp__playwright__browser_wait_for(time=5)
   ```

4. **For animations, wait for completion:**
   ```
   mcp__playwright__browser_evaluate(
     function="() => new Promise(resolve => setTimeout(resolve, 2000))"
   )
   ```

5. **Capture screenshot:**
   ```
   mcp__playwright__browser_take_screenshot(filename="dashboard-loaded.png")
   ```

---

<!-- section_id: "3596c605-4e27-44f9-94bb-c8b735fb73c3" -->
## Workflow 8: Screenshot Series (Documentation)

<!-- section_id: "f50e21eb-9a13-4308-902f-401c3f70fb7b" -->
### Use Case
Capture a series of screenshots documenting a workflow.

<!-- section_id: "2db47b6e-eddd-4005-a8a7-bdedc68fb89f" -->
### Steps

1. **Step 1 Screenshot:**
   ```
   mcp__playwright__browser_navigate(url="https://example.com/app")
   mcp__playwright__browser_wait_for(time=2)
   mcp__playwright__browser_take_screenshot(filename="step-01-landing.png")
   ```

2. **Step 2 Screenshot:**
   ```
   mcp__playwright__browser_click(element="Sign In", ref="ref_signin")
   mcp__playwright__browser_wait_for(time=1)
   mcp__playwright__browser_take_screenshot(filename="step-02-login-form.png")
   ```

3. **Step 3 Screenshot:**
   ```
   mcp__playwright__browser_type(element="Email", ref="ref_email", text="user@example.com")
   mcp__playwright__browser_take_screenshot(filename="step-03-email-entered.png")
   ```

4. **Continue for remaining steps...**

<!-- section_id: "68137d87-924e-46ec-8f28-c3c0ef6f7ab1" -->
### Naming Convention
- Use consistent prefix: `{workflow}-{step}-{description}.png`
- Examples: `signup-01-form.png`, `signup-02-filled.png`, `signup-03-submitted.png`

---

<!-- section_id: "41547b0d-77c1-426a-a2d3-90d0fd5cdb42" -->
## Workflow 9: JPEG Screenshots (Smaller Files)

<!-- section_id: "cecc3456-cf14-407b-85f2-03c611a00d9a" -->
### Use Case
Capture screenshots in JPEG format for smaller file sizes.

<!-- section_id: "b4cb763c-8616-47c7-b3cc-7ac663de4a20" -->
### Steps

1. **Capture JPEG screenshot:**
   ```
   mcp__playwright__browser_take_screenshot(
     type="jpeg",
     filename="page.jpeg"
   )
   ```

<!-- section_id: "7d1d61dc-796e-45f7-a346-78d7fb22ab62" -->
### When to Use JPEG
- Large screenshots where file size matters
- Photographic content (not UI/text heavy)
- When slight quality loss is acceptable

<!-- section_id: "d544be1b-82e3-4213-baae-0711ba56358e" -->
### When to Use PNG (Default)
- UI screenshots with text
- Screenshots requiring transparency
- Visual regression testing (pixel-perfect needed)

---

<!-- section_id: "081bdf55-fae2-40c3-a914-626990e26351" -->
## Image Format Reference

| Format | Best For | Quality | File Size |
|--------|----------|---------|-----------|
| PNG (default) | UI, text, sharp edges | Lossless | Larger |
| JPEG | Photos, gradients | Lossy | Smaller |

---

<!-- section_id: "fb76f113-548e-48d3-94fb-271b05b12e12" -->
## Screenshot Quality Tips

1. **Wait for complete load:**
   ```
   mcp__playwright__browser_wait_for(time=2)
   ```

2. **Ensure consistent viewport:**
   ```
   mcp__playwright__browser_resize(width=1920, height=1080)
   ```

3. **Hide scrollbars (optional):**
   ```
   mcp__playwright__browser_evaluate(
     function="() => document.documentElement.style.overflow = 'hidden'"
   )
   ```

4. **Disable animations:**
   ```
   mcp__playwright__browser_evaluate(
     function="() => {
       const style = document.createElement('style');
       style.textContent = '*, *::before, *::after { animation-duration: 0s !important; transition-duration: 0s !important; }';
       document.head.appendChild(style);
     }"
   )
   ```

---

<!-- section_id: "596e7966-d9bb-49bf-825a-1929722045f5" -->
## Error Handling

<!-- section_id: "1c774c45-232b-487b-82cf-6be28f3271ea" -->
### Blank Screenshots
**Cause**: Page not fully loaded or headless rendering issue.
**Solution**:
```
mcp__playwright__browser_wait_for(time=3)
mcp__playwright__browser_snapshot()  # Verify content
mcp__playwright__browser_take_screenshot()
```

<!-- section_id: "4503fab2-9892-41af-910f-d8f2337dafe0" -->
### Element Not Found
**Cause**: Invalid element reference.
**Solution**:
```
mcp__playwright__browser_snapshot()  # Get updated refs
# Use correct ref from snapshot
```

<!-- section_id: "65564387-2468-43cd-864e-aa5211a62d6c" -->
### Screenshot Too Large
**Cause**: Full page on very long page.
**Solution**: Capture viewport only or specific element.

---

<!-- section_id: "7240ed4a-f1ac-4f0d-be78-375251d1506d" -->
## Example: Complete Screenshot Documentation

```
# 1. Set up consistent viewport
mcp__playwright__browser_resize(width=1280, height=800)

# 2. Navigate to application
mcp__playwright__browser_navigate(url="https://app.example.com")
mcp__playwright__browser_wait_for(time=2)

# 3. Hide distracting elements
mcp__playwright__browser_evaluate(
  function="() => {
    document.querySelectorAll('.toast, .banner, .chat-widget').forEach(el => el.remove());
  }"
)

# 4. Capture landing page
mcp__playwright__browser_take_screenshot(filename="01-landing.png")

# 5. Click feature button
mcp__playwright__browser_click(element="Features button", ref="ref_features")
mcp__playwright__browser_wait_for(time=1)

# 6. Capture features section
mcp__playwright__browser_take_screenshot(filename="02-features.png")

# 7. Take full page for reference
mcp__playwright__browser_take_screenshot(fullPage=true, filename="full-page.png")

# 8. Capture specific component
mcp__playwright__browser_take_screenshot(
  element="Pricing table",
  ref="ref_pricing",
  filename="pricing-table.png"
)

# 9. Clean up
mcp__playwright__browser_close()
```

---

<!-- section_id: "bcd245fb-af57-4194-9d00-be636c2d16fe" -->
## Output File Locations

Screenshots are typically saved to the current working directory or a configured output path. Check your MCP configuration for custom output directories.

Default naming: `page-{timestamp}.png`
Custom naming: Use `filename` parameter

---

**Last Updated**: 2026-01-13
**Applies To**: Playwright MCP Server for Claude Code CLI
