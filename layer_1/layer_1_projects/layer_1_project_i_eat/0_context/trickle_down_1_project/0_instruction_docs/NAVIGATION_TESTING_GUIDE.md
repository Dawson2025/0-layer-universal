---
resource_id: "98f5871f-c876-454c-9498-c4f719258bd1"
resource_type: "document"
resource_name: "NAVIGATION_TESTING_GUIDE"
---
# Navigation Testing Guide

<!-- section_id: "b0a026a8-4227-4f5b-8d13-8629a3542fde" -->
## Overview

See also: docs/for_ai/DEPTH_FIRST_SLICE.md for the depth-first slice prototype strategy we follow when expanding or tightening automation checks.

This project now supports **dual-mode testing** for all automation test scripts. Each test can be run in two different navigation modes:

- **Direct Mode** (fast): Uses direct URL navigation for quick validation
- **Realistic Mode** (thorough): Uses only UI buttons/links to simulate real user navigation

<!-- section_id: "11e537d5-5f02-4db6-ae00-be898eb35d08" -->
## Why Two Modes?

<!-- section_id: "906474f0-500f-41ac-a012-48a6d80b776f" -->
### Direct Mode Benefits
- ⚡ **Speed**: 30-50% faster execution
- 🔄 **CI/CD**: Ideal for continuous integration pipelines
- 🎯 **API Focus**: Tests core functionality regardless of UI
- 📊 **Regression**: Quick smoke tests to catch breaking changes

<!-- section_id: "5276994f-7f2e-4341-83dd-d27372d6753f" -->
### Realistic Mode Benefits
- 🔍 **UX Validation**: Ensures features are actually accessible to users
- 🐛 **Navigation Gaps**: Exposes pages only accessible via URL changes
- 👤 **User Experience**: Tests actual user workflows and discoverability
- 📝 **Documentation**: Validates that documentation matches reality

<!-- section_id: "f77de12c-ca34-4cf2-86be-0de4b2a6aacc" -->
## Navigation Gaps Detected

During the creation of realistic tests, we discovered several pages that may not be accessible via standard UI navigation:

- `/admin/templates` - Template administration (onboarding journey)
- `/words/create/table-based` - Table-based word creation (may require alternate path)
- Storage option visibility depends on Firebase availability

**These gaps are now tracked and can be validated with realistic mode tests.**

<!-- section_id: "85fae902-ef9b-4245-8601-71b5c249258a" -->
## Running Tests

<!-- section_id: "9fb0a486-6cb6-45e6-a023-f0b79180d8c9" -->
### Run All Tests (Direct Mode Only)
```bash
python scripts/automation/run_user_stories.py --plan scripts/automation/story_plan.sample.json --navigation-mode direct
```

<!-- section_id: "b2cf69b1-bdc1-433e-a771-be3791cc0679" -->
### Run All Tests (Realistic Mode Only)
```bash
python scripts/automation/run_user_stories.py --plan scripts/automation/story_plan.sample.json --navigation-mode realistic
```

<!-- section_id: "27f8df01-5525-4bf3-9140-61c5d58b20e2" -->
### Run All Tests (Both Modes)
```bash
python scripts/automation/run_user_stories.py --plan scripts/automation/story_plan.sample.json --navigation-mode both
```

<!-- section_id: "c6609512-5392-445b-9425-cedfbc8a4a9e" -->
### Run Specific Test Group
```bash
# Run only authentication tests in both modes
python scripts/automation/run_user_stories.py --plan scripts/automation/story_plan.sample.json --filter "US-001" --navigation-mode both
```

<!-- section_id: "7053edb4-e447-4cb2-bec1-1bbb69fdd870" -->
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

<!-- section_id: "1bef2536-485f-491e-9433-082d7cba978f" -->
## When to Use Each Mode

<!-- section_id: "cba2d9a6-4430-4ec4-89cc-b73547470abc" -->
### Use Direct Mode For:
- Daily development workflow
- Quick regression checks
- CI/CD pipelines (fast feedback)
- API/backend validation
- Pre-commit hooks

<!-- section_id: "33470f26-7c3d-4125-874e-30ff0495dd9e" -->
### Use Realistic Mode For:
- Pre-release QA validation
- UX review sessions
- Onboarding validation
- Navigation structure audits
- Monthly comprehensive testing

<!-- section_id: "2c29e6e6-9493-4a40-b444-3ba298ee3eca" -->
### Use Both Modes For:
- Complete test suite runs
- Major release validation
- Monthly/quarterly testing cycles
- Comprehensive regression testing

