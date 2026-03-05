---
resource_id: "ed3e1cec-e5da-414a-8a0e-ddb28c541596"
resource_type: "document"
resource_name: "cloud_integration_tests"
---
# Cloud Integration Tests

- **Source Prompt**: `docs/prompts.txt/cloud/making_tests/coudTests.md`
- **Related Implementation**: `tests/integration/test_cloud_integration.py`

<!-- section_id: "9d044bda-fda2-4e26-a879-295b9578f6c3" -->
## Goal
Guarantee that Firebase-backed features remain functional by exercising real Firestore and Storage operations through automated integration tests.

<!-- section_id: "baf57def-45b7-4c8a-a83c-c16741c63b31" -->
## Functional Requirements
- Provide automated tests that create a cloud project and associated words, then verify their presence in Google Firestore.
- Validate that media assets tied to words (e.g., videos or pictures) can be uploaded to and retrieved from Firebase Storage.
- Isolate all integration data under clearly-scoped, temporary identifiers and clean it up after the test run.
- Skip the integration suite safely when Firebase services, credentials, or required SDKs are unavailable.

<!-- section_id: "59380900-4f38-4c27-b501-1051100b74e1" -->
## Acceptance Criteria
- Executing `RUN_FIREBASE_INTEGRATION_TESTS=1 python3 -m unittest tests.integration.test_cloud_integration` runs Firestore and Storage tests that pass (or skip when cloud access is unavailable) without requiring manual steps.
- Firestore test coverage confirms that the created word is retrievable via both project-scoped and direct document lookups.
- Storage test coverage confirms that an uploaded asset can be fetched with matching content and that the blob is removed during cleanup.

<!-- section_id: "2fd83573-b3c0-4a9f-a26d-686c677f6ef2" -->
## Notes
- Tests must avoid mutating production projects; they should target the development environment by default and annotate test artifacts with an `integration-tests` prefix.
- Future cloud features should add corresponding cases to `tests/integration/test_cloud_integration.py` to preserve comprehensive coverage.
- Set the `RUN_FIREBASE_INTEGRATION_TESTS=1` environment variable to opt in to these cloud-touching tests; they remain skipped by default to keep offline development flows fast and safe.
