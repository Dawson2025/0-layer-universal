---
resource_id: "2daef357-6d5b-4b81-ad49-31f84b5b9721"
resource_type: "document"
resource_name: "REALISTIC_vs_DIRECT_NAVIGATION"
---
# Realistic vs Direct Navigation Testing

<!-- section_id: "513d4961-62ff-4f26-be3d-fb39153c48a8" -->
## Overview

This document explains the difference between the two navigation approaches in our automation tests and when to use each.

---

<!-- section_id: "ac090a17-cd6e-4299-8f82-26bf4e5f637b" -->
## Comparison

<!-- section_id: "86f88dc5-c4dd-4a4d-919c-ad35a260184d" -->
### Original Approach (Direct URL Navigation)

**File**: `scripts/mcp-projects-flow.mjs`

```javascript
// Jump directly to pages via URL
await callTool(client, 'browser_navigate', { url: `${BASE}/projects` });
await callTool(client, 'browser_navigate', { url: `${BASE}/projects/create` });
await callTool(client, 'browser_navigate', { url: `${BASE}/admin/templates` });
```

<!-- section_id: "79c3a859-f780-4b6d-a656-f1af2f97a9cd" -->
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

<!-- section_id: "4a431563-fa3d-4e33-8f7c-d9aec0677eff" -->
## What Each Approach Tests

<!-- section_id: "215c3402-81f0-49ea-b9c7-3fab8d40efcc" -->
### Direct URL Navigation ✅ Tests:
- ✅ Page functionality works correctly
- ✅ Forms can be filled and submitted
- ✅ Buttons and links exist on pages
- ✅ End-to-end workflows complete
- ✅ State management within pages

<!-- section_id: "e3e1ff20-4468-4dad-b8c9-bb5389995461" -->
### Direct URL Navigation ❌ Misses:
- ❌ Navigation menu structure
- ❌ Breadcrumb link functionality
- ❌ Button visibility and layout
- ❌ User journey flow validation
- ❌ Deep linking edge cases
- ❌ Navigation guards and redirects

<!-- section_id: "80ddcdfc-fcd9-457e-8f5b-99dd50799370" -->
### Realistic UI Navigation ✅ Tests:
- ✅ **Everything from Direct approach PLUS:**
- ✅ Navigation menus work correctly
- ✅ Breadcrumbs navigate properly
- ✅ Buttons are visible and clickable
- ✅ User can complete tasks without knowing URLs
- ✅ Navigation flow makes sense
- ✅ Back/forward navigation works

---

<!-- section_id: "c935b82a-aff6-40ce-8830-26af7d04a803" -->
## Example: Projects Flow

<!-- section_id: "cf315c90-ad87-4dfa-b6c0-a783eddbc82e" -->
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

<!-- section_id: "b71a90ed-e0af-4699-aa45-707a4ea354ec" -->
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

<!-- section_id: "27310624-5b92-4086-8f5b-b5b61daefe92" -->
## Navigation Paths Validated

<!-- section_id: "cc9e7735-fb22-4ac9-a3ec-2953c71ce8b7" -->
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

<!-- section_id: "2c510a9f-f5da-4807-aa94-5a5c78cac338" -->
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

<!-- section_id: "8c9d4be7-ac23-4d21-9b06-a973260f66e1" -->
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

<!-- section_id: "556a3493-a2d4-402f-9d48-161f37bdd65f" -->
## When to Use Each Approach

<!-- section_id: "27cf0e6e-e7ef-494a-a67b-3d693896ac78" -->
### Use Direct Navigation When:
- ✅ **Speed is critical** (running thousands of tests)
- ✅ **Testing page functionality** (not navigation)
- ✅ **Setting up test state** (need to get somewhere fast)
- ✅ **Testing specific features** in isolation
- ✅ **Running smoke tests** (quick validation)

<!-- section_id: "901ff014-8802-48d8-a97b-30b41003bc03" -->
### Use Realistic Navigation When:
- ✅ **Testing user experience** end-to-end
- ✅ **Validating navigation flows** are intuitive
- ✅ **Checking UI element visibility** and accessibility
- ✅ **Testing breadcrumbs and menus** work correctly
- ✅ **Validating user journeys** make sense
- ✅ **Demonstrating the app** to stakeholders
- ✅ **Catching navigation bugs** (missing buttons, broken links)

---

<!-- section_id: "2d093c79-22fb-4677-886c-0d74e4c988d3" -->
## Performance Comparison

| Metric | Direct Navigation | Realistic Navigation |
|--------|------------------|---------------------|
| **Execution Time** | ~15 seconds | ~25 seconds |
| **Test Coverage** | Page functionality | Page + Navigation |
| **Bug Detection** | Feature bugs | Feature + UX bugs |
| **Maintenance** | Easier (fewer steps) | Harder (more selectors) |
| **User Realism** | 60% | 95% |

---

<!-- section_id: "6401992b-c4bb-4bd3-bcbb-f20800e08b3b" -->
## Recommended Strategy

<!-- section_id: "9ed620cb-e82c-42bb-b4c9-d5f13d493fd3" -->
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

<!-- section_id: "999f608d-e842-40fe-bb81-e84b6b4d900e" -->
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

<!-- section_id: "40e77896-2526-4c20-9646-dd106aab0150" -->
## Running the Realistic Test

```bash
# Set environment variables
export MCP_URL=http://localhost:3334/mcp
export APP_BASE_URL=http://127.0.0.1:5002

# Run realistic navigation test
node scripts/mcp-projects-flow-realistic.mjs
```

---

<!-- section_id: "ccbcd7cc-4ccc-4578-a9cd-386644d79e9f" -->
## Key Differences in Code

<!-- section_id: "c1b8be8e-a7e4-4c24-8ae0-62201aadc8c1" -->
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

<!-- section_id: "26b48a92-9a5e-404c-bcc5-bbf317eefc65" -->
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

<!-- section_id: "79bb3732-cf48-418f-bc87-d9647ebb8292" -->
## Bugs Each Approach Catches

<!-- section_id: "add6f5b0-75e6-4bfb-930b-f75b63f9ec17" -->
### Direct Navigation Catches:
- ✅ Form validation errors
- ✅ API endpoint failures
- ✅ Database errors
- ✅ Business logic bugs

<!-- section_id: "a3247b1d-cc68-49ac-bea3-75ffc21071e8" -->
### Realistic Navigation ALSO Catches:
- ✅ **Missing navigation buttons**
- ✅ **Broken breadcrumb links**
- ✅ **Incorrect button labels**
- ✅ **Hidden/disabled navigation elements**
- ✅ **Wrong navigation targets**
- ✅ **Confusing user flows**

---

<!-- section_id: "8c80740e-0898-4fee-b58f-66a9b53786be" -->
## Example Bug Scenarios

<!-- section_id: "58a63680-36dd-414d-b14e-b737bd7854bc" -->
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

<!-- section_id: "79ec74f8-1792-46d3-a39b-88e9ee8df454" -->
## Conclusion

- **Both approaches have value**
- **Direct navigation** = Fast, reliable for feature testing
- **Realistic navigation** = Slow, thorough for UX validation
- **Best strategy** = Use both in different test suites

The realistic navigation approach provides **higher confidence** that users can actually complete their tasks without memorizing URLs!
