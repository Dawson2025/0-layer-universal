#!/bin/bash
# resource_id: "466bf580-be77-4759-806b-50f6d066f39d"
# resource_type: "script"
# resource_name: "on-stage-enter.sync-conflict-20260126-035814-IF2WOGZ"
# Hook script: Called when entering this stage
# Customize as needed

STAGE_DIR="$(dirname "$(dirname "$0")")"
echo "Entering 01_request_gathering stage"

# Add custom initialization here
