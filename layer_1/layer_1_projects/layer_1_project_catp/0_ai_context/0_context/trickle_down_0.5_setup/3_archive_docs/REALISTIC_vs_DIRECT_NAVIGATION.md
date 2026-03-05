---
resource_id: "654707a9-0295-4f06-a4d1-56c2f0ff5da6"
resource_type: "document"
resource_name: "REALISTIC_vs_DIRECT_NAVIGATION"
---
# Realistic vs Direct Navigation Testing

<!-- section_id: "07d4e166-c5df-4779-8071-c4fdf5e3b9d1" -->
## Overview

This document explains the difference between the two navigation approaches in our automation tests and when to use each.

---

<!-- section_id: "796d1304-e199-4189-a49a-e648520c3a11" -->
## Comparison

<!-- section_id: "a2cb1b52-cee4-4a2e-8507-9ea09841d75a" -->
### Original Approach (Direct URL Navigation)

**File**: `scripts/mcp-projects-flow.mjs`

```javascript
// Jump directly to pages via URL
await callTool(client, 'browser_navigate', { url: `${BASE}/projects` });
await callTool(client, 'browser_navigate', { url: `${BASE}/projects/create` });
await callTool(client, 'browser_navigate', { url: `${BASE}/admin/templates` });
```

<!-- section_id: "a7c46fdb-6e05-4bc4-8fdf-b1f0dece4ccf" -->
### Realistic Approach (UI Navigation)

**Files**:
- `scripts/mcp-playwright-demo-realistic.mjs`
- `scripts/mcp-projects-flow-realistic.mjs`

```javascript
// Navigate by clicking buttons/links
await callTool(client, 'browser_evaluate', {
  function: "() => {
    const btn = document.querySelector('a[href=\"/projects\"]');
    if (btn) { btn.click(); return 'clicked'; }
  }"
}, 'Click "📂 Open My Projects" button');
```

---

<!-- section_id: "8f53190f-0360-4bd7-8b4f-3e622bb41394" -->
## What Each Approach Tests

<!-- section_id: "76624637-b227-4837-a292-d235aa93aa50" -->
### Direct URL Navigation ✅ Tests:
- ✅ Page functionality works correctly
- ✅ Forms can be filled and submitted
- ✅ Buttons and links exist on pages
- ✅ End-to-end workflows complete
- ✅ State management within pages

<!-- section_id: "0ee40889-622e-4537-9c13-f4307bc8427a" -->
### Direct URL Navigation ❌ Misses:
- ❌ Navigation menu structure
- ❌ Breadcrumb link functionality
- ❌ Button visibility and layout
- ❌ User journey flow validation
- ❌ Deep linking edge cases
- ❌ Navigation guards and redirects

<!-- section_id: "eb28bd6a-2611-4fe9-aeb8-6ba84c5436ec" -->
### Realistic UI Navigation ✅ Tests:
- ✅ **Everything from Direct approach PLUS:**
- ✅ Navigation menus work correctly
- ✅ Breadcrumbs navigate properly
- ✅ Buttons are visible and clickable
- ✅ User can complete tasks without knowing URLs
- ✅ Navigation flow makes sense
- ✅ Back/forward navigation works

---

<!-- section_id: "cca99a03-27b0-4f96-84ab-806d018414dd" -->
## Example: Projects Flow

<!-- section_id: "f42d81f6-a3d1-47f7-9286-33a2d65f6936" -->
### Original (Direct Navigation)
```javascript
// 1. Login
await navigate('/login');
// ... login ...

// 2. Jump to projects
await navigate('/projects');

// 3. Jump to create form
await navigate('/projects/create');

// 4. Create project
// ... fill form ...

// 5. Jump back to projects
await navigate('/projects');
```

**Issues**:
- Doesn't validate that "Open My Projects" button exists
- Doesn't validate that "➕ New Project" button is clickable
- Doesn't validate breadcrumb navigation
- User would be lost without knowing URLs

<!-- section_id: "392aa530-5c6d-433e-82e5-c87ae4737b83" -->
### Realistic (UI Navigation)
```javascript
// 1. Login
await navigate('/login');
// ... login ...

// 2. Click "Open My Projects" from Dashboard
await click('a[href="/projects"]');

// 3. Click "➕ New Project" button
await click('a[href="/projects/create"]');

// 4. Create project
// ... fill form ...

// 5. Click "← My Projects" breadcrumb
await click('a[href="/projects"]');
```

**Validates**:
- ✅ Dashboard has "Open My Projects" button
- ✅ Projects page has "➕ New Project" button
- ✅ Breadcrumb "← My Projects" exists and works
- ✅ User can navigate without knowing any URLs

---

<!-- section_id: "36fc3034-53e5-4121-8ca9-0c36e631e821" -->
## Navigation Paths Validated

<!-- section_id: "13903288-625c-47e5-9a80-a905a59985dc" -->
### Realistic Test Validates These Flows:

1. **Dashboard → Projects**
   - Via "📂 Open My Projects" button
   - Validates: Button exists, is clickable, navigates correctly

2. **Projects → Create Form**
   - Via "➕ New Project" button
   - Validates: Button is visible, accessible, works

