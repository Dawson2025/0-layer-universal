#!/bin/bash
# resource_id: "32a9ffe8-7ea8-4627-b547-3ad577049b7d"
# resource_type: "script"
# resource_name: "on-stage-enter.sync-conflict-20260126-035816-IF2WOGZ"
# Hook script: Called when entering this stage
# Customize as needed

STAGE_DIR="$(dirname "$(dirname "$0")")"
echo "Entering 10_current_product stage"

# Add custom initialization here
