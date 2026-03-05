---
resource_id: "a5c5ad32-96db-42be-827e-ff9f6ac4ef03"
resource_type: "document"
resource_name: "screenshot_capture_workflow"
---
# Screenshot Capture Workflow (Playwright MCP)

## Overview

This protocol defines standard procedures for capturing screenshots using Playwright MCP. Screenshots are useful for documentation, visual verification, debugging, and analyzing page layouts.

## Prerequisites

1. Playwright MCP server must be running and accessible
2. Page must be loaded before taking screenshots
3. For headed mode, ensure DISPLAY environment is set

---

## Workflow 1: Basic Viewport Screenshot

### Use Case
Capture the currently visible portion of the page.

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

### Output
- PNG image of current viewport
- Default filename: `page-{timestamp}.png`

---

## Workflow 2: Full Page Screenshot

### Use Case
Capture the entire scrollable page, not just the visible viewport.

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

### Notes
- Full page screenshots can be very tall
- May take longer for pages with many images
- Cannot be combined with element screenshots

---

## Workflow 3: Element-Specific Screenshot

### Use Case
Capture a specific element (form, chart, component) rather than full page.

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

### Best Practices
- Ensure element is visible (scroll into view if needed)
- Wait for dynamic content within element to load
- Use descriptive element names for clarity

---

## Workflow 4: Screenshot with Specific Dimensions

### Use Case
Capture screenshot at specific viewport dimensions (responsive testing).

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

## Workflow 5: Screenshot for Visual Comparison

### Use Case
Capture screenshots for before/after comparison or regression testing.

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

### Comparison Notes
- Use consistent viewport sizes for comparisons
- Ensure same wait times for dynamic content
- Consider caching/CDN differences between captures

---

## Workflow 6: Screenshot with Hidden Elements

### Use Case
Hide certain elements (modals, overlays, ads) before capturing.

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

## Workflow 7: Screenshot of Dynamic Content

### Use Case
Capture content that loads dynamically (charts, animations, lazy-loaded images).

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

## Workflow 8: Screenshot Series (Documentation)

### Use Case
Capture a series of screenshots documenting a workflow.

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

### Naming Convention
- Use consistent prefix: `{workflow}-{step}-{description}.png`
- Examples: `signup-01-form.png`, `signup-02-filled.png`, `signup-03-submitted.png`

---

## Workflow 9: JPEG Screenshots (Smaller Files)

### Use Case
Capture screenshots in JPEG format for smaller file sizes.

### Steps

1. **Capture JPEG screenshot:**
   ```
   mcp__playwright__browser_take_screenshot(
     type="jpeg",
     filename="page.jpeg"
   )
   ```

### When to Use JPEG
- Large screenshots where file size matters
- Photographic content (not UI/text heavy)
- When slight quality loss is acceptable

### When to Use PNG (Default)
- UI screenshots with text
- Screenshots requiring transparency
- Visual regression testing (pixel-perfect needed)

---

## Image Format Reference

| Format | Best For | Quality | File Size |
|--------|----------|---------|-----------|
| PNG (default) | UI, text, sharp edges | Lossless | Larger |
| JPEG | Photos, gradients | Lossy | Smaller |

---

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

## Error Handling

### Blank Screenshots
**Cause**: Page not fully loaded or headless rendering issue.
**Solution**:
```
mcp__playwright__browser_wait_for(time=3)
mcp__playwright__browser_snapshot()  # Verify content
mcp__playwright__browser_take_screenshot()
```

### Element Not Found
**Cause**: Invalid element reference.
**Solution**:
```
mcp__playwright__browser_snapshot()  # Get updated refs
# Use correct ref from snapshot
```

### Screenshot Too Large
**Cause**: Full page on very long page.
**Solution**: Capture viewport only or specific element.

---

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

## Output File Locations

Screenshots are typically saved to the current working directory or a configured output path. Check your MCP configuration for custom output directories.

Default naming: `page-{timestamp}.png`
Custom naming: Use `filename` parameter

---

**Last Updated**: 2026-01-13
**Applies To**: Playwright MCP Server for Claude Code CLI
