---
resource_id: "8988aca1-76ee-4922-a9bd-7e1c8285281c"
resource_type: "output"
resource_name: "REQ-03_windows_line_endings"
---
# REQ-03: Windows Line Ending Compatibility

## Requirement

The pointer sync system MUST handle files with Windows line endings (`\r\n`) correctly.

## Specification

- `has_pointer_fm()` must strip `\r` when checking the first line for `---`
- `extract_fm()` must strip `\r` from field values
- `grep` searches for frontmatter must work regardless of line ending style
- Updated pointer files should preserve the original line ending style (currently writes Unix-style `\n`)

## Rationale

In a cross-platform team (or when files are edited on Windows), `.md` files may have `\r\n` line endings. The sync script must not break on these files.

## Test Coverage

- Test 1.5 validates that Windows line ending files are detected as pointer files
- The script uses `tr -d '\r'` in both `has_pointer_fm` and `extract_fm` to strip carriage returns

## Known Limitation

The awk-based update mechanism writes Unix-style line endings. If the original file had `\r\n`, the updated line will have `\n` while the rest of the file retains `\r\n`. This is acceptable for most workflows but could be improved.
