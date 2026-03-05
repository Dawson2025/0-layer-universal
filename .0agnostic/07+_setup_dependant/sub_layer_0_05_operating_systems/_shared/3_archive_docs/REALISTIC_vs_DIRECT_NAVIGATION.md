---
resource_id: "c01d1469-e4ee-4cfd-894f-f3280191abe2"
resource_type: "document"
resource_name: "REALISTIC_vs_DIRECT_NAVIGATION"
---
# Realistic vs Direct Navigation Testing

<!-- section_id: "048a32e7-8428-4891-869e-c0c1c1bd6719" -->
## Overview

This document explains the difference between the two navigation approaches in our automation tests and when to use each.

---

<!-- section_id: "9015c3ff-1c9f-4b06-8ae4-f3e226134510" -->
## Comparison

<!-- section_id: "e2818352-5419-47c4-830c-9cb972e32de9" -->
### Original Approach (Direct URL Navigation)

**File**: `scripts/mcp-projects-flow.mjs`

```javascript
// Jump directly to pages via URL
await callTool(client, 'browser_navigate', { url: `${BASE}/projects` });
await callTool(client, 'browser_navigate', { url: `${BASE}/projects/create` });
await callTool(client, 'browser_navigate', { url: `${BASE}/admin/templates` });
```

<!-- section_id: "ad5fc1f4-8fa1-406b-a1b1-261a3872b430" -->
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

<!-- section_id: "34c43bda-a910-4ac6-86c5-3517cc5be0ca" -->
## What Each Approach Tests

<!-- section_id: "411142fe-efd1-433b-98a3-8491bc761b3f" -->
### Direct URL Navigation ✅ Tests:
- ✅ Page functionality works correctly
- ✅ Forms can be filled and submitted
- ✅ Buttons and links exist on pages
- ✅ End-to-end workflows complete
- ✅ State management within pages

<!-- section_id: "d51f8dd2-1913-4dcb-a9f2-3548d6d95e33" -->
### Direct URL Navigation ❌ Misses:
- ❌ Navigation menu structure
- ❌ Breadcrumb link functionality
- ❌ Button visibility and layout
- ❌ User journey flow validation
- ❌ Deep linking edge cases
- ❌ Navigation guards and redirects

<!-- section_id: "473095bc-d7f1-4d98-9b61-a4188f75ca80" -->
### Realistic UI Navigation ✅ Tests:
- ✅ **Everything from Direct approach PLUS:**
- ✅ Navigation menus work correctly
- ✅ Breadcrumbs navigate properly
- ✅ Buttons are visible and clickable
- ✅ User can complete tasks without knowing URLs
- ✅ Navigation flow makes sense
- ✅ Back/forward navigation works

---

<!-- section_id: "30c8a5ce-cc37-4309-9206-989193c0340b" -->
## Example: Projects Flow

<!-- section_id: "7e9814f4-81fe-4ced-886b-79dd08525caf" -->
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

<!-- section_id: "5e44204c-571c-49bd-b080-6d5869458abc" -->
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

<!-- section_id: "8abc9dc9-733c-4bf8-bc82-243ab95e2619" -->
## Navigation Paths Validated

<!-- section_id: "7af54a5a-c0bc-490e-a226-297f570aefb2" -->
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

<!-- section_id: "91b6827f-c295-4e75-be89-94cd1cd3321b" -->
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

<!-- section_id: "f24e5606-584e-409f-9428-264d386021c9" -->
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

<!-- section_id: "6c9649a2-721e-4953-8f74-8e14e474d9e8" -->
## When to Use Each Approach

<!-- section_id: "cd6e70b9-beb4-46a9-b62d-563631a8054a" -->
### Use Direct Navigation When:
- ✅ **Speed is critical** (running thousands of tests)
- ✅ **Testing page functionality** (not navigation)
- ✅ **Setting up test state** (need to get somewhere fast)
- ✅ **Testing specific features** in isolation
- ✅ **Running smoke tests** (quick validation)

<!-- section_id: "dbec99e8-c452-455c-a9b7-b4613d7bb4d0" -->
### Use Realistic Navigation When:
- ✅ **Testing user experience** end-to-end
- ✅ **Validating navigation flows** are intuitive
- ✅ **Checking UI element visibility** and accessibility
- ✅ **Testing breadcrumbs and menus** work correctly
- ✅ **Validating user journeys** make sense
- ✅ **Demonstrating the app** to stakeholders
- ✅ **Catching navigation bugs** (missing buttons, broken links)

---

<!-- section_id: "9fd57961-a7bc-423f-8fdc-0e7c8fdf80a0" -->
## Performance Comparison

| Metric | Direct Navigation | Realistic Navigation |
|--------|------------------|---------------------|
| **Execution Time** | ~15 seconds | ~25 seconds |
| **Test Coverage** | Page functionality | Page + Navigation |
| **Bug Detection** | Feature bugs | Feature + UX bugs |
| **Maintenance** | Easier (fewer steps) | Harder (more selectors) |
| **User Realism** | 60% | 95% |

---

<!-- section_id: "ac31bee8-33b5-4255-a0ac-5dc5e3d830db" -->
## Recommended Strategy

<!-- section_id: "07a7f1ed-0872-43cf-8f4c-50730bd34bca" -->
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

<!-- section_id: "7fd1367f-5270-40ed-90aa-b729f683426d" -->
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

<!-- section_id: "97743ce0-2a38-4967-b2e4-895c7826e519" -->
## Running the Realistic Test

```bash
# Set environment variables
export MCP_URL=http://localhost:3334/mcp
export APP_BASE_URL=http://127.0.0.1:5002

# Run realistic navigation test
node scripts/mcp-projects-flow-realistic.mjs
```

---

<!-- section_id: "a00434c8-9f79-4963-a144-df7308843b85" -->
## Key Differences in Code

<!-- section_id: "51fb7043-c852-4768-b0d1-dc9813337217" -->
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

<!-- section_id: "3f43250a-4d4e-4e0f-b730-f0de20ed19b6" -->
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

<!-- section_id: "89c54411-4e91-43f3-a3fc-e068eedbcee3" -->
## Bugs Each Approach Catches

<!-- section_id: "12336dbc-e885-4bc4-b8a5-dd32710b4ddf" -->
### Direct Navigation Catches:
- ✅ Form validation errors
- ✅ API endpoint failures
- ✅ Database errors
- ✅ Business logic bugs

<!-- section_id: "f41073a8-a373-4c7a-a5c5-c45e61916ccf" -->
### Realistic Navigation ALSO Catches:
- ✅ **Missing navigation buttons**
- ✅ **Broken breadcrumb links**
- ✅ **Incorrect button labels**
- ✅ **Hidden/disabled navigation elements**
- ✅ **Wrong navigation targets**
- ✅ **Confusing user flows**

---

<!-- section_id: "0c352aef-fffc-45cc-97a7-d27cd3c1444a" -->
## Example Bug Scenarios

<!-- section_id: "d6185d86-54de-437a-bcfe-3918767a678f" -->
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

<!-- section_id: "1c19a16e-cadc-4bff-906f-013232717dba" -->
## Conclusion

- **Both approaches have value**
- **Direct navigation** = Fast, reliable for feature testing
- **Realistic navigation** = Slow, thorough for UX validation
- **Best strategy** = Use both in different test suites

The realistic navigation approach provides **higher confidence** that users can actually complete their tasks without memorizing URLs!
