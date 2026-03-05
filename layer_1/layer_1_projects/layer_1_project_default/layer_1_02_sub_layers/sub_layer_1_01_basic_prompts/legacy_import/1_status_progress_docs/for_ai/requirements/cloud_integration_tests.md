---
resource_id: "051e29fc-5347-42c6-879f-4279d084336f"
resource_type: "document"
resource_name: "cloud_integration_tests"
---
# Cloud Integration Tests

- **Source Prompt**: `docs/prompts.txt/cloud/making_tests/coudTests.md`
- **Related Implementation**: `tests/integration/test_cloud_integration.py`

<!-- section_id: "157d4fbe-c91b-40c8-8f38-da84d5915d6f" -->
## Goal
Guarantee that Firebase-backed features remain functional by exercising real Firestore and Storage operations through automated integration tests.

<!-- section_id: "652d5ad0-ada3-4da8-9248-ef643dd6a6e5" -->
## Functional Requirements
- Provide automated tests that create a cloud project and associated words, then verify their presence in Google Firestore.
- Validate that media assets tied to words (e.g., videos or pictures) can be uploaded to and retrieved from Firebase Storage.
- Isolate all integration data under clearly-scoped, temporary identifiers and clean it up after the test run.
- Skip the integration suite safely when Firebase services, credentials, or required SDKs are unavailable.

<!-- section_id: "941dfafd-204e-47ee-bfc1-fffd413c6220" -->
## Acceptance Criteria
- Executing `RUN_FIREBASE_INTEGRATION_TESTS=1 python3 -m unittest tests.integration.test_cloud_integration` runs Firestore and Storage tests that pass (or skip when cloud access is unavailable) without requiring manual steps.
- Firestore test coverage confirms that the created word is retrievable via both project-scoped and direct document lookups.
- Storage test coverage confirms that an uploaded asset can be fetched with matching content and that the blob is removed during cleanup.

<!-- section_id: "36971926-3c00-48e6-b914-1b837f3b95f7" -->
## Notes
- Tests must avoid mutating production projects; they should target the development environment by default and annotate test artifacts with an `integration-tests` prefix.
- Future cloud features should add corresponding cases to `tests/integration/test_cloud_integration.py` to preserve comprehensive coverage.
- Set the `RUN_FIREBASE_INTEGRATION_TESTS=1` environment variable to opt in to these cloud-touching tests; they remain skipped by default to keep offline development flows fast and safe.
