# Request Gathering Stage Scripts

Utility scripts for the request_gathering stage.

## Available Scripts

### validate_requests.sh
Validates that all requests have complete documentation.

```bash
#!/bin/bash
# Validates request folder completeness

REQUESTS_DIR="outputs/requests"
ERRORS=0

for dir in "$REQUESTS_DIR"/request_*/; do
  name=$(basename "$dir")

  for file in request.md requirements.md specs.md; do
    if [[ ! -f "$dir/$file" ]]; then
      echo "MISSING: $name/$file"
      ((ERRORS++))
    fi
  done
done

if [[ $ERRORS -eq 0 ]]; then
  echo "All requests complete"
else
  echo "Found $ERRORS missing files"
  exit 1
fi
```

### count_requirements.sh
Counts requirements across all request files.

```bash
#!/bin/bash
# Counts requirements in all requests

FUNCTIONAL=$(grep -r "^### REQ-.*-F" outputs/requests/*/requirements.md | wc -l)
NONFUNCTIONAL=$(grep -r "^### REQ-.*-NF" outputs/requests/*/requirements.md | wc -l)

echo "Functional Requirements: $FUNCTIONAL"
echo "Non-Functional Requirements: $NONFUNCTIONAL"
echo "Total: $((FUNCTIONAL + NONFUNCTIONAL))"
```

## Usage

Scripts can be:
1. Called directly via Bash tool
2. Invoked from hooks
3. Run as part of validation workflows

## Adding New Scripts

1. Create script in this directory
2. Make executable: `chmod +x script.sh`
3. Document in this README
4. Optionally add to hooks.json for automatic execution
