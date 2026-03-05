#!/bin/bash
# resource_id: "eb4f165b-b5ed-498c-9c3b-bd05e6688676"
# resource_type: "script"
# resource_name: "on-stage-enter.sync-conflict-20260126-035813-IF2WOGZ"
# Hook script: Called when entering this stage
# Customize as needed

STAGE_DIR="$(dirname "$(dirname "$0")")"
echo "Entering 11_archives stage"

# Add custom initialization here
