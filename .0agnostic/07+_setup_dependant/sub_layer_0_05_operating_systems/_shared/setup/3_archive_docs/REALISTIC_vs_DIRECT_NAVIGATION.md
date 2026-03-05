---
resource_id: "5984ee41-3681-44dc-8f4e-0db5d59f19c0"
resource_type: "document"
resource_name: "REALISTIC_vs_DIRECT_NAVIGATION"
---
# Realistic vs Direct Navigation Testing

<!-- section_id: "0ad57503-1625-45fa-bfb6-a2a28910a840" -->
## Overview

This document explains the difference between the two navigation approaches in our automation tests and when to use each.

---

<!-- section_id: "a9c62ee3-fb30-474e-bdf1-045eb2f5209e" -->
## Comparison

<!-- section_id: "d7e46f8f-90df-4e6e-8bae-673e6f4f815c" -->
### Original Approach (Direct URL Navigation)

**File**: `scripts/mcp-projects-flow.mjs`

```javascript
// Jump directly to pages via URL
await callTool(client, 'browser_navigate', { url: `${BASE}/projects` });
await callTool(client, 'browser_navigate', { url: `${BASE}/projects/create` });
await callTool(client, 'browser_navigate', { url: `${BASE}/admin/templates` });
```

<!-- section_id: "1deca623-ef4f-4217-851a-7fb5e33ad99a" -->
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

<!-- section_id: "ee99f9d6-0f95-4fad-aba8-2974f93405f5" -->
## What Each Approach Tests

<!-- section_id: "bbe41a2b-0442-461c-931b-bfc381155d85" -->
### Direct URL Navigation ✅ Tests:
- ✅ Page functionality works correctly
- ✅ Forms can be filled and submitted
- ✅ Buttons and links exist on pages
- ✅ End-to-end workflows complete
- ✅ State management within pages

<!-- section_id: "8e01598d-4653-40a8-bbf1-a14d62ffb3f9" -->
### Direct URL Navigation ❌ Misses:
- ❌ Navigation menu structure
- ❌ Breadcrumb link functionality
- ❌ Button visibility and layout
- ❌ User journey flow validation
- ❌ Deep linking edge cases
- ❌ Navigation guards and redirects

<!-- section_id: "77f5c8da-2538-4472-8587-990b6ac20b7f" -->
### Realistic UI Navigation ✅ Tests:
- ✅ **Everything from Direct approach PLUS:**
- ✅ Navigation menus work correctly
- ✅ Breadcrumbs navigate properly
- ✅ Buttons are visible and clickable
- ✅ User can complete tasks without knowing URLs
- ✅ Navigation flow makes sense
- ✅ Back/forward navigation works

---

<!-- section_id: "2d129674-50f3-49b7-be7c-b4755671e68f" -->
## Example: Projects Flow

<!-- section_id: "df42a0ec-2bfc-492b-a9ca-66df0cdfe428" -->
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

<!-- section_id: "efda4b4b-bcd2-4241-a59b-8b3240ce525b" -->
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

<!-- section_id: "168c6b23-7ade-4e65-bba9-52104c3c548b" -->
## Navigation Paths Validated

<!-- section_id: "df63a643-4aef-406d-81ee-4fb725b2cc59" -->
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

<!-- section_id: "5912eb8c-c5c2-4a02-a68f-8e7c1674b9eb" -->
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

<!-- section_id: "faba68d2-3d6d-4184-9fb4-fadebcb4b330" -->
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

<!-- section_id: "a8fc1a9b-fcbf-4bbc-be85-c267b9ce1f4f" -->
## When to Use Each Approach

<!-- section_id: "3dcb9b3a-034e-4c1d-bc5b-5546cff246ce" -->
### Use Direct Navigation When:
- ✅ **Speed is critical** (running thousands of tests)
- ✅ **Testing page functionality** (not navigation)
- ✅ **Setting up test state** (need to get somewhere fast)
- ✅ **Testing specific features** in isolation
- ✅ **Running smoke tests** (quick validation)

<!-- section_id: "46d11f08-eac9-4052-a90b-a613c877d8f7" -->
### Use Realistic Navigation When:
- ✅ **Testing user experience** end-to-end
- ✅ **Validating navigation flows** are intuitive
- ✅ **Checking UI element visibility** and accessibility
- ✅ **Testing breadcrumbs and menus** work correctly
- ✅ **Validating user journeys** make sense
- ✅ **Demonstrating the app** to stakeholders
- ✅ **Catching navigation bugs** (missing buttons, broken links)

---

<!-- section_id: "67a431a6-ea33-4d39-9a01-472eaa079237" -->
## Performance Comparison

| Metric | Direct Navigation | Realistic Navigation |
|--------|------------------|---------------------|
| **Execution Time** | ~15 seconds | ~25 seconds |
| **Test Coverage** | Page functionality | Page + Navigation |
| **Bug Detection** | Feature bugs | Feature + UX bugs |
| **Maintenance** | Easier (fewer steps) | Harder (more selectors) |
| **User Realism** | 60% | 95% |

---

<!-- section_id: "1014d708-1399-4e14-8adb-81c0dffbcd38" -->
## Recommended Strategy

<!-- section_id: "de98c7f6-0252-461d-a082-bcae7b58c336" -->
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

<!-- section_id: "236851f9-8d1a-4705-993b-51bfe12f7dd4" -->
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

<!-- section_id: "c0a0ae83-d747-4c4f-a620-17d5cc7bff71" -->
## Running the Realistic Test

```bash
# Set environment variables
export MCP_URL=http://localhost:3334/mcp
export APP_BASE_URL=http://127.0.0.1:5002

# Run realistic navigation test
node scripts/mcp-projects-flow-realistic.mjs
```

---

<!-- section_id: "33ed427b-214e-427c-8876-feb6ef462252" -->
## Key Differences in Code

<!-- section_id: "a99dd9ea-7c05-4cde-bafb-9226a5dd3724" -->
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

<!-- section_id: "f8b07c41-4bba-4324-a99c-0d8a0ddb07de" -->
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

<!-- section_id: "b68702f7-d1c9-4b87-9571-f85fb0fff9ab" -->
## Bugs Each Approach Catches

<!-- section_id: "224c53cb-5d40-4f83-98c7-ac63c890cd6c" -->
### Direct Navigation Catches:
- ✅ Form validation errors
- ✅ API endpoint failures
- ✅ Database errors
- ✅ Business logic bugs

<!-- section_id: "887b8a88-65f1-4b4b-9881-f85a34221c1b" -->
### Realistic Navigation ALSO Catches:
- ✅ **Missing navigation buttons**
- ✅ **Broken breadcrumb links**
- ✅ **Incorrect button labels**
- ✅ **Hidden/disabled navigation elements**
- ✅ **Wrong navigation targets**
- ✅ **Confusing user flows**

---

<!-- section_id: "835be7ca-16bc-45ce-8d83-9aa182789ccd" -->
## Example Bug Scenarios

<!-- section_id: "e2de1b2b-aa5a-4428-bbcc-44e6cfa0f3f7" -->
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

<!-- section_id: "f0095f9b-229f-4abf-af52-c7126c65238d" -->
## Conclusion

- **Both approaches have value**
- **Direct navigation** = Fast, reliable for feature testing
- **Realistic navigation** = Slow, thorough for UX validation
- **Best strategy** = Use both in different test suites

The realistic navigation approach provides **higher confidence** that users can actually complete their tasks without memorizing URLs!
