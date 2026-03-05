---
resource_id: "6c930f39-be8d-409e-a4ef-b402e0fd543c"
resource_type: "document"
resource_name: "NAVIGATION_TESTING_GUIDE"
---
# Navigation Testing Guide

<!-- section_id: "6b3d2ce7-f4a6-492d-88d2-5d31d738bab6" -->
## Overview

See also: docs/for_ai/DEPTH_FIRST_SLICE.md for the depth-first slice prototype strategy we follow when expanding or tightening automation checks.

This project now supports **dual-mode testing** for all automation test scripts. Each test can be run in two different navigation modes:

- **Direct Mode** (fast): Uses direct URL navigation for quick validation
- **Realistic Mode** (thorough): Uses only UI buttons/links to simulate real user navigation

<!-- section_id: "89e26b60-1d0b-4321-af60-be760887e46b" -->
## Why Two Modes?

<!-- section_id: "f1db15f7-1c10-4e7b-a7b3-58d1aa010468" -->
### Direct Mode Benefits
- ⚡ **Speed**: 30-50% faster execution
- 🔄 **CI/CD**: Ideal for continuous integration pipelines
- 🎯 **API Focus**: Tests core functionality regardless of UI
- 📊 **Regression**: Quick smoke tests to catch breaking changes

<!-- section_id: "a7eb57e5-d751-44c8-867a-d548a4f4ebb3" -->
### Realistic Mode Benefits
- 🔍 **UX Validation**: Ensures features are actually accessible to users
- 🐛 **Navigation Gaps**: Exposes pages only accessible via URL changes
- 👤 **User Experience**: Tests actual user workflows and discoverability
- 📝 **Documentation**: Validates that documentation matches reality

<!-- section_id: "35fc64b9-3c2f-4495-907a-2b132ed5b0de" -->
## Navigation Gaps Detected

During the creation of realistic tests, we discovered several pages that may not be accessible via standard UI navigation:

- `/admin/templates` - Template administration (onboarding journey)
- `/words/create/table-based` - Table-based word creation (may require alternate path)
- Storage option visibility depends on Firebase availability

**These gaps are now tracked and can be validated with realistic mode tests.**

<!-- section_id: "190faf42-8b18-478a-9a45-be033c4a98c5" -->
## Running Tests

<!-- section_id: "7dfcd020-c251-4823-8336-120c68501138" -->
### Run All Tests (Direct Mode Only)
```bash
python scripts/automation/run_user_stories.py --plan scripts/automation/story_plan.sample.json --navigation-mode direct
```

<!-- section_id: "598aa4af-f552-48f7-b44b-84eaf3d24108" -->
### Run All Tests (Realistic Mode Only)
```bash
python scripts/automation/run_user_stories.py --plan scripts/automation/story_plan.sample.json --navigation-mode realistic
```

<!-- section_id: "4285f122-d97e-4ced-8c31-059088bbdf92" -->
### Run All Tests (Both Modes)
```bash
python scripts/automation/run_user_stories.py --plan scripts/automation/story_plan.sample.json --navigation-mode both
```

<!-- section_id: "851de343-9c6f-422f-b9fa-7b08796049c3" -->
### Run Specific Test Group
```bash
# Run only authentication tests in both modes
python scripts/automation/run_user_stories.py --plan scripts/automation/story_plan.sample.json --filter "US-001" --navigation-mode both
```

<!-- section_id: "1db97e74-a774-49bb-b80a-7a1d6e282dfc" -->
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

<!-- section_id: "ba07ef9e-86aa-4ebe-b3e6-240350105392" -->
## When to Use Each Mode

<!-- section_id: "8e9fca27-de0e-4b9a-b3ad-e182102b7026" -->
### Use Direct Mode For:
- Daily development workflow
- Quick regression checks
- CI/CD pipelines (fast feedback)
- API/backend validation
- Pre-commit hooks

<!-- section_id: "92daf793-8d74-4eca-a6a9-343decaab8dd" -->
### Use Realistic Mode For:
- Pre-release QA validation
- UX review sessions
- Onboarding validation
- Navigation structure audits
- Monthly comprehensive testing

<!-- section_id: "cfef0568-ba07-4d9b-b90a-cc2dd2a7bdb2" -->
### Use Both Modes For:
- Complete test suite runs
- Major release validation
- Monthly/quarterly testing cycles
- Comprehensive regression testing

<!-- section_id: "03868ee8-ec4d-42bc-88b5-6006477ae175" -->
## Understanding Results

