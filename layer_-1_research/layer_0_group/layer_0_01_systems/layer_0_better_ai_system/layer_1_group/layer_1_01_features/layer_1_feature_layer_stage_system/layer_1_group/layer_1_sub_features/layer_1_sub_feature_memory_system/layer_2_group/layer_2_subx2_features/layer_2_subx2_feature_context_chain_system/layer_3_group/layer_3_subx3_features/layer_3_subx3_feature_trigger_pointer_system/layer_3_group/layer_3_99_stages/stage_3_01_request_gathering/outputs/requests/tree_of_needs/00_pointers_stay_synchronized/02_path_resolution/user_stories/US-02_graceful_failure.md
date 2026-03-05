---
resource_id: "bd8a6253-6fb3-49e5-92ec-1d8162e57db1"
resource_type: "output"
resource_name: "US-02_graceful_failure"
---
# US-02: Graceful Failure When Entity Not Found

<!-- section_id: "b0db44c9-5ed7-4267-bfeb-973752861f4a" -->
## User Story

As a developer running pointer-sync.sh,
I want the system to report broken pointers clearly without crashing,
so that I can identify and fix problems one at a time.

<!-- section_id: "6adb424a-39f9-46ff-b972-b011da276c11" -->
## Acceptance Criteria

1. When a `canonical_entity` doesn't match any directory, the pointer is reported as BROKEN with the entity name in the error message
2. When a `canonical_stage` doesn't exist within the resolved entity, the pointer is reported as BROKEN
3. When a `canonical_subpath` doesn't exist, the pointer is reported as BROKEN
4. Broken pointers do not prevent other valid pointers from being processed
5. The summary at the end shows correct counts of broken vs. valid pointers
6. `--validate` exits with code 1 if ANY pointer is broken or stale

<!-- section_id: "76497a47-a814-4573-9e16-030266cfd68b" -->
## Test Coverage

- Tests 3.2 (unknown entity), 3.4 (invalid stage), 3.6 (invalid subpath) validate graceful failure
- Test 7.4 (mixed valid/broken) validates that broken pointers don't block processing of valid ones
