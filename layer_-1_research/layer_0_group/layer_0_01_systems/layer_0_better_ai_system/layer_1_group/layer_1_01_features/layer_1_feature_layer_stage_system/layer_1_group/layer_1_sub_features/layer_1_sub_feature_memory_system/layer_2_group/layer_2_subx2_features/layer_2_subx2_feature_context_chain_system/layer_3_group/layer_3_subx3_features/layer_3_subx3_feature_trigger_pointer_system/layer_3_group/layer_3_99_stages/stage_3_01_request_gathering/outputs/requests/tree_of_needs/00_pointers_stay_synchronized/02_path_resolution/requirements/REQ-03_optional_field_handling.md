---
resource_id: "fed11c45-e293-449f-97b6-f1a037094292"
resource_type: "output"
resource_name: "REQ-03_optional_field_handling"
---
# REQ-03: Optional Field Handling

## Requirement

The pointer sync system MUST handle missing optional frontmatter fields gracefully, without crashing.

## Specification

- `canonical_stage` is optional — if absent, resolution stops at the entity directory
- `canonical_subpath` is optional — if absent, resolution stops at the entity or stage directory
- `canonical_entity` is required — if absent, the pointer is SKIP'd (not processed)
- `pointer_to` is required — if empty, the pointer is SKIP'd
- The `extract_fm` function must return an empty string for missing fields instead of causing a pipeline failure

## Bug Found During Testing

The original `extract_fm` function used a pipeline with `grep "^${field}:"`. With `set -euo pipefail`, when the field was absent, `grep` returned exit code 1, which propagated through `pipefail` and caused the entire script to exit silently.

**Fix applied**: Added `|| true` to the pipeline in `extract_fm` so missing fields return empty string instead of crashing.

## Test Coverage

- Test 2.4 validates that missing `canonical_stage` still resolves the entity
- Test 7.2 validates that missing `canonical_entity` results in SKIP
- Test 7.3 validates that empty `pointer_to` results in SKIP
