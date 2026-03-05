---
resource_id: "2249ec17-faaf-4d34-adc9-bf55f2c627da"
resource_type: "document"
resource_name: "NAVIGATION_TESTING_GUIDE"
---
# Navigation Testing Guide

<!-- section_id: "040eddb6-19ae-4054-bff9-cc35c13a84cc" -->
## Overview

See also: docs/for_ai/DEPTH_FIRST_SLICE.md for the depth-first slice prototype strategy we follow when expanding or tightening automation checks.

This project now supports **dual-mode testing** for all automation test scripts. Each test can be run in two different navigation modes:

- **Direct Mode** (fast): Uses direct URL navigation for quick validation
- **Realistic Mode** (thorough): Uses only UI buttons/links to simulate real user navigation

<!-- section_id: "00ae91f9-9ae9-42cb-8902-40181fab6d1b" -->
## Why Two Modes?

<!-- section_id: "527c1977-c708-4c2e-9a27-73ce8b47f6a6" -->
### Direct Mode Benefits
- ⚡ **Speed**: 30-50% faster execution
- 🔄 **CI/CD**: Ideal for continuous integration pipelines
- 🎯 **API Focus**: Tests core functionality regardless of UI
- 📊 **Regression**: Quick smoke tests to catch breaking changes

<!-- section_id: "246c38be-e9e6-4890-bda5-1847f980caf5" -->
### Realistic Mode Benefits
- 🔍 **UX Validation**: Ensures features are actually accessible to users
- 🐛 **Navigation Gaps**: Exposes pages only accessible via URL changes
- 👤 **User Experience**: Tests actual user workflows and discoverability
- 📝 **Documentation**: Validates that documentation matches reality

<!-- section_id: "8d97e8bf-3393-4e4a-b2f6-3fe2ec84852e" -->
## Navigation Gaps Detected

During the creation of realistic tests, we discovered several pages that may not be accessible via standard UI navigation:

- `/admin/templates` - Template administration (onboarding journey)
- `/words/create/table-based` - Table-based word creation (may require alternate path)
- Storage option visibility depends on Firebase availability

**These gaps are now tracked and can be validated with realistic mode tests.**

<!-- section_id: "c4da5db2-0920-4f26-8574-67b48f9cc0c5" -->
## Running Tests

<!-- section_id: "e2d09048-769a-4506-9401-df95c5727d98" -->
### Run All Tests (Direct Mode Only)
```bash
python scripts/automation/run_user_stories.py --plan scripts/automation/story_plan.sample.json --navigation-mode direct
```

<!-- section_id: "d1d84ea3-6de7-4e25-9eee-ae1eb2c68ded" -->
### Run All Tests (Realistic Mode Only)
```bash
python scripts/automation/run_user_stories.py --plan scripts/automation/story_plan.sample.json --navigation-mode realistic
```

<!-- section_id: "bc9f07c1-ddbb-4f2a-a64d-626e15f63b9b" -->
### Run All Tests (Both Modes)
```bash
python scripts/automation/run_user_stories.py --plan scripts/automation/story_plan.sample.json --navigation-mode both
```

<!-- section_id: "4d246967-22f5-4ce0-aaee-ccd26ece92f6" -->
### Run Specific Test Group
```bash
# Run only authentication tests in both modes
python scripts/automation/run_user_stories.py --plan scripts/automation/story_plan.sample.json --filter "US-001" --navigation-mode both
```

<!-- section_id: "adba7fef-281d-42d4-985f-e3d0a8a5acf8" -->
## Test Coverage

All 67 user stories now have both direct and realistic test versions:

