---
resource_id: "0c2e1a28-11b4-49cd-898c-cbccfc272edf"
resource_type: "document"
resource_name: "NAVIGATION_TESTING_GUIDE"
---
# Navigation Testing Guide

<!-- section_id: "78e0551d-df82-40cb-8c69-2befd85baaeb" -->
## Overview

See also: docs/for_ai/DEPTH_FIRST_SLICE.md for the depth-first slice prototype strategy we follow when expanding or tightening automation checks.

This project now supports **dual-mode testing** for all automation test scripts. Each test can be run in two different navigation modes:

- **Direct Mode** (fast): Uses direct URL navigation for quick validation
- **Realistic Mode** (thorough): Uses only UI buttons/links to simulate real user navigation

<!-- section_id: "a3759f32-8621-4b86-8577-53be3fb107ea" -->
## Why Two Modes?

<!-- section_id: "7abd3e1d-c194-4076-8189-9ca27472cd55" -->
### Direct Mode Benefits
- ⚡ **Speed**: 30-50% faster execution
- 🔄 **CI/CD**: Ideal for continuous integration pipelines
- 🎯 **API Focus**: Tests core functionality regardless of UI
- 📊 **Regression**: Quick smoke tests to catch breaking changes

<!-- section_id: "4e42f92c-74af-4e2a-8784-9f0d80f3aba9" -->
### Realistic Mode Benefits
- 🔍 **UX Validation**: Ensures features are actually accessible to users
- 🐛 **Navigation Gaps**: Exposes pages only accessible via URL changes
- 👤 **User Experience**: Tests actual user workflows and discoverability
- 📝 **Documentation**: Validates that documentation matches reality

<!-- section_id: "1652d9b6-7178-4e40-8a53-63824395821f" -->
## Navigation Gaps Detected

During the creation of realistic tests, we discovered several pages that may not be accessible via standard UI navigation:

- `/admin/templates` - Template administration (onboarding journey)
- `/words/create/table-based` - Table-based word creation (may require alternate path)
- Storage option visibility depends on Firebase availability

**These gaps are now tracked and can be validated with realistic mode tests.**

<!-- section_id: "e85214ce-a84b-4620-8eeb-9d5d669f9016" -->
## Running Tests

<!-- section_id: "08b42600-70bc-4344-9a62-756cc306399f" -->
### Run All Tests (Direct Mode Only)
```bash
python scripts/automation/run_user_stories.py --plan scripts/automation/story_plan.sample.json --navigation-mode direct
```

<!-- section_id: "06ccaee3-1d10-4bfa-b438-38e8fa1f4330" -->
### Run All Tests (Realistic Mode Only)
```bash
python scripts/automation/run_user_stories.py --plan scripts/automation/story_plan.sample.json --navigation-mode realistic
```

<!-- section_id: "215a9421-1c26-468e-86b8-c27cb85ce51e" -->
### Run All Tests (Both Modes)
```bash
python scripts/automation/run_user_stories.py --plan scripts/automation/story_plan.sample.json --navigation-mode both
```

<!-- section_id: "304bb0a8-7ec7-4fd6-9525-0255aefae42f" -->
### Run Specific Test Group
```bash
# Run only authentication tests in both modes
python scripts/automation/run_user_stories.py --plan scripts/automation/story_plan.sample.json --filter "US-001" --navigation-mode both
```

<!-- section_id: "3afb8e01-1990-47ae-b181-170e74c27f69" -->
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

<!-- section_id: "76fcb743-2a86-4026-a398-f6b64f931535" -->
## When to Use Each Mode

<!-- section_id: "fc4053a8-82af-496a-a398-d4554cc204a2" -->
### Use Direct Mode For:
- Daily development workflow
- Quick regression checks
- CI/CD pipelines (fast feedback)
- API/backend validation
- Pre-commit hooks

<!-- section_id: "06cc1705-5b6a-4d3f-a833-881f8b263162" -->
### Use Realistic Mode For:
- Pre-release QA validation
- UX review sessions
- Onboarding validation
- Navigation structure audits
- Monthly comprehensive testing

<!-- section_id: "c32ecdd1-e5b3-45e9-8b23-3c2f2f752585" -->
### Use Both Modes For:
- Complete test suite runs
- Major release validation
- Monthly/quarterly testing cycles
- Comprehensive regression testing

<!-- section_id: "50509f25-96a5-4b1b-9c9e-a755753636fd" -->
## Understanding Results