3. **Create Form → Projects List**
   - Via "← My Projects" breadcrumb
   - Validates: Breadcrumb exists after creation, navigates back

4. **Projects → Enter Project**
   - Via "🎯 Enter" button on project card
   - Validates: Enter button appears on each project

5. **Project Menu → Dashboard**
   - Via "← Dashboard" breadcrumb
   - Validates: Breadcrumb navigation from project context

6. **Dashboard → Projects → Create** (full path)
   - Validates: Complete user journey without shortcuts

---

<!-- section_id: "58abbd29-cd73-4ac8-acda-c59d9297bdcd" -->
## Conversion Progress

| User Stories | Direct Script | Realistic Script | Status |
| --- | --- | --- | --- |
| US-001-005 | `scripts/mcp-playwright-demo.mjs` | `scripts/mcp-playwright-demo-realistic.mjs` | ✅ Completed |
| US-006-011 | `scripts/mcp-user-stories-006-009.mjs` | `scripts/mcp-user-stories-006-009-realistic.mjs` | ✅ Completed |
| US-012-015 | `scripts/mcp-projects-flow.mjs` | `scripts/mcp-projects-flow-realistic.mjs` | ✅ Completed |
| US-016-017-024 | `scripts/mcp-project-variants.mjs` | `scripts/mcp-project-variants-realistic.mjs` | ✅ Completed |
| US-018-023 | `scripts/mcp-project-share-delete.mjs` | `scripts/mcp-project-share-delete-realistic.mjs` | ✅ Completed |
| US-025-028 | `scripts/mcp-phonemes-flat.mjs` | `scripts/mcp-phonemes-flat-realistic.mjs` | ✅ Completed |
| US-029-037 | `scripts/mcp-words-flow.mjs` | `scripts/mcp-words-flow-realistic.mjs` | ✅ Completed |
| US-038-049 | `scripts/mcp-phoneme-admin.mjs` | _(pending)_ | 🚧 In Progress |
| US-050-053 | `scripts/mcp-admin-database-tools.mjs` | _(pending)_ | 🚧 In Progress |
| US-054-056 | `scripts/mcp-tts-experience.mjs` | _(pending)_ | 🚧 In Progress |
| US-057-059 | `scripts/mcp-storage-resilience.mjs` | _(pending)_ | 🚧 In Progress |
| US-060-061 | `scripts/mcp-storage-resilience.mjs` (subset) | _(pending)_ | 🚧 In Progress |
| US-062-063 | `scripts/mcp-projects-flow.mjs` (subset) | _(pending)_ | 🚧 In Progress |
| US-064 | `scripts/mcp-journey-onboarding.mjs` | _(pending)_ | 🚧 In Progress |
| US-065 | `scripts/mcp-journey-collaboration.mjs` | _(pending)_ | 🚧 In Progress |
| US-066 | `scripts/mcp-journey-branching.mjs` | _(pending)_ | 🚧 In Progress |
| US-067 | `scripts/mcp-journey-mobile.mjs` | _(pending)_ | 🚧 In Progress |

---

<!-- section_id: "2dd4420d-e587-44eb-995f-b6aaeef92dcb" -->
## Running Both Modes

```bash
# Direct navigation only
python scripts/automation/run_user_stories.py --navigation-mode direct

# Realistic navigation slice (only runs stories with UI flows defined)
python scripts/automation/run_user_stories.py --navigation-mode realistic

# Full comparison run (direct + realistic where available)
python scripts/automation/run_user_stories.py --navigation-mode both
```

The runner reads `scripts/automation/story_plan.sample.json`, which now maps each user-story bundle to both the direct and realistic scripts where available. You can supply a different plan file with the same structure if you need to customize coverage.

---

<!-- section_id: "26ca6a40-e6da-4b4c-be05-158588783545" -->
## When to Use Each Approach

<!-- section_id: "8f2894dd-4133-4859-a7fc-9d7b77c94b72" -->
### Use Direct Navigation When:
- ✅ **Speed is critical** (running thousands of tests)
- ✅ **Testing page functionality** (not navigation)
- ✅ **Setting up test state** (need to get somewhere fast)
- ✅ **Testing specific features** in isolation
- ✅ **Running smoke tests** (quick validation)

<!-- section_id: "77c46b3a-d24f-4444-835d-e91c3564cd62" -->
### Use Realistic Navigation When:
- ✅ **Testing user experience** end-to-end
- ✅ **Validating navigation flows** are intuitive
- ✅ **Checking UI element visibility** and accessibility
- ✅ **Testing breadcrumbs and menus** work correctly
- ✅ **Validating user journeys** make sense
- ✅ **Demonstrating the app** to stakeholders
- ✅ **Catching navigation bugs** (missing buttons, broken links)

---

<!-- section_id: "25911180-3c26-4606-a24d-e3f0b45b11ea" -->
## Performance Comparison

| Metric | Direct Navigation | Realistic Navigation |
|--------|------------------|---------------------|
| **Execution Time** | ~15 seconds | ~25 seconds |
| **Test Coverage** | Page functionality | Page + Navigation |
| **Bug Detection** | Feature bugs | Feature + UX bugs |
| **Maintenance** | Easier (fewer steps) | Harder (more selectors) |
| **User Realism** | 60% | 95% |