| Test Group | Direct Script | Realistic Script | User Stories |
|------------|--------------|------------------|--------------|
| Auth Basics | `mcp-playwright-demo.mjs` | `mcp-playwright-demo-realistic.mjs` | US-001-005 |
| Groups | `mcp-user-stories-006-009.mjs` | `mcp-user-stories-006-009-realistic.mjs` | US-006-011 |
| Projects | `mcp-projects-flow.mjs` | `mcp-projects-flow-realistic.mjs` | US-012-015 |
| Variants | `mcp-project-variants.mjs` | `mcp-project-variants-realistic.mjs` | US-016-017, 024 |
| Share/Delete | `mcp-project-share-delete.mjs` | `mcp-project-share-delete-realistic.mjs` | US-018-023 |
| Phoneme Views | `mcp-phonemes-flat.mjs` | `mcp-phonemes-flat-realistic.mjs` | US-025-028 |
| Words & Media | `mcp-words-flow.mjs` | `mcp-words-flow-realistic.mjs` | US-029-037 |
| Admin Phonemes | `mcp-phoneme-admin.mjs` | `mcp-phoneme-admin-realistic.mjs` | US-038-049 |
| Database Tools | `mcp-admin-database-tools.mjs` | `mcp-admin-database-tools-realistic.mjs` | US-050-053 |
| TTS Experience | `mcp-tts-experience.mjs` | `mcp-tts-experience-realistic.mjs` | US-054-056 |
| Storage | `mcp-storage-resilience.mjs` | `mcp-storage-resilience-realistic.mjs` | US-057-059 |
| Onboarding | `mcp-journey-onboarding.mjs` | `mcp-journey-onboarding-realistic.mjs` | US-064 |
| Collaboration | `mcp-journey-collaboration.mjs` | `mcp-journey-collaboration-realistic.mjs` | US-065 |
| Branching | `mcp-journey-branching.mjs` | `mcp-journey-branching-realistic.mjs` | US-066 |
| Mobile | `mcp-journey-mobile.mjs` | `mcp-journey-mobile-realistic.mjs` | US-067 |

**Total: 15 test groups covering all 67 user stories**

<!-- section_id: "c4828dc4-708a-4aad-9a5e-a39f54fe4ca4" -->
## When to Use Each Mode

<!-- section_id: "907583f1-2469-485d-8b86-027fca83488b" -->
### Use Direct Mode For:
- Daily development workflow
- Quick regression checks
- CI/CD pipelines (fast feedback)
- API/backend validation
- Pre-commit hooks

<!-- section_id: "fd9e1b75-b595-40e5-b25c-7af47f655cc3" -->
### Use Realistic Mode For:
- Pre-release QA validation
- UX review sessions
- Onboarding validation
- Navigation structure audits
- Monthly comprehensive testing

<!-- section_id: "213df9bf-db80-47f8-9942-8b0ac7eb3046" -->
### Use Both Modes For:
- Complete test suite runs
- Major release validation
- Monthly/quarterly testing cycles
- Comprehensive regression testing

<!-- section_id: "79d9a270-e664-4bfb-a62d-ee6e4180427a" -->
## Understanding Results

<!-- section_id: "95fef6ca-b446-4590-8d1c-9880d37e6cff" -->
### Direct Mode Results
- **Pass**: Feature functionality works correctly
- **Fail**: Core functionality is broken (critical)

<!-- section_id: "ce13c846-3e5c-4c73-8692-bfd5a16a9ed2" -->
### Realistic Mode Results
- **Pass**: Feature is accessible AND works correctly
- **Fail (Functionality)**: Feature is broken (critical)
- **Fail (Navigation)**: Feature works but isn't accessible via UI (UX issue)

<!-- section_id: "32405203-6a16-48f3-ad4f-e658c53afc0b" -->
### Navigation Gap Detection
Realistic tests track navigation gaps in their output:

```json
{
  "navigationGaps": [
    {
      "feature": "Admin Templates",
      "note": "Not accessible via standard UI navigation"
    }
  ]
}
```

<!-- section_id: "7ef1d299-3813-473d-9aea-879000675f40" -->
## Test Execution Times

Based on initial benchmarking:

| Mode | Average Time per Test Group | Total Suite Time (15 groups) |
|------|------------------------------|-------------------------------|
| Direct | 15-25 seconds | ~5 minutes |
| Realistic | 25-40 seconds | ~8 minutes |
| Both | Combined | ~13 minutes |

<!-- section_id: "e5245431-5f73-46f5-9a72-667232412280" -->
## CI/CD Integration

<!-- section_id: "35888d29-16e6-4b9c-ac1c-cb3b7ff20537" -->
### Recommended Strategy

**Fast Feedback (On Every Commit)**
```bash
# Run only direct mode tests for quick validation
python scripts/automation/run_user_stories.py --navigation-mode direct
```

**Comprehensive (Nightly/Weekly)**
```bash
# Run both modes to catch both functionality and UX issues
python scripts/automation/run_user_stories.py --navigation-mode both
```