<!-- section_id: "cd942a51-3777-4f77-bbff-6a95c3368974" -->
## Understanding Results

<!-- section_id: "1f36634d-2fd0-400f-8b4a-340a435c7845" -->
### Direct Mode Results
- **Pass**: Feature functionality works correctly
- **Fail**: Core functionality is broken (critical)

<!-- section_id: "9e7816a1-0687-45e5-be45-b227526cecad" -->
### Realistic Mode Results
- **Pass**: Feature is accessible AND works correctly
- **Fail (Functionality)**: Feature is broken (critical)
- **Fail (Navigation)**: Feature works but isn't accessible via UI (UX issue)

<!-- section_id: "0956baf2-55b2-4b0f-811b-ee778e9b283f" -->
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

<!-- section_id: "470ea75a-40fb-4d65-bdab-12d428fc0035" -->
## Test Execution Times

Based on initial benchmarking:

| Mode | Average Time per Test Group | Total Suite Time (15 groups) |
|------|------------------------------|-------------------------------|
| Direct | 15-25 seconds | ~5 minutes |
| Realistic | 25-40 seconds | ~8 minutes |
| Both | Combined | ~13 minutes |

<!-- section_id: "4ece4853-d4ed-4092-9293-e5388afb84bc" -->
## CI/CD Integration

<!-- section_id: "e52c8704-35f2-4c50-96c8-db5177d24e82" -->
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

<!-- section_id: "f39645dd-c855-4747-9654-b07994abfb98" -->
## Common Patterns

<!-- section_id: "f248c623-ae73-43fc-98a9-bf30b024d5c5" -->
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

<!-- section_id: "b236185b-8998-4e89-8313-f02cdaa49e23" -->
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

<!-- section_id: "ba4074c0-66d4-42c2-9f75-b0238acfa5a3" -->
## Troubleshooting

<!-- section_id: "5bd7d307-10e3-4fd1-a0a1-6e5f2937f5cb" -->
### Test Fails in Realistic Mode but Passes in Direct Mode
This indicates a **navigation gap** - the feature works but isn't accessible via UI. This is a UX issue that should be addressed.

<!-- section_id: "48e5ebd7-8df9-4633-a83b-e2494c040b29" -->
### Test Fails in Both Modes
This indicates a **functionality issue** - the feature is broken and needs immediate attention.

<!-- section_id: "261d81ca-5962-400b-a428-34c233b19922" -->
### Realistic Test Timeout
Realistic tests are slower. Consider:
- Increasing timeout values
- Reducing concurrency
- Checking for UI elements that may not be appearing

<!-- section_id: "a66de6e8-4d53-4648-81f7-a9e4ca51657c" -->
## Navigation Helpers Reference

The `scripts/lib/navigation-helpers.mjs` library provides:

- **`clickElement(selector, description)`** - Click any element by selector
- **`clickButtonWithText(text)`** - Find and click button by text content
- **`clickBreadcrumb(text)`** - Navigate using breadcrumb links
- **`fillField(selector, value)`** - Fill form input field
- **`navigateFromDashboard(section)`** - Navigate from dashboard to section
- **`switchTab(index)`** - Switch between UI tabs
- **`waitForElement(selector, timeout)`** - Wait for element to appear

<!-- section_id: "48e29bea-4040-40da-9408-67af42f7faf7" -->
## Best Practices

1. **Always run both modes before major releases**
2. **Use direct mode for rapid iteration during development**
3. **Use realistic mode to validate new features are discoverable**
4. **Document navigation gaps found by realistic tests**
5. **Fix navigation gaps as UX improvements**
6. **Keep both test versions in sync when updating tests**

<!-- section_id: "85ef7d27-a962-448e-9ca2-b8d566b8e77c" -->
## Future Enhancements

Potential improvements to the testing infrastructure:

- [ ] Parallel execution of direct + realistic mode pairs
- [ ] Navigation gap tracking dashboard
- [ ] Automated screenshot comparison between modes
- [ ] Performance benchmarking reports
- [ ] Integration with accessibility testing tools
- [ ] Visual regression testing
- [ ] Mobile viewport testing enhancements

<!-- section_id: "af0ade4c-48c2-4a2b-b463-4aaad6392d76" -->
## Related Documentation

- [Realistic vs Direct Navigation Comparison](./REALISTIC_vs_DIRECT_NAVIGATION.md)
- [Complete Automation Coverage](./for_ai/COMPLETE_AUTOMATION_COVERAGE.md)
- [Test Orchestrator Documentation](../scripts/automation/README.md)

---

**Last Updated**: October 2025
**Maintained By**: Automation Team
