---
resource_id: "0d1e2f3a-4b5c-4d6e-7f8a-9b0c1d2e3f4a"
resource_type: "output"
resource_name: "REQ-01_resolve_uuid_function"
---
# REQ-01: resolve-uuid Shell Function

**Need**: [UUID-Based Reference Resolution](../README.md)

<!-- section_id: "1e2f3a4b-5c6d-4e7f-8a9b-0c1d2e3f4a5b" -->
## Requirements

- **MUST** accept a UUID string (full or short prefix) and return the current absolute filesystem path
- **MUST** resolve from `.uuid-index.json` at the repository root (found via `git rev-parse --show-toplevel`)
- **MUST** return exit code 0 on success, 1 on not-found, 2 on index-missing
- **MUST** print error to stderr on failure (never to stdout, which carries the path)
- **MUST** complete resolution in <10ms including index load
- **MUST** work within sandboxed environments (no network, no elevated permissions — only reads a local JSON file)
- **MUST** support short UUID prefixes (e.g., `08a4e9bc` matches `08a4e9bc-8cc1-457e-b966-0a912ae6dff7`) like git does with commit SHAs
- **SHOULD** be usable as a subshell expansion: `bash "$(resolve-uuid 08a4e9bc)"`
- **SHOULD** be distributable as both a standalone script and a sourceable function
- **MUST NOT** require any dependencies beyond `jq` and standard shell utilities
- **MUST NOT** hardcode any path except the index location relative to repo root (`.uuid-index.json`)
