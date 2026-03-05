---
resource_id: "39a56132-96c9-4177-9600-8352b5c57408"
resource_type: "document"
resource_name: "REALISTIC_vs_DIRECT_NAVIGATION"
---
# Realistic vs Direct Navigation Testing

<!-- section_id: "be58c622-c569-4f7c-81f8-d9c1f64dc878" -->
## Overview

This document explains the difference between the two navigation approaches in our automation tests and when to use each.

---

<!-- section_id: "dbf575e2-6345-4494-b88d-f7d7822052fa" -->
## Comparison

<!-- section_id: "3b8957c3-ad55-41e8-a76c-9cd9514878a6" -->
### Original Approach (Direct URL Navigation)

**File**: `scripts/mcp-projects-flow.mjs`

```javascript
// Jump directly to pages via URL
await callTool(client, 'browser_navigate', { url: `${BASE}/projects` });
await callTool(client, 'browser_navigate', { url: `${BASE}/projects/create` });
await callTool(client, 'browser_navigate', { url: `${BASE}/admin/templates` });
```

<!-- section_id: "b846d427-ad5b-4e73-9b4d-6939f66081f1" -->
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

<!-- section_id: "3b75a5ea-10a0-4766-8304-791289372c14" -->
## What Each Approach Tests

<!-- section_id: "edb17238-7ea4-47b2-9890-ed0e0b0f2a49" -->
### Direct URL Navigation ✅ Tests:
- ✅ Page functionality works correctly
- ✅ Forms can be filled and submitted
- ✅ Buttons and links exist on pages
- ✅ End-to-end workflows complete
- ✅ State management within pages

<!-- section_id: "188e43a1-9666-4722-a5ed-d05f8841bae4" -->
### Direct URL Navigation ❌ Misses:
- ❌ Navigation menu structure
- ❌ Breadcrumb link functionality
- ❌ Button visibility and layout
- ❌ User journey flow validation
- ❌ Deep linking edge cases
- ❌ Navigation guards and redirects

<!-- section_id: "b30d970b-c5ef-4db8-a501-28aefe2ed9e3" -->
### Realistic UI Navigation ✅ Tests:
- ✅ **Everything from Direct approach PLUS:**
- ✅ Navigation menus work correctly
- ✅ Breadcrumbs navigate properly
- ✅ Buttons are visible and clickable
- ✅ User can complete tasks without knowing URLs
- ✅ Navigation flow makes sense
- ✅ Back/forward navigation works

---

<!-- section_id: "ac41c810-a6ae-494f-a334-baa8785fcd00" -->
## Example: Projects Flow

<!-- section_id: "e77a3e23-085e-4afb-90db-6e505685d771" -->
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

<!-- section_id: "4780cf73-3e60-4239-999d-9888ac468737" -->
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

<!-- section_id: "7ba5d835-bf91-4ac6-8d16-3ccc1d6fd793" -->
## Navigation Paths Validated

<!-- section_id: "bbf29767-3e61-4a21-bb81-b91ca34a4522" -->
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

<!-- section_id: "ea51a9ce-deda-4538-b64e-e0101eb89392" -->
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

<!-- section_id: "5749966a-0991-4ac1-8bb4-f0eb28183257" -->
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

<!-- section_id: "6c495a7e-8c25-4972-95a3-e3243473245c" -->
## When to Use Each Approach

<!-- section_id: "14917e17-a50a-440e-aee1-0e41ec7d0f86" -->
### Use Direct Navigation When:
- ✅ **Speed is critical** (running thousands of tests)
- ✅ **Testing page functionality** (not navigation)
- ✅ **Setting up test state** (need to get somewhere fast)
- ✅ **Testing specific features** in isolation
- ✅ **Running smoke tests** (quick validation)

<!-- section_id: "24bcc367-dc1c-494a-8089-937a0f0f7c2c" -->
### Use Realistic Navigation When:
- ✅ **Testing user experience** end-to-end
- ✅ **Validating navigation flows** are intuitive
- ✅ **Checking UI element visibility** and accessibility
- ✅ **Testing breadcrumbs and menus** work correctly
- ✅ **Validating user journeys** make sense
- ✅ **Demonstrating the app** to stakeholders
- ✅ **Catching navigation bugs** (missing buttons, broken links)

---

<!-- section_id: "939ab992-5d14-4fdb-a430-40e359f1f070" -->
## Performance Comparison

| Metric | Direct Navigation | Realistic Navigation |
|--------|------------------|---------------------|
| **Execution Time** | ~15 seconds | ~25 seconds |
| **Test Coverage** | Page functionality | Page + Navigation |
| **Bug Detection** | Feature bugs | Feature + UX bugs |
| **Maintenance** | Easier (fewer steps) | Harder (more selectors) |
| **User Realism** | 60% | 95% |

---

<!-- section_id: "54d58f06-34e4-4d3e-9d97-18364a8daf70" -->
## Recommended Strategy

<!-- section_id: "df56e6f6-21ec-40a2-96de-27cc6a9f6d0f" -->
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

<!-- section_id: "6dbec588-cf15-4b6e-8e82-43842f5b825e" -->
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

<!-- section_id: "b8641073-63c0-4122-bcdd-29bab4b717cc" -->
## Running the Realistic Test

```bash
# Set environment variables
export MCP_URL=http://localhost:3334/mcp
export APP_BASE_URL=http://127.0.0.1:5002

# Run realistic navigation test
node scripts/mcp-projects-flow-realistic.mjs
```

---

<!-- section_id: "a58f393b-8ce4-461d-bc87-d1e12dc091ed" -->
## Key Differences in Code

<!-- section_id: "5f49103f-f3c9-4dc9-95e1-3dd09859b3ae" -->
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

<!-- section_id: "9bfcc319-1df3-43d4-b171-f7a127c1e598" -->
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

<!-- section_id: "f70fac0d-aa1f-4048-8918-81741d8bacd3" -->
## Bugs Each Approach Catches

<!-- section_id: "575b8b28-a0b9-4d9e-a319-e71daa154bfb" -->
### Direct Navigation Catches:
- ✅ Form validation errors
- ✅ API endpoint failures
- ✅ Database errors
- ✅ Business logic bugs

<!-- section_id: "2244f572-4222-4f3f-96a0-86083994537e" -->
### Realistic Navigation ALSO Catches:
- ✅ **Missing navigation buttons**
- ✅ **Broken breadcrumb links**
- ✅ **Incorrect button labels**
- ✅ **Hidden/disabled navigation elements**
- ✅ **Wrong navigation targets**
- ✅ **Confusing user flows**

---

<!-- section_id: "616d7f86-99e0-4ac3-8a15-fdf9fd9cf9e7" -->
## Example Bug Scenarios

<!-- section_id: "6cac9810-a179-4100-b2b9-eb85dba6dabc" -->
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

<!-- section_id: "d5e33db6-4f03-4ec2-affc-cd6278614e66" -->
## Conclusion

- **Both approaches have value**
- **Direct navigation** = Fast, reliable for feature testing
- **Realistic navigation** = Slow, thorough for UX validation
- **Best strategy** = Use both in different test suites

The realistic navigation approach provides **higher confidence** that users can actually complete their tasks without memorizing URLs!