**Pre-Release (Before Deployment)**
```bash
# Full realistic mode validation
python scripts/automation/run_user_stories.py --navigation-mode realistic --concurrency 1
```

<!-- section_id: "15ff17fe-561f-43f6-ad35-d2516f65672f" -->
## Common Patterns

<!-- section_id: "9846f3e0-0ba1-4909-8f8c-719822ea958c" -->
### Realistic Test Structure
All realistic tests follow this pattern:

```javascript
import {
  switchTab,
  fillField,
  clickButtonWithText,
  clickElement,
  waitForElement,
  navigateFromDashboard,
} from './lib/navigation-helpers.mjs';

// Navigation via UI
await clickElement(client, callTool, 'a[href="/projects"]', 'Projects button');

// Form interaction via UI
await fillField(client, callTool, '#name', 'My Project');
await clickButtonWithText(client, callTool, 'Create Project');
```

<!-- section_id: "6bec97cf-a061-461c-b660-27476ce79f4d" -->
### Direct Test Structure
Direct tests use URL navigation:

```javascript
// Direct URL navigation
await callTool(client, 'browser_navigate', { url: `${BASE}/projects` });

// JS-based interaction
await callTool(client, 'browser_evaluate', {
  function: "() => { /* JS code */ }"
});
```

<!-- section_id: "5281db1d-b31d-4a6b-8d48-0b67fa3835ef" -->
## Troubleshooting

<!-- section_id: "a193afd1-514a-4f08-ac66-b51a9a7fe799" -->
### Test Fails in Realistic Mode but Passes in Direct Mode
This indicates a **navigation gap** - the feature works but isn't accessible via UI. This is a UX issue that should be addressed.

<!-- section_id: "38d2045c-7e37-41c7-815e-abf8f8aa232c" -->
### Test Fails in Both Modes
This indicates a **functionality issue** - the feature is broken and needs immediate attention.

<!-- section_id: "7df8b938-4daa-4127-8586-9948fcc57e51" -->
### Realistic Test Timeout
Realistic tests are slower. Consider:
- Increasing timeout values
- Reducing concurrency
- Checking for UI elements that may not be appearing

<!-- section_id: "35fa4ed7-4ec6-4a3f-ac13-57794c0ecf58" -->
## Navigation Helpers Reference

The `scripts/lib/navigation-helpers.mjs` library provides:

- **`clickElement(selector, description)`** - Click any element by selector
- **`clickButtonWithText(text)`** - Find and click button by text content
- **`clickBreadcrumb(text)`** - Navigate using breadcrumb links
- **`fillField(selector, value)`** - Fill form input field
- **`navigateFromDashboard(section)`** - Navigate from dashboard to section
- **`switchTab(index)`** - Switch between UI tabs
- **`waitForElement(selector, timeout)`** - Wait for element to appear

<!-- section_id: "bb2ae620-afec-4096-b82b-42e47de979e3" -->
## Best Practices

1. **Always run both modes before major releases**
2. **Use direct mode for rapid iteration during development**
3. **Use realistic mode to validate new features are discoverable**
4. **Document navigation gaps found by realistic tests**
5. **Fix navigation gaps as UX improvements**
6. **Keep both test versions in sync when updating tests**

<!-- section_id: "9ea37d65-911b-43b6-9b22-dce9230f7393" -->
## Future Enhancements

Potential improvements to the testing infrastructure:

- [ ] Parallel execution of direct + realistic mode pairs
- [ ] Navigation gap tracking dashboard
- [ ] Automated screenshot comparison between modes
- [ ] Performance benchmarking reports
- [ ] Integration with accessibility testing tools
- [ ] Visual regression testing
- [ ] Mobile viewport testing enhancements

<!-- section_id: "6a90761b-a842-4ea5-b6af-fdbf1be82905" -->
## Related Documentation

- [Realistic vs Direct Navigation Comparison](./REALISTIC_vs_DIRECT_NAVIGATION.md)
- [Complete Automation Coverage](./for_ai/COMPLETE_AUTOMATION_COVERAGE.md)
- [Test Orchestrator Documentation](../scripts/automation/README.md)

---

**Last Updated**: October 2025
**Maintained By**: Automation Team