<!-- section_id: "20c2387c-b782-43ce-a406-c30da7a20057" -->
### Direct Mode Results
- **Pass**: Feature functionality works correctly
- **Fail**: Core functionality is broken (critical)

<!-- section_id: "6b822786-9fb2-4854-b887-3d9c6cc80aff" -->
### Realistic Mode Results
- **Pass**: Feature is accessible AND works correctly
- **Fail (Functionality)**: Feature is broken (critical)
- **Fail (Navigation)**: Feature works but isn't accessible via UI (UX issue)

<!-- section_id: "9224c5b8-9dc8-4a61-8a08-a049119c580f" -->
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

<!-- section_id: "a38e0a13-4c3b-4e68-b11d-a635222c0475" -->
## Test Execution Times

Based on initial benchmarking:

| Mode | Average Time per Test Group | Total Suite Time (15 groups) |
|------|------------------------------|-------------------------------|
| Direct | 15-25 seconds | ~5 minutes |
| Realistic | 25-40 seconds | ~8 minutes |
| Both | Combined | ~13 minutes |

<!-- section_id: "403e2058-63bb-428a-b408-7ef151f99b7e" -->
## CI/CD Integration

<!-- section_id: "a7489f7c-2d3b-4537-a640-7352aa121e61" -->
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

<!-- section_id: "44b3bd47-3b22-486a-b26f-9ec7a55180ca" -->
## Common Patterns

<!-- section_id: "08239dac-678e-48f6-9b05-598d3a3555a0" -->
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

<!-- section_id: "1c4c02ed-ac06-4c99-a2bb-6a49238cc291" -->
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

<!-- section_id: "e6944d7d-99cd-4b55-b37f-9ff04bbdf399" -->
## Troubleshooting

<!-- section_id: "f7c0cce9-fd20-46c5-9cfe-90de6aade908" -->
### Test Fails in Realistic Mode but Passes in Direct Mode
This indicates a **navigation gap** - the feature works but isn't accessible via UI. This is a UX issue that should be addressed.

<!-- section_id: "3921c471-a7a5-4635-a18e-b64e4d0d935f" -->
### Test Fails in Both Modes
This indicates a **functionality issue** - the feature is broken and needs immediate attention.

<!-- section_id: "e5732739-031b-4ed4-a0ef-51a61ed3922a" -->
### Realistic Test Timeout
Realistic tests are slower. Consider:
- Increasing timeout values
- Reducing concurrency
- Checking for UI elements that may not be appearing

<!-- section_id: "18efc5db-a506-4340-bb9f-e52bd6d93943" -->
## Navigation Helpers Reference

The `scripts/lib/navigation-helpers.mjs` library provides:

- **`clickElement(selector, description)`** - Click any element by selector
- **`clickButtonWithText(text)`** - Find and click button by text content
- **`clickBreadcrumb(text)`** - Navigate using breadcrumb links
- **`fillField(selector, value)`** - Fill form input field
- **`navigateFromDashboard(section)`** - Navigate from dashboard to section
- **`switchTab(index)`** - Switch between UI tabs
- **`waitForElement(selector, timeout)`** - Wait for element to appear

<!-- section_id: "55cb189a-85a6-4c1d-baad-620d5d63846c" -->
## Best Practices

1. **Always run both modes before major releases**
2. **Use direct mode for rapid iteration during development**
3. **Use realistic mode to validate new features are discoverable**
4. **Document navigation gaps found by realistic tests**
5. **Fix navigation gaps as UX improvements**
6. **Keep both test versions in sync when updating tests**

<!-- section_id: "5570bbb5-a5d6-4486-911d-109be5f4567d" -->
## Future Enhancements

Potential improvements to the testing infrastructure:

- [ ] Parallel execution of direct + realistic mode pairs
- [ ] Navigation gap tracking dashboard
- [ ] Automated screenshot comparison between modes
- [ ] Performance benchmarking reports
- [ ] Integration with accessibility testing tools
- [ ] Visual regression testing
- [ ] Mobile viewport testing enhancements

<!-- section_id: "e966755e-8b17-4a54-8154-e146623f600c" -->
## Related Documentation

- [Realistic vs Direct Navigation Comparison](./REALISTIC_vs_DIRECT_NAVIGATION.md)
- [Complete Automation Coverage](./for_ai/COMPLETE_AUTOMATION_COVERAGE.md)
- [Test Orchestrator Documentation](../scripts/automation/README.md)

---

**Last Updated**: October 2025
**Maintained By**: Automation Team
