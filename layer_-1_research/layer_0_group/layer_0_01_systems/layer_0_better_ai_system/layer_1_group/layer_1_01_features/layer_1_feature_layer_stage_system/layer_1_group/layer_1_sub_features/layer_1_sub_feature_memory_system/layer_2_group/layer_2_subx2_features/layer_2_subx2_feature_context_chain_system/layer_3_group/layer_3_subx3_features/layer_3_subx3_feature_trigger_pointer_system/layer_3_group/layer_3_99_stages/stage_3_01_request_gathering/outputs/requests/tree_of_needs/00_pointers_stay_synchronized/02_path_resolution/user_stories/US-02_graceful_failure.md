# US-02: Graceful Failure When Entity Not Found

## User Story

As a developer running pointer-sync.sh,
I want the system to report broken pointers clearly without crashing,
so that I can identify and fix problems one at a time.

## Acceptance Criteria

1. When a `canonical_entity` doesn't match any directory, the pointer is reported as BROKEN with the entity name in the error message
2. When a `canonical_stage` doesn't exist within the resolved entity, the pointer is reported as BROKEN
3. When a `canonical_subpath` doesn't exist, the pointer is reported as BROKEN
4. Broken pointers do not prevent other valid pointers from being processed
5. The summary at the end shows correct counts of broken vs. valid pointers
6. `--validate` exits with code 1 if ANY pointer is broken or stale

## Test Coverage

- Tests 3.2 (unknown entity), 3.4 (invalid stage), 3.6 (invalid subpath) validate graceful failure
- Test 7.4 (mixed valid/broken) validates that broken pointers don't block processing of valid ones