---

<!-- section_id: "ec05e374-6d9c-45cf-84f6-1b98a143b657" -->
## Recommended Strategy

<!-- section_id: "046a6b69-d39e-4a1c-8240-6131b34fe63f" -->
### Hybrid Approach (Best of Both Worlds)

1. **Smoke Tests**: Use direct navigation
   - Fast validation that core features work
   - Run on every commit

2. **Integration Tests**: Use realistic navigation
   - Validate complete user journeys
   - Run daily or before releases

3. **Regression Tests**: Mix both
   - Direct navigation for speed
   - Realistic for critical user paths

<!-- section_id: "76150d55-c7d1-4d21-b2bd-5df52ec612aa" -->
### Example Test Suite Structure:

```
tests/
├── smoke/                    # Direct navigation (fast)
│   ├── auth-smoke.mjs
│   ├── projects-smoke.mjs
│   └── words-smoke.mjs
├── integration/              # Realistic navigation (thorough)
│   ├── user-journey-new-user.mjs
│   ├── user-journey-collaboration.mjs
│   └── navigation-flows.mjs
└── regression/               # Mixed approach
    ├── critical-paths.mjs    # Realistic
    └── feature-coverage.mjs  # Direct
```

---

<!-- section_id: "1873e83c-6582-4a5f-84f0-35eecf2cf1d3" -->
## Running the Realistic Test

```bash
# Set environment variables
export MCP_URL=http://localhost:3334/mcp
export APP_BASE_URL=http://127.0.0.1:5002

# Run realistic navigation test
node scripts/mcp-projects-flow-realistic.mjs
```

---

<!-- section_id: "18fa1bb2-b0ea-4738-9364-7b8f7cccb305" -->
## Key Differences in Code

<!-- section_id: "0685a1c6-c3ee-4da1-bf90-f9e7601667f1" -->
### Finding Elements

**Original (assumes you know page structure):**
```javascript
await navigate('/projects/create');
await fillForm('#name', 'My Project');
```

**Realistic (finds elements on current page):**
```javascript
// First, find the "New Project" button
const snapshot = await browser_snapshot();
const ref = extractRef(snapshot, 'New Project');
await browser_click({ element: 'New Project button', ref });

// Then fill form on whichever page we landed
await fillForm('#name', 'My Project');
```

<!-- section_id: "616c50e6-bb20-482a-aa23-fe9c18850b64" -->
### Navigation Validation

**Original:**
```javascript
// Just go there
await navigate('/projects');
```

**Realistic:**
```javascript
// Verify the button exists and click it
const result = await evaluate(`
  const btn = document.querySelector('a[href="/projects"]');
  if (btn) {
    btn.click();
    return 'clicked';
  }
  return 'button-not-found';
`);
if (result === 'button-not-found') {
  throw new Error('❌ "Open My Projects" button not found on Dashboard');
}
```

---

<!-- section_id: "6cc3866f-9eff-4ddd-ae25-f60342dd86e1" -->
## Bugs Each Approach Catches

<!-- section_id: "a1f468f8-3e73-4653-93b5-0fe753c9d96f" -->
### Direct Navigation Catches:
- ✅ Form validation errors
- ✅ API endpoint failures
- ✅ Database errors
- ✅ Business logic bugs

<!-- section_id: "ffb69648-be21-49f6-b321-a906ecc1076b" -->
### Realistic Navigation ALSO Catches:
- ✅ **Missing navigation buttons**
- ✅ **Broken breadcrumb links**
- ✅ **Incorrect button labels**
- ✅ **Hidden/disabled navigation elements**
- ✅ **Wrong navigation targets**
- ✅ **Confusing user flows**

---

<!-- section_id: "d44bbf8a-ff19-40e0-899f-176cc71a82cd" -->
## Example Bug Scenarios

<!-- section_id: "29206cf2-54c5-491a-9341-5a8d404b9782" -->
### Bug Only Realistic Navigation Would Catch:

**Scenario**: Developer accidentally removes "Open My Projects" button from Dashboard

- ❌ **Direct navigation**: Test passes (jumps directly to /projects)
- ✅ **Realistic navigation**: Test fails (can't find button to click)

**Scenario**: Breadcrumb "← My Projects" points to wrong URL

- ❌ **Direct navigation**: Never tests breadcrumbs
- ✅ **Realistic navigation**: Catches incorrect navigation target

**Scenario**: "New Project" button hidden by CSS on mobile

- ❌ **Direct navigation**: Never clicks the button
- ✅ **Realistic navigation**: Fails when button not clickable

---

<!-- section_id: "be478b67-56f3-46cf-9e6e-9a3898c3fae2" -->
## Conclusion

- **Both approaches have value**
- **Direct navigation** = Fast, reliable for feature testing
- **Realistic navigation** = Slow, thorough for UX validation
- **Best strategy** = Use both in different test suites

The realistic navigation approach provides **higher confidence** that users can actually complete their tasks without memorizing URLs!