<!-- section_id: "9eeb4eff-736f-4d27-aba1-f70944bdc523" -->
### Direct Mode Results
- **Pass**: Feature functionality works correctly
- **Fail**: Core functionality is broken (critical)

<!-- section_id: "df7af93d-0341-411b-b719-ea5f0b00e2fa" -->
### Realistic Mode Results
- **Pass**: Feature is accessible AND works correctly
- **Fail (Functionality)**: Feature is broken (critical)
- **Fail (Navigation)**: Feature works but isn't accessible via UI (UX issue)

<!-- section_id: "3401ab09-230e-4df5-b666-9c760daac609" -->
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

<!-- section_id: "f59dbf33-b627-4ade-97d4-78b0f838525c" -->
## Test Execution Times

Based on initial benchmarking:

| Mode | Average Time per Test Group | Total Suite Time (15 groups) |
|------|------------------------------|-------------------------------|
| Direct | 15-25 seconds | ~5 minutes |
| Realistic | 25-40 seconds | ~8 minutes |
| Both | Combined | ~13 minutes |

<!-- section_id: "6f70e528-298a-4d76-96cc-29b98b3bfabb" -->
## CI/CD Integration

<!-- section_id: "c52026d8-235e-4dcf-9062-bf2ff98bb467" -->
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

<!-- section_id: "57670252-6f26-4d67-855b-7fc499d1ef19" -->
## Common Patterns

<!-- section_id: "011190a5-d81d-438f-8ae1-98d4d0cb288f" -->
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

<!-- section_id: "903deeec-a9df-4b67-b071-9abbd9dbedb9" -->
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

<!-- section_id: "0d2114c1-6a29-45bf-bb8d-b7ac4ad76e84" -->
## Troubleshooting

<!-- section_id: "28c559ae-7933-4154-8f34-c4750bd84d88" -->
### Test Fails in Realistic Mode but Passes in Direct Mode
This indicates a **navigation gap** - the feature works but isn't accessible via UI. This is a UX issue that should be addressed.

<!-- section_id: "d92ba564-bd0e-4ead-a796-7028be9fa40d" -->
### Test Fails in Both Modes
This indicates a **functionality issue** - the feature is broken and needs immediate attention.

<!-- section_id: "45589db2-4d18-44e4-b678-5214ae993320" -->
### Realistic Test Timeout
Realistic tests are slower. Consider:
- Increasing timeout values
- Reducing concurrency
- Checking for UI elements that may not be appearing

<!-- section_id: "a202a516-dda6-407f-875f-19511b68f424" -->
## Navigation Helpers Reference

The `scripts/lib/navigation-helpers.mjs` library provides:

- **`clickElement(selector, description)`** - Click any element by selector
- **`clickButtonWithText(text)`** - Find and click button by text content
- **`clickBreadcrumb(text)`** - Navigate using breadcrumb links
- **`fillField(selector, value)`** - Fill form input field
- **`navigateFromDashboard(section)`** - Navigate from dashboard to section
- **`switchTab(index)`** - Switch between UI tabs
- **`waitForElement(selector, timeout)`** - Wait for element to appear

<!-- section_id: "a4c6dc18-ce2a-4753-88f4-7e34d73eb7f6" -->
## Best Practices

1. **Always run both modes before major releases**
2. **Use direct mode for rapid iteration during development**
3. **Use realistic mode to validate new features are discoverable**
4. **Document navigation gaps found by realistic tests**
5. **Fix navigation gaps as UX improvements**
6. **Keep both test versions in sync when updating tests**

<!-- section_id: "999e5b99-9fd1-418e-868f-85e0a44c9aa3" -->
## Future Enhancements

Potential improvements to the testing infrastructure:

- [ ] Parallel execution of direct + realistic mode pairs
- [ ] Navigation gap tracking dashboard
- [ ] Automated screenshot comparison between modes
- [ ] Performance benchmarking reports
- [ ] Integration with accessibility testing tools
- [ ] Visual regression testing
- [ ] Mobile viewport testing enhancements

<!-- section_id: "34adc550-af85-449e-95a3-ca54a7306fdc" -->
## Related Documentation

- [Realistic vs Direct Navigation Comparison](./REALISTIC_vs_DIRECT_NAVIGATION.md)
- [Complete Automation Coverage](./for_ai/COMPLETE_AUTOMATION_COVERAGE.md)
- [Test Orchestrator Documentation](../scripts/automation/README.md)

---

**Last Updated**: October 2025
**Maintained By**: Automation Team
